# Pairing and remote management

## Pairing

Pairing turns a device into a managed screen in an account.

1. Start the OptiSigns player. It connects to OptiSigns and shows a short pair code.
2. In the portal: Screens > **Add Screen**, enter the code.
3. The screen joins the account and team you're working in, and uses one screen license.
4. Assign content and it starts downloading.

Rules:
- **One account at a time.** To move a device to another account, unpair it first (delete the screen
  in the portal, or Unpair from the device menu). Otherwise the new account sees it as already paired.
  https://support.optisigns.com/hc/en-us/articles/360058700673
- **It needs internet.** No pair code at all usually means a firewall, the internet provider or
  enterprise Wi-Fi sign-in is blocking OptiSigns. Fix the network first, not the app.
- **It needs a free license.** With none, the screen goes to the OnHold folder and doesn't play until a
  license is added or freed.
- **Large fleets** can skip codes: OptiSigns players can ship preconfigured to pair themselves on
  first boot, and Enterprise has mass provisioning.
  https://support.optisigns.com/hc/en-us/articles/4416542923667
- Smart TVs and streaming sticks pair the same way, but may not reopen the app after a power cut.

First screen: https://support.optisigns.com/hc/en-us/articles/360016374813

## Remote management

OptiSigns can manage players remotely from the portal (Screens > Edit > Advanced). It's fullest on
OptiSigns players (OptiStick, Pro Player, ProMax), where the management software comes preinstalled.
Most commands need **Pro Plus or higher**.

| Command | What it does |
|---|---|
| Refresh and Relaunch | Restarts a frozen app without a reboot; works on any device |
| Reboot | Restarts the device |
| Take Screenshot | Shows what's on the screen now |
| Remote Control | Live view you can click into (more than a preview) |
| Add/Remove Wi-Fi, Update Time Zone, Device Info | Network, clock, model, version, IP and MAC |
| HDMI-CEC, RS-232 | Turn the TV on or off |
| Install version, auto update | Control the player version |
| Command history | Log of commands sent |

- **Several screens at once:** Execute Remote Commands targets one screen, a tag group or all screens
  (Pro Player and ProMax).
- **Commands only reach online devices.**
- **Offline alerts** email chosen people when screens stay down past a threshold (Pro Plus). The
  on-screen offline icon is a separate setting.
- **Remote command line** on Windows, Linux and Raspberry Pi is off by default; the account owner asks
  support to turn it on.
- **Third-party devices** get only what their OS allows. On a smart TV, a Fire Stick or BrightSign,
  expect few or no remote buttons.
- **Missing buttons** usually mean the plan doesn't include them or the device isn't an OptiSigns
  player. That's expected, not a fault.

## OptiSigns and company device management

Use both. Tools like Jamf, Intune or Chrome Enterprise manage the device and its operating system.
OptiSigns manages the signage app, content and screen commands. OptiSigns doesn't enroll laptops or
manage arbitrary PCs. For ChromeOS, an OptiSigns template in Chrome device management pairs devices
automatically on boot.

**Conference-room systems** (Zoom Rooms, Microsoft Teams Rooms, Webex) are managed through their own
cloud services with OptiEdge MDM (Enterprise). They support sync, restart app and viewing issues, but
not reboot or screenshot.

## Recovery

- Frozen app: Refresh and Relaunch.
- Remote won't respond, or the device is stuck: plug in a USB keyboard to reach recovery, or factory
  reset, reconnect Wi-Fi and re-pair. Content downloads again from the cloud.
