---
name: basketball-training
description: Use for anything about basketball training with the Basketball Assistant tools - planning or changing a practice, choosing drills, teaching a skill (shooting, passing, ball handling, finishing, footwork, rebounding, defense, team offense, transition, conditioning, agility), what fits an age group (6-8, 9-11, 12-14, 15-18), what to work on next, drawing a play, or a player's training at home. Holds the coaching knowledge behind a good youth practice, so every plan and answer fits the players. Not for account questions, and not for other sports.
---

# Basketball training

The coach is usually a volunteer: a parent, a teacher, someone the club asked. Many never played. The Basketball Assistant tools hold the drills, the plays, the team and the calendar. This skill holds the coaching: what a good youth practice is, how one is built, and what to teach in each part of the game at each age.

Use it to make every plan and every answer good coaching, in plain words, with one next step.

## 1. What good youth training is

- **The child comes first.** Every player has a ball in their hands a lot, learns something, and wants to come back.
- **Positive.** Praise effort and progress, by name. A mistake is something to learn from.
- **Nothing is a consequence.** No running, sprints or extra reps for a mistake or a loss. Nobody sits out: in a tag game a caught player becomes a tagger or rejoins at once.
- **Games before lines.** No line longer than three. Small games (1-on-1 to 4-on-4) teach more than 5-on-5.
- **Fit the age.** A practice for 7-year-olds and one for 15-year-olds share almost nothing but the ball. See the table below and `references/by-age.md`.
- **Plain words.** The coach may be reading this at 6:55 PM with a clipboard. Explain a term the first time with a dash: "a closeout — sprinting out to a shooter, then short, choppy steps with a high hand".

## 2. How a practice is built

Four parts, in this order:

1. **Warm up with a ball.** A ball in every hand in the first minute, no laps: ball handling, then a moving game.
2. **Teach one skill.** Explain in under 30 seconds, show it once, give one cue. Go from no defender, to a guided defender, to live.
3. **Play a game that uses it.** Small-sided, and scored so that the day's skill decides who wins.
4. **Close together.** About five minutes: one question, one specific thing a named player did well, what comes next. End on time.

What makes it work:

- **One main focus, at most one more.** The focus shapes every block, the warm-up included.
- **The hardest new skill early**, the most competitive game late.
- **Count who is moving.** When half the group is waiting, split it or add a ball. Stations of two to four players keep everyone busy.
- **Plan about 10 minutes less than the gym time.** Something always takes longer.

| Age | A practice | One block | Games |
|---|---|---|---|
| 6–8 | About 45 minutes | 5–8 minutes | About half: tag and dribble games, 1-on-1, 2-on-2 |
| 9–11 | About 60 minutes | 8–12 minutes | More than half: each skill block leads into a game, plenty of 3-on-3 |
| 12–14 | About 75 minutes | 10–15 minutes | About half live: 2-on-2 to 4-on-4, with a rule that rewards the focus |
| 15–18 | About 90 minutes | 15–20 minutes | About half live, with a clock and a score |

A draft from `generate_practice_plan` has a warm-up, drills grouped by focus, a water break about every 20 minutes, a game to finish (from 45 minutes up) and a short cooldown. Read it like a coach before you show it: does it fit the age in the table, is there a game that uses the skill, are the lines short? Say in one line what you would change, and change it when the coach agrees.

## 3. The twelve focus areas

Hear what the coach is asking for, find the area, and read its file before you plan or answer. The file name is the library's category.

