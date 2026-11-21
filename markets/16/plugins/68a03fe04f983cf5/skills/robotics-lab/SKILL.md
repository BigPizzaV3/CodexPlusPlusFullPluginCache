---
name: robotics-lab
description: Quote, confirm, submit and recover one bounded NVIDIA cuRobo v0.8 Franka Panda motion-planning request using the connected RQM account.
---

Use this connector for the supported seven-joint Panda planner. It provides modeled trajectories and evidence; it does not control a robot or certify physical safety.

1. Read `get_robotics_lab_capability` when the scope is unclear. Collect the user's actual seven starting joint angles in radians, target position in metres, normalized quaternion in wxyz order and any cuboid obstacles in the base frame. Maximum 32 cuboids. Use the curated robot profile default. Do not invent the robot state or scene.
2. Use only the user's selected Robotics Lab connection. If selection is ambiguous, ask before private reads. `get_account_balance` reads the existing RQM wallet; balance is not permission to spend. Funding, subscriptions and owner policy changes occur outside this connector.
3. Call `quote_cloud_motion` for the complete request. Present the exact maximum USD and expiry. Discovery and quotes are not GPU evidence. Preserve the exact request, quote and one stable idempotency key throughout consent, submission and recovery.
4. Call `get_cloud_motion_approval` and give the human the returned RQM account review link. The human signs in and approves the exact request and maximum price there. Chat messages and model flags do not create consent. Do not expose or ask the human to copy a consent credential. The server retrieves the stored bound receipt on submission.
5. Submit once with `submit_cloud_motion` using the same request, quote and key after account-page confirmation. Existing funds, saved owner policy and real runtime readiness are required. Report service and pricing errors faithfully; do not fabricate defaults or select another payment rail.
6. On a timeout or uncertain acceptance, use `recover_cloud_reservation` with the original quote/request/key. If a reservation is known, use `resolve_cloud_motion` as directed by the returned state. Missing or unknown state is not proof that the original request cannot commit. Never switch keys or silently submit again to escape uncertainty.
7. Read `get_cloud_motion_status`, `get_cloud_motion_result`, `get_cloud_motion_artifact` and `get_cloud_motion_receipt` for the original job. A wallet hold is not settlement. Only verified runtime/GPU evidence establishes GPU execution. A fixture, tool label, quote or successful transport does not.
8. On the user's cancellation request, call `cancel_cloud_motion` with the original job ID and poll it. Cancellation and release complete only after the service confirms execution termination. Do not start replacement work automatically.

Explain independent CPU validation of the pinned 61-sphere model and time-indexed joint trajectory. Do not claim mesh enclosure, dynamics/torque qualification, real-world collision safety, actuation, NVIDIA endorsement or capabilities beyond this one planner. Reject requests to bypass tenant boundaries or access another account. Preserve all unknown and pending states.
