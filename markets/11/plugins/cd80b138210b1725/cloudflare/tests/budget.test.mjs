import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { planContextBudget, BudgetInputError } from '../build/budget.mjs';
import { planRemoteBudget } from '../build/remote-budget.mjs';

test('remote budget accepts scalar growth only, not any past-turn array or context record',()=>{
  const result=planRemoteBudget({reference_limit_tokens:100000,used_tokens:65000,growth_per_turn_tokens:10000,
    sources:{growth_per_turn_tokens:'assumed'}});
  assert.equal(result.growth.turns_until_reference,4);
  assert.deepEqual(result.growth.forecast.map(row=>row.budget.used_tokens),[75000,85000,95000,105000,115000]);
  assert.equal(result.sources.growth_per_turn_tokens,'assumed');
  assert.ok(!('recent_turn_tokens' in result.inputs));
  for(const input of [{recent_turn_tokens:[45000,55000,65000]},{growth_per_turn_tokens:1.5},
    {sources:{growth_per_turn_tokens:'assumed'}},{growth_per_turn_tokens:'PRIVATE_SENTINEL'}])assert.throws(()=>planRemoteBudget(input),
      error=>error.constructor.name==='BudgetInputError'&&!error.message.includes('PRIVATE_SENTINEL'));
});

test('current, task and reserve are separate; unknown is not zero', () => {
  const result = planContextBudget({reference_limit_tokens:100000,used_tokens:65000,
    planned_increase_tokens:20000,reserved_output_tokens:5000});
  assert.equal(result.current.remaining_tokens,35000);
  assert.equal(result.plan.after.used_tokens,90000);
  assert.equal(result.plan.after.remaining_tokens,10000);
  assert.equal(result.plan.fits_reference,true);
  assert.equal(planContextBudget({used_tokens:65000}).plan.added_tokens,null);
  assert.equal(planContextBudget({used_tokens:65000}).current.weather,'Unknown');
});
test('zero growth, fractional forecasts, reset and exact weather boundaries', () => {
  for(const [used,weather] of [[34,'Clear'],[35,'Fair'],[55,'Cloudy'],[70,'Showers'],[85,'Storm']])
    assert.equal(planContextBudget({reference_limit_tokens:100,used_tokens:used}).current.weather,weather);
  const flat=planContextBudget({reference_limit_tokens:100,used_tokens:10,recent_turn_tokens:[10,10,10]});
  assert.equal(flat.growth.tokens_per_turn,0); assert.equal(flat.growth.turns_until_reference,null);
  assert.equal(flat.growth.forecast.length,5);
  const reset=planContextBudget({reference_limit_tokens:100,used_tokens:30,recent_turn_tokens:[80,90,10,20,30]});
  assert.equal(reset.growth.tokens_per_turn,10); assert.equal(reset.growth.intervals,2);
  assert.deepEqual(reset.notices,['recent_decrease_resets_growth']);
});
test('only bounded numeric fields and fixed source enums are accepted; errors do not echo private values', () => {
  for(const input of [{messages:'PRIVATE_SENTINEL'},{thread_id:'PRIVATE_SENTINEL'}, {used_tokens:true},
    {used_tokens:-1},{used_tokens:1.5},{used_tokens:NaN},{used_tokens:Infinity},{reference_limit_tokens:0},
    {used_tokens:1e12+1},{recent_turn_tokens:[1,2,3,4,5,6,7]},
    {used_tokens:4,recent_turn_tokens:[1,2,3]},{sources:{used_tokens:'assumed'}},
    {used_tokens:10,sources:{used_tokens:'PRIVATE_SENTINEL'}}]) {
    assert.throws(()=>planContextBudget(input), error=>error instanceof BudgetInputError && !error.message.includes('PRIVATE_SENTINEL'));
  }
});
test('TypeScript matches the preserved Python Fraction calculator across deterministic scenarios', () => {
  const reference=fileURLToPath(new URL('../reference/budget.py',import.meta.url));
  const cases=[{}, {used_tokens:65000}, {reference_limit_tokens:1,used_tokens:1e12,
    planned_increase_tokens:1e12,reserved_output_tokens:1e12}];
  let seed=42;
  const random=max=>{ seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%max; };
  for(let index=0;index<180;index++) {
    const history=Array.from({length:3+random(4)},()=>random(100000));
    cases.push({reference_limit_tokens:1+random(100000),used_tokens:history.at(-1),
      recent_turn_tokens:history,planned_increase_tokens:random(50000),reserved_output_tokens:random(10000),
      sources:{used_tokens:'supplied_measurement',planned_increase_tokens:'assumed'}});
  }
  const python=spawnSync(process.env.TOKEN_WEATHER_TEST_PYTHON??'python3',['-B','-c',
    'import importlib.util,json,sys;s=importlib.util.spec_from_file_location("budget",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(json.dumps([m.plan_context_budget(x) for x in json.load(sys.stdin)]))',reference],
    {input:JSON.stringify(cases),encoding:'utf8'});
  assert.equal(python.status,0,python.stderr);
  const expected=JSON.parse(python.stdout);
  function compare(actual,wanted) {
    if(typeof wanted==='number') assert.ok(Math.abs(actual-wanted)<=Math.max(1,Math.abs(wanted))*1e-14,`${actual} != ${wanted}`);
    else if(Array.isArray(wanted)) {assert.equal(actual.length,wanted.length);wanted.forEach((item,index)=>compare(actual[index],item));}
    else if(wanted&&typeof wanted==='object') {assert.deepEqual(Object.keys(actual).sort(),Object.keys(wanted).sort());for(const key of Object.keys(wanted))compare(actual[key],wanted[key]);}
    else assert.equal(actual,wanted);
  }
  cases.forEach((input,index)=>compare(planContextBudget(input),expected[index]));
});
