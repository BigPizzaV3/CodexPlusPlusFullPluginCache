import type { components } from "@oai/aardvark-client/components";
import { useMutation, useQuery } from "@tanstack/react-query";
import { useId, useState } from "react";
import { FormattedMessage, useIntl } from "react-intl";

import { useCloud } from "../app-context";
import { downloadFile, securityClient } from "../client";
import type { DefenseFactoryFile } from "../contract";
import { Report } from "../ui";
import { WorkbenchButton as Button } from "./controls";
import { WorkbenchState } from "./layout";
import { workbenchStyles } from "./styles";

const MAX_INLINE_ARTIFACT_BYTES = 1_048_576;
const WORKFLOW_RUN_ID_PATTERN = /^wfr_[0-9a-f]{64}$/;
const WORKFLOW_OUTPUT_ID_PATTERN = /^wfo_[0-9a-f]{64}$/;

type WorkflowArtifact = components["schemas"]["WorkflowArtifactRef"];

const CODE_FORMATS: ReadonlyArray<{
  language: string;
  extensions: readonly string[];
  mediaTypes: readonly string[];
}> = [
  {
    language: "javascript",
    extensions: ["js", "mjs", "cjs"],
    mediaTypes: ["text/javascript", "application/javascript"],
  },
  { language: "jsx", extensions: ["jsx"], mediaTypes: ["text/jsx"] },
  {
    language: "typescript",
    extensions: ["ts", "mts", "cts"],
    mediaTypes: ["text/typescript", "application/typescript"],
  },
  { language: "tsx", extensions: ["tsx"], mediaTypes: ["text/tsx"] },
  {
    language: "python",
    extensions: ["py", "pyi", "pyw"],
    mediaTypes: ["text/x-python", "application/x-python-code"],
  },
  {
    language: "json",
    extensions: ["json"],
    mediaTypes: ["application/json", "text/json"],
  },
  {
    language: "bash",
    extensions: ["sh", "bash", "zsh"],
    mediaTypes: ["application/x-sh", "text/x-shellscript", "text/x-sh"],
  },
  {
    language: "markup",
    extensions: ["html", "htm", "xml", "xhtml", "svg"],
    mediaTypes: ["text/html", "text/xml", "application/xml"],
  },
  { language: "css", extensions: ["css"], mediaTypes: ["text/css"] },
  {
    language: "sql",
    extensions: ["sql"],
    mediaTypes: ["application/sql", "text/sql", "text/x-sql"],
  },
  {
    language: "markdown",
    extensions: ["md", "markdown", "mdown"],
    mediaTypes: ["text/markdown", "text/x-markdown"],
  },
  {
    language: "yaml",
    extensions: ["yaml", "yml"],
    mediaTypes: ["application/yaml", "text/yaml", "text/x-yaml"],
  },
  { language: "go", extensions: ["go"], mediaTypes: ["text/x-go"] },
  {
    language: "diff",
    extensions: ["diff", "patch"],
    mediaTypes: ["text/x-diff", "text/x-patch"],
  },
  {
    language: "toml",
    extensions: ["toml"],
    mediaTypes: ["application/toml", "text/toml"],
  },
];

function normalizedMediaType(value: string): string {
  return value.split(";", 1)[0]?.trim().toLowerCase() ?? "";
}

function previewFormat(artifact: WorkflowArtifact): {
  language: string;
  isText: boolean;
} {
  const mediaType = normalizedMediaType(artifact.media_type);
  const extension =
    artifact.filename
      ?.split(/[\\/]/)
      .at(-1)
      ?.split(".")
      .at(-1)
      ?.toLowerCase() ?? "";
  const filenameLanguage = CODE_FORMATS.find(({ extensions }) =>
    extensions.includes(extension),
  )?.language;
  const mediaTypeLanguage = CODE_FORMATS.find(({ mediaTypes }) =>
    mediaTypes.includes(mediaType),
  )?.language;
  return {
    language: filenameLanguage ?? mediaTypeLanguage ?? "text",
    isText: mediaType.startsWith("text/") || mediaTypeLanguage != null,
  };
}

function canPreviewInline(artifact: WorkflowArtifact): boolean {
  return (
    previewFormat(artifact).isText &&
    Number.isSafeInteger(artifact.size_bytes) &&
    artifact.size_bytes >= 0 &&
    artifact.size_bytes <= MAX_INLINE_ARTIFACT_BYTES
  );
}

function safeDownloadFilename(artifact: WorkflowArtifact): string {
  const filename = artifact.filename;
  return filename && /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(filename)
    ? filename
    : "security-scan-artifact";
}

