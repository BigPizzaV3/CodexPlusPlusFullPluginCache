---
name: teaching-the-agent
description: Use when the owner wants to change what their AssistantLabs customer-service agent says or knows.
---

# Teaching the agent

The agent answers real customers, so a change here reaches them on their next message. Show the owner what will change before saving.

**No agent yet** (a tool says this connection has no agent): call `get_workspace_setup` first. If it shows an agent, the business has one that this connection can't reach: never make a second; they disconnect AssistantLabs in ChatGPT and connect again, ticking it. Only when it shows none, build it first, as the start skill's **Build the agent** says, from whatever they have: what you already know about the business, their website, a document, past conversations or a few questions.

For a temporary note, or anything the owner tells the agent in their own words, such as "this week we're closed on Friday" or "from now on, deliveries take 3 business days":

1. Add it with `set_extra_instructions`, passing the new line as `add`. It goes after what is there, so nothing needs reading first.
2. Only to rewrite or remove part of the instructions, read them with `get_extra_instructions` and `includePhoneAndEmail` set, change that part, and save the whole text as `instructions`, which replaces what was there.

Phone numbers and email addresses in what the agent knows are hidden when it is read, unless `includePhoneAndEmail` is set. Set it only when the owner asks for one, or before saving an edited copy back. A card number, ID number or password always shows as a placeholder such as `[card number hidden]`, and text holding one is refused. If that happens, tell the owner, and leave that part out or have them type the real detail.

For lasting knowledge, use the tool for that kind of content: `save_agent_faq` for a question and answer, `save_agent_link` for a link, `save_agent_catalog_item` for a product, and `save_agent_guideline` when the owner asks to add to or change the agent's list of rules. List what exists first so nothing gets added twice.

For how the agent sounds, read it with `get_agent_persona` and change it with `set_agent_persona`. For the language it answers in, read it with `get_agent_language` and change it with `set_agent_language`.

After saving, read it back with the same tool you read it with, such as `get_agent_persona` or `get_extra_instructions`, and tell the owner what is now true.
