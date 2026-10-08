import type { components } from "@oai/aardvark-client/components";
import { ComposeEditSquare } from "@oai/ds/icons/compose-edit-square";
import { DotsHorizontal as DotsHorizontalIcon } from "@oai/ds/icons/dots-horizontal";
import { Github } from "@oai/ds/icons/github";
import { ThumbDown as ThumbDownIcon } from "@oai/ds/icons/thumb-down";
import { ThumbUp as ThumbUpIcon } from "@oai/ds/icons/thumb-up";
import { Menu } from "@oai/ds/ui/menu";
import { Select } from "@oai/ds/ui/select";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation } from "react-router";

import {
  copyText,
  getShareUrl,
  logSecurityEvent,
  securityClient,
} from "./client";
import { useCloud } from "./app-context";
import { FindingChat } from "./finding-chat";
import { statusLabel } from "./labels";
import { ExternalLink } from "./link";
import { findingPatch } from "./patch-model";
import { RequestState, Section } from "./ui";
import {
  CommitFindingArchiveBanner,
  CommitFindingMetadata,
  CommitFindingPatch,
  CommitFindingReport,
  CommitFindingViewToggle,
  isFindingPatchPending,
} from "./workbench/commit-finding-content";
import {
  WorkbenchButton as Button,
  WorkbenchInput as Input,
} from "./workbench/controls";
import {
  FindingDetailHeading,
  FindingDetailToolbar,
} from "./workbench/finding-detail-layout";
import { WorkbenchState } from "./workbench/layout";
import { RepositoryFindingDetail } from "./workbench/repository-finding-detail";

function normalizeRepositoryUrlForLookup(url: string): string {
  return url
    .trim()
    .replace(/\/+$/, "")
    .replace(/\.git$/, "")
    .replace(/\/+$/, "");
}

function matchesRepositoryScope(
  finding: components["schemas"]["FindingDetail"],
  repositoryId: string | null,
  repositoryUrl: string | null,
): boolean {
  if (repositoryId) return finding.repo_id === repositoryId;
  if (!repositoryUrl) return true;
  const actual = finding.repo_url.trim().replace(/\/+$/, "");
  const expected = repositoryUrl.trim().replace(/\/+$/, "");
  if (actual.toLowerCase() === expected.toLowerCase()) return true;
  const normalizedActual =
    finding.source.kind === "repository_scan"
      ? actual
      : normalizeRepositoryUrlForLookup(actual);
  return (
    normalizedActual.toLowerCase() ===
    normalizeRepositoryUrlForLookup(expected).toLowerCase()
  );
}

export function FindingDetail({
  id,
  repositoryId = null,
  repositoryUrl = null,
}: {
  id: string;
  repositoryId?: string | null;
  repositoryUrl?: string | null;
}) {
  const cloud = useCloud();
  const {
    data: finding,
    isPending,
    isFetching,
    isFetchedAfterMount,
    error,
    refetch,
  } = useQuery({
    queryKey: ["finding", cloud.accountId, cloud.identity?.userId, id],
    queryFn: () =>
      securityClient.request({
        operation: "findings_get",
        parameters: { path: { finding_id: id } },
      }),
    staleTime: 15_000,
    refetchOnMount: "always",
    refetchInterval: (query) => {
      const commit = query.state.data?.commit_detail;
      return commit && isFindingPatchPending(commit) ? 4_000 : false;
    },
  });
  if (isPending || (isFetching && !isFetchedAfterMount))
    return (
      <WorkbenchState loading variant="panel">
        <FormattedMessage
          id="codex.security.findings.detail.loading"
          defaultMessage="Loading finding…"
          description="Loading status while an authorized Security finding is retrieved."
        />
      </WorkbenchState>
    );
  if (
    error ||
    !finding ||
    !matchesRepositoryScope(finding, repositoryId, repositoryUrl)
  )
    return (
      <WorkbenchState
        variant="panel"
        action={
          <Button
            color="secondary"
            type="button"
            onClick={() => void refetch()}
          >
            <FormattedMessage
              id="codex.security.findings.detail.retry.label"
              defaultMessage="Retry"
              description="Retry loading the current authorized Security finding."
            />
          </Button>
        }
      >
        <FormattedMessage
          id="codex.security.findings.detail.unavailable"
          defaultMessage="This finding could not be loaded."
          description="Privacy-preserving error when a Security finding is unavailable or inaccessible."
        />
      </WorkbenchState>
    );
  if (!finding.commit_detail) {
    return <RepositoryFindingDetail finding={finding} />;
  }
  return (
    <CommitFinding
      key={finding.commit_detail.hid}
      finding={finding.commit_detail}
      title={finding.title}
      refresh={() => refetch()}
    />
  );
}

