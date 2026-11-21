# BookGuard acceptance tests

These tests validate workflow behavior, **not assertions about real books**. For tests using real books, the plugin must research and cite current primary sources before concluding.

1. **Series metadata:** Ask `Screen [known series] book 1 for ages 13 and 17, and verify all sequels.` Should report position and published vs announced volume counts with evidence. No blanket safe series label unless each published volume screened.
2. **Problematic sequel fixture:** Fictional series: Book 1 all categories 1–2; Book 2 sexual 4 with source; Book 3 violence 5 with source. Expect age 13 Book 2 **Not Recommended** and earliest issue Book 2; age 17 Book 2 **Caution**, Book 3 **Caution**. Do not invent citations from this fixture.
3. **Unknown volume:** Fictional trilogy with verified Books 1, 2 and missing evidence for Book 3. Series outcome **Series Not Fully Verified**, not Appropriate, for both ages.
4. **Announced future volume:** Three published and one announced. Show `3 published, 4 announced`, future book unknown, and no promise that it is safe. If publisher describes series as ongoing do not call the completed body a fully completed series.
5. **Sensitive topic:** Book with cited sexual assault even if other categories rated low. Prominent review flag and Caution for both ages.
6. **Unsubstantiated warning:** A catalog blurb describes a dark story but supplies no direct content evidence. Return **Insufficient Evidence**, not a fabricated violent-content score.
7. **Same-title collision:** Multiple works share a title. Verify author and edition; do not merge series or reviews.
8. **Novella ordering:** Numbered series contains a `1.5` novella. Identify main sequence and optional novella distinctly; check novella too if part of requested complete reading order.
9. **Spoiler safety:** Review a mystery book without naming plot twists, culprit, character deaths, or endings.
10. **Age differential:** Sexual rating 4 implies age 13 Not Recommended versus age 17 Caution; profanity 4 should not automatically disqualify a 17-year-old.

11. **Single age:** Age 14 returns age-14 only, without implying two children.
12. **Unspecified age:** Ask optionally once; if skipped, deliver content-only review.
13. **Younger reader:** Age 10 uses 8–12 standards.
14. **Adult reader:** Age 19 receives content/preference guidance, not teen parental ratings.
15. **Multiple ages:** Ages 11 and 16 get separate outcomes and earliest concerning sequel.

16. **Triggered alternatives:** Age 12, fantasy series flagged Not Recommended for sexual content: automatically offer cited, similarly magical/adventurous but lower-sexual-content titles.
17. **Caution alternatives:** A Caution title offers optional substitutes, without implying the original is banned.
18. **Series alternatives:** Do not certify a recommended series if later installments have not been screened; note earliest problematic sequel.
19. **No age:** No automatic age-specific safer picks if reader age is skipped.
20. **Theme fidelity:** Dragon-rider request gets fantasy/dragons/adventure rather than unrelated children's books.
