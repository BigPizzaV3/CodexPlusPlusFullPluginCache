import { cp, mkdir, readFile, writeFile, access } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFile, spawn } from 'node:child_process';
import { promisify } from 'node:util';
import { createHash } from 'node:crypto';

const exec = promisify(execFile);
const [repoArg, outputArg, packagesArg] = process.argv.slice(2);
if (process.platform !== 'darwin' || !repoArg || !outputArg) throw new Error('Usage on macOS: node scripts/setup-native-renderer.mjs /path/to/CarouselKit /path/to/runtime [cached SourcePackages]');
const repo = resolve(repoArg), output = resolve(outputArg);
const staging = join(output, 'source'), derived = join(output, 'build');
const project = join(staging, 'CarouselKit.xcodeproj');
const bundleId = 'software.quokka.ace-plugin-renderer';
await access(join(repo, 'CarouselKit/Sources/Services/SlideRasterizer.swift'));
await mkdir(staging, { recursive: true });
// A private build snapshot: never alter the user's app, project or simulator install.
await cp(join(repo, 'CarouselKit'), join(staging, 'CarouselKit'), { recursive: true, filter: path => !path.endsWith('GoogleService-Info.plist') });
await cp(join(repo, 'CarouselKit.xcodeproj'), project, { recursive: true, filter: path => !path.includes('xcuserdata') });
await cp(new URL('../native/RendererApp.swift', import.meta.url), join(staging, 'CarouselKit/Sources/CarouselKitApp.swift'));
const args = ['-project', project, '-scheme', 'CarouselKit', '-configuration', 'Debug', '-sdk', 'iphonesimulator', '-destination', 'generic/platform=iOS Simulator', '-derivedDataPath', derived, 'CODE_SIGNING_ALLOWED=NO', `PRODUCT_BUNDLE_IDENTIFIER=${bundleId}`, 'INFOPLIST_KEY_CFBundleDisplayName=ACE Renderer', 'build'];
if (packagesArg) args.unshift('-clonedSourcePackagesDirPath', resolve(packagesArg), '-disableAutomaticPackageResolution', '-skipPackageUpdates');
console.log('Building ACE native preview worker…');
await new Promise((resolve, reject) => {
  const process = spawn('/usr/bin/xcodebuild', args, { stdio: 'inherit' });
  process.once('error', reject);
  process.once('exit', code => code === 0 ? resolve() : reject(new Error(`xcodebuild exited ${code}`)));
});
const app = join(derived, 'Build/Products/Debug-iphonesimulator/CarouselKit.app');
await access(app);
const { stdout } = await exec('/usr/bin/xcrun', ['simctl', 'list', 'devices', 'available', '-j']);
const devices = JSON.parse(stdout).devices;
let device = Object.values(devices).flat().find(device => device.name === 'ACE Plugin Renderer');
if (!device) {
  const runtimes = JSON.parse((await exec('/usr/bin/xcrun', ['simctl', 'list', 'runtimes', '-j'], { maxBuffer: 2 * 1024 * 1024 })).stdout).runtimes
    .filter(runtime => runtime.isAvailable && runtime.identifier.includes('.iOS-'))
    .sort((a, b) => b.version.localeCompare(a.version, undefined, { numeric: true }));
  if (!runtimes.length) throw new Error('Install an iOS Simulator runtime in Xcode first');
  const type = runtimes[0].supportedDeviceTypes.find(type => type.productFamily === 'iPhone');
  if (!type) throw new Error('No iPhone device type is available');
  const created = await exec('/usr/bin/xcrun', ['simctl', 'create', 'ACE Plugin Renderer', type.identifier, runtimes[0].identifier]);
  device = { udid: created.stdout.trim(), state: 'Shutdown' };
}
if (device.state !== 'Booted') await exec('/usr/bin/xcrun', ['simctl', 'boot', device.udid]);
await exec('/usr/bin/xcrun', ['simctl', 'bootstatus', device.udid, '-b'], { timeout: 180_000 });
await exec('/usr/bin/xcrun', ['simctl', 'install', device.udid, app], { timeout: 120_000 });
const hash = createHash('sha256').update(await readFile(join(repo, 'CarouselKit/Sources/Services/SlideRasterizer.swift'))).digest('hex');
const configuration = { protocol: 1, engine: 'ACE SlideRasterizer', device: device.udid, bundleId, app, rasterizer_sha256: hash, built_at: new Date().toISOString() };
const config = join(output, 'renderer.json');
await writeFile(config, JSON.stringify(configuration, null, 2) + '\n');
console.log(JSON.stringify({ configuration: config, environment: { CAROUSEL_RENDERER_CONFIG: config } }, null, 2));
