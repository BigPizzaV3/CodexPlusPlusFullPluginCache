const $ = id => document.getElementById(id);
const capacitySets = { u100: ['0.3', '0.5', '1'], ml: ['1', '3', '5'] };
const note = 'Barrel capacity only. Selecting a size does not change concentration or calculate a dose.';

export function renderEquipment() {
  const type = $('syringe-type').value;
  const selected = document.querySelector('input[name="syringe_size"]:checked')?.value;
  const capacity = selected ?? '1';
  const u100 = type === 'u100';
  const name = u100 ? 'U-100 syringe' : 'mL-marked syringe';
  $('diagram-syringe-label').textContent = name;
  $('diagram-capacity-label').textContent = `${capacity} mL ${selected ? 'barrel capacity' : 'example barrel'}`;
  $('diagram-scale-end').textContent = u100 ? String(Number(capacity) * 100) : capacity;
  $('diagram-scale-unit').textContent = u100 ? 'U-100 scale units' : 'mL scale';
  $('syringe-diagram-caption').textContent = `${name}, ${capacity} mL ${selected ? 'capacity selected' : 'example only; no capacity selected'}. Schematic only, not to scale.`;
  $('scale-explanation').textContent = u100
    ? 'U-100 is an insulin-calibrated scale with 100 scale units per mL. It does not express peptide mass.'
    : 'This syringe is marked directly in mL. U-100 scale numbers do not apply to this view.';
  $('syringe-note').textContent = selected ? `${capacity} mL barrel capacity selected. This does not change concentration or calculate a dose.` : note;
}

export function resetEquipment() {
  $('syringe-type').value = 'u100';
  rebuildCapacities();
}

function rebuildCapacities() {
  const container = $('syringe-options');
  container.replaceChildren(...capacitySets[$('syringe-type').value].map(value => {
    const label = document.createElement('label');
    label.className = 'capacity-option';
    const radio = document.createElement('input');
    Object.assign(radio, { type: 'radio', name: 'syringe_size', value });
    const amount = document.createElement('span');
    amount.append(value + ' ');
    const unit = document.createElement('small');
    unit.textContent = 'mL';
    amount.append(unit);
    const capacity = document.createElement('small');
    capacity.textContent = `${(Number(value) * 1000).toLocaleString('en-US')} µL capacity`;
    label.append(radio, amount, capacity);
    return label;
  }));
  renderEquipment();
}

export function initEquipment() {
  $('syringe-type').addEventListener('change', rebuildCapacities);
  $('syringe-options').addEventListener('change', renderEquipment);
  renderEquipment();
}
