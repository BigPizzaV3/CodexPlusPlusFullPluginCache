# Units

Source: [units](https://hetalang.github.io/specifications/units.html).

## Built-in units

Use the `units` property (plural). These unit names are built into the Compiler:

- Amount and volume: `mole`, `item`, `avogadro`, `litre`.
- Time: `second`, `minute`, `hour`, `day`, `year`.
- Other units: `gram`, `kilogram`, `metre`, `ampere`, `kelvin`, `candela`,
  `katal`, `joule`, `watt`, `volt`, `newton`, `becquerel`, `coulomb`, `farad`,
  `gray`, `henry`, `hertz`, `lumen`, `lux`, `ohm`, `pascal`, `radian`, `siemens`,
  `sievert`, `steradian`, `tesla`, `weber`.
- Dimensionless: `dimensionless`.

Use these exact names. For example, `litre` is built in, while `liter` is not.

## Units from `heta init`

For a project created with `heta init`, first inspect `src/qsp-units.heta` and
use its existing unit names instead of redefining common abbreviations. The
generated `src/index.heta` already includes it with
`include ./qsp-units.heta;`. This module supplies names such as `pmole`, `mL`,
`mg`, `pM`, `nM`, `uM`, `mM`, `s`, `h`, `cell`, and `percent`. The name is `pmole`,
not `pmol`. Keep the existing include in an initialized project; do not add it
twice. These names are available only when that module is included; for a
standalone source or another project, check its actual included modules.

## Custom units and expressions

Unit definitions are global to the platform and available in every namespace.
For readable `index.heta` code, put any new `#defineUnit` statements near the
beginning, after the unit-module include and before model components or
namespace blocks. Define each unit once; do not repeat it inside namespaces.

```heta
include ./qsp-units.heta;
squared_concentration #defineUnit { units: pmole^2/mL^2 };
clearance @Const { units: mL/h } = 0.2;
gain @Const { units: (1e-12 mole)^2/(1e-3 litre)^2 } = 1;
```

User-defined units can be used inside another `#defineUnit`, as with
`pmole^2/mL^2` above. The `gain` example shows the same unit written without
the abbreviations. Add a new `#defineUnit` only when the needed unit is absent
from the included modules.

Unit expressions use `*`, `/`, and `^`. Parentheses may enclose a scaled unit
such as `(1e-12 mole)` but cannot arbitrarily group
compound expressions. For example use `gram/litre/hour` instead of
`gram/(litre*hour)`.

Structured UnitsComponent arrays provide kind, multiplier, and exponent; consult
the units reference when using them.

## Dimensionless and unspecified units

For a dimensionless value, explicitly write `units: dimensionless` or
`units: 1`. If `units` is omitted, the unit is unspecified; that is not the
same as dimensionless. `item` is a count unit, not a dimensionless unit.

## Time unit

Set the time unit on `t` in the namespace whose model uses it. At the top
level, this sets it for the default `nameless` namespace:

```heta
t { units: second };
```

In a named namespace, place the same statement inside its `begin ... end`
block.

## Dimensional checks

Species units must match isAmount; reaction units are amount/time. Preserve
declared units and intended numerical scale when editing expressions.

Within Heta expressions, units do not convert numeric values automatically.
For example, a value stored in `g` is not multiplied by 1000 when used in a
quantity declared in `mg`. The Compiler checks the units of the two sides and
reports an inconsistency; write the numerical conversion explicitly.

Numeric literals inside expressions are dimensionless. A literal such as
`1000` cannot carry `mg/g` there. Assign the conversion factor to a Const with
units, then use that Const in the expression. With `qsp-units.heta` included:

```heta
dose_in_gram @Const { units: g } = 1;
gram_to_mg @Const { units: mg/g } = 1000;
dose_in_mg @Record { units: mg } .= gram_to_mg*dose_in_gram;
```

Writing `dose_in_mg @Record { units: mg } .= 1000*dose_in_gram;` instead
leaves the expression in `g` and produces a unit warning.

Use `--units-check` for dimensional checking, and inspect warnings as well as
errors.
