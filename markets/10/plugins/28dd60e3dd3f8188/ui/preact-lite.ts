// Card-only stand-in for react, react-dom and react-dom/client (see scripts/chatgpt-extension-bundle.mjs).
// The price button uses five hooks, one root and flushSync, and nothing else from React. preact/compat (the React
// layer on top of preact) is ~5.7 KB of the card that none of it needs, and the card budget is a loading-speed limit.
import { render, type ComponentChild } from "preact"

export { useCallback, useEffect, useLayoutEffect, useRef, useState } from "preact/hooks"

// preact renders the first pass synchronously, which is all the card relies on; flushSync is the same call-through
// preact/compat makes.
export const flushSync = <T>(callback: () => T): T => callback()

export function createRoot(container: Element) {
  return { render: (node: ComponentChild) => render(node, container), unmount: () => render(null, container) }
}
