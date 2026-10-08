import { useQuery } from "@tanstack/react-query";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation, useNavigate } from "react-router";

import { useCloud } from "./app-context";
import { securityClient } from "./client";
import {
  getOverviewApiRange,
  getOverviewDateRange,
  isOverviewDateRangeTooLong,
  type OverviewDateRange,
} from "./overview-dates";
import {
  OverviewRequestError,
  overviewAsOf,
} from "./workbench/overview-components";
import {
  getOverviewRepositories,
  getOverviewSearch,
  getPipelineDateRange,
  getPipelineSearch,
} from "./workbench/overview-filters";
import { OverviewDateControls } from "./workbench/overview-date-controls";
import { OverviewCurrentStatus } from "./workbench/overview-findings";
import { OverviewFindingsActivity } from "./workbench/overview-findings-activity";
import { OverviewSeverityChart } from "./workbench/overview-severity-chart";
import { OverviewFindingPipeline } from "./workbench/overview-finding-pipeline";
import { OverviewAttention } from "./workbench/overview-attention";
import { OPEN_FINDING_STATUSES } from "./workbench/findings-utils";
import { useFindingStatusCounts } from "./workbench/finding-status-counts";
import { workbenchStyles } from "./workbench/styles";
import { WorkbenchNavigation } from "./workbench/navigation";
import { WorkbenchRefreshControls } from "./workbench/refresh-controls";
import "./workbench/overview-layout.css";

