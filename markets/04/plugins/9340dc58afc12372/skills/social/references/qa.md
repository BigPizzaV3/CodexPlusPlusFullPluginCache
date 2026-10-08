# QA before delivery

## Blocking
| Check | Fails when |
|---|---|
| Rendered text | Baked-in letterforms in a generated image |
| Carousel shortfall | Fewer slides than requested and not disclosed — billing is per requested slide, up front, not refunded |
| Thumbnail claims | A vertical cover was promised; the tool is 16:9 only |
| Caption source | The video isn't hosted by this server — it cannot be captioned |
| Caption preset | Not passed verbatim; the upstream match is exact |

## Quality
| Check | Fails when |
|---|---|
| Thumbnail legibility | Unreadable at 120px wide |
| Deck coherence | Carousel slides don't share a visual system |
| Safe area | Content sits where the platform crops or overlays UI |
| Caption cost | An animated preset was used without flagging the doubled cost |
