# Ads, Trailers and Motion Design

59 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Whose Camera Is This Meant To Be

**Also called:** the advert selector, the promo fork, who is apparently speaking  
**What it is:** The card at the head of the `promo.` shelf. It describes no shot. It asks the three questions the shelf's own pair graph asks over and over — **whose camera the viewer is meant to think this is, whether the piece has to survive being checked, and whether it owns its frame or is a guest in somebody's feed** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the shelf's `Yields to:` conditions, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the shot which does reach the screen was chosen against the product, the claim and the platform, rather than picked because it was the last advert the writer watched.  
**Used for and where it works best:** Answer the three questions **in order and out loud, one sentence each, before you open the shelf**. Answer one eliminates roughly two-thirds of the file in a single stroke, because the shelf's largest fault line runs straight down it. Answers two and three leave a shortlist of three to six. If you cannot answer question one you are not choosing a shot, you are still writing the brief. Where the honest answer to question one is *both* — a brand-built piece delivered in a creator's voice — that is two pieces, not one, and the two will fight in the same cut.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Corporate / Training | genres: all  
**Avoid when:** **The piece has no product and no title to sell.** This shelf assumes something is being offered, and a map built on *whose camera* has nothing to say about a film that is only itself. Also **distrust this map on any 9:16 delivery**, which is now the honest answer to axis three for most of the shelf: there it hands you cards written for a slot the piece no longer has, and it hands several of them the same position in the frame at the same moment without noticing. **On a 9:16 delivery, use this map to choose the shot and take its position in the frame and its timing from the vertical shelf** ([`vertical-short-form.md`](vertical-short-form.md)), with the band figures on `vertical.safe_zones`. And **distrust the whole map on any platform figure.** Few cards on this shelf carry a `**Shelf life:**` line, so most of it does not date itself, and a shelf whose cards cannot go stale is a shelf that will quietly go wrong; where a number about somebody else's product is needed, `vertical.safe_zones` owns it and this map only points.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Whose camera is the viewer meant to think this is?**
Asked first, because it is the condition the shelf repeats most and the only one that cuts the file in three. Sixteen `Yields to:` lines turn on it and they are stated as facts about the product, not feelings about the viewer: *"Creator ad where a lit plinth reads as advertising"* (`promo.demo_shot`), *"Staged opening reads as an ad, honesty is the point"* (`promo.unboxing`), *"Premium product the phone look would cheapen"* (`promo.ugc_talking_head`), *"Premium brand the unpolished look would cheapen"* (`promo.ugc_phone_look`), *"Broadcast spot where the lit demonstration is right"* (`promo.ugc_product_in_hand`), *"Polished aspiration reads as stock footage"* (`promo.lifestyle_broll`), *"The composed frame makes the testimony look manufactured"* (`promo.testimonial_frame`), *"Real use proves more than designed motion"* (`promo.ui_animation`), *"Creator piece where close sound replaces the signature"* (`promo.product_sound`). The third value is not a tier of polish at all: it is the register in which nobody on this shelf shot anything, because the material already exists and the piece is an arrangement of it.

**Axis 2 — Does this have to be believed, or only wanted?**
Ten conditions turn on whether a fact about the world has to hold before the card will work: *"No press yet; proof comes from a customer"* (`promo.critic_quote`), *"No real objection exists to answer"* (`promo.ugc_reply_comment`), *"No genuine mistake to confess"* (`promo.ugc_mistake_hook`), *"It is not genuinely the first time"* (`promo.ugc_first_use_reaction`), *"Product not yet circulating; the first try is the content"* (`promo.ugc_made_me_buy`), *"The cut invites doubt, proof must be uncut"* (`promo.problem_solution`), *"Comparison against a rival is not legally safe"* (`promo.ugc_split_compare`), *"The result shows in one take; a month is not needed"* (`promo.ugc_thirty_days`), *"Existing lines cannot honestly carry the story"* (`promo.dialogue_as_narration`). Their `Avoid when:` lines agree and go further — they are about **exposure**, not taste: *an invented quote has no defence*, *any change voids the proof*, *people recognise how real comments read*, *claim only what the footage itself shows*. The third value, *withheld*, is the reverse condition: the piece's whole job is to refuse, and its `Avoid when:` lines are about spending too early — *spends the curiosity before the story*, *makes the rest descend instead of climb*, *do not explain anything in a teaser*.

**Axis 3 — Does the piece own its frame, or is it a guest in somebody's feed?**
Eight conditions are about the delivery and nothing else: *"Vertical or very short, no room for three movements"* (`promo.three_act_trailer`), *"Vertical, where long silence reads as a broken video"* (`promo.silence_drop`), *"Vertical, where repeated black reads as playback fault"* (`promo.black_frame_punch`), *"Vertical reel, sign-off from inside the last live shot"* (`promo.end_card`), *"Short ad where the build steals the time"* (`promo.logo_animation`), *"A story that cannot be understood in six seconds"* and its exact reverse in `promo.cutdown_15s`, and `promo.super`, whose whole pair field is an authority yield to `vertical.safe_zones` *on any 9:16 delivery*. It is asked last because it does not change what the piece is — it changes who else has already claimed the frame, and that is where the shelf's two unsettled disputes live.

---

**The map**

**Axis 1 — whose camera**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The brand's — built, lit, composed, and not pretending otherwise** (twenty-five) | `promo.hero_shot` · `promo.product_reveal` · `promo.macro_texture` · `promo.pour_splash` · `promo.levitation` · `promo.problem_solution` · `promo.before_after_wipe` · `promo.demo_shot` · `promo.usage_reaction` · `promo.unboxing` · `promo.pack_shot` · `promo.logo_sting` · `promo.end_card` · `promo.logo_animation` · `promo.shape_wipes` · `promo.bumper_6s` · `promo.cutdown_15s` · `promo.product_match_cut` · `promo.product_sound` · `promo.lifestyle_broll` · `promo.testimonial_frame` · `promo.super` · `promo.kinetic_typography` · `promo.ui_animation` · `promo.audio_hit_sync` |
| **A customer's or a creator's — first person, and looking produced is the failure** (twenty-six) | `promo.ugc_talking_head` · `promo.ugc_unboxing` · `promo.ugc_grwm` · `promo.ugc_product_in_hand` · `promo.ugc_pov_format` · `promo.ugc_text_hook_face` · `promo.ugc_mistake_hook` · `promo.ugc_three_reasons` · `promo.ugc_hook_demo_cta` · `promo.ugc_made_me_buy` · `promo.ugc_reply_comment` · `promo.ugc_duet_stitch_brand` · `promo.ugc_before_after_oner` · `promo.ugc_phone_look` · `promo.ugc_single_take_testimonial` · `promo.ugc_day_in_life` · `promo.ugc_greenscreen_page` · `promo.ugc_founder_piece` · `promo.ugc_first_use_reaction` · `promo.ugc_stop_scrolling` · `promo.ugc_end_cta_offer` · `promo.ugc_thirty_days` · `promo.ugc_screen_recording` · `promo.ugc_asmr_closeup` · `promo.ugc_caption_carries` · `promo.ugc_split_compare` |
| **Nobody's — the piece is cut from footage that already exists** (nineteen) | `promo.three_act_trailer` · `promo.trailer_rise` · `promo.silence_drop` · `promo.quick_cut_montage` · `promo.ramping_cut_rate` · `promo.black_frame_punch` · `promo.stutter_rewind` · `promo.title_cards` · `promo.one_line_over_montage` · `promo.dialogue_as_narration` · `promo.money_shot` · `promo.character_card` · `promo.teaser_image_date` · `promo.date_card` · `promo.credit_block` · `promo.critic_quote` · `promo.end_tag` · `promo.braaam` · `promo.trailer_voice` |

**Axis 2 — believed, withheld, or only wanted**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Believed — a claim is being made and somebody can check it** (twenty-four) | `promo.problem_solution` · `promo.before_after_wipe` · `promo.demo_shot` · `promo.usage_reaction` · `promo.ui_animation` · `promo.testimonial_frame` · `promo.critic_quote` · `promo.credit_block` · `promo.dialogue_as_narration` · `promo.ugc_before_after_oner` · `promo.ugc_split_compare` · `promo.ugc_thirty_days` · `promo.ugc_screen_recording` · `promo.ugc_single_take_testimonial` · `promo.ugc_founder_piece` · `promo.ugc_first_use_reaction` · `promo.ugc_made_me_buy` · `promo.ugc_reply_comment` · `promo.ugc_mistake_hook` · `promo.ugc_three_reasons` · `promo.ugc_talking_head` · `promo.ugc_day_in_life` · `promo.ugc_grwm` · `promo.ugc_phone_look` |
| **Withheld — the piece promises and then refuses** (twenty-three) | `promo.product_reveal` · `promo.unboxing` · `promo.ugc_unboxing` · `promo.teaser_image_date` · `promo.money_shot` · `promo.three_act_trailer` · `promo.trailer_rise` · `promo.silence_drop` · `promo.braaam` · `promo.black_frame_punch` · `promo.stutter_rewind` · `promo.quick_cut_montage` · `promo.ramping_cut_rate` · `promo.title_cards` · `promo.one_line_over_montage` · `promo.character_card` · `promo.date_card` · `promo.end_tag` · `promo.trailer_voice` · `promo.ugc_stop_scrolling` · `promo.ugc_pov_format` · `promo.ugc_text_hook_face` · `promo.ugc_hook_demo_cta` |
| **Wanted — nothing is asserted, the thing is simply made attractive** (twenty-three) | `promo.hero_shot` · `promo.macro_texture` · `promo.pour_splash` · `promo.levitation` · `promo.pack_shot` · `promo.product_match_cut` · `promo.product_sound` · `promo.lifestyle_broll` · `promo.logo_sting` · `promo.logo_animation` · `promo.shape_wipes` · `promo.super` · `promo.kinetic_typography` · `promo.audio_hit_sync` · `promo.bumper_6s` · `promo.cutdown_15s` · `promo.end_card` · `promo.ugc_end_cta_offer` · `promo.ugc_asmr_closeup` · `promo.ugc_caption_carries` · `promo.ugc_product_in_hand` · `promo.ugc_greenscreen_page` · `promo.ugc_duet_stitch_brand` |

