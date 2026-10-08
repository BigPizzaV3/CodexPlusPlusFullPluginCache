import { WorkbenchBadge as Badge, WorkbenchLink } from "./controls";
import type { ReactNode } from "react";
import { FormattedMessage } from "react-intl";
import { useLocation } from "react-router";

import type { DefenseFactoryResponse } from "../contract";
import { ExternalLink } from "../link";
import { DateTime, repositoryLabel } from "../ui";
import {
  FindingDetailHeading,
  FindingDetailToolbar,
  FindingMetadataRow,
  FindingSeverityBadge,
  FindingStatusBadge,
} from "./finding-detail-layout";
import { shortHash } from "./findings-utils";
import { WorkbenchScanTypeBadge } from "./scan-type-badge";
import { workbenchStyles } from "./styles";

type CombinedFindingDetail = DefenseFactoryResponse<"findings_get">;

function evidenceText(value: unknown): string {
  if (typeof value === "string") return value;
  if (
    value &&
    typeof value === "object" &&
    "summary" in value &&
    typeof value.summary === "string"
  ) {
    return value.summary;
  }
  return "";
}

function savedRepositoryHref(repoUrl: string): string | null {
  try {
    const url = new URL(repoUrl);
    if (url.origin !== "https://github.com" || url.username || url.password) {
      return null;
    }
    return `${url.origin}${url.pathname.replace(/\/+$/, "")}`;
  } catch {
    return null;
  }
}

function locationLabel(
  location: NonNullable<CombinedFindingDetail["locations"]>[number],
) {
  return location.start_line
    ? `${location.path}:${location.start_line}`
    : location.path;
}

