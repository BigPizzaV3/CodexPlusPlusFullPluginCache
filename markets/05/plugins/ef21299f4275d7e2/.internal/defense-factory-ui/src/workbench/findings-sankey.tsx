import { useId } from "react";
import { FormattedMessage, FormattedNumber, useIntl } from "react-intl";

import { STATUS_MESSAGES } from "./messages";
import { overviewSeverityMessages } from "./overview-breakdown-data";
import { getFindingsSankeyLayout } from "./findings-sankey-layout";
import type { Finding } from "./types";
import "./findings-sankey.css";

export function FindingsSankey({
  findings,
  total,
}: {
  findings: Finding[];
  total: number;
}) {
  const intl = useIntl();
  const headingId = useId();
  const { groups, statuses, height, root, severityNodes, statusNodes, bands } =
    getFindingsSankeyLayout(findings, {
      root: intl.formatMessage({
        id: "codexSecurity.findings.sankey.root",
        defaultMessage: "Findings",
        description:
          "Root count of the visible-page severity and status diagram.",
      }),
      severities: Object.entries(overviewSeverityMessages).map(
        ([key, message]) => ({ key, label: intl.formatMessage(message) }),
      ),
      status: (status) => intl.formatMessage(STATUS_MESSAGES[status]),
    });

  return (
    <section className="df-findings-sankey" aria-labelledby={headingId}>
      <div className="df-findings-sankey-header">
        <h2 id={headingId}>
          <FormattedMessage
            id="codexSecurity.findings.sankey.title"
            defaultMessage="Severity and status"
            description="Title of a current-page finding distribution diagram."
          />
        </h2>
        <p>
          <FormattedMessage
            id="codexSecurity.findings.sankey.scope"
            defaultMessage="Current page · {shown, number} of {total, number} matching findings"
            description="Explicitly limits the chart to the findings loaded on the current page, not all matching findings."
            values={{ shown: findings.length, total }}
          />
        </p>
      </div>
      <div
        className="df-findings-sankey-scroll"
        tabIndex={0}
        role="region"
        aria-labelledby={headingId}
      >
        <div className="df-findings-sankey-plot" style={{ height }} aria-hidden>
          {bands.map(({ key, clipPath, fromColor, toColor }) => (
            <div
              key={key}
              className="df-findings-sankey-band"
              style={{
                clipPath,
                background: `linear-gradient(to right, ${fromColor}, ${toColor})`,
              }}
            />
          ))}
          {[root, ...severityNodes, ...statusNodes].map((node) => (
            <div
              key={node.key}
              className="df-findings-sankey-node"
              style={{ left: `${node.x}%`, top: node.y + node.height / 2 }}
            >
              <span
                className="df-findings-sankey-bar"
                style={{
                  height: Math.max(28, node.height),
                  background: node.color,
                }}
              />
              <span className="df-findings-sankey-label">
                <span>{node.label}</span>
                <strong>
                  <FormattedNumber value={node.count} />
                </strong>
              </span>
            </div>
          ))}
        </div>
      </div>
      {/* Keep exact chart values accessible without a duplicate visual table. */}
      <div className="sr-only">
        <table>
          <caption className="sr-only">
            <FormattedMessage
              id="codexSecurity.findings.sankey.table"
              defaultMessage="Current-page findings by severity and current status"
              description="Caption of the diagram's exact-count data table."
            />
          </caption>
          <thead>
            <tr>
              <th scope="col">
                <FormattedMessage
                  id="codexSecurity.findings.sankey.severity"
                  defaultMessage="Severity"
                  description="Severity column in the diagram data table."
                />
              </th>
              {statusNodes.map((node) => (
                <th key={node.key} scope="col">
                  {node.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {groups.map(({ key, items }, index) => (
              <tr key={key}>
                <th scope="row">{severityNodes[index].label}</th>
                {statuses.map(({ key: status }) => (
                  <td key={status}>
                    <FormattedNumber
                      value={
                        items.filter((finding) => finding.status === status)
                          .length
                      }
                    />
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
