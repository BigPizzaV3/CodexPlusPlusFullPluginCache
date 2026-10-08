import { ArrowUp as ArrowUpIcon } from "@oai/ds/icons/arrow-up";
import type React from "react";

interface PageTableSortHeaderButtonProps {
  active: boolean;
  direction: "asc" | "desc";
  disabled?: boolean;
  onClick: () => void;
  className?: string;
  children: React.ReactNode;
}

export const PageTableSortHeaderButton = ({
  active,
  direction,
  disabled,
  onClick,
  className,
  children,
}: PageTableSortHeaderButtonProps) => {
  "use forget";

  return (
    <button
      type="button"
      aria-pressed={active}
      disabled={disabled}
      onClick={onClick}
      className={[
        "focus-visible:outline-2 focus-visible:outline-offset-4 flex items-center gap-1 text-start outline-none",
        className,
      ]
        .flat()
        .filter(Boolean)
        .join(" ")}
      data-page-table-header-focus-target="true"
      data-page-table-header-cell-focus-target="true"
    >
      {children}
      {active && (
        <ArrowUpIcon
          aria-hidden="true"
          className={[
            "text-token-icon-secondary h-[14px] w-[14px] transition-transform",
            direction === "desc" && "rotate-180",
          ]
            .flat()
            .filter(Boolean)
            .join(" ")}
        />
      )}
    </button>
  );
};
