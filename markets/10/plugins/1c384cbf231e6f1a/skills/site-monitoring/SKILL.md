---
name: site-monitoring
description: Use when the user wants a website watched over time, their own or a client's: monitor a site for new SEO problems, get an email when something breaks or changes, see which sites are monitored, or stop monitoring a site.
---

Set up, list or stop Sitewalk monitoring for a site.

1. Monitoring works on a site that has been audited before. If the user has not audited the site, run the audit as usual first, then continue.
2. To start, call `monitor_site` with the site address. Show the user the message it returns, including how often the site will be checked.
3. To see what is monitored, call `list_monitored_sites`. To stop, call `stop_monitoring` with the site address, after the user confirms which site.
4. Tell the user what happens next, using the tool's own message: Sitewalk checks the site again on the schedule and emails them only when something changes.

Say only what the tools return about schedules and limits. If a tool says a schedule is not available, relay its message as it is.
