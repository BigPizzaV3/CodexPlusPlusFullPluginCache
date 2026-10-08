# Using the TPNote App

## Weather

Open an upcoming event that has a place or map location to see its forecast on iPhone, iPad, or Mac. TPNote uses the event's resolved place location, not current weather. Completed events show no weather section. Weather is generated on demand, so it is not included in portable `.tpnote` files and does not require a CloudKit schema change.

When a scheduled event is within the next nine days, opening it shows a forecast at its event time. Ongoing events show the remaining forecast from now. Expand **Hourly forecast** to see conditions from up to two hours before the event through two hours after it ends, when forecast data is available, plus the day's high/low and rain chance. Temperatures are rounded to whole degrees. You can refresh the forecast; it is loaded in event details and kept in a bounded in-memory cache for the app session until refreshed. Events farther away show that the forecast will be available closer to the date. Forecasts are estimates and do not modify or sync trip data. After the user confirms the complete editor draft for a new or replacement Apple Maps place, TPNote saves the event and then resolves its Google Place ID and prewarms its thumbnail in the background. After upgrading, TPNote also performs one background migration after the initial CloudKit reconciliation: legacy events without Google IDs are resolved sequentially, duplicate Apple place identities share one lookup, photos are not prefetched, and one CloudKit synchronization is requested after the pass. The migration does not delay app launch and does not repeat after completion. Events with the same Apple Maps place identity reuse that ID; matching address text alone never merges places. Opening a located event automatically loads the Essentials compact Google place component once for that editor presentation, including its photos, rating, and business information. TPNote stores only the durable Place ID; Google manages its Places data and on-device cache. If automatic resolution did not find an ID, the editor performs one fresh IDs-only lookup before showing the component. Agenda thumbnails remain a separate REST photo path: they only request Google photos for events that already have a Google Place ID, reuse one of up to 160 self-evicting in-memory entries for the same place, and do not perform paid text searches while the user scrolls. Media inside the compact UI component does not add a Place Details Photos charge, but agenda thumbnails use that separately billed photo SKU and may request the network again after relaunch. TPNote does not offer an unsupported Weather app link; the small **Data sources** link is required WeatherKit attribution, not a way to open the Weather app.

If Weather reports authorization code 2, the request reached WeatherKit but Apple's authorization failed before weather data was returned. Check the TPNote App ID's WeatherKit setting under both Capabilities and App Services in Apple Developer and confirm developer agreements are current. If those are already enabled, contact Apple Developer Support with the error code. Retrying or changing the event's address will not fix this account-level failure.

## Place names and event titles

Build 23 also uses linked place coordinates, address, category and contacts. A transit event at a hotel retains its transit marker, but its place card uses the hotel's category. Ordinary event edits cannot overwrite the linked place with a stale location snapshot. Saved contacts remain available when a matching Apple Maps result omits them. Search results without a close name/location match fall back to the saved location.

An event's place card displays its saved address first. Apple Maps supplies an address only when the event has none saved, so a device-specific live lookup cannot change the address shown for a synced trip.

Map pins and place cards show the linked place name, not the activity title. Use an event title for `Check in at Conrad Tokyo`, event Notes for arrival instructions, and Booking details for reservation numbers and stay dates. The place name itself should be `Conrad Tokyo`. Build 22 prefers linked place names over older descriptive subtitles without deleting those subtitles. If an imported place name is also wrong, replace its location using Search Maps or Pick on Map; do not assume the app can infer the correct business from coordinates or booking text.

Use this reference for user questions about the TPNote interface and workflows. Give concise, ordered instructions for the requested task rather than reciting the whole guide.

## Main controls

On a true cold launch, TPNote briefly shows **Preparing your trips** while local data and the planner workspace warm and the first CloudKit check begins. This screen has a short upper limit and does not wait indefinitely for the network. It does not reappear when returning from the background; any unfinished synchronization continues quietly.

