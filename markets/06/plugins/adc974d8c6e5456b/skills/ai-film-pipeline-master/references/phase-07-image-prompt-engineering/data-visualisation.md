# Data Visualisation and Information Graphics

Designing the frame when the subject is a number. Charts, maps, counters and diagrams are the
picture on an explainer, not decoration on top of one — on a data-led piece they routinely carry
three-quarters of the runtime, and the package had beat cards saying *a chart goes here* and nothing
about how to make one.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and
the prompt written out in full.

**Two rules govern the whole file and are not repeated on every card.** First: **the numbers are
claims.** A figure comes from the brief first; otherwise search the skill and the web,
take the most suitable current figure, name its publication beside it, and record the choice under
`decisions`. The work never waits on a source. Second:
**the type is never generated.** Axis labels, figures, legends and source lines are set as an overlay
in the edit — `textimg.short_text_rule` and the Edit Overlay Rule govern, and a generated chart with
generated numbers on it is a chart with invented numbers on it.

*(Markers are defined in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set and the rule that each one closes two ways — resolved, or `unobtainable`, with what was done instead.)*

---

### Pick the Chart from the Question

**Also called:** chart choice, form follows the claim
**What it is:** Choosing the graphic from **the sentence you are trying to prove**, not from the shape of the spreadsheet. A change over time is a line. A comparison between a few things is a bar. A share of a whole is a stacked bar, almost never a pie. A relationship between two measures is a scatter. A place is a map — and only when the *place* is the point, because a map of one number per country is usually a bar chart wearing a costume.
**Effect on the audience:** They read the claim almost at once, without being taught the graphic first. The wrong form makes an audience decode before they can agree or disagree, and most of them stop at decoding.
**Used for and where it works best:** Write the sentence first — *"it fell by four-fifths and came back by half"* — then draw the smallest thing that shows it. **If the sentence has one number in it, you probably want one number on screen, not a chart.** Where two claims are fighting for one graphic, that is two graphics.
**Best in:** formats: Explainer, Documentary Feature, Heritage / Historical Documentary, News Report / Reportage, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** The data is the subject of the film and its structure is the story — then the graphic is exploratory and wants density, and this card's minimalism works against it.
**Prompt:** `[Edit Overlay Instruction]: single horizontal bar comparison, four bars, no gridlines, direct labels at the end of each bar`
**Yields to:** `dataviz.one_number_held` — The sentence carries a single number.  
`dataviz.chart_from_the_question`

---

### The Zero Baseline

**Also called:** axis truncation, the cut axis
**What it is:** A bar chart's value axis starts at zero, because a bar's **length** is the quantity — cut the axis and you have drawn a different number. A line chart may start elsewhere, because a line's **slope** is the quantity and the baseline is not carrying meaning.
**Effect on the audience:** A truncated bar axis makes a two per cent difference look like a doubling, and it works: people believe the picture over the label every time. It is the single commonest way an honest team publishes a dishonest chart.
**Used for and where it works best:** Bars from zero, always. On a line, **say what the axis covers** and let the range be whatever shows the change — then, if the change is genuinely small, that is information and the film should say so rather than the axis hiding it. Where a true zero is impossible or absurd — a temperature series, an index — use a form that does not encode length, and mark the break visibly if one is unavoidable.
**Best in:** formats: Explainer, News Report / Reportage, Corporate / Training, Documentary Feature | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** Never avoided on bars. On a line the zero baseline can flatten a real and important change into a straight line, which is its own kind of lie.
**Prompt:** `[Edit Overlay Instruction]: bar chart with the value axis beginning at zero, no axis break, gridlines at round intervals only`
**Yields to:** `dataviz.scale_choice` — True zero impossible or absurd, or it flattens the change.  
`dataviz.zero_baseline`

---

### Truncated and Logarithmic Scales, and When Each Is Honest

**Also called:** log scale, scale choice
**What it is:** A **log scale** compresses large ranges so that equal *ratios* take equal space — right for growth, contagion, orders of magnitude, anything spanning thousands. A **truncated linear scale** shows a narrow band of a large number, right when the variation within that band is the subject.
**Effect on the audience:** A log axis is honest and almost nobody reads it correctly without help; a doubling and a tenfold rise look similar. Truncation is the reverse — instantly readable and easy to over-read.
**Used for and where it works best:** If you use a log scale, **say so out loud in the narration**, and label at least three values so the spacing is visible. If you truncate, show the full range first for a beat and then push in, so the audience sees what was cut. **Either way the choice belongs in the script, not only in the chart**, because the voice is what stops the picture being misread.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage | genres: Science / Educational, Informational
**Avoid when:** A general audience meets one log chart once, in passing, with no narration supporting it. There, use a different framing — *"ten times as many"* — and keep the axis linear.
**Prompt:** `[Edit Overlay Instruction]: logarithmic value axis, labelled at 1, 10, 100 and 1000, with the scale type stated on the chart`
**Yields to:** `dataviz.memorable_number` — One log chart in passing with no narration behind it.  
`dataviz.scale_choice`

