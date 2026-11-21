from __future__ import annotations
import io
import stat
import unittest
import zipfile
import warnings
from iteration.safety import canonical,code_path,decode_file,read_archive,IterationError,validate_schema

class SafetyTests(unittest.TestCase):
    def test_good_path(self):self.assertEqual(code_path('PROGRAM/assets/hello.png'),'PROGRAM/assets/hello.png')
    def test_text_decoding(self):self.assertEqual(decode_file({'content':'hello'}),b'hello')
    def test_base64_decoding(self):self.assertEqual(decode_file({'content':'AAEC','encoding':'base64'}),b'\x00\x01\x02')
    def test_bad_base64(self):
        with self.assertRaises(IterationError):decode_file({'content':'@@','encoding':'base64'})
    def test_bad_encoding(self):
        with self.assertRaises(IterationError):decode_file({'content':'x','encoding':'rot13'})
    def test_secret_pattern(self):
        with self.assertRaises(IterationError):decode_file({'content':'sk-'+'a'*35})
    def test_private_key_pattern(self):
        with self.assertRaises(IterationError):decode_file({'content':'-----BEGIN '+'PRIVATE KEY-----'})
    def test_bool_not_integer(self):
        with self.assertRaises(IterationError):validate_schema(True,{'type':'integer'})
    def test_unknown_schema_property(self):
        with self.assertRaises(IterationError):validate_schema({'bad':1},{'type':'object','properties':{},'additionalProperties':False})
    def test_missing_schema_property(self):
        with self.assertRaises(IterationError):validate_schema({}, {'type':'object','properties':{'id':{'type':'string'}},'required':['id']})
    def test_schema_range(self):
        with self.assertRaises(IterationError):validate_schema(101,{'type':'integer','maximum':100})
    def test_empty_archive(self):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w'):pass
        with self.assertRaises(IterationError):read_archive(b.getvalue())
    def test_invalid_archive(self):
        with self.assertRaises(IterationError):read_archive(b'not a zip')
    def test_zip_traversal(self):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w') as z:z.writestr('../outside','bad')
        with self.assertRaises(IterationError):read_archive(b.getvalue())
    def test_zip_symlink(self):
        b=io.BytesIO();zi=zipfile.ZipInfo('PROGRAM/link');zi.create_system=3;zi.external_attr=(stat.S_IFLNK|0o777)<<16
        with zipfile.ZipFile(b,'w') as z:z.writestr(zi,'/outside')
        with self.assertRaises(IterationError):read_archive(b.getvalue())
    def test_zip_duplicate(self):
        b=io.BytesIO()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            with zipfile.ZipFile(b,'w') as z:z.writestr('PROGRAM/a','x');z.writestr('PROGRAM/a','y')
        with self.assertRaises(IterationError):read_archive(b.getvalue())
    def test_zip_case_collision(self):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w') as z:z.writestr('PROGRAM/A.txt','x');z.writestr('PROGRAM/a.txt','y')
        with self.assertRaises(IterationError):read_archive(b.getvalue())
    def test_zip_compression_bomb(self):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED) as z:z.writestr('PROGRAM/bomb','a'*(2*1024*1024))
        with self.assertRaises(IterationError):read_archive(b.getvalue())

BAD_PATHS=['../a','/abs','C:/drive','PROGRAM/a\\b','PROGRAM/../a','PROGRAM/./a','PROGRAM//a','PROGRAM/a:stream',
           'PROGRAM/CON','PROGRAM/aux.txt','PROGRAM/a.','PROGRAM/a ','PROGRAM/a\x00b','PROGRAM/a\nb','PROGRAM/x?y','PROGRAM/LPT1.txt']
for index,path in enumerate(BAD_PATHS):
    def test(self,p=path):
        with self.assertRaises(IterationError):canonical(p)
    setattr(SafetyTests,f'test_reject_windows_path_{index:02d}',test)
for index,path in enumerate(['PROGRAM/.env','PROGRAM/.git/config','PROGRAM/.ssh/id_rsa','PROGRAM/keys/private.pem','PROGRAM/Automation/A00.json']):
    def test(self,p=path):
        with self.assertRaises(IterationError):code_path(p)
    setattr(SafetyTests,f'test_reject_protected_path_{index:02d}',test)
