import templates from './templates.json' with {type:'json'};
const text={type:'string',minLength:1,maxLength:2000};
const array={type:'array',minItems:1,maxItems:32,items:text};
const object=(properties)=>({type:'object',additionalProperties:false,required:Object.keys(properties),properties});
export const draftSchema=object({name:{...text,maxLength:80},goal:{...text,maxLength:4000},trigger:text,inputs:array,outputs:array,steps:array,constraints:array,nonGoals:array,claims:{type:'array',minItems:1,maxItems:32,items:object({id:{type:'string',pattern:'^C-[A-Za-z0-9-]{1,32}$',maxLength:34},statement:text,probe:text})},evidencePlan:{type:'array',minItems:1,maxItems:32,items:object({claimId:{type:'string',pattern:'^C-[A-Za-z0-9-]{1,32}$',maxLength:34},method:text})}});
export class InputError extends Error { constructor(code,message){super(message);this.code=code;} }
function check(value,s,path='arguments',errors=[]){
 if(s.type==='object'){
  if(!value||typeof value!=='object'||Array.isArray(value)){errors.push(`${path}: expected object`);return errors;}
  for(const k of Object.keys(value))if(!Object.hasOwn(s.properties,k))errors.push(`${path}: unknown field`);
  for(const k of s.required)if(!Object.hasOwn(value,k))errors.push(`${path}.${k}: required`);
  for(const [k,v]of Object.entries(s.properties))if(Object.hasOwn(value,k))check(value[k],v,`${path}.${k}`,errors);
 }else if(s.type==='array'){
  if(!Array.isArray(value)){errors.push(`${path}: expected array`);return errors;}
  if(value.length<s.minItems||value.length>s.maxItems)errors.push(`${path}: invalid item count`);
  value.slice(0,s.maxItems).forEach((v,i)=>check(v,s.items,`${path}[${i}]`,errors));
 }else if(s.type==='string'){
  if(typeof value!=='string'){errors.push(`${path}: expected string`);return errors;}
  if(!value.trim()||value.length<(s.minLength??1)||value.length>s.maxLength)errors.push(`${path}: invalid text length`);
  if(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f\u202a-\u202e\u2066-\u2069]/u.test(value))errors.push(`${path}: unsupported control character`);
  if(s.pattern&&!new RegExp(s.pattern).test(value))errors.push(`${path}: invalid identifier`);
 }
 return errors;
}
const annotations={readOnlyHint:true,destructiveHint:false,idempotentHint:true,openWorldHint:false};
export const tools=[
 ['list_capability_templates','List the bounded public capability template snapshot.',object({})],
 ['get_capability_template','Get one public capability template by ID.',object({id:{type:'string',minLength:1,maxLength:40}})],
 ['validate_capability_draft','Check draft structure and claim references. Does not test runtime behavior.',object({draft:draftSchema})],
 ['render_capability_draft','Render a structurally valid draft as inert Markdown. Does not execute it.',object({draft:draftSchema})]
].map(([name,description,inputSchema])=>({name,description,inputSchema,annotations:{...annotations},_meta:{securitySchemes:[{type:'noauth'}]}}));
export function validate(draft){
 const errors=check(draft,draftSchema,'draft');
 if(!errors.length){
  const ids=draft.claims.map(c=>c.id);
  if(new Set(ids).size!==ids.length)errors.push('claims: duplicate stable ID');
  const refs=draft.evidencePlan.map(e=>e.claimId);
  if(refs.some(id=>!ids.includes(id)))errors.push('evidencePlan: unknown claim reference');
  if(ids.some(id=>!refs.includes(id)))errors.push('evidencePlan: every claim requires a method');
 }
 return {structural_pass:errors.length===0,needs_review:true,not_runtime_tested:true,errors,reviewNotes:['Human review must assess scope, instructions, permissions, and evidence quality.','No runtime probe or capability execution was performed.']};
}
// Encode Markdown punctuation/HTML as numeric entities; preserve raw goal separately.
const escape=s=>s.replace(/[&<>\\`*_{}\[\]()#+.!|~\-]/g,c=>`&#${c.codePointAt(0)};`).replace(/\r\n?/g,'\n').replace(/\n/g,'\n> ');
export function render(d){
 const result=validate(d);if(!result.structural_pass)throw new InputError('INVALID_DRAFT',result.errors.join('; '));
 const sections=[['Goal',d.goal],['Trigger',d.trigger],...['inputs','outputs','steps','constraints','nonGoals'].map(k=>[k,d[k].join('\n')]),['Claims',d.claims.map(c=>`${c.id}: ${c.statement}\nProbe: ${c.probe}`).join('\n')],['Evidence plan',d.evidencePlan.map(e=>`${e.claimId}: ${e.method}`).join('\n')]];
 return {...result,goal:d.goal,markdown:`# ${escape(d.name)}\n\nStructural pass. Needs review. Not runtime tested.\n\n`+sections.map(([h,v])=>`## ${h}\n\n> ${escape(v)}\n`).join('\n')};
}
export function call(name,args){
 const tool=tools.find(t=>t.name===name);if(!tool)throw new InputError('UNKNOWN_TOOL','Unknown operation');
 if(new TextEncoder().encode(JSON.stringify(args??null)).byteLength>65536)throw new InputError('INPUT_TOO_LARGE','Input exceeds 65536 bytes');
 const errors=check(args,tool.inputSchema);if(errors.length)throw new InputError('INVALID_INPUT',errors.slice(0,12).join('; '));
 if(name==='list_capability_templates')return {snapshotVersion:'1',templates:templates.map(({id,name,description})=>({id,name,description}))};
 if(name==='get_capability_template'){const t=templates.find(t=>t.id===args.id);if(!t)throw new InputError('TEMPLATE_NOT_FOUND','Unknown public template ID');return structuredClone(t);}
 if(name==='validate_capability_draft')return validate(args.draft);
 return render(args.draft);
}
