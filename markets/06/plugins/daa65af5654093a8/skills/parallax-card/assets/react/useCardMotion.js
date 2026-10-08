import { useCallback, useEffect, useRef, useState } from 'react'

const clamp = (value, min, max) => Math.min(max, Math.max(min, value))
const normalizeDepth = (value) =>
  Number.isFinite(Number(value)) ? clamp(Number(value), 0, 100) / 100 : 0
const emptyPosition = () => ({ x: 0, y: 0, lift: 0 })

/**
 * Drives CSS variables directly without rendering on every animation frame.
 * --rx/--ry: card rotation in degrees; --px/--py: depth-scaled position (-1..1);
 * --mx/--my: light position in percent; --lift: depth-scaled engagement (0..1).
 * Use fixed layer distances with --px/--py; depth is already applied here.
 */
export default function useCardMotion({
  depth = 70,
  autoRotate = false,
  enabled = true,
} = {}) {
  const cardRef = useRef(null)
  const engineRef = useRef(null)
  const optionsRef = useRef({ depth, autoRotate, enabled })
  const [reducedMotion, setReducedMotion] = useState(() =>
    typeof window !== 'undefined'
      ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
      : false,
  )

  useEffect(() => {
    const media = window.matchMedia('(prefers-reduced-motion: reduce)')
    let prefersReducedMotion = media.matches
    let frameId = 0
    let lastTime = 0
    let disposed = false
    let hovered = false
    let keyboardActive = false
    let touchPointer = null
    let captureNode = null
    let orbitStartedAt = performance.now()
    let current = emptyPosition()
    let target = emptyPosition()

    const strength = () =>
      optionsRef.current.enabled && !prefersReducedMotion
        ? normalizeDepth(optionsRef.current.depth)
        : 0

    function writePosition() {
      const element = cardRef.current
      if (!element) return
      const amount = strength()
      const x = current.x * amount
      const y = current.y * amount
      element.style.setProperty('--rx', `${(-y * 14).toFixed(3)}deg`)
      element.style.setProperty('--ry', `${(x * 14).toFixed(3)}deg`)
      element.style.setProperty('--px', x.toFixed(4))
      element.style.setProperty('--py', y.toFixed(4))
      element.style.setProperty('--mx', `${(50 + x * 50).toFixed(2)}%`)
      element.style.setProperty('--my', `${(50 + y * 50).toFixed(2)}%`)
      element.style.setProperty('--lift', (current.lift * amount).toFixed(4))
    }

    function cancelFrame() {
      if (frameId) cancelAnimationFrame(frameId)
      frameId = 0
      lastTime = 0
    }

    function schedule() {
      if (!disposed && !document.hidden && !frameId) {
        frameId = requestAnimationFrame(animate)
      }
    }

    function animate(timestamp) {
      frameId = 0
      if (disposed) return
      if (!strength()) {
        current = emptyPosition()
        target = emptyPosition()
        writePosition()
        lastTime = 0
        return
      }

      const orbit = optionsRef.current.autoRotate && !hovered && !keyboardActive
      if (orbit) {
        const elapsed = timestamp - orbitStartedAt
        target = {
          x: Math.sin(elapsed / 4200) * 0.42,
          y: Math.sin(elapsed / 5700) * 0.3,
          lift: 0.55,
        }
      }

      const delta = lastTime ? clamp(timestamp - lastTime, 0, 64) : 1000 / 60
      const smoothing = 1 - Math.exp(-delta / 85)
      lastTime = timestamp
      let remaining = 0
      for (const axis of ['x', 'y', 'lift']) {
        current[axis] += (target[axis] - current[axis]) * smoothing
        const distance = Math.abs(target[axis] - current[axis])
        if (distance < 0.0005) current[axis] = target[axis]
        else remaining = Math.max(remaining, distance)
      }
      writePosition()
      if (orbit || remaining > 0) schedule()
      else lastTime = 0
    }

    function releaseCapture() {
      if (touchPointer !== null && captureNode) {
        try {
          if (captureNode.hasPointerCapture(touchPointer)) {
            captureNode.releasePointerCapture(touchPointer)
          }
        } catch {
          // The browser may already have cancelled a touch to begin scrolling.
        }
      }
      touchPointer = null
      captureNode = null
    }

    function rest() {
      hovered = false
      keyboardActive = false
      target = emptyPosition()
      schedule()
    }

    function pointerMove(event) {
      if (!strength()) return
      if (event.pointerType === 'touch' && event.pointerId !== touchPointer) return
      const element = cardRef.current
      if (!element) return
      const bounds = element.getBoundingClientRect()
      if (!bounds.width || !bounds.height) return
      hovered = true
      keyboardActive = false
      target = {
        x: clamp(((event.clientX - bounds.left) / bounds.width) * 2 - 1, -1, 1),
        y: clamp(((event.clientY - bounds.top) / bounds.height) * 2 - 1, -1, 1),
        lift: 1,
      }
      schedule()
    }

    function pointerDown(event) {
      if (!strength() || event.isPrimary === false) return
      if (event.pointerType === 'touch') {
        touchPointer = event.pointerId
        captureNode = event.currentTarget
        try {
          captureNode.setPointerCapture(touchPointer)
        } catch {
          // Pointer capture is optional; native touch scrolling stays enabled.
        }
      }
      pointerMove(event)
    }

    function pointerUp(event) {
      if (event.pointerId === touchPointer) {
        releaseCapture()
        rest()
      }
    }

    function pointerLeave(event) {
      if (event.pointerType === 'touch' && touchPointer !== null) return
      rest()
    }

    function pointerCancel(event) {
      if (event.pointerId === touchPointer) releaseCapture()
      rest()
    }

    function reset() {
      releaseCapture()
      hovered = false
      keyboardActive = false
      current = emptyPosition()
      target = emptyPosition()
      orbitStartedAt = performance.now()
      cancelFrame()
      writePosition()
      if (strength() && optionsRef.current.autoRotate) schedule()
    }

    function keyDown(event) {
      if (['Escape', 'Home', '0'].includes(event.key)) {
        event.preventDefault()
        reset()
        return
      }
      if (!strength() || !event.key.startsWith('Arrow')) return
      const directions = {
        ArrowLeft: [-0.2, 0],
        ArrowRight: [0.2, 0],
        ArrowUp: [0, -0.2],
        ArrowDown: [0, 0.2],
      }
      const direction = directions[event.key]
      if (!direction) return
      event.preventDefault()
      keyboardActive = true
      hovered = false
      target = {
        x: clamp(target.x + direction[0], -1, 1),
        y: clamp(target.y + direction[1], -1, 1),
        lift: 1,
      }
      schedule()
    }

    function refresh() {
      if (!strength()) {
        reset()
        return
      }
      if (!hovered && !keyboardActive && !optionsRef.current.autoRotate) {
        target = emptyPosition()
      }
      schedule()
    }

    function motionPreferenceChanged(event) {
      prefersReducedMotion = event.matches
      setReducedMotion(event.matches)
      refresh()
    }

    function visibilityChanged() {
      if (document.hidden) cancelFrame()
      else refresh()
    }

    engineRef.current = {
      pointerMove,
      pointerDown,
      pointerUp,
      pointerLeave,
      pointerCancel,
      keyDown,
      rest,
      reset,
      refresh,
    }
    media.addEventListener('change', motionPreferenceChanged)
    document.addEventListener('visibilitychange', visibilityChanged)
    writePosition()
    refresh()

    return () => {
      disposed = true
      cancelFrame()
      releaseCapture()
      media.removeEventListener('change', motionPreferenceChanged)
      document.removeEventListener('visibilitychange', visibilityChanged)
      engineRef.current = null
    }
  }, [])

  useEffect(() => {
    optionsRef.current = { depth, autoRotate, enabled }
    engineRef.current?.refresh()
  }, [depth, autoRotate, enabled])

  const onPointerMove = useCallback((event) => engineRef.current?.pointerMove(event), [])
  const onPointerDown = useCallback((event) => engineRef.current?.pointerDown(event), [])
  const onPointerUp = useCallback((event) => engineRef.current?.pointerUp(event), [])
  const onPointerLeave = useCallback((event) => engineRef.current?.pointerLeave(event), [])
  const onPointerCancel = useCallback((event) => engineRef.current?.pointerCancel(event), [])
  const onKeyDown = useCallback((event) => engineRef.current?.keyDown(event), [])
  const onBlur = useCallback(() => engineRef.current?.rest(), [])
  const reset = useCallback(() => engineRef.current?.reset(), [])

  return {
    cardRef,
    bind: {
      onPointerMove,
      onPointerDown,
      onPointerUp,
      onPointerLeave,
      onPointerCancel,
      onKeyDown,
      onBlur,
    },
    reset,
    reducedMotion,
  }
}
