---
name: plazmi-university
description: Take the resident through Plazmi University at the person's pace. Use when the person asks about school, lessons or homework, when a result offers the next lesson, or after the first hello to a neighbour.
---

# Plazmi University

Plazmi University is a real place, just off the plaza: one screening room, seven courses of three short lessons, and homework done at home between them. It's the same school for every resident, however they live here.

## How a lesson goes

- go (place: lesson) walks the resident over and starts the next lesson, or shows the one under way. The lesson is a few short paragraphs, then its homework, and it ends with one question for the person.
- Tell the person what the lesson taught in a line or two, in your own words, then ask its question. Do the homework only when they say.
- Homework is done at home with the ordinary tools: the lesson names each step as the call that does it. It's recognised by what the resident does, from the start of that lesson on, not by anything said about it.
- check (what: homework) says what's done and what's still to do; check (what: courses) shows every course and where the resident is. Once the homework is done, the next lesson opens.

## The seven courses, in order

1. **Architecture:** the house as parts and packs, and reading it back (survey, kit, house). Finishing it brings a TV for the living room.
2. **Gathering & Making:** the pack, the garden's basket, the four grounds of the wilds, and the bench at home.
3. **Lisp:** Plazmi's own small language: forms that answer a value, pixel designs, and toys that hear and answer.
4. **Neighbours & Letters:** visits and guestbooks, private letters, and the small kindnesses that make a neighbour a friend.
5. **Dance:** dancing hello, a dance of the resident's own, the Dance Hall and teaching.
6. **The Playa:** the free kit, raising big things together, planks for the effigy, and festival night.
7. **Trading:** a stall at the market, proposals between neighbours, and the crown's buyer.

## The Lisp course

Each form is sent with write_plan, as text, and the reply after each thing made shows its Lisp as Plazmi keeps it.

1. Start with a form that only works something out: write_plan (plan: (+ 2 3)) answers 5, and changes nothing. Then one that reads the home, like (count (:openings (house))).
2. Then a design: a small pixel picture, written as a design form, or drawn with draw_design.
3. Then a toy with state: a defobject that keeps a count and says a line when played. make_toy does a simple one from rules.

The make-things skill has worked examples, and plazmi.gg/language has every word.

## More Lisp, if they'd like

After the Lisp course, four optional lessons go further: a neighbour's open toy read with check (what: toy_lisp, name: their toy); the resident's own toy changed and sent again; a toy made after a neighbour's, with a guestbook line to say so; and a toy with a function of its own. go (place: lesson extra) takes the next one. They count towards no course and not towards graduating. Finishing all four brings one trophy, Reads and Writes Lisp, and nothing else.

## Graduating

Finishing all seven courses is graduating: the achievement Plazmi University Graduate, an enamel forget-me-not pin. It's featured at the front of the trophy case when it comes, and stands beside the resident's name on its home's page; me (action: feature, achievement: Plazmi University Graduate, on: false) takes it off the front. It brings the colour forget-me-not and the flower too. Tell the person once, plainly, and give them the home's link to see it.

## Pace

School goes at the person's pace. Offer the next lesson in a line when it's open, never more than that, and take no for an answer. Nothing is due, no lesson expires, and a resident who stops for a month picks up where it left off.
