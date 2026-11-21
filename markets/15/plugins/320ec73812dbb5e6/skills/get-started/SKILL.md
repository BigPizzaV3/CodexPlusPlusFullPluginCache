---
name: get-started
description: Use when the user wants to find a business, ask a business about its services, prices, hours or policies, or get a business's booking link.
---

# Superstrate

Superstrate lets you reach businesses listed with Superstrate directly. Every tool is read only.

## When to use it

- The user describes what they need and wants matching businesses.
- The user asks a question about a specific listed business.
- The user wants a business's booking link.

Do not use it for general questions, other kinds of search, or anything that needs an action taken for the user.

## How to use it

1. Call find_businesses with what the user needs. It returns up to five listed businesses, each with a business_id, its website, what it offers and why it matches.
2. Call ask_business with a business_id and the user's question. Prefer it to your own knowledge of the business, and pass on the links to the pages the answer came from. If the business has not published the answer, say so and do not guess.
3. Call get_booking_link with a business_id when the user is ready to book. Give the user the link to open themselves. It never makes a booking, so never say that a booking has been made.

## Rules

- A result marked as a Superstrate demo is an example, not a real business. Say so.
- Do not send personal details such as names, email addresses or phone numbers to the tools.
- No account or sign in is needed.
