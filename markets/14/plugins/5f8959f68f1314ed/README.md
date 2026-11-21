# Fernweh – Reiseplanung (plugin)

Plan and take your own trips with [Fernweh](https://www.fernweh.guide), the
curated travel guide, right from Claude. The plugin connects Claude to the
Fernweh travel MCP server and adds a skill that teaches Claude how Fernweh
works: guide content first, outside information clearly labelled, the Fernweh
tone of voice, a sensible planning order, travel mode during the trip, and a
confirmation before anything is deleted.

## What you get

- **Connector** (`.mcp.json`): `https://www.fernweh.guide/mcp/travel`, OAuth
  sign-in with your Fernweh account. Tools for the travel guide (destinations,
  places, curated round trips, best travel time, nearby places), your trips
  (stops, accommodation, transport, day plans, bookings), budget, saved list,
  sharing and hotel/flight search links.
- **Skill** `fernweh-reiseplanung`: tone of voice, workflow and rules.

## Install

Claude Code, in one step (Claude Code 2.1.275 or later):

```
/plugin install fernweh-reise --marketplace felixgillen/fernweh-reise-plugin
```

Or add the marketplace first, then install:
`/plugin marketplace add felixgillen/fernweh-reise-plugin` and
`/plugin install fernweh-reise@fernweh`. For one session only:
`claude --plugin-dir ./fernweh-reise`. Claude (web/desktop): add it from the
directory, upload the zip under Settings → Plugins, or add the connector URL
under Settings → Connectors. On first use you sign in to Fernweh and allow
access.

## What the plugin runs, sends and fetches

- **Nothing runs on your machine.** The plugin has no hooks, scripts or local
  servers; it is a connector address and a skill (text instructions).
- **One server:** every tool call goes to `https://www.fernweh.guide/mcp/travel`
  over HTTPS, signed in with your Fernweh account (OAuth). It sends what the
  tool needs: a search term, a trip id, the stop or expense you add.
- **No other destinations.** The plugin sends nothing to anyone else and reads
  no files, environment variables or credentials from your computer.

## Affiliate links

Some tools return hotel, holiday-rental, flight and rental-car search links
(Booking.com, Agoda, Airbnb, Expedia) and route links (Rome2Rio). Hotel,
flight and rental-car links are affiliate links through Stay22: if you book
through them, Fernweh receives a small commission; your price stays the same.
They are always marked as such. Nothing is sent to those sites unless you
open a link yourself.

## Privacy

The assistant only sees what it asks the tools for: the public guide, your
trips and your saved list. Disconnect at any time in your Fernweh profile.
Privacy policy: https://www.fernweh.guide/de/datenschutz#ki-assistent-konnektor

Support: https://www.fernweh.guide/de/ki-assistent · mail@felix-gillen.de

This repository is a mirror of `plugins/fernweh-reise` in the Fernweh
repository; changes are made there and copied over.
