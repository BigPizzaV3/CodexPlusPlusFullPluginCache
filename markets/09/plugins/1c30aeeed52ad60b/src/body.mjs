export const BODY_LIMIT=65536;
export const BODY_TIMEOUT_MS=10000;
export class BodyError extends Error {constructor(code){super(code);this.code=code;}}
export async function readBoundedBody(reader,timeoutMs=BODY_TIMEOUT_MS){
 if(!reader)return new Uint8Array();
 let timer;
 const deadline=new Promise((_,reject)=>{timer=setTimeout(()=>reject(new BodyError('BODY_TIMEOUT')),timeoutMs);});
 let bytes=0;const chunks=[];
 try{
  while(true){const {done,value}=await Promise.race([reader.read(),deadline]);if(done)break;bytes+=value.byteLength;if(bytes>BODY_LIMIT)throw new BodyError('BODY_TOO_LARGE');chunks.push(value);}
  const body=new Uint8Array(bytes);let offset=0;for(const c of chunks){body.set(c,offset);offset+=c.byteLength;}return body;
 }catch(e){reader.cancel().catch(()=>{});throw e;}finally{clearTimeout(timer);reader.releaseLock();}
}
