# Professional discretion policy

Professional discretion is controlled authority, not permission to redesign the product.

Grant it only through a named role contract and task execution contract. State the target, invariants, bounds, evidence, reversibility, checkpoint, reviewer, and stop condition. The lead logs every material Class-2 choice with rationale and observed result.

Discretion must not:

- alter product, brand, governance, architecture, data, security, external interfaces, or scope;
- resolve source conflicts;
- introduce tools, dependencies, services, or irreversible changes without authorization;
- suppress a failure because the specification was followed;
- replace owner approval when the outcome materially changes.

If the role, bounds, evidence, or review path is missing, classify the choice as `OWNER_DECISION_REQUIRED` or a documentation gap rather than guessing.
