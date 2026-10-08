import { env } from "cloudflare:workers";

export function progressDb() {
  if (!env.DB) throw new Error("Progress database is unavailable");
  return env.DB;
}
