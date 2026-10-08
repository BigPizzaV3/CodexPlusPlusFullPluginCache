import { Modal } from "@oai/ds/ui/modal";
import { SegmentedControl } from "@oai/ds/ui/segmented-control";
import { useId, useState, type ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { WorkbenchButton as Button } from "./controls";
import { WorkbenchPageHeader, WorkbenchState } from "./layout";
import { WorkbenchScanTypeBadge } from "./scan-type-badge";
import {
  WorkbenchScanCommitBadge,
  WorkbenchScanDurationBadge,
  WorkbenchScanInitiatorBadge,
  WorkbenchScanRepositoryBadge,
  WorkbenchScanStartedBadge,
  WorkbenchScanStatusBadge,
} from "./scans-metadata";
import { getScanStatus, type WorkbenchScan } from "./scans-model";
import { WorkbenchSource } from "./source";
import { workbenchStyles } from "./styles";

export function ScanDetailPresentation({
  scan,
  outputs,
  findings,
  failureMessage,
  isCanceling,
  onRequestCancel,
  cancelConfirmation,
}: {
  scan: WorkbenchScan;
  outputs?: ReactNode;
  findings: ReactNode;
  failureMessage?: string | null;
  isCanceling: boolean;
  onRequestCancel: () => void;
  cancelConfirmation?: ReactNode;
}) {
  const intl = useIntl();
  const panelId = useId();
  const [activePanel, setActivePanel] = useState<"outputs" | "findings">(
    "outputs",
  );
  const [hasOpenedFindings, setHasOpenedFindings] = useState(false);
  const outputsLabel = intl.formatMessage({
    id: "codexSecurity.workbench.scans.detail.panels.outputs",
    defaultMessage: "Outputs",
    description:
      "Selector option for generated files and artifact previews on a scan detail page.",
  });
  const findingsLabel = intl.formatMessage({
    id: "codexSecurity.workbench.scans.detail.panels.findings",
    defaultMessage: "Findings",
    description:
      "Selector option for findings associated with a scan on a scan detail page.",
  });
  const scanStatus = getScanStatus(scan);
  const canCancel =
    scan.workflow != null &&
    scan.workflow.is_owner !== false &&
    ["queued", "preparing", "running", "validating_output"].includes(
      scan.workflow.status,
    );

  return (
    <div className={workbenchStyles.scanDetailPage}>
      <WorkbenchPageHeader
        kind="detail"
        titlePrefix={
          <>
            <WorkbenchScanStatusBadge scan={scan} />
            <WorkbenchScanTypeBadge scanType={scan.scanType} />
          </>
        }
        title={
          <WorkbenchSource
            environmentLabel={scan.environmentLabel}
            repositoryId={scan.repositoryId}
            repositoryUrl={scan.repositoryUrl}
            variant="table"
            isLoading={scan.isEnvironmentLoading}
          />
        }
        titleAdornment={
          <>
            <WorkbenchScanStartedBadge scan={scan} />
            <WorkbenchScanDurationBadge scan={scan} />
            <WorkbenchScanRepositoryBadge scan={scan} />
            <WorkbenchScanCommitBadge scan={scan} />
            <WorkbenchScanInitiatorBadge scan={scan} />
          </>
        }
        actions={
          canCancel ? (
            <Button
              color="outlineSurface"
              disabled={isCanceling}
              onClick={onRequestCancel}
            >
              <FormattedMessage
                id="codexSecurity.workbench.scans.detail.cancel"
                defaultMessage="Cancel scan"
                description="Requests cancellation of a running repository security scan."
              />
            </Button>
          ) : null
        }
      />

      {scanStatus === "failed" && failureMessage ? (
        <WorkbenchState variant="inline">{failureMessage}</WorkbenchState>
      ) : null}

      <div className="-m-1 flex w-fit max-w-full shrink-0 p-1">
        <SegmentedControl<"outputs" | "findings">
          className="df-segmented-control"
          value={activePanel}
          onChange={(panel) => {
            setActivePanel(panel);
            if (panel === "findings") setHasOpenedFindings(true);
          }}
          aria-label={intl.formatMessage({
            id: "codexSecurity.workbench.scans.detail.panels.selector",
            defaultMessage: "Scan panels",
            description:
              "Accessible name for the Outputs and Findings selector on a scan detail page.",
          })}
          size="lg"
          pill
        >
          <SegmentedControl.Option
            value="outputs"
            aria-controls={`${panelId}-outputs`}
          >
            {outputsLabel}
          </SegmentedControl.Option>
          <SegmentedControl.Option
            value="findings"
            aria-controls={`${panelId}-findings`}
          >
            {findingsLabel}
          </SegmentedControl.Option>
        </SegmentedControl>
      </div>

      <section
        id={`${panelId}-outputs`}
        aria-label={outputsLabel}
        className="min-h-0 flex-1 overflow-auto overscroll-contain"
        hidden={activePanel !== "outputs"}
      >
        {outputs ??
          (scanStatus === "created" ||
          scanStatus === "in_progress" ||
          scanStatus === "queued" ||
          scanStatus === "preparing" ||
          scanStatus === "running" ||
          scanStatus === "validating_output" ||
          scanStatus === "cancel_requested" ? (
            <WorkbenchState variant="inline">
              <FormattedMessage
                id="codexSecurity.workbench.scans.detail.running"
                defaultMessage="Results will appear here when this scan finishes."
                description="Status message for a queued or running repository security scan."
              />
            </WorkbenchState>
          ) : (
            <WorkbenchState>
              <FormattedMessage
                id="codexSecurity.workbench.scans.detail.outputs.empty"
                defaultMessage="No outputs available."
                description="Empty state when a finished scan has no generated files available."
              />
            </WorkbenchState>
          ))}
      </section>
      <section
        id={`${panelId}-findings`}
        aria-label={findingsLabel}
        className="min-h-0 flex-1 overflow-auto overscroll-contain"
        hidden={activePanel !== "findings"}
      >
        {hasOpenedFindings ? findings : null}
      </section>

      {cancelConfirmation}
    </div>
  );
}

export function ScanFindingsUnavailable() {
  return (
    <WorkbenchState>
      <FormattedMessage
        id="codexSecurity.workbench.scans.detail.findings.unavailable"
        defaultMessage="Findings cannot currently be scoped to this individual run. Open repository findings to review results without mixing in unrelated scan data here."
        description="Privacy-safe explanation when the API cannot associate findings with one workflow run."
      />
    </WorkbenchState>
  );
}

export function ScanCancelConfirmation({
  open,
  canceling,
  failed,
  onOpenChange,
  onConfirm,
}: {
  open: boolean;
  canceling: boolean;
  failed: boolean;
  onOpenChange: (open: boolean) => void;
  onConfirm: () => void;
}) {
  return (
    <Modal
      open={open}
      onOpenChange={(nextOpen) => {
        if (!canceling) onOpenChange(nextOpen);
      }}
    >
      <Modal.Content maxWidth={440}>
        <Modal.Body>
          <Modal.Title>
            <FormattedMessage
              id="codexSecurity.workbench.scans.detail.cancel.confirmation"
              defaultMessage="Cancel this scan?"
              description="Confirmation title before canceling a running repository security scan."
            />
          </Modal.Title>
          <Modal.Description>
            <FormattedMessage
              id="codexSecurity.workbench.scans.detail.cancel.description"
              defaultMessage="The scan will stop as soon as the current work can be canceled."
              description="Explanation in the scan cancellation confirmation."
            />
          </Modal.Description>
          {failed ? (
            <div className="mt-4">
              <WorkbenchState variant="inline">
                <FormattedMessage
                  id="codexSecurity.workbench.scans.detail.cancel.error"
                  defaultMessage="The cancellation request could not be completed. Try again."
                  description="Sanitized error after a scan cancellation request fails."
                />
              </WorkbenchState>
            </div>
          ) : null}
        </Modal.Body>
        <Modal.Footer>
          <Button
            color="ghostSecondary"
            disabled={canceling}
            onClick={() => onOpenChange(false)}
          >
            <FormattedMessage
              id="codexSecurity.workbench.scans.detail.cancel.dismiss"
              defaultMessage="Keep running"
              description="Dismisses scan cancellation and leaves the scan running."
            />
          </Button>
          <Button
            color="dangerSolid"
            loading={canceling}
            disabled={canceling}
            onClick={onConfirm}
          >
            <FormattedMessage
              id="codexSecurity.workbench.scans.detail.cancel.confirm"
              defaultMessage="Cancel scan"
              description="Confirms cancellation of a running repository security scan."
            />
          </Button>
        </Modal.Footer>
      </Modal.Content>
    </Modal>
  );
}
