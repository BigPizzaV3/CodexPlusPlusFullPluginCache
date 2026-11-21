# How content reaches a screen

## Four building blocks

```
ASSET  ->  PLAYLIST  ->  SCHEDULE  ->  SCREEN
what       order and     when          where
           duration
```

- **Asset**: one playable thing: an image, video, PDF, website, app (weather, calendar, dashboard),
  a Designer design, or a split-screen layout.
- **Playlist**: an ordered list of assets, each with its own duration. Options: shuffle, transitions,
  background audio, scaling. Playlists can contain other playlists.
- **Schedule**: time rules that decide which asset or playlist plays when (see
  [scheduling.md](scheduling.md)).
- **Screen**: the paired device. Any of the three above can be assigned to it.

**A screen plays one assignment at a time.** To combine two playlists, nest them in a parent playlist
or use a schedule. To show several things at once, use a split-screen layout with zones.

**Default item duration** is an account setting (Settings > Preferences > Default item duration). It
applies when an item is added. Changing it doesn't touch items already in a playlist; fix those with
Select All > Edit Duration. The product default is 20 seconds.

## What happens when you assign content

1. You pick the screens: one, several, a folder, or a tag group. You only see screens your role and
   folder permissions allow.
2. OptiSigns checks the content exists and that the plan covers it (interactive content needs
   Engage).
3. The assignment is saved and the player is notified right away. Players also check in regularly, so
   a missed notice never leaves a screen stuck.
4. The player downloads the files and plays from its own storage.

Assign now, or set a go-live time with a schedule.
https://support.optisigns.com/hc/en-us/articles/18988049363859

## "Did my change reach the screen?"

Check three things, in this order:

1. **Was it assigned?** The screen in the portal shows the new content.
2. **Did the player hear about it?** It must be online. A Refresh forces it.
3. **Did the files finish downloading?** A large new video can show a gap on first play until it's
   downloaded.

Old content still showing after a delete: the player still has it stored; refresh and clear cache.

## Offline playback

Players keep a local copy of downloaded content so screens keep playing through internet outages.

| Keeps playing offline | Skipped while offline |
|---|---|
| Images | YouTube and live streams |
| Video files | Social feeds |
| PDFs and documents | Live websites and dashboards |

- Content must **finish downloading while online** first. A screen that never finished has nothing to
  play.
- Changes made while a screen is offline apply when it reconnects. Nothing needs to be re-pushed.
- Storage limits what can be stored locally on the device: OptiStick 16 to 64 GB, Pro Player 128 GB,
  ProMax 256 GB.
- Nothing is lost if a player dies or is reset: the cloud has everything. Re-pair and it downloads
  again.
- Smart TV apps and the web player store content less reliably. OptiSigns players are the
  offline-resilient choice.

## When a screen looks offline

- **The TV says it's online, OptiSigns says offline:** a firewall is likely blocking the OptiSigns
  domains while general internet works. See the firewall article:
  https://support.optisigns.com/hc/en-us/articles/360047275934
- **Black screen, network fine:** an operational schedule may be turning the TV off.
- **Old content plays, new content never arrives:** check that the update and download domains aren't
  blocked.
- **A temporary push never reverted:** set an end time on the temporary content.
