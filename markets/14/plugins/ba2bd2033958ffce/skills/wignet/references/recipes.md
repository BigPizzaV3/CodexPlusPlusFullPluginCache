# Recipes

Every recipe starts with `get_state` and ends with `get_state` again to
check `health.image_status` / `last_run.error` (see SKILL.md §3).

## "Put 'Back at 6' on the frame for the afternoon"
1. `push_content` `{"text": "# Back at 6\n\nKeys are with the neighbour", "duration_seconds": 14400}`
   (duration is capped at 4 h; without it, the frame goes back at the
   previous service's next due refresh).
2. Tell the owner it shows at the next wake-up (`interval_seconds`).

## "Show this photo" (the user attached a picture)
1. `get_orientation`, `get_capabilities`.
2. Sandbox with no network:
   `python3 scripts/compose.py image photo.jpg --fit cover --width <logical_width> --height <logical_height> [--profile spectra6] --base64 --print-base64`
3. `push_content` `{"image_base64": "<printed string>", "image_sha256": "<printed sha256>", "mode": "dither"}` — the image inherits the frame's orientation.
4. With network instead: add `--upload <frame link>` to step 2 and skip step 3.

## "Make a chart of X and show it"
1. Draw it at the logical size with thick strokes, black on white
   (`references/eink-design.md`), save as PNG.
2. `compose.py image chart.png --mode threshold --base64 --print-base64 --full`
   (`--full`: a chart is sharper as an exact black-and-white PNG than as a
   compact JPEG, and stays small).
3. `push_content` with `image_base64`, `image_sha256`, `"mode": "threshold"`.

## "Show the surf forecast for my spot" / weather / bus
1. Read the `set_service` tool description (or the guide §2) for the
   service slug and its settings; never invent a spot, city or stop id.
2. `set_service` `{"service": "meteo", "params": {"city": "Lyon"}}`
   (surf/wind services take `spot`, Vélib `station_id`).
3. If `get_state` shows `schedule_rules`, the rule for the current hour wins
   over `set_service`: tell the owner, or edit the rules (guide §4).

## "Weather in the morning, bus times at 8, message board otherwise"
Schedule rules have no connector tool. Over HTTP: guide §4 ("Modifier
finement") — `PUT https://app.ecranpapier.com/api/owner/<id>` **replaces** name,
service, params and rules as a whole, so `GET` first, change only the rules
(each rule's `service_slug` becomes the matching numeric `service_id`),
send everything back, verify. `days`: `*`, `lun-ven`, `sam,dim`…
With the connector alone, say so and send the owner to their frame's page
(`https://app.ecranpapier.com/w/<id>`) to set the hours there.

## "We're away for two weeks"
`sleep` with `seconds` (default 12 h). The panel keeps its image with no
power. `wake` when they are back. A sleep in progress can't be cut short.

## "Keep this image on the frame for good" / "a new picture every day"
The push store keeps one image for 24 h at most. Host the image (a public
bucket, a static page, a small function that regenerates it), then
`set_service` `{"service": "custom", "params": {"url": "https://…"}}`.
The platform re-downloads it at every refresh. The URL must return an
image; ideally already at the frame's size.

## "How much is a frame? Is there any left?"
Shop connector `list_products` (or `https://ecranpapier.com/api/shop/products`): quote the
price (VAT and shipping included) and `remaining` as they are, point to
https://ecranpapier.com/boutique.html to order. Anything else → contact@ecranpapier.com.
