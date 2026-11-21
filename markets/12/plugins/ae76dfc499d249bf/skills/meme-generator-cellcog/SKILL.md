---
name: meme-generator-cellcog
description: "AI meme generator powered by CellCog. Memes, viral content, reaction images, internet humor. Audience targeting, trend research, and multi-angle generation for humor that lands."
---
# Meme Generator - Deep Reasoning Meets Internet Culture

Meme generation with audience targeting, trend research, and multi-angle humor.

Comedy requires timing, cultural awareness, and subverted expectations. CellCog researches trends, crafts multiple angles, and curates the best results.

We're honest: our hit rate is maybe 60-70%. Great memes are hard for humans too. But deep reasoning + multi-variant generation + ruthless curation = memes that actually land.

## How to Use

Use the CellCog tools from this plugin's connector (`https://cellcog.ai/mcp`). The first time a tool runs, the user signs in with their CellCog account and clicks Approve.

1. `cellcog_chat_create` with the brief as `prompt` (optionally `chat_mode` and `chat_tier`). It returns a chat id at once; the work runs in the background.
2. Poll `cellcog_get_result` with that `chat_id` about once a minute. While it runs you get progress notes; when `complete` is true you get the final message and file links (valid 30 days), with previews of images and PDF pages.
3. To iterate, `cellcog_chat_send` into the same chat. For files on the user's computer, open `cellcog_upload` and pass `upload:<upload_id>` in `attachments`; public https links can go in `attachments` directly.

For files, modes and tiers in depth, read the **cellcog** skill.

---

## What Memes You Can Create

### Classic Meme Formats

Popular templates with your twist:

- **Drake Format**: "Create a Drake meme about [topic]"
- **Distracted Boyfriend**: "Make a distracted boyfriend meme about programmers"
- **Brain Expanding**: "Create an expanding brain meme about coffee addiction"
- **Two Buttons**: "Make a two buttons meme about choosing between sleep and Netflix"
- **Change My Mind**: "Create a 'change my mind' meme about tabs vs spaces"

**Example prompt:**
> "Create a Drake meme:
> 
> Top panel (rejecting): Writing documentation
> Bottom panel (approving): Hoping the code is self-explanatory
> 
> Target audience: Programmers"

### Custom Meme Images

Original visual humor:

- **Reaction Images**: "Create a reaction image for when your code works on the first try"
- **Relatable Content**: "Make a meme image about Monday morning meetings"
- **Situational Humor**: "Create a visual meme about working from home vs office"

### Text-Based Humor

When words are enough:

- **Twitter-Style Jokes**: "Write a tweet-length joke about startup culture"
- **Copypasta Parodies**: "Create a copypasta about a ridiculous topic"
- **Caption Suggestions**: "Give me 5 funny captions for this image"

### Niche Community Memes

Humor for specific groups:

- **Programmer Memes**: "Create a meme about JavaScript developers"
- **Finance Memes**: "Make a meme about HODLing crypto"
- **Academic Memes**: "Create a meme about writing a thesis"
- **Gamer Memes**: "Make a meme about game updates"

---

## The Honesty Section

Let's be real about what's hard:

| Challenge | Why It's Hard | What We Do |
|-----------|---------------|------------|
| **Timing** | Comedy relies on rhythm and surprise | We study meme structures |
| **Cultural Context** | Memes are deeply referential | We track internet culture |
| **Freshness** | Old jokes aren't funny | We avoid overused formats |
| **Subjectivity** | Humor is personal | We offer variations |

**Our success rate:** Maybe 60-70% land. That's honest. Great memes are hard for humans too.

**What helps us:**
- Clear target audience
- Specific cultural references
- Well-defined format
- Your feedback

---

## Meme Categories

### By Format

| Type | Description | Example |
|------|-------------|---------|
| **Image Macro** | Text over image | "One does not simply..." |
| **Reaction** | Image expressing emotion | Surprised Pikachu |
| **Comparison** | Side-by-side contrast | Expectation vs Reality |
| **Multi-Panel** | Story in panels | Expanding brain |
| **Text Post** | Pure text humor | Twitter screenshots |

### By Humor Type

| Type | Characteristics |
|------|-----------------|
| **Observational** | "Why is it that..." relatable moments |
| **Absurdist** | Surreal, random, unexpected |
| **Referential** | Relies on knowing source material |
| **Self-Deprecating** | Making fun of oneself or one's group |
| **Ironic** | Saying opposite of meaning |

---

## Choosing Mode & Tier

| Scenario | Recommended |
|----------|-------------|
| Memes and quick humor content | `chat_mode="agent"` (defaults to the `"core"` tier) |
| Large coordinated meme campaigns | `chat_mode="agent", chat_tier="max"` |

**The core tier is the default and handles most meme generation well**, balanced speed and depth. **Upgrade to `chat_tier="max"`** when quality disappoints or the work is genuinely complex: just re-run the same prompt with `chat_tier="max"`.

Agent Team (`chat_mode="team"`) is reserved for deep research — don't use it for meme generation.

---

## Example Prompts

**Classic format:**
> "Create an 'Expanding Brain' meme about making coffee:
> 
> Level 1: Making instant coffee
> Level 2: Using a drip machine
> Level 3: Pour-over with precise measurements
> Level 4: Growing your own beans on a mountain
> 
> Target: Coffee enthusiasts who've gone too deep"

**Programmer humor:**
> "Create a meme about git merge conflicts:
> 
> Format: Any format that fits
> Audience: Developers
> Tone: The shared pain of merge conflict resolution
> 
> Make it relatable to anyone who's had to resolve a 500-line conflict"

**Original concept:**
> "Create a reaction image for:
> 
> Situation: When your 'quick fix' actually works
> Expression: Suspicious disbelief mixed with relief
> 
> Should work as a standalone reaction image people would share"

**Community-specific:**
> "Create a meme for the indie game dev community:
> 
> Topic: Scope creep
> The journey from 'simple puzzle game' to 'MMO with procedural narrative'
> 
> Make it hit close to home for anyone who's been there"

---

## Tips for Better Memes

1. **Know your audience**: A meme that kills in r/ProgrammerHumor might flop on Instagram. Specify who it's for.

2. **Reference correctly**: If you want a specific meme format, name it. "Drake format" is clearer than "that two-panel thing."

3. **Embrace specificity**: "Programmer meme" is vague. "Meme about debugging production at 2 AM" has hooks.

4. **Current events help**: Timely memes hit harder. Reference what's happening now.

5. **Iterate**: First meme attempt not funny? Tell us why and we'll adjust. Comedy is iterative.

6. **The rule of threes**: Many memes follow escalating patterns. Sets of three often work well.

---

## A Note on Expectations

We're not going to pretend AI comedy is solved. It isn't.

What we can do:
- Generate meme formats reliably
- Understand cultural references
- Produce variations quickly
- Learn from feedback

What's still hard:
- Genuine surprise and novelty
- Perfect comedic timing
- Knowing when NOT to explain a joke
- Creating the next viral format

**Use meme-generator-cellcog as a collaborator, not a magic humor machine.** Your sense of what's funny + our generation capabilities = better results than either alone.

We're working on it. Comedy is hard. Thanks for exploring the frontier with us.