function decodeInlineArtifact(
  artifact: WorkflowArtifact,
  file: DefenseFactoryFile & { base64: string },
): string {
  const responseMediaType = normalizedMediaType(file.contentType);
  if (
    responseMediaType &&
    responseMediaType !== normalizedMediaType(artifact.media_type)
  ) {
    throw new Error("Artifact type does not match");
  }
  const bytes = Uint8Array.from(atob(file.base64), (character) =>
    character.charCodeAt(0),
  );
  if (bytes.byteLength > MAX_INLINE_ARTIFACT_BYTES) {
    throw new Error("Artifact is too large");
  }
  const content = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  return previewFormat(artifact).language === "json"
    ? JSON.stringify(JSON.parse(content), null, 2)
    : content;
}

export function ScanWorkflowOutput({
  runId,
  outputId,
}: {
  runId: string;
  outputId: string;
}) {
  const cloud = useCloud();
  const intl = useIntl();
  const previewId = useId();
  const identifiersAreValid =
    WORKFLOW_RUN_ID_PATTERN.test(runId) &&
    WORKFLOW_OUTPUT_ID_PATTERN.test(outputId);
  const { data, error, isPending, isFetching, isFetchedAfterMount, refetch } =
    useQuery({
      queryKey: [
        "scan-output",
        cloud.accountId,
        cloud.identity?.userId,
        runId,
        outputId,
      ],
      queryFn: () =>
        securityClient.request({
          operation: "workflow_output",
          parameters: { path: { run_id: runId, output_id: outputId } },
        }),
      enabled: identifiersAreValid,
      staleTime: 15_000,
      refetchOnMount: "always",
    });
  const outputMatchesRun =
    data?.workflow_run_id === runId && data.output_id === outputId;
  const artifacts = !error && outputMatchesRun ? data.value.artifacts : [];
  const [selectedArtifactId, setSelectedArtifactId] = useState<string | null>(
    null,
  );
  const artifact =
    artifacts.find(
      (candidate) => candidate.artifact_id === selectedArtifactId,
    ) ?? artifacts[0];

  if (!identifiersAreValid || error || (data && !outputMatchesRun)) {
    return (
      <OutputUnavailable
        loading={isFetching}
        onRetry={identifiersAreValid ? () => void refetch() : undefined}
      />
    );
  }
  if (isPending || (isFetching && !isFetchedAfterMount) || !data) {
    return (
      <WorkbenchState loading>
        <FormattedMessage
          id="codexSecurity.workbench.scans.detail.artifacts.loading"
          defaultMessage="Loading scan artifacts…"
          description="Loading status while a scan's artifact list is retrieved."
        />
      </WorkbenchState>
    );
  }
  if (!artifact) {
    return (
      <WorkbenchState>
        <FormattedMessage
          id="codexSecurity.workbench.scans.detail.artifacts.empty"
          defaultMessage="No artifacts are available for this run."
          description="Empty state when a completed scan output contains no artifacts."
        />
      </WorkbenchState>
    );
  }

  return (
    <div
      className={[workbenchStyles.card, workbenchStyles.outputsGrid].join(" ")}
    >
      <nav
        aria-label={intl.formatMessage({
          id: "codexSecurity.workbench.scans.detail.artifacts.label",
          defaultMessage: "Scan artifacts",
          description:
            "Accessible name for the artifact list beside a scan artifact preview.",
        })}
        className={workbenchStyles.outputsSidebar}
      >
        <ul className="space-y-1">
          {artifacts.map((candidate) => (
            <li key={candidate.artifact_id}>
              <button
                type="button"
                aria-pressed={candidate.artifact_id === artifact.artifact_id}
                aria-controls={previewId}
                title={candidate.filename ?? candidate.artifact_id}
                onClick={() => setSelectedArtifactId(candidate.artifact_id)}
                className={[
                  "w-full rounded-lg px-3 py-2 text-start text-[14px] leading-5 font-normal break-words focus-visible:outline focus-visible:outline-2 focus-visible:-outline-offset-2",
                  candidate.artifact_id === artifact.artifact_id
                    ? "bg-token-bg-secondary-surface text-token-text-primary"
                    : "text-token-text-secondary hover:bg-token-bg-secondary-surface",
                ].join(" ")}
              >
                {candidate.filename ?? candidate.artifact_id}
              </button>
            </li>
          ))}
        </ul>
      </nav>
      <ArtifactPreview
        key={artifact.artifact_id}
        id={previewId}
        runId={runId}
        outputId={outputId}
        artifact={artifact}
      />
    </div>
  );
}