---

### One Number, Held

**Also called:** the stat card, the single figure
**What it is:** One figure alone in the frame, large, held long enough to land, with nothing competing. No chart, no axis, no second number.
**Effect on the audience:** It is the graphic form built to be remembered after the film is over, and with no competing chart marks it stays legible on a phone at arm's length.
**Used for and where it works best:** Use it for the number the film is *about*, once or twice, never five times. **The number is rounded to what a person can hold** — *four-fifths*, *nine in ten*, *half a million* — and the exact figure goes underneath in small type or into the source line. Give it a unit and a subject in the same frame, because a number alone is a number about nothing. And hold it: this is the one graphic where cutting early destroys the whole effect.
**Best in:** formats: Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Commercial / TVC, News Report / Reportage | genres: Science / Educational, Informational, Current Affairs, Heritage (civilisation-focused)
**Avoid when:** The figure needs its context to mean anything — a number that is only meaningful against another number wants a comparison, not a hero card.
**Prompt:** `[Edit Overlay Instruction]: one large figure centred in frame with a one-line subject beneath it, held for four seconds, nothing else on screen`
**Yields to:** `dataviz.chart_from_the_question` — The figure means nothing without a second one.  
`dataviz.one_number_held`

---

### The Counter That Counts

**Also called:** rolling number, count-up, odometer
**What it is:** A figure that animates from one value to another rather than cutting to it.
**Effect on the audience:** The count *is* the argument: watching a number climb for three seconds makes its size physical in a way the final frame alone does not.
**Used for and where it works best:** **Count at a speed that means something.** A counter that runs for the same two seconds regardless of the quantity says nothing; one whose speed or duration is tied to the real rate — a year per second, a death per frame — is an argument. **Ease it out at the end** so the final figure settles rather than stopping dead, and hold the settled number afterwards, because that is the frame people screenshot. On a muted feed, the motion is what stops the scroll.
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Commercial / TVC, Documentary Feature | genres: Informational, Science / Educational, Current Affairs
**Avoid when:** The subject is deaths, casualties or suffering and the counter turns a number of people into a slot machine. There, a still figure held in silence is stronger and is not in poor taste.
**Prompt:** `[Edit Overlay Instruction]: number counting up over three seconds at one year per second, easing to a stop, then held`
**Yields to:** `dataviz.one_number_held` — Deaths or suffering; hold a still figure in silence.  
`dataviz.the_counter`

---

### The Transition Is the Argument

**Also called:** animated change, before and after
**What it is:** On an animated chart, **the movement between two states carries the claim**, not either state. A shape shrinking is the loss; a line rising is the growth. The frames in between are the sentence.
**Effect on the audience:** Change seen is believed; change stated is evaluated. This is why an animated map of a shrinking marsh lands harder than two still maps side by side, even though the stills carry the same information.
**Used for and where it works best:** **Animate only the thing that changed** and hold everything else perfectly still — the axes, the labels, the coastline, the frame. One moving element reads as a fact; three read as a title sequence. Give the transition a real duration, two to four seconds, and match its shape to the real one: a gradual loss eases, a sudden collapse does not. **Show the start state before you move it**, for a beat, so there is something to compare against.
**Best in:** formats: Explainer, Documentary Feature, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** Nothing changed. Animating a static comparison is decoration, and it teaches the audience that your movement means nothing, which costs you the next transition.
**Prompt:** `[Edit Overlay Instruction]: the water area contracts over three seconds while coastline, labels and frame hold absolutely still; ease in, hard stop at the final extent`
**Yields to:** `dataviz.small_multiples_or_animate` — Nothing changed; the comparison is static.  
`dataviz.transition_is_the_argument`

---

### Colour That Carries Meaning

