"""Independent generated-app fixtures: meaningful actual paths, not a customer app."""
from __future__ import annotations
import json
import os
from pathlib import Path
import tempfile
import textwrap
import unittest
from iteration.engine import Engine
from deliver import deliver
from test_qualified_delivery import full_plan


GUI_SOURCE = '''from Automation.RT42 import ready, case
import sys, tkinter as tk
root=tk.Tk();root.title('Independent validation fixture')
text=tk.StringVar(value='0');status=tk.StringVar(value='');value=tk.IntVar(value=0)
entry=tk.Entry(root,textvariable=text);entry.pack()
label=tk.Label(root,textvariable=status);label.pack()
def apply():
    s=text.get()
    if not s.isascii() or not s.isdecimal() or len(s)>10:
        status.set('Enter a whole number between 0 and 2147483647');return
    n=int(s)
    if n>2147483647:
        status.set('That number is too large');return
    value.set(n);status.set('Saved')
button=tk.Button(root,text='Apply',command=apply);button.pack()
root.update_idletasks();root.update()
if '--iteration-smoke-test' in sys.argv:
    with case('open','startup'):
        assert root.winfo_exists() and button.winfo_ismapped()
        text.set('5');button.invoke();root.update();assert value.get()==5
    ready();print('ITERATION_SMOKE_OK')
else:
    ready()
    with case('valid','primary'):
        text.set('27');button.invoke();assert value.get()==27 and status.get()=='Saved'
    with case('invalid','invalid-input'):
        for s in ('', '3.5', '-2', 'abc'):
            text.set(s);button.invoke();root.update();assert value.get()==27 and status.get()!='Saved'
    with case('limit','boundary'):
        for s in ('2147483647','0'):
            text.set(s);button.invoke();assert value.get()==int(s)
        for s in ('9'*6000, '2147483648'):
            text.set(s);button.invoke();root.update()
            assert root.winfo_exists() and value.get()==0 and status.get()!='Saved'
        text.set('7');button.invoke();assert value.get()==7
    print('ITERATION_SELF_TEST_OK')
root.destroy()
'''

CSV_SOURCE = r'''from Automation.RT42 import ready,case
import csv,io,os,sys
from pathlib import Path
root=Path(os.environ['ITERATION_TEST_DATA_DIR'])
output=root/'result.csv'
def transform(s):
    rows=list(csv.DictReader(io.StringIO(s)))
    result=[]
    for r in rows:
        n=r.get('amount','')
        if not n.isascii() or not n.isdecimal() or len(n)>6 or int(n)>100000:
            raise ValueError('Invalid amount')
        result.append((r['name'].strip(),int(n)))
    return result
def save(rows):
    # Exclusive creation refuses collisions rather than overwriting.
    with output.open('x',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['name','amount']);w.writerows(rows)
if '--iteration-smoke-test' in sys.argv:
    with case('open','startup'):
        save(transform('name,amount\nalpha,2\n'))
        assert transform(output.read_text())==[('alpha',2)]
    ready();print('ITERATION_SMOKE_OK')
else:
    ready()
    with case('valid','primary'):
        save(transform('name,amount\nbeta,12\n'))
        assert transform(output.read_text())==[('beta',12)]
    with case('invalid','invalid-input'):
        before=output.read_bytes()
        try: transform('name,amount\nbeta,bad\n')
        except ValueError: pass
        else: raise AssertionError('Invalid accepted')
        assert output.read_bytes()==before
    with case('limit','boundary'):
        assert transform('name,amount\nz,100000\n')==[('z',100000)]
        for number in ('100001','9'*5000):
            try: transform('name,amount\nz,'+number+'\n')
            except ValueError: pass
            else: raise AssertionError('Overflow accepted')
    with case('safe','file-safety'):
        before=output.read_bytes()
        try: save([('overwrite',9)])
        except FileExistsError: pass
        else: raise AssertionError('Collision overwritten')
        assert output.read_bytes()==before
    print('ITERATION_SELF_TEST_OK')
'''

