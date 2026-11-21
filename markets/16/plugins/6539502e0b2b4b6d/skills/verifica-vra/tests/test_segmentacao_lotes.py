"""Testes de segmentação física local sem inferência de leitura Gemini."""
import pathlib, tempfile, sys, unittest, json
BASE=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'scripts'))
from preparar_autos_em_partes import split_corpus
try:import fitz
except ImportError: fitz=None

@unittest.skipUnless(fitz is not None,'PyMuPDF não disponível')
class TestSegmentacao(unittest.TestCase):
    def test_integridade_cobertura_serie(self):
        with tempfile.TemporaryDirectory() as t:
            root=pathlib.Path(t); p=root/'origem.pdf'
            with fitz.open() as doc:
                for i in range(13):
                    pg=doc.new_page(); pg.insert_text((48,48),f'Página real {i+1}; Movimento {i//3+1}')
                doc.save(p)
            r=split_corpus(p,root/'partes',pages_per_part=5,batch_size=2)
            self.assertEqual(r['origin']['pdf_pages'],13)
            self.assertEqual([(x['first_original_pdf_page'],x['last_original_pdf_page']) for x in r['parts']],[(1,5),(6,10),(11,13)])
            self.assertEqual(len(r['batches']),2)
            self.assertEqual(r['verification']['reading_by_gemini'],'NOT_VERIFIED')
            self.assertEqual(sum(x['page_count'] for x in r['parts']),13)
            for item in r['parts']:
                with fitz.open(root/'partes'/item['filename']) as d:
                    self.assertEqual(len(d),item['page_count'])
    def test_nao_sobrescrever_dados(self):
        with tempfile.TemporaryDirectory() as t:
            root=pathlib.Path(t);p=root/'in.pdf'
            with fitz.open() as d:
                for _ in range(6):d.new_page()
                d.save(p)
            split_corpus(p,root/'out',pages_per_part=5)
            with self.assertRaises(FileExistsError):split_corpus(p,root/'out',pages_per_part=5)
    def test_limites(self):
        with self.assertRaises(ValueError):split_corpus('missing.pdf','/tmp/test',pages_per_part=3)

if __name__=='__main__':unittest.main()
