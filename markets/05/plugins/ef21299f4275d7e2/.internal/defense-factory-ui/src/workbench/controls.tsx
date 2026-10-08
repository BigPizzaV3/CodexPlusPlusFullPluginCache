import { Search } from "@oai/ds/icons/search";
import { XCircle } from "@oai/ds/icons/x-circle";
import { Badge } from "@oai/ds/ui/badge";
import { Button } from "@oai/ds/ui/button";
import { Input } from "@oai/ds/ui/input";
import {
  useRef,
  type ComponentProps,
  type ReactNode,
  type RefObject,
} from "react";
import { useIntl } from "react-intl";

import { AppLink, ExternalLink } from "../link";

type WorkbenchButtonProps = Omit<
  ComponentProps<typeof Button>,
  "color" | "size" | "variant" | "pill" | "squircle"
> & {
  color?: keyof typeof buttonAppearance;
  size?: keyof typeof buttonSizes;
  radius?: "default" | "small";
};

type WorkbenchSearchInputProps = {
  id: string;
  inputRef?: RefObject<HTMLInputElement | null>;
  label: string;
  onSearchQueryChange: (value: string) => void;
  placeholder: string;
  searchQuery: string;
};

const buttonAppearance = {
  primary: { color: "primary", variant: "solid" },
  secondary: { color: "primary", variant: "soft" },
  outlineSurface: { color: "primary", variant: "outline" },
  ghost: { color: "secondary", variant: "ghost" },
  ghostSecondary: { color: "secondary", variant: "ghost" },
  danger: { color: "danger", variant: "soft" },
  dangerSolid: { color: "danger", variant: "solid" },
} as const;

const buttonSizes = {
  toolbar: "lg",
  compact: "xs",
  iconCircle: "lg",
  iconCircleSm: "3xs",
} as const;

const badgeColors = {
  default: "secondary",
  outline: "secondary",
  success: "success",
  warning: "warning",
  danger: "danger",
  reserve: "warning",
} as const;

// Keep the workbench's presentation API while shared controls own interaction.
export function WorkbenchButton({
  className,
  color = "primary",
  size = "toolbar",
  radius = "default",
  uniform = false,
  ...props
}: WorkbenchButtonProps) {
  return (
    <Button
      {...props}
      {...buttonAppearance[color]}
      size={buttonSizes[size]}
      pill={radius === "default" && size !== "toolbar" && size !== "compact"}
      squircle={false}
      uniform={uniform || size === "iconCircle" || size === "iconCircleSm"}
      data-workbench-color={color}
      data-workbench-size={size}
      className={["df-button", size === "toolbar" && "df-control", className]
        .filter(Boolean)
        .join(" ")}
    />
  );
}

/** Navigation uses an anchor; the DS Button only renders an action button. */
export function WorkbenchLink({
  color = "primary",
  className,
  ...props
}: (ComponentProps<typeof AppLink> | ComponentProps<typeof ExternalLink>) & {
  color?: "primary" | "outlineSurface" | "ghostSecondary";
}) {
  const linkProps = {
    ...props,
    "data-workbench-color": color,
    className: ["df-button df-control df-button-link", className]
      .filter(Boolean)
      .join(" "),
  };
  return "to" in linkProps ? (
    <AppLink {...linkProps} />
  ) : (
    <ExternalLink {...linkProps} />
  );
}

export function WorkbenchInput({
  className,
  ...props
}: ComponentProps<typeof Input>) {
  return (
    <Input
      {...props}
      className={["df-input", className].filter(Boolean).join(" ")}
    />
  );
}

export function WorkbenchSearchInput({
  id,
  inputRef,
  label,
  onSearchQueryChange,
  placeholder,
  searchQuery,
}: WorkbenchSearchInputProps) {
  const intl = useIntl();
  const localInputRef = useRef<HTMLInputElement>(null);
  const searchInputRef = inputRef ?? localInputRef;

  return (
    <div className="df-search" role="search">
      <label className="sr-only" htmlFor={id}>
        {label}
      </label>
      <WorkbenchInput
        id={id}
        ref={searchInputRef}
        autoComplete="off"
        onChange={(event) => onSearchQueryChange(event.target.value)}
        placeholder={placeholder}
        role="searchbox"
        value={searchQuery}
        startAdornment={<Search className="df-search-icon" aria-hidden />}
        endAdornment={
          searchQuery.length > 0 ? (
            <Button
              color="secondary"
              variant="ghost"
              size="3xs"
              uniform
              aria-label={intl.formatMessage({
                id: "skills.pageSearchInput.clear",
                defaultMessage: "Clear search",
                description: "Accessible label for clearing a search field",
              })}
              onClick={() => {
                onSearchQueryChange("");
                searchInputRef.current?.focus();
              }}
            >
              <XCircle aria-hidden />
            </Button>
          ) : undefined
        }
      />
    </div>
  );
}

// Preserve the existing status variants through the shared badge primitive.
export function WorkbenchBadge({
  children,
  className,
  variant = "default",
}: {
  children: ReactNode;
  className?: string;
  variant?: keyof typeof badgeColors;
}) {
  return (
    <Badge
      className={["df-badge", `df-badge-${variant}`, className]
        .filter(Boolean)
        .join(" ")}
      color={badgeColors[variant]}
      variant={variant === "outline" ? "outline" : "soft"}
      pill={variant !== "default" && variant !== "outline"}
    >
      {children}
    </Badge>
  );
}
