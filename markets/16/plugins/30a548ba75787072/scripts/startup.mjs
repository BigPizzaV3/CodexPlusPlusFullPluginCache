import fs from 'node:fs/promises';
import path from 'node:path';

export async function startupSettings(base){
 try{return JSON.parse(await fs.readFile(path.join(base,'startup.json'),'utf8'));}
 catch(e){if(e.code==='ENOENT')return {enabled:false,paused:false};throw e;}
}
export async function pauseStartup(base,paused){
 const settings=await startupSettings(base);
 if(settings.enabled)await fs.writeFile(path.join(base,'startup.json'),JSON.stringify({...settings,paused}));
}
export async function configureStartup(root,base,enabled){
 if(process.platform!=='win32')throw Error('Automatic startup is currently supported on Windows only.');
 if(!process.env.APPDATA)throw Error('Windows application-data folder is unavailable.');
 const folder=path.join(process.env.APPDATA,'Microsoft','Windows','Start Menu','Programs','Startup');
 const launcher=path.join(folder,'Pace Plugin.vbs');
 await fs.mkdir(base,{recursive:true});
 if(!enabled){
  await fs.writeFile(path.join(base,'startup.json'),JSON.stringify({enabled:false,paused:false}));
  try{await fs.unlink(launcher);}catch(e){if(e.code!=='ENOENT')throw e;}
  return {startupEnabled:false};
 }
 // Keep a stable, versioned runtime outside the plugin cache. History is separate.
 const bundle=path.join(base,'installed','0.2.1');
 for(const name of ['scripts','lib','web'])await fs.cp(path.join(root,name),path.join(bundle,name),{recursive:true});
 const script=path.join(bundle,'scripts','pace.mjs');
 const quoted=s=>'"'+s.replaceAll('"','""')+'"';
 const command='"'+process.execPath+'" "'+script+'" resume-startup';
 const vbs=['Set sh = CreateObject("WScript.Shell")',
  'sh.Environment("PROCESS")("PACE_DATA_DIR") = '+quoted(base),
  'sh.Run '+quoted(command)+', 0, False'].join('\r\n');
 await fs.mkdir(folder,{recursive:true});
 await fs.writeFile(launcher,Buffer.from('\ufeff'+vbs,'utf16le'));
 await fs.writeFile(path.join(base,'startup.json'),JSON.stringify({enabled:true,paused:false,script}));
 return {startupEnabled:true,script};
}