**Axis 3 — owns the frame, or a guest in it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A guest — 9:16, a scroll, an interface that already owns bands of the frame** (twenty-nine) | `promo.ugc_talking_head` · `promo.ugc_unboxing` · `promo.ugc_grwm` · `promo.ugc_product_in_hand` · `promo.ugc_pov_format` · `promo.ugc_text_hook_face` · `promo.ugc_mistake_hook` · `promo.ugc_three_reasons` · `promo.ugc_hook_demo_cta` · `promo.ugc_made_me_buy` · `promo.ugc_reply_comment` · `promo.ugc_duet_stitch_brand` · `promo.ugc_before_after_oner` · `promo.ugc_phone_look` · `promo.ugc_single_take_testimonial` · `promo.ugc_day_in_life` · `promo.ugc_greenscreen_page` · `promo.ugc_founder_piece` · `promo.ugc_first_use_reaction` · `promo.ugc_stop_scrolling` · `promo.ugc_end_cta_offer` · `promo.ugc_thirty_days` · `promo.ugc_screen_recording` · `promo.ugc_asmr_closeup` · `promo.ugc_caption_carries` · `promo.ugc_split_compare` · `promo.bumper_6s` · `promo.teaser_image_date` · `promo.super` |
| **It owns the frame — a slot, a screen, a cinema, a page** (forty-one) | Every other card named in the two tables above. It is named by complement on purpose: listing forty-one ids here would make the map longer than the shelf, which is the one thing the template forbids. |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally three to six cards wide.*

**Two disputes this map reaches and does not settle.** Both fire only under axis three's first value, and neither has a row in `COLLISIONS.md`.

**The last frame of a vertical reel is claimed four times.** `promo.end_card` describes the final static frame and then, in its own `Avoid when:`, rules itself out on a vertical reel in favour of the logo sitting on the last live shot. `promo.pack_shot` places itself *at the end, just before or with the end card*, and sets its own hold. `promo.date_card` calls itself *a final or near final card*. `vertical.end_cta` gives the last seconds to a single spoken and written request, and to audio alone if the piece loops. `promo.ramping_cut_rate` hands the final frame to `promo.end_card` on a commissioned advert, and `promo.ugc_end_cta_offer` hands it back. **Four cards, one frame, four different holds, and each is right on its own page.** Take the answer from the brief, not from this map.

**The upper band of the 9:16 frame is claimed three times.** `vertical.eyes_upper_third` puts the eyeline there as the working rule for every talking head. `vertical.caption_bar` puts a permanent series band at the top and keeps it there for the whole piece. `vertical.safe_zones` says the top band belongs to the platform's interface and owns the only figures in the package for it. `promo.super` yields its own position outward to that card on any 9:16 delivery, which is the correct behaviour and the only card here that performs it. **Nothing routes any of the other three to each other.** Read `vertical.safe_zones` before you place anything, take the figure from the platform's own current page as that card itself instructs, and do not take a number from any other card — its `**Shelf life:**` line records that these figures have already been wrong once and that other files copied the error.

---

**The default, and the one against it**

**The default is `promo.testimonial_frame` — a composed frame of one person saying it happened — and it is measured, not asserted.** It is the most-yielded-to card on the shelf, and unlike the runners-up its inbound edges do not collapse. Four cards send a reader here and they send them for four different reasons: `promo.ugc_talking_head` (*"Premium product the phone look would cheapen"*), `promo.critic_quote` (*"No press yet; proof comes from a customer"*), `promo.ugc_single_take_testimonial` (*"The framing, not the absence of cuts, does the work"*) and `promo.ugc_founder_piece` (*"Founder cannot speak unscripted; use a composed frame"*). Product tier, absent press, the device being wrong, and a speaker who cannot perform — four unrelated failures, one destination. That is a fallback.

**The obvious pick is not it, and the shelf says so.** The card a writer reaches for first on an advert shelf is `promo.hero_shot`, and it is yielded to twice, on what is really one condition wearing two coats — `promo.levitation` (*"Heavy or humble product where floating looks artificial"*) and `promo.ugc_phone_look` (*"Premium brand the unpolished look would cheapen"*). Both say *the other card is wrong for this product's tier*. The hero shot is where the shelf goes when something else was too much or too little, not where it goes when it is right. Two other cards look like defaults and are not: `promo.ugc_asmr_closeup` takes three edges and all three say the same thing — *close sound is doing the work the picture was doing* — which makes it a sound escape hatch; and `promo.end_card` takes three edges that all say *a designed sign-off frame is contractually required*, which makes it a format escape hatch and is exactly why it sits in the middle of the dispute above.

**The one against it is `promo.ugc_reply_comment`.** Nothing routes to it; it is named by no `Yields to:` on the shelf; and it is the only card here where **the advert is authored by somebody who is not selling anything.** Every other card on this shelf decides what to say and then finds a way to say it. This one waits until the market has said something, and then answers the hardest thing it said. Its own `Avoid when:` refuses both cheats that would make it easy — *do not invent a comment*, and *do not pick an easy objection: the hard one is what sells, because it removes the last barrier* — which means the card cannot be used without conceding that the objection is real. Its only stated cost is that a real objection must exist, which a piece with any audience at all already has. **Its near cousin against the grain is `promo.teaser_image_date`**, likewise never yielded to, and the only card on the shelf that sells by refusing to show anything at all.

---

**The unasked**

**Thirty-four of the seventy reachable cards are the target of no `Yields to:` field anywhere on this shelf.** They can be chosen but nothing ever sends you to them. By id:

`promo.audio_hit_sync` · `promo.character_card` · `promo.credit_block` · `promo.critic_quote` · `promo.date_card` · `promo.kinetic_typography` · `promo.levitation` · `promo.lifestyle_broll` · `promo.one_line_over_montage` · `promo.pack_shot` · `promo.pour_splash` · `promo.problem_solution` · `promo.product_match_cut` · `promo.product_reveal` · `promo.quick_cut_montage` · `promo.ramping_cut_rate` · `promo.stutter_rewind` · `promo.super` · `promo.teaser_image_date` · `promo.ugc_caption_carries` · `promo.ugc_duet_stitch_brand` · `promo.ugc_founder_piece` · `promo.ugc_greenscreen_page` · `promo.ugc_hook_demo_cta` · `promo.ugc_made_me_buy` · `promo.ugc_mistake_hook` · `promo.ugc_phone_look` · `promo.ugc_reply_comment` · `promo.ugc_split_compare` · `promo.ugc_stop_scrolling` · `promo.ugc_talking_head` · `promo.ugc_text_hook_face` · `promo.ugc_thirty_days` · `promo.ui_animation`

**And the shape of that list is the finding, not its length.** Look at what axis two put under *believed*, then look at how much of it is on this list. **Almost every card whose use depends on a fact about the world being true is unasked** — `promo.ugc_mistake_hook`, `promo.ugc_reply_comment`, `promo.ugc_made_me_buy`, `promo.ugc_thirty_days`, `promo.ugc_split_compare`, `promo.ugc_founder_piece`, `promo.ugc_talking_head`, `promo.ugc_phone_look`, `promo.critic_quote`, `promo.problem_solution`, `promo.ui_animation`, `promo.product_match_cut`. This is not an oversight and it is not repairable by adding edges. **A card that yields can only name a condition it can see from where it stands — a property of the shot, the product or the format.** It cannot name *whether a real customer has actually complained*, *whether the founder can speak*, *whether a month of results exists*. Those conditions live outside every card on the shelf, so no card can ever be the destination of a yield that turns on them. The pair graph is a graph of **things you can decide**, and half this shelf is made of **things you can only discover.**

The second thing the list shows: **the whole reply-and-response region is unasked** — `promo.ugc_reply_comment`, `promo.ugc_duet_stitch_brand`, `promo.ugc_greenscreen_page`, `promo.ugc_split_compare`, `promo.ugc_stop_scrolling`. Every one of these makes an advert out of something that is already on the platform, and nothing on the shelf routes to any of them. The shelf treats an advert as a thing written from a brief and then shot. Nothing on it treats **the feed itself as the material** — as footage the piece is answering rather than a place it is dropped into. The new card this shelf wants is the one whose first frame is somebody else's video and whose whole structure is the answer to it; and the nearest thing that exists, `promo.ugc_duet_stitch_brand`, records that failure in its own `Avoid when:` — *if your answer is agreement with no test in it, you have added nothing and simply repeated the brand* — without anything routing a reader there to read it.

`promo.choose_whose_camera`

---

### Product Hero Shot

**Also called:** hero product shot, hero frame, product beauty angle  
**What it is:** A shot built entirely around the product alone: a clean or graded background, drawn lighting, a lit edge and the angle that shows its best shape. Do not confuse it with the Beauty Shot: the beauty shot sells a feeling, while the hero shot sells the form and the identity.  
**Effect on the audience:** It turns an object into a protagonist. The viewer reads it as larger and more valuable than it really is, and this is the frame that stays in memory.  
**Used for and where it works best:** It sits at the moment of introduction in the middle of the film once you have built the need, returns at the close, and is the same frame the product page uses. Shoot slightly low so the product reads as imposing, add a rim light to separate it from the background, and leave air around it without clipping its edges. In vertical let it fill half the frame height so it reads on a phone.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Explainer, Fashion Film, Travel / Real Estate / Hospitality, Title Sequence / Opening Credits, AI-Generated Clip | genres: Family, Slice of Life, Comedy, Science / Educational, Romance, Drama  
**Avoid when:** A hero shot against a busy background loses all its value, and held longer than three seconds with no movement it becomes a dull still. When the product does not read from the angle you picked, beauty cannot rescue a lost silhouette, and do not open on it before the viewer has a reason to care.  
**Prompt:** `product hero shot on a seamless gradient background, slightly low angle, rim lit edges, slow push in, studio lighting`  
**Yields to:** `frame.beauty_shot` — The moment sells a feeling, not the form.  
`promo.hero_shot`

### Product Reveal

**Also called:** the reveal, unveiling shot  
**What it is:** The product comes into the light after being hidden: a cover is pulled away, a box opens, a hand moves aside, or light travels across it in the dark.  
**Effect on the audience:** It turns the product into an event. The reveal gives the ad a peak moment and makes the object feel new even when the audience already knows it.  
**Used for and where it works best:** Its natural place is after the problem and before the solution. Keep the movement single, continuous and slow, and tie it to one clean sound. In a vertical ad put the reveal at second three, not at the end.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Corporate / Training, AI-Generated Clip | genres: Family, Science / Educational, Slice of Life, Action, Romance, Fantasy / Epic  
**Avoid when:** A slow reveal of an ordinary product reads as empty theatre. Usually one reveal in an ad, because the second cancels the first; the exception is a two product spot where each one gets its own beat.  
**Prompt:** `a silk cover slides off the product in one continuous slow motion, light sweeping across the surface as it is uncovered`  
**Yields to:** `promo.unboxing` — Ordinary product where staged theatre reads empty.  
`promo.product_reveal`

### Macro Texture

