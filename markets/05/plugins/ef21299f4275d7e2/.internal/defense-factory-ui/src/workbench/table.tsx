import clsx from "clsx";
import type {
  AriaAttributes,
  ComponentProps,
  HTMLAttributes,
  ReactNode,
} from "react";
import { AppLink } from "../link";
import "./table.css";

function TableHeader({ children }: { children?: ReactNode }) {
  return (
    <thead>
      <tr>{children}</tr>
    </thead>
  );
}

function TableHeaderCell({
  textAlign = "left",
  children,
  className,
  ariaSort,
}: {
  textAlign?: "left" | "right" | "center";
  children?: ReactNode;
  className?: string;
  ariaSort?: AriaAttributes["aria-sort"];
}) {
  return (
    <th
      aria-sort={ariaSort}
      className={clsx(
        "text-token border-token-border-medium bg-token-main-surface-primary sticky top-0 z-10 border-b-[0.5px] py-2 pe-4 font-semibold last:pe-0",
        textAlign === "left"
          ? "text-start"
          : textAlign === "right"
            ? "text-end"
            : "text-center",
        className,
      )}
    >
      {children}
    </th>
  );
}

function TableBody({
  children,
  ...rest
}: HTMLAttributes<HTMLTableSectionElement>) {
  return <tbody {...rest}>{children}</tbody>;
}

function TableRow({
  children,
  className,
}: {
  children?: ReactNode;
  className?: string;
}) {
  return <tr className={clsx("df-table-row", className)}>{children}</tr>;
}

/** One primary link spans the row; other links and controls keep their targets. */
function TableRowLink({
  className,
  ...props
}: ComponentProps<typeof AppLink>) {
  return (
    <AppLink
      {...props}
      className={clsx("df-table-row-link", className)}
    />
  );
}

/** Row metadata remains selectable without adding another keyboard stop. */
function TableRowTextLink({
  className,
  ...props
}: ComponentProps<typeof AppLink>) {
  return (
    <AppLink
      {...props}
      className={clsx("df-table-row-text-link", className)}
      tabIndex={-1}
    />
  );
}

function TableCell({
  textAlign = "left",
  children,
  className,
  divClassName = "min-h-[40px] items-center",
  colSpan,
}: {
  textAlign?: "left" | "right" | "center";
  children?: ReactNode;
  className?: string;
  divClassName?: string;
  colSpan?: number;
}) {
  return (
    <td
      className={clsx(
        "border-token-border-medium border-b-[0.5px] pe-4 align-top last:pe-0 [tr:last-child_&]:border-b-0",
        textAlign === "left"
          ? "text-left"
          : textAlign === "right"
            ? "text-right"
            : "text-center",
        className,
      )}
      colSpan={colSpan}
    >
      <div
        className={clsx(
          "flex",
          textAlign === "right" && "justify-end",
          textAlign === "center" && "justify-center",
          divClassName,
        )}
      >
        {children}
      </div>
    </td>
  );
}

function TableRoot({
  children,
  fixed = false,
  className,
}: {
  children?: ReactNode;
  className?: string;
  fixed?: boolean;
}) {
  return (
    <div className={clsx("text-token-text-primary text-sm", className)}>
      <table
        className={clsx(
          "w-full border-separate border-spacing-0",
          fixed && "table-fixed",
        )}
      >
        {children}
      </table>
    </div>
  );
}

const Table = {
  Root: TableRoot,
  Header: TableHeader,
  HeaderCell: TableHeaderCell,
  Body: TableBody,
  Row: TableRow,
  RowLink: TableRowLink,
  RowTextLink: TableRowTextLink,
  Cell: TableCell,
};
export default Table;
