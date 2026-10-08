---
name: whatchanged
description: Use when the user asks what has changed, moved, or shifted in the 2026 US midterm race ratings or forecast — "what's new in the forecast", "which races moved", "any rating changes lately". Compares published revisions of the data with ratings_changed.
---

# Show what moved in the forecast

Call `ratings_changed`. With no arguments it compares the two most recent published
revisions. If the user names revisions, pass them as `fromRevision` and `toRevision`.

## Reporting the result

- Lead with the biggest moves. A Safe seat becoming a Toss-up is the news; a one-notch
  drift is not. The tool already returns them in that order.
- If nothing moved, say so plainly. That is a real answer, and a common one between
  revisions.

Say exactly what a change is: **a forecaster revised their view of a race that has not
happened.** Never write it as though something happened in that state or district.
