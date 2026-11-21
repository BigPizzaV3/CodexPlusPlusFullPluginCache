# Psiri Vibes

Private plugin for hotel information, room selection, reviews, rates, and availability.

## Connection

- Endpoint: https://api.rateparity.com/mcp/property/PSIRIVIBES
- Transport: Streamable HTTP
- Authentication: None, per supplied RateParity MCP documentation.
- Property code: PSIRIVIBES, supplied by the creator.

## Verification status — 2026-09-30

The initialization request reached the host but returned HTTP 404 with “response 404 (backend NotFound), service rules for the path non-existent”. This suggests the public route is not deployed or routed on this host. Live tool discovery and functional calls remain unverified. Tool workflows are based on the supplied mcp.md, not a successful discovery response.

The server operator should expose POST /mcp/property/PSIRIVIBES and ensure this property's active=true and chatbotSubscription=PRO eligibility. Then initialize with Content-Type: application/json and Accept: application/json, text/event-stream, send notifications/initialized, inspect tools/list, and verify get_property_info returns Psiri Vibes. Test room, review, monthly-rate, and explicit future-date availability and shopper requests before relying on live results.

Expected tools: get_property_info, get_property_rooms, get_property_reviews, get_property_lowest_monthly_rates, shop_property_rate, get_property_availability_single. No reservation mutation tools are documented.

## Branding

Official logo sourced from https://code.rateparity.com/psirivibes/logo-V2.svg and framed in square SVG assets. Brand pink #ED0677 and yellow #F9ED1A were read from https://www.psirivibes.com/. Branding was requested by the creator. No claim of public listing or completed hotel booking is made.
