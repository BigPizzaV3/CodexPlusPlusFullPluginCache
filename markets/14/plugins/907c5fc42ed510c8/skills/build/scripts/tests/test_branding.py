"""B005 retained-branding regression checks for packaged branding and release consistency."""
import copy
import hashlib
import json
import struct
import unittest
import zlib
from pathlib import Path
from branding_check import PNG, ICON_FIELDS, ICON_PATHS, png_info, validate_branding_contract
from check_package import ROOT, AUTO, payload, read_json, validate
from iteration import BUILD, __version__


def chunk(kind, data):
    return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)


def make_png(w=48,h=48,depth=8,colour=2,rows=None,interlace=0):
    if rows is None:rows=(b'\0'+b'\x17\x47\xad'*w)*h
    return PNG+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,depth,colour,0,0,interlace))+chunk(b'IDAT',zlib.compress(rows))+chunk(b'IEND',b'')


class BrandingTests(unittest.TestCase):
    def setUp(self):
        self.m=read_json(ROOT/'.codex-plugin/plugin.json')

    def test_all_display_surfaces_use_approved_icon(self):
        info=validate_branding_contract(ROOT,self.m)
        self.assertEqual(set(info['fields']),set(ICON_FIELDS))
        self.assertEqual(info['host_rendering'],'not_tested')
        self.assertFalse(info['automatic_account_update_claimed'])
        for field, item in info['fields'].items():
            self.assertEqual((item['width'],item['height']),(1254,1254))
            self.assertEqual(item['path'],ICON_PATHS[field])

    def test_full_wordmark_not_the_listing_icon(self):
        for field in ICON_FIELDS:
            self.assertNotIn('wordmark',self.m['interface'][field])
        self.assertTrue((ROOT/'assets/build-wordmark.png').is_file())

    def test_missing_dark_variant_is_rejected(self):
        for field in ('logoDark','composerIconDark'):
            m=copy.deepcopy(self.m);del m['interface'][field]
            with self.assertRaises(ValueError):validate_branding_contract(ROOT,m)

    def test_unsafe_or_old_asset_references_rejected(self):
        for ref in ('https://example.com/icon.png','../icon.png','./assets/icon.svg','./assets/build-icon-b004.png'):
            m=copy.deepcopy(self.m);m['interface']['logo']=ref
            with self.assertRaises(ValueError):validate_branding_contract(ROOT,m)

    def test_real_files_pass_structure_and_decompression(self):
        for p in (ROOT/'assets').glob('*.png'):
            self.assertEqual(png_info(p.read_bytes())['structure_crc_and_decompression'],'passed')

    def test_approved_asset_hashes_match(self):
        record=read_json(AUTO/'BR24.json')
        self.assertEqual(record['build'],BUILD)
        current=read_json(AUTO/'AB60.json')['file_sha256']
        for rel,item in record['assets'].items():
            p=ROOT/rel
            checksum=hashlib.sha256(p.read_bytes()).hexdigest()
            self.assertEqual(checksum,current[rel])
            if 'wordmark' in rel:  # unchanged historical reference artwork
                self.assertEqual(checksum,item['sha256'])
                self.assertEqual(p.stat().st_size,item['bytes'])

    def test_release_identity_consistent(self):
        self.assertEqual((BUILD,__version__),('B005','0.5.0'))
        for name in ('AB60.json','BR24.json','EB25.json','VT83.json'):
            r=read_json(AUTO/name)
            expected_build,expected_version = ('B005','0.5.0') if name=='BR24.json' else ('B007','0.7.0')
            self.assertEqual(r['build'],expected_build,name)
            self.assertEqual(r['version'],expected_version,name)
        self.assertEqual(self.m['version'],'0.8.6')

    def test_integrity_inventory_never_indexes_runtime_reports(self):
        inv=read_json(AUTO/'AB60.json')['file_sha256']
        self.assertFalse(any('logreport' in p.casefold() or '__pycache__' in p or p.endswith('.pyc') for p in inv))
        actual={rel:hashlib.sha256(p.read_bytes()).hexdigest() for rel,p in payload(ROOT) if rel!='skills/build/Automation/AB60.json'}
        self.assertEqual(inv,actual)

    def test_b003_failures_are_not_presented_as_a_host_diagnosis(self):
        r=read_json(AUTO/'BR24.json')
        self.assertFalse(r['host_update_performed'])
        self.assertFalse(r['stored_listing_metadata_inspected'])
        self.assertIn('undetermined',r['cause_of_book_icon'])

    def test_release_recorded_production_bytes_match(self):
        r=read_json(AUTO/'AB60.json')
        self.assertEqual(r['baseline'],'Build_ B006')
        self.assertEqual(len(r['production_files_sha256']),15)
        for rel,h in r['production_files_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),h,rel)

    def test_crc_damage_rejected(self):
        raw=bytearray(make_png());raw[-1]^=1
        with self.assertRaises(ValueError):png_info(bytes(raw))

    def test_non_square_and_small_images_rejected(self):
        for w,h in ((47,47),(48,49),(4097,4097)):
            with self.assertRaises(ValueError):png_info(make_png(w,h,rows=b'\0'))

    def test_truncation_and_trailing_content_rejected(self):
        for raw in (make_png()[:-2],make_png()+b'extra',b'\x89PNG\r\n\x1a\n',b'not PNG'):
            with self.assertRaises(ValueError):png_info(raw)

    def test_bad_scanline_size_rejected(self):
        for rows in (b'\0',b'\0'*100000):
            with self.assertRaises(ValueError):png_info(make_png(rows=rows))

    def test_invalid_row_filter_rejected(self):
        with self.assertRaises(ValueError):png_info(make_png(rows=(b'\x05'+b'\0'*144)*48))

    def test_unknown_critical_chunk_rejected(self):
        raw=make_png();offset=8+25
        with self.assertRaises(ValueError):png_info(raw[:offset]+chunk(b'ABCD',b'')+raw[offset:])

    def test_valid_minimum_rgb_is_accepted(self):
        self.assertEqual(png_info(make_png())['width'],48)

    def test_unsupported_export_mode_rejected(self):
        for kwargs in ({'depth':16},{'colour':3},{'interlace':1}):
            with self.assertRaises(ValueError):png_info(make_png(**kwargs))

    def test_too_large_input_rejected(self):
        with self.assertRaises(ValueError):png_info(make_png()+b'0'*(5*1024*1024))

    def test_documented_example_style_asset_paths(self):
        self.assertEqual(ICON_PATHS, {
            'composerIcon':'./assets/icon.png', 'composerIconDark':'./assets/icon-dark.png',
            'logo':'./assets/logo.png', 'logoDark':'./assets/logo-dark.png'})
        self.assertEqual(len(set(ICON_PATHS.values())), 4)

    def test_variants_keep_approved_art_without_redesign(self):
        r=read_json(AUTO/'BR24.json')
        self.assertTrue(r['controlled_retry']['approved_icon_bytes_preserved'])
        current=read_json(AUTO/'AB60.json')['public_submission']['immutable_user_export_files_sha256']
        for path in ICON_PATHS.values():
            rel=path.removeprefix('./')
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),current[rel])

    def test_zip_round_trip_resolves_each_icon_from_plugin_root(self):
        import io, zipfile
        data=io.BytesIO()
        with zipfile.ZipFile(data,'w',zipfile.ZIP_DEFLATED) as z:
            for rel,p in payload(ROOT): z.writestr(rel,p.read_bytes())
        data.seek(0)
        with zipfile.ZipFile(data) as z:
            self.assertIsNone(z.testzip())
            m=json.loads(z.read('.codex-plugin/plugin.json'))
            for field in ICON_FIELDS:
                name=m['interface'][field].removeprefix('./')
                raw=z.read(name)
                self.assertEqual(png_info(raw)['width'],1254)
                self.assertEqual(raw,(ROOT/name).read_bytes())

    def test_controlled_retry_is_not_presented_as_diagnosis(self):
        r=read_json(AUTO/'BR24.json')['controlled_retry']
        self.assertTrue(r['original_b004_local_package_check_passed'])
        self.assertFalse(r['original_reference_style_proven_defective'])
        self.assertFalse(r['host_icon_change_guaranteed'])
