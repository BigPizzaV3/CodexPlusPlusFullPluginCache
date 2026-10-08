---
name: master-change-guard
description: Compare an approved master document with an iterated version and its stated change request. Use when a user needs to verify that a prompt, production master, SOP, policy, specification, or other baseline document was changed only as intended; identify omissions, weakened rules, out-of-scope edits, version residue, and create evidence-backed repair tickets.
---

# Master Change Guard

Audit a change; do not casually rewrite the master. The approved old version is the baseline. The stated change request defines the permitted change. Everything else must be preserved unless the user explicitly authorizes otherwise.

## Required input

Obtain all three items before giving a final verdict:

1. **Baseline** — the approved, previously working version.
2. **Candidate** — the iterated version under review.
3. **Change request** — what this iteration is allowed and required to change.

If a change request is incomplete or ambiguous, list the ambiguity and return `needs_human_review` with `reason_code: scope_ambiguous`; do not invent permission to change unrelated content.

## Audit workflow

1. Extract the baseline's important assets: purpose, scope, workflow or gates, hard rules, boundaries, output formats, acceptance criteria, reusable cards/templates, version/source identity, and operational examples.
2. Extract the candidate's corresponding assets and map them to the baseline. Compare meaning, not just identical wording.
3. Check the change request separately: each requested change must appear in the correct operating location, have an enforceable rule or acceptance check, and not merely be mentioned in a version note.
4. Identify four kinds of findings:
   - `missing_or_weakened_baseline_asset`
   - `change_request_not_fully_implemented`
   - `out_of_scope_change`
   - `identity_or_release_residue`
5. Keep content correctness separate from document usability. If files are supplied, flag broken rendering, unreadable layout, or unusable navigation as `document_usability_issue`.
6. Do not claim that every baseline detail is preserved unless it was actually mapped or checked. Mark unverified areas clearly.

## Verdict rules

Return one of:

- `pass` — required changes are complete; no material baseline asset is missing or weakened; no unresolved residue or out-of-scope change remains.
- `pass_with_observations` — no release-blocking problem, but limited or non-material observations remain.
- `needs_human_review` — evidence is incomplete, the allowed scope is ambiguous, or a material semantic comparison cannot be made reliably.
- `fail` — a requested change is incomplete, a material baseline asset is missing/weakened, an unauthorized change exists, or release identity is inconsistent.

Do not treat a successful version note, a new appendix, or a broad claim of inheritance as evidence that the required operational rule was integrated.

## Required output

Use this structure in Chinese unless the user requests another language.

```text
# 母版变更验收报告

## 1. 验收结论
- 总结论：pass / pass_with_observations / needs_human_review / fail
- 是否允许成为新基线：允许 / 不允许 / 需人工决定
- 一句话原因：
- 原因码：`scope_ambiguous`（仅在变更范围不完整或含糊时使用；其他情况可省略）

## 2. 本次迭代覆盖
For each requested change:
- 迭代项：
- 应落位置：
- 候选版证据：
- 判断：已完整落地 / 部分落地 / 未落地

## 3. 旧基线资产保留
- 已确认保留：
- 未确认或疑似弱化：
- 不应变更却发生变化：

## 4. 问题单
For each finding:
- 问题编号：
- 类型：
- 严重度：阻断 / 高 / 中 / 低
- 位置：
- 旧基线证据：
- 候选版现状：
- 与本次迭代范围的关系：
- 判断理由：
- 建议修复动作：
- 修复边界（禁止改什么）：

## 5. 未来修复接口
- 可直接交给修复器的定点动作：
- 修复后必须回归的检查：
- 不允许由修复器自行决定的事项：

## 6. 文档可用性（如适用）
- 版本身份 / 源稿身份：
- 阅读与排版：
- 结论：
```

## Safety boundary for future repair

This skill audits and produces repair tickets. It does not silently regenerate the whole candidate. If the user later asks for repair, require the repair action to use only the approved tickets, preserve all unaffected baseline assets, and then run this audit again as an independent recheck.