**Also called:** texture insert, surface macro  
**What it is:** An extremely close shot of the product's surface: coffee grounds, fabric weave, droplets on metal, the grain of leather.  
**Effect on the audience:** It transmits touch through the eye, so the viewer imagines the feel of the thing, which creates more desire than any description.  
**Used for and where it works best:** Placed between usage shots to break the rhythm and sell the quality. Light it from the side so the texture is drawn by its own shadow. For food, fragrance and fabric it is the single most important shot in the ad.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Fashion Film, Corporate / Training, Heritage / Historical Documentary, AI-Generated Clip | genres: Family, Slice of Life, Romance, Science / Educational, Heritage (civilisation-focused), Nature / Wildlife  
**Avoid when:** Macro on a cheap or scratched surface exposes the product instead of selling it. Without precise focus it comes out soft and damages the impression.  
**Prompt:** `extreme macro on the product surface, hard side light raking across the texture, shallow depth of field, slow drift`  
**Yields to:** `promo.ugc_asmr_closeup` — Texture carried by close sound, not raking light.  
`promo.macro_texture`

### Pour And Splash In High Speed

**Also called:** liquid hero, slow motion splash  
**What it is:** Liquid pours or bursts and is captured at a very high frame rate, so it plays slow with every droplet defined.  
**Effect on the audience:** It turns an everyday instant into something epic and delivers the freshness and purity that sell drinks, cleaning products and fragrance.  
**Used for and where it works best:** Keep the background dark and the light behind so the liquid glows and reads as transparent. Shoot the pour on a single axis with a locked camera; the movement is already in the liquid. Ideal for drinks, honey, oil and soap advertising.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, AI-Generated Clip | genres: Family, Slice of Life, Science / Educational, Romance  
**Avoid when:** Over-slowing makes the shot drag and kills the pace. The same splash used three times makes the ad feel empty.  
**Prompt:** `high speed slow motion pour into a glass, backlit against a dark background, every droplet sharp, locked camera`  
**Yields to:** `promo.ugc_asmr_closeup` — A pour sold intimately instead of as spectacle.  
`promo.pour_splash`

### Levitation

**Also called:** floating product, suspended shot  
**What it is:** The product and its ingredients hang in the air with no visible support, still or slowly turning inside a clean space.  
**Effect on the audience:** Removing gravity removes reality with it, so the product reads as weightless, perfect and outside the ordinary world.  
**Used for and where it works best:** It works for fragrance, cosmetics and composed food: each ingredient floats around the product then gathers onto it. Keep the light soft and the background graded. It suits AI generation particularly well because no real rig is needed.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Title Sequence / Opening Credits | genres: Family, Science / Educational, Fantasy / Epic, Slice of Life, Surreal / Absurdist  
**Avoid when:** Floating a heavy or humble product for no reason looks artificial. Too many flying elements crowd the frame and the product stops reading.  
**Prompt:** `product floating in mid air with its ingredients suspended around it, soft gradient background, slow rotation, no supports`  
**Yields to:** `promo.hero_shot` — Heavy or humble product where floating looks artificial.  
`promo.levitation`

### Problem-Then-Solution Cut

**Also called:** before and after logic, pain to relief  
**What it is:** One shot states the problem clearly, then a straight cut to the same situation solved by the product, usually in the same framing.  
**Effect on the audience:** The cut itself is the argument. The difference between the two frames persuades faster than any line, and the viewer concludes it themselves.  
**Used for and where it works best:** The base structure of advertising: problem, product, solution, sign-off. Keep the problem to one short, slightly heightened shot and stage the solution from the same angle so the comparison reads instantly. In vertical, fit both inside the first four seconds.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Corporate / Training, Meme / Comedy Edit | genres: Family, Comedy, Slice of Life, Drama, Science / Educational  
**Avoid when:** A problem exaggerated to the point of parody makes the solution unbelievable. Do not give the problem more time than the solution or the ad turns grim.  
**Prompt:** `same framing shown twice, the frustrating problem then a hard cut to the same moment solved by the product`  
**Yields to:** `promo.ugc_before_after_oner` — The cut invites doubt, proof must be uncut.  
`promo.problem_solution`

### Before / After Wipe

**Also called:** split wipe, slider comparison  
**What it is:** A line travels across the frame revealing the new state over the old one, with the framing itself never changing. It differs from the straight-cut Before / After, because here the comparison runs continuously inside one shot instead of being cut.  
**Effect on the audience:** It makes the comparison continuous rather than cut, so the viewer watches the change happen and reads it as credible.  
**Used for and where it works best:** Suits cleaning, restoration, beauty and image editing. The camera must be locked and the light identical in both passes. In heritage documentary use it between the ruins today and the imagined reconstruction.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Explainer, Heritage / Historical Documentary, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation | genres: Science / Educational, Heritage (civilisation-focused), Historical / Biopic, Family, Slice of Life, Nature / Wildlife  
**Avoid when:** A fast wipe that gives no time to compare wastes the idea. If the angle changed between the two passes the wipe exposes it and trust is gone.  
**Prompt:** `locked frame with a vertical wipe line travelling across revealing the after state over the before state`  
**Yields to:** `vertical.before_after` — The straight cut, not the travelling line, carries it.  
`promo.before_after_wipe`

### Hands With The Product

**Also called:** hand model shot, in hand insert  
**What it is:** Human hands hold the product, operate it or open it, with the face usually out of frame or unimportant.  
**Effect on the audience:** It gives a true sense of scale and a feeling of ownership: the viewer imagines holding it. It is also the cheapest way to bring a human element in.  
**Used for and where it works best:** The backbone of short product content and of heritage documentary alike: a hand holding the piece, opening the lid, pressing the switch. Keep the hand clean and the movement calm and slow, shooting from above or at product level. In heritage work it is the answer when faces must stay hidden.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary, Explainer, Corporate / Training, Kids Content | genres: Family, Slice of Life, Heritage (civilisation-focused), Science / Educational, Historical / Biopic  
**Avoid when:** A tense hand or attention-grabbing nails pull focus off the product. Fast movement means the viewer never gets to see the thing.  
**Prompt:** `clean hands lifting and opening the product in a top down framing, slow deliberate movement, soft even light`  
`promo.hands_with_product`

### Demonstration Shot

**Also called:** product in use, functional proof  
**What it is:** One continuous shot showing the product doing the thing it promises, from the start to the result with no cut.  
**Effect on the audience:** A cut invites doubt; continuity builds trust. The absence of a cut is itself the proof.  
**Used for and where it works best:** Essential for functional products: cleaning, cutting, sticking, cooking. Frame wide enough that the start and the end fit in the same shot. In vertical use a top down angle so the whole action fits the frame.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Kids Content | genres: Science / Educational, Family, Slice of Life, Comedy  
**Avoid when:** A cut in the middle of the demonstration makes the viewer suspect something was hidden. Do not speed the shot up when real time is part of the claim.  
**Prompt:** `single unbroken shot of the product performing its function from start to finished result, wide enough to show both`  
**Yields to:** `promo.ugc_product_in_hand` — Creator ad where a lit plinth reads as advertising.  
`promo.demo_shot`

### Satisfaction Reaction

**Also called:** the happy reaction, payoff face  
**What it is:** A close shot of the user's face right after the product works: relief, mild surprise, a small smile.  
**Effect on the audience:** It hands the viewer the emotional result. The face states what you will feel, and emotional mirroring makes the viewer feel it too.  
**Used for and where it works best:** It comes immediately after the demonstration and must be short, one second to one and a half. Keep the smile small and real rather than wide. It matters most in vertical ads, where it puts a human face among product shots.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Kids Content, Explainer | genres: Family, Comedy, Slice of Life, Romance, Drama  
**Avoid when:** An overplayed expression makes the ad look fake and unintentionally funny. A reaction placed before the viewer has seen its cause usually lands as noise, because there is nothing to attach it to; the exception is a teaser cut where the cause arrives as the punchline.  
**Prompt:** `one second close-up of the user's face right after the product works, small genuine smile, soft key light`  
**Yields to:** `cut.reaction_first` — Teaser cut where the cause is the punchline.  
`promo.usage_reaction`

### UGC Talking Head

**Also called:** creator style ad, user generated look  
**What it is:** An ad shot on a phone in the person's own hand, with no advertising lighting, the speaker describing their experience in ordinary language.  
**Effect on the audience:** It wears the shape of ordinary feed content so it is not rejected the way an ad is, and the trust comes from the look of the image itself.  
**Used for and where it works best:** Best for everyday products, apps, supplements and services. Use a real home background, keep the room tone in, and let the speech sound unrehearsed. Cut it with jump cuts and let the product enter frame from below.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Vlog / YouTube Long-Form, Mockumentary, Corporate / Training | genres: Slice of Life, Comedy, Family, Drama  
**Avoid when:** A memorised advertising script in an announcer voice exposes the format in two seconds. Do not use it for a premium product; the contradiction cheapens the brand.  
**Prompt:** `handheld phone framing in a real home, one person talking to the lens about the product, available light, natural room sound`  
**Yields to:** `promo.testimonial_frame` — Premium product the phone look would cheapen.  
`promo.ugc_talking_head`

### Unboxing

**Also called:** box opening, first look  
**What it is:** The box is opened in front of the camera step by step: the wrap, the lid, the layers, then the product, usually from a top down angle.  
**Effect on the audience:** It reproduces the real pleasure of receiving something, and the viewer lives the moment of ownership before buying.  
**Used for and where it works best:** The backbone of product, gift and tech content. Shoot from above with soft even light and open each layer in one clean movement with its real sound. In vertical let the box fill the width of the frame.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, Kids Content, Corporate / Training | genres: Family, Slice of Life, Science / Educational, Comedy  
**Avoid when:** A long slow opening with no surprise loses the viewer before the product appears. Do not let your hand cover the product at the moment it appears.  
**Prompt:** `top down shot of hands opening the packaging layer by layer with real sound, soft even light, product revealed last`  
**Yields to:** `promo.ugc_unboxing` — Staged opening reads as an ad, honesty is the point.  
`promo.unboxing`

### Pack Shot

**Also called:** packaging shot, product with packaging, packshot, end frame product shot  
**What it is:** The product with its packaging in a clear steady shot showing the brand, the name and the shape the shopper will see on the shelf.  
**Effect on the audience:** It connects the ad to the moment of purchase. The viewer has to know exactly what to look for, and this shot is the bridge.  
**Used for and where it works best:** It sits at the end, just before or with the end card, and holds for at least three seconds. Shoot it straight on with even light, high contrast and the fewest elements possible, because it is usually seen on a phone with the sound off. In vertical scale it up more than feels right, keep the pack centred above the lower interface band, and keep the shot live rather than frozen: the pack itself stays steady while a subtle background or camera move keeps the frame alive — on a reel it is the last live shot that carries the logo and the line under `promo.end_card`, and a frozen frame there is dead air.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Explainer, Travel / Real Estate / Hospitality, AI-Generated Clip | genres: Family, Slice of Life, Science / Educational, Comedy, Drama  
**Avoid when:** A pack at an angle or with a shadow cutting the name defeats the purpose, and crowding it with text and logos means nothing lands at all. Do not place it at the top of the ad, where it spends the curiosity before the story, and do not let it be the only good looking shot in the film.  
**Prompt:** horizontal — `straight on pack shot with even soft light, brand name fully legible, product beside its packaging, static three second hold` · vertical — `straight on pack shot scaled up and centred above the lower band, even soft light, brand name fully legible, the pack itself steady while the background or camera still moves under the logo and line, three second hold`  
`promo.pack_shot`

