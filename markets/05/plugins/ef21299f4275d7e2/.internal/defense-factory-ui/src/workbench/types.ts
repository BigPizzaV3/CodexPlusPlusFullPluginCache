import type { DefenseFactoryResponse } from "../contract";
export type Finding = DefenseFactoryResponse<"findings_list">["items"][number];
export type FindingStatus = Finding["status"];
export type FindingCriticality = NonNullable<Finding["criticality"]>;
