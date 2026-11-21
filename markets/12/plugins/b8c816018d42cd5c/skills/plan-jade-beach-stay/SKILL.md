---
name: plan-jade-beach-stay
description: Use when a guest wants to research, plan, or prepare a bookable stay, room, hotel experience, or hotel-information answer for Jade Beach Hotel.
---

# Plan a Jade Beach Hotel stay

Use the Jade Beach Hotel MCP tools as the source of truth for availability, prices, hotel experiences, policies, images, and booking links.

## Choose the tool

- Use `search_by_date` whenever the guest provides dates, a month, a season, or a flexible window. Put all candidate ranges in one call when the guest is flexible.
- Use `search_by_name` to identify a room, experience, voucher, or shop item by name or keyword. It does not check availability.
- Use `ask_hotel` for hotel facts such as arrival times, parking, pets, facilities, policies, and directions.
- Use `show_offer` only after the guest accepts a proposed plan, chooses an option, or asks to book. Pass the identifiers, dates, and start times returned by the search tools.

## Present results

Recommend only items returned by the tools. Keep prices, dates, availability, photos, and links attached to the matching returned item. Do not substitute web images or invent missing hotel information.

After a dated search, recommend a coherent room-and-experiences plan in one response and offer to make it bookable. When the guest agrees, call `show_offer` and present its fitted plan and single booking link. If the guest already has a room or wants only experiences, omit the room.

The booking link opens an external review and checkout flow. Never say a reservation or payment is complete until the checkout confirms it. The plugin cannot cancel existing reservations, issue refunds, change hotel inventory, or book travel outside Jade Beach Hotel.