- Tap the trip name in the top bar to open the plan menu and switch plans.
- The top **+** menu adds dated events, places, notes, unscheduled ideas, and dates.
- The list icon shows or hides the selected date's itinerary.
- The horizontal date strip changes both the itinerary and map.
- A horizontal swipe across Agenda or Timeline gives the itinerary body a short, screen-responsive drawer pull, then parks it while the finger continues. Crossing the release threshold gives one selection haptic. Moving back pulls the body toward center and cancels the change; releasing beyond the actual distance threshold changes dates without velocity prediction. The Agenda/Timeline control stays fixed above the body. TPNote never keeps two list trees layered together and does not preload neighboring lists or thumbnails.
- Numbered map markers match the current event order and open their event.
- The itinerary opens in a compact preview so the map remains visible. The grabber sits inside the shorter date header. Drag the grabber or date title upward to move through compact, split, and full-screen itinerary views. The panel locks onto vertical movement, freezes its current dimensions, and moves its header, dates, mode control, and rows together. After reaching the selected top edge, it performs one nonanimated layout update to fill the destination height; temporary empty map space during expansion is preferable to rows repeatedly relocating. Settling does not bounce, and release velocity is bounded so a short flick does not overshoot the intended height. Dragging the date controls does not activate Rename Date. In a full-screen Agenda already at its first item, a deliberate downward pull returns to the split view for easier one-handed use. Full screen hides the map search bar, and the chevron remains a quick collapse or restore control.

## Plans and dates

TPNote remembers the last selected plan and date locally on each device and restores them after relaunch. This navigation preference is not shared through CloudKit, and a trip that loads earlier during synchronization does not replace the remembered choice.

The plan menu contains **New Plan**, **Import Plan**, **Export Plan**, **Trip Settings**, **Getting Started**, and **Collaborate** or **Manage Collaboration**. Once a portable export is ready, **Send Plan File** can share that snapshot.

**New Plan** asks for the trip name, start and end dates, and destination time zone. TPNote creates every date in that inclusive range in one operation and opens the first date. Using the same start and end creates a one-day trip.

Use **Add Date** from the **+** menu, then choose **Single Date** or **Date Range**. A single date can have a custom title. Rename the selected date with the pencil beside its title, or touch and hold a date card for **Rename Date** and **Delete Date**.

An empty date shows direct **Add Activity**, **Find a Place**, and **Add Note** actions. In the compact map preview, use the empty card's **+** menu to reach the same choices without expanding the panel. Expanded and wide layouts show the direct buttons. Empty Unscheduled follows the same pattern for saving an activity or place before choosing a date. On first launch, TPNote presents a four-page welcome tour explaining the trip switcher, collaboration, add menu, search, date navigation, itinerary views, map markers, unscheduled ideas, event actions, and reactions. Open **Getting Started** from the trip menu or question-mark button on iPhone, the **More** menu on iPad, or the sidebar and **More** menu on Mac to view the tour again at any time. The tour is local, makes no network requests, and does not add prompts to activity or note editors.

TPNote displays each date's localized weekday, month, and day using that day's destination time zone in both the horizontal date strip and the wide iPad or Mac sidebar. A Tokyo itinerary should keep its Tokyo calendar dates even when viewed from a device in the United States. Generated `.tpnote` files must use the appropriate IANA time zone identifier for every date.

New dates inherit the trip's destination time zone. On an empty date, the first selected Apple Maps place can establish the destination time zone, so new activities use that location's local date and clock time. Moving an activity to another date preserves its local clock time and duration. Changing its start in the iPhone or iPad editor keeps the duration until you edit End separately. TPNote does not rewrite older saved times automatically; if a timeline block is unexpectedly long, check whether the event's End field says AM or PM.

On Mac, event times and the editor use the selected itinerary day's destination time zone. Selecting an event recenters its place in the map column beside the inspector. **Collaborate** or **Manage Collaboration** opens the native Mac CloudKit sharing manager for invitations, participants, permissions, and stopping a share.

**Trip Settings** changes the shared theme. An owner can delete the trip; a participant sees **Leave Trip**, which removes the local shared trip without deleting the owner's copy.

