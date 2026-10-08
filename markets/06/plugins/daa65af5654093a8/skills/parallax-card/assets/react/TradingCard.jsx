import { useEffect, useRef } from 'react'
import { Droplets, Sparkles } from 'lucide-react'
import useCardMotion from './useCardMotion'
import './Card.css'

function BrandMark({ className = '' }) {
  return <span className={`brand-mark ${className}`} aria-hidden="true"><i /><i /><i /></span>
}

function TradingCard({ finish, depth, autoRotate, foil, exploded, flipped, setFlipped, focusRef }) {
  const { cardRef, bind, reset, reducedMotion } = useCardMotion({ depth, autoRotate, enabled: !flipped })
  const pointerStart = useRef(null)
  const dragged = useRef(false)
  useEffect(() => { focusRef.current = cardRef.current }, [cardRef, focusRef])
  const onKeyDown = event => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault()
      setFlipped(value => !value)
    } else bind.onKeyDown(event)
  }

  return <div className={`card-perspective ${exploded ? 'is-exploded' : ''}`}>
    <div className="card-ground-shadow" aria-hidden="true" />
    <div ref={cardRef} className={`card-motion ${flipped ? 'is-flipped' : ''} finish-${finish} ${foil ? 'has-foil' : ''}`}
      {...bind} onKeyDown={onKeyDown} tabIndex={0} role="button"
      onPointerDown={event => { pointerStart.current = [event.clientX, event.clientY]; dragged.current = false; bind.onPointerDown(event) }}
      onPointerMove={event => {
        if (pointerStart.current && Math.hypot(event.clientX - pointerStart.current[0], event.clientY - pointerStart.current[1]) > 8) dragged.current = true
        bind.onPointerMove(event)
      }}
      onPointerUp={event => { pointerStart.current = null; bind.onPointerUp(event) }}
      onPointerCancel={event => { pointerStart.current = null; dragged.current = true; bind.onPointerCancel(event) }}
      onPointerLeave={event => { pointerStart.current = null; bind.onPointerLeave(event) }}
      aria-label={`Aetherion collectible card. ${flipped ? 'Back' : 'Front'} face. Click or press Enter to flip, arrow keys to tilt, Home to reset.`}
      aria-pressed={flipped} aria-describedby="card-instructions"
      onClick={event => { if (event.detail === 0 || !dragged.current) { reset(); setFlipped(value => !value) } dragged.current = false }}>
      <div className="card-flipper">
        <div className="card-face card-front" aria-hidden={flipped}>
          <div className="card-base"><div className="edge-detail" /></div>
          <div className="card-world depth-layer">
            <img src="/assets/astral-world.png" alt="" draggable="false" />
            <div className="world-vignette" />
            <span className="layer-label">01 — THE WORLD</span>
          </div>
          <div className="card-stars depth-layer" aria-hidden="true">
            {Array.from({ length: 17 }, (_, index) => <i key={index} style={{ '--star-x': `${8 + ((index * 37) % 88)}%`, '--star-y': `${12 + ((index * 23) % 70)}%`, '--star-size': `${index % 3 === 0 ? 5 : 2}px`, '--star-delay': `${index * -0.4}s` }} />)}
            <div className="orbital-ring ring-one" /><div className="orbital-ring ring-two" />
          </div>
          <div className="card-creature depth-layer">
            <img src="/assets/astral-dragon.png" alt="Aetherion, an icy blue celestial dragon with sweeping fins and a curling tail" draggable="false" />
            <span className="layer-label">02 — THE CREATURE</span>
          </div>
          <div className="card-print depth-layer">
            <div className="card-heading"><div><span className="basic-label">CELESTIAL</span><h2>Aetherion <em>ex</em></h2></div><div className="card-hp"><small>HP</small><b>230</b><span><Droplets size={16} strokeWidth={2.7} /></span></div></div>
            <div className="card-bottom">
              <div className="creature-species">NO. 001 · THE ASTRAL TIDE DRAGON</div>
              <div className="attack"><span className="energy-cost"><Droplets /><Sparkles /></span><strong>Tidal Reverie</strong><b>80</b></div>
              <p>Draw from the depths. Restore 30 energy to this creature.</p>
              <div className="attack second-attack"><span className="energy-cost"><Droplets /><Droplets /><Sparkles /></span><strong>Astral Overflow</strong><b>160</b></div>
              <div className="card-rule"><span>weakness <b>ϟ ×2</b></span><span>resistance <b>−30</b></span><span>retreat <b>✧ ✧</b></span></div>
              <div className="card-collector"><span>ASTRAL ORIGINS</span><span>001 / 024 <b>✦ ✦ ✦</b></span></div>
            </div>
            <span className="layer-label">03 — THE DETAILS</span>
          </div>
          <div className="card-foil" aria-hidden="true" /><div className="card-glare" aria-hidden="true" />
          <div className="card-rim" aria-hidden="true" />
        </div>
        <div className="card-face card-back" aria-hidden={!flipped}>
          <div className="back-border" /><div className="back-orbit orbit-a" /><div className="back-orbit orbit-b" /><div className="back-orbit orbit-c" />
          <span className="back-edition">THE ASTRAL ORIGINS COLLECTION</span>
          <div className="back-center"><BrandMark /><span>parallax<span className="brand-period">.</span></span><small>A WORLD WITHIN.</small></div>
          <div className="back-star star-a">✧</div><div className="back-star star-b">✧</div>
          <span className="back-number">FIRST EDITION · NO. 001</span>
        </div>
      </div>
    </div>
    {reducedMotion && <span className="motion-notice">Reduced motion is on</span>}
  </div>
}


export default TradingCard
