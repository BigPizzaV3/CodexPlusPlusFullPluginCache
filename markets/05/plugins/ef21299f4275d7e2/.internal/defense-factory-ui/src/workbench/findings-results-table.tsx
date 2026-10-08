import type { ReactNode } from "react";
import { FormattedMessage } from "react-intl";
import { findingFields, type FindingSortField } from "./findings-fields";
import { PageTableSortHeaderButton } from "./sort-header";
import Table from "./table";

// The design uses priority, owner, issue status, and due date. Those are not
// list fields yet, so preserve its row hierarchy using actual severity/status.
const tableFields = ["severity", "finding", "status", "detected"] as const;
export type FindingsColumnId = (typeof tableFields)[number];

export function FindingsResultsTable({
  activeSortField,
  sortDirection,
  onSort,
  children,
}: {
  activeSortField: FindingSortField;
  sortDirection: "asc" | "desc";
  onSort: (field: FindingSortField) => void;
  children: (layout: {
    columnCount: number;
    renderCells: (values: Record<FindingsColumnId, ReactNode>) => ReactNode;
  }) => ReactNode;
}) {
  return (
    <Table.Root className="df-findings-table-scroll">
      <Table.Header>
        {tableFields.map((id) => {
          const field = findingFields.find((item) => item.id === id)!;
          const sort = field.sort;
          return (
            <Table.HeaderCell
              key={id}
              className={`df-findings-column-${id}`}
              ariaSort={
                sort
                  ? activeSortField === sort
                    ? sortDirection === "asc"
                      ? "ascending"
                      : "descending"
                    : "none"
                  : undefined
              }
            >
              {sort ? (
                <PageTableSortHeaderButton
                  active={activeSortField === sort}
                  direction={sortDirection}
                  onClick={() => onSort(sort)}
                >
                  <FormattedMessage {...field.label} />
                </PageTableSortHeaderButton>
              ) : (
                <FormattedMessage {...field.label} />
              )}
              {id === "finding" ? (
                <span className="df-findings-mobile-sort">
                  {findingFields.map((item) => {
                    const mobileSort = item.sort;
                    return mobileSort ? (
                      <PageTableSortHeaderButton
                        key={item.id}
                        active={activeSortField === mobileSort}
                        direction={sortDirection}
                        onClick={() => onSort(mobileSort)}
                      >
                        <FormattedMessage {...item.label} />
                        {activeSortField === mobileSort ? (
                          <span className="sr-only">
                            {" — "}
                            <FormattedMessage
                              id="defenseFactory.findings.sort.direction"
                              defaultMessage="{direction, select, asc {Sorted ascending} other {Sorted descending}}"
                              description="Announces the current sort direction on the active compact findings table sort button."
                              values={{ direction: sortDirection }}
                            />
                          </span>
                        ) : null}
                      </PageTableSortHeaderButton>
                    ) : null;
                  })}
                </span>
              ) : null}
            </Table.HeaderCell>
          );
        })}
      </Table.Header>
      <Table.Body>
        {children({
          columnCount: tableFields.length,
          renderCells: (values) =>
            tableFields.map((id) => (
              <Table.Cell
                key={id}
                className={`df-findings-column-${id}`}
                divClassName="df-findings-cell"
              >
                {values[id]}
              </Table.Cell>
            )),
        })}
      </Table.Body>
    </Table.Root>
  );
}
