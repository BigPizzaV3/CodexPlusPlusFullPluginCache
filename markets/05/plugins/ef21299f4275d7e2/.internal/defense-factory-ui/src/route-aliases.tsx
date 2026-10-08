import { useQuery } from "@tanstack/react-query";
import { Navigate, useParams, useSearchParams } from "react-router";

import { securityClient } from "./client";
import { RequestState } from "./ui";

export function ArchivedFindings() {
  const [search] = useSearchParams();
  const parameters = new URLSearchParams(search);
  parameters.set("status", "fixed,wontfix,duplicate,false_positive");
  parameters.delete("cursor");
  return (
    <Navigate
      replace
      to={{ pathname: "/findings", search: parameters.toString() }}
    />
  );
}

export function ScanConfiguration() {
  const { id } = useParams();
  const [search] = useSearchParams();
  const { data, error, isPending, refetch } = useQuery({
    queryKey: ["monitoring", id],
    queryFn: () =>
      securityClient.request({
        operation: "monitoring_get",
        parameters: { path: { id: id! } },
      }),
    enabled: !id!.startsWith("github-"),
    staleTime: 15_000,
  });
  if (!id!.startsWith("github-") && (isPending || error))
    return <RequestState error={error} retry={() => void refetch()} />;
  const parameters = new URLSearchParams(search);
  parameters.set("repo_id", data?.scan_input.repo_id ?? id!);
  if (data) {
    parameters.set("repo", data.scan_input.repo_url);
    parameters.set("scan_configuration_id", id!);
  }
  return (
    <Navigate
      replace
      to={{ pathname: "/scans", search: parameters.toString() }}
    />
  );
}
