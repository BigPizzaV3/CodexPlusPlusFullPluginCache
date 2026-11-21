# Julia environment and compatibility

Sources: [HetaSimulator installation](https://hetalang.github.io/HetaSimulator.jl/stable/#Installation)
and [Julia project environments](https://pkgdocs.julialang.org/v1/environments/).

## Find and verify Julia

First try `julia --version` and `julia -e 'println(1+1)'`. Treat a failed command
or a PATH entry as inconclusive: a Juliaup launcher or Windows App Execution Alias
may exist without working in the current process. A successful check prints the
version and then `2`. When `julia` works, `julia -e 'println(Sys.BINDIR)'`
identifies the directory of the running version; still test the binary there
directly before relying on it.

If `julia` fails, try `juliaup status` to see installed channels. This command
shows versions, not necessarily executable paths, and may fail even when a Julia
binary is installed. Do not update or install channels merely to locate Julia.

On Windows, use PowerShell to inspect likely locations without scanning the
whole disk:

```powershell
Get-Command julia,juliaup -All -ErrorAction SilentlyContinue
Get-ChildItem "$env:USERPROFILE\.julia\juliaup\julia-*\bin\julia.exe" -ErrorAction SilentlyContinue
Get-ChildItem "$env:LOCALAPPDATA\Programs\Julia*\bin\julia.exe" -ErrorAction SilentlyContinue
Get-ChildItem "$env:ProgramFiles\Julia*\bin\julia.exe" -ErrorAction SilentlyContinue
```

If `JULIAUP_DEPOT_PATH` is set, search its `juliaup/julia-*/bin/julia.exe`
subdirectories instead of assuming the default depot. A zero-byte `julia.exe`
under `%LOCALAPPDATA%\Microsoft\WindowsApps` is an execution alias, not the
versioned Julia binary. For a candidate path, run:

```powershell
& "C:\path\to\julia.exe" --version
& "C:\path\to\julia.exe" -e 'println(1+1)'
```

On macOS or Linux, check `command -v julia`, `~/.juliaup/bin/julia`, and
`~/.julia/juliaup/julia-*/bin/julia` (or the configured Juliaup depot). Test a
candidate with the same version and execution checks. If several versions work,
prefer the one required by the project's manifest or existing instructions;
otherwise use the configured Juliaup default when available. If none works,
ask the user for the installation path or help installing Julia.

## Existing project

Inspect Project.toml, Manifest.toml (including version-specific manifests), and
the project's existing launch instructions. Activate that environment.
Use Pkg.instantiate() when recorded dependencies need to be restored; do not
replace a manifest or run a general update as a routine launch step.

If HetaSimulator is already configured, use it. If an existing environment lacks
the package required for this task, add it there rather than creating a second
environment or installing into Julia's shared default environment.
Check direct imports in the runner against the active project's `Project.toml`.
If an imported non-stdlib package is missing, add it with `Pkg.add` in that
project and keep the resulting `Project.toml` and `Manifest.toml` changes. In
particular, `using CSV` requires CSV as a direct dependency; reading a scenario
table through HetaSimulator's `read_scenarios` does not itself require the runner
to import CSV. Install only packages the task actually uses. Inspect package
resolution before accepting changes to existing versions; do not run a general
`Pkg.update()` as a repair step.

Recommended dependencies by task:

| Package | Add when |
| --- | --- |
| `HetaSimulator` | Running Heta simulations. |
| `Plots` | Calling `plot` on HetaSimulator results or making ordinary custom plots. |
| `DataFrames` | Calling `DataFrame(results)` directly or analyzing result tables. |
| `CSV` | Calling `CSV.read` or `CSV.write` directly; not for `read_scenarios` alone. |
| `XLSX` | Directly reading or writing Excel files; not for HetaSimulator's own scenario loader alone. |
| `StatsPlots` | Using statistical recipes or `@df` table plots when the installed Plots version needs the separate package. |

The package name is `StatsPlots`. Its repository notes that
StatsPlots functionality is integrated into Plots v2, so inspect the installed
Plots version and available recipes before adding the separate package. Do not
add both plotting packages merely because a tutorial imports both. See the
[HetaSimulator plotting guide](https://hetalang.github.io/HetaSimulator.jl/stable/tutorial/plots/)
and [StatsPlots repository](https://github.com/JuliaPlots/StatsPlots.jl).

## New environment in the project root

Run from the root, or pass its absolute path to Pkg.activate:

```julia
using Pkg
Pkg.activate(".")
Pkg.Registry.update()
Pkg.add("HetaSimulator")
Pkg.status(["HetaSimulator"])
```

The add operation writes Project.toml and Manifest.toml as applicable; activation
alone does not install packages. Package downloads live in Julia's depot, while
the environment description lives in the project root.

For new installations, request the latest stable registered release, not a
development Git branch or a hardcoded package version. Pkg resolves versions
against Julia and other dependencies. Verify the resolved version against the
registry's [release list](https://github.com/JuliaRegistries/General/blob/master/H/HetaSimulator/Versions.toml).
If constraints prevent the newest release, explain them instead of calling an
older resolution the latest or silently changing Julia.

Launch project scripts from the root with `julia --project=. path/to/script.jl`,
or with the verified absolute executable path when the launcher is unavailable.
Check `Base.active_project()`, `VERSION`, and Pkg.status when environment identity
is uncertain. Install additional packages only when the task uses them.

## Heta Compiler mismatch

HetaSimulator supplies its compiler as an artifact. Updating a globally installed
heta executable does not necessarily change the compiler used by load_platform.
Read the actual loading error and compiler diagnostics; if needed inspect the
installed package/artifact metadata. Do not infer its version from the package
version or from `heta --version`.

builderVersion is a compiler compatibility range, not a HetaSimulator version.
For the example ^0.12.2 versus bundled 0.12.1, proposing ^0.12.1 lowers the
minimum accepted patch version; it does not prove the source is compatible.
Check any newer features first and present the proposed edit to the user.
After agreement, change only the relevant requirement and retry the actual
HetaSimulator load. If newer features are required, describe the blocker rather
than loosening the range.

First installation can involve downloads and precompilation; absence of immediate
output is not a failure. Follow the running process until it completes.
