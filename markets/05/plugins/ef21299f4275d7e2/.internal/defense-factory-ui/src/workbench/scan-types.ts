import { defineMessages } from "react-intl";

export const scanTypeLabels = defineMessages({
  commit_scan: {
    id: "codexSecurity.workbench.scans.launch.scope.option.diff",
    defaultMessage: "Commit changes",
    description:
      "Short scan-type label in Codex Security creation, findings and scans tables, filters, and scan details. Selects analysis focused on security issues introduced by changes in commits, rather than a review of the entire repository. Does not describe when scans run.",
  },
  repository_scan: {
    id: "codexSecurity.workbench.scans.launch.scope.option.full_commit",
    defaultMessage: "Repository",
    description:
      "Short scan-type label in Codex Security creation, findings and scans tables, filters, and scan details. Means analysis across the repository at a specific revision, not just changes introduced by a commit. Does not describe when scans run.",
  },
});

export type ScanType = keyof typeof scanTypeLabels;
export const SCAN_TYPES = ["commit_scan", "repository_scan"] as const;

export const scanTypeDescriptions = defineMessages({
  commit_scan: {
    id: "codexSecurity.workbench.scans.launch.scope.diff.description",
    defaultMessage: "Find security issues introduced by changes in commits.",
    description:
      "Brief explanation of Commit changes in the What to scan info popover on the Codex Security New Scan page. Helps users understand that analysis focuses on issues introduced by code changes, without claiming that surrounding unchanged code is never read.",
  },
  repository_scan: {
    id: "codexSecurity.workbench.scans.launch.scope.full_commit.description",
    defaultMessage:
      "Find security issues across the repository at a specific revision.",
    description:
      "Brief explanation of Repository in the What to scan info popover on the Codex Security New Scan page. Contrasts analysis of a repository snapshot with analysis focused on commit changes. Does not imply a recurring schedule or guaranteed exhaustive coverage.",
  },
});

export const scanTypeMessages = defineMessages({
  label: {
    id: "codexSecurity.workbench.scanType.label",
    defaultMessage: "Scan type",
    description:
      "Short column heading, filter label, and accessible badge label in Codex Security findings and scans views. Identifies whether the scan analyzed commit changes or the entire repository. Distinct from Source, which identifies the environment and revision.",
  },
  all: {
    id: "codexSecurity.workbench.scanType.all",
    defaultMessage: "All scan types",
    description:
      "Option in Codex Security findings and scans filters that includes both Commit changes and Repository scans. Removes only the scan-type restriction and preserves other filters.",
  },
});
