# Tables and input modules

Sources: [tabular format](https://hetalang.github.io/specifications/tabular-format.html)
and [modules](https://hetalang.github.io/specifications/modules.html).

## Choosing a source format

A Heta platform can combine `.heta` source, CSV/XLSX tables, Heta JSON or YAML
action modules, and imported SBML. JSON input must follow Heta's
action-dictionary module structure; arbitrary JSON is not a Heta module.

An existing SBML model can be included as a module. Prefer testing that import
before transcribing the whole model into Heta syntax. Compile and inspect
warnings and resulting components; successful import alone does not establish
identical model behavior.

## Table structure

Tables represent the same ordered actions as Heta code. Each data row is an
action; headers identify properties.

- Simple headers: on, id, class, action, space, num, compartment, units.
- The `space` column selects the namespace for a row. Declare a named
  namespace before its component rows, for example with an `action: setNS` row.
- Nested assignment headers have the form `assignments.<key>`:
  `assignments.start_` corresponds to `x .= expression;`,
  `assignments.ode_` to `x := expression;`, and
  `assignments.pulse` to `x [pulse]= expression;`. Here `pulse` is the ID of a
  declared Switcher; use that Switcher's ID after the dot for other events.
- Simple arrays: header tags[] and cell value pk;human.
- Empty cells leave a property unset; they are not numeric zero.
- Cell strings do not require Heta-code quoting.
- Include an `on` column. The Compiler loads only rows with numeric 1 or
  Boolean true; 0, false, or an empty cell skips a row. Without this column,
  the rows are skipped. Use numeric or Boolean XLSX cells rather than text
  resembling those values.

```csv
on,id,class,num,compartment,assignments.start_,assignments.ode_,actors
1,clearance,Const,0.2,,,,
1,central,Compartment,,,3,,
1,drug,Species,,central,10,,
1,elimination,Reaction,,,,clearance*drug,drug =>
```

For an event assignment, declare the Switcher and put its ID in the target
component's assignment header:

```csv
on,id,class,compartment,assignments.start_,assignments.pulse,start
1,central,Compartment,,1,,
1,pulse,TimeSwitcher,,,,5
1,drug,Species,central,0,drug + 1,
```

The rate is a model expression in assignments.ode_, not an Excel formula
calculating a current numeric value. Keep model expressions as text.
Preserve row order when insert, update, or import actions depend on it.

## Loading tables alongside code

```heta
include ./model.csv type table;
#include { source: ./model.xlsx, type: table, sheet: 0, omitRows: 1 };
```

Include workbook sheets separately. sheet is zero-based, default 0.
omitRows skips rows after the header and before component rows, not the header
itself. transpose: true supports components arranged in columns.
For incomplete imports, inspect headers, sheet selection, and enabled rows.
Not every workbook sheet is imported automatically.

## Other modules

The default module type is heta. Specify other types explicitly.
JSON and YAML modules are arrays of Heta action dictionaries, for example:

```json
[
  {"id":"central","class":"Compartment","assignments":{"start_":"3"}},
  {"id":"drug","class":"Species","compartment":"central","assignments":{"start_":"10"}}
]
```

Include using `#include { source: ./model.json, type: json };`, or type: yaml.
JSON from an unrelated exporter, including SbioToStruct, does not automatically
constitute a Heta JSON module.

Include an existing SBML model with `#include { source: ./model.xml, type: sbml };`.
Consult [SBML conversion](https://hetalang.github.io/specifications/sbml-conversion.html)
when the import needs investigation. Input modules and Compiler exports are
different interfaces: do not assume any JSON-shaped output is reloadable as a
module.
