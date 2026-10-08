import { Cube as CubeIcon } from "@oai/ds/icons/cube";
import type { ComponentProps } from "react";
import { FormattedMessage } from "react-intl";
import { useLocation } from "react-router";
import { AppLink, ExternalLink } from "../link";
import { commitUrl, shortHash } from "./findings-utils";
import Table from "./table";

/** Shared source links for findings and scans, using the producing environment. */
export function WorkbenchSource({
  environmentLabel,
  repositoryId,
  repositoryUrl,
  commitHash,
  variant = "table",
  isLoading = false,
  rowLinkProps,
}: {
  environmentLabel?: string | null;
  repositoryId: string;
  repositoryUrl: string;
  commitHash?: string | null;
  variant?: "table" | "breadcrumb";
  isLoading?: boolean;
  rowLinkProps?: ComponentProps<typeof Table.RowTextLink>;
}) {
  "use forget";
  const location = useLocation();
  const params = new URLSearchParams({
    repo: repositoryUrl,
    repo_id: repositoryId,
  });
  const preview = new URLSearchParams(location.search).get(
    "workflow_runs_preview",
  );
  if (preview) params.set("workflow_runs_preview", preview);
  const commitHref = commitHash ? commitUrl(repositoryUrl, commitHash) : null;

  return (
    <span
      className={[
        "flex min-w-0 items-center gap-2",
        variant === "table" &&
          "text-token-text-secondary text-[12px] leading-4 font-normal",
      ]
        .filter(Boolean)
        .join(" ")}
    >
      {isLoading ? (
        <span
          aria-busy="true"
          className="h-4 w-32 animate-pulse rounded bg-token-bg-tertiary"
        >
          <span className="sr-only">
            <FormattedMessage
              id="codexSecurity.workbench.source.loading"
              defaultMessage="Loading environment…"
              description="Screen-reader status while the Security workbench resolves the environment that produced a finding or scan."
            />
          </span>
        </span>
      ) : environmentLabel ? (
        <AppLink
          to={{
            pathname: `/repositories/${encodeURIComponent(repositoryId)}`,
            search: `?${params.toString()}`,
          }}
          state={location.state}
          className="inline-flex min-w-0 items-center gap-1.5 underline-offset-2 hover:underline"
          title={environmentLabel}
        >
          <CubeIcon
            aria-hidden="true"
            className="text-token-text-tertiary h-4 w-4 shrink-0"
          />
          <span className="truncate">{environmentLabel}</span>
        </AppLink>
      ) : (
        <span className="text-token-text-tertiary">
          <FormattedMessage
            id="aardvark.placeholder.missing"
            defaultMessage="—"
            description="Dash placeholder indicating missing value"
          />
        </span>
      )}
      {commitHash ? (
        <>
          <span aria-hidden className="text-token-text-tertiary">
            <FormattedMessage
              id="codexSecurity.workbench.source.separator"
              defaultMessage="/"
              description="Separator between the environment name and commit ID links in the Source column of Security findings and scans tables."
            />
          </span>
          {commitHref ? (
            <ExternalLink
              href={commitHref}
              target="_blank"
              rel="noopener noreferrer"
              className="shrink-0 underline-offset-2 hover:underline"
              title={commitHash}
            >
              {shortHash(commitHash)}
            </ExternalLink>
          ) : rowLinkProps ? (
            <Table.RowTextLink
              {...rowLinkProps}
              className="shrink-0"
              title={commitHash}
            >
              {shortHash(commitHash)}
            </Table.RowTextLink>
          ) : (
            <span className="shrink-0" title={commitHash}>
              {shortHash(commitHash)}
            </span>
          )}
        </>
      ) : null}
    </span>
  );
}
