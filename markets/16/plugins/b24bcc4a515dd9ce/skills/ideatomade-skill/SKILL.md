---
name: ideatomade-skill
description: Use when the user wants to develop, design, refine or physically verify a physical product or mechanical system for real-world use, or prepare it for DIY making, manufacturing and assembly. Supports DIY making and manufacturing workflows involving processes such as 3D printing, CNC machining, woodworking, sheet-metal fabrication, cutting, drilling, bending, fastening and assembly. Covers parametric modeling, physical simulations, interactive inspection, production files, drawings, bills of materials and assembly instructions using IdeaToMade MCP.
---

# IdeaToMade Skill

## Develop a complete physical product or mechanical system

Develop a complete physical product or mechanical system users can
understand, inspect, refine and make through their chosen process. This includes
furniture and woodworking, printed products, welded frames, sheet-metal assemblies,
enclosures, jigs, fixtures,
robotic mechanisms, automation equipment, small machines, lab, test rigs, etc.
Keep the making process, tools, materials and intended use central: elegant geometry
that cannot be assembled or manufactured does not fulfill the request. Completion
requires sufficient physical and geometric verification, the complete files needed
to manufacture and assemble that revision, and available for user's interactive inspection.
Call get_environment in IdeaToMade MCP to check available tools, libraries, import names, interpreters and launchers before choosing how to model and verify the design.
Use specialized engineering tools in sandboxes.

## Aim for a design that is fit for purpose

The design must meet the user's intended outcomes and the inherent functional
and physical requirements of its intended use, making process, assembly and
applicable disassembly. It must be feasible to make or manufacture, assemble
and use within the user's constraints.

## Verify physical behavior

Verify the relevant physical behaviors of the product, its manufacturing and assembly
processes, part interactions, and intended disassembly.

- Use physical simulations in the IdeaToMade MCP sandbox to verify the product's
  intended functions and relevant physical behaviors, including manufacturing,
  assembly, part interactions and intended disassembly.

## Assess computations against the intended physical research

Base confidence in a computation on how well its results answer the intended
physical research. Choose checks
appropriate to the model and intended use
and define acceptance criteria before evaluating results, so they reflect the task
rather than whichever outcome the solver happens to produce.

## Choose tools for the engineering task

The table is a capability guide;
the appropriate combination depends on the design and the evidence needed.
Use `get_environment` for current availability, import names, interpreters and
launchers, since native tools can require separate environments.