### Logo Sting

**Also called:** brand sting, audio logo  
**What it is:** A short appearance of the logo with a distinctive brand sound, lasting one to two seconds.  
**Effect on the audience:** It ties the brand to a sound, and sound is remembered longer than an image. Repetition builds instant recognition.  
**Used for and where it works best:** Its only place is at the end after the message, and it repeats identically across all the brand's films. Keep the movement simple: appear, settle, leave. In very short ads cut it to half a second.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Title Sequence / Opening Credits, Corporate / Training, Trailer / Teaser, Explainer | genres: all  
**Avoid when:** A sting at the top drives viewers away in short-form. Changing its look in every film cancels the entire benefit.  
**Prompt:** `logo resolves into place over a clean background with a short signature sound, holds one second, no camera move`  
**Yields to:** `promo.logo_animation` — Title sequence needing a built, moving mark.  
`promo.logo_sting`

### End Card

**Also called:** closing frame, sign-off card, outro card, final frame card  
**What it is:** The final static frame carrying the logo, the line and the action information: the website, the store, the date, sitting on a finished design rather than on a random frame. It differs from the long-form platform Outro End Card, which offers the next video and a follow prompt across ten to twenty seconds.  
**Effect on the audience:** It closes the ad with something actionable. This is where the viewer decides what to do, so the information must be single and clear.  
**Used for and where it works best:** One piece of information in large type, and in vertical respect the reserved lower band. In heritage work: the site name and its date in clean type.

**How long it holds depends on how the viewer arrived, not on the aspect, and the two answers are different enough to be stated separately.**

- **Anything the viewer chose to watch — broadcast, trailer, TVC, a film played on purpose:** hold **three seconds or more.** Less than that and it is not read, and an unread end card is the whole reason the ad was made, thrown away in the last second.
- **Anything that arrives in a feed and can be scrolled past — reels, Shorts, TikTok, and a horizontal feed reel as well:** **do not build a separate static card at all.** The right move is to **fold the logo and the line into the last live shot**, over the pack shot or over the final frame while it is still moving. A static frame at the end of a feed piece is dead air, and two seconds of dead air costs completion, which costs reach, which costs everything the card was for. If a separate card is required — a contract requires it, or the client's brief names one ("end card", "closing card" or "end frame" in so many words; "end on the logo and the phone number" names what goes on the ending, not a separate card, and is folded into the last live shot) — two seconds is the floor and one second is not a card — it is a flash nobody read. A card only the craft suggests is folded into the last live shot. Record which case it is under `decisions`.

This is also where `promo.ramping_cut_rate` stops. The accelerating edit governs the picture and ends at the last live shot; the lock-up sits outside the curve. A ramp that runs down to half a second and then hands over to a three-second frozen card is the one arrangement that fails at both ends.

**Outranks:** `promo.ramping_cut_rate` — on the final frame of a commissioned advert, where the client's mark has to be readable and the ramp does not reach it.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Corporate / Training, Explainer, Title Sequence / Opening Credits, Kids Content, Travel / Real Estate / Hospitality, Heritage / Historical Documentary | genres: all  
**Avoid when:** An end card crowded with a website, four handles and a phone number leaves none of them read, and under two seconds it is not read at all. A separate static card on a feed reel in any aspect, where the logo belongs on the last live frame instead. A call to action on a dramatic piece usually breaks the world you just built; the exception is a campaign film where the cause is the reason the piece exists.  
**Prompt:** chosen — `static end card with the logo centred, one line of copy and a single call to action, clean background, three second hold` · feed — `logo and single line held over the last live shot while it is still moving, copy in the upper two thirds, clear of the lower band`  
**Source:** assumption — the package's working figures (three seconds on a chosen watch, a two-second floor for a required feed card), not a published standard; they are defaults, and a hold the brief names is built as asked.  
**Shelf life:** dated — review 2027-03. The hold figures, and the claim that dead air on a reel costs completion and reach, are undated statements about viewing and platform ranking, and the ranking moves whenever the platform changes it; folding the sign-off into the last live shot is the durable part.  
**Yields to:** `promo.ugc_end_cta_offer` — Feed reel in any aspect, sign-off from inside the last live shot.  
`promo.end_card`

### Logo Animation

**Also called:** logo build, brand animation  
**What it is:** The logo builds from its own elements or transforms from a shape related to the brand, in a short move that ends on the official static form.  
**Effect on the audience:** It gives the brand a moving personality, and with repetition it becomes part of the viewer's visual memory.  
**Used for and where it works best:** Let the movement come from the meaning of the brand: lines gathering, light passing, a shape opening. Keep it under two seconds and end on a full stop. In heritage work build the mark from an element of the same civilisation, such as a carved motif.  
**Best in:** formats: Title Sequence / Opening Credits, Commercial / TVC, Corporate / Training, Product Video / Motion Design, Explainer, Trailer / Teaser | genres: all  
**Avoid when:** A complex animation steals attention from the content and lengthens the ad. Do not let it keep moving after it settles; the stillness is what fixes the shape.  
**Prompt:** `the logo assembles from its own graphic elements in one short move and locks into its final static form`  
**Yields to:** `promo.logo_sting` — Short ad where the build steals the time.  
`promo.logo_animation`

### Motion-Graphic Shape Wipes

**Also called:** shape transitions, graphic wipe  
**What it is:** A coloured shape (a circle, a bar, a triangle) crosses the frame and drags the new shot behind it instead of a straight cut.  
**Effect on the audience:** It gives the film a unified graphic identity and makes the transitions part of the design rather than filler. It works best for brands with defined colours.  
**Used for and where it works best:** Use the brand's own colours and one repeating shape through the whole film. Keep the direction constant, right to left every time for instance. Ideal for explainers, product and educational video, and for vertical where it adds energy without camera movement.  
**Best in:** formats: Explainer, Commercial / TVC, Product Video / Motion Design, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Title Sequence / Opening Credits | genres: Science / Educational, Family, Comedy, Slice of Life  
**Avoid when:** A different shape and colour on every transition makes the film look like a template pack. A shape covering the frame too long breaks the flow.  
**Prompt:** `a brand coloured bar sweeps across the frame from right to left carrying the next shot behind it, same direction every time`  
**Yields to:** `promo.black_frame_punch` — Trailer or dramatic cut where brand graphics are wrong.  
`promo.shape_wipes`

### Six-Second Bumper

**Also called:** bumper ad, six second cut  
**What it is:** An ad exactly six seconds long: one idea, one or two shots and the logo, with no set-up and no story.  
**Effect on the audience:** It forces you to choose the single thing you want remembered, and that constraint usually produces cleaner work than a long film.  
**Used for and where it works best:** The working structure: hook or problem for two seconds, product for two, logo for two. Keep the copy to two or three words. Ideal as a reminder before a launch or alongside a bigger campaign, and it suits vertical advertising very well.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Title Sequence / Opening Credits, Corporate / Training | genres: Comedy, Family, Slice of Life, Action, Science / Educational  
**Avoid when:** Cramming a full story into six seconds produces an ad nobody understands. Do not put the logo at both ends; there is no time left for the product.  
**Prompt:** `six second structure, two seconds hook, two seconds product in use, two seconds logo card, one line of copy only`  
**Shelf life:** dated — review 2027-03. The six-second length is a platform ad product, not a craft fact: which placements sell it, and at what length, is the platform's to change.  
**Yields to:** `promo.cutdown_15s` — A story that cannot be understood in six seconds.  
`promo.bumper_6s`

### Fifteen-Second Cutdown

**Also called:** cutdown, short version  
**What it is:** A shorter version built from the same material as the original: the connective beats are removed, the shots are trimmed and only the spine is left.  
**Effect on the audience:** It keeps the campaign spine in a shorter unit and works on the placements that will not carry anything longer.  
**Used for and where it works best:** Design the long film knowing the cutdown comes out of it: make every shot readable on its own. The cutdown starts on the hook shot and jumps straight to the product. Always keep the logo and the pack shot.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Corporate / Training | genres: all  
**Avoid when:** A mechanical trim from the middle leaves a story with a hole in it. Do not speed the shots up to fit the duration; the rhythm breaks and it reads as rushed.  
**Prompt:** `rebuild the film as fifteen seconds keeping the hook shot, the demonstration, the reaction, the pack shot and the logo`  
**Shelf life:** dated — review 2027-03. Which placements will not carry anything longer, and so the fifteen-second ceiling, are placement specifications that move with the platforms; building the cutdown from the spine is the durable part.  
**Yields to:** `promo.bumper_6s` — Trimming leaves a hole; one idea is all that fits.  
`promo.cutdown_15s`

### Three-Act Trailer Structure

**Also called:** the three movements, trailer arc  
**What it is:** The trailer is built in three movements: introduce the world and the character, escalate the problem, then a fast cut sequence on a rhythm that ends in silence and one final shot.  
**Effect on the audience:** It gives the viewer a complete-feeling story in two minutes without spending the ending, and the escalation makes the rising energy physically felt.  
**Used for and where it works best:** The first movement runs on longer shots and calm music, the second shortens the shots as the conflict enters, the third is rapid fire then absolute silence then a closing shot or a joke. It works for features, series, heritage documentary and even large product launches.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Documentary Series, Heritage / Historical Documentary, Game Cinematic / Gameplay, Music Video, Corporate / Training | genres: Action, Thriller / Suspense, Drama, Fantasy / Epic, Horror, Historical / Biopic, Heritage (civilisation-focused), Sci-Fi  
**Avoid when:** Three movements at the same pace cancel the escalation and flatten the trailer. Spending the climax in the third movement usually sells the film short, because a trailer works as a promise rather than a delivery; the exception is a final trailer for a title already sold on spectacle.  
**Prompt:** `three movement trailer structure, long shots and calm score first, escalating cuts second, rapid fire then silence and a final shot`  
**Yields to:** `promo.trailer_rise` — Vertical or very short, no room for three movements.  
`promo.three_act_trailer`

### The Trailer Rise

**Also called:** riser, build up  
**What it is:** A sound layer climbs steadily while the shots get progressively shorter, all travelling toward one burst or one abrupt cut.  
**Effect on the audience:** It creates physical tension: the viewer's breathing quickens with the climb, so when the cut lands the impact is doubled.  
**Used for and where it works best:** The rise must have an exact destination: a cut to black, a hit, or the title. Make every shot shorter than the one before it. Suits trailers, documentary and dramatic advertising, and works very well for vertical teasers.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Documentary Series, Heritage / Historical Documentary, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay | genres: Thriller / Suspense, Horror, Action, Drama, Historical / Biopic, Sci-Fi, War  
**Avoid when:** A rise with no clear destination leaves the viewer deflated. Two rises back to back in the same trailer cancel each other.  
**Prompt:** `rising sound layer under progressively shorter shots, all building to a hard cut to black on the peak`  
**Yields to:** `promo.silence_drop` — Land the title by dropping out, not by building.  
`promo.trailer_rise`

