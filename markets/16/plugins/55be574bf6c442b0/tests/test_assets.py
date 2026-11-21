import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/homey-device-asset-creator/scripts'))
from make_png_sizes import square_on_white,SIZES
from asset_validation import validate_pngs,validate_svg,render_svg

SVG='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 960"><circle cx="480" cy="480" r="380" fill="none" stroke="#000000" stroke-width="24"/></svg>'

class AssetChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        self.master=self.root/'master.png'
        im=Image.new('RGB',(1200,1200),'white')
        d=ImageDraw.Draw(im)
        d.ellipse((120,120,1080,1080),fill='#E5E7EB',outline='black',width=8)
        im.save(self.master)
        for name,size in SIZES.items():
            im.resize((size,size),Image.Resampling.LANCZOS).save(self.root/name)
        self.svg=self.root/'icon.svg'
        self.svg.write_text(SVG)
    def tearDown(self):
        self.tmp.cleanup()
    def test_valid_common_master(self):
        self.assertEqual(validate_pngs(self.root,self.master),[])
    def test_three_device_shapes(self):
        for shape in ('sensor','wall-switch','glass-display'):
            im=Image.new('RGBA',(1300,1050),'white')
            d=ImageDraw.Draw(im)
            if shape=='sensor':
                d.ellipse((210,85,1090,965),fill='#EEEEEE',outline='black',width=12)
            else:
                d.rounded_rectangle((260,80,1040,970),radius=55,fill='#EEEEEE' if shape=='wall-switch' else '#202024')
                d.rectangle((360,220,940,730),fill='#DDDDDD' if shape=='wall-switch' else '#566D79')
            im=square_on_white(im)
            im.save(self.master)
            for name,size in SIZES.items():
                im.resize((size,size),Image.Resampling.LANCZOS).save(self.root/name)
            self.assertEqual(validate_pngs(self.root,self.master),[],shape)
    def test_edge_contamination_away_from_corners(self):
        p=self.root/'large.png'
        with Image.open(p) as im:
            im.putpixel((250,0),(250,250,250)); im.save(p)
        self.assertTrue(validate_pngs(self.root))
    def test_transparency(self):
        p=self.root/'large.png'
        with Image.open(p) as im:
            im=im.convert('RGBA'); im.putpixel((250,250),(255,255,255,0)); im.save(p)
        self.assertTrue(validate_pngs(self.root))
    def test_master_mismatch(self):
        p=self.root/'large.png'
        with Image.open(p) as im:
            im.putpixel((250,250),(1,2,3)); im.save(p)
        self.assertTrue(validate_pngs(self.root,self.master))
    def test_corrupt_file(self):
        (self.root/'large.png').write_bytes(b'bad')
        self.assertTrue(validate_pngs(self.root))
    def test_wrong_size(self):
        Image.new('RGB',(500,499),'white').save(self.root/'large.png')
        self.assertTrue(validate_pngs(self.root))
    def test_missing_file(self):
        (self.root/'large.png').unlink()
        self.assertTrue(validate_pngs(self.root))
    def test_empty_file(self):
        Image.new('RGB',(500,500),'white').save(self.root/'large.png')
        self.assertTrue(validate_pngs(self.root))
    def test_valid_svg(self):
        self.assertEqual(validate_svg(self.svg),[])
    def test_forbidden_svg_techniques(self):
        for fragment in ('<image href="x.png"/>','<filter/>','<mask/>','<clipPath/>','<linearGradient/>','<style>circle{fill:red}</style>','<script/>','<animate/>','<use href="https://example.com/x.svg"/>','<foreignObject/>'):
            with self.subTest(fragment=fragment):
                self.svg.write_text(SVG.replace('</svg>',fragment+'</svg>'))
                self.assertTrue(validate_svg(self.svg))
    def test_disallowed_paint_and_attributes(self):
        for substitution in ('fill="white"','fill="url(#x)"','opacity="0.5"','onload="run()"','style="filter:none"','stroke-width="NaN"'):
            with self.subTest(value=substitution):
                self.svg.write_text(SVG.replace('fill="none"',substitution))
                self.assertTrue(validate_svg(self.svg))
    def test_fixed_root_and_viewbox(self):
        for content in (SVG.replace('<svg ','<svg width="960" '),SVG.replace('0 0 960 960','0 0 24 24'),SVG.replace('<circle','<image')):
            self.svg.write_text(content)
            self.assertTrue(validate_svg(self.svg))
    def test_all_render_sizes(self):
        self.assertEqual(render_svg(self.svg,self.root/'renders'),[])
        self.assertEqual(len(list((self.root/'renders').glob('*.png'))),5)
    def test_opaque_svg_background(self):
        self.svg.write_text(SVG.replace('<circle','<rect width="960" height="960" fill="black"/><circle'))
        self.assertTrue(render_svg(self.svg,self.root/'renders'))

if __name__=='__main__':
    unittest.main(verbosity=2)
