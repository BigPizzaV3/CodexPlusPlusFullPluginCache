import { useId } from "react";
import { FormattedMessage, FormattedRelativeTime, useIntl } from "react-intl";

import { AppLink } from "../link";
import type { DefenseFactoryResponse } from "../contract";
import { repositoryLabel } from "../ui";
import { WorkbenchBadge as Badge, WorkbenchButton } from "./controls";
import { findingFields } from "./findings-fields";
import { findingSourceLabels } from "./finding-source-types";
import {
  getRelativeTimeParts,
  OPEN_FINDING_STATUSES,
  parseDateString,
  shortHash,
} from "./findings-utils";
import { WorkbenchState } from "./layout";
import { CRITICALITY_MESSAGES, STATUS_MESSAGES } from "./messages";
import { workbenchStyles } from "./styles";
import Table from "./table";
import type { Finding } from "./types";

import "./findings-presentation.css";
import "./overview-attention.css";

const attentionColumns = ["severity", "finding", "status", "detected"] as const;

export function OverviewAttention({
  repositories,
  findingsQuery,
}: {
  repositories: string[];
  findingsQuery: {
    data?: DefenseFactoryResponse<"findings_list">;
    isPending: boolean;
    isFetching: boolean;
    error: unknown;
    refetch: () => unknown;
  };
}) {
  const headingId = useId();
  const search = new URLSearchParams({
    status: OPEN_FINDING_STATUSES.join(","),
    sort: "sev_desc,date_desc",
  });
  if (repositories.length > 0) search.set("repo", repositories.join(","));
  const findings = findingsQuery.data?.items ?? [];
  const isLoading = findingsQuery.isPending && findings.length === 0;

  return (
    <section className="df-overview-attention" aria-labelledby={headingId}>
      <h2 id={headingId}>
        <FormattedMessage
          id="defenseFactory.overview.attention.title"
          defaultMessage="Needs attention"
          description="Overview section showing the highest-severity open findings in the selected repository scope."
        />
      </h2>
      <div className="df-findings-table" aria-busy={findingsQuery.isFetching}>
        <Table.Root>
          <Table.Header>
            {attentionColumns.map((id) => (
              <Table.HeaderCell
                key={id}
                className={`df-findings-column-${id}`}
                ariaSort={id === "severity" ? "descending" : undefined}
              >
                <FormattedMessage
                  {...findingFields.find((field) => field.id === id)!.label}
                />
              </Table.HeaderCell>
            ))}
          </Table.Header>
          <Table.Body>
            {isLoading || findingsQuery.error || findings.length === 0 ? (
              <Table.Row>
                <Table.Cell
                  colSpan={attentionColumns.length}
                  divClassName="w-full"
                >
                  <WorkbenchState
                    variant="table"
                    loading={isLoading}
                    action={
                      findingsQuery.error ? (
                        <WorkbenchButton
                          color="secondary"
                          size="toolbar"
                          loading={findingsQuery.isFetching}
                          onClick={() => void findingsQuery.refetch()}
                        >
                          <FormattedMessage
                            id="codexSecurity.workbench.findings.table.retry"
                            defaultMessage="Retry"
                            description="Retry loading the authorized findings shown in this table."
                          />
                        </WorkbenchButton>
                      ) : undefined
                    }
                  >
                    {isLoading ? (
                      <FormattedMessage
                        id="codexSecurity.workbench.findings.table.loading"
                        defaultMessage="Loading findings…"
                        description="Progress message while the first page of authorized findings loads."
                      />
                    ) : findingsQuery.error ? (
                      <FormattedMessage
                        id="codexSecurity.workbench.findings.table.error"
                        defaultMessage="Findings could not be loaded."
                        description="Privacy-preserving error when authorized findings cannot be retrieved."
                      />
                    ) : (
                      <FormattedMessage
                        id="defenseFactory.overview.attention.empty"
                        defaultMessage="No open findings in this scope."
                        description="Empty overview finding preview without implying that a scan has run."
                      />
                    )}
                  </WorkbenchState>
                </Table.Cell>
              </Table.Row>
            ) : (
              findings.map((finding) => (
                <AttentionFindingRow
                  key={finding.id}
                  finding={finding}
                  search={`?${search}`}
                />
              ))
            )}
          </Table.Body>
        </Table.Root>
        <div className="df-overview-attention-footer">
          <AppLink
            to={`/findings?${search}`}
            className={workbenchStyles.tableLink}
          >
            <FormattedMessage
              id="defenseFactory.overview.attention.viewAll"
              defaultMessage="View all findings"
              description="Open the complete severity-sorted open findings list while preserving the overview repository scope."
            />
          </AppLink>
        </div>
      </div>
    </section>
  );
}

