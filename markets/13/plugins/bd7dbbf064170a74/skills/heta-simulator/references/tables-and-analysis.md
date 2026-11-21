# Scenario tables and additional analyses

## Scenario tables

Source: [scenario table documentation](https://hetalang.github.io/HetaSimulator.jl/stable/table-formats/scenario/).

CSV and XLSX scenario tables describe simulation settings, not model-component
definitions. Load them with read_scenarios and add_scenarios!:

```julia
using HetaSimulator, Plots, DataFrames

table = read_scenarios("scenarios.csv")
add_scenarios!(platform, table)
results = sim(platform)
baseline = results[:baseline][2]
plot(baseline)
combined = DataFrame(results)
```

This runs all attached scenarios. Use `sim(scenarios(platform)[:baseline])`
when only one scenario should run. Use `DataFrame(results)` when a combined table
helps comparison or export; keep the original results for status checks and
individual plots. A runner using `plot` and `DataFrame` directly should declare
Plots and DataFrames as direct project dependencies. The scenario-indexed result
is a pair; `[2]` selects its `SimResult`.

Important columns:
- id: unique scenario identifier.
- model: model namespace, default nameless.
- tspan: table-format end time, with start at zero. This differs from the Julia
  Scenario constructor's two-element time span.
- parameters.<id>: parameter override; missing values leave it unchanged.
- saveat[] and observables[]: semicolon-separated output times and names.
- events_active.<id>: enable or disable an event.
- events_save.<id>: before/after saving flags; check installed-version support.

Inspect model and scenario IDs after importing. Do not assume a successful file
read means all intended conditions have been selected.

## Read on demand

Use these official guides when the corresponding analysis is requested:
- [Measurements](https://hetalang.github.io/HetaSimulator.jl/stable/table-formats/measurement/)
  and [fitting](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/fit/):
  connect data to scenarios and define the observation/error model before fitting.
- [Parameter tables](https://hetalang.github.io/HetaSimulator.jl/stable/table-formats/parameters/):
  configure fitted parameters, initial guesses, bounds, and estimation flags.
- [Monte Carlo](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/mc/):
  specify distributions, sample count, and requested summary.
- [Parallel execution](https://hetalang.github.io/HetaSimulator.jl/stable/basics/distributed/):
  check supported execution modes and worker environments.
- [Sensitivity analysis](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/gsa/):
  specify the parameter domain and outputs being studied.

These links route advanced tasks; their APIs are not assumed stable across
versions. Inspect the relevant guide and installed help before using them.
