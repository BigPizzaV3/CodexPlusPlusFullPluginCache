import net from 'node:net';
import {spawn} from 'node:child_process';
import {resolve} from 'node:path';

// A development source archive is wired to this exact loopback URL. Never
// silently switch ports, take over a listener or stop another project.
const probe=net.createServer();
try {
  await new Promise((accept,reject)=>{
    probe.once('error',reject);
    probe.listen(8787,'127.0.0.1',accept);
  });
  await new Promise((accept,reject)=>probe.close(error=>error?reject(error):accept()));
} catch {
  console.error('Port 8787 is in use or unavailable. No server was started. Keep the existing service; use matching config/MCP URLs for a separately chosen free port.');
  process.exit(2);
}
const child=spawn(process.execPath,[resolve('node_modules/wrangler/bin/wrangler.js'),'dev','--local','--ip','127.0.0.1','--port','8787'],
  {stdio:'inherit',env:{...process.env,WRANGLER_SEND_METRICS:'false'}});
process.on('SIGINT',()=>child.kill('SIGINT'));
process.on('SIGTERM',()=>child.kill('SIGTERM'));
child.on('error',()=>{console.error('Local runtime could not start. No deployment was attempted.');process.exitCode=2;});
child.on('exit',(code,signal)=>{process.exitCode=code??(signal?130:0);});