### Silence Drop Before The Title

**Also called:** the drop out, dead air beat  
**What it is:** All audio cuts out abruptly for half a second to two seconds before the title or the final shot arrives.  
**Effect on the audience:** Silence after noise stops time. The ear stays open and the viewer's attention snaps onto whatever comes next.  
**Used for and where it works best:** The strongest device at the end of a trailer: rapid fire, then total silence on a held frame or on black, then the title. It also works before the key line in an ad and before a reveal in documentary. Use it once only in a film.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Documentary Series, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Title Sequence / Opening Credits | genres: Thriller / Suspense, Horror, Drama, Action, War, Historical / Biopic, Mystery / Whodunit  
**Avoid when:** A very long silence in vertical makes the viewer think the video has broken and they leave. A drop to silence with nothing strong behind it usually reads as a fault rather than a beat; the exception is a comic pause where the emptiness is the joke.  
**Prompt:** `hard silence for one second on a held frame after the fast cut sequence, then the title appears with a single hit`  
**Yields to:** `promo.braaam` — Vertical, where long silence reads as a broken video.  
`promo.silence_drop`

### Quick-Cut Montage To Hits

**Also called:** cut sequence, rapid fire montage  
**What it is:** A run of very short shots, each locked to a percussive hit, each carrying exactly one piece of information.  
**Effect on the audience:** It delivers scale and variety in a short time: the viewer feels they have seen a whole world in ten seconds.  
**Used for and where it works best:** The third movement of a trailer, the end of a launch film, the recap in a series. Order the shots by scale with the biggest last — the biggest of the run, not the production's largest image, which `promo.money_shot` holds back for the final shot after the silence. Every shot has to carry one idea readable at the length it is actually cut to, which means clean, simple compositions; measure that length in the cut rather than assuming it.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Documentary Series, Sports Broadcast / Sports Film | genres: Action, Thriller / Suspense, Fantasy / Epic, Sci-Fi, War, Sports Drama, Musical, Adventure  
**Avoid when:** Complex compositions are lost in half a second and the montage becomes noise. Do not run the sequence past ten seconds; it stops landing.  
**Prompt:** `rapid montage of one second shots each cut on a drum hit, simple compositions, scale increasing toward the last shot, the hero image kept out of the run`  
`promo.quick_cut_montage`

### Ramping Cut Rate

**Also called:** accelerating edit, pace ramp  
**What it is:** The average shot length falls steadily from around three seconds at the start to under half a second at the end. Those timings are starting points for a cut, not measured laws of attention.  
**Effect on the audience:** It produces a rising energy curve the body feels without the viewer noticing it, so the pace seems to pull them along.  
**Used for and where it works best:** Trailers and long-form ads whose emotional curve needs acceleration: begin patient, finish fast. Apply it to longer reels as well: three seconds on the first shot, half a second on the last. Measure the average on the timeline rather than trusting the feel. Fast cuts between ordinary images are not a flash question; only a stretch that alternates bright and dark frames on purpose goes to `safety.photosensitive_flash`, as a note in the handoff.

**Where the ramp ends.** The ramp governs the **picture** — the montage, the shots that carry the film. It ends at the last live shot. A pack shot, a lock-up or an end card is a separate object that comes after it, and it is not counted in the curve and not subject to it. Reading the ramp as though it reached the end card produces the collision that has no solution: a half-second final shot immediately followed by a three-second static frame, which is the energy curve rising to its peak and then stopping dead.

**And the floor is not the same in every frame.** Half a second is a real shot at cinema scale. On a phone, in 9:16, at the end of a piece under about forty-five seconds, it is a flash — the eye has not finished the shot before it is gone, and the montage reads as noise rather than as acceleration. **In vertical short form the ramp bottoms out at about 0.8 seconds, not 0.5.** The curve is the same shape; it is simply drawn between different ends. Keep the ratio — patient start, fast finish — and let the floor be set by what the frame can actually deliver.

**Shelf life:** dated — review 2027-03. The vertical floor and the short-piece band are stated about phone viewing with no source, and they move with how the platforms present a reel; the shape of the curve, patient start and fast finish, is the durable part.  
**Yields to:** `promo.end_card` — on the final frame of a commissioned advert, where the lock-up sits outside the ramp rather than at the bottom of it.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Game Cinematic / Gameplay, Sports Broadcast / Sports Film, Documentary Series | genres: Action, Thriller / Suspense, Sports Drama, Fantasy / Epic, War, Musical, Sci-Fi  
**Avoid when:** Accelerating too early burns the energy and leaves the ending cold. If every shot is the same length the trailer reads flat no matter how strong the images are. And do not run the vertical floor down to the cinema floor — half-second shots in a phone frame are a different thing from half-second shots on a screen.  
**Prompt:** horizontal — `shot lengths falling steadily from three seconds to half a second across the film, the shortest shots reserved for the finish` · vertical short form — `shot lengths falling steadily from three seconds to about eight tenths of a second, the shortest reserved for the finish, the lock-up outside the ramp`  
`promo.ramping_cut_rate`

### Black Frame Punch / Cut To Black On Beats

**Also called:** black flash, staccato black  
**What it is:** Short black frames are placed between shots on the beat, so the picture blinks out and returns.  
**Effect on the audience:** It creates a pulse and makes each shot land as a separate blow, stopping a fast montage from turning into mush.  
**Used for and where it works best:** Use it in the third movement of a trailer and in launch advertising: four shots separated by black, then one long shot. Keep every black gap the same length. In documentary it works between hard facts.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Documentary Series, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Title Sequence / Opening Credits | genres: Action, Thriller / Suspense, Horror, War, True Crime, Drama, Sci-Fi  
**Avoid when:** A long black gap makes the viewer think the video has ended. In vertical, repeated black reads like a playback fault.  
**Prompt:** `four frames of black between each shot in the fast sequence, gaps timed to the beat, identical length every time`  
**Yields to:** `promo.shape_wipes` — Vertical, where repeated black reads as playback fault.  
`promo.black_frame_punch`

### Stutter / Rewind Trailer Edit

**Also called:** stutter cut, glitch repeat  
**What it is:** The same shot repeats three or four times in a few frames, or runs backwards then continues, locked to the audio.  
**Effect on the audience:** It creates a glitching, nervous tension and forces attention onto a specific moment without adding a new shot.  
**Used for and where it works best:** Suits psychological, horror and cyberpunk trailers and youth advertising. Use it on an impact or on a head turn. Lock the stutter exactly to the rhythm or it reads as a technical fault.  
**Best in:** formats: Trailer / Teaser, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Commercial / TVC, Meme / Comedy Edit | genres: Psychological Horror, Horror, Thriller / Suspense, Cyberpunk, Action, Sci-Fi, Dark Comedy / Satire  
**Avoid when:** Stuttering in calm or formal content destroys the credibility. Off the beat it reads as a corrupted file rather than a style.  
**Prompt:** `four frame stutter repeating the head turn three times locked to the beat, then the shot continues normally`  
**Yields to:** `vertical.punch_in` — Calm or formal content a glitch would discredit.  
`promo.stutter_rewind`

### Title Cards Between Shots

**Also called:** text cards, copy cards  
**What it is:** Short text cards placed between shots, each carrying a word or a line that builds the meaning step by step.  
**Effect on the audience:** They give a reading rhythm that alternates with the image rhythm, steering the viewer's understanding without a voice over.  
**Used for and where it works best:** The standard alternative to narration in trailers and documentary advertising: three cards of three words building one sentence. Keep the design identical and land each one on a beat. Useful in vertical because they work with the sound off.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Documentary Series, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Video Essay | genres: Drama, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), True Crime, War, Action  
**Avoid when:** Too many cards turn the trailer into reading and waste the images. A card carrying a long sentence is read only halfway.  
**Prompt:** `three word text cards cut between shots on the beat, identical typeface and position, building one sentence`  
**Yields to:** `promo.trailer_voice` — Too many cards turn the trailer into reading.  
`promo.title_cards`

### One Line Of Dialogue Over Montage

**Also called:** single line bed, hero line  
**What it is:** A single line of dialogue from the film is laid across several shots, becoming the thread that links them instead of narration.  
**Effect on the audience:** It gives meaning to shots that have no connection, and the human voice makes the montage emotional rather than a showreel.  
**Used for and where it works best:** Choose the line that states the theme, not the one that explains the plot. Start it a quarter of a second before its shot. The basis of the drama trailer and heritage documentary, and it works in advertising when the voice is a customer's testimony.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Documentary Series, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Music Video | genres: Drama, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), War, Romance, Tragedy  
**Avoid when:** A line that explains the plot spends the film and turns the trailer into a summary. Do not lay two lines over the same montage; both are lost.  
**Prompt:** `one line of dialogue carried across four shots, starting a quarter second before the first image, music underneath`  
**Yields to:** `promo.dialogue_as_narration` — One line cannot carry it, several must be arranged.  
`promo.one_line_over_montage`

### Dialogue Used As Narration

**Also called:** dialogue bed, borrowed narration  
**What it is:** Lines of dialogue from different scenes are collected and arranged as a continuous narration serving the trailer's story rather than the film's.  
**Effect on the audience:** It builds a new meaning from existing material and makes the trailer feel purpose-written without shooting anything new.  
**Used for and where it works best:** This is how the modern trailer is built: arrange the lines so they ask a question and answer it, with pictures drawn from other scenes. Extremely useful in documentary, where interviews become the narration. Respect the original meaning of each line and never invert it.  
**Best in:** formats: Trailer / Teaser, Documentary Series, Heritage / Historical Documentary, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Video Essay | genres: Drama, Thriller / Suspense, True Crime, Historical / Biopic, Heritage (civilisation-focused), Mystery / Whodunit, War  
**Avoid when:** Assembling lines into a meaning the film does not contain leaves the viewer feeling cheated when they watch it. Do not pack in too many lines or the trailer becomes chatter.  
**Prompt:** `cut interview and dialogue lines from different scenes into one continuous narration bed under unrelated images`  
**Yields to:** `promo.trailer_voice` — Existing lines cannot honestly carry the story.  
`promo.dialogue_as_narration`

### Money Shot Held To The End

