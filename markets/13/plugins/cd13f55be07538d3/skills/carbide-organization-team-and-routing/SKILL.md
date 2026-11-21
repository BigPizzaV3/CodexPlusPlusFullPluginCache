---
name: carbide-organization-team-and-routing
description: Audit and configure Carbide organization profile, members, staff roles, estimator routing, availability, territories, crews, trades, equipment, and coordination. Use for administrative setup and team routing.
---

# Carbide organization, team, and routing

Start by reading the current state with `get_organization`, member and profile lists, estimator and CSR routing rules, project areas, trades, equipment, coordination, crew members, and crews.

- Use `list_health_check_issues` to prioritize missing setup.
- Make the smallest requested configuration change and re-read it afterward.
- Add staff profiles before assigning their availability, territory, crew membership, trades.
- For production teams, create crew members before crews, then attach members and capabilities with exact IDs.
- A crew's territory is its postal codes: send the complete list to `update_crew_territory` (read the current `zip_codes` from `list_crews` first, since a code left out is removed).
- Treat member deactivation, role changes, removals, and routing rule replacement as consequential. State the target and effect before calling the tool.

## Routing rules

The organization routes estimators and CSRs with ordered rule lists.

- Read `get_estimator_routing_rules` first.
- Each rule is a verb (select, exclude, prioritize, deprioritize) applied to the estimators its qualifier picks: who match or don't match an attribute, with highest or lowest of a ranked value, or chosen estimators.
- Send the complete ordered list to `replace_estimator_routing_rules`; a rule left out is deleted. Run `simulate_estimator_routing` with a realistic request before and after a change, and describe the difference.
- CSR rules work the same way through `get_csr_routing_rules`, `replace_csr_routing_rules` and `simulate_csr_routing`; CSR ids are user ids from `list_dispatcher_profiles`.
- Crew rules (Job Scheduling only) decide which crew Schedule Job (`auto_schedule_job`) places a job on: read `get_crew_routing_rules`, then send the complete ordered list to `replace_crew_routing_rules`. They use the same verbs and qualifiers over customer history, territory, trades and first availability, with crew ids from `list_crews`.

## Estimator settings

- `list_estimator_profiles` returns every estimator setting, preference levels per project area, the performance rate (owners and admins only) and a `settings_url`. Add an anchor such as `#performance-rate` to point a person at one setting.
- Preference levels go through `update_estimator_profile_project_areas`, the rate through `update_estimator_profile_performance_rate`, and "use default" switches through `set_estimator_setting_default`.
- Sales targets: `list_sales_targets`, then `create_estimator_sales_target`, `update_sales_target` or `delete_estimator_sales_target`. Work addresses: `list_estimator_work_addresses` and the create, update and delete tools.

Organization and production-team setup requires `mcp.write` and an owner or administrator role. This includes verified addresses, trades, equipment, coordination, crew members, crews, memberships, leads, and capabilities. Day-to-day job scheduling and job-team changes use `mcp.operate`; underlying Carbide policies remain authoritative.
