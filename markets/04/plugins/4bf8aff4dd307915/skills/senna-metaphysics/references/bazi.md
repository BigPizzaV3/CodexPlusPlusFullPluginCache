# BaZi workflow

## Required input

Collect all of the following before calling `senna_bazi_analyze`:

- gender as accepted by the tool;
- Gregorian birth date and local clock time;
- city and country of birth only; never ask for or pass a street, home, hospital, or other exact address;
- approximate city-center latitude and longitude only;
- historical standard UTC offset for that place and date;
- DST offset at birth, including explicit zero;
- day-boundary and southern-season options when the user requires a non-default convention.

Coordinates and time-zone history may be looked up only from a reliable source. Prefer resolving approximate city-center coordinates without asking the user to provide coordinates. If the source or historical DST rule is uncertain, disclose the uncertainty and confirm with the user before treating the chart as final.

## Interpretation rules

- Show true-solar-time correction and the resulting four pillars before interpretation.
- Keep strength, pattern, yongshen, evidence, counter-evidence, and confidence as separate concepts.
- If layered yongshen directions differ, preserve that conflict; do not collapse them into one universally favorable element.
- Treat luck cycles and annual items as thematic windows. They do not prove that marriage, divorce, illness, wealth, employment, or another concrete event will occur.
- If birth time is uncertain or close to an hour/day boundary, recommend a sensitivity comparison rather than presenting one chart as certain.

## Minimum answer shape

Provide the chart basis, core traditional interpretation, material counter-evidence, confidence meaning, and the traditional-interpretation boundary. Do not reproduce internal calculation details that are absent from the public response.
