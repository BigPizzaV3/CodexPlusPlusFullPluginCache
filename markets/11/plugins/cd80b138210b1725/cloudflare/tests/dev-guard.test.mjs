import test from 'node:test';
import assert from 'node:assert/strict';
import net from 'node:net';
import {spawnSync} from 'node:child_process';

test('local start refuses an occupied port without stopping or replacing its listener',async()=>{
  const listener=net.createServer(socket=>socket.end());
  let owned=false;
  try{
    try{await new Promise((accept,reject)=>{listener.once('error',reject);listener.listen(8787,'127.0.0.1',accept);});owned=true;}
    catch(error){if(error.code!=='EADDRINUSE')throw error;}
    const result=spawnSync(process.execPath,['scripts/dev-local.mjs'],{encoding:'utf8',timeout:10000});
    assert.equal(result.status,2,result.stderr);
    assert.ok(result.stderr.includes('No server was started'));
    assert.ok(!result.stdout.includes('Ready on'));
    if(owned)assert.ok(listener.listening);
  }finally{if(owned)await new Promise(accept=>listener.close(accept));}
});