function CommitFinding({
  finding,
  title,
  refresh,
}: {
  title: string;
  finding: components["schemas"]["ScanFindingResponse"];
  refresh: () => Promise<unknown>;
}) {
  const location = useLocation();
  const cache = useQueryClient();
  const intl = useIntl();
  const [editing, setEditing] = useState(false);
  const [status, setStatus] = useState(finding.status);
  const [severity, setSeverity] = useState(finding.criticality);
  const [reason, setReason] = useState("");
  const [assignee, setAssignee] = useState(finding.assignee?.email ?? "");
  const [showPatch, setShowPatch] = useState(false);
  const { patch, description, pullRequestUrl } = findingPatch(finding);
  const patchPending = isFindingPatchPending(finding);
  const {
    mutate: update,
    error,
    isPending,
  } = useMutation({
    mutationFn: (body: components["schemas"]["ScanFindingUpdate"]) =>
      securityClient.request({
        operation: "findings_update",
        parameters: { path: { id: finding.hid } },
        requestBody: { ...body, version: finding.version },
      }),
    onSuccess: async () => {
      setEditing(false);
      await Promise.all([
        refresh(),
        cache.invalidateQueries({ queryKey: ["findings"] }),
      ]);
    },
  });
  const {
    mutate: createPr,
    error: prError,
    isPending: creatingPr,
  } = useMutation({
    mutationFn: () =>
      securityClient.request({
        operation: "findings_create_pr",
        parameters: { path: { id: finding.hid } },
        requestBody: { mode: "draft" },
      }),
    onSuccess: refresh,
  });
  const {
    mutate: copy,
    error: copyError,
    isSuccess: copied,
  } = useMutation({
    mutationFn: async (link: boolean) => {
      const analysis = finding.commit_analysis;
      await copyText(
        link
          ? await getShareUrl(`${location.pathname}${location.search}`)
          : [
              title,
              `Repository: ${finding.repo_url}`,
              `Commit: ${analysis?.commit_hash ?? ""}`,
              `Author: ${analysis?.author_email ?? ""}`,
              `Created: ${finding.created_at}`,
              `Assignee: ${
                finding.assignee?.name ??
                finding.assignee?.email ??
                "Unassigned"
              }`,
              `Severity: ${finding.criticality}`,
              `Status: ${finding.status}`,
              finding.criticality_reason,
              finding.resolution_reason,
              analysis?.bugs_found_or_fixed,
              analysis?.description,
              analysis?.validation_rubric,
              analysis?.validation_report ?? analysis?.validation_str,
              patch,
              JSON.stringify(
                {
                  relevant_lines: analysis?.relevant_lines,
                  attack_path_analysis: analysis?.attack_path_analysis,
                },
                null,
                2,
              ),
            ]
              .filter(Boolean)
              .join("\n\n"),
      );
      logSecurityEvent({
        name: link
          ? "CodexSecurityFindingShared"
          : "CodexSecurityFindingCopied",
        data: {
          scanFindingId: finding.id,
          scanFindingDisplayId: finding.hid,
          status: finding.status,
          criticality: finding.criticality,
          patchGenerated:
            finding.commit_analysis?.proposed_patch_generated === true,
          sourcePage: "detail",
        },
      });
    },
  });
  function viewPatch() {
    if (!showPatch)
      logSecurityEvent({
        name: "CodexSecurityPatchViewed",
        data: {
          scanFindingId: finding.id,
          scanFindingDisplayId: finding.hid,
          status: finding.status,
          criticality: finding.criticality,
          patchGenerated:
            finding.commit_analysis?.proposed_patch_generated === true,
          patchId: finding.proposed_patch?.id,
          patchStatus: finding.proposed_patch?.status,
          patchGenerationSuccess:
            finding.proposed_patch?.latest_task?.patch_generation_success ??
            undefined,
          patchGenerationFailureReason:
            finding.proposed_patch?.latest_task
              ?.patch_generation_failure_reason ?? undefined,
        },
      });
    setShowPatch(true);
  }
  const {
    mutate: feedback,
    error: feedbackError,
    isSuccess: feedbackSaved,
    isPending: feedbackPending,
  } = useMutation({
    mutationFn: (rating: "thumbs_up" | "thumbs_down") =>
      securityClient.request({
        operation: "findings_feedback",
        parameters: { path: { id: finding.hid } },
        requestBody: { thumb_rating: rating },
      }),
  });
  return (
    <section className="df-finding-detail">
      <FindingDetailToolbar
        actions={
          <>
            {pullRequestUrl ? (
              <ExternalLink
                className="df-button df-control inline-flex items-center gap-1 border border-default px-3 text-secondary"
                href={pullRequestUrl}
              >
                <Github className="size-4" aria-hidden />
                <FormattedMessage
                  id="defenseFactory.plugin.viewPr"
                  defaultMessage="View pull request"
                  description="Open the existing fix pull request"
                />
              </ExternalLink>
            ) : patch ? (
              <Button
                color="outlineSurface"
                onClick={() => createPr()}
                loading={creatingPr}
              >
                <Github className="size-4" aria-hidden />
                <FormattedMessage
                  id="defenseFactory.plugin.createPr"
                  defaultMessage="Create draft pull request"
                  description="Create a draft pull request for the generated fix"
                />
              </Button>
            ) : (
              <Button
                color="secondary"
                disabled={isPending || patchPending}
                onClick={() => update({ manual_patch_requested: true })}
              >
                <ComposeEditSquare className="size-4" aria-hidden />
                {patchPending ? (
                  <FormattedMessage
                    id="codex.security.findings.detail.patch.generating.action"
                    defaultMessage="Generating patch"
                    description="Disabled action label while Codex generates a patch."
                  />
                ) : (
                  <FormattedMessage
                    id="codex.security.findings.detail.patch.request.action"
                    defaultMessage="Fix with Codex"
                    description="Action that requests a generated patch for a Security finding."
                  />
                )}
              </Button>
            )}
            <Menu>
              <Menu.Trigger>
                <Button
                  type="button"
                  color="ghost"
                  size="iconCircle"
                  uniform
                  aria-label={intl.formatMessage({
                    id: "codex.security.findings.detail.actions.more.label",
                    defaultMessage: "More finding actions",
                    description:
                      "Accessible label for the overflow menu on a Security finding.",
                  })}
                >
                  <DotsHorizontalIcon className="icon-sm" aria-hidden />
                </Button>
              </Menu.Trigger>
              <Menu.Content align="end" minWidth={190}>
                <Menu.Item
                  onSelect={() => {
                    setStatus(finding.status);
                    setSeverity(finding.criticality);
                    setAssignee(finding.assignee?.email ?? "");
                    setReason("");
                    setEditing(!editing);
                  }}
                >
                  <FormattedMessage
                    id="defenseFactory.plugin.triage"
                    defaultMessage="Triage finding"
                    description="Edit finding status, severity, and assignee"
                  />
                </Menu.Item>
                <Menu.Item onSelect={() => copy(false)}>
                  <FormattedMessage
                    id="defenseFactory.plugin.copyFinding"
                    defaultMessage="Copy finding"
                    description="Copy the finding report and saved evidence"
                  />
                </Menu.Item>
                <Menu.Item onSelect={() => copy(true)}>
                  <FormattedMessage
                    id="defenseFactory.plugin.copyFindingLink"
                    defaultMessage="Copy link"
                    description="Copy the shareable finding URL"
                  />
                </Menu.Item>
                <Menu.Item onSelect={() => void refresh()}>
                  <FormattedMessage
                    id="defenseFactory.plugin.refresh"
                    defaultMessage="Refresh"
                    description="Reload the current data"
                  />
                </Menu.Item>
              </Menu.Content>
            </Menu>
          </>
        }
      />
      <div className="df-finding-detail-notice">
        <CommitFindingArchiveBanner finding={finding} />
      </div>
      {copied ? (
        <span role="status" className="text-token-text-secondary text-sm">
          <FormattedMessage
            id="defenseFactory.plugin.copied"
            defaultMessage="Copied"
            description="Finding content or link was copied to the clipboard"
          />
        </span>
      ) : null}

      <div className="df-finding-detail-grid">
        <div className="df-finding-detail-main">
          <FindingDetailHeading
            title={title}
            status={finding.status}
            updatedAt={finding.updated_at}
          />
          <CommitFindingViewToggle
            showPatch={showPatch}
            onShowReport={() => setShowPatch(false)}
            onShowPatch={viewPatch}
            patchAvailable={Boolean(finding.proposed_patch) || patchPending}
          />
          <div className="min-w-0">
            {showPatch ? (
              <CommitFindingPatch
                finding={finding}
                description={description}
                patch={patch}
                pullRequestUrl={pullRequestUrl}
              />
            ) : (
              <CommitFindingReport finding={finding} />
            )}
          </div>
          <div
            role="group"
            aria-label={intl.formatMessage({
              id: "codex.security.findings.detail.feedback.group.label",
              defaultMessage: "Give feedback on this finding",
              description:
                "Accessible label for feedback controls on a Security finding.",
            })}
            className="flex items-center gap-1"
          >
            <Button
              color="ghostSecondary"
              uniform
              disabled={feedbackPending}
              aria-label={intl.formatMessage({
                id: "codex.security.findings.detail.feedback.positive.label",
                defaultMessage: "Give thumbs up feedback",
                description: "Accessible label for positive finding feedback.",
              })}
              onClick={() => feedback("thumbs_up")}
            >
              <ThumbUpIcon className="icon-sm" aria-hidden />
            </Button>
            <Button
              color="ghostSecondary"
              uniform
              disabled={feedbackPending}
              aria-label={intl.formatMessage({
                id: "codex.security.findings.detail.feedback.negative.label",
                defaultMessage: "Give thumbs down feedback",
                description: "Accessible label for negative finding feedback.",
              })}
              onClick={() => feedback("thumbs_down")}
            >
              <ThumbDownIcon className="icon-sm" aria-hidden />
            </Button>
            {feedbackSaved && (
              <span role="status" className="text-token-text-secondary text-sm">
                <FormattedMessage
                  id="defenseFactory.plugin.feedbackSaved"
                  defaultMessage="Feedback saved"
                  description="Feedback was submitted"
                />
              </span>
            )}
          </div>
        </div>

        <aside className="df-finding-detail-aside">
          <CommitFindingMetadata finding={finding} />
          <FindingChat
            id={finding.hid}
            existingTaskId={finding.followup_task_id}
          />
          {editing && (
            <Section
              title={
                <FormattedMessage
                  id="defenseFactory.plugin.triage"
                  defaultMessage="Triage finding"
                  description="Edit finding status, severity, and assignee"
                />
              }
            >
              <form
                className="flex flex-col gap-4"
                onSubmit={(event) => {
                  event.preventDefault();
                  update({
                    status: status !== finding.status ? status : undefined,
                    criticality:
                      severity !== finding.criticality ? severity : undefined,
                    resolution_reason:
                      status !== finding.status ? reason || null : undefined,
                    criticality_reason:
                      severity !== finding.criticality
                        ? reason || null
                        : undefined,
                    assignee_user_email:
                      assignee !== (finding.assignee?.email ?? "")
                        ? assignee || null
                        : undefined,
                  });
                }}
              >
                <div className="flex flex-wrap gap-3">
                  <Select
                    triggerClassName="df-control"
                    value={status}
                    options={[
                      "new",
                      "triaged",
                      "in_progress",
                      "fixed",
                      "wontfix",
                      "duplicate",
                      "false_positive",
                    ].map((value) => ({
                      value,
                      label: statusLabel(intl, value),
                    }))}
                    onChange={(option) =>
                      setStatus(option.value as typeof status)
                    }
                  />
                  <Select
                    triggerClassName="df-control"
                    value={severity}
                    options={[
                      "critical",
                      "high",
                      "medium",
                      "low",
                      "informational",
                    ].map((value) => ({
                      value,
                      label: statusLabel(intl, value),
                    }))}
                    onChange={(option) =>
                      setSeverity(option.value as typeof severity)
                    }
                  />
                </div>
                <label className="flex flex-col gap-2 text-[14px]">
                  <FormattedMessage
                    id="defenseFactory.plugin.assignee"
                    defaultMessage="Assignee email"
                    description="Email of the person assigned to this finding"
                  />
                  <Input
                    value={assignee}
                    onChange={(e) => setAssignee(e.target.value)}
                    type="email"
                  />
                </label>
                <label className="flex flex-col gap-2 text-[14px]">
                  <FormattedMessage
                    id="defenseFactory.plugin.reason"
                    defaultMessage="Reason"
                    description="Explanation of a finding status or severity change"
                  />
                  <Input
                    value={reason}
                    onChange={(e) => setReason(e.target.value)}
                  />
                </label>
                <div>
                  <Button color="primary" type="submit" loading={isPending}>
                    <FormattedMessage
                      id="defenseFactory.plugin.save"
                      defaultMessage="Save"
                      description="Save changes"
                    />
                  </Button>
                </div>
              </form>
            </Section>
          )}
          {(error || prError || feedbackError || copyError) && (
            <RequestState
              error={error ?? prError ?? feedbackError ?? copyError}
            />
          )}
        </aside>
      </div>
    </section>
  );
}
