import { useEffect, useState } from "react"
import { createRoot } from "react-dom/client"
import { flushSync } from "react-dom"
import { InlineConfirmPill } from "../../../src/components/builder/inline-confirm-pill"

// The armed "Confirm · 1 credit" state stays long enough to read and reach (SIT-486: the five-second window lapsed in the 16 Oct dry run).
const CONFIRM_WINDOW_MS = 12_000
// A second click within this of arming is the same double-click, never a Confirm (SIT-486: "thats a double clikc race").
const SAME_GESTURE_MS = 400

type Quote = { quoteId: string; label: string; credits: number; expiresAt: number }

function PaidConfirm({ quote, confirm, expired }: { quote: Quote; confirm: () => Promise<"approval" | void>; expired: () => void }) {
  const [pending, setPending] = useState<false | "starting" | "approval">(false)
  const [error, setError] = useState("")
  const [stale, setStale] = useState(() => quote.expiresAt <= Date.now())
  useEffect(() => {
    const timer = setTimeout(() => { setStale(true); expired() }, Math.max(0, quote.expiresAt - Date.now()))
    return () => clearTimeout(timer)
  }, [quote, expired])
  const price = `${quote.credits} credit${quote.credits === 1 ? "" : "s"}`
  return <><InlineConfirmPill label={`${pending === "approval" ? "Waiting for approval" : pending ? "Starting…" : quote.label} · ${price}`} price={price} consentKey={quote.quoteId}
    confirmable={!stale && !pending} confirmWindowMs={CONFIRM_WINDOW_MS} sameGestureMs={SAME_GESTURE_MS} disabled={stale || Boolean(pending)} className="paid-pill" confirmClassName="paid-pill-armed"
    onAction={() => {
      setError("")
      setPending("starting")
      void Promise.resolve().then(confirm).then(result => setPending(result === "approval" ? "approval" : false), failure => {
        setError(failure instanceof Error ? failure.message : "This action could not start. Check its status in chat before retrying.")
        setPending(false)
      })
    }} />{error && <p className="paid-error" role="alert">{error}</p>}</>
}

declare global {
  interface Window {
    iter0PaidConfirm: { mount: (element: HTMLElement, quote: Quote, confirm: () => Promise<"approval" | void>, expired: () => void) => () => void }
  }
}

window.iter0PaidConfirm = { mount(element, quote, confirm, expired) {
  const root = createRoot(element)
  flushSync(() => root.render(<PaidConfirm quote={quote} confirm={confirm} expired={expired} />))
  return () => root.unmount()
} }
