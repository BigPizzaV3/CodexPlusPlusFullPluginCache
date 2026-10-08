import { useId, type ReactNode } from "react";
import { FormattedMessage } from "react-intl";

import type { DefenseFactoryResponse } from "../contract";
import { OverviewMetric } from "./overview-components";
import { OverviewOpenFindings } from "./overview-open-findings";

type CurrentFindings = DefenseFactoryResponse<"dashboard_findings">["findings"];
type RepositoryCounts =
  DefenseFactoryResponse<"dashboard_repositories">["repositories"];

export function OverviewCurrentStatus({
  findings,
  repositories,
  selectedRepositories,
  fixedFindings,
  fixedFindingsError,
  findingsError,
  repositoriesError,
}: {
  findings: CurrentFindings | undefined;
  repositories: RepositoryCounts | undefined;
  selectedRepositories: string[];
  fixedFindings: number | undefined;
  fixedFindingsError: boolean;
  findingsError?: ReactNode;
  repositoriesError?: ReactNode;
}) {
  const headingId = useId();
  const showFindings = findings != null || findingsError == null;
  const showRepositories = repositories != null || repositoriesError == null;
  const showFixed = fixedFindings != null || !fixedFindingsError;
  const isRepositoryFiltered = selectedRepositories.length > 0;

  return (
    <section aria-labelledby={headingId} className="flex flex-col gap-4">
      <h2 id={headingId} className="sr-only">
        <FormattedMessage
          id="codexSecurity.overview.currentStatus.title"
          defaultMessage="Current status"
          description="Screen-reader heading grouping current repository scanning counts and open findings."
        />
      </h2>
      {repositoriesError}
      {findingsError}
      {showFindings || showRepositories || showFixed ? (
        <div className="df-overview-metrics df-overview-summary">
          {showRepositories ? (
            <OverviewMetric
              label={
                isRepositoryFiltered ? (
                  <FormattedMessage
                    id="codexSecurity.overview.repositories.selected.label"
                    defaultMessage="Selected repositories"
                    description="Number of repositories selected in the overview scope control."
                  />
                ) : (
                  <FormattedMessage
                    id="codexSecurity.overview.repositories.configured.label"
                    defaultMessage="Configured repositories"
                    description="Current distinct configured repositories in the permitted Security scope."
                  />
                )
              }
              value={
                isRepositoryFiltered
                  ? selectedRepositories.length
                  : repositories?.configured_repositories
              }
            />
          ) : null}
          {showFindings ? <OverviewOpenFindings findings={findings} /> : null}
          {showFixed ? (
            <OverviewMetric
              label={
                <FormattedMessage
                  id="codexSecurity.overview.currentFixed.label"
                  defaultMessage="Findings fixed"
                  description="All findings currently marked fixed in the selected repository scope, independent of discovery dates."
                />
              }
              value={fixedFindings}
            />
          ) : null}
          {showRepositories ? (
            <OverviewMetric
              label={
                <FormattedMessage
                  id="codexSecurity.overview.repositories.enabled.label"
                  defaultMessage="Continuous scanning enabled"
                  description="Current repositories with continuous security scanning enabled."
                />
              }
              value={repositories?.continuous_scanning_enabled}
            />
          ) : null}
        </div>
      ) : null}
    </section>
  );
}
