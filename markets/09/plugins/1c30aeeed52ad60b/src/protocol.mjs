import {call,tools,InputError} from './core.mjs';
export const versions=['2025-11-25','2025-06-18'];
export function rpc(message){
 if(!message||message.jsonrpc!=='2.0'||typeof message.method!=='string'||(message.id!==undefined&&typeof message.id!=='string'&&!Number.isInteger(message.id)))return {jsonrpc:'2.0',id:null,error:{code:-32600,message:'Invalid request'}};
 if(message.id===undefined)return null;
 const reply=result=>({jsonrpc:'2.0',id:message.id,result});
 const invalid=()=>({jsonrpc:'2.0',id:message.id,error:{code:-32602,message:'Invalid params'}});
 const obj=v=>v!==null&&typeof v==='object'&&!Array.isArray(v);
 if(message.params!==undefined&&!obj(message.params))return invalid();
 if(message.method==='initialize'){
  const p=message.params;if(!obj(p)||typeof p.protocolVersion!=='string'||!obj(p.capabilities)||!obj(p.clientInfo)||typeof p.clientInfo.name!=='string'||typeof p.clientInfo.version!=='string')return invalid();
  return reply({protocolVersion:versions.includes(p.protocolVersion)?p.protocolVersion:versions[0],capabilities:{tools:{}},serverInfo:{name:'scaffolde-capability-builder',version:'0.1.3'}});
 }
 if(message.method==='ping')return reply({});
 if(message.method==='tools/list')return reply({tools});
 if(message.method==='tools/call'){
  if(!obj(message.params)||typeof message.params.name!=='string'||(message.params.arguments!==undefined&&!obj(message.params.arguments)))return invalid();
  try{const result=call(message.params?.name,message.params?.arguments??{});return reply({content:[{type:'text',text:JSON.stringify(result)}],structuredContent:result,isError:false});}
  catch(e){if(e instanceof InputError&&e.code==='UNKNOWN_TOOL')return invalid();return reply({content:[{type:'text',text:JSON.stringify({code:e instanceof InputError?e.code:'INTERNAL_ERROR',message:e instanceof InputError?e.message:'Unable to process request'})}],isError:true});}
 }
 return {jsonrpc:'2.0',id:message.id,error:{code:-32601,message:'Method not found'}};
}
