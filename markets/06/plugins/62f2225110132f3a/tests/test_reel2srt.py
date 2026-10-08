import importlib.util
import math
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('reel2srt',Path(__file__).parents[1]/'skills/reel2srt/scripts/reel2srt.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def w(start,end,text=' hello'):
    return {'start':start,'end':end,'word':text}

class SubtitleTests(unittest.TestCase):
    def test_duration_language_matrix(self):
        for duration in [30,60,180,300]:
            for text in ['สวัสดีครับ',' Hello world','วันนี้เล่น basketball']:
                with self.subTest(duration=duration,text=text):
                    cues=m.build_cues([w(1,2,text),w(duration-2,duration-1,text)],duration)
                    self.assertEqual([(c['start_ms'],c['end_ms']) for c in cues],[(1000,2000),((duration-2)*1000,(duration-1)*1000)])
                    self.assertEqual([c['text'] for c in cues],[text.strip()]*2)
    def test_exact_pause_splits(self):
        self.assertEqual(len(m.build_cues([w(1,2),w(2.2,3)],30)),2)
    def test_short_gap_groups(self):
        self.assertEqual(len(m.build_cues([w(1,2),w(2.19,3)],30)),1)
    def test_no_stretch(self):
        self.assertEqual(m.build_cues([w(5,6)],300),[{'start_ms':5000,'end_ms':6000,'text':'hello'}])
    def test_character_limit(self):
        self.assertEqual(len(m.build_cues([w(1,2,'a'*30),w(2,3,'b'*20)],30)),2)
    def test_seconds_limit(self):
        self.assertEqual(len(m.build_cues([w(0,3),w(3,5)],30)),2)
    def test_long_token_requires_review(self):
        for word in [w(1,2,'x'*43),w(0,5)]:
            with self.assertRaises(m.QualityError):m.build_cues([word],30)
    def test_thai_zero_duration_subwords(self):
        cues=m.build_cues([w(.94,1.14,'ม'),w(1.14,1.14,'ี'),w(1.14,1.32,' 2')],30)
        self.assertEqual(cues,[{'start_ms':940,'end_ms':1320,'text':'มี 2'}])
    def test_combining_mark_never_starts_new_cue(self):
        with self.assertRaises(m.QualityError):
            m.build_cues([w(1,2,'ก'*42),w(2,2,'ี')],30)
    def test_invalid_durations(self):
        for duration in [0,-1,300.0001,math.nan,math.inf,True,'30']:
            with self.subTest(duration=duration),self.assertRaises(m.QualityError):m.build_cues([],duration)
    def test_bad_times(self):
        for word in [w(-1,1),w(1,1),w(2,1),w(29,30.001),w(math.nan,2),w(1,math.inf)]:
            with self.subTest(word=word),self.assertRaises(m.QualityError):m.build_cues([word],30)
    def test_no_overlap_or_sort(self):
        for words in [[w(1,3),w(2,4)],[w(5,6),w(1,2)]]:
            with self.assertRaises(m.QualityError):m.build_cues(words,30)
    def test_invalid_text(self):
        for text in ['', '  ', 'hello\n\n99', '-->',None]:
            with self.assertRaises(m.QualityError):m.build_cues([w(1,2,text)],30)
    def test_submillisecond_interval(self):
        with self.assertRaises(m.QualityError):m.build_cues([w(1.0001,1.0002)],30)
    def test_rounding_stays_inside(self):
        cue=m.build_cues([w(29.0001,29.9999)],29.9999)
        self.assertEqual((cue[0]['start_ms'],cue[0]['end_ms']),(29001,29999))
    def test_silence(self):
        self.assertEqual(m.render(m.build_cues([],300)),'')
    def test_srt_format(self):
        self.assertEqual(m.render(m.build_cues([w(1,2,'ไทย English'),w(3,4,'test')],30)),
                         '1\n00:00:01,000 --> 00:00:02,000\nไทย English\n\n2\n00:00:03,000 --> 00:00:04,000\ntest\n\n')

if __name__=='__main__':unittest.main()
