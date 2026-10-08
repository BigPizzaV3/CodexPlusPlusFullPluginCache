// packages/remotion-kit/scripts/stills.mjs
// One still per beat (at the 0.5 mark) of every fixture, to out/stills/<fixture>/<n>-<beat>-<t>.png.
// Set STILLS_ALL=1 to render three per beat (0.15, 0.5, 0.9); the default keeps the run short.
// Reviewed by eye before a kit PR opens (.claude/skills/verify-ui/SKILL.md): jsdom cannot see any of this.
import { execFileSync } from 'node:child_process'
import { mkdirSync, readdirSync, readFileSync } from 'node:fs'
import { join } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('..', import.meta.url))
const marks = process.env.STILLS_ALL === '1' ? [0.15, 0.5, 0.9] : [0.5]
const fixtures = readdirSync(join(root, 'src/fixtures')).filter((f) => f.endsWith('.json'))
for (const file of fixtures) {
  const name = file.replace('.json', '')
  const props = JSON.parse(readFileSync(join(root, 'src/fixtures', file), 'utf8'))
  const dir = join(root, 'out/stills', name)
  mkdirSync(dir, { recursive: true })
  props.spec.beats.forEach((beat, index) => {
    const len = beat.end - beat.start
    for (const at of marks) {
      const frame = Math.round((beat.start + len * at) * 30)
      const out = join(dir, `${String(index + 1).padStart(2, '0')}-${beat.type}-${at}.png`)
      execFileSync('npx', ['remotion', 'still', 'src/index.ts', 'AdComposition', out, `--props=${join(root, 'src/fixtures', file)}`, `--frame=${frame}`], { cwd: root, stdio: 'inherit' })
    }
  })
}
