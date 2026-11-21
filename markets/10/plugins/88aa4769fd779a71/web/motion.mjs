export function initMotion() {
  const button = document.getElementById('motion-toggle');
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  let userPaused = false;
  const sync = () => {
    const paused = userPaused || preference.matches;
    document.body.dataset.motion = paused || document.hidden ? 'paused' : 'active';
    button.textContent = preference.matches ? 'Motion off' : userPaused ? 'Resume motion' : 'Pause motion';
    button.setAttribute('aria-pressed', String(paused));
    button.disabled = preference.matches;
    button.title = preference.matches ? 'Reduced motion is enabled in your system settings.' : '';
  };
  button.addEventListener('click', () => { userPaused = !userPaused; sync(); });
  preference.addEventListener('change', sync);
  document.addEventListener('visibilitychange', sync);
  sync();
}