function ArtifactPreview({
  id,
  runId,
  outputId,
  artifact,
}: {
  id: string;
  runId: string;
  outputId: string;
  artifact: WorkflowArtifact;
}) {
  const cloud = useCloud();
  const inline = canPreviewInline(artifact);
  const format = previewFormat(artifact);
  const load = () =>
    securityClient.request({
      operation: "workflow_artifact",
      parameters: {
        path: {
          run_id: runId,
          output_id: outputId,
          artifact_id: artifact.artifact_id,
        },
      },
    });
  const { data, error, isPending, isFetching, isFetchedAfterMount, refetch } =
    useQuery({
      queryKey: [
        "scan-artifact",
        cloud.accountId,
        cloud.identity?.userId,
        runId,
        outputId,
        artifact.artifact_id,
      ],
      queryFn: async () => {
        const file = await load();
        return {
          file,
          content: "base64" in file ? decodeInlineArtifact(artifact, file) : null,
        };
      },
      enabled: inline,
      staleTime: Infinity,
      refetchOnMount: "always",
    });
  const download = useMutation({
    mutationFn: async () => {
      // Download grants expire, so fetch a fresh URL for every download.
      const file = data?.file && "base64" in data.file ? data.file : await load();
      await downloadFile({
        ...file,
        fileName: safeDownloadFilename(artifact),
      });
    },
  });
  const unavailable = error || download.error;

  return (
    <section
      id={id}
      aria-label={artifact.filename ?? artifact.artifact_id}
      className={workbenchStyles.outputsPreview}
    >
      <div className="mb-5 flex min-w-0 flex-wrap items-center justify-between gap-3">
        <span className="text-token-text-primary min-w-0 truncate text-[14px] leading-5 font-medium">
          {artifact.filename ?? artifact.artifact_id}
        </span>
        <Button
          color="outlineSurface"
          loading={download.isPending}
          disabled={download.isPending}
          onClick={() => download.mutate()}
        >
          <FormattedMessage
            id="codexSecurity.workbench.scans.detail.artifact.download"
            defaultMessage="Download artifact"
            description="Downloads the selected authorized scan artifact."
          />
        </Button>
      </div>
      {unavailable ? (
        <WorkbenchState
          action={
            <Button
              color="outlineSurface"
              loading={isFetching || download.isPending}
              onClick={() => {
                if (download.error) download.mutate();
                else void refetch();
              }}
            >
              <FormattedMessage
                id="codexSecurity.workbench.scans.detail.output.retry"
                defaultMessage="Retry"
                description="Retries loading or downloading the selected scan artifact."
              />
            </Button>
          }
        >
          <FormattedMessage
            id="codexSecurity.workbench.scans.detail.artifact.unavailable"
            defaultMessage="This artifact is unavailable."
            description="Sanitized error when an authorized artifact cannot be retrieved or previewed."
          />
        </WorkbenchState>
      ) : !inline || (data && data.content === null) ? (
        <WorkbenchState>
          <FormattedMessage
            id="codexSecurity.workbench.scans.detail.artifact.noPreview"
            defaultMessage="This file cannot be previewed. Download it to view its contents."
            description="Explanation for an artifact whose format or size prevents inline preview."
          />
        </WorkbenchState>
      ) : isPending || (isFetching && !isFetchedAfterMount) || !data ? (
        <WorkbenchState loading>
          <FormattedMessage
            id="codexSecurity.workbench.scans.detail.artifact.loading"
            defaultMessage="Loading artifact…"
            description="Loading status for the selected scan artifact preview."
          />
        </WorkbenchState>
      ) : format.language === "markdown" && data.content !== null ? (
        <Report>{data.content}</Report>
      ) : (
        <pre
          data-language={format.language}
          className="bg-token-bg-secondary-surface text-token-text-primary max-h-[36rem] overflow-auto rounded-lg p-4 font-mono text-[12px] leading-5 whitespace-pre"
        >
          <code>{data.content}</code>
        </pre>
      )}
    </section>
  );
}

function OutputUnavailable({
  loading,
  onRetry,
}: {
  loading: boolean;
  onRetry?: () => void;
}) {
  return (
    <WorkbenchState
      action={
        onRetry ? (
          <Button color="outlineSurface" loading={loading} onClick={onRetry}>
            <FormattedMessage
              id="codexSecurity.workbench.scans.detail.output.retry"
              defaultMessage="Retry"
              description="Retries fetching the authorized scan artifact list."
            />
          </Button>
        ) : undefined
      }
    >
      <FormattedMessage
        id="codexSecurity.workbench.scans.detail.artifacts.unavailable"
        defaultMessage="The scan artifacts are unavailable."
        description="Sanitized error when an authorized scan artifact list cannot be retrieved."
      />
    </WorkbenchState>
  );
}