export function RepositoryFindingDetail({
  finding,
}: {
  finding: CombinedFindingDetail;
}) {
  const location = useLocation();
  const evidence = finding.repository_evidence;
  const repositoryHref = savedRepositoryHref(finding.repo_url);
  const repositoryDisplayLabel = repositoryLabel(finding.repo_url);
  const revision = finding.observed_revision;
  const revisionHref =
    repositoryHref && revision
      ? `${repositoryHref}/commit/${encodeURIComponent(revision)}`
      : null;
  const workflowRunId =
    finding.source.kind === "repository_scan"
      ? finding.source.workflow_run_id
      : null;

  return (
    <section className="df-finding-detail">
      <FindingDetailToolbar
        actions={
          workflowRunId ? (
            <WorkbenchLink
              color="outlineSurface"
              to={`/runs/${encodeURIComponent(workflowRunId)}`}
              state={location.state}
            >
              <FormattedMessage
                id="codex.security.findings.detail.source.open_scan"
                defaultMessage="View scan"
                description="Open the Security scan that produced this finding."
              />
            </WorkbenchLink>
          ) : undefined
        }
      />
      <div className="df-finding-detail-grid">
        <div className="df-finding-detail-main">
          <FindingDetailHeading
            title={finding.title}
            status={finding.status}
            updatedAt={finding.updated_at}
          />
          <RepositoryEvidenceSection
            title={
              <FormattedMessage
                id="codex.security.findings.detail.summary.label"
                defaultMessage="Summary"
                description="Heading for the summary of a Security finding."
              />
            }
            value={finding.summary}
          />
          <RepositoryEvidenceSection
            title={
              <FormattedMessage
                id="codex.security.findings.detail.root_cause.label"
                defaultMessage="Root cause"
                description="Heading above the validated cause of a repository vulnerability."
              />
            }
            value={evidenceText(evidence?.rootCause)}
          />
          <RepositoryEvidenceSection
            title={
              <FormattedMessage
                id="codex.security.findings.detail.attack_path.label"
                defaultMessage="Attack path"
                description="Heading above how the repository vulnerability could be exploited."
              />
            }
            value={evidenceText(evidence?.attackPath)}
          />
          <RepositoryEvidenceSection
            title={
              <FormattedMessage
                id="codex.security.findings.detail.validation.label"
                defaultMessage="Validation"
                description="Heading above evidence validating the repository vulnerability."
              />
            }
            value={evidenceText(evidence?.validation)}
          />
          <RepositoryEvidenceSection
            title={
              <FormattedMessage
                id="codex.security.findings.detail.remediation.label"
                defaultMessage="Remediation"
                description="Heading above the suggested repository vulnerability fix."
              />
            }
            value={evidenceText(evidence?.remediation)}
          />
          {evidence ? (
            <details>
              <summary className="cursor-pointer">
                <FormattedMessage
                  id="codex.security.findings.detail.evidence.label"
                  defaultMessage="Full finding evidence"
                  description="Expandable complete validated finding document."
                />
              </summary>
              <pre className="mt-3 overflow-x-auto text-xs break-words whitespace-pre-wrap">
                {JSON.stringify(evidence, null, 2)}
              </pre>
            </details>
          ) : null}
        </div>

        <aside className="df-finding-detail-aside">
          <dl className="df-finding-metadata">
            <div className="df-finding-metadata-row">
              <dt className={workbenchStyles.metadataLabel}>
                <FormattedMessage
                  id="codex.security.findings.detail.reported_severity.label"
                  defaultMessage="Reported severity"
                  description="Severity assigned in the saved repository scan report."
                />
              </dt>
              <dd className={workbenchStyles.metadataValue}>
                <FindingSeverityBadge severity={finding.criticality} />
              </dd>
            </div>
            <FindingMetadataRow
              label={
                <FormattedMessage
                  id="defenseFactory.finding.metadata.status"
                  defaultMessage="Status"
                  description="The finding triage status, not a linked issue status."
                />
              }
            >
              <FindingStatusBadge status={finding.status} />
            </FindingMetadataRow>
            <div className="df-finding-metadata-row">
              <dt className={workbenchStyles.metadataLabel}>
                <FormattedMessage
                  id="codex.security.findings.detail.revision.label"
                  defaultMessage="Observed revision"
                  description="Commit revision where the repository scan observed the vulnerability."
                />
              </dt>
              <dd
                className={`${workbenchStyles.metadataValue} font-mono break-all`}
              >
                {revisionHref ? (
                  <ExternalLink
                    href={revisionHref}
                    className={workbenchStyles.link}
                    title={revision ?? undefined}
                  >
                    {shortHash(revision ?? "")}
                  </ExternalLink>
                ) : revision ? (
                  <span title={revision}>{shortHash(revision)}</span>
                ) : (
                  "—"
                )}
              </dd>
            </div>
            <div className="df-finding-metadata-row">
              <dt className={workbenchStyles.metadataLabel}>
                <FormattedMessage
                  id="codex.security.findings.detail.repository.label"
                  defaultMessage="Repository"
                  description="Repository whose code was scanned."
                />
              </dt>
              <dd className={`${workbenchStyles.metadataValue} break-words`}>
                {repositoryHref ? (
                  <ExternalLink
                    href={repositoryHref}
                    className={workbenchStyles.link}
                  >
                    {repositoryDisplayLabel}
                  </ExternalLink>
                ) : (
                  repositoryDisplayLabel
                )}
              </dd>
            </div>
            <FindingMetadataRow
              label={
                <FormattedMessage
                  id="defenseFactory.finding.metadata.detected"
                  defaultMessage="Detected"
                  description="When this finding was created."
                />
              }
            >
              <DateTime value={finding.created_at} />
            </FindingMetadataRow>
            <div className="df-finding-metadata-row">
              <dt className={workbenchStyles.metadataLabel}>
                <FormattedMessage
                  id="codex.security.findings.detail.locations.label"
                  defaultMessage="Affected locations"
                  description="Repository-relative files and lines identified by a Security finding."
                />
              </dt>
              <dd
                className={`${workbenchStyles.metadataValue} flex flex-wrap gap-x-4 gap-y-1`}
              >
                {finding.locations?.length
                  ? finding.locations.map((location) => {
                      const path = location.path
                        .split("/")
                        .map(encodeURIComponent)
                        .join("/");
                      const anchor = location.start_line
                        ? `#L${location.start_line}${
                            location.end_line &&
                            location.end_line > location.start_line
                              ? `-L${location.end_line}`
                              : ""
                          }`
                        : "";
                      const href =
                        repositoryHref && revision
                          ? `${repositoryHref}/blob/${encodeURIComponent(
                              revision,
                            )}/${path}${anchor}`
                          : null;
                      return (
                        <div
                          className="font-mono break-all"
                          key={`${location.path}:${location.start_line}:${location.end_line}`}
                        >
                          {href ? (
                            <ExternalLink
                              href={href}
                              className={workbenchStyles.link}
                            >
                              {locationLabel(location)}
                            </ExternalLink>
                          ) : (
                            locationLabel(location)
                          )}
                        </div>
                      );
                    })
                  : "—"}
              </dd>
            </div>
          </dl>
          <div className="space-y-2 text-sm text-secondary">
            <WorkbenchScanTypeBadge scanType={finding.source.kind} />
            <Badge variant="outline">
              <FormattedMessage
                id="codex.security.findings.detail.read_only.label"
                defaultMessage="Read-only result"
                description="Capability label on a saved repository finding whose triage fields cannot be changed."
              />
            </Badge>
          </div>
        </aside>
      </div>
    </section>
  );
}

function RepositoryEvidenceSection({
  title,
  value,
}: {
  title: ReactNode;
  value: string;
}) {
  if (!value) return null;
  return (
    <section className="df-finding-report-section">
      <h2>{title}</h2>
      <p className="df-finding-report-body whitespace-pre-wrap">{value}</p>
    </section>
  );
}
