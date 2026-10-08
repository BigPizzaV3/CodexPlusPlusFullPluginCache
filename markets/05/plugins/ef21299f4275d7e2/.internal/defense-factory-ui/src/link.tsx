import type { ComponentProps } from "react";
import { useState } from "react";
import {
  createPath,
  Link as RouterLink,
  useLinkClickHandler,
  useResolvedPath,
} from "react-router";
import { useCloud } from "./app-context";
import { openLink } from "./client";

export function AppLink({
  to,
  onClick,
  ...props
}: ComponentProps<typeof RouterLink>) {
  const { hostAppUrl } = useCloud();
  const path = useResolvedPath(to, { relative: props.relative });
  const handleClick = useLinkClickHandler(to, props);
  const url = hostAppUrl ? new URL(hostAppUrl) : undefined;
  // Native new-tab and copy-link actions bypass onClick and must leave the sandbox.
  if (url) url.hash = createPath(path);
  return (
    <RouterLink
      {...props}
      to={url?.href ?? to}
      onClick={(event) => {
        onClick?.(event);
        if (!event.defaultPrevented && !props.reloadDocument) handleClick(event);
      }}
    />
  );
}

/** Keep report links outside the sandbox and on the host's normal link-opening path. */
export function ExternalLink({
  href,
  children,
  onClick,
  ...props
}: ComponentProps<"a">) {
  const [error, setError] = useState<string | null>(null);
  return (
    <>
      <a
        {...props}
        href={href}
        onClick={(event) => {
          onClick?.(event);
          // Leave native new-tab, download, and document-fragment actions intact.
          if (
            event.defaultPrevented ||
            !href ||
            event.button !== 0 ||
            event.metaKey ||
            event.ctrlKey ||
            event.shiftKey ||
            event.altKey ||
            props.download != null ||
            !/^[a-z][a-z\d+.-]*:/i.test(href)
          )
            return;
          event.preventDefault();
          void openLink(href).catch((error: Error) => setError(error.message));
        }}
      >
        {children}
      </a>
      {error && (
        <span role="alert" className="text-sm text-secondary">
          {error}
        </span>
      )}
    </>
  );
}