## Events, places, and notes

For the selected date, the **+** menu offers:

- **New Activity** for manual event entry.
- **Find a Place** for Apple Maps search and location selection.
- **New Note** for date-level information.

On iPhone and iPad, tap anywhere in an event card or tap its map marker to edit it. The editor supports name, start and end time, timeline role, category, location, notes, booking details, weather/place information, and reminders. Start and End each use separate native date and time controls, so the two rows keep the same date style and move together into a narrow-layout fallback when needed. End may equal Start, but it cannot be earlier. Activity and note detail panels can be dragged from preview through split to full screen; full screen provides a larger writing area for long notes. Opening the keyboard does not change the selected panel height or move the complete panel upward; scroll content keeps the focused field reachable within the stable editor. The title and action/close controls remain visible while the rest of the detail scrolls. Editors stay focused on one item and do not include previous/next item buttons. New activities, places, and notes remain temporary, and edits to an existing item remain in a detached draft. For an event, the checkmark replaces the **...** action menu in the same header position whenever the draft has changes; it commits the complete draft while leaving the editor open, then disappears until another change is made. X discards changes made since the last confirmation and closes the editor. A deliberate swipe from the left edge to the right performs that same cancel-and-close action; short or mostly vertical drags do nothing. Booking details, reminders, and replacement locations use the same transaction. When the event is clean, its **...** menu supports move to another date, move to unscheduled, and delete.

In a full-screen Agenda or Unscheduled list, the list keeps control of a drag that begins while content is scrolled. Only a deliberate downward pull that begins when the list is already at the top returns the panel to the split map-and-list view. Changing panel size preserves the visible list position.

Choosing **Add booking details** immediately replaces the add button with an editable draft section. The linked booking is created only when the complete event draft is confirmed, so X can discard it together with the other edits. Expand the booking and choose **Add Attachment**, then use its compact source menu to select **Photo Library** for a provider-issued QR screenshot or ticket image or **Files** for one or more image or PDF tickets. Each attachment may be up to 5 MB. The files remain drafts until the event checkmark is selected; X discards pending selections.

Closing an editor reveals the retained itinerary without animating row changes made while the editor was open. This keeps the list stable after changes such as switching an event's Timeline role.

Duplicating an event creates an independent saved place link. Choosing a different place for one copy no longer changes the other copy's address or map location.

Repeated events at the same named place on one date share a map marker such as `4/8`. Tap that marker to choose which event to open. Separate businesses at the same coordinates keep separate markers.

Use timeline role **Event** for normal activities. Use **Background** for a hotel stay or other long context that intentionally overlaps scheduled events.

## Agenda and timeline

**Agenda** is the ordered event list. **Timeline** is a daily time grid; overlaps receive separate columns and background events span behind them. Tap the fixed segmented control to switch views; swipe horizontally in either body to switch dates. Each touch locks to its first clear direction, so a vertical list scroll that later moves sideways stays a scroll. Releasing a genuine date swipe over an event or note does not open that item's details; use a separate tap to open it. A committed change moves one active body at a time, replaces its date while it is offscreen, preserves each date's scroll memory, and honors Reduce Motion.

Itinerary cards, floating panels, and every date tile have a one-point trip-theme outline blended with an appearance-aware contrast layer, keeping pale themes distinct from the map. The selected date uses a stronger accent edge. Agenda/Timeline retains the original compact native segmented-control style with a thin outline around the complete control.

Agenda event cards use compact subheadline titles, smaller metadata and 60-point thumbnails in an 80-point row. Text-led note cards use a 56-point row. Events retain their action and reaction controls, while the denser sizing lets the itinerary display more entries without additional loading work.

When a resizable itinerary or unscheduled panel is released, TPNote fixes the list at its destination layout and animates only the panel position. The list should settle without a final bounce or visible relayout.

