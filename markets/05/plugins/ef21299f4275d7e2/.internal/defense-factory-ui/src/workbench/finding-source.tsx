import { useQuery } from "@tanstack/react-query";
import type { ComponentProps } from "react";
import { useCloud } from "../app-context";
import { securityClient } from "../client";
import type { FindingTableRow } from "./findings-table";
import { WorkbenchSource } from "./source";
import type Table from "./table";

export function FindingSource({
  finding,
  rowLinkProps,
}: {
  finding: FindingTableRow;
  rowLinkProps: ComponentProps<typeof Table.RowTextLink>;
}) {
  const { accountId } = useCloud();
  const source = finding.environmentSource;
  const environment = useQuery({
    queryKey: ["finding-environment", accountId, source, finding.repo_id],
    queryFn: async () => {
      if (source.kind === "environment") return source.id;
      // The combined list omits the environment. Resolve the producing scan,
      // rather than guessing among environments that share the repository.
      if (source.kind === "workflow_run") {
        const run = await securityClient.request({
          operation: "workflow_get",
          parameters: { path: { run_id: source.id } },
        });
        return run.repo_id === finding.repo_id ? run.environment_id : null;
      }
      const detail = await securityClient.request({
        operation: "findings_get",
        parameters: { path: { finding_id: source.id } },
      });
      return detail.repo_id === finding.repo_id
        ? detail.commit_detail?.environment_id ?? null
        : null;
    },
    staleTime: 60_000,
  });
  // The plugin exposes a secret-free environment list, not the Cloud detail API.
  // Share this one lookup across rows and match the exact producing environment.
  const environments = useQuery({
    queryKey: ["finding-environments", accountId],
    queryFn: () => securityClient.request({ operation: "environments_list" }),
    enabled: Boolean(environment.data),
    staleTime: 60_000,
  });
  return (
    <WorkbenchSource
      environmentLabel={
        environments.data?.find((item) => item.id === environment.data)?.label
      }
      repositoryId={finding.repo_id}
      repositoryUrl={finding.repo_url}
      commitHash={finding.commit_hash}
      rowLinkProps={rowLinkProps}
      isLoading={
        environment.isPending ||
        (Boolean(environment.data) && environments.isPending)
      }
    />
  );
}
