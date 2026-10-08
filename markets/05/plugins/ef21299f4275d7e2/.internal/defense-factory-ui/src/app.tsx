import { useQuery } from "@tanstack/react-query";
import { useEffect, useRef, useState } from "react";
import { FormattedMessage, IntlProvider } from "react-intl";
import {
  MemoryRouter,
  Navigate,
  Route,
  Routes,
  useLocation,
  useNavigate,
  useNavigationType,
} from "react-router";

import { CloudContext, useCloud } from "./app-context";
import {
  connectClient,
  navigate as navigateHost,
  subscribeToHostContext,
} from "./client";
import { Findings } from "./findings";
import { Overview } from "./overview";
import { Repositories } from "./repositories";
import { Scans } from "./scans";
import { ArchivedFindings, ScanConfiguration } from "./route-aliases";
import { RequestState } from "./ui";
import { WorkbenchButton as Button, WorkbenchLink } from "./workbench/controls";
import { WorkbenchNavigation } from "./workbench/navigation";

const ROOT = "/codex/cloud/security";

export function App() {
  const {
    data: cloud,
    error,
    isPending,
    refetch,
  } = useQuery({
    queryKey: ["bootstrap"],
    queryFn: connectClient,
    staleTime: 15_000,
  });
  if (isPending || error)
    return <RequestState error={error} retry={() => void refetch()} />;
  if (cloud.access !== "allowed" || !cloud.identity?.workflowsEnabled)
    return (
      <div className="flex min-h-full flex-col items-center justify-center gap-4 p-8">
        <h1 className="heading-lg">
          <FormattedMessage
            id="defenseFactory.plugin.unavailable"
            defaultMessage="Codex Security Cloud is not available in this workspace"
            description="The current workspace cannot access Security workflows"
          />
        </h1>
        {cloud.requiresCodexCloud && (
          <p className="text-secondary">
            <FormattedMessage
              id="defenseFactory.plugin.cloudRequired"
              defaultMessage="Your workspace administrator needs to enable Codex Cloud"
              description="The workspace has not enabled the required Cloud access"
            />
          </p>
        )}
        <Button color="outlineSurface" onClick={() => void refetch()}>
          <FormattedMessage
            id="defenseFactory.plugin.retry"
            defaultMessage="Try again"
            description="Retry loading Security access"
          />
        </Button>
      </div>
    );
  const initial = pluginPath(cloud.initialPath);
  return (
    <IntlProvider locale={cloud.locale} defaultLocale="en">
      <CloudContext.Provider value={cloud}>
        <MemoryRouter key={cloud.accountId} initialEntries={[initial]}>
          {cloud.githubConnected === false ? (
            <GithubConnectionSetup retry={() => void refetch()} />
          ) : (
            <Workbench />
          )}
        </MemoryRouter>
      </CloudContext.Provider>
    </IntlProvider>
  );
}

function GithubConnectionSetup({ retry }: { retry: () => void }) {
  const cloud = useCloud();
  return (
    <div className="flex min-h-full flex-col items-center justify-center gap-4 p-8">
      <h1 className="heading-lg text-center">
        <FormattedMessage
          id="defenseFactory.plugin.githubSetupTitle"
          defaultMessage="Connect GitHub to get started"
          description="Setup required before loading Codex Security Cloud repository data"
        />
      </h1>
      <p className="max-w-lg text-center text-secondary">
        <FormattedMessage
          id="defenseFactory.plugin.githubSetupDescription"
          defaultMessage="GitHub isn't connected in this workspace. Connect it to load findings, repositories, and scans. A connection in another workspace won't apply here."
          description="Explain why Codex Security Cloud cannot load repository data"
        />
      </p>
      <div className="flex flex-wrap justify-center gap-2">
        <WorkbenchLink
          href={
            new URL(
              "/codex/cloud/settings/connectors#settings/Connectors",
              cloud.webOrigin,
            ).href
          }
        >
          <FormattedMessage
            id="defenseFactory.plugin.openConnectionSettings"
            defaultMessage="Open connection settings"
            description="Open the workspace's GitHub connection settings"
          />
        </WorkbenchLink>
        <Button color="outlineSurface" onClick={retry}>
          <FormattedMessage
            id="defenseFactory.plugin.checkConnection"
            defaultMessage="I've connected GitHub"
            description="Check GitHub setup again after returning from settings"
          />
        </Button>
      </div>
    </div>
  );
}

function Workbench() {
  const cloud = useCloud();
  const location = useLocation();
  const navigate = useNavigate();
  const navigationType = useNavigationType();
  const [navigationError, setNavigationError] = useState<Error | null>(null);
  const syncedPath = useRef(`${location.pathname}${location.search}`);
  useEffect(
    () =>
      subscribeToHostContext((context) => {
        const deepLink = context?.["openai/deepLink"];
        if (
          !deepLink ||
          typeof deepLink !== "object" ||
          !("url" in deepLink) ||
          typeof deepLink.url !== "string"
        )
          return;
        const path = pluginPath(deepLink.url);
        if (path !== syncedPath.current) {
          syncedPath.current = path;
          void navigate(path, { replace: true });
        }
      }),
    [navigate],
  );
  useEffect(() => {
    const path = `${location.pathname}${location.search}`;
    if (path === syncedPath.current) return;
    syncedPath.current = path;
    // Host activations already own their history entry; local route redirects
    // should not add a second entry through the self-deep-link protocol.
    if (navigationType === "REPLACE") return;
    void navigateHost(path)
      .then(() => setNavigationError(null))
      .catch((error: Error) => setNavigationError(error));
  }, [location.pathname, location.search, navigationType]);
  return (
    <div className="flex min-h-full flex-col bg-surface text-default">
      <main className="df-workbench-shell">
        <WorkbenchNavigation />
        {navigationError && <RequestState error={navigationError} />}
        <Routes>
          <Route
            path="/overview"
            element={
              cloud.overviewEnabled ? (
                <Overview />
              ) : (
                <Navigate replace to="/findings" />
              )
            }
          />
          <Route path="/findings/:id?" element={<Findings />} />
          <Route path="/repositories" element={<Repositories />} />
          <Route path="/repositories/:id" element={<Repositories />} />
          <Route path="/scans" element={<Scans />} />
          <Route path="/scans/new" element={<Scans />} />
          <Route path="/runs/:id" element={<Scans />} />
          <Route path="/scans/:id" element={<ScanConfiguration />} />
          <Route
            path="/repositories/:repositoryId/:section/:id?"
            element={<Repositories />}
          />
          <Route path="/archives" element={<ArchivedFindings />} />
          <Route path="*" element={<Navigate replace to="/overview" />} />
        </Routes>
      </main>
    </div>
  );
}

function pluginPath(path: string) {
  return path.startsWith(ROOT)
    ? path.slice(ROOT.length) || "/overview"
    : path.startsWith("/")
      ? path
      : "/overview";
}