The itinerary panel has three heights: compact preview, split map and itinerary, and full-screen itinerary. On medium and taller screens, the complete split itinerary surface occupies 60 percent of the available planner height; very short screens preserve a minimum usable height. On compact iPhone layouts, the workspace and draggable panels extend through the bottom safe area for extra usable height, while the resting bottom bar and scroll content retain device-specific home-indicator clearance. Event and note editors use the same split height. Shared typography roles keep panel titles, row titles, compact controls, and metadata aligned across the planner and editors. Form sections use six-point spacing and 44-point touch rows; date, event-type, transport, and note-type controls use compact labels. Paired controls stay side by side when they fit and stack automatically in narrow windows or at larger text sizes. The Apple Maps section uses a smaller header and 34-point visual buttons inside 44-point touch targets. Moving the itinerary to split height fits all current date markers inside the actual map area exposed between the header and panel. The camera uses that area's width, height, and aspect ratio and keeps extra clearance around pin heads at each edge. Opening an event uses the same geometry for its selected marker. The camera updates once after the target panel state is chosen rather than continuously during the drag. Vertical drags on the handle change panel height; horizontal swipes inside the itinerary switch dates. From the top of a full-screen Agenda, a deliberate downward pull also returns the panel to split height.

Opening an event or note and returning preserves the itinerary's current scroll position.

Event ordering controls marker numbers and which adjacent events receive transportation controls. Timeline times determine vertical placement; overlaps are allowed.

## iPad

At regular window widths, TPNote uses a collapsible trip/date sidebar, a persistent itinerary column, a map canvas, and a trailing event or note editor. This is the primary iPad landscape workspace. iPad portrait keeps the itinerary and map side by side while the sidebar can collapse.

Long trip names use the compact navigation title in this workspace and truncate within the available bar instead of covering the map controls. The full name remains visible in the trip sidebar and plan menu.

Each date remembers its own Agenda and Timeline scroll position while the planner remains open. Dates that have not been viewed begin at the top; switching dates restores the saved position without eagerly rendering another date's rows.

Opening an event or note collapses the trip sidebar so the itinerary, map, and fixed editor columns have enough space. Closing the editor restores the previous user-selected sidebar state; if you collapsed it manually, it stays collapsed. Use iPadOS's single native sidebar icon in the leading toolbar to show it again. TPNote recenters the selected place after the columns change the available map width.

With the itinerary, map, and editor visible together in a wide iPad window, the editor occupies a fixed right-hand column and the map shrinks to the real middle column. The editor content scrolls, but the panel itself does not drag. TPNote centers the selected place in that middle map column after the columns finish resizing.

Wide iPad column changes use stable layout updates rather than continuously resizing Apple Maps through each animation frame. Opening or closing an editor should therefore remain responsive on older iPads without changing the resulting three-column workspace.

If collaboration reports that CloudKit did not return a trip record for a zone, compare the zone UUID in the message with the current trip's exported `plan.id`. A different UUID identifies an incomplete legacy zone, not damage to the exported trip. Current TPNote builds isolate such zones so they cannot block synchronization or collaboration for valid trips; the server zone is left untouched.

When an iPad Stage Manager window becomes narrow, TPNote automatically uses the compact phone layout and its draggable panels. iPad supports portrait and landscape; iPhone is portrait-only.

## Native Mac

The native Mac app uses a desktop workspace rather than running the iPad interface. Select a trip, date, or **Unscheduled** in the sidebar. The itinerary and Apple Maps canvas resize independently, and selecting an event or note opens a persistent trailing inspector. Its header stays visible while the form scrolls; the event **...** menu can move or delete the event, and Close stays accessible. In a narrow window, the inspector uses macOS's native inspector presentation; the Mac app does not use the iPhone draggable panel.

Use the toolbar to synchronize, review AI changes, collaborate, import, or export. The **Trip** menu includes **Review AI Changes** and **Sync Now**. Shortcuts are **Command-N** for a new window, **Option-Command-N** for a new event, **Shift-Command-N** for a new trip, **Shift-Command-O** to import, **Shift-Command-E** to export, **Shift-Command-R** to review AI changes, and **Option-Command-S** to synchronize. Right-click an event for duplicate, move to Unscheduled, and delete actions.

