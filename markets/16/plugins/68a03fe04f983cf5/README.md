# Robotics Lab 0.1.1

Private connector package source for RQM Technologies LLC. ChatGPT, Claude and Cursor are the intended front ends. The company's standalone Robotics Lab web application is not required for the new product; the existing RQM account sign-in, funding and human confirmation pages remain part of the account infrastructure.

The package points to `https://jobs.rqmtechnologies.com/mcp/plugins/robotics-lab`. The dedicated server exposes one NVIDIA cuRobo v0.8 Franka Panda capability and its complete lifecycle. It contains no Quantum operations, legacy Robotics portfolio, funding tools or subscription tools. It uses the current approved Robotics gimbal.

RQM Account Core gives this audience a separate delegated principal and maps it to the existing `robotics` financial product and prepaid wallet. Existing products and audiences remain supported. No AWS resources are part of this product plan.

## Build and status

CI runs `node scripts/build-robotics-lab-package.mjs` and uploads the deterministic ZIP and checksum as a workflow artifact. The archive has root `plugin.json` and `mcp.json`, one skill, legal notices and artwork. OAuth discovery follows the company's actual RQM package template; no secrets, client IDs or app registration identifiers are copied.

This is source preparation for a private test. The remote endpoint still requires deployment, real GPU/runtime qualification and actual account configuration before a working hosted execution can be claimed. The review cases in the manifest are draft cases, not completed test evidence. The package deliberately contains no invented demo recording or reviewer credentials. Private registration, review submission and public publication are separate actions; none is performed by the build.

## Supported journey

Inspect capability → collect actual scene → quote → open the exact account approval page → human confirms → submit once → poll/cancel/recover the original job → retrieve trajectory, GPU/runtime evidence and authoritative Core receipt. The skill contains the precise uncertainty and spending rules.

The software validates modeled sphere geometry independently. It does not actuate robots or certify physical safety. The initial engine is pinned to cuRobo v0.8.0 commit `4ea77366ca48ee453e7df139e39fa6532af49f3b`.

See [TEMPLATE-COMPARISON.md](TEMPLATE-COMPARISON.md) for template provenance and product separation.
