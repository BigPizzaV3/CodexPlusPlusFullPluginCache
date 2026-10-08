import { env } from "cloudflare:workers";
import { progressDb } from "./progress";
import type { ChatGPTUser } from "../app/chatgpt-auth";

export type ManagerRole = "owner" | "manager" | null;

export async function managerRole(user: ChatGPTUser | null): Promise<ManagerRole> {
  if (!user) return null;
  const email = user.email.trim().toLowerCase();
  if (env.OWNER_EMAIL && email === env.OWNER_EMAIL.trim().toLowerCase()) return "owner";
  const manager = await progressDb()
    .prepare("SELECT email FROM tracker_managers WHERE email = ?")
    .bind(email)
    .first<{ email: string }>();
  return manager ? "manager" : null;
}

export async function requireManager(user: ChatGPTUser | null) {
  return (await managerRole(user)) !== null;
}

export async function requireOwner(user: ChatGPTUser | null) {
  return (await managerRole(user)) === "owner";
}

