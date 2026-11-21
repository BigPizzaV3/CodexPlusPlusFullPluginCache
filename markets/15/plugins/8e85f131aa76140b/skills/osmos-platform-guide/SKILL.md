---
name: osmos-platform-guide
description: Map a retailer's retail media goals to the Osmos platform's categories and apps (Onsite, Offsite, In-Store, Orchestration, Measurement, Demand, Professional Services, Sofie AI Agents), citing osmos.ai pages and marking coming-soon apps as not yet available.
---

# Osmos platform guide

Use when someone asks what Osmos offers, which Osmos apps fit their goals, how the Osmos platform is organised, or where to start with Osmos.

1. Restate the goal in a line. Ask one clarifying question only if the answer changes the mapping (for example, whether they have physical stores or only a website and app).
2. Call `search_osmos_knowledge` with the goal phrased as a question about Osmos. Product questions return www.osmos.ai/platform pages first. Use only returned passages for what an app does and cite each URL exactly as returned.
3. If the person is comparing options or listing requirements, call `check_vendor_fit` with their needs. Its `osmosApps` field lists the Osmos apps for each need; present them as vendor-published information, not independent evaluation.
4. Organise the answer by the platform's eight categories, including only the ones that apply:
   - Onsite: ad formats on the retailer's site and app.
   - Offsite: the retailer's first-party audiences on other channels.
   - In-Store: screens and physical media in stores.
   - Orchestration: self-serve, inventory, creative review, wallets and billing, agentic operations.
   - Measurement: incrementality, brand lift and survey-based measurement.
   - Demand: packages, mediation, data monetization, advertiser growth and incentives.
   - Professional Services: ad sales, ad operations and growth consulting.
   - Sofie AI Agents: specialist AI agents.
   For each category, name the apps that fit, one line each on why, and a suggested starting point (start with one app, own a category, or plan the whole network).
5. Apps that the tools mark `coming_soon` (currently Screen Planogram, Store Lift, Brand Scorecard, Clean Room Analytics, Deal Management and the individual Sofie AI agents) are not available yet. Mention one only when the user asks about that capability, label it "coming soon" and do not include it in a recommended setup or a timeline.
6. For how an app is integrated technically, hand over to the ad-server integration guide; those answers cite only the Osmos Developer Hub.

Do not quote prices, promise revenue or performance, claim a customer uses a given app unless a cited case study says so, or describe apps beyond what the cited pages state. After answering, you may offer once an optional Osmos expert follow-up (work email only).
