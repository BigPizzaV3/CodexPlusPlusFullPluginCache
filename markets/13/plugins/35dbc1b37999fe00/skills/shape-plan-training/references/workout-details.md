# Structured intervals and swim workouts

Use the live tool schema for accepted fields. The examples below illustrate payloads, not permission to save a workout or a suggested training prescription.

## Step structure

A regular step needs `stepType`, `displayName` and `endCondition`. Step types include `warmup`, `interval`, `recovery` and `cooldown`. End conditions and intensity targets are separate:

- For `endCondition: "distance"`, `endConditionValue` is meters.
- For `endCondition: "time"`, `endConditionValue` is seconds.
- `"lap.button"` and `"open"` do not need a duration/distance value.
- A repeated block uses `stepType: "repeat"`, `numberOfIterations` and `workoutSteps`. The count is the total number of repetitions: 5×400 m means 5, not 4. Children are regular steps; do not nest another repeat group.
- Use `skipLastRestStep: true` only when the final recovery is intentionally omitted. Include warmup, recoveries and cooldown when calculating totals and load.

## Target units

| `targetType` | `targetValueOne` / `targetValueTwo` units |
| --- | --- |
| `pace` | Seconds per kilometer; smaller is faster |
| `speed` | Meters per second |
| `heart.rate` | Beats per minute |
| `power` | Watts |
| `cadence` | Revolutions or steps per minute for the sport |

For a pace range, the first bound is faster and the second is slower. A 4:00–4:15/km range is 240–255. Never put an interval's distance or duration in these target fields. Use `zoneNumber` as an alternative when the user asks for a training zone; do not invent numerical bounds without their thresholds. Secondary targets use the units of `secondaryTargetType`, independent of the primary target.

Example repeat group for five 400 m intervals at 4:00/km, each followed by 90 seconds recovery:

```json
{
  "stepType": "repeat",
  "numberOfIterations": 5,
  "workoutSteps": [
    {
      "stepType": "interval",
      "displayName": "400 m",
      "endCondition": "distance",
      "endConditionValue": 400,
      "targetType": "pace",
      "targetValueOne": 240,
      "targetValueTwo": 240
    },
    {
      "stepType": "recovery",
      "displayName": "Recovery",
      "endCondition": "time",
      "endConditionValue": 90,
      "targetType": "no.target"
    }
  ]
}
```

## Swimming

Swim pace targets also use seconds per kilometer. Multiply the athlete's seconds per 100 m by 10: 2:00/100 m is 1200, not 120. Keep their preferred per-100 m pace when explaining the workout.

- Set `poolLength` when the user names it: `25m`, `50m`, `33m`, `20m`, `25yd` or `any`. Omit it when not specified so their saved pool setting can apply. A yard pool does not change distance-field units; convert yard distances to meters.
- Set `swimDrill` to `drill`, `kick` or `pull` on every corresponding step. A drill name in `displayName` alone will not communicate this to the watch.
- Set `swimStroke` on steps with a named stroke: `freestyle`, `backstroke`, `breaststroke`, `butterfly`, `im`, `rimo`, `mixed` or `choice`.
- `swimEquipment` is one value: `fins`, `kickboard`, `paddles`, `pull_buoy` or `snorkel`. For several pieces of equipment, use the piece the set is built around: a pull buoy for pull with buoy and paddles, a kickboard for kick sets, otherwise the first named piece.

Example regular step for a 200 m freestyle pull set using a pull buoy:

```json
{
  "stepType": "interval",
  "displayName": "Freestyle pull",
  "endCondition": "distance",
  "endConditionValue": 200,
  "targetType": "no.target",
  "swimStroke": "freestyle",
  "swimDrill": "pull",
  "swimEquipment": "pull_buoy"
}
```
