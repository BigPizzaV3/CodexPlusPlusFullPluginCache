---
name: coleworld-ml-to-rl-design
description: Design bounded experiments connecting machine-learning models to reinforcement-learning workflows. Use to assess ML-to-RL migration claims, define states/actions/rewards, compare supervised learning and contextual bandits with sequential RL, plan offline evaluation, and check framework compatibility without launching training or live exploration.
---
# ColeWorld ML-to-RL Experiment Design

Explain that reinforcement learning is a branch of machine learning, not a universal model file format. A classifier, embedding model, or language model cannot simply be renamed into an RL agent. Specify what can actually be reused: authorized data, features, compatible weights, an encoder, a reward estimator, or a behavior policy. Separate format conversion from training and deployment.

## Connected assessment tools

For requests to create, save, list, read, update observations, export or delete an
assessment, read [workspace-tools.md](references/workspace-tools.md) first and use
the connected workspace tools. Follow its exact required fields, methodology and
status mappings, provenance, retry rules and confirmation requirements. Verify
saved state before reporting success. If tools are unavailable, label the result
unsaved and state the blocker.

## Choose the simplest justified approach

Gather the decision to improve, existing model and framework/version, observation schema, action space, available feedback, intervention risks, and compute constraints. Read current primary sources in references/sources.md before algorithm-specific recommendations.

Compare:
- Rules or supervised learning when labeled predictions or known targets solve the problem.
- A contextual bandit when choosing among actions with feedback for the selected action and no material multi-step state consequences in the proposed model.
- Sequential RL when actions influence later states and delayed cumulative outcomes matter.

Do not force RL onto an ordinary prediction task. If data or a valid environment is absent, recommend a baseline and instrumentation design rather than fabricate a trainable experiment.

## Write the experiment contract

Specify:
1. Task and user-benefit objective; a measurable baseline and minimum improvement worth pursuing.
2. Observation/state fields, missing-data handling, permitted actions, prohibited actions, transition assumptions, horizon, and termination versus time-limit truncation.
3. Reward definition and timing, units/range, cost penalties, missing/delayed feedback treatment, and independent safety constraints.
4. Offline dataset provenance, license/consent, collection policy, train/validation/test split, leakage risks, and retention/deletion plan. Do not assume plugin use grants training rights or permission to reuse private voice/shared memory.
5. Simulator or evaluation environment, its fidelity limits, and how it differs from production.
6. Candidate algorithm, framework/version, observation/action compatibility, and what existing model components can be reused. Verify checkpoint architecture and preprocessing compatibility; never promise universal import or equivalent behavior after conversion.

Use synthetic or explicitly authorized de-identified data for examples. Never export raw secrets or private user records as evaluation artifacts.

## Make reward failures visible

List ways the agent could game the reward or harm users while improving the metric: repeated actions, fabricated success, unsafe shortcuts, excessive cost, manipulation, or concentration on easy cases. Add counter-metrics, adversarial cases, action limits, and independent human review. For commerce, do not optimize spending or conversion without consent, fairness, refund/complaint, and user-benefit constraints. Never use this skill to automate high-impact eligibility decisions.

Treat a learned reward score as a proxy, not proof of correctness. Keep held-out tests and independent checks outside the training reward. Do not claim models learn automatically from ordinary plugin usage.

## Plan evaluation before training

Compare against a frozen baseline on held-out data and a documented simulator where appropriate. Specify seeds, sample sizes, uncertainty intervals, subgroup checks when appropriate, latency, cost, safety violations, and robustness to drift.

For logged-policy/off-policy evaluation, inspect action probabilities, support/coverage, confounding and selection bias. Do not invent missing propensities or claim unbiased policy value from observational logs without justified assumptions. Explain estimator limits and simulator-to-real gaps. Offline improvement alone does not establish safe live performance.

Separate evaluation results from intended tests using observed, inferred, proposed, and not run labels. Record dataset/model hashes or versions, configuration, environment, and reproducibility limits.

## Bound cost and deployment

Estimate a range from planned runs × runtime × verified compute rate, plus inference, evaluation, storage, and transfer. State assumptions and pricing date; if runtime is unknown, propose a small authorized benchmark rather than an exact bill. Include retries and algorithm rollout overshoot. A timestep target is not necessarily a hard spend cap.

Do not launch jobs, collect live feedback, enable exploration, modify credentials, spend money, or deploy merely because this skill is invoked. Present an approval-ready plan with total budget, stop rules, monitoring, isolated data, and owner.

Require staged gates: reproducible baseline → offline/simulation evidence → independent review → explicitly authorized bounded trial → monitored release. Define rollback model/configuration, automatic stop triggers, and who can revoke the trial. Preserve working plugin behavior and personal memory boundaries.

## Deliver

Return a one-page experiment brief: recommendation and alternatives; reuse-versus-rebuild map; experiment contract; evaluation and reward-risk checklist; estimated cost range; unresolved assumptions; and the exact next approval or missing input. Say plainly when no training or deployment occurred.

## Attribution

Prepared for Sophia Cole / ColeWorld™ with AI assistance. © 2026 Sophia Cole. These notices do not claim trademark or copyright registration, platform endorsement, or third-party ownership.