JSON_SOURCE = r'''from Automation.RT42 import ready,case,fail
import json,os,sys,shutil,subprocess,zipfile,uuid
from pathlib import Path
root=Path(os.environ['ITERATION_TEST_DATA_DIR']);root.mkdir(parents=True,exist_ok=True)
path=root/'settings.json'
def read(p):
    v=json.loads(p.read_text())
    if not isinstance(v,dict) or v.get('version')!=1 or type(v.get('count')) is not int or not 0<=v['count']<=1000:
        raise ValueError('Invalid configuration')
    return v
def write(count):
    if type(count) is not int or not 0<=count<=1000:raise ValueError('Invalid count')
    tmp=root/('tmp-'+uuid.uuid4().hex)
    tmp.write_text(json.dumps({'version':1,'count':count}));tmp.replace(path)
def backup():
    target=root/('recovery-'+uuid.uuid4().hex+'.json')
    with target.open('xb') as f:f.write(path.read_bytes())
    assert read(target)==read(path)
    return target
if not any(x in sys.argv for x in ('--iteration-smoke-test','--iteration-self-test')):
    try: read(path)
    except (ValueError,OSError):fail('configuration-invalid')
    else:ready()
elif '--iteration-smoke-test' in sys.argv:
    with case('open','startup'):
        write(3);assert read(path)['count']==3
    ready();print('ITERATION_SMOKE_OK')
else:
    ready()
    with case('valid','primary'):
        write(7);assert read(path)['count']==7
    with case('invalid','invalid-input'):
        before=path.read_bytes()
        for v in (-1,1.5,True,'3'):
            try: write(v)
            except ValueError: pass
            else: raise AssertionError('Invalid accepted')
        assert before==path.read_bytes()
    with case('limit','boundary'):
        for v in (0,1000):write(v);assert read(path)['count']==v
        for v in (1001,10**60):
            try:write(v)
            except ValueError:pass
            else:raise AssertionError('Oversize accepted')
    with case('persist','persistence'):
        write(9)
        subprocess.run([sys.executable,'-c',"import json,sys; assert json.load(open(sys.argv[1]))['count']==9",str(path)],check=True)
    with case('refuse','startup-refusal'):
        # Exercise actual app initialization in another supervised program copy.
        app=root/'refusal-case';shutil.copytree(Path(__file__).parent,app/'PROGRAM')
        state=app/'data';state.mkdir();bad=state/'settings.json';bad.write_text('{broken')
        before=bad.read_bytes()
        result=subprocess.run([sys.executable,str(app/'PROGRAM/Automation/ZP90.py')],
            env={**os.environ,'ITERATION_TEST_DATA_DIR':str(state)},capture_output=True,timeout=8)
        with zipfile.ZipFile(app/'LogReport.zip') as z:record=json.loads(z.read('report.json'))
        assert result.returncode!=0 and record['process_exit_code']==0
        assert record['state']=='startup_failed' and not record['lifecycle']['ready']
        assert 'configuration-invalid' in record['lifecycle']['failure_codes']
        assert bad.read_bytes()==before
    with case('snapshots','collision-recovery'):
        write(3);a=backup();write(4);b=backup()
        assert a!=b and read(a)['count']==3 and read(b)['count']==4
    with case('safe','file-safety'):
        saved=path.read_bytes();bad=root/'bad.json';bad.write_text('{broken')
        try: read(bad)
        except ValueError: pass
        else: raise AssertionError('Bad input accepted')
        assert path.read_bytes()==saved
    print('ITERATION_SELF_TEST_OK')
'''


class IndependentApplicationCases(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='iteration-real-fixtures-')
        self.root=Path(self.temp.name);self.engine=Engine(self.root/'state')
    def tearDown(self):self.engine.close();self.temp.cleanup()
    def run_case(self,source,plan):
        p=self.engine.create_project('Disposable type fixture');t=self.engine.begin(p['id'],0,'Exercise this actual application type')
        self.engine.write_files(t['id'],0,[{'path':'PROGRAM/main.py','content':textwrap.dedent(source)}])
        self.engine.configure_checks(t['id'],1,plan)
        b=self.engine.package(t['id'],2,'Type fixture',[],['Windows untested'],['Run fixture'])
        r=deliver(self.engine,b['id'],self.root/'fixture.zip',allow_execute=True)
        self.assertEqual(r['status'],'passed',json.dumps(r,indent=2))
        self.assertTrue(all(c['application_ready'] for c in r['evidence']['checks']))
        return r
    def test_real_tk_validation_handles_oversized_input_without_closing_window(self):
        if os.name!='nt' and not os.environ.get('DISPLAY'):self.skipTest('Real Tk display required')
        self.run_case(GUI_SOURCE,full_plan('gui'))
    def test_csv_tool_qualifies_real_transform_invalid_inputs_and_file_collision(self):
        self.run_case(CSV_SOURCE,full_plan('cli',['writes-files'],[('safe','regression','file-safety','Refuse output collisions and preserve the original file.')]))
    def test_json_tool_checks_actual_startup_refusal_persistence_and_unique_snapshots(self):
        extras=[('persist','regression','persistence','Read saved state in a second real process.'),
                ('refuse','regression','startup-refusal','Run actual startup against malformed saved state; require failed diagnostics.'),
                ('snapshots','regression','collision-recovery','Repeated snapshots retain both distinct earlier states.'),
                ('safe','regression','file-safety','Refusing a malformed input does not modify valid state.')]
        self.run_case(JSON_SOURCE,full_plan('cli',['persistent-data','backup-restore','writes-files'],extras))
