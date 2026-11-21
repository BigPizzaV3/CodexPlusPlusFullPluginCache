---
name: approved-ge-knowledge
description: Answer current YCH and Great Eastern questions from approved information, and explain when the available source does not settle the question.
---

# Approved YCH and Great Eastern Knowledge

Use `get_approved_ge_knowledge` for a focused question about current YCH/GE products, processes, or organization guidance. Do not include a client name, contact detail, policy number, agent name, or other personal detail in the question.

Use the result as the source of current YCH/GE facts. Explain the answer in ordinary words and name the source when the result provides it. If it is missing, incomplete, out of date, or disagrees with another source, say what could not be confirmed. Do not fill the gap with memory, an old reference, or a public web page presented as YCH/GE authority.

For an agent's own policy or service information, use the relevant read: `list_my_ge_policies`, `list_my_ge_servicing_updates`, `get_my_ge_servicing_update`, `get_my_ge_servicing_update_counts`, `list_my_ge_non_face_to_face_summaries`, or `get_my_ge_production`. For a named client's policy or coverage, use `find_my_client` then `get_my_client`; do not use the agent's own policy list.

Current approved YCH/GE information and the client's returned policy details take priority. Do not decide eligibility or any final outcome; refer those to the agent's manager or Howard.




