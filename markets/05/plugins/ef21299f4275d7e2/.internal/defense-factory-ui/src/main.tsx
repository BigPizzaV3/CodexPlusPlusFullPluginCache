import "./styles.css";

import { DesignSystemProvider } from "@oai/ds/ui/design-system-provider";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { createRoot } from "react-dom/client";
import { IntlProvider } from "react-intl";

import { App } from "./app";
import { ExternalLink } from "./link";

const root = document.getElementById("root");
if (!root) throw new Error("Security UI root is missing");
const queries = new QueryClient({
  defaultOptions: { queries: { retry: 1, staleTime: 15_000 } },
});
createRoot(root).render(
  <IntlProvider locale="en" defaultLocale="en">
    <DesignSystemProvider
      radixPortalContainer={document.body}
      linkComponent={ExternalLink}
    >
      <QueryClientProvider client={queries}>
        <App />
      </QueryClientProvider>
    </DesignSystemProvider>
  </IntlProvider>,
);
