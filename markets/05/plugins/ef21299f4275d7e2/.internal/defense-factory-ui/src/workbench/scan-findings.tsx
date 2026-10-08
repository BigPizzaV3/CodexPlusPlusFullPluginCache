import { useQuery } from "@tanstack/react-query";
import { useState } from "react";
import { FormattedMessage } from "react-intl";

import { useCloud } from "../app-context";
import { securityClient } from "../client";
import type { DefenseFactoryRequest } from "../contract";
import {
  FindingsTableView,
  pageSize,
  type FindingTableRow,
} from "./findings-table";
import type { Finding } from "./types";

function findingRow(finding: Finding): FindingTableRow {
  return {
    id: finding.id,
    repo_id: finding.repo_id,
    repo_url: finding.repo_url,
    title: finding.title,
    criticality: finding.criticality,
    status: finding.status,
    created_at: finding.created_at,
    scanType: finding.source.kind,
    commit_hash:
      finding.source.kind === "commit_scan"
        ? finding.observed_revision ?? null
        : null,
    environmentSource:
      finding.source.kind === "repository_scan"
        ? { kind: "workflow_run", id: finding.source.workflow_run_id }
        : { kind: "finding", id: finding.id },
  };
}

export function ScanFindings({
  detailBasePath,
  repositoryId,
  repositoryUrl,
  scanId,
  scanStatus,
  source,
}: {
  detailBasePath: string;
  repositoryId: string;
  repositoryUrl: string;
  scanId: string;
  scanStatus: string;
  source: "repository_scan" | "commit_scan";
}) {
  const cloud = useCloud();
  const [search, setSearch] = useState(() =>
    new URLSearchParams({
      repo: repositoryUrl,
      repo_id: repositoryId,
      source,
      status: "",
      limit: "50",
    }).toString(),
  );
  // These cursors belong to this scan, not the broader findings detail route.
  const [cursors, setCursors] = useState<(string | null)[]>([null]);
  const params = new URLSearchParams(search);
  const currentCursor = cursors.at(-1);
  const limit = pageSize(search);
  const queryParameters: NonNullable<
    DefenseFactoryRequest<"findings_list">["parameters"]
  >["query"] = {
    repo: repositoryUrl,
    source,
    scan_id: scanId,
    status: "",
    sort: params.get("sort") ?? "sev_desc,date_desc",
    limit,
    cursor: currentCursor ?? undefined,
  };
  const query = useQuery({
    queryKey: [
      "scan-findings",
      cloud.accountId,
      cloud.identity?.userId,
      repositoryId,
      queryParameters,
      scanStatus,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "findings_list",
        parameters: { query: queryParameters },
      }),
    refetchOnMount: "always",
    staleTime: 15_000,
  });
  const page = query.error ? undefined : query.data;
  const offset = page?.offset ?? 0;

  function changePage(nextOffset: number) {
    if (nextOffset > offset) {
      if (page?.next_cursor) setCursors([...cursors, page.next_cursor]);
    } else if (cursors.length > 1) {
      setCursors(cursors.slice(0, -1));
    }
  }

  return (
    <FindingsTableView
      detailBasePath={detailBasePath}
      search={search}
      onSearchChange={(nextSearch) => {
        setSearch(nextSearch);
        setCursors([null]);
      }}
      cursor={offset}
      hasPrevious={cursors.length > 1}
      hasNext={Boolean(page?.next_cursor)}
      onPageChange={changePage}
      emptyMessage={
        <FormattedMessage
          id="codexSecurity.workbench.scans.detail.findings.empty"
          defaultMessage="No findings are available for this scan."
          description="Neutral empty state when no authorized findings are associated with this exact scan."
        />
      }
      findingsQuery={{
        data: {
          items: page?.items.map(findingRow) ?? [],
          total: page?.total ?? 0,
        },
        isLoading: query.isPending,
        isFetching: query.isFetching,
        error: query.error,
        refetch: query.refetch,
      }}
    />
  );
}