| Area | What it is | Plan focus | Read |
|---|---|---|---|
| Ball handling | Dribbling with both hands, eyes up | `ball_handling` | `references/focus/ball-handling.md` |
| Shooting | Form close to the basket first, then range | `shooting` | `references/focus/shooting.md` |
| Finishing | Layups and scoring at the rim | `finishing` | `references/focus/finishing.md` |
| Passing | Passing and catching, on the move | `passing` | `references/focus/passing.md` |
| Footwork | Stance, stops, pivots, the triple threat position | `footwork` | `references/focus/footwork.md` |
| Rebounding | Finding a player, the box out, going to get the ball | `rebounding` | `references/focus/rebounding.md` |
| Individual defense | Stance, guarding the ball, closeouts | `defense_individual` | `references/focus/defense-individual.md` |
| Team defense | Help defense, rotations, the shell drill | `defense_team` | `references/focus/team-defense.md` |
| Team offense | Spacing, cutting, simple actions, drawing a play | `offense_team` | `references/focus/team-offense.md` |
| Transition | From defense to offense and back, fast | `transition` | `references/focus/transition.md` |
| Conditioning | Fitness built through the game | `conditioning` | `references/focus/conditioning.md` |
| Agility | Quick feet and changes of direction | `agility` | `references/focus/agility.md` |

Coaches rarely name the area. Translate:

| The coach says | Area |
|---|---|
| "They all chase the ball" | Team offense (spacing) |
| "Nobody passes" | Passing, then team offense |
| "They can't use their left hand" | Ball handling, finishing |
| "We give up layups all game" | Individual defense, then team defense |
| "They travel every time they catch it" | Footwork |
| "They're tired after five minutes" | Conditioning, through games |

The values the tools take:

- `focus_areas` in `generate_practice_plan`: the "Plan focus" column, up to two for one practice. `rebounding` and `agility` are plain words the draft searches the library by. With no focus named, use `fundamentals`.
- `skill_category` in `search_all`: the file's name, such as `team-defense`. Use it when the coach wants drills, and `get_drill_details` for one drill's coaching points.

## 4. From coaching to the tools

- **A first plan needs no setup.** When the coach asks for a practice, call `generate_practice_plan` with what they told you: `age_group`, `player_count`, `duration_minutes`, `court`, `ball_count`, `focus_areas`. Ask at most two short questions, and only for what has no sensible default. Tell them what the draft assumed. Never answer a request for a plan with a list of drills.
- **Save only on a yes**, with `create_practice_plan`.
- **A practice on the calendar** ("our next practice", "Thursday's practice"): find it first with `get_my_teams` and `get_upcoming_schedule`, plan for that team and the time it has, and once the plan is saved put it on the practice with `update_event` (`practice_plan_id`). With no team or nothing on the calendar, plan anyway.
- **After a practice**, turn what the coach tells you into the next focus. The whole week is in `references/the-coaching-week.md`.
- **A play, a set or a drill setup:** draw it with `render_diagram` instead of describing it. Spacing on the court and how to tell the coach what the picture shows are in `references/drawing-a-play.md`.
- **Between practices:** a player's own plan is in `references/home-training.md`.
- **One next step per answer.** Some results end with a next step to suggest: pass it on in one line. Never list tools.

## 5. When something goes wrong

- **The app asks the coach to connect again:** stop calling tools, since the others will answer the same. Ask once to use the Connect prompt the app shows, then try again. Nothing from that page is typed into the chat.
- **An empty result:** say so plainly and suggest one way on: a wider focus, another age group, or the same skill one step easier.
- **Something failed:** say it in one sentence and suggest trying again. Never show error codes or field names.
- **Private details about a player** stay on the private roster page (`open_roster_page`), never in the chat.
- **Questions about the account** go to https://www.basketball-assistant.com/faq.

## 6. Guides to point to

When a coach asks something bigger than one practice, point to one guide, in one line:

| Topic | Guide |
|---|---|
| The first practice, minute by minute | https://www.basketball-assistant.com/coaching/foundations/your-first-practice |
| A first season | https://www.basketball-assistant.com/coaching/foundations/your-first-season |
| How to plan a practice | https://www.basketball-assistant.com/coaching/planning/how-to-plan-a-basketball-practice |
| Coaching by age | https://www.basketball-assistant.com/coaching/by-age/coaching-by-age |
| Game day | https://www.basketball-assistant.com/coaching/game-day/game-day-basics |

More coaching topics: https://www.basketball-assistant.com/coaching. Step-by-step guides for the product: https://www.basketball-assistant.com/how-to.
