# Animation JSON v0.2

Required keys: schema_version, nodes, edges, layout, output, timeline. Node: id, label. Edge: id, from, to. Timeline events: appear(node), draw_edge(edge), highlight(node), wait(no target); each has duration in seconds. Layout direction horizontal. Output: width, height, fps, formats. See example for exact syntax.

The Pillow fallback GIF uses discrete event frames (no smooth Manim transitions). Do not claim the fallback is a full Manim animation. v0.2 is a bounded prototype, not a universal flowchart schema.