Private trips and collaborations use the same iCloud container and CloudKit data as iPhone and iPad, so no export or re-import is needed when every device uses the same CloudKit environment. An Xcode Debug run of the Mac app uses CloudKit Development, while TestFlight and distributed builds use Production. Those environments have separate trip records. Mac Settings shows the active environment; use a signed Production/TestFlight Mac build when verifying current iPhone and iPad trips. The native Mac target uses Apple Maps search; Google Places' iOS SDK is not part of the Mac app. A signed Mac build requires the Mac App ID, shared iCloud container, shared app group, and Push Notifications capability.

## Find and preview places on the map

Choose **Find a Place** from the add menu. The search UI is shown during that explicit add flow, after tapping an Apple Maps business or landmark on the main map, or while replacing an event location, rather than occupying the main map at all times. The itinerary minimizes while place discovery is active, leaving the map available for browsing. Enter a business, landmark, or address and choose from the nearby Apple Maps results. Selecting a result centers the map and shows a preview without creating an event yet. The selected-place card keeps clearance above the home indicator.

Use **Place Details** for Apple's native place card, including the address and Apple Maps actions. Use **Add Activity** to add the selected place to the current date, or **Save for Later** when no date is selected. You can also pan or zoom the main map and tap an Apple Maps business or landmark directly to start the same preview and draft-add workflow. Map taps are ignored while an editor or location picker is open so an unfinished draft remains intact.

In an existing event, **Search Maps** opens the shared search with the keyboard ready. **Pick on Map** opens map browsing without the keyboard. **Use This Place** updates only the editor draft; press the editor checkmark to commit the replacement, or use X to discard it.

Activity and note editor drafts remain detached from the saved itinerary until the checkmark is pressed. Opening an editor therefore does not add another map marker or list row; X discards the detached draft without changing the trip. The editor captures the itinerary day's destination time zone before detaching, so its date and time controls match the selected date even when the device is elsewhere.

## Unscheduled planning

Under **Plan Later**, choose **New Unscheduled Activity**, **Save Place for Later**, or **View Unscheduled**. These events belong to the trip but have no date. Its compact header and grabber match the dated itinerary; drag from preview through split to full screen, and use an event's **...** menu to assign it to a date later. The event detail **...** menu can also move an event to a date or Unscheduled, or delete it after confirmation; pending edits are saved before a move.

## Transportation

Between consecutive located events, tap **Add transportation** and choose Public Transit, Walking, Driving, Cycling, or Flight. TPNote draws the available route or curved estimate with theme-based sibling colors.

Public-transit cards show an Apple Maps ETA for the scheduled departure when available, including the date for a non-today leg. They do not substitute a "now" route when that request fails, show a precise ETA more than seven days before departure, or estimate a leg whose destination begins before the source event ends. Adjust conflicting times first. **Open in Apple Maps** provides current route alternatives, lines, stops, platforms, and turn-by-turn details. Route data is not stored in `.tpnote` exports.

## Booking details and reminders

Open an event and choose **Add booking details**. The collapsible section stores booking title, provider, confirmation number, cost or payment note, traveler/contact, phone, email, website, optional booking dates, booking notes, and provider-issued QR or ticket attachments. The website is saved as a tappable booking link. Choose **Add Attachment**, then select **Photo Library** for a QR screenshot or ticket image or **Files** for one or more image or PDF tickets, then confirm with the event checkmark. Images open fitted inside a full-screen preview with pinch, drag, and double-tap zoom; PDFs open in a native full-screen document reader. Saved files synchronize privately through the trip's CloudKit zone, and collaborators download the original only when opening the booking. A QR created from a URL is only a shortcut for opening the website on another device, and a confirmation number must never be turned into a guessed ticket QR.