export function Overview() {
  const cloud = useCloud();
  const intl = useIntl();
  const location = useLocation();
  const navigate = useNavigate();
  const dateRange = getOverviewDateRange(location.search);
  const { startDate, endDate } = dateRange;
  const dateRangeTooLong = isOverviewDateRangeTooLong(dateRange);
  const repositories = getOverviewRepositories(location.search);
  const repo = repositories.join(",");
  const findingStatusCountsQuery = useFindingStatusCounts(repo);
  const pipelineDateRange = getPipelineDateRange(location.search);
  const pipelineCountsQuery = useFindingStatusCounts(repo, pipelineDateRange);
  const currentScope = {
    accountId: cloud.accountId,
    userId: cloud.identity?.userId,
    repo,
  };
  const periodScope = { ...currentScope, startDate, endDate };

  const repositoriesQuery = useQuery({
    queryKey: ["overview", "repositories", currentScope],
    queryFn: () =>
      securityClient.request({
        operation: "dashboard_repositories",
        parameters: { query: { repo: repo || undefined } },
      }),
    staleTime: 60_000,
  });
  const currentFindingsQuery = useQuery({
    queryKey: ["overview", "findings", currentScope],
    queryFn: () =>
      securityClient.request({
        operation: "dashboard_findings",
        parameters: { query: { repo: repo || undefined } },
      }),
    staleTime: 60_000,
  });
  const attentionQuery = useQuery({
    queryKey: ["findings", "overview-attention", currentScope],
    queryFn: () =>
      securityClient.request({
        operation: "findings_list",
        parameters: {
          query: {
            repo: repo || undefined,
            status: OPEN_FINDING_STATUSES.join(","),
            sort: "sev_desc,date_desc",
            limit: 8,
          },
        },
      }),
    staleTime: 60_000,
  });
  const activityQuery = useQuery({
    queryKey: ["overview", "activity", periodScope],
    enabled: !dateRangeTooLong,
    queryFn: () =>
      securityClient.request({
        operation: "dashboard_activity",
        parameters: {
          query: { ...getOverviewApiRange(dateRange), repo: repo || undefined },
        },
      }),
    staleTime: 60_000,
  });
  const dashboardQueries = [
    repositoriesQuery,
    currentFindingsQuery,
    activityQuery,
  ];
  const refreshableQueries = [
    ...dashboardQueries,
    findingStatusCountsQuery,
    ...(pipelineDateRange ? [pipelineCountsQuery] : []),
    attentionQuery,
  ];
  const isRefreshing = refreshableQueries.some((query) => query.isFetching);
  const hasData = dashboardQueries.some((query) => query.data != null);
  const asOf =
    dateRangeTooLong ||
    findingStatusCountsQuery.error ||
    pipelineCountsQuery.error ||
    attentionQuery.error
      ? undefined
      : overviewAsOf(dashboardQueries, isRefreshing);

  function changeFilters(
    nextDateRange: OverviewDateRange,
    selectedRepositories: string[],
  ) {
    navigate({
      pathname: location.pathname,
      search: getOverviewSearch(
        nextDateRange,
        selectedRepositories,
        location.search,
      ),
    });
  }

  function refreshDashboard() {
    for (const query of refreshableQueries) {
      void query.refetch({ cancelRefetch: false });
    }
  }

  return (
    <div className={`${workbenchStyles.collectionPage} df-overview-page`}>
      <h1 className="sr-only">
        <FormattedMessage
          id="codexSecurity.overview.title"
          defaultMessage="Security overview"
          description="Page heading for the existing Codex Security Cloud overview dashboard."
        />
      </h1>
      <WorkbenchNavigation
        actions={
          <WorkbenchRefreshControls
            asOf={asOf}
            showRefresh={hasData && !dateRangeTooLong}
            isRefreshing={isRefreshing}
            onRefresh={refreshDashboard}
          />
        }
      />

      <div className="df-overview-current">
        <OverviewCurrentStatus
          findings={currentFindingsQuery.data?.findings}
          repositories={repositoriesQuery.data?.repositories}
          selectedRepositories={repositories}
          fixedFindings={findingStatusCountsQuery.data?.fixed}
          fixedFindingsError={Boolean(findingStatusCountsQuery.error)}
          findingsError={
            currentFindingsQuery.error ? (
              <OverviewRequestError
                isRetrying={currentFindingsQuery.isFetching}
                asOf={currentFindingsQuery.data?.as_of}
                onRetry={() => {
                  void currentFindingsQuery.refetch({ cancelRefetch: false });
                }}
              >
                <FormattedMessage
                  id="codexSecurity.overview.currentFindings.error"
                  defaultMessage="Unable to load current open findings."
                  description="Section error when current finding counts fail to load. Other overview sections remain available."
                />
              </OverviewRequestError>
            ) : undefined
          }
          repositoriesError={
            repositoriesQuery.error ? (
              <OverviewRequestError
                isRetrying={repositoriesQuery.isFetching}
                asOf={repositoriesQuery.data?.as_of}
                onRetry={() => {
                  void repositoriesQuery.refetch({ cancelRefetch: false });
                }}
              >
                <FormattedMessage
                  id="codexSecurity.overview.repositories.error"
                  defaultMessage="Unable to load repository counts."
                  description="Section error when configured-repository counts fail to load. Other overview sections remain available."
                />
              </OverviewRequestError>
            ) : undefined
          }
        />

        {pipelineDateRange && findingStatusCountsQuery.error ? (
          <OverviewRequestError
            isRetrying={findingStatusCountsQuery.isFetching}
            onRetry={() => {
              void findingStatusCountsQuery.refetch({ cancelRefetch: false });
            }}
          >
            <FormattedMessage
              id="codexSecurity.overview.currentFixed.error"
              defaultMessage="Unable to refresh the all-time fixed findings count."
              description="Error for the independent summary total when a Pipeline discovery period is selected."
            />
          </OverviewRequestError>
        ) : null}
        <OverviewFindingPipeline
          counts={pipelineCountsQuery.data}
          repositories={repositories}
          dateRange={pipelineDateRange}
          onDateRangeChange={(range) =>
            navigate({
              pathname: location.pathname,
              search: getPipelineSearch(location.search, range),
            })
          }
          error={
            pipelineCountsQuery.error ? (
              <OverviewRequestError
                isRetrying={pipelineCountsQuery.isFetching}
                onRetry={() => {
                  void pipelineCountsQuery.refetch({ cancelRefetch: false });
                }}
              >
                <FormattedMessage
                  id="codexSecurity.overview.findingPipeline.error"
                  defaultMessage="Unable to load finding status counts."
                  description="Section error when the current finding pipeline cannot load."
                />
              </OverviewRequestError>
            ) : undefined
          }
        />
      </div>

      <OverviewAttention
        repositories={repositories}
        findingsQuery={attentionQuery}
      />

      <section
        aria-labelledby="codex-security-overview-activity-heading"
        className="df-overview-activity"
      >
        <h2 id="codex-security-overview-activity-heading" className="sr-only">
          <FormattedMessage
            id="codexSecurity.overview.activity.title"
            defaultMessage="Activity"
            description="Section heading grouping current severity and selected-period discovery charts."
          />
        </h2>
        {!dateRangeTooLong && activityQuery.error ? (
          <OverviewRequestError
            isRetrying={activityQuery.isFetching}
            asOf={activityQuery.data?.as_of}
            onRetry={() => {
              void activityQuery.refetch({ cancelRefetch: false });
            }}
          >
            <FormattedMessage
              id="codexSecurity.overview.activity.error"
              defaultMessage="Unable to load new findings."
              description="Section error when selected-period finding activity fails to load."
            />
          </OverviewRequestError>
        ) : null}
        <div className="df-overview-chart-grid">
          {currentFindingsQuery.data || currentFindingsQuery.isPending ? (
            <OverviewSeverityChart
              findings={currentFindingsQuery.data?.findings}
              repositories={repositories}
            />
          ) : null}
          {!dateRangeTooLong &&
          (activityQuery.data?.findings.daily !== undefined ||
            activityQuery.isPending) ? (
            <OverviewFindingsActivity
              daily={activityQuery.data?.findings.daily}
              dateControls={
                <OverviewDateControls
                  dateRange={dateRange}
                  onChange={(range) => changeFilters(range, repositories)}
                />
              }
            />
          ) : null}
        </div>
        {dateRangeTooLong ||
        (!activityQuery.isPending &&
          activityQuery.data?.findings.daily === undefined) ? (
          <OverviewDateControls
            dateRange={dateRange}
            onChange={(range) => changeFilters(range, repositories)}
          />
        ) : null}
      </section>
    </div>
  );
}
