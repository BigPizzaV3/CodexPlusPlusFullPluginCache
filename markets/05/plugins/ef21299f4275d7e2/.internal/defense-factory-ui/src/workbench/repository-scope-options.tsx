import { Checkbox } from "@oai/ds/ui/checkbox";
import { useLayoutEffect, useRef, useState, type KeyboardEvent } from "react";

const ROW_HEIGHT = 40;
const VIEWPORT_HEIGHT = 320;
const OVERSCAN = 2;

type RepositoryOption = { value: string; label: string };

// Fixed-height windowing keeps the shared checkboxes and popover independent of
// host-only list components. Search is handled by the parent over the full set.
export function RepositoryScopeOptions({
  options,
  selected,
  onToggle,
}: {
  options: RepositoryOption[];
  selected: Set<string>;
  onToggle: (repository: string, checked: boolean) => void;
}) {
  const viewport = useRef<HTMLDivElement>(null);
  const pendingFocus = useRef<number | null>(null);
  const [firstVisibleRow, setFirstVisibleRow] = useState(0);
  const [focusedRow, setFocusedRow] = useState<number | null>(null);
  const first = Math.max(0, firstVisibleRow - OVERSCAN);
  const end = Math.min(
    options.length,
    firstVisibleRow + VIEWPORT_HEIGHT / ROW_HEIGHT + OVERSCAN,
  );
  const renderedRows = Array.from(
    { length: Math.max(0, end - first) },
    (_, index) => first + index,
  );
  // Wheel scrolling must not unmount the focused checkbox and drop focus to body.
  if (
    focusedRow !== null &&
    options[focusedRow] &&
    !renderedRows.includes(focusedRow)
  ) {
    renderedRows.push(focusedRow);
    renderedRows.sort((left, right) => left - right);
  }

  useLayoutEffect(() => {
    if (pendingFocus.current === null) return;
    const checkbox = viewport.current?.querySelector<HTMLElement>(
      `[data-repository-index="${pendingFocus.current}"] [role="checkbox"]`,
    );
    if (checkbox) {
      checkbox.focus({ preventScroll: true });
      pendingFocus.current = null;
    }
  }, [firstVisibleRow, focusedRow, options]);

  function handleKeyDown(event: KeyboardEvent<HTMLDivElement>) {
    const row = (event.target as HTMLElement).closest<HTMLElement>(
      "[data-repository-index]",
    );
    const container = viewport.current;
    if (!row || !container) return;
    const index = Number(row.dataset.repositoryIndex);
    let next: number;
    switch (event.key) {
      case "ArrowDown":
        next = index + 1;
        break;
      case "ArrowUp":
        next = index - 1;
        break;
      case "Home":
        next = 0;
        break;
      case "End":
        next = options.length - 1;
        break;
      case "Tab":
        next = index + (event.shiftKey ? -1 : 1);
        // At the full list's boundaries, let Tab reach the controls outside it.
        if (next < 0 || next >= options.length) return;
        break;
      default:
        return;
    }
    event.preventDefault();
    next = Math.max(0, Math.min(options.length - 1, next));
    const top = next * ROW_HEIGHT;
    if (top < container.scrollTop) container.scrollTop = top;
    else if (top + ROW_HEIGHT > container.scrollTop + container.clientHeight) {
      container.scrollTop = top + ROW_HEIGHT - container.clientHeight;
    }
    pendingFocus.current = next;
    setFirstVisibleRow(Math.floor(container.scrollTop / ROW_HEIGHT));
    setFocusedRow(next);
  }

  return (
    <div
      ref={viewport}
      role="list"
      className="overflow-y-auto overscroll-contain"
      style={{
        height: Math.min(VIEWPORT_HEIGHT, options.length * ROW_HEIGHT),
        maxHeight: "calc(75vh - 8rem)",
      }}
      onScroll={(event) =>
        setFirstVisibleRow(
          Math.floor(event.currentTarget.scrollTop / ROW_HEIGHT),
        )
      }
      onKeyDown={handleKeyDown}
      onBlur={(event) => {
        if (!event.currentTarget.contains(event.relatedTarget))
          setFocusedRow(null);
      }}
    >
      <div
        role="presentation"
        style={{ height: options.length * ROW_HEIGHT, position: "relative" }}
      >
        {renderedRows.map((index) => {
          const option = options[index];
          return (
            <div
              key={option.value}
              role="listitem"
              aria-posinset={index + 1}
              aria-setsize={options.length}
              data-repository-index={index}
              onFocus={() => setFocusedRow(index)}
              style={{
                position: "absolute",
                top: index * ROW_HEIGHT,
                height: ROW_HEIGHT,
                width: "100%",
              }}
            >
              <label
                className="hover:bg-token-interactive-bg-tertiary-hover flex h-full cursor-pointer items-center gap-3 rounded-lg px-2 text-[14px] leading-5"
                title={option.value}
              >
                <Checkbox
                  checked={selected.has(option.value)}
                  onCheckedChange={(checked) =>
                    onToggle(option.value, checked === true)
                  }
                  aria-label={option.label}
                />
                <span className="min-w-0 truncate">{option.label}</span>
              </label>
            </div>
          );
        })}
      </div>
    </div>
  );
}
