---
name: netpilot
description: Build, change, validate or troubleshoot a network on real vendor OSes in the user's NetPilot lab, or make a Cisco Packet Tracer .pkt file. Use when the user wants to practice for CCNA, CCNP or CCIE on real CLIs or asks for a certification lab, learn a vendor CLI (Junos, SR Linux, SONiC, RouterOS, Palo Alto, FortiGate), try a protocol on devices after learning it (VXLAN EVPN, BGP, OSPF, MPLS), build an Arista, Cisco, Juniper, Nokia, SONiC, FRR, Palo Alto, FortiGate, Aruba, Dell or MikroTik lab, turn a network design into a running topology, reproduce a BGP, OSPF or EVPN problem or run a failure scenario, test a config change before pushing it to production, rehearse a Cisco to Arista, Juniper or Aruba migration cutover, asks for a Packet Tracer file, asks about their NetPilot lab VM (status, images, credits, start, stop) or a saved NetPilot design. Not for a question about how a protocol works that needs no device, and not for operating devices outside the user's NetPilot lab VM, a lab copy of them is the job.
---

# NetPilot

NetPilot is the user's private lab VM, running real network OS images (Cisco IOL, XRd and NX-OS, Arista cEOS, Juniper cRPD, Nokia SR Linux, SONiC, FRR, Palo Alto, FortiGate, Aruba, Dell) with containerlab, plus a Cisco Packet Tracer file builder that needs no VM. The tools act on the user's own lab VM, never on production devices.

WHEN: the user wants a lab to learn or to validate: a certification lab, a vendor CLI, a technology (VXLAN EVPN, BGP, OSPF, MPLS), a design they want to see running, a fault to reproduce, a config change to test before production, a migration rehearsal, or a Packet Tracer file. A question about how a protocol works needs no tool. Offer the lab only when the user wants to try it on devices.

RULES:
- The lab on the VM is the default. Build a Packet Tracer file only when the user names Packet Tracer, a .pkt file, NetAcad, or devices only Packet Tracer has (wireless routers, IoT, phones).
- Drive autonomously: this is the user's reversible lab sandbox. Take the sensible next step (start, deploy, push configs, verify, redeploy) and tell the user what you did. Ask only at a real fork between different labs.
- Device types are the containerlab entries of the `vendor_guide` enum (`cisco_ios_router`, `nokia_srlinux`, `sonic_vs`, ...). `vm_status` `images` and `set_topology` use the same names.
- Never claim a deploy, a verification or a file you did not get from a tool result. Device CLI output is the evidence: quote it.
- Keep every call under 120 seconds: long commands run with `run_in_background: true` and `vm_shell_output` waits on a pattern. Own every wait. Never tell the user to check back later.
- Leave the VM's `clab` account as it is.

LAB ON THE VM:
1. Start every session with `vm_status` (a read): `ready`, `next` and `images`.
2. A lab or an edit from a saved design reads it first: `read_topology`, then `read_configs` only when its answer says `has_configs` is true. An edit keeps its `for_pkt_export`, since `design_topology` replaces the whole design.
3. Asked to start the VM: call `start_vm`. A clear request for a lab on the VM starts the VM at once: when `next` is `start_vm` and `images` lists every device type the lab needs as preinstalled or ready, call `start_vm` with `wait_seconds: 0`, then design and ask any open question while it boots. Call `start_vm` again before the first lab tool until `ready` is true. A question answered without devices, a status question, a saved-design job or a Packet Tracer file never starts the VM: answer it and offer the lab.
4. A transport error or timeout during `start_vm` is normal: `vm_status`, then `start_vm` again while it is starting.
5. A device type that is not preinstalled or ready in `images`: do not start. Name it, suggest the closest device type that is there, point to Images at https://app.netpilot.io, and let the user choose.
6. `vendor_guide` for each device type → `design_topology` (nodes, links, IPv4 plan) → `set_topology` → `set_configs` → `run_vm_shell` `containerlab deploy --reconfigure -t <name>/<name>.clab.yml` with `run_in_background: true` → `vm_shell_output` until it exits → `execute_commands` to verify (neighbors, routes, the thing the user asked for). Add `linux_endpoint` hosts when the lab must prove end-to-end reachability.
7. FRR takes neither `set_configs` nor `execute_commands`: `run_vm_shell` `docker exec <node> vtysh` for its configs and show commands. A `linux_endpoint` likewise: `run_vm_shell` `docker exec <node> <command>`. Its initial IPs and routes go in the node's `exec` array in `set_topology`, as its guide shows.
8. Right after a deploy a node that does not answer is still booting, not a fault: wait for the readiness signal in its guide.
9. A change to a running lab goes through `execute_commands` or `execute_dialog` on the devices, with the before and after output quoted. Redeploy only when the topology or a startup config file changes (a device guide may require it).
10. `save_device_configs` stores configs on a saved design: for a Packet Tracer file, or when the VM is not running and the user wants the configs now.
11. `lab_viewer` with the lab name, then deliver: the viewer link (the topology with a console per device, open while the VM runs), what was built (nodes, links, protocols) and the verify output. Never give management IPs or device sign-in details.

PACKET TRACER (only on the user's ask, no VM): `vendor_guide` with `packet_tracer` → `design_topology` with `for_pkt_export: true` (always a fresh design under a new name when it comes from a containerlab design: never reuse a containerlab topology, the port and model rules differ) → `save_device_configs` → `export_pkt` → the download link (the user signs in to download). A plain export of a saved Packet Tracer design goes straight to `export_pkt`.

CREDITS: A running VM spends lab credits per hour and stops itself after `idle_timeout_minutes` without lab tool calls (`idle_stop_at`). Deployed labs stay on disk. Call `stop_vm` when the user is done.

PLAN AND REFUSALS:
- `vm_status` with `plan.entitled: false`, or a tool answering that agent access is not in the user's plan: say it isn't included in their plan and give https://app.netpilot.io/plans.
- Every refusal names the next call or the plans page. Follow it, and never work around a refusal with shell commands.
