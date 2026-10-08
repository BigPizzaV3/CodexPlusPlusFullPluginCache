import type { Finding, FindingStatus } from "./types";

type SankeyNode = {
  key: string;
  label: string;
  count: number;
  x: number;
  y: number;
  height: number;
  color: string;
};

const statusOrder: FindingStatus[] = [
  "fixed",
  "in_progress",
  "triaged",
  "new",
  "wontfix",
  "duplicate",
  "false_positive",
];

// Filtering out other statuses should not move a node along the workflow.
const statusPositions: Record<FindingStatus, number> = {
  new: 44,
  triaged: 59,
  in_progress: 74,
  fixed: 89,
  wontfix: 44,
  duplicate: 44,
  false_positive: 44,
};

// The band's thickness is a count, not a claim about movement between states.
// Sample a smooth curve for CSS, independent of the host's chart runtime.
function ribbon(
  source: SankeyNode,
  target: SankeyNode,
  from: number,
  to: number,
  thickness: number,
  height: number,
) {
  const edge = (offset: number, reverse: boolean) =>
    Array.from({ length: 25 }, (_, index) => {
      const t = (reverse ? 24 - index : index) / 24;
      const ease = t * t * (3 - 2 * t);
      return `${source.x + (target.x - source.x) * t}% ${
        ((from + (to - from) * ease + offset) / height) * 100
      }%`;
    });
  return `polygon(${[...edge(0, false), ...edge(thickness, true)].join(",")})`;
}

export function getFindingsSankeyLayout(
  findings: Finding[],
  labels: {
    root: string;
    severities: Array<{ key: string; label: string }>;
    status: (status: FindingStatus) => string;
  },
) {
  const groups = labels.severities
    .map(({ key, label }) => ({
      key,
      label,
      items: findings.filter(
        (finding) => (finding.criticality ?? "unknown") === key,
      ),
    }))
    .filter(({ items }) => items.length > 0);
  const statuses = statusOrder
    .map((key) => ({
      key,
      count: findings.filter((finding) => finding.status === key).length,
    }))
    .filter(({ count }) => count > 0);
  const height = Math.max(
    248,
    Math.max(groups.length, statuses.length) * 48 + 24,
  );
  // Leave room for readable two-line labels even for a one-finding node.
  const largestNode = Math.max(
    ...groups.map(({ items }) => items.length),
    ...statuses.map(({ count }) => count),
  );
  const unit = Math.min(96 / findings.length, 40 / largestNode);
  const totalHeight = findings.length * unit;
  const root: SankeyNode = {
    key: "findings",
    label: labels.root,
    count: findings.length,
    x: 1,
    y: (height - totalHeight) / 2,
    height: totalHeight,
    color: "var(--color-text-tertiary)",
  };
  function makeNode(
    key: string,
    label: string,
    count: number,
    x: number,
    index: number,
    length: number,
    color: string,
  ): SankeyNode {
    const nodeHeight = count * unit;
    const center =
      length === 1 ? height / 2 : 28 + (index * (height - 56)) / (length - 1);
    return {
      key,
      label,
      count,
      x,
      y: center - nodeHeight / 2,
      height: nodeHeight,
      color,
    };
  }
  const severityNodes = groups.map(({ key, label, items }, index) =>
    makeNode(
      key,
      label,
      items.length,
      23,
      index,
      groups.length,
      key === "critical"
        ? "var(--color-text-danger)"
        : key === "high"
        ? "var(--color-text-warning)"
        : key === "medium"
        ? "var(--color-text-caution)"
        : key === "low"
        ? "var(--color-text-info)"
        : "var(--color-text-tertiary)",
    ),
  );
  const statusNodes = statuses.map(({ key, count }, index) =>
    makeNode(
      key,
      labels.status(key),
      count,
      statusPositions[key],
      index,
      statuses.length,
      key === "fixed"
        ? "var(--color-text-success)"
        : key === "in_progress"
        ? "var(--color-text-info)"
        : "var(--color-text-tertiary)",
    ),
  );
  const bands: Array<{
    key: string;
    clipPath: string;
    fromColor: string;
    toColor: string;
  }> = [];
  const targetOffsets = statusNodes.map(() => 0);
  let rootOffset = 0;
  groups.forEach(({ key, items }, index) => {
    const source = severityNodes[index];
    bands.push({
      key,
      clipPath: ribbon(
        root,
        source,
        root.y + rootOffset,
        source.y,
        source.height,
        height,
      ),
      fromColor: root.color,
      toColor: source.color,
    });
    rootOffset += source.height;
    let sourceOffset = 0;
    statuses.forEach(({ key: status }, targetIndex) => {
      const count = items.filter((finding) => finding.status === status).length;
      if (!count) return;
      const target = statusNodes[targetIndex];
      const thickness = count * unit;
      bands.push({
        key: `${key}:${status}`,
        clipPath: ribbon(
          source,
          target,
          source.y + sourceOffset,
          target.y + targetOffsets[targetIndex],
          thickness,
          height,
        ),
        fromColor: source.color,
        toColor: target.color,
      });
      sourceOffset += thickness;
      targetOffsets[targetIndex] += thickness;
    });
  });
  return { groups, statuses, height, root, severityNodes, statusNodes, bands };
}
