# Tabularia

Read and revise a [Tabularia](https://tabularia.app) novel, nonfiction book, article, or screenplay with ChatGPT. The plugin connects ChatGPT to your Tabularia account and adds skills that say how a good editor does each job.

## Use it

Add the plugin, then sign in to Tabularia when ChatGPT asks you to connect. Ask in your own words:

| Skill                   | Ask for                                                                     |
| ----------------------- | --------------------------------------------------------------------------- |
| `structural-read`       | "Does my structure work?" "Does the middle drag?"                           |
| `continuity-check`      | "Have I contradicted myself?" "Is the timeline consistent?"                 |
| `line-edit`             | "Tighten this chapter." "Fix the grammar in this scene."                    |
| `prose-read`            | "How does this read?" "Am I repeating myself?"                              |
| `natural-voice`         | "Make this sound less like AI." "Write it the way I would."                 |
| `review-triage`         | "What's waiting for me?" "Where did I leave off?"                           |
| `story-thread-draft`    | "Revise this thread across the book in a draft."                            |
| `story-sheets`          | "Make me a character list." "Update my character sheets from the book."     |
| `story-structure-beats` | "Put my Save the Cat beats where they really happen." "Name these Anchors." |
| `story-shape`           | "Which structure does my book fit?" "Map my draft onto the Hero's Journey." |
| `synopsis-and-query`    | "Write my synopsis." "Draft a query letter."                                |
| `opening-pages`         | "Would an agent keep reading?" "Does my first chapter hook?"                |
| `finish-the-book`       | "Add a title page and drop caps." "Make it look like a real book."          |
| `nonfiction-read`       | "Does my argument hold?" "Is my proposal ready?"                            |
| `article-edit`          | "Improve this blog post." "Is my headline working?"                         |
| `screenplay-read`       | "Give me coverage." "Is my script formatted right?"                         |

ChatGPT works in a draft. Unless you name one, its changes go into a draft of its own, which you read beside the original in Tabularia and merge all at once, one change at a time, or not at all. Ask it to change your text itself and it will, after Tabularia takes a Snapshot. Whether ChatGPT checks with you before each change is up to ChatGPT; every tool tells it which changes only add and which rewrite or remove.

## Data

The plugin runs nothing on your computer. You sign in on Tabularia's own page when you connect, and ChatGPT holds that sign-in.

The connector at `mcp.tabularia.app` reads the manuscripts on the Tabularia account you sign in with and writes the drafts, comments, and edits you ask for. It fetches a picture from outside Tabularia only when you ask for one from Wikimedia Commons, Unsplash, or Flickr. Tabularia does not train on your writing. Whether OpenAI uses your chats to improve its models is a setting in ChatGPT: **Settings › Data controls › Improve the model for everyone**. See the [privacy policy](https://tabularia.app/privacy).
