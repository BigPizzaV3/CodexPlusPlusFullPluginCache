import { Info as InfoIcon } from "@oai/ds/icons/info";
import { LoadingIndicator as Spinner } from "@oai/ds/ui/indicator";
import { workbenchStyles } from "./styles";
import { Badge, type BadgeProps } from "@oai/ds/ui/badge";
import type { ReactNode } from "react";
import { FormattedMessage } from "react-intl";

export const WorkbenchPageHeader = ({
  title,
  description,
  actions,
  kind = "collection",
  titlePrefix,
  titleAdornment,
  metadata,
}: {
  title?: ReactNode;
  description?: ReactNode;
  actions?: ReactNode;
  kind?: "collection" | "detail";
  titlePrefix?: ReactNode;
  titleAdornment?: ReactNode;
  metadata?: ReactNode;
}) => {
  "use forget";
  const Heading = kind === "detail" ? "h1" : "h2";

  return (
    <header className="flex flex-col items-start gap-4 sm:flex-row sm:justify-between">
      <div className="w-full min-w-0 flex-1 space-y-2 sm:w-auto">
        <div className="flex flex-wrap items-center gap-3">
          {titlePrefix}
          {title != null ? (
            <Heading
              className={
                kind === "detail"
                  ? workbenchStyles.detailTitle
                  : workbenchStyles.collectionTitle
              }
            >
              {title}
            </Heading>
          ) : null}
          {titleAdornment}
        </div>
        {description ? (
          <div className={workbenchStyles.description}>{description}</div>
        ) : null}
        {metadata ? (
          <div className="text-token-text-secondary flex flex-wrap items-center gap-3 text-sm">
            {metadata}
          </div>
        ) : null}
      </div>
      {actions ? (
        <div className="flex max-w-full flex-wrap items-center gap-2 sm:shrink-0">
          {actions}
        </div>
      ) : null}
    </header>
  );
};

export const WorkbenchToolbar = ({ children }: { children: ReactNode }) => {
  "use forget";
  return <div className="df-toolbar">{children}</div>;
};

export const WorkbenchTableFooter = ({
  summary,
  children,
}: {
  summary: ReactNode;
  children?: ReactNode;
}) => {
  "use forget";
  return (
    <div className="df-table-footer">
      <div>{summary}</div>
      {children ? (
        <div className="flex flex-wrap items-center gap-2">{children}</div>
      ) : null}
    </div>
  );
};

export const WorkbenchState = ({
  children,
  title,
  loading = false,
  variant = "panel",
  action,
}: {
  children?: ReactNode;
  title?: ReactNode;
  loading?: boolean;
  variant?: "inline" | "table" | "panel";
  action?: ReactNode;
}) => {
  "use forget";
  const message =
    children ??
    (loading ? (
      <FormattedMessage
        id="codex.security.workbench.state.loading.label"
        defaultMessage="Loading…"
        description="Short, reassuring loading status beside a spinner in a Codex Security operations-workspace table or detail panel when a more specific loading message is not available. It is announced to screen-reader users while the requested content is being fetched."
      />
    ) : null);
  const icon = loading ? (
    <Spinner
      className={[
        "text-token-text-tertiary h-4 w-4 shrink-0",
        variant === "inline" && "mt-0.5",
      ]
        .flat()
        .filter(Boolean)
        .join(" ")}
    />
  ) : variant === "inline" ? (
    <InfoIcon className="icon-sm mt-0.5 shrink-0" />
  ) : null;

  return (
    <div
      className={[
        "text-token-text-secondary flex gap-3 text-[14px] leading-5",
        variant === "inline"
          ? "border-token-border-light bg-token-bg-tertiary/40 items-start rounded-xl border px-4 py-3"
          : "items-center justify-center p-6 text-center",
        variant === "table" && "min-h-40 w-full",
        variant === "panel" && [workbenchStyles.card, "min-h-48"],
      ]
        .flat()
        .filter(Boolean)
        .join(" ")}
      role="status"
    >
      {variant !== "inline" ? icon : null}
      <div
        className={[
          "min-w-0",
          variant === "inline"
            ? "flex flex-1 flex-wrap items-center gap-x-4 gap-y-2"
            : "space-y-2",
        ]
          .flat()
          .filter(Boolean)
          .join(" ")}
      >
        <div
          className={[
            "min-w-0",
            variant === "inline" && "flex flex-1 basis-48 items-start gap-3",
          ]
            .flat()
            .filter(Boolean)
            .join(" ")}
        >
          {variant === "inline" ? icon : null}
          <div className="min-w-0 space-y-2">
            {title ? (
              <h2 className={workbenchStyles.sectionTitle}>{title}</h2>
            ) : null}
            {message ? <div>{message}</div> : null}
          </div>
        </div>
        {action ? (
          <div className={variant === "inline" ? "ms-auto shrink-0" : "pt-1"}>
            {action}
          </div>
        ) : null}
      </div>
    </div>
  );
};

const WORKBENCH_BADGE_COLORS = {
  success: "success",
  danger: "danger",
  warning: "warning",
  info: "info",
  purple: "discovery",
  neutral: "secondary",
  muted: "secondary",
  critical: "danger",
  high: "warning",
  medium: "warning",
  low: "success",
  informational: "info",
} as const satisfies Record<string, NonNullable<BadgeProps["color"]>>;

export type WorkbenchStatusBadgeVariant = keyof typeof WORKBENCH_BADGE_COLORS;

export const WorkbenchStatusBadge = ({
  variant,
  icon,
  label,
  children,
}: {
  variant: WorkbenchStatusBadgeVariant;
  icon?: ReactNode;
  label?: string;
  children: ReactNode;
}) => {
  "use forget";
  return (
    <div
      className="puik-root inline-flex w-fit max-w-full shrink-0"
      title={label}
    >
      <Badge
        className={`df-status-badge max-w-full${
          variant === "medium" ? " df-finding-severity-medium" : ""
        }`}
        color={WORKBENCH_BADGE_COLORS[variant]}
        variant="soft"
        size="sm"
      >
        {icon}
        {label ? (
          <span className="sr-only">
            <FormattedMessage
              id="codexSecurity.workbench.badge.accessibleLabel"
              defaultMessage="{label}: "
              description="Screen-reader prefix before a metadata badge value. The label identifies what the value represents, such as Repository or Started."
              values={{ label }}
            />
          </span>
        ) : null}
        {children}
      </Badge>
    </div>
  );
};