**Also called:** the hero image, saved shot  
**What it is:** The most expensive image in the production (the biggest vista, the largest effect, the strongest moment) is held for the last ten seconds and never shown before.  
**Effect on the audience:** It leaves the viewer at the highest point, and this is the image they will remember and talk about.  
**Used for and where it works best:** Order the whole trailer so the images grow and the largest arrives after the silence. The same principle applies in advertising: the best product image goes at the end, not the start. In heritage documentary save the widest view of the site for the final second.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Heritage / Historical Documentary, Documentary Series, Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), Music Video | genres: Fantasy / Epic, Action, Sci-Fi, War, Historical / Biopic, Heritage (civilisation-focused), Adventure, Mythology / Ancient Epic  
**Avoid when:** Showing the money shot at the top makes the rest of the trailer descend instead of climb. Do not save an ordinary shot and present it as a climax.  
**Prompt:** `the largest and most expensive image of the production placed as the final shot after the silence`  
**Yields to:** `promo.end_tag` — Comic or family close where the last beat is a joke.  
`promo.money_shot`

### Character Card Intro

**Also called:** name card, cast card  
**What it is:** Each character gets their own shot with their name or role written on it, in the same design for everyone.  
**Effect on the audience:** It organises the world fast and hands the viewer a map of the characters before the story begins.  
**Used for and where it works best:** Useful in series trailers, multi-character documentary and sports. Give each card a shot that expresses the character through an action rather than a pose. In heritage documentary use it for kings or deities with each one's emblem.  
**Best in:** formats: Trailer / Teaser, Documentary Series, Heritage / Historical Documentary, Game Cinematic / Gameplay, Sports Broadcast / Sports Film, Commercial / TVC, Title Sequence / Opening Credits | genres: Fantasy / Epic, Historical / Biopic, Heritage (civilisation-focused), Action, Mythology / Ancient Epic, Sports Drama, Crime / Procedural, War  
**Avoid when:** Too many cards and the viewer remembers none; five is the ceiling. Do not card a character who has no real place in the story.  
**Prompt:** `one action shot per character with a clean name plate in the same position and typeface for all of them`  
**Yields to:** `doc.lower_third` — A real subject named over their shot, not carded.  
`promo.character_card`

### The Teaser: One Image Plus A Date

**Also called:** date teaser, announcement teaser  
**What it is:** A very short piece, five to fifteen seconds, with one image or one movement and then the date or title, with no story at all.  
**Effect on the audience:** It works on curiosity rather than information: it announces existence and leaves the viewer asking. The mystery is the product.  
**Used for and where it works best:** Ideal weeks before the full trailer, and ideal in vertical because it is already short. Choose the most intriguing and elegant image, not the most explanatory. Tie it to one distinctive sound repeated across the whole campaign.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Game Cinematic / Gameplay, Product Video / Motion Design, Music Video | genres: Thriller / Suspense, Mystery / Whodunit, Horror, Sci-Fi, Fantasy / Epic, Action, Historical / Biopic  
**Avoid when:** A teaser with no distinctive image disappears in the feed and becomes spend with no return. Do not explain anything in a teaser; explanation is the trailer's job.  
**Prompt:** `one striking image with a single slow movement, then the date card, one signature sound, under fifteen seconds`  
**Yields to:** `promo.three_act_trailer` — The piece must explain rather than intrigue.  
`promo.teaser_image_date`

### Release Date Card

**Also called:** date lockup, coming soon card  
**What it is:** A final or near final card carrying the release date or the timing line, designed to match the title lockup.  
**Effect on the audience:** It converts desire into an appointment. The viewer leaves the trailer with one actionable piece of information.  
**Used for and where it works best:** Place it straight after the title, in the same typeface and relative size across every piece of the campaign. In vertical enlarge the date because the screen is small, and set it over the last live shot rather than on its own held frame, as `promo.end_card` requires on a reel. If there is no date, use one clear timing line instead.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Game Cinematic / Gameplay, Product Video / Motion Design | genres: all  
**Avoid when:** A small date under the title is unreadable on a phone. Do not announce an unconfirmed date; changing it later costs trust.  
**Prompt:** horizontal — `title lockup then a clean date card in matching type, large enough to read on a phone, two second hold` · vertical — `title lockup and date in matching type over the last live shot while it is still moving, large enough to read on a phone`  
**Yields to:** `promo.end_card` — Advert where the date belongs on the sign-off, not its own frame.  
`promo.date_card`

### The Credit Block

**Also called:** billing block, credits crawl  
**What it is:** The dense block of text at the end of the trailer carrying the production and cast names, in a condensed typeface and a fixed layout.  
**Effect on the audience:** It gives the material an institutional, official look even though little of it is read, and signals that this is a complete work rather than a clip.  
**Used for and where it works best:** It sits at the end under the title, small and centred. In vertical reduce it to three lines or drop it; the space does not allow it. In independent documentary use it for the supporting institutions.  
**Best in:** formats: Trailer / Teaser, Title Sequence / Opening Credits, Commercial / TVC, Documentary Series, Corporate / Training | genres: all  
**Avoid when:** A full block in a vertical video eats half the frame and is not read. Placed before the title it usually reads as an error, because the block is written to follow the title; the exception is a festival card carrying a laurel line of its own.  
**Prompt:** `condensed centred credit block under the title lockup, small type, static, three seconds`  
`promo.credit_block`

### Critic Quote Cards

**Also called:** review cards, press quotes  
**What it is:** Short cards carrying a line from a published review with the source's name, cut between the shots.  
**Effect on the audience:** They move the judgement from the maker to a third party, which builds trust faster than any self-made claim.  
**Used for and where it works best:** Used in post-release trailers and in advertising after launch. Keep the quote to three to five words with the source smaller beneath it. The same device works for products using real user reviews.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Product Video / Motion Design, Documentary Series, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits | genres: Drama, Comedy, Thriller / Suspense, Historical / Biopic, Action, Romance  
**Avoid when:** A quote trimmed so its meaning changes exposes you when people check the source. An invented quote or an invented source has no defence at all once that check is made, and on a released title it is always made.  
**Prompt:** `short review quote card in bold type with the publication name smaller beneath, cut on the beat between shots`  
**Yields to:** `promo.testimonial_frame` — No press yet; proof comes from a customer.  
`promo.critic_quote`

### End Tag / The Button

**Also called:** the tag, post logo gag  
**What it is:** A short shot that arrives after the logo or after the end card, usually a joke or a small surprise.  
**Effect on the audience:** It rewards whoever stayed to the end and leaves a light final impression, which gets the ad talked about.  
**Used for and where it works best:** Works in comedy, family advertising and comedy trailers. Keep it under three seconds and independent of the main message. In vertical it is an excellent reason for the viewer to stay to the end.  
**Best in:** formats: Commercial / TVC, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, Kids Content, Product Video / Motion Design | genres: Comedy, Family, Dark Comedy / Satire, Rom-Com, Slice of Life  
**Avoid when:** An end tag on serious or sad content breaks the whole tone. If the joke is weak the ending goes cold and damages the impression.  
**Prompt:** `two second comic beat after the logo card, same characters, single static shot, one clean punchline action`  
**Yields to:** `promo.money_shot` — Serious or sad content a joke would break.  
`promo.end_tag`

### Product Match Cut

**Also called:** product continuity cut, shape match on product  
**What it is:** The product stays in the same position and size in frame while everything around it changes: the place, the time, the user, the season.  
**Effect on the audience:** It presents the product as a constant presence running through people's lives, giving scale without ever losing the hero.  
**Used for and where it works best:** Ideal for brand films showing reach or history: the same cup in four homes, the same shoe in four cities. Lock the size and position in frame on every shot and cut on movement. Especially useful in vertical because the eye never has to search.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Travel / Real Estate / Hospitality | genres: Family, Slice of Life, Romance, Comedy, Drama, Adventure  
**Avoid when:** Changing the product's size between shots breaks the match and it becomes an ordinary cut. Do not let the backgrounds look alike; the whole idea is in the difference.  
**Prompt:** `the product locked at the same size and position in frame across four cuts while the location and the people change`  
**Yields to:** `promo.ugc_day_in_life` — Backgrounds cannot differ enough for the match.  
`promo.product_match_cut`

### Hero Product Sound

**Also called:** signature sound, product foley  
**What it is:** The product's real sound is recorded clean and amplified: the can opening, the click, the slide, the crunch, the engine.  
**Effect on the audience:** Sound delivers quality directly, and the ear believes a real sound more than any marketing line.  
**Used for and where it works best:** Record it separately in a studio rather than off the camera, and let it stand alone in its moment with the music pulled down. Repeat it across all the brand's films so an audio signature is built. Strongest for food, drinks, cars and devices.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Explainer, AI-Generated Clip | genres: Family, Slice of Life, Science / Educational, Comedy, Action  
**Avoid when:** A generic library effect instead of the real sound makes the product feel fake. Loud music over the moment wastes the most valuable second in the ad.  
**Prompt:** `macro shot of the product action with its real recorded sound isolated and amplified, music ducked to silence`  
**Yields to:** `promo.ugc_asmr_closeup` — Creator piece where close sound replaces the signature.  
`promo.product_sound`

### Creator Unboxing

**Also called:** UGC unboxing, first-person box opening  
**What it is:** The same idea as the polished box opening, except the camera is in the person's own hand or propped on the table and the hands are his. There is no studio light and no arranged angle: it happens in one sitting with unrehearsed commentary.  
**Effect on the audience:** The viewer feels he is sitting beside a friend opening a parcel rather than watching an ad. The small mess, torn cardboard and ordinary room light, is exactly what carries the honesty.  
**Used for and where it works best:** Products where the arrival is part of the pleasure: tech, beauty, gifts, subscription boxes. Shoot one continuous angle from above or from chest height, keep the sound of cardboard and plastic loud, and let the first reaction be genuine rather than replayed.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Meme / Comedy Edit, Corporate / Training | genres: Slice of Life, Comedy, Family, Science / Educational  
**Avoid when:** Do not stage the box so it looks perfect; the staging destroys the very reason you chose this format. And if the commentary is read off a page, the casual look becomes an obvious lie.  
**Prompt:** `handheld phone shot of real hands tearing open the parcel on a kitchen table, room light only, loud natural packaging sound, one continuous take`  
**Yields to:** `promo.unboxing` — Premium or gift product that needs the lit opening.  
`promo.ugc_unboxing`

### Get Ready With Me

**Also called:** GRWM, routine format  
**What it is:** The person talks to camera while doing a routine, getting ready for work, for a wedding, for bed, and the product enters at its natural place among the steps. The camera is fixed on the mirror or propped on a shelf.  
**Effect on the audience:** It sells the product inside a habit rather than on its own. The viewer sees it as part of someone's life and starts imagining it inside his own.  
**Used for and where it works best:** Beauty, skincare, clothing, coffee and supplements. Let the talking be about something else, a story, the day, an opinion, and let the product pass quietly, because the viewer stays for the story and buys because of what he saw on the way.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Fashion Film, Vertical Micro-Drama | genres: Slice of Life, Comedy, Romance, Family, Drama  
**Avoid when:** If every line is about the product the format reverts to an ad and is seen through. Do not over-cut either, because heavy cutting loses the real-time feel that defines this form.  
**Prompt:** `fixed phone on the bathroom shelf, she talks to the lens while doing her routine, the product used naturally in the middle, daylight from the window`  
**Yields to:** `promo.ugc_day_in_life` — The product lives across a day, not inside one routine.  
`promo.ugc_grwm`

