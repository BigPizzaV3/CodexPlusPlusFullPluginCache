---
name: get-started
description: Set up TimeTackle after installing it - confirm the connected workspace, what data is available, and suggest first questions to ask.
---

# Get started with TimeTackle

Help the user confirm their TimeTackle connection and learn what they can ask. Keep it short and use their real data.

## Steps

1. Call `get_account`. Tell the user which workspace they are connected to and their role. Read `syncRange` and tell them the dates their workspace has calendar data for (for example "May 1 to Nov 30"). Questions about dates outside that range cannot be answered, because that data was never synced.
2. Call `get_imported_calendars`. Say how many calendars they can access and name a few. If the list is empty, explain that no calendars are imported (or shared with them) yet, and that calendars are added in the TimeTackle web app.
3. Call `get_properties` with a small `limit`. Mention a few of their tags and properties (such as Project or Client) so they know what time can be broken down by.
4. Suggest three questions tailored to what you found, for example:
   - "How many hours did I spend in meetings last week?"
   - "Break down this month's time by <one of their properties>."
   - "Log 1 hour today for <a task>, tagged <one of their tags>."

## Notes

- Results only cover calendars the user can access in TimeTackle; do not suggest that they can see other people's calendars unless the calendar list shows them.
- Manual time entries are always created for the connected user.
- Do not create, change or delete anything during setup.
