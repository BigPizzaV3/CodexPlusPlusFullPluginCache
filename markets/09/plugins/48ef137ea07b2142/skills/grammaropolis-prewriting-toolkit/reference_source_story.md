# Reference: Source Story (the Garvin default)

*The Garvin source story as a structured object the skill loads when no custom source story is provided. It comes from the Grammaropolis Writing Framework's worked examples, structured here as the input schema the skill expects.*

---

## The Garvin source story

```yaml
source_story:

  premise: |
    The time I cooked dinner for Garvin's parents' anniversary.

  narrator_stake: |
    Being proud of myself. The narrator helped a friend pull off something hard
    that the friend could not have done alone, and the narrator's pride in that
    is the emotional through-line.

  narrator_identity: |
    Unnamed kid friend of Garvin. About the same age as Garvin (Grade 3-5 voice
    in the framework's worked examples). First-person.

  characters:
    - name: Garvin
      relationship_to_narrator: Best friend since they were three years old
      physical_traits:
        - Short, curly hair
        - Brown eyes
        - Three inches taller than the narrator
      personality_traits:
        - Goofy
        - Loves practical jokes
        - Loves chocolate and cheeseburgers, in that order
        - Wants to be a professional basketball player but is a much better singer
        - Gets super angry when you eat his dessert when he isn't looking
        - Tripped on the curb once and knocked his front teeth
      possessions_and_quirks:
        - Has a huge collection of Pokemon cards he never actually looks at

    - name: Mr. James
      relationship_to_narrator: Garvin's father
      traits:
        - Loves salt
        - Anniversary recipient
        - Patient eater

    - name: Mrs. James
      relationship_to_narrator: Garvin's mother
      traits:
        - Loves butter
        - Anniversary recipient
        - Patient eater

    - name: Sara
      relationship_to_narrator: Cousin (mentioned, not present in the scene)
      traits:
        - Taught the narrator a little bit about cooking, specifically breakfast

    - name: Stella
      relationship_to_narrator: Narrator's yellow labrador dog
      traits:
        - The cutest thing in the world
        - Sometimes sleeps with narrator in bed despite being supposed to sleep on the floor
      role_in_scene: Mentioned as part of "what we do together" backdrop, not present at the dinner

  setting:
    location: Garvin's house, in the kitchen, mostly. Some action in the dining room.
    time_of_day: Evening
    date: About six months ago, after school
    sensory_details:
      - Bright kitchen, white countertop, 4-burner stove
      - Egg whites and broken yolk on the counter (total mess)
      - Sizzling sound of eggs in the frying pan
      - Clinking sound of potato masher against the pot
      - Bubbling sound of boiling water
      - Smell of burning butter
      - Earthy scent of peeling potatoes
      - Pepper in the narrator's nose
      - Hot handle on the frying pan
      - Slimy egg white texture
      - Gooey hummus texture
      - Cold countertop

  events:
    - I went to Garvin's house after school
    - We decided to do something special for Garvin's parents
    - We rode our bikes to the store
    - We bought eggs, potatoes, hummus with Garvin's savings
    - Garvin squeezed an egg too hard trying to crack it and the egg white went everywhere
    - Garvin admitted he had never fried an egg
    - I peeled the potatoes and almost cut a big chunk out of my finger
    - Garvin started calling them "finger potatoes"
    - I turned the stove up too high and burned the butter
    - Smoke filled the kitchen
    - Garvin finally figured out how to crack an egg without getting it everywhere
    - I put all the food on a plate and took it to the dining room
    - Mr. and Mrs. James ate everything we served them
    - I was super proud

  comparison_opportunity:
    sub_topic_a: Cooking fried eggs
    sub_topic_b: Cooking mashed potatoes
    a_only_features:
      - Easy to mess up
      - Sizzling sound
      - Takes a minute
      - Need a spatula
      - Mrs. James loves the butter
      - Frying pan
      - One main ingredient
    b_only_features:
      - Fun to mash
      - Garvin loves them
      - Gurgling sound
      - Takes an hour
      - Boiling water
      - Hard to mess up
      - Pot
      - Potato peeler
    overlap_features:
      - Cooked on stove
      - Mr. James loves both
      - Salt

  menu_for_dinner:
    - Fried eggs
    - Mashed potatoes
    - Green beans
    - Fresh carrots
    - Snap peas
    - Hummus

  why_this_story_works:
    - Specific enough that all 8 techniques produce distinct content (rare for invented stories to hit this)
    - Has a binary comparison built in (fried eggs vs. mashed potatoes) for the Venn Diagram
    - Has multiple parallel-story possibilities (the narrator could also have written about the handstand, the coat gift, the address memorization) which exercises the Brainstorm technique
    - Has chronological events with enough variety for the Series of Events (14 discrete events)
    - Has sensory richness across all 5 senses for the Five Senses
    - Has one detailed character (Garvin) for the Character Sketch
    - Has a clear narrator stake (pride) for the Freewrite to wander into
    - Has factual content (who, what, when, where, why, how) for 5W and H
    - Has thematic groupability (anniversary, cooking, friendship, mess) for the Cluster

  elevator_pitch: |
    Garvin's parents had an anniversary, so my friend Garvin and I tried to cook
    them dinner even though we had never cooked together before. It was a disaster
    in the middle but they ate everything and I felt amazing.
```

