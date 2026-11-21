---
name: kinpress
description: Make a wedding seating chart from a guest list, as an 18x24 PDF, with a printed foam board available by delivery in the US. Use when the user has a guest list or table assignments and wants a seating chart to print, display or have printed and shipped.
---

# Kinpress workflow

- Call `create_seating_chart` when the user has a guest list or table assignments and wants a chart.
- If guests have no tables yet, help assign them first, and confirm before making the chart.
- Send every name exactly as the user wrote it. Never correct, translate or transliterate a name without asking.
- Compare the guest counts the tool returns with the user's list, and say so if they differ.
- The card shows the chart. Don't repeat the guest list. Use only the links the tool returned.
- To change anything, call the tool again with the full list.
- Don't quote a price or delivery date. The order page has the price, and Kinpress confirms the date by e-mail.
- If the tool refuses a name it can't print, tell the user why. Don't change the name to fit.
- Don't use Kinpress for invitations, place cards, menus or classroom plans.
