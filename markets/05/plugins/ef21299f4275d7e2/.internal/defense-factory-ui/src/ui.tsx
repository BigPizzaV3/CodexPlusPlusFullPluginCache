import { Badge } from "@oai/ds/ui/badge";
import { Markdown, type MarkdownComponent } from "@oai/ds/ui/markdown";
import { TextLink } from "@oai/ds/ui/text-link";
import type { ReactNode } from "react";
import { FormattedDate, FormattedMessage, useIntl } from "react-intl";

import { statusLabel } from "./labels";
import { ExternalLink } from "./link";
import { WorkbenchButton as Button } from "./workbench/controls";

const ReportLink: MarkdownComponent = ({ node: _node, children, ...props }) => (
  <TextLink {...props} as={ExternalLink}>
    {children}
  </TextLink>
);

const reportComponents = { a: ReportLink };

export function RequestState({
  error,
  retry,
}: {
  error?: Error | null;
  retry?: () => void;
}) {
  return (
    <div
      className="flex min-h-40 flex-col items-center justify-center gap-4 p-8 text-secondary"
      role={error ? "alert" : "status"}
    >
      {error ? (
        <>
          <p>{error.message}</p>
          {retry && (
            <Button color="outlineSurface" onClick={retry}>
              <FormattedMessage
                id="defenseFactory.plugin.retry"
                defaultMessage="Try again"
                description="Retry a failed Security request"
              />
            </Button>
          )}
        </>
      ) : (
        <FormattedMessage
          id="defenseFactory.plugin.loading"
          defaultMessage="Loading…"
          description="Security data is loading"
        />
      )}
    </div>
  );
}

export function Empty({ children }: { children: ReactNode }) {
  return (
    <div className="flex min-h-40 items-center justify-center p-8 text-secondary">
      {children}
    </div>
  );
}

export function Section({
  title,
  children,
}: {
  title: ReactNode;
  children: ReactNode;
}) {
  return (
    <section className="flex min-w-0 flex-col gap-4 rounded-xl border border-default p-6">
      <h2 className="heading-md">{title}</h2>
      {children}
    </section>
  );
}

export function Property({
  title,
  children,
}: {
  title: ReactNode;
  children: ReactNode;
}) {
  return (
    <div className="flex min-w-0 flex-col gap-1">
      <dt className="text-sm text-secondary">{title}</dt>
      <dd className="min-w-0 break-words">{children}</dd>
    </div>
  );
}

export function Status({ value }: { value: string }) {
  const intl = useIntl();
  const color =
    value === "critical" || value === "failed"
      ? "danger"
      : value === "high"
      ? "warning"
      : value === "completed" || value === "fixed"
      ? "success"
      : "secondary";
  return (
    <Badge className="df-status-badge" color={color}>
      {statusLabel(intl, value)}
    </Badge>
  );
}

export function DateTime({ value }: { value: string | null | undefined }) {
  return value ? (
    <FormattedDate
      value={value}
      year="numeric"
      month="short"
      day="numeric"
      hour="numeric"
      minute="2-digit"
    />
  ) : (
    <>—</>
  );
}

export function Report({ children }: { children: string }) {
  // Reports are repository-controlled content. Render text/links, never remote images or raw HTML.
  return (
    <Markdown
      skipHtml
      disallowedElements={["img"]}
      components={reportComponents}
    >
      {children}
    </Markdown>
  );
}

export function Pager({
  previous,
  next,
  children,
  busy,
  first,
}: {
  first?: boolean;
  previous?: () => void;
  next?: () => void;
  children?: ReactNode;
  busy?: boolean;
}) {
  return (
    <footer className="df-table-footer">
      <span>{children}</span>
      <div className="flex gap-2">
        <Button
          color="outlineSurface"
          disabled={!previous || busy}
          onClick={previous}
        >
          {first ? (
            <FormattedMessage
              id="defenseFactory.plugin.firstPage"
              defaultMessage="First page"
              description="Return to the first page when arriving from a shared cursor link"
            />
          ) : (
            <FormattedMessage
              id="defenseFactory.plugin.previous"
              defaultMessage="Previous"
              description="Previous results page"
            />
          )}
        </Button>
        <Button color="outlineSurface" disabled={!next || busy} onClick={next}>
          <FormattedMessage
            id="defenseFactory.plugin.next"
            defaultMessage="Next"
            description="Next results page"
          />
        </Button>
      </div>
    </footer>
  );
}

export function repositoryLabel(url: string) {
  return url.replace(/^https:\/\/github\.com\//, "").replace(/\.git$/, "");
}
