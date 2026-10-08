import type { components } from "@oai/aardvark-client/components";
import { SegmentedControl } from "@oai/ds/ui/segmented-control";
import { User } from "@oai/ds/icons/user";
import { Avatar } from "@oai/ds/ui/avatar";
import type { ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { ExternalLink } from "../link";
import { DateTime, Report, repositoryLabel } from "../ui";
import { CLOSED_FINDING_STATUSES, shortHash } from "./findings-utils";
import {
  FindingMetadataRow,
  FindingSeverityBadge,
  FindingStatusBadge,
} from "./finding-detail-layout";
import { WorkbenchState } from "./layout";
import { STATUS_MESSAGES } from "./messages";
import { workbenchStyles } from "./styles";

type CommitFinding = components["schemas"]["ScanFindingResponse"];

export function isFindingPatchPending(finding: CommitFinding) {
  return (
    finding.manual_patch_request_status === "queued" ||
    finding.manual_patch_request_status === "running" ||
    finding.proposed_patch?.status === "in_progress"
  );
}

export function CommitFindingArchiveBanner({
  finding,
}: {
  finding: CommitFinding;
}) {
  const intl = useIntl();
  if (!CLOSED_FINDING_STATUSES.includes(finding.status)) return null;

  const email = finding.resolution_set_by_email?.trim();
  const reason = finding.resolution_reason?.trim();
  const automatic = !email && reason?.startsWith("Auto-closed by Aardvark");
  const statusLabel = intl.formatMessage(STATUS_MESSAGES[finding.status]);

  return (
    <WorkbenchState variant="inline">
      {automatic ? (
        <FormattedMessage
          id="codex.security.findings.detail.closed.automatic"
          defaultMessage="This finding was automatically closed because the issue is no longer detected."
          description="Banner shown when Security automatically closes a finding that is no longer detected."
        />
      ) : email ? (
        <FormattedMessage
          id="codex.security.findings.detail.closed.by_user"
          defaultMessage="Closed by {email}. Reason: {statusLabel}.{reason}"
          description="Banner identifying who closed a Security finding, why it was closed, and optional extra context."
          values={{
            email,
            statusLabel,
            reason: reason ? ` ${reason}` : "",
          }}
        />
      ) : (
        <FormattedMessage
          id="codex.security.findings.detail.closed"
          defaultMessage="Closed. Reason: {statusLabel}.{reason}"
          description="Banner explaining why a Security finding is closed when no user email is available."
          values={{
            statusLabel,
            reason: reason ? ` ${reason}` : "",
          }}
        />
      )}
    </WorkbenchState>
  );
}

export function CommitFindingMetadata({ finding }: { finding: CommitFinding }) {
  const analysis = finding.commit_analysis;
  const hash = analysis?.commit_hash ?? "";
  const repositoryHref = githubRepositoryUrl(finding.repo_url);
  const commitHref =
    repositoryHref && hash
      ? `${repositoryHref}/commit/${encodeURIComponent(hash)}`
      : null;
  const author = stripSurroundingQuotes(
    analysis?.author ?? analysis?.author_email ?? "",
  );
  const committedAt =
    analysis?.committer_date ?? analysis?.author_date ?? finding.created_at;

  return (
    <dl className="df-finding-metadata">
      <FindingMetadataRow
        label={
          <FormattedMessage
            id="codex.security.findings.detail.severity.label"
            defaultMessage="Severity"
            description="Severity metadata label on a commit-scan finding."
          />
        }
      >
        <FindingSeverityBadge severity={finding.criticality} />
      </FindingMetadataRow>
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
      <FindingMetadataRow
        label={
          <FormattedMessage
            id="defenseFactory.finding.metadata.owner"
            defaultMessage="Owner"
            description="Person assigned to this finding."
          />
        }
      >
        <div className="flex items-center gap-2">
          <Avatar size={24} color="secondary" variant="solid" Icon={User} />
          <span className="min-w-0">
            {finding.assignee?.name || finding.assignee?.email || (
              <FormattedMessage
                id="defenseFactory.finding.metadata.unassigned"
                defaultMessage="Unassigned"
                description="No person is currently assigned to this finding."
              />
            )}
          </span>
        </div>
      </FindingMetadataRow>
      <FindingMetadataRow
        label={
          <FormattedMessage
            id="codex.security.findings.detail.commit.label"
            defaultMessage="Commit"
            description="Commit metadata label on a commit-scan finding."
          />
        }
      >
        <div className="flex flex-wrap items-baseline gap-x-2 gap-y-1">
          {commitHref ? (
            <ExternalLink
              href={commitHref}
              className={`${workbenchStyles.link} font-mono text-sm`}
            >
              {shortHash(hash)}
            </ExternalLink>
          ) : (
            <span className="font-mono text-sm">{hash || "—"}</span>
          )}
          <span className="text-token-text-tertiary text-xs leading-5">
            <DateTime value={committedAt} />
          </span>
        </div>
        {author ? (
          <p className="text-token-text-tertiary text-xs leading-5 break-words">
            <FormattedMessage
              id="codex.security.findings.detail.commit.author"
              defaultMessage="by {author}"
              description="Author shown beneath the commit on a Security finding."
              values={{ author }}
            />
          </p>
        ) : null}
      </FindingMetadataRow>
      <FindingMetadataRow
        label={
          <FormattedMessage
            id="codex.security.findings.detail.repository.label"
            defaultMessage="Repository"
            description="Repository metadata label on a commit-scan finding."
          />
        }
      >
        {repositoryHref ? (
          <ExternalLink href={repositoryHref} className={workbenchStyles.link}>
            {repositoryLabel(finding.repo_url)}
          </ExternalLink>
        ) : (
          repositoryLabel(finding.repo_url)
        )}
      </FindingMetadataRow>
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
    </dl>
  );
}

export function CommitFindingViewToggle({
  showPatch,
  onShowReport,
  onShowPatch,
  patchAvailable,
}: {
  showPatch: boolean;
  onShowReport: () => void;
  onShowPatch: () => void;
  patchAvailable: boolean;
}) {
  const intl = useIntl();
  return (
    <SegmentedControl
      value={showPatch ? "patch" : "report"}
      onChange={(id) => (id === "patch" ? onShowPatch() : onShowReport())}
      size="md"
      gutterSize="md"
      variant="ghost"
      pill
      className="df-finding-content-toggle w-fit"
      aria-label={intl.formatMessage({
        id: "defenseFactory.finding.view.label",
        defaultMessage: "Finding content",
        description:
          "Accessible label for choosing the finding report or patch.",
      })}
    >
      <SegmentedControl.Option value="report">
        {intl.formatMessage({
          id: "codex.security.findings.detail.report.label",
          defaultMessage: "Report",
          description:
            "Segmented control option for the Security finding report.",
        })}
      </SegmentedControl.Option>
      <SegmentedControl.Option value="patch" disabled={!patchAvailable}>
        {intl.formatMessage({
          id: "codex.security.findings.detail.patch.label",
          defaultMessage: "Patch",
          description:
            "Segmented control option for the proposed Security fix.",
        })}
      </SegmentedControl.Option>
    </SegmentedControl>
  );
}

export function CommitFindingReport({ finding }: { finding: CommitFinding }) {
  const analysis = finding.commit_analysis;
  const summary = [analysis?.bugs_found_or_fixed, analysis?.description]
    .filter((value, index, values): value is string =>
      Boolean(value && values.indexOf(value) === index),
    )
    .join("\n\n");
  const validationRubric = analysis?.validation_rubric
    ?.replace(/\\n/g, "\n")
    .trim();
  const validationReport = (
    analysis?.validation_report ?? analysis?.validation_str
  )?.trim();
  const validationArtifactUrl = analysis?.validation_artifact?.download_url;
  const relevantLines = analysis?.relevant_lines ?? [];

  return (
    <div className="space-y-8">
      <ContentSection
        title={
          <FormattedMessage
            id="codex.security.findings.detail.summary.label"
            defaultMessage="Summary"
            description="Heading for the summary of a Security finding."
          />
        }
      >
        {summary ? (
          <Report>{summary}</Report>
        ) : (
          <EmptyContent>
            <FormattedMessage
              id="codex.security.findings.detail.summary.empty"
              defaultMessage="No summary available for this finding yet."
              description="Fallback shown when a Security finding has no summary."
            />
          </EmptyContent>
        )}
      </ContentSection>

      {validationRubric || validationReport || validationArtifactUrl ? (
        <ContentSection
          title={
            <FormattedMessage
              id="codex.security.findings.detail.validation.label"
              defaultMessage="Validation"
              description="Heading for validation details on a Security finding."
            />
          }
        >
          <div className="space-y-4">
            {validationRubric ? <Report>{validationRubric}</Report> : null}
            {validationReport && validationReport !== validationRubric ? (
              <Report>{validationReport}</Report>
            ) : null}
            {validationArtifactUrl ? (
              <ExternalLink
                href={validationArtifactUrl}
                className={workbenchStyles.link}
              >
                <FormattedMessage
                  id="codex.security.findings.detail.validation.artifact.label"
                  defaultMessage="Validation artifact"
                  description="Link label for a Security finding validation artifact."
                />
              </ExternalLink>
            ) : null}
          </div>
        </ContentSection>
      ) : null}

      <ContentSection
        title={
          <FormattedMessage
            id="codex.security.findings.detail.evidence.label"
            defaultMessage="Evidence"
            description="Heading for vulnerable code evidence on a Security finding."
          />
        }
      >
        {relevantLines.length ? (
          <div className="space-y-6">
            {relevantLines.map((line, index) => (
              <div
                key={`${line.path}:${line.start_line_number}:${line.end_line_number}:${index}`}
                className="min-w-0 space-y-3"
              >
                <div className="text-token-text-secondary font-mono text-xs break-all">
                  {line.path}:L{formatLineRange(line)}
                </div>
                {line.content ? (
                  <pre className="bg-token-bg-secondary-surface max-w-full overflow-x-auto rounded-xl p-4 text-sm whitespace-pre">
                    {line.content}
                  </pre>
                ) : null}
                {line.comment ? <Report>{line.comment}</Report> : null}
              </div>
            ))}
          </div>
        ) : (
          <EmptyContent>
            <FormattedMessage
              id="codex.security.findings.detail.evidence.empty"
              defaultMessage="No evidence available."
              description="Fallback shown when a Security finding has no vulnerable code evidence."
            />
          </EmptyContent>
        )}
      </ContentSection>

      {analysis?.attack_path_analysis ? (
        <ContentSection
          title={
            <FormattedMessage
              id="codex.security.findings.detail.attack_path.label"
              defaultMessage="Attack-path analysis"
              description="Heading for attack-path analysis on a Security finding."
            />
          }
        >
          <AttackPathContent
            value={analysis.attack_path_analysis}
            fallbackAdjustmentReason={analysis.attack_path_adjustment_reason}
          />
        </ContentSection>
      ) : null}
    </div>
  );
}

export function CommitFindingPatch({
  finding,
  description,
  patch,
  pullRequestUrl,
}: {
  finding: CommitFinding;
  description: string;
  patch: string;
  pullRequestUrl: string | null;
}) {
  const pending = isFindingPatchPending(finding);
  const latestTask = finding.proposed_patch?.latest_task;
  const failure =
    latestTask?.patch_generation_success === false
      ? latestTask.patch_generation_failure_message ||
        latestTask.patch_generation_failure_reason
      : null;

  if (pending && !patch) {
    return (
      <WorkbenchState loading>
        <FormattedMessage
          id="codex.security.findings.detail.patch.generating"
          defaultMessage="Generating patch…"
          description="Status shown while Codex generates a patch for a Security finding."
        />
      </WorkbenchState>
    );
  }

  if (failure && !patch) {
    return (
      <WorkbenchState variant="inline">
        <FormattedMessage
          id="codex.security.findings.detail.patch.failed"
          defaultMessage="Patch generation failed: {failure}"
          description="Failure shown when a proposed Security patch could not be generated."
          values={{ failure }}
        />
      </WorkbenchState>
    );
  }

  if (!patch && !description) {
    return (
      <EmptyContent>
        <FormattedMessage
          id="codex.security.findings.detail.patch.empty"
          defaultMessage="Patch details are not available yet."
          description="Fallback shown when a Security patch has no details yet."
        />
      </EmptyContent>
    );
  }

  return (
    <div className="space-y-6">
      {description ? <Report>{description}</Report> : null}
      {patch ? (
        <pre className="bg-token-bg-secondary-surface max-w-full overflow-x-auto rounded-xl p-4 text-sm whitespace-pre">
          {patch}
        </pre>
      ) : null}
      {pullRequestUrl ? (
        <ExternalLink href={pullRequestUrl} className={workbenchStyles.link}>
          <FormattedMessage
            id="defenseFactory.plugin.viewPr"
            defaultMessage="View pull request"
            description="Open the existing fix pull request"
          />
        </ExternalLink>
      ) : null}
    </div>
  );
}

function ContentSection({
  title,
  children,
}: {
  title: ReactNode;
  children: ReactNode;
}) {
  return (
    <section className="df-finding-report-section">
      <h2>{title}</h2>
      <div className="df-finding-report-body">{children}</div>
    </section>
  );
}

function EmptyContent({ children }: { children: ReactNode }) {
  return <p className="text-token-text-secondary text-sm">{children}</p>;
}

function AttackPathContent({
  value,
  fallbackAdjustmentReason,
}: {
  value: components["schemas"]["AttackPathAnalysis"];
  fallbackAdjustmentReason?: string | null;
}) {
  const adjustmentReason =
    displayString(value.adjustment_reason) ||
    displayString(fallbackAdjustmentReason);
  const likelihood = levelAndReason(value.likelihood);
  const impact = levelAndReason(value.impact);
  const assumptions = uniqueStrings([
    ...(value.assumptions ?? []),
    ...(value.facts?.precondition?.requires ?? []),
  ]);
  const controls = uniqueStrings(value.controls ?? []);
  const blindspots = uniqueStrings(value.blindspots ?? []);
  const recommendations = uniqueStrings(value.recommendations ?? []);
  const diagram = formatAttackPathDiagram(value.attack_path);
  const narrative = displayString(value.narrative);
  const hasStructuredSummary =
    adjustmentReason ||
    likelihood ||
    impact ||
    assumptions.length ||
    controls.length ||
    blindspots.length ||
    recommendations.length ||
    diagram ||
    narrative;

  if (!hasStructuredSummary) {
    return (
      <pre className="max-w-full overflow-x-auto text-sm whitespace-pre-wrap">
        {JSON.stringify(value, null, 2)}
      </pre>
    );
  }

  return (
    <div className="space-y-4 text-sm leading-6">
      {adjustmentReason ? <p>{adjustmentReason}</p> : null}
      {diagram || narrative ? (
        <div className="space-y-2">
          <h3 className="text-token-text-tertiary font-medium">
            <FormattedMessage
              id="codex.security.findings.detail.attack_path.path.label"
              defaultMessage="Path"
              description="Heading for the attack path diagram and narrative."
            />
          </h3>
          {diagram ? (
            <pre className="bg-token-bg-tertiary overflow-x-auto rounded-xl p-3 text-xs leading-5 whitespace-pre-wrap">
              {diagram}
            </pre>
          ) : null}
          {narrative ? <Report>{narrative}</Report> : null}
        </div>
      ) : null}
      {likelihood || impact ? (
        <div className="grid gap-3 md:grid-cols-2">
          <InfoField
            label={
              <FormattedMessage
                id="codex.security.findings.detail.attack_path.likelihood.label"
                defaultMessage="Likelihood"
                description="Label for attack-path likelihood."
              />
            }
            value={likelihood}
          />
          <InfoField
            label={
              <FormattedMessage
                id="codex.security.findings.detail.attack_path.impact.label"
                defaultMessage="Impact"
                description="Label for attack-path impact."
              />
            }
            value={impact}
          />
        </div>
      ) : null}
      <InfoList
        title={
          <FormattedMessage
            id="codex.security.findings.detail.attack_path.assumptions.label"
            defaultMessage="Assumptions"
            description="Heading for attack-path assumptions."
          />
        }
        items={assumptions}
      />
      <InfoList
        title={
          <FormattedMessage
            id="codex.security.findings.detail.attack_path.controls.label"
            defaultMessage="Controls"
            description="Heading for attack-path controls."
          />
        }
        items={controls}
      />
      <InfoList
        title={
          <FormattedMessage
            id="codex.security.findings.detail.attack_path.blindspots.label"
            defaultMessage="Blindspots"
            description="Heading for attack-path blindspots."
          />
        }
        items={blindspots}
      />
      <InfoList
        title={
          <FormattedMessage
            id="codex.security.findings.detail.attack_path.recommendations.label"
            defaultMessage="Recommendations"
            description="Heading for remediation recommendations in attack-path analysis."
          />
        }
        items={recommendations}
      />
    </div>
  );
}

function InfoField({
  label,
  value,
}: {
  label: ReactNode;
  value: string | null;
}) {
  if (!value) return null;
  return (
    <div>
      <div className="text-token-text-tertiary font-medium">{label}</div>
      <div className="mt-1">{value}</div>
    </div>
  );
}

function InfoList({ title, items }: { title: ReactNode; items: string[] }) {
  if (!items.length) return null;
  return (
    <div className="space-y-2">
      <h3 className="text-token-text-tertiary font-medium">{title}</h3>
      <ul className="list-disc space-y-1 ps-5">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

function levelAndReason(
  value:
    | components["schemas"]["LikelihoodInfo"]
    | components["schemas"]["ImpactInfo"]
    | null
    | undefined,
) {
  const level = displayString(value?.level);
  const reason = displayString(value?.why);
  if (!level && !reason) return null;
  const label = level
    ? level.charAt(0).toUpperCase() + level.slice(1)
    : "Unknown";
  return reason ? `${label} — ${reason}` : label;
}

function formatAttackPathDiagram(
  graph: components["schemas"]["AttackPathGraph"] | null | undefined,
) {
  if (!graph) return "";
  const nodes = graph.nodes ?? [];
  if (!nodes.length) return displayString(graph.ascii);

  const nodeById = new Map(nodes.map((node) => [node.id, node.label]));
  const edges = graph.edges ?? [];
  const nextById = new Map(edges.map((edge) => [edge.from_id, edge]));
  const orderedIds: string[] = [];
  const visited = new Set<string>();
  let currentId: string | undefined = graph.entry || nodes[0]?.id;

  while (currentId && !visited.has(currentId)) {
    visited.add(currentId);
    orderedIds.push(currentId);
    currentId = nextById.get(currentId)?.to_id;
  }

  if (!orderedIds.length) return displayString(graph.ascii);
  return orderedIds
    .flatMap((id, index) => {
      const nextId = orderedIds[index + 1];
      const label = nodeById.get(id) ?? id;
      if (!nextId) return [label];
      const edgeLabel = edges.find(
        (edge) => edge.from_id === id && edge.to_id === nextId,
      )?.label;
      return [label, edgeLabel ? ` --${edgeLabel}--> ` : " → "];
    })
    .join("");
}

function uniqueStrings(values: Array<string | null | undefined>) {
  return Array.from(
    new Set(
      values
        .map((value) => value?.trim())
        .filter((value): value is string => Boolean(value)),
    ),
  );
}

function displayString(value: unknown) {
  return typeof value === "string" ? value.trim() : "";
}

function formatLineRange(line: components["schemas"]["RelevantLine"]): string {
  return line.end_line_number > line.start_line_number
    ? `${line.start_line_number}-L${line.end_line_number}`
    : String(line.start_line_number);
}

function githubRepositoryUrl(value: string): string | null {
  try {
    const url = new URL(value.replace(/\.git$/, ""));
    if (url.origin !== "https://github.com" || url.username || url.password) {
      return null;
    }
    return `${url.origin}${url.pathname.replace(/\/+$/, "")}`;
  } catch {
    return null;
  }
}

function stripSurroundingQuotes(value: string) {
  const trimmed = value.trim();
  if (
    (trimmed.startsWith('"') && trimmed.endsWith('"')) ||
    (trimmed.startsWith("'") && trimmed.endsWith("'"))
  ) {
    return trimmed.slice(1, -1).trim();
  }
  return trimmed;
}
