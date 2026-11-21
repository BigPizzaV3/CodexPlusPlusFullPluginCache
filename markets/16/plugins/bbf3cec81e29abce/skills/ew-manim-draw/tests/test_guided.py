import copy,json,sys,unittest
from pathlib import Path
from PIL import ImageChops
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P/'scripts'))
from guided import validate,layout,state,raster,svg,make_html,wrap,font
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
class GuidedTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((P/'examples/guided_architecture.json').read_text())
 def test_nested_groups_open_branch_and_bidirectional(self):
  validate(self.d);l=layout(self.d,F)
  self.assertEqual(next(e for e in l['edges'] if e['id']=='no').get('to'),None)
  self.assertEqual(next(e for e in l['edges'] if e['id']=='e6')['direction'],'both')
  self.assertEqual(next(g for g in l['groups'] if g['id']=='workers')['parent'],'platform')
 def test_reject_unknown_and_unmapped_and_cycle(self):
  mutations=[lambda d:d.update(code='print(1)'),lambda d:d['sources'][0].update(targets=['platform']),lambda d:d['graph']['groups'][0].update(parent='workers'),lambda d:d['graph']['nodes'][0].update(bounds=[80,430,195,float('nan')]),lambda d:d['graph']['edges'][0].update(to='missing'),lambda d:d['graph']['groups'][0].update(columns=1.5),lambda d:d['story']['steps'][1].update(id='s1'),lambda d:d['story']['steps'][0].update(duration=float('inf'))]
  for mutate in mutations:
   d=copy.deepcopy(self.d);mutate(d)
   with self.assertRaises(ValueError):validate(d)
 def test_geometry_rejects_clipping_and_crossing(self):
  d=copy.deepcopy(self.d);d['graph']['nodes'][0]['label']='An exceptionally long label repeated '*15
  with self.assertRaises(ValueError):layout(validate(d),F)
  d=copy.deepcopy(self.d);d['graph']['edges'][0]['points']=[[275,490],[500,490],[500,385],[360,385]]
  with self.assertRaisesRegex(ValueError,'crosses card'):layout(validate(d),F)
 def test_timeline_boundary_and_reset(self):
  self.assertEqual(state(self.d,0)['index'],0);self.assertEqual(state(self.d,3)['index'],1);self.assertEqual(state(self.d,21)['index'],0)
  self.assertIn('e1',state(self.d,4)['trail']);self.assertNotIn('e2',state(self.d,4)['trail']);self.assertIn('e2',state(self.d,4)['active'])
 def test_static_labels_and_changing_particles(self):
  l=layout(self.d,F);a=raster(self.d,l,F,.25);b=raster(self.d,l,F,1.5)
  self.assertIsNotNone(ImageChops.difference(a,b).getbbox())
  self.assertIsNone(ImageChops.difference(a.crop((95,455,258,525)),b.crop((95,455,258,525))).getbbox())
 def test_literal_text_and_word_wrap(self):
  d=copy.deepcopy(self.d);d['title']='</script><img src=x>'
  l=layout(validate(d),F);s=svg(d,l);h=make_html(d,l,s)
  self.assertNotIn('<img src=x>',h);self.assertIn('\\u003c/script',h)
  lines=wrap('Request gateway',font(F,30),244)
  self.assertEqual(lines,['Request','gateway'])
 def test_missing_language_glyph_rejected(self):
  d=copy.deepcopy(self.d);d['title']='中文架構';d['locale']='zh-TW'
  with self.assertRaisesRegex(ValueError,'lacks glyph'):layout(validate(d),F)
 def test_auto_grid_nine_cards(self):
  d=copy.deepcopy(self.d);d['graph']={'groups':[{'id':'grid','label':'Nine modules','columns':3}], 'nodes':[{'id':'n'+str(i),'label':'Module '+str(i),'group':'grid'} for i in range(9)],'edges':[]};d['sources'][0]['targets']=['grid']+['n'+str(i) for i in range(9)];d['story']['steps']=[{'id':'step','text':'Nine modules in one persistent group.','targets':['grid'],'duration':3}]
  l=layout(validate(d),F);self.assertEqual(len(l['nodes']),9);self.assertEqual(len({n['bounds'][1] for n in l['nodes']}),3)
if __name__=='__main__':unittest.main()