function AttentionFindingRow({
  finding,
  search,
}: {
  finding: Finding;
  search: string;
}) {
  const intl = useIntl();
  const findingLinkProps = {
    to: {
      pathname: `/findings/${encodeURIComponent(finding.id)}`,
      search,
    },
  };
  const detectedDate = parseDateString(finding.created_at);
  const relativeTime = getRelativeTimeParts(detectedDate);
  const severity = (
    <Table.RowTextLink {...findingLinkProps}>
      {finding.criticality ? (
        <Badge
          variant={
            finding.criticality === "critical"
              ? "danger"
              : finding.criticality === "high"
              ? "warning"
              : finding.criticality === "medium"
              ? "reserve"
              : "default"
          }
          className={`df-findings-badge df-findings-severity-${finding.criticality}`}
        >
          {intl.formatMessage(CRITICALITY_MESSAGES[finding.criticality])}
        </Badge>
      ) : (
        <span className="text-token-text-tertiary">
          <FormattedMessage
            id="aardvark.placeholder.missing"
            defaultMessage="—"
            description="Dash placeholder indicating missing value"
          />
        </span>
      )}
    </Table.RowTextLink>
  );
  const status = (
    <Table.RowTextLink {...findingLinkProps}>
      <Badge
        variant={finding.status === "triaged" ? "warning" : "default"}
        className={`df-findings-badge df-findings-status-${finding.status}`}
      >
        {intl.formatMessage(STATUS_MESSAGES[finding.status])}
      </Badge>
    </Table.RowTextLink>
  );
  const detected = (
    <Table.RowTextLink {...findingLinkProps}>
      <span
        className="df-overview-attention-detected"
        title={
          detectedDate
            ? intl.formatDate(detectedDate, {
                year: "numeric",
                month: "long",
                day: "numeric",
                hour: "numeric",
                minute: "2-digit",
              })
            : undefined
        }
      >
        {relativeTime ? (
          <FormattedRelativeTime
            value={relativeTime.value}
            unit={relativeTime.unit}
            numeric="auto"
          />
        ) : (
          "—"
        )}
      </span>
    </Table.RowTextLink>
  );
  const title = (
    <div className="df-findings-title-cell">
      <Table.RowLink
        {...findingLinkProps}
        className={`${workbenchStyles.tableLink} df-findings-title`}
        aria-label={intl.formatMessage(
          {
            id: "codexSecurity.workbench.findings.table.row.open",
            defaultMessage: "Open finding: {title}",
            description: "Accessible label for an interactive finding table row.",
          },
          { title: finding.title },
        )}
      >
        <span>{finding.title}</span>
      </Table.RowLink>
      <div className="df-findings-row-source">
        <Table.RowTextLink
          {...findingLinkProps}
          className="truncate"
          title={finding.repo_url}
        >
          {repositoryLabel(finding.repo_url)}
        </Table.RowTextLink>
        <span aria-hidden>·</span>
        <Table.RowTextLink {...findingLinkProps}>
          {intl.formatMessage(findingSourceLabels[finding.source.kind])}
        </Table.RowTextLink>
        {finding.observed_revision ? (
          <>
            <span aria-hidden>·</span>
            <Table.RowTextLink
              {...findingLinkProps}
              title={finding.observed_revision}
            >
              {shortHash(finding.observed_revision)}
            </Table.RowTextLink>
          </>
        ) : null}
      </div>
      <div className="df-findings-mobile-metadata">
        {severity}
        {status}
        {detected}
      </div>
    </div>
  );
  const cells = { severity, finding: title, status, detected };

  return (
    <Table.Row className="df-findings-row">
      {attentionColumns.map((id) => (
        <Table.Cell
          key={id}
          className={`df-findings-column-${id}`}
          divClassName="df-findings-cell"
        >
          {cells[id]}
        </Table.Cell>
      ))}
    </Table.Row>
  );
}
