import { WorkbenchButton as Button, WorkbenchSearchInput } from "./controls";
import { WorkbenchIcon } from "./icons";
import { Checkbox } from "@oai/ds/ui/checkbox";
import { Popover } from "@oai/ds/ui/popover";
import { useQuery } from "@tanstack/react-query";
import { useId, useMemo, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { securityClient } from "../client";
import { repositoryLabel } from "../ui";
import { OverviewRequestError } from "./overview-components";

import { RepositoryScopeOptions } from "./repository-scope-options";

export function RepositoryScopeControl({
  repositories,
  onChange,
}: {
  repositories: string[];
  onChange: (repositories: string[], repositoryId?: string) => void;
}) {
  const intl = useIntl();
  const searchId = useId();
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const query = useQuery({
    queryKey: ["monitoring-metadata"],
    queryFn: () => securityClient.request({ operation: "monitoring_metadata" }),
    staleTime: 60_000,
  });

  const options = useMemo(
    () =>
      Array.from(
        new Set([
          ...(query.data?.items.map((item) => item.repo_url) ?? []),
          ...repositories,
        ]),
      )
        .filter(Boolean)
        .sort()
        .map((value) => ({ value, label: repositoryLabel(value) || value })),
    [query.data, repositories],
  );
  const term = search.trim().toLocaleLowerCase();
  const matchingOptions = useMemo(
    () =>
      options.filter((option) =>
        option.label.toLocaleLowerCase().includes(term),
      ),
    [options, term],
  );
  const selected = useMemo(() => new Set(repositories), [repositories]);
  const onlyRepository = repositories[0];
  const triggerLabel =
    repositories.length === 0
      ? intl.formatMessage({
          id: "codexSecurity.overview.repositories.filter.all",
          defaultMessage: "All repositories",
          description:
            "Overview repository filter value when no repository scope is selected.",
        })
      : repositories.length === 1 && onlyRepository
      ? repositoryLabel(onlyRepository) || onlyRepository
      : intl.formatMessage(
          {
            id: "codexSecurity.overview.repositories.filter.count",
            defaultMessage: "{count, number} repositories",
            description:
              "Overview repository filter value when several repositories are selected.",
          },
          { count: repositories.length },
        );

  function setRepository(repository: string, checked: boolean) {
    const next = new Set(repositories);
    if (checked) next.add(repository);
    else next.delete(repository);
    const selectedRepositories = Array.from(next).sort();
    const repositoryId =
      selectedRepositories.length === 1
        ? query.data?.items.find(
            (item) => item.repo_url === selectedRepositories[0],
          )?.repo_id
        : undefined;
    onChange(selectedRepositories, repositoryId);
  }

  return (
    <div className="df-repository-scope">
      <span className="sr-only">
        <FormattedMessage
          id="codexSecurity.overview.repositories.filter.label"
          defaultMessage="Repositories"
          description="Label for the Security overview repository scope filter."
        />
      </span>
      <Popover
        open={open}
        onOpenChange={(nextOpen) => {
          if (nextOpen) setSearch("");
          setOpen(nextOpen);
        }}
      >
        <Popover.Trigger>
          <Button
            color="outlineSurface"
            size="toolbar"
            radius="small"
            className="w-full justify-between"
            aria-label={intl.formatMessage(
              {
                id: "codexSecurity.overview.repositories.filter.ariaLabel",
                defaultMessage: "Repositories: {selection}",
                description:
                  "Accessible label for the overview repository scope control.",
              },
              { selection: triggerLabel },
            )}
          >
            <span className="max-w-72 truncate">{triggerLabel}</span>
            <WorkbenchIcon name="chevronDown" />
          </Button>
        </Popover.Trigger>
        <Popover.Content align="start" minWidth={300} width={360}>
          <div className="flex max-h-[min(30rem,75vh)] flex-col gap-3 p-3">
            <WorkbenchSearchInput
              id={searchId}
              searchQuery={search}
              onSearchQueryChange={setSearch}
              placeholder={intl.formatMessage({
                id: "codexSecurity.overview.repositories.filter.search",
                defaultMessage: "Search repositories",
                description:
                  "Placeholder in the overview repository filter search field.",
              })}
              label={intl.formatMessage({
                id: "codexSecurity.overview.repositories.filter.search",
                defaultMessage: "Search repositories",
                description:
                  "Accessible label for the overview repository filter search field.",
              })}
            />
            <div className="min-h-0">
              <label className="hover:bg-token-interactive-bg-tertiary-hover flex min-h-10 cursor-pointer items-center gap-3 rounded-lg px-2 py-2 text-[14px] leading-5">
                <Checkbox
                  checked={repositories.length === 0}
                  onCheckedChange={() => onChange([])}
                  aria-label={intl.formatMessage({
                    id: "codexSecurity.overview.repositories.filter.all",
                    defaultMessage: "All repositories",
                    description:
                      "Overview repository filter option that clears repository narrowing.",
                  })}
                />
                <FormattedMessage
                  id="codexSecurity.overview.repositories.filter.all"
                  defaultMessage="All repositories"
                  description="Overview repository filter option that clears repository narrowing."
                />
              </label>
              {query.isPending ? (
                <p
                  className="text-token-text-tertiary px-2 py-4 text-sm"
                  role="status"
                >
                  <FormattedMessage
                    id="codexSecurity.overview.repositories.filter.loading"
                    defaultMessage="Loading repositories…"
                    description="Status in the overview repository filter while its authorized options load."
                  />
                </p>
              ) : matchingOptions.length === 0 ? (
                <p
                  className="text-token-text-tertiary px-2 py-4 text-sm"
                  role="status"
                >
                  <FormattedMessage
                    id="codexSecurity.overview.repositories.filter.empty"
                    defaultMessage="No matching repositories"
                    description="Empty state when repository filter search finds no options."
                  />
                </p>
              ) : (
                <RepositoryScopeOptions
                  key={term}
                  options={matchingOptions}
                  selected={selected}
                  onToggle={setRepository}
                />
              )}
            </div>
          </div>
        </Popover.Content>
      </Popover>
      {query.error ? (
        <OverviewRequestError
          isRetrying={query.isFetching}
          onRetry={() => void query.refetch({ cancelRefetch: false })}
        >
          <FormattedMessage
            id="codexSecurity.overview.repositories.filter.error"
            defaultMessage="Unable to load the repository list."
            description="Error in the overview repository selector. The current scope and dashboard data remain unchanged."
          />
        </OverviewRequestError>
      ) : null}
    </div>
  );
}
