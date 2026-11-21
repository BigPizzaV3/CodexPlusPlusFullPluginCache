#!/usr/bin/env node

// src/exec-worker.ts
import fs2 from "node:fs/promises";
import { createWriteStream } from "node:fs";
import path3 from "node:path";
import { spawn } from "node:child_process";

// src/util.ts
import fs from "node:fs/promises";
import { createHash, randomUUID } from "node:crypto";
import path from "node:path";
async function readJson(file2) {
  return JSON.parse(await fs.readFile(file2, "utf8"));
}
async function writeJson(file2, data) {
  await fs.mkdir(path.dirname(file2), { recursive: true });
  const temp = `${file2}.${randomUUID()}.tmp`;
  try {
    await fs.writeFile(temp, JSON.stringify(data, null, 2) + "\n");
    await fs.rename(temp, file2);
  } finally {
    await fs.rm(temp, { force: true });
  }
}
async function exists(file2) {
  return fs.stat(file2).then(() => true, () => false);
}

// src/core/windowsExecution.ts
import path2 from "node:path";
var WINDOWS_JOB_SCRIPT = String.raw`
$ErrorActionPreference = 'Stop'
$request = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($env:WANDEO_EXECUTION_REQUEST)) | ConvertFrom-Json
$env:WANDEO_EXECUTION_REQUEST = $null
Add-Type -TypeDefinition @'
using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Text;
public static class OOVideoProjectJob {
 [StructLayout(LayoutKind.Sequential)] struct STARTUPINFO {
  public int cb; public IntPtr reserved; public IntPtr desktop; public IntPtr title;
  public uint x,y,xSize,ySize,xCount,yCount,fill,flags; public ushort show,cbReserved;
  public IntPtr reserved2,stdin,stdout,stderr;
 }
 [StructLayout(LayoutKind.Sequential)] struct PROCESSINFO { public IntPtr process,thread; public uint pid,tid; }
 [StructLayout(LayoutKind.Sequential)] struct BASIC_LIMITS {
  public long processTime,jobTime; public uint flags; public UIntPtr minWorking,maxWorking;
  public uint activeProcesses; public UIntPtr affinity; public uint priority,scheduling;
 }
 [StructLayout(LayoutKind.Sequential)] struct IO_COUNTERS { public ulong a,b,c,d,e,f; }
 [StructLayout(LayoutKind.Sequential)] struct EXTENDED_LIMITS {
  public BASIC_LIMITS basic; public IO_COUNTERS io;
  public UIntPtr processMemory,jobMemory,peakProcess,peakJob;
 }
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)] static extern IntPtr CreateJobObjectW(IntPtr attr,string name);
 [DllImport("kernel32.dll", SetLastError=true)] static extern bool SetInformationJobObject(IntPtr job,int kind,ref EXTENDED_LIMITS info,int size);
 [DllImport("kernel32.dll", SetLastError=true)] static extern bool AssignProcessToJobObject(IntPtr job,IntPtr process);
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)] static extern bool CreateProcessW(string app,StringBuilder command,IntPtr pa,IntPtr ta,bool inherit,uint flags,IntPtr env,string cwd,ref STARTUPINFO si,out PROCESSINFO pi);
 [DllImport("kernel32.dll")] static extern IntPtr GetStdHandle(int kind);
 [DllImport("kernel32.dll")] static extern uint ResumeThread(IntPtr thread);
 [DllImport("kernel32.dll")] static extern uint WaitForSingleObject(IntPtr handle,uint ms);
 [DllImport("kernel32.dll")] static extern bool GetExitCodeProcess(IntPtr process,out uint code);
 [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr handle);
 [DllImport("kernel32.dll")] static extern bool TerminateProcess(IntPtr process,uint code);
 public static int Run(string command,string cwd) {
  var job=CreateJobObjectW(IntPtr.Zero,null);
  if(job==IntPtr.Zero) throw new Win32Exception();
  var pi=new PROCESSINFO();
  try {
   var limits=new EXTENDED_LIMITS(); limits.basic.flags=0x2000;
   if(!SetInformationJobObject(job,9,ref limits,Marshal.SizeOf(limits))) throw new Win32Exception();
   var si=new STARTUPINFO(); si.cb=Marshal.SizeOf(si); si.flags=0x100;
   si.stdin=GetStdHandle(-10); si.stdout=GetStdHandle(-11); si.stderr=GetStdHandle(-12);
   if(!CreateProcessW(null,new StringBuilder(command),IntPtr.Zero,IntPtr.Zero,true,0x08000004,IntPtr.Zero,cwd,ref si,out pi)) throw new Win32Exception();
   if(!AssignProcessToJobObject(job,pi.process)) { TerminateProcess(pi.process,1); throw new Win32Exception(); }
   if(ResumeThread(pi.thread)==0xffffffff) { TerminateProcess(pi.process,1); throw new Win32Exception(); }
   WaitForSingleObject(pi.process,0xffffffff);
   uint code; if(!GetExitCodeProcess(pi.process,out code)) throw new Win32Exception();
   return unchecked((int)code);
  } finally {
   if(pi.thread!=IntPtr.Zero) CloseHandle(pi.thread);
   if(pi.process!=IntPtr.Zero) CloseHandle(pi.process);
   CloseHandle(job);
  }
 }
}
'@
try { exit [OOVideoProjectJob]::Run($request.commandLine, $request.cwd) }
catch { [Console]::Error.WriteLine('Project process launch failed: ' + $_.Exception.Message); exit 1 }
`;
function quoteWindowsArgument(value) {
  return '"' + value.replace(/(\\*)"/g, '$1$1\\"').replace(/(\\+)$/g, "$1$1") + '"';
}
function windowsProjectLaunch(command, args, cwd) {
  return {
    executable: path2.join(
      process.env.SystemRoot ?? "C:\\Windows",
      "System32",
      "WindowsPowerShell",
      "v1.0",
      "powershell.exe"
    ),
    args: [
      "-NoProfile",
      "-NonInteractive",
      "-EncodedCommand",
      Buffer.from(WINDOWS_JOB_SCRIPT, "utf16le").toString("base64")
    ],
    payload: Buffer.from(
      JSON.stringify({
        commandLine: [command, ...args].map(quoteWindowsArgument).join(" "),
        cwd
      })
    ).toString("base64")
  };
}

// src/exec-worker.ts
var file = process.argv[2];
async function main() {
  const requestFile = file.replace(/\.json$/, ".request.json");
  const request = await readJson(requestFile);
  const env = {};
  for (const key of ["PATH", "SystemRoot", "SYSTEMROOT", "WINDIR", "COMSPEC", "PATHEXT", "LANG", "LC_ALL", "TMPDIR", "TMP", "TEMP"]) if (process.env[key]) env[key] = process.env[key];
  const environmentRoot = path3.join(request.workspace, ".wandeo-environment");
  await fs2.mkdir(environmentRoot, { recursive: true });
  await fs2.writeFile(path3.join(environmentRoot, "empty-config"), "");
  Object.assign(env, { ...request.env, PATH: [...request.binDirectories, path3.join(request.workspace, "node_modules", ".bin"), env.PATH || ""].join(path3.delimiter), npm_config_cache: path3.join(environmentRoot, "npm-cache"), npm_config_userconfig: path3.join(environmentRoot, "empty-config"), GIT_CONFIG_GLOBAL: path3.join(environmentRoot, "empty-config"), PIP_CACHE_DIR: path3.join(environmentRoot, "pip-cache") });
  const state = { ...request, env: void 0, workerPid: process.pid, status: "starting" };
  const log = createWriteStream(file.replace(/\.json$/, ".log"), { flags: "a" });
  const privateValues = Object.entries(request.env || {}).filter(([key]) => /token|secret|password|key/i.test(key)).map(([, value]) => String(value)).filter((value) => value.length > 3);
  let logBytes = 0;
  const record = (data) => {
    if (logBytes >= 2 * 1024 ** 2) return;
    let text = data.toString("utf8");
    for (const value of privateValues) text = text.replaceAll(value, "[redacted]");
    logBytes += Buffer.byteLength(text);
    log.write(text);
  };
  const requestedCommand = request.command;
  let command = requestedCommand, args = request.args || [], windowsPayload;
  if (process.platform === "win32" && /^(npm|npx)(\.cmd)?$/i.test(path3.basename(command))) {
    const cliName = /^npx/i.test(path3.basename(command)) ? "npx-cli.js" : "npm-cli.js";
    const directories = [...path3.isAbsolute(command) ? [path3.dirname(command)] : [], ...(env.PATH || "").split(path3.delimiter), path3.dirname(process.execPath)];
    let found, npmNode = process.execPath;
    for (const directory of directories) {
      const candidate = path3.join(directory, "node_modules", "npm", "bin", cliName);
      if (await exists(candidate)) {
        found = candidate;
        if (await exists(path3.join(directory, "node.exe"))) npmNode = path3.join(directory, "node.exe");
        break;
      }
    }
    if (!found) throw new Error("npm CLI is missing; prepare a portable Node runtime or use its absolute npm-cli.js path.");
    args = [found, ...args];
    command = npmNode;
  }
  const directNodeCommand = process.platform === "win32" && /(?:^|[\\/])node(?:\.exe)?$/i.test(command);
  if (process.platform === "win32" && !directNodeCommand) {
    const launch = windowsProjectLaunch(command, args, request.cwd);
    command = launch.executable;
    args = launch.args;
    windowsPayload = launch.payload;
  }
  const child = spawn(command, args, { cwd: request.cwd, env: { ...env, ...windowsPayload ? { WANDEO_EXECUTION_REQUEST: windowsPayload } : {} }, windowsHide: true, detached: process.platform !== "win32", stdio: ["ignore", "pipe", "pipe"] });
  child.stdout.on("data", record);
  child.stderr.on("data", record);
  const completion = new Promise((resolve) => {
    let settled = false;
    const finish = (result2) => {
      if (!settled) {
        settled = true;
        resolve(result2);
      }
    };
    let exitFallback;
    child.once("error", (error) => finish({ error: error.message }));
    child.once("close", (code, signal) => finish({ code, signal }));
    child.once("exit", (code, signal) => {
      exitFallback = setTimeout(() => {
        if (settled) return;
        child.stdout.destroy();
        child.stderr.destroy();
        finish({ code, signal });
      }, 500);
    });
    child.once("close", () => {
      if (exitFallback) clearTimeout(exitFallback);
    });
  });
  state.pid = child.pid;
  state.status = "running";
  await writeJson(file, state);
  let stopping = false, forceTimer;
  const stop = () => {
    if (stopping) return;
    stopping = true;
    if (child.pid) {
      if (process.platform === "win32") {
        try {
          child.kill();
        } catch {
        }
        spawn("taskkill", ["/PID", String(child.pid), "/T", "/F"], { stdio: "ignore", windowsHide: true });
      } else {
        try {
          process.kill(-child.pid, "SIGTERM");
        } catch {
        }
        forceTimer = setTimeout(() => {
          try {
            process.kill(-child.pid, "SIGKILL");
          } catch {
          }
        }, 3e3);
      }
    }
  };
  process.on("SIGTERM", stop);
  process.on("SIGINT", stop);
  const timer = setInterval(() => {
    void exists(file.replace(/\.json$/, ".stop")).then((value) => {
      if (value) stop();
    });
  }, 150);
  const result = await completion;
  state.exitCode = result.code;
  state.signal = result.signal;
  state.error = result.error;
  state.status = stopping ? "cancelled" : !result.error && result.code === 0 ? "succeeded" : "failed";
  clearInterval(timer);
  if (forceTimer) clearTimeout(forceTimer);
  if (process.platform !== "win32" && child.pid) {
    try {
      process.kill(-child.pid, "SIGKILL");
    } catch {
    }
  }
  await new Promise((resolve) => log.end(() => resolve()));
  state.finishedAt = (/* @__PURE__ */ new Date()).toISOString();
  await writeJson(file, state);
  await fs2.rm(requestFile, { force: true });
}
main().catch(async (error) => {
  const previous = await readJson(file).catch(() => ({}));
  await writeJson(file, { ...previous, env: void 0, workerPid: process.pid, status: "failed", error: error.message, finishedAt: (/* @__PURE__ */ new Date()).toISOString() });
  process.exitCode = 1;
});
