import {createServer} from 'node:http';
import {pathToFileURL} from 'node:url';
import {rpc,versions} from './protocol.mjs';
import {BODY_LIMIT,BODY_TIMEOUT_MS} from './body.mjs';
export {rpc} from './protocol.mjs';
export function start(port=8787){
 const server=createServer(async(req,res)=>{
  res.setHeader('Cache-Control','no-store');
  if(req.url!=='/mcp'){res.writeHead(404).end();return;}
  if(req.method!=='POST'){res.writeHead(405,{Allow:'POST'}).end();return;}
  if(req.headers['mcp-protocol-version']&&!versions.includes(req.headers['mcp-protocol-version'])){res.writeHead(400).end();return;}
  if(req.headers.origin){res.writeHead(403).end();return;}
  if(!req.headers['content-type']?.includes('application/json')){res.writeHead(415).end();return;}
  const bodyTimer=setTimeout(()=>{if(!res.headersSent)res.writeHead(408).end();req.destroy();},BODY_TIMEOUT_MS);
  try{
   let size=0;const chunks=[];for await(const c of req){size+=c.length;if(size>BODY_LIMIT){res.writeHead(413).end();return;}chunks.push(c);}
   let m;try{m=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(Buffer.concat(chunks)));}catch{res.writeHead(400,{'Content-Type':'application/json'}).end(JSON.stringify({jsonrpc:'2.0',id:null,error:{code:-32700,message:'Parse error'}}));return;}
   const result=rpc(m);if(result===null){res.writeHead(202).end();return;}
   res.writeHead(200,{'Content-Type':'application/json'}).end(JSON.stringify(result));
  }catch{if(!res.headersSent)res.writeHead(400).end();}finally{clearTimeout(bodyTimer);}
 });
 server.requestTimeout=10000;server.headersTimeout=10000;server.listen(port,'127.0.0.1');return server;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href)start();
