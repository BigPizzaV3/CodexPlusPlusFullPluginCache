"""Trusted fixed recipe only. Run in a timeout-controlled child process."""
import ctypes as C
import hashlib
import math
from pathlib import Path
import sys

def validate(path, name, expected_hash):
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected_hash
    class Descriptor(C.Structure): pass
    P = C.POINTER(Descriptor)
    Instantiate = C.CFUNCTYPE(C.c_void_p, P, C.c_double, C.c_char_p, C.c_void_p)
    Connect = C.CFUNCTYPE(None, C.c_void_p, C.c_uint32, C.c_void_p)
    Activate = C.CFUNCTYPE(None, C.c_void_p)
    Run = C.CFUNCTYPE(None, C.c_void_p, C.c_uint32)
    Extension = C.CFUNCTYPE(C.c_void_p, C.c_char_p)
    Descriptor._fields_ = [('uri',C.c_char_p),('instantiate',Instantiate),('connect',Connect),
                           ('activate',Activate),('run',Run),('deactivate',Activate),
                           ('cleanup',Activate),('extension',Extension)]
    lib = C.CDLL(path)
    lib.lv2_descriptor.argtypes = [C.c_uint32]; lib.lv2_descriptor.restype = P
    ptr = lib.lv2_descriptor(0); assert ptr and not lib.lv2_descriptor(1)
    d = ptr.contents; assert d.uri.decode() == 'urn:dispro:'+name
    for rate in (44100,48000,96000):
        h = d.instantiate(ptr,rate,str(Path(path).parent).encode()+b'/',None); assert h
        try:
            for n in (0,64,257):
                values = [0.125*math.sin(i*0.31) for i in range(n)]
                for level, effective in ((0.,0.),(.5,.5),(1.,1.),(2.,2.),(-1.,0.),(3.,2.),(float('nan'),1.)):
                    for inplace in (False,True):
                        inp = (C.c_float*max(n,1))(*values)
                        out = inp if inplace else (C.c_float*max(n,1))()
                        gain = C.c_float(level)
                        d.connect(h,0,inp); d.connect(h,1,out); d.connect(h,2,C.byref(gain))
                        d.run(h,n)
                        assert all(math.isfinite(out[i]) and abs(out[i]-values[i]*effective)<1e-6 for i in range(n))
        finally: d.cleanup(h)
    print('LV2 offline contract passed')

if __name__ == '__main__': validate(*sys.argv[1:])
