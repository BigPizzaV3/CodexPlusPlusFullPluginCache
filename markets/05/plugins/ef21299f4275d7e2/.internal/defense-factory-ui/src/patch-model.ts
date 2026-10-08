import type { components } from "@oai/aardvark-client/components";
import { z } from "zod";

// The generated Aardvark schema leaves the embedded Cloud turn untyped.
const patchTurnSchema = z.object({
  role: z.literal("assistant"),
  output_items: z.array(
    z.object({
      type: z.string(),
      diff: z.string().optional(),
      output_diff: z.object({ diff: z.string() }).optional(),
      reviewed_diff: z.object({ diff: z.string() }).nullish(),
      content: z.array(z.object({ text: z.string().optional() })).optional(),
    }),
  ),
  pull_request_status: z.string().nullish(),
  pull_request_data: z.object({ url: z.string().nullish() }).nullish(),
});

export function findingPatch(
  finding: components["schemas"]["ScanFindingResponse"],
): {
  patch: string;
  description: string;
  pullRequestUrl: string | null;
} {
  const parsed = patchTurnSchema.safeParse(
    finding.proposed_patch?.latest_task?.codex_task_turn?.turn,
  );
  const turn = parsed.success ? parsed.data : null;
  const patch =
    turn?.output_items
      .flatMap((item) => {
        if (item.type === "output_diff") {
          return item.diff ? [item.diff] : [];
        }
        if (item.type === "pr") {
          return item.output_diff ? [item.output_diff.diff] : [];
        }
        if (item.type === "cr" || item.type === "sr") {
          return item.reviewed_diff ? [item.reviewed_diff.diff] : [];
        }
        return [];
      })
      .join("\n\n") ?? "";
  return {
    patch,
    description:
      turn?.output_items
        .filter((item) => item.type === "message")
        .flatMap(
          (item) =>
            item.content?.flatMap((content) =>
              content.text ? [content.text] : [],
            ) ?? [],
        )
        .join("\n\n") ?? "",
    pullRequestUrl:
      turn?.pull_request_status === "externally_created"
        ? null
        : turn?.pull_request_data?.url ?? null,
  };
}
