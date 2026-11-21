---
name: heta-language
description: Write and revise Heta model source with correct language semantics in Chat or Codex. Use for model structure, reactions, assignments, namespaces, and syntax explanations; validate specific models with the local Heta Compiler or Heta API.
---

# Heta language

Write the smallest complete Heta model that expresses the requested behavior and can be checked. Start with one `index.heta` source and direct expressions; add units, namespaces, modules, or `#defineFunction` when the model or user request calls for them. Preserve the structure of an existing project. Consult the relevant reference below for unfamiliar syntax.

## Model patterns

- **Source format:** When the user asks for model code without naming a format, write `.heta` source. Use CSV/XLSX tables or Heta JSON action modules when requested or when extending an existing project in those formats. If an existing SBML model is supplied, try including it as an `sbml` module before rewriting it manually; compile the result and inspect import diagnostics. See [tables and modules](references/tables-and-modules.md).
- **One model:** Write components at the top level. They belong to the default `nameless` namespace; do not introduce a named namespace just to group a single model.
- **Named models and templates:** In `.heta` source, put components inside `namespace name begin ... end`. `namespace name;` only declares a namespace and does not move subsequent unqualified components into it. In tables, use the `space` column. Use named namespaces when the user requests them or when the platform contains separate models or reusable templates. See [namespaces and imports](references/namespaces-and-imports.md) for variants and component reuse.
- **Choose the state class by meaning:** Represent molecules, particles, cells, and other entities present in a compartment as Species. Describe their production, conversion, transport, and loss with Reactions. Do not replace these with Records merely because the equations can be written that way. Give each Species a compartment and an initial value unless a `:=` rule defines it. Species represents concentration by default; use `isAmount: true` for an absolute amount or count.
- **Dynamic, boundary, or rule-based:** Species and Record can be dynamic states, boundary values, or rule-based values without changing their classes. `boundary: true` blocks Reaction/Process contributions but still permits event assignments. `:=` on a Species or Record defines an explicit rule; its value is then determined by that expression rather than by Reactions or Processes. The rule also takes precedence over initial and event assignments.
- **Reaction rates and units:** A Reaction rate represents amount per time, even when unit annotations are omitted. For a first-order reaction of concentration `A` with `k` in inverse time, use `k*A*cell`; for an amount `A`, use `k*A`. The `actors` property gives stoichiometry, not the kinetic law.
- **Declaring units:** Unit annotations are optional. Omit them in simple test examples when units are not specified. When units are known or the user provides them, declare them on the relevant components and keep expressions dimensionally consistent; do not invent missing units. See [units](references/units.md).
- **Other dynamic variables:** Use a Record and Process for dynamic quantities that are not entities in a compartment, such as an abstract activity or response. A Record does not require a compartment. Initialize a state with `.=`. On a Record, `:=` defines an algebraic rule, not its derivative; on a Reaction or Process, `:=` defines the rate.
- **Parameters and derived values:** Use `Const` for numeric parameters. If a value is calculated from other components, define it as a `Record` with `:=` instead of putting an expression in `Const.num`.
- **Adjustable initial values:** Put an initial value in a numeric Const, for example `A_init @Const = 10; A @Species { compartment: cell } .= A_init;`. Scenarios in HetaSimulator.jl or internal heta scenarios can override `A_init`; they do not directly override the Species initial assignment.
- **Events:** Define a switcher and an assignment to the affected state. A switcher alone changes nothing, and an event assignment cannot change a Const. Assign a concentration to a concentration Species and an amount to an amount Species; convert a dose using the compartment size when needed.
- **Simulation outputs:** Set `output: true` on components the user wants in default simulation results.
- **Declaration and update order:** Declare each component once with `@Class`, with any initial properties. Later statements can update its properties without `@Class`. Repeating `@Class` for the same ID inserts a replacement component, discards its earlier properties, and warns about the replacement. For an intentional replacement, use `#forceInsert id @Class ...;` to suppress that warning. References in expressions or properties such as `compartment` may point to components declared later; order declarations logically for readability.

A minimal concentration model illustrates the ordinary case:

```heta
cell @Compartment .= 1;
A @Species { compartment: cell } .= 10;
B @Species { compartment: cell } .= 0;
k @Const = 0.1;
r @Reaction { actors: A => 2B } := k*A*cell;
```

For a nonmaterial dynamic variable, use a Record and Process without a compartment:

```heta
k @Const = 0.1;
activity @Record .= 5;
decay @Process { actors: activity => } := k*activity;
```

## Details and validation

- [Language reference](references/heta-language.md): actions, classes, expressions, functions, and scenarios.
- [Namespaces and imports](references/namespaces-and-imports.md): separate model variants and reusable components.
- [Events](references/events.md): switchers and event assignments.
- [Units](references/units.md): unit syntax and dimensional checks.
- [Tables and modules](references/tables-and-modules.md): tabular sources and included modules.

For a model you create or change, use `heta-compiler` when the local Compiler and source files are available; otherwise use `heta-modeling-api` when its `buildPlatform` tool is available. Check the result before calling the model valid. If neither is available, say that the source is unverified. Consult the [official language specifications](https://hetalang.github.io/specifications/) when the bundled references do not resolve a syntax question or conflict with compiler diagnostics. Compilation does not run a numerical simulation.
