# Events

Source: [classes](https://hetalang.github.io/specifications/classes.html).

## Switchers

- TimeSwitcher schedules events: start defaults to 0; period repeats; stop limits
  the schedule. These properties accept numbers or Const references.
  For one event omit period and stop.
- DSwitcher takes a Boolean trigger and fires on a false-to-true transition
  checked at integration points. Timing can depend on simulation time steps.
- CSwitcher takes a numeric trigger and fires at a negative-to-positive zero
  crossing. Actual numerical handling depends on the simulator.
- StopSwitcher supplies a Boolean stop condition; check simulator support.

TimeSwitcher does not use `atStart`; do not copy that property from old examples.
DSwitcher and CSwitcher have their own `atStart` property.

The Switcher property is `active`, not `isActive`. When omitted, `active` is
`true`. Setting `active: false` keeps the event in the model but disables it
by default. A scenario can override this setting for a simulation with
`events_active: { switcherId: true }` or
`events_active: { switcherId: false }`.

```heta
volume @Compartment .= 2;
drug @Species { compartment: volume } .= 0;
dose @Const = 10;
pulse @TimeSwitcher { start: 0, period: 12, stop: 24 };
drug [pulse]= drug + dose/volume;
```

For concentration add dose/volume; for amount add dose directly.
An event assignment uses `target [switcher]= expression;` and replaces the
target's value when the event fires. If an event changes several targets,
evaluate all right-hand sides from the state before the event, then apply the
new values together. Events can update a Species or Record, including one with
`boundary: true`. A `:=` rule takes precedence over event assignments, so an
event assignment cannot control a rule-defined value.
Distinguish accumulation from replacement, such as `drug [pulse]= dose/volume`.

DSwitcher example, which may fire after `t` reaches 5:

```heta
x @Record .= 0;
on_time @DSwitcher { trigger: t >= 5 };
x [on_time]= 1;
```

CSwitcher example, crossing at `t = 5`:

```heta
x @Record .= 0;
on_time @CSwitcher { trigger: t - 5 };
x [on_time]= 1;
```

To keep an event available but off by default, set `active: false`; then enable
or disable it for individual scenarios:

```heta
x @Record .= 0;
pulse @TimeSwitcher { start: 5, active: false };
x [pulse]= 1;
with_pulse #setScenario { tspan: [0, 10], events_active: { pulse: true } };
without_pulse #setScenario { tspan: [0, 10], events_active: { pulse: false } };
```