| Need | Familiar interface | Boundary |
| --- | --- | --- |
| Exact parametric geometry | `build123d` | Source for production STEP, tessellated previews and mesh exports |
| 2D drawings/cutting outlines | `ezdxf` | Layers, dimensions, annotations, blocks, DXF units and cutting geometry |
| Mechanism motion/contact | `mujoco` Python, MJCF/XML | Headless dynamics, joints, actuators and trajectories |
| Beams/frames/plates | `from Pynite import FEModel3D` | Structural forces, reactions and deflections in explicitly consistent units |
| FEA mesh | `gmsh` Python or CLI | CAD discretization, element quality and mesh refinement |
| 3D FEA | `ccx -i analysis` | CalculiX `.inp` deck; inspect `.dat`, `.frd` and solver messages |
| CNC CAM | `FreeCADCmd` + CAM Python | Stock, operations, tools and controller-specific postprocessor |
| Cutter geometry | `import opencamlib as ocl` in system Python | Toolpath computation used where supported by the CAM workflow |
| 3D print preparation | `prusa-slicer` CLI | Explicit printer, filament and print profiles; leave upstream source unchanged |
| Numerical checks | NumPy: `import numpy as np` | Arrays, vector/matrix operations, tolerances, finite-value checks and analytical comparisons; export numerical CSV/JSON |
| Technical PDF documents | ReportLab: `reportlab.pdfgen`, `reportlab.platypus` | Generate vector drawings, tables, bills of materials and assembly instructions |
| SVG inclusion in PDFs | svglib: `svg2rlg` | Convert supported SVG content into ReportLab vector objects; check dimensions and unsupported features |
| PDF assembly and inspection | pypdf: `PdfReader`, `PdfWriter` | Merge, split, inspect and annotate PDFs |
| Plot-data preparation | `matplotlib` | Prepare numerical series, contour coordinates and color mappings |
| Numerical engineering methods | `scipy` | Optimization, integration, interpolation, sparse solvers and signal processing; supply the physical equations and constraints |
| Symbolic engineering calculations | `sympy`, `sympy.physics.mechanics` | Derive equations, simplify expressions and obtain analytical references; numerical evaluation requires explicit parameters |
| Beam cross-section properties | `sectionproperties` | Compute area, centroid, inertias, torsion and warping properties; requires section geometry and material definitions |
| Flexible multibody dynamics | `exudyn` | Simulate rigid and flexible bodies, joints and mechanical systems |
| Fatigue assessment | `fatpack` | Rainflow counting and cumulative fatigue damage from load histories; requires applicable fatigue curves |
| Composite laminate properties | `composites` | Calculate laminate stiffness matrices and lamination parameters from ply materials, thicknesses and orientations |
| Custom finite-element formulations | scikit-fem: `import skfem` | Assemble and solve finite-element equations; explicitly define elements, material laws, loads and boundary conditions |
| Robot kinematics and dynamics | Pinocchio: `import pinocchio as pin` | Compute poses, Jacobians, mass matrices and inverse dynamics; contact behavior needs a suitable additional model |
| Impact and nonlinear dynamics | OpenCourant: `starter_linux64_gf`, `engine_linux64_gf` | Explicit FEA for impacts and large-deformation contact; use `.rad` decks and inspect stability and energy balance |
| Triangle-mesh processing | `trimesh` | Inspect connectivity, watertightness, volume and transforms; mesh accuracy depends on tessellation and topology |
| Planar geometry operations | `shapely` | Polygon intersections, offsets, containment and clearances; operates on planar geometry rather than 3D solids |
| Solid mesh Boolean operations | `manifold3d` | Union, intersection and difference of manifold triangle meshes; preserves mesh geometry rather than exact CAD surfaces |
| Assembly and process graphs | `networkx` | Represent connectivity, dependencies and operation ordering; graph results alone do not establish physical feasibility |
| Image and voxel analysis | scikit-image: `import skimage` | Segmentation, measurements and isosurface extraction from image or voxel data; preserve physical scale |
| Manufacturing mesh packaging | `lib3mf` | Read and write supported 3MF geometry, components, units and metadata; does not generate printer toolpaths |
| Alternative filament slicing | `CuraEngine slice` | Generate G-code using explicit machine, extruder, material and print settings |
| Resin print-file processing | `UVtoolsCmd` | Inspect, repair and convert supported sliced resin files; verify printer format, layer and exposure settings |
| Spatial candidate searches | `rtree` | Accelerate bounding-box searches for proximity and collision candidates; exact geometry checks remain necessary |
| Simulation mesh exchange | `meshio` | Convert supported mesh formats and transfer field data; verify units, cell types, tags and connectivity |
| Point-cloud reconstruction | `open3d` | Register, filter and reconstruct measured geometry; retain measurement uncertainty |
| Configurable finite-element analysis | SfePy: `import sfepy` | Solve supported PDE and continuum-mechanics formulations; explicitly define materials, fields, equations and boundaries |
| Variational finite-element analysis | FEniCSx: `dolfinx`, `ufl` | Express and solve custom weak-form PDEs; requires appropriate discretization, boundary conditions and convergence checks |
| Physical units and conversions | Pint: `import pint` | Track dimensions and convert units; solver inputs still require an explicitly consistent unit system |
| Finite-volume transport models | FiPy: `import fipy` | Solve diffusion, convection and reaction equations on meshes with specified coefficients and boundary conditions |
| Time-dependent field equations | py-pde: `import pde` | Solve PDEs on supported grids, including diffusion and reaction systems; check spatial and temporal resolution |
| Fluid-system calculations | `fluids` | Pressure losses, pipe flow and equipment correlations; applicability depends on flow regime and correlation assumptions |
| Alloy phase equilibrium | `pycalphad` | Calculate phase equilibria and thermodynamic properties using compatible material databases; does not predict processing kinetics |
| Heat-transfer calculations | `ht` | Heat-transfer correlations and heat-exchanger sizing; requires suitable properties, geometry and operating conditions |
| Interactive visual inspection | `three.js` | View GLB/glTF and JSON with part and assembly controls |
| glTF/GLB format validation | glTF-Validator: `import validator from 'gltf-validator'` | Check format compliance, references, buffers and accessors; engineering dimensions and simulation agreement need separate checks |

## Estimate long runs

## Prepare machine output from the actual setup

Printer output depends on the chosen printer, nozzle, material and print profile.
CNC output depends on the machine, controller/postprocessor, tools, stock, work origin,
fixturing, safe heights, feeds/speeds and operations. Research decisive missing facts
before calling output machine-ready; reversible internal geometric drafts can proceed
earlier, while shared previews and delivery still follow the evidence thresholds.
Identify which
checks were actually performed. Do not send commands to physical equipment through
this plugin.

## Provide manufacturing and assembly documentation
Provide the complete set of equipment- and manufacturing-process-specific files required to make/manufacture and assemble the product using the chosen setup.
For DIY projects, dimensioned drawings, a cut list, a bill of materials and assembly
instructions are part of the package where relevant. Distinguish parts to make from
components to obtain. Show assembly order, fasteners, tolerances and tool access.
For commissioned manufacture, communicate the material, finish, fabrication and
acceptance requirements the supplier needs. Generate spreadsheets and technical
PDFs using suitable document-writing libraries.


## Make the physical product inspectable and validate the inspection files
Convert and validate engineering files for fully interactive Three.js part/assembly inspection.
Make the physical product inspectable through rotation, zoom, fit-to-model,
individual-part inspection and outside/inside inspection using suitable visibility
or section controls. For assemblies, provide assembled/disassembled states and
controls to explore the applicable assembly/disassembly sequence. Respect permanent
joints and monolithic parts. Keep the initial view centered on the model and useful controls.
When sharing these inspection files, tell the user in one sentence which Three.js viewer file to open in their browser to interactively inspect the parts or assembly.

## Export all before auto-deletion

