# ISG3 - Credit Mastery — ChatGPT plugin package

Built with BizInGPT AI for ISG3 - Credit Mastery. Upload this ZIP on the OpenAI Platform: **Plugins → Upload new or existing plugin → Upload plugin**.

## What's inside
- `plugin.json` — the plugin manifest and its directory listing (name, descriptions, category, links, starter prompts, logo).
- `mcp.json` — your hosted plugin server: `https://app.bizingpt.com/api/mcp/f94954e6e1a07d148f671fb794901c4c8f2af0bf` (streamable HTTP, no sign-in). Keep this URL private; it is your plugin's address.
- `skills/` — how ChatGPT should run your workflows: `business-answer-rules`, `business-notes`.
- `assets/logo.png` — your logo, square, used as the listing logo and composer icon.

## Review details (paste these into Review information → Review details)
- Support URL: https://app.bizingpt.com/api/pages/eBa9PJGC10747f703cf74e9f7437d2bd1793f083f/support
- Demo video: https://isg3.com/wp-content/uploads/2026/10/ChatGPT-ISG3-Recording-2026-10-23-162955.mp4
- Reviewer credentials: not needed (no sign-in).

### Positive test cases
1. **Asks about the seminar schedule.**  
   Prompt: What days and times are the in-person seminars?  
   Expected tools: get_class_schedule  
   Expected behavior: Answer using the live class schedule, show the relevant class card, and offer the link to book a free demo class without confirming a booking.
2. **Asks which seminar topics are available.**  
   Prompt: What types of Credit Mastery classes do you offer?  
   Expected tools: list_class_types  
   Expected behavior: List class types and their weekly session counts from live data, show a relevant card, and offer the free demo class link.
3. **Asks where the business is located and how to contact it.**  
   Prompt: Where are you located, and how can I contact you?  
   Expected tools: get_business_info  
   Expected behavior: Provide the address and contact details from live business information, show a business card, and offer the free demo class link.
4. **Asks who leads the seminars.**  
   Prompt: Who teaches the in-person Credit Mastery seminars?  
   Expected tools: list_trainers  
   Expected behavior: Name trainers and their weekly class counts using live data, show a relevant card, and offer the free demo class link.
5. **Asks for a particular trainer's sessions.**  
   Prompt: Which classes does Iron Dane Richards teach on Saturdays?  
   Expected tools: find_classes_by_trainer  
   Expected behavior: Show Iron Dane Richards's Saturday sessions from live data, display the relevant class card, and offer the free demo class link without booking.

### Negative test cases
1. **Unrelated request; the plugin should decline and redirect to seminar information it can provide.**  
   Prompt: Write me a Python script to sort a list of numbers.
2. **Requests direct booking; the plugin should not book or confirm a place and should offer the free demo class link instead.**  
   Prompt: Book me into the next seminar and confirm my seat.
3. **Requests financial advice; the plugin should avoid personalized financial advice and direct the user to appropriate professional guidance or its educational class information.**  
   Prompt: Should I borrow $50,000 for my business, and which loan is best for me?

Generated 2026-10-29 23:21 UTC · version 1.1.202610292320
