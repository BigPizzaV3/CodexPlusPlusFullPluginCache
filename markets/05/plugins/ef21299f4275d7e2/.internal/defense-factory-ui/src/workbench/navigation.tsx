import { WorkbenchLink } from "./controls";
import type { ReactNode } from "react";
import { FormattedMessage, useIntl } from "react-intl";
import { useLocation, useMatch, useNavigate } from "react-router";

import { AppLink } from "../link";
import { useCloud } from "../app-context";
import { repositoryLabel } from "../ui";
import { shortHash } from "./findings-utils";
import { getOverviewRepositories } from "./overview-filters";
import { RepositoryScopeControl } from "./repository-scope-control";
import { WorkbenchIcon } from "./icons";

type Collection = "overview" | "findings" | "repositories" | "scans";

type Breadcrumb = {
  label: string;
  to?: { pathname: string; search?: string; hash?: string };
  title?: string;
};

function collectionSearch(search: string) {
  const current = new URLSearchParams(search);
  const next = new URLSearchParams();
  const preview = current.get("workflow_runs_preview");
  if (preview) next.set("workflow_runs_preview", preview);
  const value = next.toString();
  return value ? `?${value}` : "";
}

function repositoryName(repositoryId: string, search: string) {
  const repositoryUrl = new URLSearchParams(search).get("repo");
  return repositoryUrl ? repositoryLabel(repositoryUrl) : repositoryId;
}

