# Loading, simulation, and results

Sources: [quick start](https://hetalang.github.io/HetaSimulator.jl/stable/basics/overview/),
[simulation tutorial](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/sim/),
[API](https://hetalang.github.io/HetaSimulator.jl/stable/api/), and
[solver guidance](https://hetalang.github.io/HetaSimulator.jl/stable/basics/solvers/).

## Load and select

Use load_platform on the existing platform directory. It handles compilation
internally; generated Julia intermediates are not the authored model source.
The Julia environment root and Heta platform directory may differ.

Illustrative code, run with the project environment active:

```julia
using HetaSimulator

platform = load_platform(".")
model = models(platform)[:nameless]
scenario = Scenario(model, (0.0, 24.0))
result = sim(scenario)
println(status(result))
```

Select the actual namespace rather than assuming nameless exists. For a different
entry file, load_platform accepts a source keyword. Inspect scenarios(platform)
before adding scenarios: loading model definitions and selecting simulation
conditions are separate steps.

## Scenario settings

Reuse existing parameters, active events, time span, and observables where supplied.
Scenario accepts parameters and events_active as Symbol/value pairs, observables
as Symbols, and saveat as output times. For example, for a model containing
dose, pulse, and drug:

```julia
scenario = Scenario(model, (0.0, 48.0);
    parameters = [:dose => 20.0],
    events_active = [:pulse => true],
    observables = [:drug],
    saveat = collect(0.0:1.0:48.0))
result = sim(scenario)
```

Example numbers are illustrative, not a default scientific protocol.
Creating a Scenario does not automatically add it to the platform; add it with
add_scenarios! when a platform-level workflow needs it.

## Numerical execution

sim accepts alg, reltol, and abstol. Preserve an existing chosen solver and
tolerances. Current documentation describes AutoTsit5(Rosenbrock23()) as the
simulation default; installed-version behavior remains authoritative.
For stiff problems the documentation discusses methods such as Rodas5P, FBDF,
and QNDF. Choose based on evidence, not simply model size. Some solvers require
additional Julia packages.

Changing a solver or tolerance changes the numerical experiment. Record such
changes when they affect interpretation; do not tune them merely to make a
comparison pass without explaining the choice.

## Inspect and save

Inspect status(result), times(result), vals(result), and observables(result).
A returned object alone is not evidence of a successful full trajectory.
Investigate failed or unexpected termination before using results.

For a standard figure, load `Plots` and call `plot(result)` directly. This works
for a single `SimResult`, a collection of scenario results, and corresponding
`MCResult` outputs. Use `vars = [:name]` to limit displayed observables. The
[simulation tutorial](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/sim/)
and [Monte Carlo tutorial](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/mc/)
show these calls. Save the plot with `savefig` when an image file is requested.

For a table or custom figure, load `DataFrames` and call `DataFrame(result)` or
`DataFrame(results)` for several scenarios. Then use `Plots` for ordinary custom
figures or `StatsPlots` for statistical/table-aware recipes when needed. Keep
the original result objects for status checks and standard plots. Use a table
writer such as `CSV.write` only when saving CSV.
Keep numeric outputs and their time coordinates, not only plots.
Event output can contain before/after rows at the same time; preserve scope
information instead of deduplicating those rows blindly.

For comparison tasks choose output times and event handling deliberately.
saveat defaults and solver-selected times need not match another implementation.
Use the task's acceptance criteria rather than inventing them in this skill.
