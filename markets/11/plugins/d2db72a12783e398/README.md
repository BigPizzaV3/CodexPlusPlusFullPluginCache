# Smart Scale

Draft Agent Plugin package for ChatGPT. Smart Scale for ChatGPT, v0.3.9. See `AUTH-SETUP.md` for the live OAuth endpoints and `PUBLICATION-CHECKLIST.md` for submission status. Website https://scale.asselabs.com , privacy /privacy.html , terms /terms.html , support /support.html .

## User-facing descriptions

**English**

Short: Kitchen scale in ChatGPT

Long: Smart Scale lets ChatGPT read the current weight from a connected kitchen scale, zero the scale, and guide you toward an ingredient weight while you pour. It is designed for everyday cooking, baking, and portioning, with clear instructions.

## Manual test prompts 

1. “How much is on the scale right now?” → `get_weight`.
2. “Zero the scale.” → `tare`.
3. “Help me measure 200 g of flour.” → `tare`, then `wait_for_weight(target_g=200)`.
4. “I added too much.” → expect `result=over`; explain the excess using the returned reading.
5. “The scale is not responding.” → brief, friendly error without technical details.

For review, connect the demo scale; the demo code goes only into the portal's secure reviewer-access field and is never included in the ZIP.
