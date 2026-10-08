---
name: dike-cite
description: Check a legal citation against Dike's index. Use when the user gives a precise citation with a number and year, such as a law, decree, cassation appeal, or fatwa number, and wants to confirm it exists or find the document it refers to.
---

Use this skill when the user provides a specific citation, for example a law number and year, and wants it verified.

1. Call `dike_cite` with the citation exactly as the user wrote it. Arabic formats for legislation, ministerial and presidential decrees, cassation rulings, and fatwas are supported.
2. Report the parsed components: document type, number, year, and article number if present. Then report whether it resolved to a document. If it did, give the title, official number, year, status, and `canonical_id`.
3. If the tool reports that the citation is ambiguous and lists candidate documents, show the candidates and ask the user which one they mean. Do not choose for them.
4. If it did not resolve, say that the citation could not be verified in Dike's index. Do not guess which document it might be. An unresolved citation can mean the document does not exist, is outside Dike's current coverage, or was misquoted.
5. If the user then asks whether the law has been amended or repealed, call `dike_graph_traverse` with the `canonical_id`, or use dike-research.

If the user's explicit instructions conflict with this skill, follow the user.
