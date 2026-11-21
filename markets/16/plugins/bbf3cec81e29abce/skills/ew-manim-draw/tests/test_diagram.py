import copy,json,sys,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P/'scripts'))
from diagram import validate,layout,make_html,svg
from validate_flow import validate as legacy
class DiagramTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((P/'examples/grouped_architecture.json').read_text())
 def test_graph(self):validate(self.d)
 def test_rejections(self):
  mutations=[lambda d:d['graph']['nodes'][0].update(id='play'),lambda d:d['sources'].append(copy.deepcopy(d['sources'][0])),lambda d:d['story']['steps'].append(copy.deepcopy(d['story']['steps'][0])),lambda d:d['story'].update(mode='loop'),lambda d:d.update(unexpected=1),lambda d:d['graph']['nodes'][0].update(id='e1'),lambda d:d['graph']['edges'][0].update(to='missing'),lambda d:d['graph']['nodes'][0].update(group='missing'),lambda d:d['story']['steps'][0].update(duration=float('nan')),lambda d:d['sources'][0].update(targets=['input']),lambda d:d['graph']['groups'][0].update(parent='output'),lambda d:d['export'].update(width=999999)]
  for mutate in mutations:
   d=copy.deepcopy(self.d);mutate(d)
   with self.assertRaises((ValueError,KeyError)):validate(d)
 def test_legacy(self):legacy(json.loads((P/'examples/simple_flow.json').read_text()))
 def test_text_is_data(self):
  d=copy.deepcopy(self.d);d['title']='</script><img src=x onerror=alert(1)>'
  l={'font_family':'Test','groups':[],'nodes':[],'edges':[],'captions':[['test']]};s=svg(d,l);h=make_html(d,l,s)
  self.assertNotIn('<img src=x',h);self.assertIn('\\u003c/script',h)
if __name__=='__main__':unittest.main()