**Also called:** encoding colour, palette discipline
**What it is:** Using colour to encode **one** thing, and only that thing — a category, a direction, a magnitude — and leaving everything else in neutral greys.
**Effect on the audience:** They learn the code once and read every subsequent graphic instantly. A film where blue means water in one chart and means 1970 in the next has taught them nothing twice.
**Used for and where it works best:** **Grey out everything that is not the subject.** One accent colour on the thing being discussed and neutral for the rest reads faster than six colours, and it lets you move the accent from element to element as the narration moves. For magnitude, use a single hue getting darker, never a rainbow — a rainbow has no natural order and the audience invents one. For a sequence with a meaningful middle — loss and recovery, above and below — use two hues meeting at a neutral. **And carry the code across the whole film**, including into the live-action shots where you can. The accent is colour doing a job, so it must not do it alone: label the accented element directly as well (`dataviz.direct_labelling`), as `access.not_colour_alone` requires wherever colour carries meaning; the single-hue ramp already carries magnitude in lightness.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage, Corporate / Training, Museum Installation | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** The piece has one graphic and no code to teach — then colour is just design, and it should serve the brand or the film's palette instead.
**Prompt:** `[Edit Overlay Instruction]: all elements in neutral grey except the single series under discussion, which carries the accent colour and a direct label; sequential single-hue ramp for magnitude`
**Yields to:** `color.color_script` — One graphic, no code to teach; the film's palette governs.  
`dataviz.colour_encodes_one_thing`

---

### Label the Thing, Not the Key

**Also called:** direct labelling, killing the legend
**What it is:** Putting each label on or beside the element it names, instead of in a legend the viewer has to look up.
**Effect on the audience:** A legend makes the eye travel — to the key, back to the chart, back to the key — and on screen, where nobody can pause, most viewers simply do not make the trip. Direct labels remove the journey.
**Used for and where it works best:** Almost always, on screen. Put the name at the end of a line, inside or beside a bar, on the region itself. **If there are too many elements to label directly, there are too many elements**: that is the real finding, and the fix is fewer series, not smaller type. Where a legend is genuinely unavoidable, put it in reading order matching the visual order of the elements, so the eye can pair them without hunting.
**Best in:** formats: Explainer, Vertical Short-Form (Reels, Shorts, TikTok), News Report / Reportage, Documentary Feature, Museum Installation | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** A dense print or interactive graphic the audience controls and can study — there a legend is efficient and the reader has time.
**Prompt:** `[Edit Overlay Instruction]: each line labelled at its right end in its own colour, no legend anywhere in frame`
`dataviz.direct_labelling`

---

### What the Axis Says and What It Implies

**Also called:** axis honesty, the implied claim
**What it is:** Checking what the chart asserts **beyond** its data: a line drawn between two yearly points implies the years in between behaved smoothly; an axis that stops at 2003 implies nothing happened after; equal category widths imply equal importance.
**Effect on the audience:** They read the implication and not the caveat. The implication is what they repeat afterwards.
**Used for and where it works best:** Interrogate every chart with one question: *"what would someone wrongly conclude from this if they saw it with the sound off?"* Then fix the picture rather than adding a caption. **Show gaps as gaps** — a break in the line where there is no data, not a straight segment across it. **Mark where the method changed**, because a series measured two different ways is two series. And where the axis ends early, say why in the frame.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** Never avoided. The most this relaxes to is a piece whose data is illustrative rather than evidential, and that must be stated on screen rather than assumed.
**Prompt:** `[Edit Overlay Instruction]: line broken where data is absent rather than interpolated, with a small marked gap and a note of the missing years`
`dataviz.axis_implication`

---

### The Map That Changes Shape

**Also called:** area change map, shrinking map
**What it is:** A map whose **extent** changes over time — water receding and returning, a forest cut back, a city spreading, a border moving.
**Effect on the audience:** Area is the one quantity an audience reads without any training at all, which makes this the most powerful and most abusable graphic in the set.
**Used for and where it works best:** **Lock everything that is not the changing extent**: the projection, the frame, the coastline, the scale, the labels. Put a **scale bar and a date** on screen throughout, because a map without either is a picture. **Show the same extent from the same viewpoint every time** — a map that also zooms while it shrinks is unreadable as evidence. Cite the source of each extent; satellite-derived areas differ between studies and the difference is often larger than the change being shown. **And name the projection** if the area matters at continental scale, because the common web projection exaggerates high latitudes enormously.
**Best in:** formats: Explainer, Documentary Feature, Heritage / Historical Documentary, News Report / Reportage, Museum Installation | genres: Science / Educational, Informational, Current Affairs, Heritage (civilisation-focused)
**Avoid when:** The change is small enough that it is invisible at any honest scale — then the map is the wrong form and a number or a chart is the right one.
**Prompt:** `[Edit Overlay Instruction]: fixed-viewpoint map, scale bar and year visible throughout, only the water extent animating between the two dated states`
**Yields to:** `dataviz.chart_from_the_question` — The change is invisible at any honest scale.  
`dataviz.map_that_changes`

---

### Small Multiples Against One Animated Chart

