---
name: heta-simulator
description: Set up and use HetaSimulator.jl in Codex with a project-local Julia environment. Use for loading Heta platforms, configuring scenarios, running simulations, inspecting results, and requested fitting or ensemble analyses.
---

# HetaSimulator.jl

Use HetaSimulator to execute Heta models in Julia. Preserve an existing project's
environment, source structure, and simulation setup. The language and standalone
Compiler workflow are covered by this plugin's `heta-language` and
`heta-compiler` skills.

## Environment

- First try `julia --version`, then a small execution check such as
  `julia -e 'println(1+1)'`. Resolve the actual executable path, especially
  when the command is a Juliaup or Windows launcher. If the launcher fails,
  search installed versions before concluding that Julia is absent. Test the
  discovered executable and use its full path for subsequent project commands
  if the launcher is unreliable. See [environment and compatibility](references/environment.md)
  for search steps. If no executable works, ask the user for its location or
  whether Julia needs to be installed.
- Reuse an existing configured Julia environment and installed package versions.
  Do not update it solely because a newer release exists.
- Make every non-stdlib package imported by a runner a direct dependency of the
  active project. Restore a recorded environment with `Pkg.instantiate()` when
  needed; add missing packages required for the task to that project with
  `Pkg.add`. Do not install optional packages merely because they appear in an
  example or alter the shared default environment. See
  [environment and compatibility](references/environment.md).
- If no environment is configured, activate the **project root** with
  `Pkg.activate(".")` (equivalent to `] activate .`) and install HetaSimulator
  from the Julia registry. Use the latest registered stable release for a new
  installation. See [environment and compatibility](references/environment.md).
- Installation, precompilation, and first simulation can take time. Retain the
  running session and wait for completion before reporting success.

Recommended project dependencies, installed only when the task uses them:
`HetaSimulator` for simulation; `Plots` for HetaSimulator's `plot` recipes and
ordinary custom plots; `DataFrames` for direct `DataFrame(results)` conversion
and table analysis; `CSV` for direct CSV reading or writing; `XLSX` for direct
Excel file handling; and `StatsPlots` for statistical recipes or table-aware
plotting when those features are not already available in the installed Plots
version. Check compatibility before adding `StatsPlots`. See
[environment and compatibility](references/environment.md).

## Simulation workflow

1. Load the existing Heta platform directly with HetaSimulator.
   No manual standalone Compiler export is required.
2. Reuse existing scenarios or define those needed for the requested task.
3. Run the requested simulations and inspect their status and numerical outputs.
4. Save the requested results with enough context to identify the scenario.

For reproducible project scenarios, prefer CSV tables in `scenarios/`. Load
them with `read_scenarios` and `add_scenarios!`, keeping scenario values in the
table rather than duplicating them in Heta declarations and Julia constants.
Set the `model` column explicitly, including `nameless` when appropriate, as an
omitted value may not resolve in the installed HetaSimulator version. Use a
programmatic `Scenario` for an interactive diagnostic or when the user requests
it. For several fixed scenarios, use `sim(platform)` and convert the returned
results with `DataFrame(results)` when a combined table is useful. Select an
individual result by scenario ID when only that result is needed. Avoid parsing
scenario CSV rows by hand or copying all result values into another structure
unless the task needs behavior that the native API does not provide.

For Heta simulations, result export, and trajectory comparison, prefer Julia as
the project analysis language. Use MATLAB or another language only when it is
needed to execute or inspect the source implementation, or when the user
explicitly requests that language. Run ordinary project scripts from the
repository root and form paths relative to that working directory. Use `@__DIR__`
when the script must also work from another directory. Keep short runners as a
linear top-level sequence with the loading, scenario setup, simulation, checks,
and outputs visible. Avoid deep nesting, a `main()` wrapper, and custom data
containers when they add no clarity. Extract helpers for meaningful repetition
or a distinct domain operation. Use `Base.invokelatest` only for a reproduced
dispatch problem, not as a routine runner pattern. Follow an existing project's
conventions when they differ.

Use `sim` for one or many fixed deterministic scenarios, including all scenarios
already attached to a platform. Use `mc` for a parameter-variation ensemble
(such as a virtual-patient or Monte Carlo analysis), not merely because several
fixed scenarios exist. Use `fit` only when parameter identification against
measurements is requested. Keep solver configuration, output reduction,
parallelism, and parameter distributions explicit for the task at hand.

Shape an ordinary project runner after the current HetaSimulator tutorial
workflow: import the required packages, load the platform, load and attach the
scenario CSV, run `sim`, inspect a baseline with `plot`, then convert results to
`DataFrame` for tabular export or a custom analysis. Make paths, selected
scenarios, plotted variables, and output locations explicit. This is a
readability pattern, not a copy-and-paste template: add code for events, `mc`,
`fit`, or project-specific validation only when needed. Prefer current installed
API examples over tutorial files marked for earlier releases.

Use HetaSimulator's `plot` recipes directly on `SimResult`, `MCResult`, or their
scenario collections for ordinary simulation and Monte Carlo figures; select
variables with `vars` when useful. Convert with `DataFrame(results)` when the
task needs a table, derived summaries, or a custom figure, then plot with
`Plots` or, when needed and compatible, `StatsPlots`. Do not convert results
solely to reproduce a standard HetaSimulator plot. Keep the numeric results, time
coordinates, scenario identifiers, units, and event semantics available
regardless of plotting level.

Read [simulation and results](references/simulation.md) for the core workflow and
[scenario tables and other analyses](references/tables-and-analysis.md) when
working with tabular scenarios, fitting, Monte Carlo, or sensitivity analysis.

## Compiler compatibility

The standalone `heta` executable and the compiler bundled with HetaSimulator
can have different versions. If loading fails on builderVersion, report the
required range and the actual bundled version. Propose a compatible range only
after checking that the model does not need newer features.

For example, if the bundled compiler is 0.12.1 and the model requests ^0.12.2,
propose ^0.12.1 when appropriate. Explain the change and obtain the user's
agreement before applying it; then retry loading. Do not silently remove the
requirement or downgrade an environment to suppress an error.

## Documentation and scope

These references were reviewed against the
[stable documentation](https://hetalang.github.io/HetaSimulator.jl/stable/)
on 2026-09-28. Stable documentation moves with releases; check installed-version
help when an API differs. No local documentation checkout is required.

This skill operates simulations; it does not decide scientific acceptance
criteria or establish equivalence to another implementation. Fit parameters,
run ensembles, or change scientific settings only as part of the requested task.
