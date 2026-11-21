# Example tunes

Original tunes, free to use and to change. Each one passes
`scripts/tune.py check` (the tests check every block below). Send the text
as the alarm's `tune`, comments included if you like.

## Sunrise — gentle, no drums

A slow melody over a plucked arpeggio and a soft bass. 8 bars, 20 s at 96.

```mml
; 4 beats per bar, 8 bars
A t96 o5 l4 v11 @1 e2 g a | g2. e | d e g e | d1 | e2 g a | b2. a | g a b >d< | c1
B o4 l8 v7 @0 s2 [c e g e]4 [d g b g]4 [c e g e]2 [e g b g]2 [d g b g]2 [c e g e]2
C o3 l2 v13 @0 q6 c g c g d g d g c g e b d g c g
```

## Morning march — all four channels

Brisk, bright, with drums. 4 bars, 7 s at 132.

```mml
A t132 o5 l8 v12 @2 q5 c c e g >c4< g4 | a4 g e f4 d4 | e e g >c< b a g f | e4 d4 c2
B o4 l8 v8 @1 q4 [r e r g]2 | r f r a r d r g | [r e r g]2 | r f r g r e r c
C o3 l4 v13 @0 q6 c g c g | f c g d | c g c g | g d c c
D l8 [v13 s2 o2 c v5 s1 o7 c v10 s2 o5 c v5 s1 o7 c]8
```

## Birdsong — sparse and high

Short chirps with long pauses: wakes you gently, doesn't nag. 2 bars, 4 s.

```mml
A t120 o6 l16 v10 @0 s1 q4 g >c< r8 r4 r2 | r2 e g e r r4
B o5 l16 v7 @1 s1 q4 r1 | r4 b >d< r8 r2
```

## Korobeiniki swing — jazz, all four channels

The Tetris melody (a Russian folk song, public domain) with swung eighths
written as `6`+`12` triplet pairs, Charleston piano stabs, a walking bass and
brushed drums. 8 bars, 13 s at 144. Played on a PhotoPainter on 2026-09-26.

```mml
; Korobeiniki Swing: a jazz take on the Tetris tune (Russian folk song, public domain).
; A minor, 8 bars of 4 beats, swung eighths written as 6+12 triplet pairs.
; Chords: Am7 | Am7 | E7 | Am7 | Dm9 | Am7 | Bm7b5 E7 | Am6
A t144 o5 l4 v12 @1 q6 e4 o4 b6 o5 c12 d4 c6 o4 b12 | o4 a4 a6 o5 c12 e4 d6 c12
A o4 b4&b6 o5 c12 d4 e4 | o5 c4 o4 a4 a2
A o5 r6 d4 f12 a4 g6 f12 | o5 e4&e6 c12 e4 d6 c12
A o4 b4 b6 o5 c12 d4 e4 | o5 c4 o4 a4 a6 o5 c12 e-6 e12
; Piano comping: Charleston rhythm on the 3rd and 7th of each chord.
B o5 v7 @2 s3 q8 c4. o4 g8 r2 | o4 g4. o5 c8 r2 | o4 g+4. d8 r2 | o5 c4. o4 g8 r2
B o4 f4. o5 c8 r2 | o5 c4. o4 g8 r2 | o4 a4. g+8 r2 | o4 f+4. o5 c8 r2
; Walking bass, kept at o3 and up for the small speaker.
C o3 v13 @0 q6 l4 a o4 c e g | o4 a g e c | o3 b o4 d e g+ | o4 a e c c+
C o4 d f a f | o4 e c o3 a o4 c | o3 b o4 d e g+ | o4 a f+ e o3 e
; Drums: soft kick on 1, swung hat on 2 and 4, ride on 3.
D [@0 o2 v10 s2 c4 @1 o7 v5 s1 c6 v3 c12 o6 v5 s3 c4 o7 v5 s1 c6 v3 c12]8
```

## Ringtone — one channel

The simplest form, like a phone ringtone. 2 bars, 3.4 s at 140.

```mml
A t140 o5 l8 v13 @2 c e g >c< g e c r | d f a >d< a f d r
```