### Product-in-Hand Demo

**Also called:** hand demo, hold and show  
**What it is:** The person holds the product, turns it, opens it and operates it in front of the lens, framed tight enough to fill the screen. The difference from the polished demo shot is that there is no plinth and no lighting: the hand itself gives the scale.  
**Effect on the audience:** The hand gives true scale instantly, which is the single piece of information a buyer wants and rarely gets from a polished commercial. Real handling also proves the thing works.  
**Used for and where it works best:** Any small or mid sized physical product: a device, a bottle, a toy, a tool. Keep the handling slow and legible, show the side people actually ask about, the handle, the lid, the port, and let the product enter frame from below.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Corporate / Training, Explainer, Vlog / YouTube Long-Form | genres: Science / Educational, Slice of Life, Family, Comedy  
**Avoid when:** Do not cover the product with your fingers while you talk about it; that is the most repeated mistake in the format. And if the hand is untidy or the background is busy, the eye goes to the wrong place.  
**Prompt:** `close handheld shot of hands turning the product to camera, filling the frame, natural window light, slow deliberate handling`  
**Yields to:** `promo.demo_shot` — Broadcast spot where the lit demonstration is right.  
`promo.ugc_product_in_hand`

### The POV Format

**Also called:** POV you, second person setup  
**What it is:** An on-screen line places the viewer inside a situation (you, on a Monday; you, after everything else failed) and the video plays that situation from his point of view. The difference from a plain vertical text hook is that this line frames the whole piece rather than only its first second.  
**Effect on the audience:** It turns the ad from talk about a product into a situation the viewer personally recognises. Recognition is what stops the thumb, not the product.  
**Used for and where it works best:** Products that solve a daily pain: sleep, back, skin, cleaning, time. Write the situation with painful precision so one person feels you described him exactly, then let the product arrive as the answer rather than the hero.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Meme / Comedy Edit, Vertical Micro-Drama, Product Video / Motion Design, Vlog / YouTube Long-Form | genres: Comedy, Slice of Life, Drama, Dark Comedy / Satire, Family, Romance  
**Avoid when:** A generic situation, you are tired, stops nobody; precision is what stops people. And do not write a situation unrelated to the product just to buy views, because the viewer feels the bait and leaves.  
**Prompt:** `on-screen line reading POV you have tried everything, then the scene plays from his point of view, handheld phone framing, real apartment`  
**Yields to:** `vertical.text_hook` — The line only opens the piece, does not frame it.  
`promo.ugc_pov_format`

### The Text-Hook-Over-Face Opener

**Also called:** caption hook on the face, hook card over talking head  
**What it is:** You open already talking to camera with the hook line set in large type directly over your face. Voice, image and caption all deliver the same idea in the first second.  
**Effect on the audience:** It works with sound and without it: whoever has audio follows the line, whoever is scrolling muted reads it. The living face behind it keeps the line personal rather than advertised.  
**Used for and where it works best:** Any ad resting on testimony or opinion. Put the caption above the brow rather than across the mouth — at the top of the text-safe band, where `vertical.text_safe_zone` sets a title above the face, not higher in the headroom, because the band is the only area that card guarantees readable on every platform — keep it to two lines at most, and change it after two seconds so the frame does not go static.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Corporate / Training, Meme / Comedy Edit | genres: Slice of Life, Comedy, Drama, Family, Science / Educational  
**Avoid when:** Type over the eyes usually costs you the trust the shot was built on, because the eyes are what build it; the exception is an anonymity piece where the face is deliberately hidden. A long line also cannot be read in a second, so write it with the fewest possible words.  
**Prompt:** `she is already mid sentence in the first frame, large caption above her eyes at the top of the central safe band, handheld phone framing in a real room`  
**Yields to:** `vertical.text_hook` — The hook must stand alone rather than sit on a face.  
`promo.ugc_text_hook_face`

### The Mistake Hook

**Also called:** I was wrong, confession opener  
**What it is:** You open with an admission: I was wrong, I wasted money for two years, I did this the wrong way my whole life. Then you explain what you discovered, and the product arrives as the outcome of that discovery.  
**Effect on the audience:** The confession lowers the viewer's defences because it is a concession rather than a sale. People listen to someone admitting a mistake far more readily than to someone praising.  
**Used for and where it works best:** Products competing with an old habit or a cheaper rival: tools, skincare, software, working methods. Keep the admission specific, a number, a duration, an amount, because specificity is what makes it credible.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Corporate / Training, Explainer | genres: Slice of Life, Drama, Comedy, Science / Educational, Dark Comedy / Satire  
**Avoid when:** A manufactured confession, I was wrong not to buy this, exposes the ad instantly. The mistake also has to be one people genuinely make, not one invented to set up the sale.  
**Prompt:** `opens on her face mid confession saying she got this wrong for years, handheld phone, real kitchen behind her, no music under the first line`  
**Yields to:** `promo.ugc_pov_format` — No genuine mistake to confess.  
`promo.ugc_mistake_hook`

### The Three Reasons Structure

**Also called:** 3 reasons why, numbered list ad  
**What it is:** You announce the number at the top, three reasons, four mistakes, then work through them in order, each with its own shot, caption and number on screen. The difference from plain vertical list cards is that every item here carries a selling argument rather than a piece of general information.  
**Effect on the audience:** The number promises a defined length, so the viewer stays to the end. The numbering also makes the content stick, because the brain holds counted things better.  
**Used for and where it works best:** Products that need a rational case: devices, subscriptions, services, health. Put the strongest reason last rather than first, and keep every reason to one line and one shot.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Explainer, Product Video / Motion Design, Corporate / Training, Vlog / YouTube Long-Form | genres: Science / Educational, Slice of Life, Comedy, Family, Medical Drama  
**Avoid when:** Do not promise three and deliver five; a broken promise loses the viewer. A long list of seven reasons also cannot finish inside the time an ad has.  
**Prompt:** `she says three reasons to camera, then three quick segments each with a number and one caption, handheld phone, cut on each new reason`  
**Yields to:** `vertical.list_cards` — Items carry general information, not selling arguments.  
`promo.ugc_three_reasons`

### The Hook, Demo, CTA Structure

**Also called:** three part UGC ad, the standard creator ad shape  
**What it is:** The backbone of a creator ad: three seconds of hook, then fifteen to twenty seconds of the product genuinely working, then three seconds of one clear call to action.  
**Effect on the audience:** Each part has exactly one job, so the ad never stumbles. Most failed creator ads break because they merge the hook with the call to action, or because they forget the demonstration entirely.  
**Used for and where it works best:** This is the default template for any performance ad on social platforms. Write the three parts before you shoot, time each one in seconds, and do not start filming until the hook exists as a single written line.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Corporate / Training, Explainer, Vertical Micro-Drama | genres: all  
**Avoid when:** Do not place the call to action in the middle, where it breaks the flow and loses people before they see the product work. And do not let the demo be talk alone: the result has to be visible on screen.  
**Prompt:** `three second hook to camera, then twenty seconds of the product actually being used with real sound, then a three second single call to action`  
**Yields to:** `promo.ugc_three_reasons` — Product needing a rational case, not one demo.  
`promo.ugc_hook_demo_cta`

### The App Made Me Buy It Reveal

**Also called:** TikTok made me buy it, feed purchase reveal  
**What it is:** You admit you bought the thing because of a video you saw, then show your own experience of it: was it worth it or not. The form imitates a buyer's review rather than a seller's ad.  
**Effect on the audience:** It works because it admits the advertising exists instead of denying it, so the viewer feels he is on your side of the claim rather than its target. Curiosity does the rest: true or false.  
**Used for and where it works best:** Products already circulating that people ask about in comments, and cheap products where the decision is fast. Include one small honest negative, because that is what makes everything else believable.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Meme / Comedy Edit, Vertical Micro-Drama | genres: Slice of Life, Comedy, Family, Science / Educational, Dark Comedy / Satire  
**Avoid when:** If every line is praise the format collapses back into an ordinary ad. And do not claim you bought it if the brand sent it to you; disclosure serves you and the brand better.  
**Prompt:** `she holds the product to camera saying she bought it after seeing it in her feed, handheld phone, real room, honest verdict at the end`  
**Yields to:** `promo.ugc_first_use_reaction` — Product not yet circulating; the first try is the content.  
`promo.ugc_made_me_buy`

### The Reply-to-Comment Format

**Also called:** comment reply video, question answer ad  
**What it is:** The video opens with the comment itself on screen, a question or an objection, and you answer it in speech and demonstration. The comment becomes both the hook and the reason the video exists.  
**Effect on the audience:** It strips the ad of its advertising character: you are not selling, you are answering. Showing the objection in public also reads as transparency.  
**Used for and where it works best:** For recurring objections: too expensive, will not work on my skin, I saw it cheaper, does it work at home. Choose a real comment from your own posts and answer it with a demonstration rather than an argument.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Corporate / Training, Vlog / YouTube Long-Form, Explainer | genres: Slice of Life, Science / Educational, Comedy, Family, Drama  
**Avoid when:** Do not invent a comment to answer; people recognise how real comments read. And do not pick an easy objection: the hard one is what sells, because it removes the last barrier.  
**Prompt:** `the video opens on a real comment pinned on screen, she reads it aloud and answers by showing the product working, handheld phone`  
**Yields to:** `promo.ugc_three_reasons` — No real objection exists to answer.  
`promo.ugc_reply_comment`

### Duet or Stitch with the Brand

**Also called:** brand duet, stitch response ad  
**What it is:** The brand posts a video and a creator answers it with a duet, screen beside screen, or a stitch, quoting a piece then continuing. The difference from duet and stitch as general formats is that here it is a declared commercial relationship between two parties.  
**Effect on the audience:** It connects two audiences and makes the ad feel like a conversation instead of a statement. An independent answer also puts the product through a public test.  
**Used for and where it works best:** A product launch, or answering the brand's own claim (they say one wipe is enough, let us test it). Keep the quoted portion very short and let your answer start in the first second.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Meme / Comedy Edit, Vlog / YouTube Long-Form, Vertical Micro-Drama | genres: Comedy, Slice of Life, Science / Educational, Dark Comedy / Satire, Family  
**Avoid when:** A long quoted section makes the viewer sit through the ad twice. And if your answer is agreement with no test in it, you have added nothing and simply repeated the brand.  
**Prompt:** `split screen duet, the brand clip on the left and the creator reacting and testing on the right, handheld phone framing, real room`  
**Yields to:** `vertical.duet` — Creator answering with no declared commercial relationship.  
`promo.ugc_duet_stitch_brand`

