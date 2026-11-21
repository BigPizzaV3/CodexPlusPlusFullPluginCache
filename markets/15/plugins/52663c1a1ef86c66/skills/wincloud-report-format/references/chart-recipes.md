# Chart recipes

## Run the script

```bash
python3 <skill folder>/scripts/chart.py spec.json chart.svg
```

Specs (all share `title`, `subtitle`, `unit`). The names and numbers below are placeholders; use the tool results:

```json
{"type":"bar","title":"Bookings by month, Q1 2026","subtitle":"By booking date","unit":"bookings",
 "categories":["Jan","Feb","Mar"],
 "series":[{"name":"Hotel A","values":[88,81,82]},{"name":"Hotel B","values":[50,52,49]}]}
```

- `bar`: columns, grouped when there are several series. Months, statuses, locations side by side.
- `hbar`: same spec, horizontal. Use for long category names; sort the categories high to low first.
- `line`: same spec; add `"dashed": true` to the estimate series.
- `donut`: one series; the categories are the parts. 5 parts or fewer.

The script prints the file it wrote. Show that SVG (or the PNG beside it, when one was written). If the environment can't display an SVG file, put the SVG source inside an HTML file and show that.

## Hand-written SVG (when you can't run the script)

Keep the same look: white background, navy `#003352` and green `#63e7a4`, a bold title at the top left, a baseline at zero, a value above each bar, a legend under the chart.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" font-family="Century Gothic, Arial, sans-serif">
  <rect width="760" height="420" fill="#fff"/>
  <text x="24" y="30" font-size="17" font-weight="bold" fill="#003352">Bookings by month, Q1 2026</text>
  <line x1="60" y1="350" x2="736" y2="350" stroke="#e3e8ec"/>
  <rect x="120" y="150" width="48" height="200" fill="#003352"/><text x="144" y="144" font-size="11" text-anchor="middle">88</text>
  <rect x="170" y="239" width="48" height="111" fill="#63e7a4"/><text x="194" y="233" font-size="11" text-anchor="middle">50</text>
  <text x="169" y="368" font-size="12" text-anchor="middle">Jan</text>
</svg>
```

Bar height is the value divided by the axis maximum, times the plot height. Take the axis maximum from the data rounded up to a round number.
