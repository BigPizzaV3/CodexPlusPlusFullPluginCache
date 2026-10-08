import { requireChatGPTUser } from "../chatgpt-auth";
import { managerRole } from "../../db/manager-access";
import { Tracker } from "../page";

export const dynamic = "force-dynamic";

export default async function ManagePage() {
  const user = await requireChatGPTUser("/manage");
  const role = await managerRole(user);

  if (!role) {
    return (
      <main className="access-denied">
        <section>
          <p className="eyebrow">MANAGER ACCESS</p>
          <h1>This editing view is restricted.</h1>
          <p>The public read-only tracker is available from the main site address.</p>
          <a className="button" href="/">Open read-only progress</a>
        </section>
      </main>
    );
  }

  return <Tracker isOwner={role === "owner"} managerEmail={user.email} />;
}
