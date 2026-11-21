import {rpc,versions} from './protocol.mjs';
import {readBoundedBody,BodyError,BODY_LIMIT} from './body.mjs';
import {servePublicPage} from './public-pages.mjs';
const origins=new Set(['https://chatgpt.com','https://chat.openai.com','https://capability-builder.scaffolde.ai']);
const baseHeaders={'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer'};
export default {async fetch(request,env){
 const page=servePublicPage(request);if(page)return page;
 const url=new URL(request.url);
 if(url.pathname!=='/mcp')return new Response(null,{status:404,headers:baseHeaders});
 if(url.search)return new Response(null,{status:400,headers:baseHeaders});
 const origin=request.headers.get('origin');
 if(request.headers.has('origin')&&!origins.has(origin))return new Response(null,{status:403,headers:baseHeaders});
 const headers=origin?{...baseHeaders,'Access-Control-Allow-Origin':origin,Vary:'Origin'}:baseHeaders;
 if(request.method==='OPTIONS'){
  if(!origin||request.headers.get('access-control-request-method')!=='POST')return new Response(null,{status:403,headers});
  const allowed=new Set(['content-type','accept','mcp-protocol-version']);
  if((request.headers.get('access-control-request-headers')??'').split(',').filter(Boolean).some(h=>!allowed.has(h.trim().toLowerCase())))return new Response(null,{status:403,headers});
  return new Response(null,{status:204,headers:{...headers,'Access-Control-Allow-Methods':'POST','Access-Control-Allow-Headers':'Content-Type, Accept, MCP-Protocol-Version','Access-Control-Max-Age':'600'}});
 }
 if(request.method!=='POST')return new Response(null,{status:405,headers:{...headers,Allow:'POST, OPTIONS'}});
 const version=request.headers.get('mcp-protocol-version');
 if(version&&!versions.includes(version))return new Response(null,{status:400,headers});
 if(!/^application\/json(?:\s*;|$)/i.test(request.headers.get('content-type')??''))return new Response(null,{status:415,headers});
 if(request.headers.has('content-encoding')&&request.headers.get('content-encoding')!=='identity')return new Response(null,{status:415,headers});
 const length=request.headers.get('content-length');
 if(length&&(!/^\d+$/.test(length)||Number(length)>BODY_LIMIT))return new Response(null,{status:413,headers});
 // A service-only counter contains no client identifier or draft content.
 try{
  if(!env?.SERVICE_RATE_LIMITER?.limit)return new Response(null,{status:503,headers});
  const {success}=await env.SERVICE_RATE_LIMITER.limit({key:'capability-builder:post'});
  if(!success)return new Response(null,{status:429,headers:{...headers,'Retry-After':'60'}});
 }catch{return new Response(null,{status:503,headers});}
 try{
  const body=await readBoundedBody(request.body?.getReader());
  let message;try{message=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(body));}catch{return Response.json({jsonrpc:'2.0',id:null,error:{code:-32700,message:'Parse error'}},{status:400,headers});}
  const result=rpc(message);return result===null?new Response(null,{status:202,headers}):Response.json(result,{headers});
 }catch(e){return new Response(null,{status:e instanceof BodyError?(e.code==='BODY_TIMEOUT'?408:413):400,headers});}
}};
