const assignmentIdPattern = /^a[1-9][0-9]*$/;
const decisionIdPattern = /^tx_([a-f0-9]{24})$/;
const rolePattern = /^[a-z0-9_]+$/;
const taskNamePattern = /^tx_(a[1-9][0-9]*)_([a-f0-9]{24})_([a-z0-9_]+)$/;
const maxTaskNameLength = 64;

function requireAssignment(assignment) {
  if (assignment === null || typeof assignment !== "object") {
    throw new TypeError("assignment must be an object");
  }
  if (!assignmentIdPattern.test(assignment.assignmentId)) {
    throw new RangeError("assignment assignmentId is invalid");
  }
  if (typeof assignment.role !== "string" || !rolePattern.test(assignment.role)) {
    throw new RangeError("assignment role is invalid");
  }
}

function decisionDigest(decisionId) {
  if (typeof decisionId !== "string") {
    throw new TypeError("decisionId must be a string");
  }
  const match = decisionId.match(decisionIdPattern);
  if (match === null) {
    throw new RangeError("decisionId is invalid for assignment token");
  }
  return match[1];
}

export function assignmentTaskName(assignment, decisionId) {
  requireAssignment(assignment);
  const taskName =
    `tx_${assignment.assignmentId}_${decisionDigest(decisionId)}_` +
    assignment.role;
  if (taskName.length > maxTaskNameLength) {
    throw new RangeError("assignment task_name exceeds the supported length");
  }
  return taskName;
}

export function assignmentTaskNameInfo(taskName) {
  if (typeof taskName !== "string" || taskName.length > maxTaskNameLength) {
    return null;
  }
  const match = taskName.match(taskNamePattern);
  return match === null
    ? null
    : { assignmentId: match[1], decisionDigest: match[2], role: match[3] };
}

export function assignmentTaskNameMatchesDecision(
  taskName,
  assignmentId,
  decisionId,
  role,
) {
  const info = assignmentTaskNameInfo(taskName);
  return info !== null &&
    info.assignmentId === assignmentId &&
    info.decisionDigest === decisionDigest(decisionId) &&
    info.role === role;
}

export function assignmentTaskNameMatchesAssignment(taskName, assignment, decisionId) {
  return assignmentTaskNameMatchesDecision(
    taskName,
    assignment?.assignmentId,
    decisionId,
    assignment?.role,
  );
}
