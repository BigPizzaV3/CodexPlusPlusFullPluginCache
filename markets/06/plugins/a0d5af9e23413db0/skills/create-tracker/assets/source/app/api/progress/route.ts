import { progressDb } from "../../../db/progress";
import { getChatGPTUser } from "../../chatgpt-auth";
import { requireManager } from "../../../db/manager-access";

const allowed = new Set(["not-started", "roughed-in", "finish-installed", "complete", "issue"]);

export async function GET() {
  try {
    const result = await progressDb().prepare("SELECT fixture_id AS fixtureId, status, CASE WHEN updated_at > COALESCE((SELECT MAX(cleared_at) FROM fixture_history_clears WHERE fixture_id IN ('*', fixture_progress.fixture_id)), '') THEN updated_at ELSE NULL END AS updatedAt FROM fixture_progress ORDER BY fixture_id").all();
    return Response.json({ progress: result.results });
  } catch { return Response.json({ error: "Progress is temporarily unavailable" }, { status: 503 }); }
}
export async function POST(request: Request) {
  try {
    const user = await getChatGPTUser();
    if (!(await requireManager(user))) {
      return Response.json({ error: "Manager access required" }, { status: 403 });
    }
    const payload = await request.json() as { updates?: Array<{ fixtureId?: string; status?: string }> };
    const updates = payload.updates || [];
    if (!updates.length || updates.length > 50) return Response.json({ error: "Valid updates are required" }, { status: 400 });
    for (const item of updates) if (!item.fixtureId || item.fixtureId.length > 100 || !item.status || !allowed.has(item.status)) return Response.json({ error: "Invalid fixture update" }, { status: 400 });
    const db = progressDb();
    const ids = updates.map(() => "?").join(",");
    const existing = await db.prepare(`SELECT fixture_id AS fixtureId, status FROM fixture_progress WHERE fixture_id IN (${ids})`).bind(...updates.map(item => item.fixtureId)).all<{ fixtureId: string; status: string }>();
    const previous = new Map(existing.results.map(row => [row.fixtureId, row.status]));
    const statements = updates.flatMap(item => {
      const prior = previous.get(item.fixtureId) || "not-started";
      if (prior === item.status) return [];
      return [
        db.prepare("INSERT INTO fixture_progress (fixture_id, status, updated_at) VALUES (?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'now')) ON CONFLICT(fixture_id) DO UPDATE SET status = excluded.status, updated_at = STRFTIME('%Y-%m-%d %H:%M:%f', 'now')").bind(item.fixtureId, item.status),
        db.prepare("INSERT INTO fixture_status_history (fixture_id, previous_status, new_status, changed_at) VALUES (?, ?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'now'))").bind(item.fixtureId, prior, item.status),
      ];
    });
    if (!statements.length) return Response.json({ saved: 0, progress: [] });
    await db.batch(statements);
    const refreshed = await db.prepare(`SELECT fixture_id AS fixtureId, status, updated_at AS updatedAt FROM fixture_progress WHERE fixture_id IN (${ids})`).bind(...updates.map(item => item.fixtureId)).all();
    return Response.json({ saved: statements.length / 2, progress: refreshed.results });
  } catch { return Response.json({ error: "Progress could not be saved" }, { status: 503 }); }
}
