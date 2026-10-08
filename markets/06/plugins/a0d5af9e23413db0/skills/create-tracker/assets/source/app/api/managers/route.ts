import { env } from "cloudflare:workers";
import { progressDb } from "../../../db/progress";
import { getChatGPTUser } from "../../chatgpt-auth";
import { requireOwner } from "../../../db/manager-access";

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

async function ownerUser() {
  const user = await getChatGPTUser();
  return user && await requireOwner(user) ? user : null;
}

export async function GET() {
  try {
    const user = await ownerUser();
    if (!user) return Response.json({ error: "Owner access required" }, { status: 403 });
    const result = await progressDb().prepare("SELECT email, added_by AS addedBy, created_at AS createdAt FROM tracker_managers ORDER BY email").all();
    return Response.json({
      ownerEmail: env.OWNER_EMAIL || user.email,
      managers: result.results,
    });
  } catch {
    return Response.json({ error: "Manager list is temporarily unavailable" }, { status: 503 });
  }
}

export async function POST(request: Request) {
  try {
    const user = await ownerUser();
    if (!user) return Response.json({ error: "Owner access required" }, { status: 403 });
    const body = await request.json() as { email?: string };
    const email = body.email?.trim().toLowerCase() || "";
    if (!emailPattern.test(email) || email.length > 254) return Response.json({ error: "Enter a valid email address" }, { status: 400 });
    if (env.OWNER_EMAIL && email === env.OWNER_EMAIL.toLowerCase()) return Response.json({ error: "The owner already has access" }, { status: 400 });
    const manager = await progressDb().prepare("INSERT INTO tracker_managers (email, added_by, created_at) VALUES (?, ?, STRFTIME('%Y-%m-%d %H:%M:%f', 'now')) ON CONFLICT(email) DO UPDATE SET added_by = excluded.added_by RETURNING email, added_by AS addedBy, created_at AS createdAt").bind(email, user.email.toLowerCase()).first();
    return Response.json({ manager }, { status: 201 });
  } catch {
    return Response.json({ error: "Manager could not be added" }, { status: 503 });
  }
}

export async function DELETE(request: Request) {
  try {
    const user = await ownerUser();
    if (!user) return Response.json({ error: "Owner access required" }, { status: 403 });
    const body = await request.json() as { email?: string };
    const email = body.email?.trim().toLowerCase() || "";
    if (!emailPattern.test(email)) return Response.json({ error: "A valid manager email is required" }, { status: 400 });
    await progressDb().prepare("DELETE FROM tracker_managers WHERE email = ?").bind(email).run();
    return Response.json({ removed: email });
  } catch {
    return Response.json({ error: "Manager could not be removed" }, { status: 503 });
  }
}

