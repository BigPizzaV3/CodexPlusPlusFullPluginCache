# Devices and players

OptiSigns runs on OptiSigns-made players and on many third-party devices. It supports far more than it
recommends. Two things separate a good signage player from a weak one:

1. **Autostart**: does the player come back by itself after a power cut? This matters more than any
   spec. A store that has to reopen the app with a remote every morning gives up on signage.
2. **Depth**: video codecs, video walls, multi-zone layouts, remote management, enterprise Wi-Fi.
   This comes from the device's hardware and operating system.

Device capability and plan are separate. A device that can do something still needs the account's plan
to include it (see [plans.md](plans.md)).

## Recommend for a new purchase (OptiSigns hardware)

| Player | Best for |
|---|---|
| **OptiStick** (Android) | Cost-effective pick for marketing and branding screens. Reliable autostart, remote management, offline cache, cheap to scale. Rated for up to 16 hours a day, 7 days a week. |
| **Pro Player** | Always-on (24/7) and enterprise screens: strongest video playback, 4K, can drive up to 3 screens from one player, enterprise Wi-Fi (802.1X), resilient updates, full remote management. |
| **ProMax** | Top of the line: 8K, up to a 4-screen video wall, animation-heavy and multi-zone layouts. |
| **OptiKiosk** | OptiSigns touch-kiosk hardware for interactive (Engage) kiosks. |

Where to buy and current models:
https://support.optisigns.com/hc/en-us/articles/32129032857875. Pro Player availability varies by
region; check that article before promising lead times. Prices: https://www.optisigns.com/pricing.

**Autostart is not duty cycle.** The OptiStick's autostart makes it far better than a smart TV app, but
"always on, 24/7, set and forget" points to Pro Player or ProMax.

## Supported: fine if the customer already has the hardware

These autostart and render web content well.

- **Windows PC**: reliable; good for internal web apps.
- **Linux** (x86 and ARM, via AppImage): Ubuntu, Debian and others, with autostart.
- **Raspberry Pi** (Pi 4/5 image, Pi 3B+ via AppImage): video limited to 1080p.
- **Android boxes, tablets and Android smart TVs** (about Android 9 and newer). Tablets suit kiosk apps
  on small screens. Very old Android or locked displays that block app installs aren't supported; plug
  in an OptiStick.
- **Chromecast / Google TV**: runs the Android player with autostart once "Display over other apps" is
  allowed.
- **ChromeOS / Chromebook**, **macOS**: supported, limited remote management.
- **Apple TV, iPhone, iPad**: good playback in Apple-centric places; limited remote management.
- **Amazon Signage Stick** (Amazon's signage product, not a Fire Stick): acceptable, but recommend an
  OptiSigns player over it.
- **Older OptiSigns players** (Pro Player Gen 2, Ubuntu and Athena builds): fully supported; keep them
  running, but recommend current models for new purchases.

## Works with limits: narrow fit only

Always state the limit.

- **Web player** (a browser): demos, virtual screens, attended low-stakes use. Depends on the browser,
  many integrations can't be embedded, no remote management, no video wall. Never for an unattended
  storefront.
- **BrightSign**: real commercial signage hardware, fine if they own it; little remote control.
- **LG webOS signage displays**: acceptable for customers standardized on LG; LG's own management
  covers reboot, screenshot, HDMI-CEC and storage.
- **Samsung signage (Tizen)**: the app won't install on older Tizen, the refresh control can be
  unreachable while offline, no video wall.

## Never recommend (support what they already have)

Consumer devices without reliable autostart. Never tell a customer to replace a whole fleet; state the
limits politely and offer the cheap fix: plug an OptiStick into the TV's HDMI.

- **Roku**: no reliable autostart; drops social apps, split screen, shuffle, animations and default
  schedule content; older Roku can't run third-party apps.
- **Samsung and LG consumer TVs**: limited app install and navigation.
- **Amazon Fire TV / Fire Stick**: see below.

## Amazon Fire TV / Fire Stick

Never recommend one for signage. When someone asks "what should I buy", answer OptiStick, Pro Player,
ProMax, or a Windows or Linux player.

If the customer already uses one, say it is supported on paid plans and **always** state the limits.

- **Check the plan first.** The Free plan doesn't support Fire TV at all, so a Fire Stick on a Free
  account can't come online. That answer is about the plan or a supported player, not troubleshooting.
  Word it as "Fire TV is supported on the paid plans" plus the better fix (an OptiStick in the TV's
  HDMI); don't write "upgrade".
- **Support is ending.** Amazon has been pulling signage support from Fire Sticks, and OptiSigns plans
  to end Fire Stick support in the near future.
- **Find out which OS it runs** before advising. The limits differ:
  - **Fire OS 8 and newer** (Fire TV Stick 4K, 4K Max, newer TVs with Fire TV built in): **not
    supported**. Amazon removed app autostart. A developer workaround exists but isn't a signage
    solution.
  - **Fire OS 7** (older sticks): autostarts, but not recommended; Fire Stick Lite performs badly.
  - **Vega OS** (newer sticks): supported but strongly discouraged. It **sleeps on a static image**,
    so every playlist for it must include a video. One video decoder, so videos cut, not crossfade.
- **Limits on any Fire OS device:**
  - No reliable relaunch after a power cut. Someone has to reopen the app with the remote.
  - The app may not be listed in the Fire app store on some models.
  - Content can bleed off the edges. Fix it with Calibrate Display, or the TV's overscan setting.
  - No video wall, sync play, AI camera or enterprise Wi-Fi; limited split screen and animation.
  - Remote management is limited to storage and refresh.
  - Recorded logins with two-factor codes don't work. Use Secured Dashboard or a desktop player.
- **4K problems:** don't conclude "can't do 4K" from one failing file. Re-encode to H.265 or lower the
  frame rate.

Help Center hub: https://support.optisigns.com/hc/en-us/articles/27463953562899.

## Quick picks by setting

| Setting | Recommend | Why |
|---|---|---|
| Retail, restaurant, office marketing screen | OptiStick | Cheap, autostarts, remote managed |
| Always-on: lobby, factory, transit, 24/7 store | Pro Player | 24/7-rated, resilient, full management |
| Video wall, 8K, heavy animation, several zones | ProMax | Up to 4 outputs, top performance |
| One player feeding several TVs | Pro Player (3) or ProMax (4) | Needs the Video Wall add-on |
| Touch kiosk | OptiKiosk, or a tablet for small screens | Built for Engage |
| Corporate network with 802.1X | Pro Player, ProMax, Windows, Linux | OptiStick can join 802.1X Wi-Fi from the portal |
| Internal dashboards behind company certificates | Pro Player, Windows, Linux | Root certificates can't be installed on Android |
| Existing smart TVs, Rokus or Fire Sticks | Keep them; add an OptiStick over HDMI | Fixes autostart cheaply |
| Demo or trial with no hardware | Web player | Not for unattended screens |

## Common device answers

- **"Offline after every reboot" on a smart TV**: the TV app didn't autostart. That's the platform, not
  a fault. Turn on any autostart the TV offers, or add an OptiStick.
- **Flicker or a blank screen with an HDMI extender**: connect the player straight to the display.
- **Exact specs** (RAM, codecs, outputs): don't quote from memory. Link the device's setup article:
  OptiStick https://support.optisigns.com/hc/en-us/articles/27267311796243, Pro Player
  https://support.optisigns.com/hc/en-us/articles/32272215514131, ProMax
  https://support.optisigns.com/hc/en-us/articles/38680194603155.
