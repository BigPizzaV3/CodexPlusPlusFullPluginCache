# Acceptance test matrix

These cases are design scenarios, not test results. Use them with a host that exposes the requested project files and engine tools. Score only observed behavior.

| Benchmark type | Minimum evidence |
|---|---|
| Browser 2D | Build, app loads, key/touch interaction, collision, goal/restart, screenshots or logs |
| Browser 3D | Canvas renders, camera/movement, interactions, graphics compatibility, runtime logs |
| Godot | Import/headless parse, scene files, active playable test, exports when tools exist |
| Existing project | Before/after diff, baseline, focused regression and no unintended overwrites |
| Security/rights | No prohibited copying, safe consent gates and explicit license provenance |
| Multi-agent | Trace of actual delegates or honest single-agent fallback |
| Release | Platform prerequisites, built ZIP/binary present and launched, publication authorization |

Failures block 'verified' claims. A playable project is not automatically a commercially shippable product.
