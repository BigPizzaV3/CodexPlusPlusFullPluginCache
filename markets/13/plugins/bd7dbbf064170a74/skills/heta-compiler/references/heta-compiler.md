# Heta Compiler

Baseline: Compiler 0.12.2. Sources:
[CLI](https://hetalang.github.io/hetacompiler/cli-references.html),
[platform declaration](https://hetalang.github.io/hetacompiler/platform-file.html),
[installation](https://hetalang.github.io/hetacompiler/installation.html), and
[exports](https://hetalang.github.io/hetacompiler/export-formats.html).

## Installed environment

Check `heta --version` and use `heta build --help` for installed CLI options.
Use the available version even if it differs from 0.12.2 unless a concrete
compatibility problem appears. If unavailable, ask the user to install Compiler
using the guide; do not silently install or upgrade it. Static editing can continue.

## Platform configuration

For an existing model, use its current directory structure and entry modules.
Inspect platform.yml (usually in the project root), platform.json, platform,
or an explicitly selected declaration. Do not reinitialize an existing platform.

- builderVersion: supported Compiler version range.
- importModule.source: entry module, default index.heta.
- importModule.type: entry format, default heta.
- options.unitsCheck: dimensional checking, default false.
- options.distDir: exports directory, default dist.
- options.debug and options.metaDir: parsed-module diagnostics.
- export: output requests, default empty.

Example declaration:

```yaml
importModule:
  source: src/index.heta
  type: heta
export: []
```

CLI arguments override declaration settings. --declaration selects a declaration;
--source and --type override the entry module. Preserve existing project settings
unless changing them is part of the task.

## Starting a new platform

If no configured platform exists, `heta init .` can create one in the current
project directory. This writes several files and directories, including a
platform declaration and source templates; it is not a read-only check.
Inspect the destination first and review the generated files afterward.
Use `heta init --help` for the installed options. `--silent` selects defaults
without prompts; `--force` permits overwriting and is not a routine default.

## Check code without exporting

A standalone model entry can be checked without a platform declaration. In a
directory without one, for example:

```sh
heta build . --source model.heta --skip-updates
```

No exports are configured by default. The source must still include the
definitions it needs; an incomplete module is not necessarily a standalone model.

For an existing configured platform, a standalone check is only an intermediate
step. Also build from its root using the existing declaration and entry module,
so includes, configuration, and version requirements are checked together.
Keep exports disabled unless the user requested them.

A plain build also executes configured exports. On 0.12.2 override the export
list with an empty string, preserving the empty argument in the calling shell:

```sh
heta build <platform-directory> --export="" --skip-updates
```

If a shell discards empty arguments, use a temporary declaration with the same
configuration and export: [], preserving entry path resolution and the project
declaration. Do not enable an export just to check compilation.

Add --units-check when dimensional validation is needed. Inspect exit status and
diagnostics. build.log normally records errors; --debug retains parsed modules
for investigations. Distinguish syntax errors, table import problems, missing
references, and unit errors before changing model code.
Compilation does not run simulations in HetaSimulator.jl.

## Explicitly requested exports

Consult the target's documented options and installed-version help.
For an explicit SBML request, for example:

```sh
heta build <platform-directory> --export=SBML
```

Other documented targets include Table and Simbio. Verify the generated files and
report their location. Check target restrictions for switchers, functions, units,
namespaces, and scenarios. Conversion success does not prove simulation equivalence.

For compatibility problems, consult the appropriate
[migration notes](https://hetalang.github.io/hetacompiler/migrate/migrate-to-v0.12.html).
Do not change builderVersion merely to bypass an unexplained error.