### Before-and-After in One Continuous Take

**Also called:** single take transformation, uncut proof  
**What it is:** You start on the before state, perform the process, and arrive at the after state, all in one take with no cut and no speed change. The difference from a before and after wipe is that there the transition is the idea, while here the absence of a cut is the evidence.  
**Effect on the audience:** The unbroken take is the argument: the viewer knows nothing was hidden. It is the strongest visual proof an ad can offer.  
**Used for and where it works best:** Cleaning, stains, skin, hair, repair and cooking. Lock the camera so the frame never moves, because a fixed frame is part of the proof, and keep the light identical from first second to last.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Corporate / Training, Explainer, Vlog / YouTube Long-Form | genres: Science / Educational, Slice of Life, Comedy, Family, Medical Drama  
**Avoid when:** Do not change the light or the angle between before and after; any change voids the proof and invites suspicion. And if the process is long, make the speed-up visible and declared rather than hidden.  
**Prompt:** `locked phone on a tripod, one continuous take, the stain cleaned in real time in front of the lens, no cuts and no speed change, identical light throughout`  
**Yields to:** `promo.before_after_wipe` — The transition, not the absent cut, is the idea.  
`promo.ugc_before_after_oner`

### The Phone-Quality Authenticity Look

**Also called:** deliberate low production look, unpolished ad look  
**What it is:** A deliberate look imitating an ordinary phone video: room light or a visible ring light, no colour grade, a little shake, autofocus arriving a beat late, and sound from the phone's own microphone.  
**Effect on the audience:** It lets the ad land in the feed like everything else around it, so it is not rejected. The eye has learned that a polished image means someone is selling and an ordinary image means someone is talking.  
**Used for and where it works best:** Every performance ad aimed at social platforms. Use a real home with real objects in it, keep the room tone, and put no advertising music under the opening line.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Vertical Micro-Drama, Meme / Comedy Edit | genres: Slice of Life, Comedy, Family, Drama, Dark Comedy / Satire  
**Avoid when:** Do not use it for a premium brand, where the contradiction cheapens the product. And do not fake extra roughness: the aim is an ordinary convincing image, not a bad one nobody can watch.  
**Prompt:** `shot to look like an ordinary phone video, ring light catching the eyes, no colour grade, slight handheld drift, autofocus hunting once`  
**Yields to:** `promo.hero_shot` — Premium brand the unpolished look would cheapen.  
`promo.ugc_phone_look`

### The No-Cut Single-Take Testimonial

**Also called:** uncut testimonial, one take review  
**What it is:** The person tells the whole experience in one take from start to finish, with no jump cuts, no captions and no music. The difference from a composed testimonial frame is that there the framing does the work, while here the absence of cutting does it.  
**Effect on the audience:** Jump cutting has become the signature of a prepared ad, so its absence reads as immediate honesty. Hesitation, breath and a repeated word are all evidence that the words are not memorised.  
**Used for and where it works best:** Products whose purchase requires trust: health, money, education, long term services. Record three or four complete takes and choose the most honest one, rather than repairing the speech with cuts.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Interview / Video Podcast, Product Video / Motion Design, Vlog / YouTube Long-Form | genres: Drama, Slice of Life, Medical Drama, Science / Educational, Family  
**Avoid when:** If the talk runs long with no development, the viewer leaves in the middle. Give the testimony a beginning, a middle and an end even though it is delivered in one breath.  
**Prompt:** `one unbroken take of him telling his experience to the phone, no cuts and no captions, room tone audible, natural pauses kept in`  
**Yields to:** `promo.testimonial_frame` — The framing, not the absence of cuts, does the work.  
`promo.ugc_single_take_testimonial`

### Day-in-the-Life with the Product

**Also called:** a day with me, routine vlog ad  
**What it is:** A string of short shots following a day from morning to night, with the product appearing in three or four natural moments inside it. The day is the story and the product is a recurring guest.  
**Effect on the audience:** Natural repetition beats insistence: the viewer sees the product three times in three different contexts and concludes it belongs to a real life.  
**Used for and where it works best:** Everyday products: coffee, water, a bag, a watch, an app, shoes. Let most shots contain no product at all, and let its appearances come in honest moments, in the car, at work, late at night.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Vlog / YouTube Long-Form, Product Video / Motion Design, Travel / Real Estate / Hospitality, Vertical Micro-Drama | genres: Slice of Life, Family, Comedy, Romance, Drama  
**Avoid when:** If the product appears in every shot the day turns into a long commercial. And do not present a flawless day either, because an over-arranged life is not believed.  
**Prompt:** `quick handheld shots through a real day, morning light to night, the product appearing naturally three times, no staging`  
**Yields to:** `promo.ugc_grwm` — One routine, not a whole day, holds the product.  
`promo.ugc_day_in_life`

### The Green-Screen React Over a Page

**Also called:** green screen over product page, standing in front of the listing  
**What it is:** You key yourself over a background and place the product page, the website or a post behind you, pointing at it while you talk. The difference from the general vertical green screen react is that here the background is a sales page and you are annotating it as evidence.  
**Effect on the audience:** It puts the person and the information in one frame, so the viewer reads and listens at once. The pointing hand also aims the eye at one exact place.  
**Used for and where it works best:** Explaining a specification, comparing a price, revealing a detail buried in a listing, answering a claim. Zoom into the section you are talking about rather than showing the entire page.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Explainer, Product Video / Motion Design, Corporate / Training, Meme / Comedy Edit | genres: Science / Educational, Comedy, Slice of Life, Dark Comedy / Satire, Family  
**Avoid when:** If the text behind you is too small to read on a phone, enlarge or crop it. And do not stand in front of the information; take the empty side of the frame.  
**Prompt:** `creator keyed over the product page behind her, she points at one enlarged section while talking, vertical framing, page text large enough to read`  
**Yields to:** `vertical.green_screen_react` — Reacting to something that is not a sales page.  
`promo.ugc_greenscreen_page`

### The Founder Piece-to-Camera

**Also called:** founder speaks, raw brand message  
**What it is:** The founder himself speaks to a phone camera from the warehouse, the workshop or the office, with no script and no lighting. He explains why the product exists or answers a criticism.  
**Effect on the audience:** It gives the brand a face, and a face carries responsibility. Viewers distinguish between a company speaking and a person speaking, and they trust the second.  
**Used for and where it works best:** A crisis, an apology, a launch, or explaining a price. Film in the real place of work so it is visible behind him, and keep the speech short, specific and free of corporate language.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Interview / Video Podcast, Vlog / YouTube Long-Form, Product Video / Motion Design | genres: Drama, Slice of Life, Science / Educational, Family, Political Thriller  
**Avoid when:** Reading from a page or speaking in press-release language destroys the entire benefit. An empty luxury office undercuts the message as well; film where the work actually happens.  
**Prompt:** `the founder talks straight to a handheld phone in his workshop, real light and real noise behind him, unscripted and short`  
**Yields to:** `promo.testimonial_frame` — Founder cannot speak unscripted; use a composed frame.  
`promo.ugc_founder_piece`

### The First-Use Reaction

**Also called:** watch me try it, first time on camera  
**What it is:** You use the product for the first time with the camera running and your genuine reaction plays in the same shot. The difference from a staged usage reaction is that here it truly is the first time, and the hesitation is part of the content.  
**Effect on the audience:** The viewer sees himself in your place, since he has not tried it either. Doubt turning into conviction plays out in front of him in real time, and he converts alongside you.  
**Used for and where it works best:** Products people hesitate over: an unusual taste, a new device, an unfamiliar method. Keep the camera on the face and the hands together, and never cut the reaction beat itself.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Vlog / YouTube Long-Form, Meme / Comedy Edit, Kids Content | genres: Comedy, Slice of Life, Family, Science / Educational, Dark Comedy / Satire  
**Avoid when:** An exaggerated reaction exposes the performance in a second. And if you tried the product before rolling, the naturalness is gone and the format is seen through.  
**Prompt:** `locked phone framing her face and hands, she uses the product for the first time, the reaction plays uncut in the same shot`  
**Yields to:** `promo.usage_reaction` — It is not genuinely the first time.  
`promo.ugc_first_use_reaction`

### The Stop-Scrolling Pattern Interrupt

**Also called:** scroll stopper, first frame interrupt for ads  
**What it is:** The first frame breaks what the eye expects: a sudden movement toward the lens, a colour that does not belong in the feed, something breaking or spilling, or a very close face already speaking. The difference from a general vertical pattern interrupt is that here the break must connect directly to the product, or the handover to the sell is lost.  
**Effect on the audience:** It buys you one second, which is everything in a paid ad. If that second is lost, the rest of the ad is never seen no matter how good it is.  
**Used for and where it works best:** Any paid ad in a feed. Test three different openings for the same ad and measure them, and make the interrupt come from inside the scene rather than from an added effect.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Meme / Comedy Edit, Vertical Micro-Drama, Trailer / Teaser | genres: Comedy, Action, Slice of Life, Dark Comedy / Satire, Thriller / Suspense, Family  
**Avoid when:** An interrupt unrelated to the product buys views and loses sales, and leaves people feeling tricked. Do not reuse the same interrupt across all your ads either, because the eye adapts to it fast.  
**Prompt:** `first frame is the product spilling toward the lens filling the screen, sudden movement and unexpected colour, cutting straight into the demo`  
**Yields to:** `vertical.pattern_interrupt` — The break does not connect to the product.  
`promo.ugc_stop_scrolling`

### The End-Card CTA with the Offer

**Also called:** closing offer card, UGC sign-off  
**What it is:** The closing beat in creator style: the same person stays in frame, says the action and the offer in his own voice, and the identical line appears as a caption. The difference from a designed end card is that there is no separate frame here; the call comes from inside the same shot.  
**Effect on the audience:** A call from a person sounds like advice, while a call from a card sounds like an ad. Keeping the face in frame also preserves the trust the rest of the video just built.  
**Used for and where it works best:** The close of any performance ad. One action only, the link in the description, the discount code, the order page, held for about three seconds, with the offer spoken and captioned together.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Corporate / Training, Explainer, Vlog / YouTube Long-Form | genres: all  
**Avoid when:** Do not offer two actions in one close, follow me and buy, because the viewer does the neither. And do not end on a polished brand logo alone, since the sudden jump to advertising finish breaks the form you just spent the whole film building.  
**Prompt:** `she stays in frame and says the single call to action with the discount code, the same words captioned on screen, three second hold, no logo card`  
**Yields to:** `promo.end_card` — A designed separate sign-off frame is required.  
`promo.ugc_end_cta_offer`
