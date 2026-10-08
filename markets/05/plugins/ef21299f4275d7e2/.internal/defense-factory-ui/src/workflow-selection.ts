import type { DefenseFactoryRequest, DefenseFactoryResponse } from "./contract";

export type WorkflowDefinition = DefenseFactoryResponse<"workflow_definition">;
export type WorkflowSelections = Record<
  string,
  { model?: string; effort?: string }
>;
type WorkflowSteps = NonNullable<
  DefenseFactoryRequest<"workflow_launch">["requestBody"]["steps"]
>;

export function workflowOptions(value: string | string[]): string[] {
  return typeof value === "string" ? [value] : value;
}

export function selectedWorkflowOption(
  options: string[],
  selected: string | undefined,
): string | undefined {
  if (options.length === 1) return options[0];
  return selected != null && options.includes(selected) ? selected : undefined;
}

export function retainWorkflowSelections(
  definition: WorkflowDefinition,
  selections: WorkflowSelections,
): WorkflowSelections {
  return Object.fromEntries(
    definition.steps.map((step) => {
      const previous = selections[step.id];
      const models = workflowOptions(step.agent.model);
      const efforts = step.agent.reasoning
        ? workflowOptions(step.agent.reasoning.effort)
        : [];
      return [
        step.id,
        {
          model:
            models.length > 1 && models.includes(previous?.model ?? "")
              ? previous?.model
              : undefined,
          effort:
            efforts.length > 1 && efforts.includes(previous?.effort ?? "")
              ? previous?.effort
              : undefined,
        },
      ];
    }),
  );
}

export function workflowStepConfigs(
  definition: WorkflowDefinition | undefined,
  selections: WorkflowSelections,
): WorkflowSteps | null {
  if (!definition?.steps.length) return null;
  const steps: WorkflowSteps = {};
  for (const step of [...definition.steps].sort((a, b) =>
    a.id.localeCompare(b.id),
  )) {
    const selected = selections[step.id];
    const model = selectedWorkflowOption(
      workflowOptions(step.agent.model),
      selected?.model,
    );
    if (model == null) return null;
    const effort = step.agent.reasoning
      ? selectedWorkflowOption(
          workflowOptions(step.agent.reasoning.effort),
          selected?.effort,
        )
      : undefined;
    if (step.agent.reasoning && effort == null) return null;
    steps[step.id] = {
      agent: { model, ...(effort != null ? { reasoning: { effort } } : {}) },
    };
  }
  return steps;
}
