# Heta language

Sources:
[syntax](https://hetalang.github.io/specifications/syntax.html),
[classes](https://hetalang.github.io/specifications/classes.html),
[actions](https://hetalang.github.io/specifications/actions.html),
[math](https://hetalang.github.io/specifications/math.html).

## Statements and actions

Heta is an ordered sequence of actions creating and updating a platform.
Action statements end with `;`; namespace blocks end with `end`. IDs start
with a letter or underscore, followed by letters, digits, or underscores.
Avoid reserved words such as `namespace`, `true`, and `pi`.

```heta
clearance @Const { units: litre/hour } = 0.2;
```

The ID is clearance, the class is Const, and the dictionary supplies properties.
Equivalent full form:
`{id: clearance, class: Const, units: litre/hour, num: 0.2};`.
Quote dictionary strings containing delimiters, including expressions with commas.
Single quotes supply a title; triple single quotes supply notes.

Heta applies statements in order. The default `#upsert` acts as an insert when
`@Class` is present and as an update when the class is omitted. Declare a
component once with `@Class`; you may set its properties in that declaration.
Later statements for the same ID can add or replace properties without repeating
`@Class`:

```heta
k1 @Const = 5;
k1 = 7; // updates the existing Const
```

Repeating `@Class` for an existing ID in the same namespace inserts a new
component, replacing the old component and discarding its earlier properties.
The compiler warns about this replacement to catch accidental duplicates. This
is true whether the two statements are on one line or on separate lines:

```heta
comp1 @Compartment { boundary: true } .= 5;
comp1 @Compartment .= 7; // warning; replaces comp1 and loses boundary: true
```

When replacement is intentional, say so explicitly with `#forceInsert`. It
still replaces the component and its properties, but does not issue the
duplicate-insert warning:

```heta
#forceInsert k1 @Const = 4;
```

A reference is resolved after the components are loaded, so an expression or
property such as `compartment` may refer to a component declared later:

```heta
k1 @Const = 5;
s1 @Species { compartment: comp1 } .= k1 * 7;
comp1 @Compartment .= 5;
```

This is valid; grouping dependencies before their uses usually makes the source
easier to read. Forward references do not make an update before the initial
`@Class` declaration valid. `#insert`, `#update`, and `#delete` make the action
explicit; consult the [actions specification](https://hetalang.github.io/specifications/actions.html)
for replacement and property-clearing details.

## Assignments and classes

- `k @Const = 0.2;` creates `k` and sets its numeric property `num`.
- `k = 0.3;` sets the value of previously created const.
- `x @Record .= 1;` sets assignments.start_, an initial expression.
  `[]=` is another spelling.
- `y @Record := 2*x;` sets assignments.ode_, a continuously evaluated rule.
  Despite its internal name, this defines y, not its derivative.
- `x [pulse]= x + 1;` sets an event assignment; see
  [events](events.md).

`Species` and `Process` inherit from `Record`; `Reaction` inherits from
`Process`. A Species adds `compartment` and `isAmount` while retaining the
Record's assignment and `boundary` behavior. The class describes what the
component represents; these properties determine how its value is obtained:

- With an initial assignment (`.=`), a non-boundary Species or Record can change
  through Reactions or Processes that list it in `actors`.
- `boundary: true` prevents those Reaction/Process contributions. The value
  stays at its initial value unless an event assignment or a rule changes it; `boundary`
  alone does not disable switchers.
- A rule assignment (`:=`) calculates the Species or Record value from its
  expression. It takes precedence over initial and event assignments, and
  Reactions/Processes do not determine that value, even if they list it in
  `actors`.

For example, a concentration elimination model can also define a derived
total amount:

```heta
central @Compartment .= 3;
drug @Species { compartment: central } .= 10;
clearance @Const = 0.2;
elimination @Reaction { actors: drug => } := clearance*drug;
total @Record := drug*central;
```

Here clearance has intended dimension volume/time. With an elimination constant
kel in 1/time, use `kel*drug*central` instead. Do not silently omit a compartment
factor.

## Expressions and functions

Expressions use `+ - * / ^`, comparisons `> >= < <= == !=`, and Boolean
operators `and or xor not`. Power is right-associative; parenthesize when
transferring expressions from languages with different precedence.
Common functions include exp, ln, log, log10, sqrt, abs, min, max, and pow.
Both ln and log mean natural logarithm.

Use `condition ? a : b` or `piecewise(a, condition, b)` for conditional values.
Without an otherwise value, piecewise returns NaN when no condition matches.
Do not assume arbitrary MATLAB or JavaScript functions are available.

```heta
#defineFunction saturate {
    arguments: [x, half],
    math: "x/(half+x)"
};
```

User functions refer to their arguments and supported functions. Pass model
quantities as arguments instead of implicitly capturing component IDs.

## Scenarios

```heta
baseline #setScenario {
    model: nameless,
    parameters: { clearance: 0.3 },
    tspan: [0, 24],
    observables: [drug]
};
```

Scenarios specify simulation conditions without rewriting components.
Parameters override Const values. Explicit output times in saveat take precedence
over tspan if both are supplied. events_active and events_save describe event
activation and before/after output selection. These declarations do not execute
a simulation; use the `heta-simulator` skill for local HetaSimulator.jl execution in Codex.

To vary a species/record' initial value between scenarios or fit it as an input, put
that value in a dedicated numeric Const and reference it in the initial
assignment:

```heta
cell @Compartment .= 1;
sp1_init @Const = 10;
sp1 @Species { compartment: cell } .= sp1_init;
```

Override `sp1_init` as a scenario parameter. Scenario parameters do not directly
override `sp1`'s initial assignment. Keep the Const's own value numeric: a Const
alias such as `sp1_init @Const = another_const;` is not valid for `Const.num`.
Use this pattern when the initial value is an input; fixed initial values can
remain direct assignments.
