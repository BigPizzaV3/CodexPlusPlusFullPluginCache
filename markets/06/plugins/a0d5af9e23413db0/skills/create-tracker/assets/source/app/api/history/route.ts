import { progressDb } from "../../../db/progress";
import { getChatGPTUser } from "../../chatgpt-auth";
import { requireManager } from "../../../db/manager-access";

export async function GET(request: Request) {
  try {
    const fixtureId = new URL(request.url).searchParams.get("fixtureId");
    if (!fixtureId || fixtureId.length > 100) return Response.json({ error: "A valid device is required" }, { status: 400 });
    const result = await progressDb().prepare("SELECT id, fixture_id AS fixtureId, previous_status AS previousStatus, new_status AS newStatus, changed_at AS changedAt FROM fixture_status_history WHERE fixture_id = ? AND changed_at > COALESCE((SELECT MAX(cleared_at) FROM fixture_history_clears WHERE fixture_id IN ('*', ?)), '') ORDER BY id DESC LIMIT 100").bind(fixtureId, fixtureId).all();
    return Response.json({ history: result.results });
  } catch {
    return Response.json({ error: "Status history is temporarily unavailable" }, { status: 503 });
  }
}

export async function DELETE(request: Request) {
  try {
    const user = await getChatGPTUser();
    if (!user || !(await requireManager(user))) return Response.json({ error: "Manager access required" }, { status: 403 });
    const body = await request.json() as { fixtureId?: string; all?: boolean };
    const db = progressDb();
    if (body.all === true) {
      await db.batch([
        db.prepare("DELETE FROM fixture_status_history"),
        db.prepare("INSERT INTO fixture_history_clears (fixture_id, cleared_at, cleared_by) VALUES ('*', STRFTIME('%Y-%m-%d %H:%M:%f', 'now'), ?) ON CONFLICT(fixture_id) DO UPDATE SET cleared_at = excluded.cleared_at, cleared_by = excluded.cleared_by").bind(user.email.toLowerCase()),
      ]);
      return Response.json({ cleared: "all" });
    }
    const fixtureId = body.fixtureId?.trim();
    if (!fixtureId || fixtureId.length > 100) return Response.json({ error: "A valid device is required" }, { status: 400 });
    await db.batch([
      db.prepare("DELETE FROM fixture_status_history WHERE fixture_id = ?").bind(fixtureId),
      db.prepare("INSERT INTO fixture_history_clears (fixture_id, cleared_at, cleared_by) VALUES (?, STRFTIME('%Y-%m-%d %H:%M:%f', 'now'), ?) ON CONFLICT(fixture_id) DO UPDATE SET cleared_at = excluded.cleared_at, cleared_by = excluded.cleared_by").bind(fixtureId, user.email.toLowerCase()),
    ]);
    return Response.json({ cleared: fixtureId });
  } catch {
    return Response.json({ error: "Status history could not be cleared" }, { status: 503 });
  }
}

