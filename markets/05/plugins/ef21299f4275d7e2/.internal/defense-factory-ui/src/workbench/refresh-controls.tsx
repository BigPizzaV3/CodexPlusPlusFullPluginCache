import { FormattedMessage, useIntl } from "react-intl";

import { WorkbenchButton } from "./controls";
import { WorkbenchIcon } from "./icons";

export function WorkbenchRefreshControls({
  asOf,
  showRefresh,
  isRefreshing,
  onRefresh,
}: {
  asOf?: number;
  showRefresh: boolean;
  isRefreshing: boolean;
  onRefresh: () => void;
}) {
  const intl = useIntl();
  return (
    <>
      {asOf !== undefined ? (
        <span className="df-dashboard-freshness">
          <FormattedMessage
            id="defenseFactory.workbench.asOf"
            defaultMessage="As of {date}"
            description="Timestamp for the currently displayed Security data."
            values={{
              date: intl.formatDate(asOf, {
                month: "short",
                day: "numeric",
                year: "numeric",
                hour: "numeric",
                minute: "2-digit",
                timeZoneName: "short",
              }),
            }}
          />
        </span>
      ) : null}
      {showRefresh ? (
        <WorkbenchButton
          color="ghostSecondary"
          size="iconCircleSm"
          loading={isRefreshing}
          aria-busy={isRefreshing}
          aria-label={intl.formatMessage({
            id: "defenseFactory.workbench.refresh",
            defaultMessage: "Refresh",
            description:
              "Refresh the current Security data without changing filters or pagination.",
          })}
          onClick={onRefresh}
        >
          <WorkbenchIcon name="refresh" />
        </WorkbenchButton>
      ) : null}
    </>
  );
}
