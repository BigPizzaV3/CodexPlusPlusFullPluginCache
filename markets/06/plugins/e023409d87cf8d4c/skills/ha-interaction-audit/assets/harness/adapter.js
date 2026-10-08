import {createMockHass} from '/mock-hass.mjs';
import {createFaultController} from '/fault-controller.mjs';

// Replace this adapter with a mount of the verified active target resources.
// Supply explicit mock contracts and synthetic data. Never import live HA auth.
const faults = createFaultController();
const mock = createMockHass({faults});
window.__HA_AUDIT = {
  ready:false,
  identity:null,
  app:null,
  mock,
  faults,
  snapshot:() => ({adapterConfigured:false,intents:mock.intents}),
  dispose:() => mock.dispose()
};
document.getElementById('fixture-root').textContent =
  'Adapter not configured. Mount the verified dashboard before running assertions.';