The **Reminders** section adds an alert at the event start or a selected time before it. Its status explains whether the alert is scheduled, acknowledged, disabled, past, or needs rescheduling. Open **Trip Settings > Reminder Health** to inspect the whole active plan or send a test notification that arrives after about five seconds.

Event notifications provide **I'm On It**, **Remind Me in 10 Minutes**, and **Open Event** actions. Acknowledgement is local to each person. Notifications must be enabled for TPNote in iOS Settings. The iPhone schedules the reminder; a paired Apple Watch receives the system-mirrored alert instead of a second independently scheduled notification.

## Widgets and Apple Watch

The iPhone **Next Trip Event** widget follows the active plan on the Home Screen or Lock Screen. Use **Pinned Trip Event** when a widget should stay on one specific saved plan. Add one pinned widget per trip to a widget stack to swipe between them. Both versions show an in-progress event first, otherwise the next event, and tapping one opens its event in TPNote.

The widget and Watch follow TPNote's iOS per-app language for labels, navigation, actions, dates, times, and countdowns, even when the Watch has a different preferred language. After changing the app language, open TPNote once to publish the updated language and itinerary.

If widget or Watch text appears in two languages after an app update, open TPNote and leave it in the foreground briefly. The app republishes the selected language and active-plan snapshot and refreshes WidgetKit and the Watch companion.

The Apple Watch app supports watchOS 10 or later, including Apple Watch Series 4 on watchOS 10. The iPhone sends every saved trip, with its active trip first. Swipe vertically through each trip's **Next** and **Today** pages. Event detail shows time, location, notes, and booking context, and can open Apple Maps directions, acknowledge the event, or request another reminder in ten minutes. The saved collection remains useful while temporarily offline.

The Watch **Next Trip Event** complication follows the active plan on a watch face or in the Smart Stack. Use **Pinned Trip Event** to choose a specific plan. If Watch or widget information is stale, open TPNote on the iPhone so the complete trip collection is published.

## Collaboration versus file sharing

**Collaborate** creates a live CloudKit share. Current TPNote invitations grant participants editing access to dates, events, places, unscheduled items, notes, booking details, reminders, transportation, and theme. All participants must be signed in to iCloud. TestFlight participants should use a current compatible build. Local confirmations save immediately; nearby routine CloudKit requests are briefly combined into one pass to keep editing responsive, while explicit refresh and share setup remain immediate.

After sharing, use **Manage Collaboration** to see participants, copy the invitation link, or stop sharing.

In build 18 or later, event cards show Like and Poop reactions. Each Apple Account can hold one reaction on each event. Tap a reaction to add it, tap the selected reaction again to remove it, or tap the other reaction to switch. Event cards retain the photo-focused two-lane layout, with the overflow menu right-aligned above the Poop reaction. Notes and reminders do not show reactions; they use a shorter card with a compact themed icon, left-shifted text, and one overflow action. Narrow phone widths keep the time visible and use the icon to communicate the type; Mac follows the same event-only reaction rule and compact note hierarchy in a native list row. Event controls and counts follow the trip theme, synchronize across the owner's devices, and become visible to current and newly invited collaborators after sharing on iPhone, iPad, and Mac. Controls remain visible but can be briefly disabled while the Apple Account or cloud copy becomes available. Reactions are live CloudKit data and are not included in `.tpnote` exports.

CloudKit is the synchronization source of truth. A private trip automatically follows the same Apple Account across iPhone, iPad, and Mac; it does not need a collaboration invitation. At cold launch, foreground return, or a CloudKit notification, TPNote discovers the account's private trip zones and downloads cloud changes before uploading queued local edits. It also checks incrementally while open and periodically performs an authoritative reconciliation. A trip shared with another person uses the shared CloudKit database but follows the same download-before-upload rule. Genuine offline edits remain queued for upload. If two devices edit the same field while both are offline, the newest revision wins when synchronization resumes and TPNote retains conflict information internally.

When a foreground check finds no changed records, change token, pending upload, or collaboration-state update, TPNote leaves local synchronization metadata untouched. This prevents a no-op cloud check from refreshing the visible planner while preserving normal download-before-upload behavior whenever anything actually changed.