---

## When to use this default

The skill defaults to this source story when no custom source story is provided. Use the default when:

- The teacher has no shared class story to work from and just wants to see the eight techniques demonstrated
- The output should match the Grammaropolis Writing Framework's worked examples
- Consistency with other Grammaropolis materials is the priority

## When to override the default

Use a custom source story when:

- The class has a shared experience worth using (the field trip, the science fair, the assembly), which makes the demonstration land harder
- The teacher wants a Grammaropolis-character source story (e.g., the Mayor preparing a speech for City Hall)
- A theme or unit calls for a different scenario (a Grade 7 persuasive unit might want a debate-focused source story)

When overriding, the custom source story must include all the structured fields above. If any field is thin, the skill cannot produce a high-quality worked-example set.

## Character traits for narrator-led options (Grammaropolis character stories)

If the skill is invoked with a Grammaropolis-character narrator, the source story should be tailored to that character's role on the cast card. Three starting points:

**Mayor story (for City Hall scenarios):**
- Premise: The time I gave a formal address at the Annual Grammaropolis Civic Banquet
- Narrator stake: Defending the dignity of correct grammar against Slang, his frenemy and living proof that language keeps changing
- Setting: City Hall main reception room
- Events: arrival, opening remarks, Slang's interruption attempt, recovery with a particularly elegant subordinate clause, applause
- Comparison opportunity: formal speech vs. informal speech (built into the Mayor's natural concerns)
- Five Senses starting points: dignified visual of City Hall, the sound of Slang's interruption, the taste of mayoral water, etc.

**Nelson story (for Noun Office scenarios):**
- Premise: The time a new compound noun walked into the Noun Office and asked to be registered
- Narrator stake: Maintaining the bureaucratic integrity of the Noun Registry
- Setting: The Noun Office, behind the front counter
- Events: arrival of the compound noun, registration paperwork begins, dispute over which root noun gets primary classification, resolution
- Comparison opportunity: simple noun vs. compound noun
- Five Senses starting points: the smell of file folders, the click of Nelson's pen, etc.

**Jake story (for descriptive scenarios):**
- Premise: The time the world went gray and only adjectives could bring it back
- Narrator stake: Restoring color and texture to a colorless scene through descriptive craft
- Setting: A gray-washed neighborhood, transformed adjective by adjective
- Events: discovery of the gray world, first adjective attempts, the moment color returns, the celebration
- Comparison opportunity: gray version of a scene vs. fully-described version
- Five Senses starting points: every sense activated as the world fills in

These character-story templates are starting points; every line generated in a character's voice must follow the bundled `reference_voice_card.md` and stay within it.
