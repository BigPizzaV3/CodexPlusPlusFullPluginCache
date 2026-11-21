# GovBot Public Lands & Wildfire Perimeters

Independent OpenAI-compatible plugin and direct-agency MCP. Listing name: **GovBot Public Lands & Wildfire**. Five no-auth, read-only tools and three workflow skills produce source-linked land/protection/perimeter briefs with map and date limits. No BLM/USGS/NIFC or OpenAI endorsement.

## Local use
Node24.19.0; `npm ci`, `npm test`, `npm run validate:package`, `npm run package`, `npm start`. Default server binds127.0.0.1:8080. Set exact GOVBOT_ALLOWED_HOSTS, GOVBOT_ALLOWED_ORIGINS and trusted loadbalancer IP only for separately approved restricted hosting. No agency credentials.

Portable plugin archive contains only8allowlisted files: plugin.json, mcp.json, README, license, logo and3skills. Runtime source, cloud config and records are not in the plugin ZIP. Root owns privateChatGPT adaptation/ownappregistration, hosting, actualclienttests/video, websitepublication and finalsubmission. Current ownappstatus is UNREGISTERED. Local validation is not hosted/client/directory acceptance.

## Scope
Sources: BLM national SMA, USGS PAD-US Manager Name, NIFC WFIGS Current Interagency Fire Perimeters. Direct fixed publicagency endpoints only; never frozenGovBot services. Schema closes all caller inputs; no arbitraryURLs/SQL. Landmetadata is not title or legalaccess; overlapping protectionrecords cannot be summed as uniqueacreage. Currentfireperimeters are provisional records, not completehistory, livealerts, evacuation/navigation/safety or spreadforecasts. Missingrecords stayunknown; sourceerrors stayerrors.

Support hello@govbot.ai. Productguide plannedhttps://govbot.ai/plugins/public-lands-wildfire.html. No publicsubmission or availability claimed.
