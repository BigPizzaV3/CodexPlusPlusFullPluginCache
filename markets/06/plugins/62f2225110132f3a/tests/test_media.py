"""Synthetic container/offset tests; not speech-recognition benchmarks."""
from fractions import Fraction
from pathlib import Path
import tempfile
import unittest
from test_reel2srt import m
try:
    import av
    import numpy as np
except ImportError:
    av=np=None

@unittest.skipUnless(av is not None, 'Requires runtime dependencies PyAV and numpy')
class MediaTests(unittest.TestCase):
    def fixture(self,path,seconds,audio=True):
        with av.open(str(path),'w') as c:
            v=c.add_stream('mpeg4',rate=1);v.width=32;v.height=32;v.pix_fmt='yuv420p'
            a=c.add_stream('pcm_s16le',rate=16000) if audio else None
            if a:a.layout='mono'
            for i in range(seconds):
                frame=av.VideoFrame.from_ndarray(np.zeros((32,32,3),dtype=np.uint8),format='rgb24');frame.pts=i
                for packet in v.encode(frame):c.mux(packet)
                # Leave one second leading silence, then one second tone; no audio packets after it.
                if i==1 and a:
                    samples=(np.sin(np.arange(16000)*2*np.pi*440/16000)*10000).astype(np.int16).reshape(1,-1)
                    f=av.AudioFrame.from_ndarray(samples,format='s16',layout='mono');f.sample_rate=16000;f.pts=16000;f.time_base=Fraction(1,16000)
                    for packet in a.encode(f):c.mux(packet)
            for packet in v.encode():c.mux(packet)
            if a:
                for packet in a.encode():c.mux(packet)
    def test_durations_and_audio_offset(self):
        with tempfile.TemporaryDirectory() as temp:
            for seconds in [30,60,180,300]:
                with self.subTest(seconds=seconds):
                    p=Path(temp)/f'{seconds}.mov';self.fixture(p,seconds)
                    audio,duration=m.decode_timeline(p)
                    self.assertAlmostEqual(duration,seconds,places=3)
                    self.assertEqual(len(audio),seconds*16000)
                    self.assertEqual(float(np.max(np.abs(audio[:16000]))),0)
                    self.assertGreater(float(np.max(np.abs(audio[16000:32000]))),.1)
                    self.assertEqual(float(np.max(np.abs(audio[32000:]))),0)
    def test_no_audio(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'no-audio.mov';self.fixture(p,2,audio=False)
            with self.assertRaises(m.QualityError):m.decode_timeline(p)
    def test_over_five_minutes(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'long.mov';self.fixture(p,301)
            with self.assertRaises(m.QualityError):m.decode_timeline(p)