**Also called:** the grid of charts, comparison layout
**What it is:** Choosing between **several small charts side by side**, which the eye compares at once, and **one chart that animates through the states**, which the eye compares across time.
**Effect on the audience:** Small multiples let an audience find the outlier themselves; animation tells them what to watch. The first is more honest, the second is stronger.
**Used for and where it works best:** On screen, animation usually wins because the frame is small and the viewer cannot study. **Use small multiples when the comparison itself is the point** — four regions where one behaved differently — and then **hold long enough to read them all**, which is longer than feels comfortable. Keep every panel on identical axes; a grid with different scales is four charts, not a comparison. If one panel is the finding, mark it with a label or a heavier frame as well as the accent, as `access.not_colour_alone` requires wherever colour carries meaning.
**Best in:** formats: Explainer, Documentary Feature, Museum Installation, Corporate / Training | genres: Science / Educational, Informational
**Avoid when:** A vertical phone frame. Small multiples do not survive it — use one chart and animate, or split across cuts.
**Prompt:** `[Edit Overlay Instruction]: four small charts in a 2x2 grid on identical axes, the outlier panel directly labelled and outlined with a heavier border as well as accented, held eight seconds, distinction intact in greyscale`
**Yields to:** `dataviz.transition_is_the_argument` — A vertical phone frame kills the grid.  
`dataviz.small_multiples_or_animate`

---

### How Long a Graphic Must Stay Up

**Also called:** reading time, chart dwell
**What it is:** The minimum time a chart needs on screen before it can be cut away from — and it is far longer than a picture needs.
**Effect on the audience:** A graphic cut too early is worse than no graphic: the audience registers that something was being explained and that they missed it, and they carry that irritation into the next sequence.
**Used for and where it works best:** **Count the elements that must be read** — a title, an axis, three labels, a figure — and give each of them time, then add the time to understand the relationship between them. As a starting point, not a measured figure, a simple bar comparison wants three to four seconds, a line chart with two series five to six, a map with a changing extent the length of the transition plus two seconds at each end. **Then measure it**: run a timed cold read at the delivery size with viewers who have not seen the chart, and end the hold only after the slower of them can state the relationship it shows. **Then read it aloud against the narration**, because the narration is what tells the eye where to look, and a chart is only on screen long enough if the words have finished pointing at it. Record the measured hold in the edit handoff; where a graphic genuinely needs longer than the script allows, simplify it and test again, or it is too complex for this film.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** The graphic is atmosphere rather than information — a background of moving figures behind a title — where nobody is meant to read it and dwell does not apply. Say which it is.
**Prompt:** `not a prompt line but a timing, to be checked by reading it aloud against the narration: hold the two-series line chart for six seconds, the last two with no new narration over it`
`dataviz.reading_time`

---

### Uncertainty on Screen

**Also called:** error bars, the range, showing what is not known
**What it is:** Showing that a figure is a range, an estimate or a disputed value, rather than drawing it as a fact.
**Effect on the audience:** Correctly done it increases trust rather than weakening the claim — an audience that sees a range believes the midpoint more than an audience shown a bare number.
**Used for and where it works best:** **Where the sources disagree, show the disagreement**: two bars, two lines, a band. Where a figure is an estimate, a band or a softened edge says so without a caption. Where one widely repeated number is wrong, **the strongest move is to cut it rather than to soften it** — a film that shows a bad figure and then qualifies it has still put the bad figure on screen, and that is the one people remember. In narration, *"between a half and four-fifths, depending on who measured"* is a sentence an audience can hold, and it is more honest than a false precision.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** Every figure in the piece carries a band and the screen becomes a fog. Choose the two or three where the uncertainty is material to the argument.
**Prompt:** `[Edit Overlay Instruction]: shaded band between the low and high estimate with the midpoint line accented, both bounds labelled`
`dataviz.uncertainty_shown`

---

### The Source Line

**Also called:** attribution, the credit under the chart
**What it is:** A small line under every graphic naming where the numbers came from and when.
**Effect on the audience:** Almost nobody reads it, and its absence is noticed by exactly the people whose objection costs most. It is also the only thing that lets a viewer check you.
**Used for and where it works best:** Name the **publication and the year**, not a website. Where a figure is derived — a percentage you computed from two published numbers — say so, because that is your claim rather than theirs. Keep it small and legible rather than tiny; set it as overlay type with the rest. **And put it on screen at the same time as the figure**, not in the end credits, because a figure and its source separated by nine minutes are not connected in anyone's mind. Where no publication was found, the line names what the figure rests on (the brief, the company, the period) and the choice is recorded under `decisions`.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage, Museum Installation, Corporate / Training | genres: Science / Educational, Informational, Current Affairs, Heritage (civilisation-focused)
**Avoid when:** A brand or promotional piece using its own internal figures — there the honest line names the company and the period, which is a different sentence and still belongs on screen.
**Prompt:** `[Edit Overlay Instruction]: source line set small beneath the chart, naming publication and year, present for as long as the figure is`
`dataviz.source_line`

