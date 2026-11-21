# BOSL2 basics for Print Ready

This guide is an original summary of the [BOSL2 wiki](https://github.com/BelfrySCAD/BOSL2/wiki), checked against Print Ready's pinned [2.0.766 source](https://github.com/BelfrySCAD/BOSL2/tree/e173fa0ae45f9e2082e0d8c0382dae98621b7c20). Upstream documentation may describe newer behavior. Consult the [full cheatsheet](https://github.com/BelfrySCAD/BOSL2/wiki/CheatSheet), [function index](https://github.com/BelfrySCAD/BOSL2/wiki/AlphaIndex), [file index](https://github.com/BelfrySCAD/BOSL2/wiki/TOC) and [tutorials](https://github.com/BelfrySCAD/BOSL2/wiki/Tutorials) for details. BOSL2 is by the BelfrySCAD contributors under the [BSD-2-Clause license](https://github.com/BelfrySCAD/BOSL2/blob/e173fa0ae45f9e2082e0d8c0382dae98621b7c20/LICENSE).

## Includes and the hosted runtime

Start with `include <BOSL2/std.scad>`. It loads standard shapes, transforms, constants and attachment support. Specialized libraries need additional includes. Use `include`, rather than replacing it with `use`, so library constants and setup remain available.

| Task | Additional include | Reference |
| --- | --- | --- |
| Chamfered or rounded shapes | None beyond std.scad | [Shapes](https://github.com/BelfrySCAD/BOSL2/wiki/shapes3d.scad) |
| Generic threads | `BOSL2/threading.scad` | [Threading](https://github.com/BelfrySCAD/BOSL2/wiki/threading.scad) |
| Standard screws and nuts | `BOSL2/screws.scad` | [Screws](https://github.com/BelfrySCAD/BOSL2/wiki/screws.scad) |
| Spur, bevel and worm gears | `BOSL2/gears.scad` | [Gears](https://github.com/BelfrySCAD/BOSL2/wiki/gears.scad) |
| Hinges | `BOSL2/hinges.scad` | [Hinges](https://github.com/BelfrySCAD/BOSL2/wiki/hinges.scad) |
| Snap pins and dovetails | `BOSL2/joiners.scad` | [Joiners](https://github.com/BelfrySCAD/BOSL2/wiki/joiners.scad) |
| Sweeps and skins | `BOSL2/skin.scad` | [Sweeps](https://github.com/BelfrySCAD/BOSL2/wiki/skin.scad) |
| Rounded paths and end treatments | `BOSL2/rounding.scad` | [Rounding](https://github.com/BelfrySCAD/BOSL2/wiki/rounding.scad) |

Print Ready supplies the pinned library to its isolated compiler. Do not install it at runtime or reference host filesystem paths. Query capabilities for current source size, triangle and runtime limits. Use moderate tessellation while iterating. STL contains geometry, not source colors or an assembly's motion constraints.

## Shapes, anchors and orientation

BOSL2 shapes generally center themselves by default. Specify `anchor=BOTTOM` when the bottom should sit at Z=0. `LEFT`, `RIGHT`, `FRONT`, `BACK`, `TOP`, `BOTTOM` and `CENTER` are direction constants; sums such as `TOP+RIGHT` describe combined anchors. `spin` rotates about the local Z axis before `orient` aims that axis in another direction. Check the anchor semantics for irregular shapes.

```openscad
include <BOSL2/std.scad>
$fn=32;
cuboid([30,20,6], chamfer=1, anchor=BOTTOM);
```

Use `rounding=` for rounded edges and `chamfer=` for bevels. `edges=` selects which edges to treat. `cyl()` supports end treatments and `tube()` creates a hollow cylindrical shape. See [cuboid](https://github.com/BelfrySCAD/BOSL2/wiki/shapes3d.scad#module-cuboid), [cyl](https://github.com/BelfrySCAD/BOSL2/wiki/shapes3d.scad#module-cyl) and [tube](https://github.com/BelfrySCAD/BOSL2/wiki/shapes3d.scad#module-tube).

`up`, `down`, `left`, `right`, `fwd` and `back` are translations. `xrot`, `yrot`, `zrot` and `rot` express rotations. `xcopies`, `grid_copies` and `zrot_copies` repeat geometry. See [transforms](https://github.com/BelfrySCAD/BOSL2/wiki/transforms.scad) and [distributors](https://github.com/BelfrySCAD/BOSL2/wiki/distributors.scad).

## Attachments and boolean tags

Make the attached object a child of its parent shape. `position(TOP)` moves to a parent's anchor; `attach(TOP,BOTTOM)` additionally aligns the child's bottom to that parent's top. `overlap=` can provide a deliberate union overlap. Native `linear_extrude`, `rotate_extrude`, `polygon` and `polyhedron` do not automatically supply BOSL2 attachment metadata. Use an attachable wrapper or the appropriate BOSL2 alternative.

```openscad
include <BOSL2/std.scad>
$fn=32;
diff()
  cuboid([30,20,6], anchor=BOTTOM)
    attach(TOP)
      tag("remove") cyl(d=6,h=14,anchor=TOP);
```

`diff()` subtracts geometry tagged `remove`. A native `difference()` does not interpret BOSL2 tags. Ensure cutters pass through the entire intended thickness, including a small overrun where coincident faces would be ambiguous. Read the [attachment overview](https://github.com/BelfrySCAD/BOSL2/wiki/Tutorial-Attachment-Overview), [basic positioning](https://github.com/BelfrySCAD/BOSL2/wiki/Tutorial-Attachment-Basic-Positioning) and [attachments reference](https://github.com/BelfrySCAD/BOSL2/wiki/attachments.scad).

## Threads and screw standards

Choose the thread's standard, nominal diameter, pitch, handedness and engagement length before designing its mating part. A generic threaded rod is not automatically a standards-compliant screw head or a validated printed fit.

```openscad
include <BOSL2/std.scad>
include <BOSL2/threading.scad>
$fn=48;
trapezoidal_threaded_rod(d=8,l=12,pitch=2,thread_angle=90,
                       thread_depth=0.60,bevel=true,blunt_start=true,
                       anchor=BOTTOM);
right(20) difference() {
  cyl(d=16,h=10,chamfer=0.6,anchor=BOTTOM);
  down(0.01) trapezoidal_threaded_rod(d=8,l=10.02,pitch=2,
    thread_angle=90,thread_depth=0.60,internal=true,$slop=0.15,
    bevel=true,blunt_start=true,anchor=BOTTOM);
  // 45 degree entry chamfers extend through the cutter's ends.
  down(0.01) cyl(d1=9.8,d2=8.6,h=0.6,anchor=BOTTOM);
  up(9.4) cyl(d1=8.6,d2=9.8,h=0.61,anchor=BOTTOM);
}
```

For custom FDM threads, `thread_angle=90` gives 45 degree flanks. Generate the female using the matching profile with `internal=true`. This V3 starting profile uses 8 mm diameter, 2 mm pitch and 0.60 mm radial depth, leaving 0.40 mm flat lands. Apply clearance once. On the female cutter, `$slop=0.15` adds 0.60 mm diametrally, or 0.30 mm radially. Do not also enlarge its nominal diameter. Include chamfered entries and blunt lead-ins, and print both axes vertically. Treat clearance as a starting value until physically tested.

Use `$slop` only where the chosen module documents it. For a standards-based fastener, inspect `screw()` and `screw_hole()` in the [screws reference](https://github.com/BelfrySCAD/BOSL2/wiki/screws.scad). See [trapezoidal_threaded_rod](https://github.com/BelfrySCAD/BOSL2/wiki/threading.scad#module-trapezoidal_threaded_rod) for the custom printable profile. Standard hardware still needs its matching standard, dimensions and tolerances.

## Gears

Use the same module or pitch convention and compatible pressure angles for mating gears. Tooth count, profile shift and backlash affect the pair. Use the documented `gear_dist()` calculation when positioning a pair with those options; do not guess center distance from the outside diameters.

```openscad
include <BOSL2/std.scad>
include <BOSL2/gears.scad>
$fn=32;
spur_gear(mod=1.5,teeth=20,thickness=6,shaft_diam=5,anchor=BOTTOM);
```

`mod` is metric module. `circ_pitch` is circular pitch, not the same numeric value. Avoid supplying incompatible pitch specifications together. Check minimum teeth, interference and clearances for the actual pair. See [spur_gear](https://github.com/BelfrySCAD/BOSL2/wiki/gears.scad#module-spur_gear) and [gear_dist](https://github.com/BelfrySCAD/BOSL2/wiki/gears.scad#function-gear_dist).

## Hinges and snap joints

```openscad
include <BOSL2/std.scad>
include <BOSL2/hinges.scad>
$fn=32;
knuckle_hinge(length=30,segs=5,offset=8,knuckle_diam=6,
              pin_diam=2,arm_height=4,anchor=BOTTOM);
```

The mating hinge leaf needs the complementary `inner` setting, matching segmentation and suitable pin and knuckle clearances. Inspect the assembly and its travel. See [knuckle_hinge](https://github.com/BelfrySCAD/BOSL2/wiki/hinges.scad#module-knuckle_hinge).

```openscad
include <BOSL2/std.scad>
include <BOSL2/joiners.scad>
$fn=32;
snap_pin("standard",l=12,anchor=BOTTOM,orient=UP);
```

This pin is double-ended. Its `l` setting controls one side rather than the total printed length. Use the corresponding `snap_pin_socket()` as a negative cutter in a receiving body; it is not a standalone finished socket. Review its size, orientation and documented clearance rules. Snap flexibility depends on material, layer direction and arm geometry. See [snap_pin](https://github.com/BelfrySCAD/BOSL2/wiki/joiners.scad#module-snap_pin) and [snap_pin_socket](https://github.com/BelfrySCAD/BOSL2/wiki/joiners.scad#module-snap_pin_socket).

## Paths and sweeps

A path is a list of points; a region can contain multiple paths and holes. Keep 2D profile data separate from rendered geometry. `path_sweep()` moves a profile along a path and `skin()` joins profiles. Abrupt corners, self-intersections and mismatched profile winding can create invalid meshes. Begin with a small simple example from the [skin reference](https://github.com/BelfrySCAD/BOSL2/wiki/skin.scad) or [rounding reference](https://github.com/BelfrySCAD/BOSL2/wiki/rounding.scad), then compile and inspect each revision.

```openscad
include <BOSL2/std.scad>
include <BOSL2/skin.scad>
$fn=24;
path_sweep(rect([4,4]),[[0,0,2],[0,0,12],[8,0,20]]);
```

## Check the result

Inspect compiler warnings, triangle count, bounds and actual previews. An unknown module warning can silently omit a component even when other geometry exports. Check every separate output and mating part. Bring the intended bed face to Z=0 and inspect underside overhangs. A successful compilation confirms supported geometry for that example; it does not prove physical fit, strength, gear meshing or hinge movement after printing.
