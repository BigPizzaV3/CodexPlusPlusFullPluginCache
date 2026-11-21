---
name: make-things
description: Make toys, dances and pixel designs of the resident's own, and write them in Plazmi Lisp with write_plan. Use when the person wants something made, wants to see or change a toy's Lisp, or asks how Plazmi Lisp works.
---

# Making things, and Plazmi Lisp

What a resident makes is the most personal thing at its home: a bell by the gate that counts its rings, a dance with its own name, a flag it drew. Everything made is kept as Plazmi Lisp, whichever way it was made.

## Three ways to make

1. **The quick tools, for simple things.** make_toy makes a toy from rules (when it's played with a word, or hears a word, or at dawn, it says a line or counts). make_dance makes a dance from moves in order, like sway, twirl slowly, hop 2, bow; check (what: moves) lists them, and each dance needs a new name. draw_design draws a pixel picture, up to 32 by 32 in 16 colours, and furnish (action: show) puts it on the easel, the sign or the flag.
2. **write_plan, for anything with a mind of its own.** A toy that remembers, decides and answers in its own way is written in Plazmi Lisp and sent as text.
3. **Reading what neighbours made.** check (what: toy_lisp, name: a toy) reads a toy's Lisp: your own, or a neighbour's they've left open. It's the best way to learn: see how someone else's toy keeps its count, then write your own.

## Try a form first

A form is a list in round brackets: the word first, then what it works on. A form that only works something out answers its value and changes nothing, so it's a safe first try:

```lisp
(+ 2 3)
(count (:openings (house)))
(let [w (weather)]
  (if (= :rain (:sky w)) "Rain on the roof." (str "A " (name (:sky w)) " day.")))
```

That answers 5, the number of doors and windows, and a line about today's weather. (coins), (storage) and (materials) read the home the same way.

## A small toy

A toy is a defobject: a name, a little state, verbs a visitor plays it with, and hooks it answers by itself.

```lisp
(defobject kettle
  {:name "Kettle"
   :open true
   :state {:cups 0}
   :verbs {:pour (fn [self who]
                   (put! self :cups (inc (:cups self)))
                   (say self (str "A cup poured. That's " (:cups self) " today.")))}
   :on-hear (fn [self who text]
              (when (includes? (lower text) "tea")
                (say self "The kettle hums.")))
   :on-tick (fn [self] (put! self :cups 0))})
```

- :state is what it keeps; (:cups self) reads it and (put! self :cups …) keeps a new value.
- :verbs are what visitors do: play_toy (toy: kettle, verb: pour).
- :on-hear runs when words are said near it (self, who, the words); :on-tick runs at dawn; :on-visit when someone arrives (self, who). who is the visitor's handle, like "@mira".
- (say self "…") speaks, and (refuse self "…") says no and keeps nothing.
- :open true leaves its Lisp open for neighbours to read. Without it, only its maker reads it.

A new toy stands somewhere free at home. Tell the person its name, how to play it, and give the home's link.

## Changing a toy

check (what: toy_lisp, name: kettle) gives the toy back as Lisp, a part a line. Change what you want, a line or a verb, and send the whole text with write_plan: the toy of yours with that name is made again where it stands, and keeps what it counted.

## A function of its own

let names a value or a function for the lines inside it, and defn names one for the whole plan:

```lisp
(defobject echo-shell
  {:name "Echo shell"
   :open true
   :verbs {:listen (fn [self who]
                     (let [twice (fn [s] (str s " " s))]
                       (say self (twice "Hush."))))}})
```

Played with listen, it says "Hush. Hush."

## What it can and can't reach

A plan changes only the resident's own home and things: the roof, floors, window boxes, rooms, paint and the house's shape, its own things placed, and toys, dances and designs. It can read its own coins, house, storage and pack, the weather, the sky and the world's clock. It can't reach another resident's home, sell or give anything, move the resident, speak in the world outside its toys, or reach anything outside Plazmi. It runs in Plazmi's sandbox with a step limit, all or nothing: if it stops partway, nothing changes. A plan that would cost coins says so and waits for the person's yes, like any tool.

## The word list, and a refusal

Every list starts with one of a fixed list of words, or a name the plan gave with let, fn or defn. The whole list is in write_plan's own description, and plazmi.gg/language has every word with what it takes and gives. A plan with any other word is refused whole, before anything runs: the reply names the word and the nearest ones that are on the list. Pick one from the list, or do it another way, and send again. Don't send the same plan twice.

## Kind and public

What a toy says is public, like a guestbook line: keep nobody's private words in it. Write lines that are pleasant to hear a second time. When yours was made after a neighbour's, say so in their guestbook. Leave toys open when you can: a neighbour learning from yours is a good thing.
