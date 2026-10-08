import { Textarea } from "@oai/ds/ui/textarea";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";
import { FormattedMessage } from "react-intl";

import { useCloud } from "./app-context";
import { openTask, securityClient } from "./client";
import { RequestState, Section } from "./ui";
import { WorkbenchButton as Button, WorkbenchLink } from "./workbench/controls";

export function FindingChat({
  id,
  existingTaskId,
}: {
  id: string;
  existingTaskId?: string | null;
}) {
  const { webOrigin } = useCloud();
  const cache = useQueryClient();
  const [expanded, setExpanded] = useState(false);
  const [text, setText] = useState("");
  const [createdTaskId, setCreatedTaskId] = useState<string>();
  const {
    mutate: start,
    data,
    error,
    isPending,
  } = useMutation({
    mutationFn: async () => {
      const result = await securityClient.request({
        operation: "findings_chat",
        parameters: { path: { id } },
        requestBody: { text, createdTaskId },
      });
      // Remember the created task before navigation or linking can fail. Retrying must not create another task.
      setCreatedTaskId(result.taskId);
      if (result.linked) {
        await cache.invalidateQueries({ queryKey: ["finding"] });
        await openTask(result.taskId, webOrigin);
      }
      return result;
    },
  });
  const chatLabel = (
    <FormattedMessage
      id="defenseFactory.plugin.chat"
      defaultMessage="Chat"
      description="Discuss this finding in a Codex Cloud task"
    />
  );
  return (
    <div className="flex flex-col gap-3">
      <div>
        {existingTaskId ? (
          <WorkbenchLink
            color="outlineSurface"
            href={
              new URL(`/remote/${encodeURIComponent(existingTaskId)}`, webOrigin)
                .href
            }
          >
            {chatLabel}
          </WorkbenchLink>
        ) : (
          <Button
            color="outlineSurface"
            loading={isPending}
            onClick={() => setExpanded(!expanded)}
          >
            {chatLabel}
          </Button>
        )}
      </div>
      {expanded && !existingTaskId && (
        <Section
          title={
            <FormattedMessage
              id="defenseFactory.plugin.discussFinding"
              defaultMessage="Discuss this finding"
              description="Start a Cloud task with the finding context"
            />
          }
        >
          <form
            className="flex flex-col gap-3"
            onSubmit={(event) => {
              event.preventDefault();
              start();
            }}
          >
            <label className="flex flex-col gap-2 text-[14px]">
              <FormattedMessage
                id="defenseFactory.plugin.chatPrompt"
                defaultMessage="What would you like to investigate?"
                description="Prompt for a new finding follow-up task"
              />
              <Textarea
                value={text}
                onChange={(event) => setText(event.target.value)}
                disabled={!!createdTaskId}
                required
              />
            </label>
            <div>
              <Button
                type="submit"
                color="primary"
                loading={isPending}
                disabled={!text.trim()}
              >
                {createdTaskId ? (
                  <FormattedMessage
                    id="defenseFactory.plugin.retryLink"
                    defaultMessage="Retry linking chat"
                    description="Retry saving an already created Cloud task on the finding"
                  />
                ) : (
                  <FormattedMessage
                    id="defenseFactory.plugin.startChat"
                    defaultMessage="Start chat"
                    description="Create and open a Cloud task about this finding"
                  />
                )}
              </Button>
            </div>
          </form>
        </Section>
      )}
      {data && !data.linked && (
        <div role="alert" className="flex flex-col items-start gap-3 text-sm">
          <p>
            <FormattedMessage
              id="defenseFactory.plugin.chatLinkFailed"
              defaultMessage="Your chat was created, but its link could not be saved to this finding. Retry linking it or open the chat."
              description="Task creation succeeded but linking it to a finding failed"
            />
          </p>
          <WorkbenchLink
            color="outlineSurface"
            href={
              new URL(`/remote/${encodeURIComponent(data.taskId)}`, webOrigin).href
            }
          >
            <FormattedMessage
              id="defenseFactory.plugin.openChat"
              defaultMessage="Open chat"
              description="Open the existing Cloud task for this finding"
            />
          </WorkbenchLink>
        </div>
      )}
      {error && <RequestState error={error} />}
    </div>
  );
}
