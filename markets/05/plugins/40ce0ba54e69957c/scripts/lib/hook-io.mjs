import {
  requirePlainObject,
  validateHookInput,
} from "./contracts.mjs";

const maxInputBytes = 1024 * 1024;
const maxContextBytes = 512;
const contextEvents = new Set(["SessionStart", "UserPromptSubmit"]);

function requireBoundedString(value, label, maxBytes = maxContextBytes) {
  if (typeof value !== "string" || value.length === 0) {
    throw new TypeError(`${label} must be a non-empty string`);
  }
  if (Buffer.byteLength(value, "utf8") > maxBytes) {
    throw new RangeError(`${label} must not exceed ${maxBytes} bytes`);
  }
}

export function parseHookInput(text) {
  if (typeof text !== "string") {
    throw new TypeError("hook input must be a string");
  }
  if (Buffer.byteLength(text, "utf8") > maxInputBytes) {
    throw new RangeError("hook input exceeds 1 MiB");
  }
  let value;
  try {
    value = JSON.parse(text);
  } catch (error) {
    throw new SyntaxError(`invalid hook input JSON: ${error.message}`);
  }
  return validateHookInput(value);
}

export function additionalContextResult(eventName, context) {
  if (!contextEvents.has(eventName)) {
    throw new RangeError(
      `additional context is unsupported for ${String(eventName)}`,
    );
  }
  requireBoundedString(context, "additional context");
  return {
    hookSpecificOutput: {
      hookEventName: eventName,
      additionalContext: context,
    },
  };
}

export function allowToolInputResult(updatedInput) {
  requirePlainObject(updatedInput, "updated Agent input");
  return {
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "allow",
      updatedInput: structuredClone(updatedInput),
    },
  };
}

export function denyToolResult(reason) {
  requireBoundedString(reason, "tool denial reason");
  return {
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: reason,
    },
  };
}

export function serializeHookResult(result) {
  requirePlainObject(result, "hook result");
  return `${JSON.stringify(result)}\n`;
}
