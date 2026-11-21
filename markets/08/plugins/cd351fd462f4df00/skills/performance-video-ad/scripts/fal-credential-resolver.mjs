import { spawnSync } from "node:child_process";

export const FAL_KEYCHAIN_SERVICE = "com.mymarketer.video.fal";
export const FAL_ENV_NAMES = ["FAL_KEY", "FAL_API_KEY"];

export const validateFalCredentialCandidate = (value) => {
  const credential = typeof value === "string" ? value.trim() : "";
  if (!credential) return { valid: false, reason: "empty" };
  if (credential.length < 20) return { valid: false, reason: "too_short" };
  if (!/^[\x21-\x7E]+$/.test(credential)) return { valid: false, reason: "non_ascii_or_whitespace" };
  return { valid: true, value: credential };
};

export const resolveKeychainAccount = ({ env = process.env, spawn = spawnSync } = {}) => {
  const configuredAccount = env.USER?.trim();
  if (configuredAccount) return configuredAccount;
  const result = spawn("/usr/bin/id", ["-un"], { encoding: "utf8" });
  return result.status === 0 ? result.stdout.trim() : null;
};

export const resolveFalCredential = ({
  env = process.env,
  platform = process.platform,
  account = null,
  spawn = spawnSync,
} = {}) => {
  for (const name of FAL_ENV_NAMES) {
    const checked = validateFalCredentialCandidate(env[name]);
    if (checked.valid) return { value: checked.value, source: `environment:${name}` };
  }

  if (platform !== "darwin") return null;
  const keychainAccount = account ?? resolveKeychainAccount({ env, spawn });
  if (!keychainAccount) return null;
  const result = spawn(
    "/usr/bin/security",
    ["find-generic-password", "-a", keychainAccount, "-s", FAL_KEYCHAIN_SERVICE, "-w"],
    { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] },
  );
  if (result.status !== 0) return null;
  const checked = validateFalCredentialCandidate(result.stdout);
  if (!checked.valid) return null;
  return { value: checked.value, source: `macos_keychain:${FAL_KEYCHAIN_SERVICE}` };
};

export const hasFalCredential = (options = {}) => Boolean(resolveFalCredential(options));
