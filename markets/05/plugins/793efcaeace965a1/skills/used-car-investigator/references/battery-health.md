# Electrified-Vehicle Battery Health

Use this for mild hybrids, full hybrids, plug-in hybrids, and BEVs. Separate measured condition from
proxies and unknowns. Never invent a state-of-health percentage when the vehicle does not expose one.

## Evidence hierarchy

Grade the evidence independently from battery condition:

- A — OEM or qualified diagnostic report tied to the VIN and dated recently
- B — credible scan/test data with method, state of charge, temperature, and date documented
- C — indirect evidence such as a controlled range or charging test
- D — dashboard estimate, seller statement, or no useful test

State the test method and limitations. Range varies with temperature, speed, HVAC, tires, wheels,
terrain, driving style, calibration, and recent use; it is never a stand-alone health measurement.

## Required battery-health card

Record when the architecture exposes the data:

- chemistry, pack family/revision, original gross and usable capacity
- current usable capacity or OEM state of health, measurement method, date, odometer, SOC, and temperature
- module/cell voltage spread, internal-resistance spread, temperature spread, and imbalance flags
- BMS, high-voltage isolation, contactor/interlock, crash, thermal, and charging fault history
- cooling/heating hardware, pumps, valves, fans, filters/intakes, coolant leaks, and water-ingress evidence
- AC and DC charging test, achieved rate, abnormal taper/restriction, charge-port condition, and compatibility
- pack enclosure/underbody impact, corrosion, prior pack opening, repair, replacement, or salvage modules
- remaining capacity/defect warranty, threshold, expiry, transferability, exclusions, and VIN applicability
- realistic replacement, module repair, remanufactured/used-pack options, specialist access, and cost exposure

For hybrids, also assess state-of-charge swing, rapid cycling, engine start/stop quality, regenerative
braking, battery cooling intake/fan condition, inverter/e-CVT faults, and block/module deviation. A hybrid
that drives normally can still have a weak battery.

## Battery-health grade

- A — strong measured health, balanced cells/modules, clean faults, normal thermal/charging operation
- B — normal age-related degradation with credible evidence and no material warning signs
- C — meaningful degradation, imbalance, restricted charging, weak hybrid blocks, or limited warranty
- D — serious fault/symptom, severe degradation, impact/water concern, or major replacement exposure
- Unknown — evidence is inadequate; never substitute an assumed passing grade

Report **Battery health: [A/B/C/D/Unknown], evidence: [A/B/C/D]**. Explain the decisive measurement,
remaining warranty, and replacement exposure. Feed the finding into propulsion, maintenance,
repairability, value, confidence, PPI, and maximum-price judgments without double-counting it.

An Unknown grade is not proof of a bad pack, but it is a material evidence gap. Require a qualified
battery diagnostic before purchase when replacement exposure could materially change the decision.
