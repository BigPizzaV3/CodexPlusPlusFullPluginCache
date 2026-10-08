import { progressDb } from "../../../db/progress";
import { getChatGPTUser } from "../../chatgpt-auth";
import { requireManager } from "../../../db/manager-access";
import { fixtures, planImages } from "../../fixtures";

const statuses: Record<string, string> = { "not-started": "Not Started", "roughed-in": "Roughed In", "finish-installed": "Finish Installed", complete: "Complete", issue: "Issue / Blocked" };
const periodTypes = new Set(["today", "week", "since-last"]);
const fixtureMap = new Map(fixtures.map(fixture => [fixture.id, fixture]));
type HistoryRow = { id: number; fixtureId: string; newStatus: string; changedAt: string };
type NoteRow = { id: number; content: string; system: string | null; floor: string | null; createdAt: string; updatedAt: string };

function sqliteTime(date: Date) { return date.toISOString().replace("T", " ").replace("Z", ""); }
function displayName(value: string) { return value.split("-").map(part => part ? part[0].toUpperCase() + part.slice(1) : part).join(" "); }
function floorName(system: string, floor: string) {
  const plans = planImages as Record<string, Record<string, { label: string }>>;
  return plans[system]?.[floor]?.label || displayName(floor);
}
function parseReport(row: Record<string, unknown>) {
  let summary = { groups: [], notes: [], deviceCount: 0, noteCount: 0, daysSincePrevious: null };
  try { summary = JSON.parse(String(row.summaryJson)); } catch {}
  return { ...row, summary };
}

export async function GET() {
  try {
    const result = await progressDb().prepare("SELECT id, period_type AS periodType, period_start AS periodStart, period_end AS periodEnd, summary_json AS summaryJson, created_at AS createdAt, created_by AS createdBy FROM progress_reports ORDER BY created_at DESC, id DESC").all<Record<string, unknown>>();
    return Response.json({ reports: result.results.map(parseReport) });
  } catch { return Response.json({ error: "Progress reports are temporarily unavailable" }, { status: 503 }); }
}

export async function POST(request: Request) {
  try {
    const user = await getChatGPTUser();
    if (!user || !(await requireManager(user))) return Response.json({ error: "Manager access required" }, { status: 403 });
    const body = await request.json() as { periodType?: string; periodStart?: string; periodEnd?: string };
    if (!body.periodType || !periodTypes.has(body.periodType)) return Response.json({ error: "Choose a valid report period" }, { status: 400 });
    const start = new Date(body.periodStart || ""); const end = new Date(body.periodEnd || "");
    if (Number.isNaN(start.getTime()) || Number.isNaN(end.getTime()) || start >= end || end.getTime() > Date.now() + 60_000) return Response.json({ error: "Choose a valid report date range" }, { status: 400 });
    const db = progressDb(); const startSql = sqliteTime(start); const endSql = sqliteTime(end);
    const history = await db.prepare("SELECT id, fixture_id AS fixtureId, new_status AS newStatus, changed_at AS changedAt FROM fixture_status_history WHERE changed_at >= ? AND changed_at <= ? AND changed_at > COALESCE((SELECT MAX(cleared_at) FROM fixture_history_clears WHERE fixture_id IN ('*', fixture_status_history.fixture_id)), '') ORDER BY changed_at ASC, id ASC").bind(startSql, endSql).all<HistoryRow>();
    const noteRows = await db.prepare("SELECT id, content, system, floor, created_at AS createdAt, updated_at AS updatedAt FROM tracker_notes WHERE (created_at >= ? AND created_at <= ?) OR (updated_at >= ? AND updated_at <= ?) ORDER BY updated_at ASC, id ASC").bind(startSql, endSql, startSql, endSql).all<NoteRow>();
    const lastByFixture = new Map<string, HistoryRow>(); history.results.forEach(row => lastByFixture.set(row.fixtureId, row));
    const grouped = new Map<string, { system: string; floor: string; deviceType: string; status: string; count: number }>();
    for (const row of lastByFixture.values()) {
      const fixture = fixtureMap.get(row.fixtureId); if (!fixture || !statuses[row.newStatus]) continue;
      const key = [fixture.system, fixture.floor, fixture.type, row.newStatus].join("\u0000"); const current = grouped.get(key);
      if (current) current.count += 1;
      else grouped.set(key, { system: displayName(fixture.system), floor: floorName(fixture.system, fixture.floor), deviceType: fixture.type, status: statuses[row.newStatus], count: 1 });
    }
    const groups = [...grouped.values()].sort((a, b) => a.system.localeCompare(b.system) || a.floor.localeCompare(b.floor) || a.deviceType.localeCompare(b.deviceType) || a.status.localeCompare(b.status));
    const notes = noteRows.results.map(note => ({ ...note, systemLabel: note.system ? displayName(note.system) : "General", floorLabel: note.floor ? floorName(note.system || "", note.floor) : null }));
    if (!groups.length && !notes.length) return Response.json({ error: "No status changes or project notes were recorded in this period." }, { status: 400 });
    const previous = await db.prepare("SELECT created_at AS createdAt FROM progress_reports ORDER BY created_at DESC, id DESC LIMIT 1").first<{ createdAt: string }>();
    const previousDate = previous?.createdAt ? new Date(`${previous.createdAt.replace(" ", "T")}Z`) : null;
    const daysSincePrevious = previousDate && !Number.isNaN(previousDate.getTime()) ? Math.max(0, Math.floor((Date.now() - previousDate.getTime()) / 86_400_000)) : null;
    const summary = { groups, notes, deviceCount: groups.reduce((total, group) => total + group.count, 0), noteCount: notes.length, daysSincePrevious };
    const report = await db.prepare("INSERT INTO progress_reports (period_type, period_start, period_end, summary_json, created_at, created_by) VALUES (?, ?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'now'), ?) RETURNING id, period_type AS periodType, period_start AS periodStart, period_end AS periodEnd, summary_json AS summaryJson, created_at AS createdAt, created_by AS createdBy").bind(body.periodType, start.toISOString(), end.toISOString(), JSON.stringify(summary), user.email.toLowerCase()).first<Record<string, unknown>>();
    return Response.json({ report: parseReport(report || {}) }, { status: 201 });
  } catch { return Response.json({ error: "Progress report could not be generated" }, { status: 503 }); }
}
