import { progressDb } from "../../../db/progress";
import { getChatGPTUser } from "../../chatgpt-auth";
import { requireManager } from "../../../db/manager-access";

function validTag(value: unknown): value is string {
  return typeof value === "string" && value.length > 0 && value.length <= 100 && /^[a-z0-9][a-z0-9-]*$/i.test(value);
}

export async function GET() {
  try {
    const result = await progressDb().prepare("SELECT id, content, system, floor, created_at AS createdAt, updated_at AS updatedAt FROM tracker_notes ORDER BY updated_at DESC, id DESC").all();
    return Response.json({ notes: result.results });
  } catch {
    return Response.json({ error: "Notes are temporarily unavailable" }, { status: 503 });
  }
}

export async function POST(request: Request) {
  try {
    if (!(await requireManager(await getChatGPTUser()))) return Response.json({ error: "Manager access required" }, { status: 403 });
    const body = await request.json() as { content?: string; system?: string | null; floor?: string | null };
    const content = body.content?.trim() || "";
    if (!content || content.length > 4000) return Response.json({ error: "A note between 1 and 4,000 characters is required" }, { status: 400 });
    const system = validTag(body.system) ? body.system : null;
    const floor = validTag(body.floor) ? body.floor : null;
    const result = await progressDb().prepare("INSERT INTO tracker_notes (content, system, floor, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING id, content, system, floor, created_at AS createdAt, updated_at AS updatedAt").bind(content, system, floor).first();
    return Response.json({ note: result }, { status: 201 });
  } catch {
    return Response.json({ error: "Note could not be saved" }, { status: 503 });
  }
}

export async function PATCH(request: Request) {
  try {
    if (!(await requireManager(await getChatGPTUser()))) return Response.json({ error: "Manager access required" }, { status: 403 });
    const body = await request.json() as { id?: number; content?: string };
    const content = body.content?.trim() || "";
    if (!Number.isInteger(body.id) || !content || content.length > 4000) return Response.json({ error: "A valid note is required" }, { status: 400 });
    const result = await progressDb().prepare("UPDATE tracker_notes SET content = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? RETURNING id, content, system, floor, created_at AS createdAt, updated_at AS updatedAt").bind(content, body.id).first();
    if (!result) return Response.json({ error: "Note not found" }, { status: 404 });
    return Response.json({ note: result });
  } catch {
    return Response.json({ error: "Note could not be updated" }, { status: 503 });
  }
}

export async function DELETE(request: Request) {
  try {
    if (!(await requireManager(await getChatGPTUser()))) return Response.json({ error: "Manager access required" }, { status: 403 });
    const body = await request.json() as { id?: number };
    if (!Number.isInteger(body.id)) return Response.json({ error: "A valid note is required" }, { status: 400 });
    await progressDb().prepare("DELETE FROM tracker_notes WHERE id = ?").bind(body.id).run();
    return Response.json({ deleted: body.id });
  } catch {
    return Response.json({ error: "Note could not be deleted" }, { status: 503 });
  }
}