---

### The Number the Audience Remembers

**Also called:** rounding, the memorable figure
**What it is:** Deciding which form of a figure goes in the narration and on screen — the precise one, or the one a person can carry.
**Effect on the audience:** *"Eighty-five and a half per cent"* is forgotten almost at once; *"more than four-fifths"* is repeated at dinner. Precision that nobody can hold is precision spent on nobody.
**Used for and where it works best:** **Say the round one, show the precise one.** The narration carries the fraction or the plain comparison; the screen carries the exact figure and the source. The exception is the number the film is about, held alone as a hero card: there the round form goes up large and the exact one sits small beneath it (`dataviz.one_number_held`). That way the piece is quotable and checkable at once, and neither audience is short-changed. **Round toward the claim's weaker side**, never the stronger — if the figure is 85.5%, *"more than four-fifths"* is safe and *"nearly ninety per cent"* is not. And pick one form and keep it: a film that says four-fifths, then 85%, then most, has three different claims in the audience's memory.
**Best in:** formats: Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, News Report / Reportage | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** The precise figure *is* the story — a record, a threshold crossed, a legal limit — where rounding destroys the point.
**Prompt:** `not a prompt line but a writing rule: narration carries the round figure, the frame carries the exact one and its source, except on a held hero number, where the round figure is large and the exact one small beneath it`
`dataviz.memorable_number`

---

### The Graphic That Works Muted and Paused

**Also called:** the silent read, screenshot test
**What it is:** Designing the chart so that it still says its one thing with the sound off, and so that any frame someone pauses on is complete.
**Effect on the audience:** Most feed viewing is muted, and the most-shared artefact of any explainer is a screenshot of one frame. A chart that needs the narration to make sense reaches a fraction of its audience.
**Used for and where it works best:** **Put the claim in the frame as a short title** — not a chart title like *"Marsh extent 1970–2025"* but the sentence, *"Four-fifths of it was gone by 2001"*. Then the graphic supports a statement rather than posing a question. **Test by pausing at three random moments**: each frame should have a subject, a unit and a source. On vertical, that title goes in the safe band and the type is sized by `textimg.subtitle_size_in_frame`.
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Explainer, News Report / Reportage, Thumbnail / Social Card | genres: Informational, Science / Educational, Current Affairs
**Avoid when:** A cinema or gallery piece watched whole with sound, where a claim stamped on every graphic becomes hectoring and the narration can carry it instead.
**Prompt:** `[Edit Overlay Instruction]: the claim set as a short sentence above the chart, subject unit and source present in every frame, legible with sound off`
`dataviz.works_muted_and_paused`

---

### Build the Chart, Do Not Generate It

**Also called:** the generated-chart trap
**What it is:** **A generative image model cannot draw a correct chart.** It produces something chart-shaped with invented tick values, mislabelled axes, bars whose lengths do not match their numbers and text that is nearly words. It looks right at a glance and is wrong in every particular.
**Effect on the audience:** On a piece whose credibility rests on its figures, one fabricated axis destroys the whole film's authority — and the people who notice are exactly the people it was made to convince.
**Used for and where it works best:** **Generate the environment, build the data.** Use the image engine for what it is good at — the marsh, the trench, the sky behind the graphic, a textured background plate, a physical object standing in for a quantity — and construct every chart, axis, label and figure as a **vector or motion-graphics layer in the edit**, from the real numbers. Where a prompt must describe a frame that will carry a chart, describe the **clean plate**: the empty space, its tone, its contrast, sized for the graphic that will sit in it. This is the same rule `textimg.short_text_rule` and `textimg.non_latin_script` state for lettering, and on data it is absolute rather than a preference.
**Best in:** formats: Explainer, Documentary Feature, News Report / Reportage, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Science / Educational, Informational, Current Affairs
**Avoid when:** The "chart" is deliberately fictional set dressing — a control room screen in a drama, an invented readout — where nobody will read the values and accuracy is not claimed. Say which it is in the prompt.
**Prompt:** `wide clean plate of the marsh at dawn, the left third held quiet and low-contrast with no detail, sized to carry a chart added in the edit; no text, no graphics, no numbers in the generated frame`
`dataviz.build_do_not_generate`
