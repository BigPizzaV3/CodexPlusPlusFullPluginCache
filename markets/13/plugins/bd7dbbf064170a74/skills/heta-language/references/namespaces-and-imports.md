# Namespaces and imports

Sources: [model variants](https://hetalang.github.io/how-to/model-variants/),
[cloning components](https://hetalang.github.io/how-to/clone-model-components/),
and [actions](https://hetalang.github.io/specifications/actions.html).

## Namespace scope

Components written at the top level belong to the default `nameless`
namespace. For one model, use that default. For a named model, put its
declarations and subsequent updates inside one `namespace name begin ... end`
block. Indent the statements between `begin` and `end`:

```heta
namespace fast begin
  cell @Compartment .= 1;
  A @Species { compartment: cell } .= 10;
  k @Const = 0.2;
end
```

The first line opens the namespace, unqualified statements inside it belong to
`fast`, and `end` closes the block. Do not put a semicolon after `end`.
`namespace fast;` only creates the namespace; it does not change the scope of
following unqualified statements. Prefer the block form for model code. Use
`fast::k = 0.3;` only for an occasional targeted update from outside the block.
A namespace must exist before components are inserted into it. Component IDs
are local to a namespace; unit definitions are global to the platform. Each
namespace has its own time component `t`.

`include ./model.heta;` reads a module in the current scope. At the top level,
its components enter `nameless`. An include does not create a namespace.

## Namespaces in tables

CSV and XLSX modules do not use `namespace ... begin ... end` blocks. Specify
each row's namespace in a separate `space` column. Declare a named namespace
before its component rows, either in Heta code before including the table or
with a `setNS` action row:

```csv
on,action,space,id,class,num
1,setNS,fast,,,
1,insert,fast,k,Const,0.2
1,insert,,base_k,Const,0.1
```

In this top-level table, `k` belongs to `fast`; the blank `space` for `base_k`
uses `nameless`. See [tables and modules](tables-and-modules.md) for other
columns and loading options.

## Independent model variants

When variants share most of a model but need different components or equations,
include the base model once and clone its namespace before making variant
updates. For example, `base-model.heta` contains:

```heta
cell @Compartment .= 1;
A @Species { compartment: cell } .= 10;
B @Species { compartment: cell } .= 0;
k @Const = 0.1;
r @Reaction { actors: A => B } := k*A*cell;
```

Then `index.heta` contains:

```heta
include ./base-model.heta;

namespace fast begin
  #importNS { fromSpace: nameless };
  k = 0.3;
end
```

This creates independent `nameless` and `fast` models. Inside the block,
`#importNS` targets `fast` and `k = 0.3;` updates `fast::k`. The update to `k`
has no `@Const`: adding the class again would replace the component instead of
updating it. If only simulation inputs differ while the model structure stays
the same, scenarios may be sufficient instead of separate namespaces.

## Repeated components in one model

Use `#importNS` to clone all components from a template namespace into a
target model. Its destination is the current namespace (`nameless` at the top
level); use `space` to choose another destination explicitly. Both namespaces
must exist before the import.

```heta
abstract namespace decay_template begin
  x @Record .= 10;
  k @Const = 0.1;
  loss @Process { actors: x => } := k*x;
end

#importNS { fromSpace: decay_template, suffix: _a, rename: { t: t } };
#importNS { fromSpace: decay_template, suffix: _b, rename: { t: t } };
k_b = 0.2;
```

The assembled `nameless` model contains `x_a`, `loss_a`, `x_b`, and `loss_b`.
The Compiler also rewrites references inside the cloned Processes, so each
uses its matching `x` and `k`. The `rename: { t: t }` rule retains the existing
time component ID instead of creating `t_a` and `t_b`. An abstract namespace
is useful for a reusable template that should not itself become a concrete
model.

`prefix` and `suffix` rename imported IDs; `rename` overrides them for
individual IDs. Mapping to an existing target ID can overwrite that component;
use it only when the copies should share that ID. Inspect the assembled model
after importing. To copy only one component, use `#import`
with `fromId`, `fromSpace`, and a new target `id`; it does not automatically
import all the component's dependencies.

```heta
#import { id: k_copy, fromId: k, fromSpace: decay_template };
```
