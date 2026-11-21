# Drawing a play

A picture beats a paragraph. When a coach describes a play, a set or a drill setup, draw it with `render_diagram` instead of describing it. The tool's own description holds the grammar of a diagram. This page is about what makes the picture good coaching.

## Before you draw

- **One idea per diagram:** an action the team can run on Saturday, or one drill setup.
- **Fit the age.** For 6–8, draw where players stand and one "pass, then go". For 9–11, one simple set and one inbounds play. From 12, two or three sets built on the same habits. See `references/by-age.md`.
- **Use the coach's own names** for the play, and the numbers 1 to 5 for the players.
- **At most one question**, and only when the description leaves the start open: "Where does the ball start?"

## Spacing on the court

Players stand on spots. Outside: the top, the slots, the wings, the deep wings and the corners. Inside: the elbows, the blocks and the dunker spots — beside the lane, close to the baseline.

- `spacing` moves the outside spots: `tight` for the youngest, who stand nearer the basket, `standard`, and `wide` for older players who shoot from farther out.
- Turn the space advisor on for a half-court play or a team drill: `space_advisor: true` uses the team's level. Leave it off when the coach says no.

| Level | The picture shows |
|---|---|
| `beginner` | The spots, taken and open, and a red ring round a player who stops in the lava |
| `intermediate` | Also the ball handler's open driving lanes, a red mark where a cut runs into a teammate, and the room after a screen or a handoff, or on a cut to the basket |
| `advanced` | Also an open lane for every player without the ball whose path to the basket is clear, the lava drawn as an area, and the help area when a defense is drawn |

The lava is the middle ground: inside the 3-point line, outside the lane. A player who stands there brings a defender into everyone else's driving room.

## Spot setups

A play has one spot setup. It decides which spots the picture rings as open, and where a player in the lava is sent.

| Setup | `spot_setup` | The spots |
|---|---|---|
| 5-out | Leave it out | The top or the slots, the wings and the corners. The dunker spots are open for a cutter |
| 4-out 1-in | `4_out_1_in` | The two slots and the two deep wings — between the corner and the wing, about 4.5 meters from the baseline. The dunker spots are for the player inside |

- Use 4-out 1-in when the coach describes four players outside and one inside, or names the deep wings.
- A play that starts with a player in the post and resets to five around the arc is still a 5-out.
- One setup for the whole play. Say which one you used, in a few words, so the coach can change it.

## Telling the coach what the picture shows

The findings in a result are for you. Say what matters in plain words: which player, which step, what to change. Then ask whether to fix it. Never quote rule names or field paths.

| The result says | Tell the coach |
|---|---|
| A player ends a step in the lava | "3 stops in the lava after the cut. Send 3 out to the open corner?" The result names an open spot |
| Two players stand too close | "2 and 4 are close enough for one defender to guard both. Move 4 to the corner?" |
| A cut runs into a teammate | "1's cut ends where 5 is standing. Clear 5 out first, or cut the other way?" |
| There is room after a screen or a handoff, or on a cut to the basket | Good news. Say who is open, and when the pass should come |

A stop the coach means, such as a post-up, is fine. Keep it when they say so (`allow_lava` on that player or that move), and don't raise it again.

## Steps, options and defense

- The setup is where everyone starts. Each step is one beat: a pass, a cut, a screen. Two or three actions per step are plenty.
- A read with two answers becomes two options from the same step. Name what the player reads: "X2 overplays: go backdoor."
- Draw the defense when the play is about beating it. On the page the coach shares, defenders stand where each step starts. Their lines show only when the coach asks for them (`defense_paths`).

## Keeping and sharing it

1. `save_diagram` once the coach likes it.
2. `share_diagram` gives a link to send the team. A diagram has to be saved first.
3. Change a saved diagram with `update_diagram` and the revision you read (`expected_revision`), so a newer version is never overwritten.

`list_my_diagrams` shows the coach's diagrams and a few starter plays to begin from. A play from the library opens with `get_play_details`.
