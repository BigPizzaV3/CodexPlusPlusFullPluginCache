"""Stage a local tutor photo using a private link returned by MatchLah MCP. Never saves the profile."""
import argparse
import json
import mimetypes
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError
import secrets

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

class FormToken(HTMLParser):
    value = None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='input' and a.get('name')=='csrf':
            self.value=a.get('value')

def upload(path, url):
    u=urlparse(url)
    if u.scheme!='https' or u.hostname!='matchlah.com' or u.port not in (None,443) or u.username or u.password or u.fragment or u.path!='/matchlah-connect/photo-upload' or set(parse_qs(u.query))!={'upload'}:
        raise ValueError('Use the private upload_url returned by create_tutor_photo_upload.')
    path=Path(path)
    if not path.is_file() or not 0<path.stat().st_size<=8388608:
        raise ValueError('Choose an existing image file no larger than 8MB.')
    if path.suffix.lower() not in ('.jpg','.jpeg','.png','.webp','.heic','.heif'):
        raise ValueError('Choose JPG, PNG, WebP, HEIC or HEIF.')
    opener=build_opener(NoRedirect())
    with opener.open(Request(url,headers={'User-Agent':'MatchLah-Photo-Upload/1.0'}),timeout=30) as r:
        page=r.read(65536).decode('utf-8')
    parser=FormToken(); parser.feed(page)
    if not parser.value:
        raise ValueError('This link was already used or expired. Read get_tutor_photo_upload or create a fresh link.')
    boundary='matchlah'+secrets.token_hex(20)
    mime=mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    # Fixed basename avoids multipart header injection from a user filename.
    head=(f'--{boundary}\r\nContent-Disposition: form-data; name="csrf"\r\n\r\n{parser.value}\r\n'
          f'--{boundary}\r\nContent-Disposition: form-data; name="photo"; filename="profile{path.suffix.lower()}"\r\nContent-Type: {mime}\r\n\r\n').encode()
    body=head+path.read_bytes()+f'\r\n--{boundary}--\r\n'.encode()
    req=Request(url,data=body,headers={'Content-Type':f'multipart/form-data; boundary={boundary}','Accept':'application/json','User-Agent':'MatchLah-Photo-Upload/1.0'},method='POST')
    with opener.open(req,timeout=60) as r:
        return json.load(r)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file',required=True);parser.add_argument('--upload-url',required=True)
    args=parser.parse_args()
    try:
        result=upload(args.file,args.upload_url)
        print(json.dumps(result))
    except (ValueError,OSError,HTTPError,URLError) as e:
        # Do not echo request URLs or local paths from exception messages.
        print(json.dumps({'uploaded':False,'error':'Upload failed. Check the image format and size, then read the upload status or request a fresh link.'}))
        raise SystemExit(1)