Current builds also retry legacy trip-deletion tombstones during one-time startup maintenance. If an older or interrupted build hid a trip locally before its deletion reached CloudKit, launch the current build on that original device while online, then synchronize the other devices.

For a trip the owner has already shared, another device signed into the owner's Apple Account automatically reconnects its local trip metadata to the existing CloudKit share. **Manage Collaboration** shows the same participants without creating a second share or a separate trip copy.

**Export Plan** and **Send Plan File** produce a portable `.tpnote` snapshot. Importing that file creates a separate private plan and does not join or update the live collaboration. Schema 6 snapshots omit booking attachment files, so retain or share images and PDFs through the live CloudKit trip.

## Import, export, and language

- **Export Plan** saves a portable `.tpnote` snapshot.
- **Import Plan** validates the file and creates a new private copy with remapped internal identifiers.
- Collaboration identity, cached photos, generated weather, and live routes are not portable.
- TPNote supports English and Simplified Chinese. The app and all companion surfaces follow the iPhone language, including a per-app selection in **Settings > Apps > TPNote > Language**. Open TPNote once after changing language to refresh widgets and Watch.

After import, current builds resolve verified imported places that have a name, address, and coordinates but no Google Place ID. This runs in the background only for the imported trip, does not block opening it, and requests one coalesced synchronization after successful matches. Thumbnail imagery can appear shortly afterward when Google Places is configured and network/provider coverage permits it.

Schema 6 exports do not contain booking attachment binaries. Images and PDFs remain with the live CloudKit trip, so a plugin should return supplied ticket files as companions for the user to attach after importing a newly generated trip.

## Review AI changes

The TPNote assistant supports two planning paths:

- **Start a New Trip** returns a complete `.tpnote` file. Importing it creates a new private trip.
- **Update an Existing TPNote Trip** starts from the latest `.tpnote` export and normally returns a `.tpnotechanges` file. Applying that file through **Review AI Changes** updates the same live trip and keeps its collaboration workflow.

If the user has not said which path they want, the assistant should present these two choices before generating a file. Importing a revised `.tpnote` creates a separate copy, so it must not be presented as the normal way to update an existing collaborated trip.

Export the current trip and give that file to an AI assistant so the stable IDs remain exact. Ask for a TPNote AI change file. The assistant returns a `.tpnotechanges` file instead of requiring you to copy JSON. Open the plan menu, choose **Review AI Changes**, choose **Choose Change File**, and select it. On Mac, you can also drag the file onto the review window. Select or deselect each proposal, then choose **Apply Selected**. **Paste JSON Instead** remains available as a fallback.

Version 2 change sets can build complete multi-day itineraries and create, update, move, reorder, link, or delete dates, events, notes, places, bookings, reminders, and transportation. TPNote assigns permanent IDs to newly proposed records, validates the accepted set as a unit, and groups proposals by type. Additions and ordinary edits start selected; deletions start unselected and show what linked data would also be removed.

Applied changes enter the same collaboration sync queue as manual edits. TPNote reconciles local reminder notifications and live route details recalculate from the resulting schedule. Use **Undo Applied Changes** to restore the previous state. Version 1 update-and-move sets remain supported. A change set for another trip, an unknown item ID, a dangling temporary reference, an unsupported field, or an invalid time/category is rejected.

## Troubleshooting prompts

For collaboration trouble, determine whether the user is opening a CloudKit invitation or a `.tpnote` file, whether iCloud is signed in, and whether every participant has a current app build. Ask for the exact displayed error before suggesting that the owner remove or recreate a share.

For unavailable routes, confirm that both events have valid locations, are ordered as intended, and have suitable times. Provider coverage can differ by country, mode, and departure time; full transit details remain available through Apple Maps when TPNote can open the route.

For import trouble, inspect and validate the attached file using the format workflow in `SKILL.md` and [tpnote-format.md](tpnote-format.md).
