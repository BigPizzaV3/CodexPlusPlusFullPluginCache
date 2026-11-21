#!/usr/bin/env node
import { options } from './options.mjs';

try {
  const [command, ...argv] = process.argv.slice(2);
  if (command === 'setup' || command === 'preflight') {
    if (argv.length) throw new Error(`${command} does not accept options`);
    const { setup } = await import('./setup.mjs');
    const report = await setup({ install: command === 'setup' });
    console.log(JSON.stringify(report, null, 2));
    if (!report.ok) process.exitCode = 1;
  } else if (command === 'prepare') {
    const { prepare } = await import('./pwaify.mjs');
    console.log(JSON.stringify(await prepare(options(argv, ['dist', 'out', 'name', 'assets', 'theme'])), null, 2));
  } else if (command === 'preview') {
    const { preview } = await import('./preview.mjs');
    await preview(options(argv, ['dir', 'port', 'qr', 'lan-address']));
  } else if (command === 'verify') {
    const { verify } = await import('./verify.mjs');
    const report = await verify(options(argv, ['url', 'expect-text', 'report', 'screenshot']));
    console.log(JSON.stringify(report, null, 2));
    if (!report.ok) process.exitCode = 1;
  } else {
    console.log('Device It: local static PWA preparation and preview\n\npreflight (read-only readiness check)\nsetup (install missing locked dependencies and matching Chromium)\nprepare --dist BUILT_DIR --out NEW_DIR --assets PUBLIC_FILES.json --name NAME\npreview --dir PREPARED_DIR --qr NEW_QR.png [--port 0] [--lan-address LOCAL_IPV4]\nverify --url http://127.0.0.1:PORT/ --expect-text VISIBLE_TEXT [--report NEW.json] [--screenshot NEW.png]\n\nRequires local Node 22+ and npm. Start with FIRST-RUN.md.');
    if (command && !['help', '--help'].includes(command)) process.exitCode = 1;
  }
} catch (error) {
  console.error(`device-it: ${error.message}`);
  process.exitCode = 1;
}
