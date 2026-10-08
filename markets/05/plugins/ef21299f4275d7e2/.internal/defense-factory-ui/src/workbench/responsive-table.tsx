import Table from "./table";
import { PageTableSortHeaderButton } from "./sort-header";
import { useSyncExternalStore, type ReactNode } from "react";
import { FormattedMessage, type MessageDescriptor } from "react-intl";

export type WorkbenchTableField<
  FieldId extends string,
  SortField extends string,
> = {
  id: FieldId;
  label: MessageDescriptor;
  sort: SortField | null;
  sortLabel?: MessageDescriptor;
  headerClassName: string;
  cellClassName: string;
  stackedFullWidth?: boolean;
};

// The first field anchors each compact row. All other fields remain visible
// beneath it, and sortable fields keep their controls in the compact header.
export const WorkbenchResponsiveTable = <
  FieldId extends string,
  SortField extends string,
>({
  fields,
  activeSortField,
  sortDirection,
  onSort,
  children,
}: {
  fields: readonly WorkbenchTableField<FieldId, SortField>[];
  activeSortField: SortField;
  sortDirection: "asc" | "desc";
  onSort: (field: SortField) => void;
  children: (layout: {
    columnCount: number;
    renderCells: (values: Record<FieldId, ReactNode>) => ReactNode;
  }) => ReactNode;
}) => {
  "use forget";
  const isWide = useSyncExternalStore(
    subscribeToWidth,
    isWideScreen,
    () => false,
  );
  const visibleFields = isWide ? fields : fields.slice(0, 1);

  const renderSortControl = (
    field: WorkbenchTableField<FieldId, SortField>,
  ) => {
    const sort = field.sort;
    if (!sort) return null;
    return (
      <PageTableSortHeaderButton
        key={field.id}
        active={activeSortField === sort}
        direction={sortDirection}
        onClick={() => onSort(sort)}
        className="whitespace-nowrap"
      >
        <span aria-hidden={field.sortLabel ? true : undefined}>
          <FormattedMessage {...field.label} />
        </span>
        {field.sortLabel ? (
          <span className="sr-only">
            <FormattedMessage {...field.sortLabel} />
          </span>
        ) : null}
      </PageTableSortHeaderButton>
    );
  };

  const renderCells = (values: Record<FieldId, ReactNode>) =>
    visibleFields.map((field) => (
      <Table.Cell
        key={field.id}
        divClassName={
          isWide
            ? field.cellClassName
            : "flex min-w-0 flex-col items-start gap-2 py-4"
        }
      >
        {values[field.id]}
        {!isWide ? (
          <div className="flex w-full flex-wrap items-center gap-x-3 gap-y-2 text-[12px] leading-4">
            {fields.slice(1).map((item) => (
              <div
                key={item.id}
                className={
                  item.stackedFullWidth
                    ? "flex w-full min-w-0 items-center gap-2"
                    : "flex min-w-0 items-center"
                }
              >
                {values[item.id]}
              </div>
            ))}
          </div>
        ) : null}
      </Table.Cell>
    ));

  return (
    <Table.Root className="overflow-x-auto" fixed={!isWide}>
      <Table.Header>
        {visibleFields.map((field) => {
          const sort = field.sort ?? (!isWide ? activeSortField : null);
          return (
            <Table.HeaderCell
              key={field.id}
              className={isWide ? field.headerClassName : "py-3 ps-4 pe-4!"}
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
              {!isWide ? (
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <FormattedMessage {...field.label} />
                  <div className="flex flex-wrap items-center gap-3">
                    {fields.map(renderSortControl)}
                  </div>
                </div>
              ) : field.sort ? (
                renderSortControl(field)
              ) : (
                <FormattedMessage {...field.label} />
              )}
            </Table.HeaderCell>
          );
        })}
      </Table.Header>
      <Table.Body>
        {children({ columnCount: visibleFields.length, renderCells })}
      </Table.Body>
    </Table.Root>
  );
};

const isWideScreen = () => window.matchMedia("(min-width: 1024px)").matches;
function subscribeToWidth(onChange: () => void) {
  const media = window.matchMedia("(min-width: 1024px)");
  media.addEventListener("change", onChange);
  return () => media.removeEventListener("change", onChange);
}
