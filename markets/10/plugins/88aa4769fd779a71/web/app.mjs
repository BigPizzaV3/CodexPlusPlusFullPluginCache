import { App } from '@modelcontextprotocol/ext-apps';
import { calculate, convertUnit, summary, InputError } from '../src/calculator.mjs';
import { initEquipment, resetEquipment } from './equipment.mjs';
import { initMotion } from './motion.mjs';

const $ = id => document.getElementById(id);
let result = null;
let hostApp = null;
let connected = false;
let currentUnits = { mass: 'mg', volume: 'mL' };
const embedded = window.parent !== window;
if (embedded) document.body.classList.add('embedded');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
function setTheme(theme) {
  document.documentElement.dataset.theme = theme === 'dark' ? 'dark' : 'light';
}
setTheme(systemTheme.matches ? 'dark' : 'light');
systemTheme.addEventListener('change', event => { if (!connected) setTheme(event.matches ? 'dark' : 'light'); });

function clearErrors() {
  for (const field of ['mass', 'volume']) {
    $(field).removeAttribute('aria-invalid');
    $(`${field}-error`).hidden = true;
    $(`${field}-error`).textContent = '';
  }
}

function clearResult(message = 'Awaiting values') {
  result = null;
  $('calculated-result').hidden = true;
  $('empty-result').hidden = false;
  $('result-tag').textContent = message;
  $('mg-result').textContent = '';
  $('mcg-result').textContent = '';
  $('formula').textContent = '';
  $('status').textContent = '';
}

function displayError(error, focus = true) {
  clearResult('Check values');
  const field = ['mass', 'volume'].includes(error.field) ? error.field : 'mass';
  $(field).setAttribute('aria-invalid', 'true');
  $(`${field}-error`).textContent = error.message;
  $(`${field}-error`).hidden = false;
  $('status').textContent = 'Calculation paused. Check the highlighted value.';
  if (focus) $(field).focus();
}

function render(next) {
  result = next;
  $('empty-result').hidden = true;
  $('calculated-result').hidden = false;
  $('result-tag').textContent = 'Calculated';
  $('mg-result').textContent = next.concentration.mgPerMl;
  $('mcg-result').textContent = next.concentration.mcgPerMl;
  $('approx').hidden = !next.concentration.rounded;
  $('rounding').textContent = next.concentration.rounded ? 'Approximately equal. Rounded to 12 significant digits.' : 'No display rounding needed.';
  $('formula').textContent = next.formula;
  $('share').hidden = !connected;
  $('status').textContent = '';
}

function input() { return { mass: $('mass').value, massUnit: $('mass-unit').value, volume: $('volume').value, volumeUnit: $('volume-unit').value }; }
initEquipment();
initMotion();

$('calculator').addEventListener('submit', event => {
  event.preventDefault(); clearErrors();
  try { render(calculate(input())); }
  catch (error) { displayError(error instanceof InputError ? error : new InputError('mass', 'Unable to calculate. Check your entries.')); }
});

for (const kind of ['mass', 'volume']) {
  $(kind).addEventListener('input', () => { clearErrors(); clearResult('Values changed'); });
  $(`${kind}-unit`).addEventListener('change', () => {
    const oldUnit = currentUnits[kind];
    const newUnit = $(`${kind}-unit`).value;
    clearErrors(); clearResult('Values changed');
    try {
      if ($(kind).value.trim()) {
        $(kind).value = convertUnit($(kind).value, oldUnit, newUnit, kind);
        $('status').textContent = 'Value converted to preserve the same quantity. Recalculate to see the concentration.';
      }
      currentUnits[kind] = newUnit;
    } catch (error) { $(`${kind}-unit`).value = oldUnit; displayError(error); }
  });
}

$('reset-calculator').addEventListener('click', () => {
  $('calculator').reset(); currentUnits = { mass: 'mg', volume: 'mL' };
  resetEquipment();
  clearErrors(); clearResult(); $('mass').focus();
  $('status').textContent = 'Calculator cleared.';
});

$('copy').addEventListener('click', async () => {
  if (!result) return;
  try { await navigator.clipboard.writeText(summary(result)); $('status').textContent = 'Result, formula, and assumptions copied.'; }
  catch { $('status').textContent = 'Clipboard access is unavailable. Select the displayed result to copy it.'; }
});

$('share').addEventListener('click', async () => {
  if (!result || !connected) return;
  const sharedResult = result;
  $('share').disabled = true;
  try {
    await hostApp.updateModelContext({ content: [{ type: 'text', text: summary(sharedResult) }] });
    $('status').textContent = result === sharedResult ? 'This result is now available to ChatGPT in the current conversation.' : 'The previously selected result was shared with ChatGPT.';
  } catch { $('status').textContent = 'Could not share with chat. The local calculation still works.'; }
  finally { $('share').disabled = false; }
});

for (const link of document.querySelectorAll('a[href^="https://"]')) {
  link.addEventListener('click', async event => {
    if (!connected) return;
    event.preventDefault();
    try {
      const response = await hostApp.openLink({ url: link.href });
      if (response.isError) $('status').textContent = `Link was not opened. You can copy this address: ${link.href}`;
    } catch { $('status').textContent = `Could not open the link. You can copy this address: ${link.href}`; }
  });
}

if (embedded) {
  hostApp = new App({ name: 'Peptide Reconstitution Calculator by Peptara Labs', version: '0.5.0' }, {});
  hostApp.ontoolinput = () => {};
  hostApp.ontoolresult = params => {
    const state = params.structuredContent;
    clearErrors();
    if (params.isError || state?.mode === 'error') {
      displayError(new InputError(state?.field ?? 'mass', state?.message ?? 'The tool could not calculate this input.'), false);
      return;
    }
    if (state?.mode === 'empty') {
      $('calculator').reset(); currentUnits = { mass: 'mg', volume: 'mL' }; resetEquipment(); clearResult(); return;
    }
    if (state?.mode === 'result' && state.result?.input) {
      try {
        // Recalculate from validated input rather than trusting display strings from the host.
        const next = calculate(state.result.input);
        for (const kind of ['mass', 'volume']) {
          $(kind).value = next.input[kind];
          $(`${kind}-unit`).value = next.input[`${kind}Unit`];
          currentUnits[kind] = next.input[`${kind}Unit`];
        }
        render(next);
      } catch (error) { displayError(error, false); }
    }
  };
  hostApp.onhostcontextchanged = params => {
    if (params.theme === 'dark' || params.theme === 'light') setTheme(params.theme);
  };
  hostApp.onerror = () => { connected = false; $('share').hidden = true; $('environment').textContent = 'Local calculation'; };
  hostApp.connect().then(() => {
    const hostTheme = hostApp.getHostContext()?.theme;
    if (hostTheme) setTheme(hostTheme);
    connected = true; $('environment').textContent = 'Connected to chat'; if (result) $('share').hidden = false;
  }).catch(() => { $('environment').textContent = 'Local calculation'; });
}