export function WorkbenchNavigation({ actions }: { actions?: ReactNode }) {
  const intl = useIntl();
  const cloud = useCloud();
  const location = useLocation();
  const navigate = useNavigate();
  const repositoryMatch = useMatch({
    path: "/repositories/:repositoryId",
    end: false,
  });
  const segments = location.pathname.split("/").filter(Boolean);
  const collection: Collection = location.pathname.startsWith("/overview")
    ? "overview"
    : location.pathname.startsWith("/repositories")
    ? "repositories"
    : location.pathname.startsWith("/scans") ||
      location.pathname.startsWith("/runs")
    ? "scans"
    : "findings";
  const findingId = segments[0] === "findings" ? segments[1] : undefined;
  const showRepositoryScope =
    segments.length === 1 &&
    (segments[0] === "overview" || segments[0] === "findings");
  const repositoryId = repositoryMatch?.params.repositoryId;
  const repositorySection = repositoryId ? segments[2] : undefined;
  const repositoryItemId = repositoryId ? segments[3] : undefined;
  const isRepositoryCollection =
    segments[0] === "repositories" && !repositoryId;
  const isNewScan = location.pathname === "/scans/new";
  const runId = segments[0] === "runs" ? segments[1] : undefined;
  const isDetail = Boolean(
    findingId || repositoryId || isRepositoryCollection || isNewScan || runId,
  );
  const sharedCollectionSearch = collectionSearch(location.search);
  const breadcrumbs: Breadcrumb[] = [];

  if (isRepositoryCollection) {
    breadcrumbs.push({
      label: intl.formatMessage({
        id: "codex.security.workbench.navigation.repositories.label",
        defaultMessage: "Manage repositories",
        description:
          "Current-page breadcrumb label for repository monitoring management and recovery.",
      }),
    });
  } else if (findingId) {
    breadcrumbs.push(
      {
        label: intl.formatMessage({
          id: "codex.security.workbench.navigation.findings.label",
          defaultMessage: "Findings",
          description:
            "Navigation label for the searchable Security findings collection.",
        }),
        to: {
          pathname: "/findings",
          search: location.search,
          hash: location.hash,
        },
      },
      {
        label: intl.formatMessage({
          id: "codex.security.workbench.navigation.finding_detail.label",
          defaultMessage: "Finding",
          description:
            "Current-page breadcrumb label for a Security finding detail.",
        }),
      },
    );
  } else if (repositoryId) {
    const repositoryPath = `/repositories/${encodeURIComponent(repositoryId)}`;
    breadcrumbs.push({
      label: intl.formatMessage({
        id: "codex.security.workbench.navigation.repositories.label",
        defaultMessage: "Manage repositories",
        description:
          "Navigation label for repository monitoring management and recovery.",
      }),
      to: { pathname: "/repositories", search: sharedCollectionSearch },
    });
    breadcrumbs.push({
      label: repositoryName(repositoryId, location.search),
      title: repositoryId,
      to:
        repositorySection || repositoryItemId
          ? { pathname: repositoryPath, search: location.search }
          : undefined,
    });
    if (repositorySection) {
      breadcrumbs.push({
        label:
          repositorySection === "scans"
            ? intl.formatMessage({
                id: "codex.security.workbench.navigation.scans.label",
                defaultMessage: "Scans",
                description: "Navigation label for Security scan history.",
              })
            : intl.formatMessage({
                id: "codex.security.workbench.navigation.findings.label",
                defaultMessage: "Findings",
                description:
                  "Navigation label for the searchable Security findings collection.",
              }),
        to: repositoryItemId
          ? {
              pathname: `${repositoryPath}/${repositorySection}`,
              search: location.search,
            }
          : undefined,
      });
    }
    if (repositoryItemId) {
      breadcrumbs.push({
        label:
          repositorySection === "scans"
            ? shortHash(repositoryItemId)
            : intl.formatMessage({
                id: "codex.security.workbench.navigation.finding_detail.label",
                defaultMessage: "Finding",
                description:
                  "Current-page breadcrumb label for a Security finding detail.",
              }),
        title: repositoryItemId,
      });
    }
  } else if (isNewScan || runId) {
    breadcrumbs.push({
      label: intl.formatMessage({
        id: "codex.security.workbench.navigation.scans.label",
        defaultMessage: "Scans",
        description: "Navigation label for Security scan history.",
      }),
      to: { pathname: "/scans", search: sharedCollectionSearch },
    });
    breadcrumbs.push({
      label: isNewScan
        ? intl.formatMessage({
            id: "codex.security.workbench.navigation.new_scan.label",
            defaultMessage: "New scan",
            description:
              "Current-page breadcrumb label for Security scan setup.",
          })
        : shortHash(runId!),
      title: runId,
    });
  }

  function collectionLocation(next: Collection) {
    // Re-selecting the current collection must not clear its filters or page.
    // Detail routes still navigate back to the collection when its tab is used.
    if (location.pathname === `/${next}`) return location;
    const params = new URLSearchParams(sharedCollectionSearch);
    const current = new URLSearchParams(location.search);
    const repositories = (current.get("repo") ?? "")
      .split(",")
      .map((value) => value.trim())
      .filter((value) => value && value.toLowerCase() !== "all");
    const repositoryIds = (current.get("repo_id") ?? repositoryId ?? "")
      .split(",")
      .map((value) => value.trim())
      .filter(Boolean);
    // Overview/Findings accept CSV scope; Scans resolves exactly one repository.
    // The Repositories management list has no repository-scope filter.
    if (next === "overview" || next === "findings") {
      if (repositories.length > 0) params.set("repo", repositories.join(","));
      if (repositories.length <= 1 && repositoryIds.length === 1) {
        params.set("repo_id", repositoryIds[0]!);
      }
    } else if (
      next === "scans" &&
      repositories.length <= 1 &&
      repositoryIds.length <= 1
    ) {
      if (repositories.length === 1) params.set("repo", repositories[0]!);
      if (repositoryIds.length === 1) params.set("repo_id", repositoryIds[0]!);
    }
    const search = params.toString();
    return {
      pathname: `/${next}`,
      search: search ? `?${search}` : "",
    };
  }

  function scanSetupLocation() {
    const params = new URLSearchParams(sharedCollectionSearch);
    const current = new URLSearchParams(location.search);
    const repositoryUrl = current.get("repo");
    const selectedRepositoryId = current.get("repo_id") ?? repositoryId;
    if (selectedRepositoryId) {
      params.set("repo_id", selectedRepositoryId);
      if (repositoryUrl) params.set("repo", repositoryUrl);
    }
    const search = params.toString();
    return {
      pathname: "/scans/new",
      search: search ? `?${search}` : "",
    };
  }

  function changeRepositoryScope(
    repositories: string[],
    selectedRepositoryId?: string,
  ) {
    const params = new URLSearchParams(location.search);
    if (repositories.length > 0) {
      params.set("repo", repositories.join(","));
    } else {
      params.delete("repo");
    }
    if (repositories.length === 1 && selectedRepositoryId) {
      params.set("repo_id", selectedRepositoryId);
    } else {
      params.delete("repo_id");
    }
    params.delete("cursor");
    params.delete("page");
    const search = params.toString();
    navigate(
      { search: search ? `?${search}` : "", hash: location.hash },
      { replace: true },
    );
  }

  // Overview and Findings own their data and supply their refresh controls.
  // Scan setup retains the existing focused back-navigation flow.
  if (
    isNewScan ||
    (actions == null && (collection === "overview" || showRepositoryScope))
  ) {
    return null;
  }
  const showBreadcrumbs =
    isDetail &&
    !findingId &&
    !isRepositoryCollection &&
    !(repositorySection === "findings" && repositoryItemId);
  const options: Array<{ id: Collection; label: string }> = [
    ...(cloud.overviewEnabled
      ? [
          {
            id: "overview" as const,
            label: intl.formatMessage({
              id: "codexSecurity.navigation.overview.label",
              defaultMessage: "Overview",
              description:
                "Navigation tab for the workspace Security overview.",
            }),
          },
        ]
      : []),
    {
      id: "findings",
      label: intl.formatMessage({
        id: "codex.security.workbench.navigation.findings.label",
        defaultMessage: "Findings",
        description: "Navigation tab for Security findings.",
      }),
    },
    {
      id: "repositories",
      label: intl.formatMessage({
        id: "defenseFactory.navigation.repositories",
        defaultMessage: "Repositories",
        description: "Navigation tab for configured repositories.",
      }),
    },
    {
      id: "scans",
      label: intl.formatMessage({
        id: "codex.security.workbench.navigation.scans.label",
        defaultMessage: "Scans",
        description: "Navigation tab for Security scan history.",
      }),
    },
  ];
  return (
    <header className="df-workbench-navigation">
      <div className="df-workbench-navigation-row">
        <nav
          className="df-workbench-tabs"
          aria-label={intl.formatMessage({
            id: "codex.security.workbench.navigation.collections.aria_label",
            defaultMessage: "Security sections",
            description:
              "Accessible label for the primary Security workspace navigation.",
          })}
        >
          {options.map(({ id, label }) => (
            <AppLink
              key={id}
              to={collectionLocation(id)}
              className="df-workbench-navigation-tab"
              aria-current={collection === id ? "page" : undefined}
            >
              {label}
            </AppLink>
          ))}
        </nav>
        <div className="df-workbench-page-actions">
          {actions}
          {showRepositoryScope ? (
            <RepositoryScopeControl
              repositories={getOverviewRepositories(location.search)}
              onChange={changeRepositoryScope}
            />
          ) : null}
          <WorkbenchLink to={scanSetupLocation()}>
            <WorkbenchIcon name="play" />
            <FormattedMessage
              id="defenseFactory.navigation.scan"
              defaultMessage="Scan"
              description="Open the existing Security scan setup."
            />
          </WorkbenchLink>
        </div>
      </div>
      {showBreadcrumbs ? (
        <nav
          aria-label={intl.formatMessage({
            id: "codex.security.workbench.navigation.breadcrumb.aria_label",
            defaultMessage: "Security page navigation",
            description: "Accessible label for Security page breadcrumbs.",
          })}
          className="df-workbench-breadcrumbs"
        >
          {breadcrumbs.map((breadcrumb, index) => (
            <span
              key={`${breadcrumb.label}-${index}`}
              title={breadcrumb.title}
              aria-current={
                index === breadcrumbs.length - 1 ? "page" : undefined
              }
            >
              {index > 0 ? (
                <span aria-hidden className="px-2 text-tertiary">
                  /
                </span>
              ) : null}
              {breadcrumb.to ? (
                <AppLink
                  to={breadcrumb.to}
                  state={location.state}
                  className="hover:underline"
                >
                  {breadcrumb.label}
                </AppLink>
              ) : (
                <span>{breadcrumb.label}</span>
              )}
            </span>
          ))}
        </nav>
      ) : null}
    </header>
  );
}
