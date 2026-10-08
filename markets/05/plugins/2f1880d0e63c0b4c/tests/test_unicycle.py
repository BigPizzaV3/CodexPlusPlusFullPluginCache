import os, subprocess, sys, tempfile, unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
import unicycle

class UnicycleTests(unittest.TestCase):
    def setUp(self):
        self.d=tempfile.TemporaryDirectory(); self.s=str(Path(self.d.name).resolve())
        unicycle.handle(self.s,'configure',{'coordinator':{'threadId':'c','hostId':'h'},'owners':[{'threadId':'o','hostId':'x','title':'Owner'}]})
    def tearDown(self): self.d.cleanup()
    def event(self,kind='decision',source='src',summary='Choose',scope='s',owner=('o','x')):
        return unicycle.handle(self.s,'add-event',{'owner':{'threadId':owner[0],'hostId':owner[1]},'sourceId':source,'kind':kind,'summary':summary,'scope':scope,'options':['a','b'] if kind=='decision' else []})
    def test_cursor_omission_and_reopen(self):
        p={'thread':{'id':'o','hostId':'x'},'cursor':'a','latestAssistantMessage':{'id':'m','phase':'working','text':'hello'}}
        self.assertEqual(len(unicycle.handle(self.s,'ingest',{'polls':[p],'errors':[]})['signals']),1)
        self.assertEqual(unicycle.handle(self.s,'ingest',{'polls':[{'thread':{'id':'o','hostId':'x'},'cursor':None}],'errors':[]})['signals'],[])
        self.assertEqual(unicycle.handle(self.s,'status',{})['targets'][0]['afterCursor'],'a')
    def test_two_decisions_and_preview(self):
        a=self.event()['eventId']; self.event(source='b'); self.event('preview',source='p')
        n=unicycle.handle(self.s,'next',{})['event']; self.assertEqual(n['eventId'],a)
        unicycle.handle(self.s,'receipt',{'eventId':a,'claim':n['claim'],'state':'delivered','evidence':'shown'})
        self.assertEqual(unicycle.handle(self.s,'next',{})['event']['kind'],'preview')
        self.assertIsNone(unicycle.handle(self.s,'next',{})['event'])
    def test_answer_association_conflict_and_duplicate(self):
        eid=self.event()['eventId']; n=unicycle.handle(self.s,'next',{})['event']
        with self.assertRaises(ValueError): unicycle.handle(self.s,'answer',{'eventId':eid,'coordinator':{'threadId':'bad','hostId':'h'},'scope':'s','text':'a','sourceMessageId':'m'})
        unicycle.handle(self.s,'receipt',{'eventId':eid,'claim':n['claim'],'state':'delivered','evidence':'shown'})
        p={'eventId':eid,'coordinator':{'threadId':'c','hostId':'h'},'scope':'s','text':'a','sourceMessageId':'m'}
        with self.assertRaises(ValueError): unicycle.handle(self.s,'answer',{**p,'coordinator':{'threadId':'c','hostId':'wrong'}})
        self.assertIn('dispatch',unicycle.handle(self.s,'answer',p)); self.assertIsNone(unicycle.handle(self.s,'answer',p)['dispatch'])
        with self.assertRaises(ValueError): unicycle.handle(self.s,'answer',{**p,'text':'b'})
    def test_dispatch_receipts_and_uncertain_reopen(self):
        eid=self.event()['eventId']; n=unicycle.handle(self.s,'next',{})['event']
        unicycle.handle(self.s,'receipt',{'eventId':eid,'claim':n['claim'],'state':'uncertain','evidence':'crash'})
        self.assertEqual(unicycle.handle(self.s,'get-event',{'eventId':eid})['state'],'uncertain')
        self.assertIsNone(unicycle.handle(self.s,'next',{})['event'])
        with self.assertRaises(ValueError): unicycle.handle(self.s,'dispatch-receipt',{'eventId':eid,'state':'delivered','evidence':'x'})
        unicycle.handle(self.s,'receipt',{'eventId':eid,'claim':n['claim'],'state':'delivered','evidence':'shown'})
        unicycle.handle(self.s,'answer',{'eventId':eid,'coordinator':{'threadId':'c','hostId':'h'},'scope':'s','text':'a','sourceMessageId':'m'})
        unicycle.handle(self.s,'dispatch-receipt',{'eventId':eid,'state':'queued','evidence':'queued'})
        self.assertEqual(unicycle.handle(self.s,'get-event',{'eventId':eid})['dispatchState']['state'],'queued')
        unicycle.handle(self.s,'dispatch-receipt',{'eventId':eid,'state':'delivered','evidence':'sent'})
        self.assertEqual(unicycle.handle(self.s,'get-event',{'eventId':eid})['dispatchState']['evidence'],'sent')
        with self.assertRaises(ValueError): unicycle.handle(self.s,'dispatch-receipt',{'eventId':eid,'state':'queued','evidence':'late'})
    def test_unknown_owner_errors_clear_and_paging(self):
        with self.assertRaises(ValueError): self.event(owner=('bad','x'))
        with self.assertRaises(ValueError): unicycle.handle(self.s,'ingest',{'polls':[],'errors':[{'threadId':'bad','hostId':'x','error':'secret'}]})
        owners=[{'threadId':f'o{i}','hostId':'x','title':f'O{i}'} for i in range(9)]
        unicycle.handle(self.s,'configure',{'coordinator':{'threadId':'c','hostId':'h'},'owners':owners})
        self.assertEqual(len(unicycle.handle(self.s,'status',{'offset':0})['targets']),8); self.assertEqual(len(unicycle.handle(self.s,'status',{'offset':8})['targets']),1)
    def test_native_long_text_turn_signal_and_same_text_suppression(self):
        p={'thread':{'id':'o','hostId':'x'},'cursor':'a','latestAssistantMessage':{'id':'m','phase':'working','text':'x'*1300},'latestTurn':{'id':'t','status':'completed'}}
        first=unicycle.handle(self.s,'ingest',{'polls':[p],'errors':[]})['signals']; self.assertEqual(len(first[0]['text']),1200); self.assertTrue(first[0]['truncated']); self.assertEqual(first[0]['status'],'turn_completed')
        p['cursor']='b'; p['latestAssistantMessage']={'id':'m2','phase':'working','text':'x'*1300}; p['latestTurn']={'id':'t','status':'completed'}
        second=unicycle.handle(self.s,'ingest',{'polls':[p],'errors':[]})['signals']; self.assertEqual(len(second),0)
    def test_source_conflict_and_pending_config_guard(self):
        eid=self.event()['eventId']
        with self.assertRaises(ValueError): self.event(source='src',summary='changed')
        with self.assertRaises(ValueError): unicycle.handle(self.s,'configure',{'coordinator':{'threadId':'new','hostId':'h'},'owners':[{'threadId':'o','hostId':'x','title':'Owner'}]})
        n=unicycle.handle(self.s,'next',{})['event']; unicycle.handle(self.s,'receipt',{'eventId':eid,'claim':n['claim'],'state':'delivered','evidence':'shown'})
        with self.assertRaises(ValueError): unicycle.handle(self.s,'answer',{'eventId':eid,'coordinator':{'threadId':'c','hostId':'h'},'scope':'wrong','text':'a','sourceMessageId':'m'})
    def test_error_clear_and_dangling_symlink(self):
        unicycle.handle(self.s,'ingest',{'polls':[],'errors':[{'owner':{'threadId':'o','hostId':'x'},'error':'secret'}]})
        self.assertEqual(unicycle.handle(self.s,'status',{})['errors'],[{'threadId':'o','hostId':'x'}])
        p={'thread':{'id':'o','hostId':'x'},'cursor':'a'}; unicycle.handle(self.s,'ingest',{'polls':[p],'errors':[]})
        self.assertEqual(unicycle.handle(self.s,'status',{})['errors'],[])
        bad=Path(self.s)/'bad'; bad.mkdir(); (bad/'state.db').symlink_to(bad/'missing.db')
        with self.assertRaises(ValueError): unicycle.handle(str(bad),'status',{})
        self.assertFalse((bad/'missing.db').exists())
    def test_bounds_capacity_permissions_and_cli(self):
        with self.assertRaises(ValueError): self.event(summary='x'*1201)
        for i in range(128): self.event(source=f'x{i}',summary=f'x{i}')
        self.assertTrue(self.event(source='x0',summary='x0')['duplicate'])
        with self.assertRaises(ValueError): self.event(source='new',summary='new')
        db=Path(self.s)/'state.db'; self.assertEqual(oct(db.stat().st_mode&0o777),'0o600'); self.assertEqual(oct(Path(self.s).stat().st_mode&0o777),'0o700')
        r=subprocess.run([sys.executable,'scripts/unicycle.py','--state-dir',self.s,'status'],input='{bad',text=True,capture_output=True); self.assertNotIn('Traceback',r.stdout); self.assertNotIn(self.s,r.stdout)
    def test_supersession_keeps_history_without_answer(self):
        old=self.event()['eventId']; claim=unicycle.handle(self.s,'next',{})['event']['claim']
        replacement=self.event(source='replacement')['eventId']
        unicycle.handle(self.s,'supersede',{'eventId':old,'replacementEventId':replacement,'evidence':'user changed request; no answer inferred'})
        self.assertEqual(unicycle.handle(self.s,'get-event',{'eventId':old})['state'],'superseded')
        self.assertIsNone(unicycle.handle(self.s,'get-event',{'eventId':old})['dispatchState'])
        self.assertEqual(unicycle.handle(self.s,'next',{})['event']['eventId'],replacement)
        with self.assertRaises(ValueError): unicycle.handle(self.s,'receipt',{'eventId':old,'claim':claim,'state':'delivered','evidence':'late'})

    def test_personas_do_not_change_approval_rules(self):
        for persona in unicycle.PERSONAS:
            cfg={'coordinator':{'threadId':'c','hostId':'h'},'owners':[{'threadId':'o','hostId':'x','title':'Owner'}],'persona':persona}
            self.assertEqual(unicycle.handle(self.s,'configure',cfg)['config']['persona'],persona)
            eid=self.event(source=persona)['eventId']
            with self.assertRaises(ValueError): unicycle.handle(self.s,'answer',{'eventId':eid,'coordinator':cfg['coordinator'],'text':'yes','scope':'s','sourceMessageId':'m'})

    def test_partial_native_results_rotate_owners_across_reopen(self):
        owners=[{'threadId':f'o{i}','hostId':'x','title':f'O{i}'} for i in range(9)]
        unicycle.handle(self.s,'configure',{'coordinator':{'threadId':'c','hostId':'h'},'owners':owners})
        unicycle.handle(self.s,'ingest',{'polls':[{'thread':{'id':'o0','hostId':'x'},'cursor':'first'}]})
        page=unicycle.handle(self.s,'status',{})['targets']
        self.assertEqual(page[0]['threadId'],'o1')
        self.assertIn('o8',[x['threadId'] for x in page])
        unicycle.handle(self.s,'ingest',{'errors':[{'threadId':'o1','hostId':'x'}]})
        self.assertEqual(unicycle.handle(self.s,'status',{})['targets'][0]['threadId'],'o2')

    def test_unclassified_signal_survives_restart_until_acknowledged(self):
        poll={'thread':{'id':'o','hostId':'x'},'cursor':'one','latestAssistantMessage':{'id':'m','phase':'final_answer','text':'Decision needed'}}
        signal=unicycle.handle(self.s,'ingest',{'polls':[poll]})['signals'][0]
        self.assertEqual(unicycle.handle(self.s,'signals',{})['signals'],[signal])
        self.assertEqual(unicycle.handle(self.s,'ingest',{'polls':[poll]})['signals'],[])
        self.assertEqual(unicycle.handle(self.s,'status',{})['pendingSignals'],1)
        unicycle.handle(self.s,'ack-signals',{'signalIds':[signal['signalId']]})
        self.assertEqual(unicycle.handle(self.s,'signals',{})['signals'],[])

    def test_concurrent_claims(self):
        eid=self.event()['eventId']
        with ThreadPoolExecutor(max_workers=2) as pool: got=list(pool.map(lambda _:unicycle.handle(self.s,'next',{})['event'],[1,2]))
        self.assertEqual(sum(x is not None for x in got),1); self.assertEqual(next(x for x in got if x)['eventId'],eid)

if __name__=='__main__': unittest.main()
