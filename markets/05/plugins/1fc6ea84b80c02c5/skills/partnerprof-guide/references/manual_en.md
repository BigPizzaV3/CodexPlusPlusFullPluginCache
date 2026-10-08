# PartnerProf — Public Computation Guide

PartnerProf accepts structured numeric reality fields. Free-form prose is not a computation input.

## Minimal input

Choose the problem family and field geometry, then confirm only the quantities that actually belong to the current reality. For each quantity, provide its numeric value when known, its unit, and whether it is a fixed fact, an observation, a free quantity, or a bounded quantity. Relations, constraints, invariants, and the goal are separate parts of the field and are never inferred from prose.

The **Default vector** is preset to **0.2** and cannot be set below 0.2. It is used for a first run when no realized history is available. Existing history can be imported as an advanced input; it is not a goal and does not determine the result by itself.

## Default quantum demonstration

The default demonstration is a structured quantum-tunnelling field with the following values:

- nuclear distance: 8 fm
- barrier width: 5 fm
- barrier height: 400 keV
- temperature: 100 MK
- declared target region: nuclear distance ≤ 5 fm
- Default vector: 0.2

These are preset numeric values, not a word problem and not an AI interpretation. A user can run the preset immediately and then inspect or modify individual quantities.

## Reading the result

The primary result is the public CML state for the exact approved numeric input. The interface reports separately:

1. whether an admissible realization was returned;
2. whether attainment of the declared goal is explicitly proven;
3. the numeric change between the approved input field and the returned field;
4. the input and output vector norms, run identifier, output digest, and result signature;
5. any additional numeric projection that was actually published with the result.

A positive CML state is not automatically described as goal attainment. Coherence is an audit characteristic, not a percentage of correctness. Returned vector coordinates are not labelled as new physical values in the original units unless an explicit decoding contract supports that interpretation.

Internal implementation details are intentionally not part of the public interface or this guide.
