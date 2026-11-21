#!/usr/bin/env node
import { readFile, open, rm, stat } from 'node:fs/promises'
import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

export function transferUrl(grant, direction) {
  const url = new URL(direction === 'upload' ? grant.upload_url : grant.url)
  const prefix = direction === 'upload' ? '/storage/v1/object/upload/sign/templates/' : '/storage/v1/object/sign/mcp-exports/'
  if (url.protocol !== 'https:' || url.username || url.password || !url.pathname.startsWith(prefix) || !url.searchParams.has('token')) throw new Error('Expected the signed Storage URL returned by Paul')
  if (!Number.isFinite(Date.parse(grant.expires_at)) || Date.parse(grant.expires_at) <= Date.now()) throw new Error('Transfer link expired; request a new one from Paul')
  return url
}
export async function transfer(direction, grant, filePath) {
  if (!['upload', 'download'].includes(direction)) throw new Error('Use upload or download')
  if (grant.isError) throw new Error('Paul did not authorize this transfer')
  // Clients may save either structured data or the complete MCP tool result.
  if (grant.structuredContent) grant = grant.structuredContent
  else if (Array.isArray(grant.content)) {
    const result = grant.content.find(item => item.type === 'text')
    if (!result) throw new Error('No transfer grant in the Paul result')
    grant = JSON.parse(result.text)
  }
  const url = transferUrl(grant, direction)
  if (direction === 'upload') {
    const info = await stat(filePath)
    if (!info.isFile() || info.size > 30 * 1024 * 1024) throw new Error('Expected a PPTX no larger than 30 MB')
    const bytes = await readFile(filePath)
    if (!filePath.toLowerCase().endsWith('.pptx') || bytes.length < 4 || bytes.length > 30 * 1024 * 1024 || bytes[0] !== 0x50 || bytes[1] !== 0x4b) throw new Error('Expected a PPTX no larger than 30 MB')
    const response = await fetch(url, { method: 'PUT', body: bytes, redirect: 'error', signal: AbortSignal.timeout(120_000), headers: { 'Content-Type': 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'x-upsert': 'false' } })
    if (!response.ok) throw new Error(`Upload failed (${response.status}); do not finish the import yet`)
    return { uploaded: true, template_id: grant.template_id, next: 'Call paul_finish_import' }
  }
  const response = await fetch(url, { redirect: 'error', signal: AbortSignal.timeout(120_000) })
  if (!response.ok || !response.body) throw new Error(`Download failed (${response.status})`)
  const file = await open(filePath, 'wx', 0o600)
  let bytes = 0
  try {
    for await (const chunk of response.body) {
      bytes += chunk.byteLength
      if (bytes > 50 * 1024 * 1024) throw new Error('Export exceeds 50 MB')
      await file.writeFile(chunk)
    }
  } catch (error) { await file.close(); await rm(filePath, { force: true }); throw error }
  await file.close()
  return { downloaded: true, bytes, path: resolve(filePath) }
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [direction, grantPath, filePath] = process.argv.slice(2)
  try {
    if (!direction || !grantPath || !filePath) throw new Error('Usage: node transfer.mjs upload|download GRANT_JSON FILE.pptx')
    console.log(JSON.stringify(await transfer(direction, JSON.parse(await readFile(grantPath, 'utf8')), filePath)))
  } catch (error) { console.error(error.message); process.exitCode = 1 }
}
