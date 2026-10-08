import { useQuery } from "@tanstack/react-query";
import { type ReactNode } from "react";
import { FormattedMessage } from "react-intl";
import { useSearchParams } from "react-router";

import { useCloud } from "./app-context";
import { securityClient } from "./client";
import { repositoryLabel } from "./ui";
import { WorkbenchButton as Button } from "./workbench/controls";
import { ScanDetailPresentation } from "./workbench/scan-detail-presentation";
import { ScanFindings } from "./workbench/scan-findings";
import { WorkbenchState } from "./workbench/layout";
import type { WorkbenchScan } from "./workbench/scans-model";

const activeStatuses = new Set(["created", "in_progress"]);

function normalizedRepositoryUrl(repositoryUrl?: string | null) {
  return repositoryUrl?.replace(/\.git$/, "");
}

export function ContinuousScanDetail({
  configurationId,
  repositoryId,
  scanId,
}: {
  configurationId?: string | null;
  repositoryId?: string | null;
  scanId: string;
}) {
  const { accountId, identity } = useCloud();
  const [search] = useSearchParams();
  const includeDeleted = search.get("include_deleted") === "true";
  const repoIdFromSearch = search.get("repo_id");
  const repoUrlFromSearch = search.get("repo");
  const scopeHintsAreValid = Boolean(
    (!search.has("repo_id") || repoIdFromSearch?.trim()) &&
      (!search.has("repo") || repoUrlFromSearch?.trim()) &&
      (!repositoryId || !repoIdFromSearch || repositoryId === repoIdFromSearch),
  );
  const configuration = useQuery({
    queryKey: [
      "continuous-scan-configuration",
      accountId,
      identity?.userId ?? "none",
      configurationId,
      includeDeleted,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_get",
        parameters: {
          path: { id: configurationId ?? "" },
          query: { include_deleted: includeDeleted },
        },
      }),
    enabled: Boolean(configurationId),
    refetchOnMount: "always",
    staleTime: 15_000,
  });
  const authorizedConfiguration =
    configuration.isFetchedAfterMount && !configuration.error
      ? configuration.data
      : undefined;
  const configurationMatchesRoute = Boolean(
    scopeHintsAreValid &&
      configurationId &&
      authorizedConfiguration &&
      (authorizedConfiguration.id === configurationId ||
        authorizedConfiguration.hid === configurationId) &&
      authorizedConfiguration.scan_type === "continuous_scan" &&
      (includeDeleted || !authorizedConfiguration.soft_deleted_at) &&
      (!repositoryId ||
        authorizedConfiguration.scan_input.repo_id === repositoryId) &&
      (!repoIdFromSearch ||
        authorizedConfiguration.scan_input.repo_id === repoIdFromSearch) &&
      (!repoUrlFromSearch ||
        normalizedRepositoryUrl(authorizedConfiguration.scan_input.repo_url) ===
          normalizedRepositoryUrl(repoUrlFromSearch)),
  );
  const run = useQuery({
    queryKey: [
      "continuous-scan",
      accountId,
      identity?.userId ?? "none",
      authorizedConfiguration?.hid,
      scanId,
      includeDeleted,
    ],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_scan_get",
        parameters: {
          path: {
            id: authorizedConfiguration?.hid ?? "",
            scan_id: scanId,
          },
          query: { include_deleted: includeDeleted },
        },
      }),
    enabled: configurationMatchesRoute,
    refetchOnMount: "always",
    staleTime: 4_000,
    refetchInterval: (query) =>
      query.state.data && activeStatuses.has(query.state.data.status)
        ? 4_000
        : false,
  });
  const authorizedRun =
    run.isFetchedAfterMount && !run.error ? run.data : undefined;
  const runMatchesConfiguration = Boolean(
    authorizedConfiguration &&
      authorizedRun &&
      authorizedRun.id === scanId &&
      (authorizedRun.scan_configuration_id === authorizedConfiguration.id ||
        authorizedRun.scan_configuration_id === authorizedConfiguration.hid) &&
      authorizedRun.scan_input.repo_id ===
        authorizedConfiguration.scan_input.repo_id &&
      normalizedRepositoryUrl(authorizedRun.scan_input.repo_url) ===
        normalizedRepositoryUrl(authorizedConfiguration.scan_input.repo_url) &&
      (authorizedRun.scan_input.repo_connector_id ?? null) ===
        (authorizedConfiguration.scan_input.repo_connector_id ?? null) &&
      (!repositoryId || authorizedRun.scan_input.repo_id === repositoryId),
  );
  const environments = useQuery({
    queryKey: ["scan-environments", accountId, identity?.userId ?? "none"],
    queryFn: () => securityClient.request({ operation: "environments_list" }),
    enabled: runMatchesConfiguration,
    refetchOnMount: "always",
    staleTime: 60_000,
  });

  if (!configurationId) return <ContinuousScanUnavailable />;
  if (configuration.isPending || !configuration.isFetchedAfterMount) {
    return <WorkbenchState loading variant="panel" />;
  }
  if (configuration.error) {
    return (
      <ContinuousScanUnavailable
        retryAction={
          <RetryButton
            loading={configuration.isFetching}
            onRetry={() => void configuration.refetch()}
          />
        }
      />
    );
  }
  if (!configurationMatchesRoute) return <ContinuousScanUnavailable />;
  if (run.isPending || !run.isFetchedAfterMount)
    return <WorkbenchState loading variant="panel" />;
  if (run.error) {
    return (
      <ContinuousScanUnavailable
        retryAction={
          <RetryButton
            loading={run.isFetching}
            onRetry={() => void run.refetch()}
          />
        }
      />
    );
  }
  if (!authorizedRun || !runMatchesConfiguration) {
    return <ContinuousScanUnavailable />;
  }

  const repositoryUrl = authorizedRun.scan_input.repo_url;
  const detailBasePath = repositoryId
    ? `/repositories/${encodeURIComponent(repositoryId)}/findings`
    : "/findings";
  const scan: WorkbenchScan = {
    id: authorizedRun.id,
    commitScan: authorizedRun,
    scanType: "commit_scan",
    repositoryId: authorizedRun.scan_input.repo_id,
    repositoryName:
      repositoryLabel(repositoryUrl) || authorizedRun.scan_input.repo_id,
    repositoryUrl,
    environmentLabel:
      environments.isFetchedAfterMount && !environments.error
        ? environments.data?.find(
            (environment) =>
              environment.id === authorizedRun.scan_input.environment_id,
          )?.label
        : undefined,
    isEnvironmentLoading:
      environments.isPending || !environments.isFetchedAfterMount,
  };

  return (
    <ScanDetailPresentation
      scan={scan}
      findings={
        <ScanFindings
          detailBasePath={detailBasePath}
          repositoryId={authorizedRun.scan_input.repo_id}
          repositoryUrl={repositoryUrl}
          scanId={authorizedRun.id}
          scanStatus={authorizedRun.status}
          source="commit_scan"
        />
      }
      isCanceling={false}
      onRequestCancel={() => undefined}
    />
  );
}

function RetryButton({
  loading,
  onRetry,
}: {
  loading: boolean;
  onRetry: () => void;
}) {
  return (
    <Button color="outlineSurface" loading={loading} onClick={onRetry}>
      <FormattedMessage
        id="codexSecurity.workbench.scans.commitDetail.retry"
        defaultMessage="Retry"
        description="Retry loading an authorized commit scan."
      />
    </Button>
  );
}

function ContinuousScanUnavailable({
  retryAction,
}: {
  retryAction?: ReactNode;
}) {
  return (
    <WorkbenchState variant="panel" action={retryAction}>
      <FormattedMessage
        id="codexSecurity.workbench.scans.commitDetail.unavailable"
        defaultMessage="This scan is unavailable or you do not have access to it."
        description="Privacy-preserving error shown when a commit scan cannot be loaded."
      />
    </WorkbenchState>
  );
}
