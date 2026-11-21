# Model parameters

Release 2026-11-13-model-selection; environment prod; contract_digest `ce9707478ab99797082dad58d61d8f51663fabd1dd294bcf02fed82fbaa51336`; selection_digest `d61b99537c159daa11ffa009f5f818d2866b50fe78b388648f15c7bb170fcc5e`.

Generated from the same reviewed workflow/UI evidence as the connected tools. Read the selected request.model section. The connected tool schema is authoritative; these labels do not add inputs or options.

Extract explicit user settings into request.options before submission. Defaults apply only to unspecified settings. UI label context helps select a value; send a context field only when the tool declares it. Nominal aspect-ratio presets may use rounded pixel sizes. Resolve unsupported or conflicting requirements before creating a task.

## image2image_banana

Tool: `image_to_image`. Model: Nano Banana. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `""` | `["","9:16","16:9","1:1","4:3","3:4","3:2","2:3","21:9"]` | Auto → "" |
| `is_idle` | `false` | `[true,false]` | True → true; False → false |

## image2image_banana_2

Tool: `image_to_image`. Model: Nano Banana Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `n` | `1` | `[1]` |  |
| `quality` | `"medium"` | `["medium"]` |  |
| `size` | `"1024x1024"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `output_format` | `"png"` | `["png"]` |  |

## image2image_gpt_image_2

Tool: `image_to_image`. Model: GPT Image 2. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `n` | `1` | `[1]` |  |
| `quality` | `"low"` | `["low","medium"]` | Low → "low"; High → "medium" |
| `size` | `"1024x1024"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `output_format` | `"png"` | `["png"]` |  |

## image2image_gpt_image_2.5

Tool: `image_to_image`. Model: GPT Image 2.5 Flare. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `size` | `"608x1088"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `quality` | `"low"` | `["low","medium","high","xhigh","max"]` | Low → "low"; Medium → "medium"; High → "high"; X-High → "xhigh"; Max → "max" |
| `output_format` | `"png"` | `["png"]` |  |
| `n` | `1` | `[1]` |  |

## image2image_gpt_image_2.5_sunburst

Tool: `image_to_image`. Model: GPT Image 2.5 Sunburst. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `size` | `"608x1088"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `quality` | `"low"` | `["low","medium","high","xhigh","max"]` | Low → "low"; Medium → "medium"; High → "high"; X-High → "xhigh"; Max → "max" |
| `output_format` | `"png"` | `["png"]` |  |
| `n` | `1` | `[1]` |  |

## image2image_media_1.0

Tool: `image_to_image`. Model: ToMoviee Image Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `dimensions` | `"1024x1024"` | `["1024x1024","848x1264","1264x848","768x1376","1376x768"]` | UI meaning: ratio; 1:1 → "1024x1024"; 2:3 → "848x1264"; 3:2 → "1264x848"; 9:16 → "768x1376"; 16:9 → "1376x768" |
| `strength_model` | `0` | `[0]` |  |

## image2image_media_2.0

Tool: `image_to_image`. Model: Tomoviee Image Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `dimensions` | `"1024x1024"` | `["1024x1024","848x1264","1264x848","768x1376","1376x768"]` | UI meaning: ratio; 1:1 → "1024x1024"; 2:3 → "848x1264"; 3:2 → "1264x848"; 9:16 → "768x1376"; 16:9 → "1376x768" |
| `strength_model` | `0` | `[0]` |  |
| `resolution` | `"1K"` | `["1K"]` |  |

## image2image_media_3.0

Tool: `image_to_image`. Model: ToMoviee Image 3.0 Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `dimensions` | `"1024x1024"` | `["1024x1024","848x1264","1264x848","768x1376","1376x768"]` | UI meaning: ratio; 1:1 → "1024x1024"; 2:3 → "848x1264"; 3:2 → "1264x848"; 9:16 → "768x1376"; 16:9 → "1376x768" |

## image2image_nano_banana_2

Tool: `image_to_image`. Model: Nano Banana 2. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","3:2","2:3","21:9"]` |  |
| `resolution` | `"1K"` | `["1K","2K","4K"]` |  |

## image2image_nano_banana_2_1

Tool: `image_to_image`. Model: Nano Banana 2.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["1:1","9:16","16:9","4:3","3:4","3:2","2:3","21:9","1:4","4:1","4:5","5:4","1:8","8:1"]` |  |
| `resolution` | `"1K"` | `["1K","2K","4K"]` |  |

## image2image_nano_banana_2_lite

Tool: `image_to_image`. Model: Nano Banana 2 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","3:2","2:3","21:9"]` |  |
| `resolution` | `"1K"` | `["1K"]` |  |

## image2image_seedream_4.0

Tool: `image_to_image`. Model: Seedream 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"1440x2560"` | `["1440x2560","2560x1440","2560x2560","1920x1440","1440x1920","2160x1440","1440x2160"]` | 9:16 → "1440x2560"; 16:9 → "2560x1440"; 1:1 → "2560x2560"; 4:3 → "1920x1440"; 3:4 → "1440x1920"; 3:2 → "2160x1440"; 2:3 → "1440x2160" |
| `seed` | `0` | `[0]` |  |

## image2image_seedream_5.0_lite

Tool: `image_to_image`. Model: Seedream 5.0 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"2K"` | `["2K","3K","1600x2848","2304x4096","2848x1600","4096x2304","2048x2048","3072x3072","2304x1728","3456x2592","1728x2304","2592x3456","2496x1664","2496x3744","1664x2496","3136x1344","4704x2016"]` | Auto (resolution="2K") → "2K"; Auto (resolution="3K") → "3K"; 9:16 (resolution="2K") → "1600x2848"; 9:16 (resolution="3K") → "2304x4096"; 16:9 (resolution="2K") → "2848x1600"; 16:9 (resolution="3K") → "4096x2304"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="3K") → "3072x3072"; 4:3 (resolution="2K") → "2304x1728"; 4:3 (resolution="3K") → "3456x2592"; 3:4 (resolution="2K") → "1728x2304"; 3:4 (resolution="3K") → "2592x3456"; 3:2 (resolution="2K") → "2496x1664"; 3:2 (resolution="3K") → "2496x3744"; 2:3 (resolution="2K") → "1664x2496"; 2:3 (resolution="3K") → "2496x3744"; 21:9 (resolution="2K") → "3136x1344"; 21:9 (resolution="3K") → "4704x2016"; Unspecified label context defaults: {"resolution":"2K"} |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `-1` | `[-1]` |  |
| `output_format` | `"png"` | `["png"]` |  |

## image2image_seedream_5.0_pro

Tool: `image_to_image`. Model: Seedream 5.0 Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"1K"` | `["1K","2K","1520x2688","752x1344","2688x1520","1344x752","2048x2048","1024x1024","2304x1728","1152x864","1728x2304","864x1152","2448x1632","1200x800","1632x2448","800x1200","3072x1312","1504x640"]` | Auto (resolution="1K") → "1K"; Auto (resolution="2K") → "2K"; 9:16 (resolution="2K") → "1520x2688"; 9:16 (resolution="1K") → "752x1344"; 16:9 (resolution="2K") → "2688x1520"; 16:9 (resolution="1K") → "1344x752"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="1K") → "1024x1024"; 4:3 (resolution="2K") → "2304x1728"; 4:3 (resolution="1K") → "1152x864"; 3:4 (resolution="2K") → "1728x2304"; 3:4 (resolution="1K") → "864x1152"; 3:2 (resolution="2K") → "2448x1632"; 3:2 (resolution="1K") → "1200x800"; 2:3 (resolution="2K") → "1632x2448"; 2:3 (resolution="3K") → "800x1200"; 21:9 (resolution="2K") → "3072x1312"; 21:9 (resolution="1K") → "1504x640"; Unspecified label context defaults: {"resolution":"2K"} |
| `width` | `"1024"` | `["1024"]` |  |
| `height` | `"1024"` | `["1024"]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `-1` | `[-1]` |  |
| `output_format` | `"png"` | `["png"]` |  |

## image2image_tomoviee_4.0

Tool: `image_to_image`. Model: ToMoviee Image 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"9:16"` | `["1:1","9:16","16:9","4:3","3:4"]` |  |
| `resolution` | `"480p"` | `["480p","720p","1080p","2k","4k"]` | 480P → "480p"; 720P → "720p"; 1K → "1080p"; 2K → "2k"; 4K → "4k" |

## image2image_wan_2.7

Tool: `image_to_image`. Model: Wan 2.7. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `enable_sequential` | `false` | `[true,false]` |  |
| `size` | `"1K"` | `["1K","2K","800*1424","1536*2720","1424*800","2720*1536","1024*1024","2048*2048","1152*864","2304*1728","864*1152","1728*2304","1248*832","2496*1664","832*1248","1664*2496"]` | Auto (resolution="1K") → "1K"; Auto (resolution="2K") → "2K"; 9:16 (resolution="1K") → "800*1424"; 9:16 (resolution="2K") → "1536*2720"; 16:9 (resolution="1K") → "1424*800"; 16:9 (resolution="2K") → "2720*1536"; 1:1 (resolution="1K") → "1024*1024"; 1:1 (resolution="2K") → "2048*2048"; 4:3 (resolution="1K") → "1152*864"; 4:3 (resolution="2K") → "2304*1728"; 3:4 (resolution="1K") → "864*1152"; 3:4 (resolution="2K") → "1728*2304"; 3:2 (resolution="1K") → "1248*832"; 3:2 (resolution="2K") → "2496*1664"; 2:3 (resolution="1K") → "832*1248"; 2:3 (resolution="2K") → "1664*2496"; Unspecified label context defaults: {"resolution":"1K"} |
| `n` | `1` | `[1]` |  |
| `thinking_mode` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `0` | `[0]` |  |

## image2image_wan_2.7_pro

Tool: `image_to_image`. Model: Wan 2.7 Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `enable_sequential` | `false` | `[true,false]` |  |
| `size` | `"1K"` | `["1K","2K","800*1424","1536*2720","1424*800","2720*1536","1024*1024","2048*2048","1152*864","2304*1728","864*1152","1728*2304","1248*832","2496*1664","832*1248","1664*2496"]` | Auto (resolution="1K") → "1K"; Auto (resolution="2K") → "2K"; 9:16 (resolution="1K") → "800*1424"; 9:16 (resolution="2K") → "1536*2720"; 16:9 (resolution="1K") → "1424*800"; 16:9 (resolution="2K") → "2720*1536"; 1:1 (resolution="1K") → "1024*1024"; 1:1 (resolution="2K") → "2048*2048"; 4:3 (resolution="1K") → "1152*864"; 4:3 (resolution="2K") → "2304*1728"; 3:4 (resolution="1K") → "864*1152"; 3:4 (resolution="2K") → "1728*2304"; 3:2 (resolution="1K") → "1248*832"; 3:2 (resolution="2K") → "2496*1664"; 2:3 (resolution="1K") → "832*1248"; 2:3 (resolution="2K") → "1664*2496"; Unspecified label context defaults: {"resolution":"1K"} |
| `n` | `1` | `[1]` |  |
| `thinking_mode` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `0` | `[0]` |  |

## text2image_banana

Tool: `text_to_image`. Model: Nano Banana. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","3:2","2:3","21:9"]` |  |
| `is_idle` | `false` | `[true,false]` | True → true; False → false |

## text2image_banana_2

Tool: `text_to_image`. Model: Nano Banana Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `n` | `1` | `[1]` |  |
| `quality` | `"medium"` | `["medium"]` |  |
| `size` | `"1024x1024"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `output_format` | `"png"` | `["png"]` |  |

## text2image_gpt_image_2

Tool: `text_to_image`. Model: GPT Image 2. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `n` | `1` | `[1]` |  |
| `quality` | `"low"` | `["low","medium"]` | Low → "low"; High → "medium" |
| `size` | `"1024x1024"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `output_format` | `"png"` | `["png"]` |  |

## text2image_gpt_image_2.5

Tool: `text_to_image`. Model: GPT Image 2.5 Flare. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `size` | `"608x1088"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `quality` | `"low"` | `["low","medium","high","xhigh","max"]` | Low → "low"; Medium → "medium"; High → "high"; X-High → "xhigh"; Max → "max" |
| `output_format` | `"png"` | `["png"]` |  |
| `n` | `1` | `[1]` |  |

## text2image_gpt_image_2.5_sunburst

Tool: `text_to_image`. Model: GPT Image 2.5 Sunburst. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `size` | `"608x1088"` | `["608x1088","1440x2560","2160x3840","1088x608","2560x1440","3840x2160","1024x1024","2048x2048","2880x2880","1024x768","2560x1920","3328x2480","768x1024","1920x2560","2480x3328","1024x688","2560x1712","3520x2336","688x1024","1712x2560","2336x3520","1248x528","2560x1088","3840x1648"]` | UI meaning: aspect_ratio; 9:16 (resolution="1K") → "608x1088"; 9:16 (resolution="2K") → "1440x2560"; 9:16 (resolution="4K") → "2160x3840"; 16:9 (resolution="1K") → "1088x608"; 16:9 (resolution="2K") → "2560x1440"; 16:9 (resolution="4K") → "3840x2160"; 1:1 (resolution="1K") → "1024x1024"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="4K") → "2880x2880"; 4:3 (resolution="1K") → "1024x768"; 4:3 (resolution="2K") → "2560x1920"; 4:3 (resolution="4K") → "3328x2480"; 3:4 (resolution="1K") → "768x1024"; 3:4 (resolution="2K") → "1920x2560"; 3:4 (resolution="4K") → "2480x3328"; 3:2 (resolution="1K") → "1024x688"; 3:2 (resolution="2K") → "2560x1712"; 3:2 (resolution="4K") → "3520x2336"; 2:3 (resolution="1K") → "688x1024"; 2:3 (resolution="2K") → "1712x2560"; 2:3 (resolution="4K") → "2336x3520"; 21:9 (resolution="1K") → "1248x528"; 21:9 (resolution="2K") → "2560x1088"; 21:9 (resolution="4K") → "3840x1648"; Unspecified label context defaults: {"resolution":"1K"} |
| `quality` | `"low"` | `["low","medium","high","xhigh","max"]` | Low → "low"; Medium → "medium"; High → "high"; X-High → "xhigh"; Max → "max" |
| `output_format` | `"png"` | `["png"]` |  |
| `n` | `1` | `[1]` |  |

## text2image_nano_banana_2

Tool: `text_to_image`. Model: Nano Banana 2. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","3:2","2:3","21:9"]` |  |
| `resolution` | `"1K"` | `["1K","2K","4K"]` |  |

## text2image_nano_banana_2_1

Tool: `text_to_image`. Model: Nano Banana 2.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["1:1","9:16","16:9","4:3","3:4","3:2","2:3","21:9","1:4","4:1","4:5","5:4","1:8","8:1"]` |  |
| `resolution` | `"1K"` | `["1K","2K","4K"]` |  |

## text2image_nano_banana_2_lite

Tool: `text_to_image`. Model: Nano Banana 2 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","3:2","2:3","21:9"]` |  |
| `resolution` | `"1K"` | `["1K"]` |  |

## text2image_seedream_4.0

Tool: `text_to_image`. Model: Seedream 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"2560x1440"` | `["2560x1440","1440x2560","2560x2560","1920x1440","1440x1920","2160x1440","1440x2160"]` | 16:9 → "2560x1440"; 9:16 → "1440x2560"; 1:1 → "2560x2560"; 4:3 → "1920x1440"; 3:4 → "1440x1920"; 3:2 → "2160x1440"; 2:3 → "1440x2160" |
| `seed` | `0` | `[0]` |  |

## text2image_seedream_5.0_lite

Tool: `text_to_image`. Model: Seedream 5.0 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"1600x2848"` | `["2K","3K","1600x2848","2304x4096","2848x1600","4096x2304","2048x2048","3072x3072","2304x1728","3456x2592","1728x2304","2592x3456","2496x1664","2496x3744","1664x2496","3136x1344","4704x2016"]` | Auto (resolution="2K") → "2K"; Auto (resolution="3K") → "3K"; 9:16 (resolution="2K") → "1600x2848"; 9:16 (resolution="3K") → "2304x4096"; 16:9 (resolution="2K") → "2848x1600"; 16:9 (resolution="3K") → "4096x2304"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="3K") → "3072x3072"; 4:3 (resolution="2K") → "2304x1728"; 4:3 (resolution="3K") → "3456x2592"; 3:4 (resolution="2K") → "1728x2304"; 3:4 (resolution="3K") → "2592x3456"; 3:2 (resolution="2K") → "2496x1664"; 3:2 (resolution="3K") → "2496x3744"; 2:3 (resolution="2K") → "1664x2496"; 2:3 (resolution="3K") → "2496x3744"; 21:9 (resolution="2K") → "3136x1344"; 21:9 (resolution="3K") → "4704x2016"; Unspecified label context defaults: {"resolution":"2K"} |
| `width` | `"1024"` | `["1024"]` |  |
| `height` | `"1024"` | `["1024"]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `-1` | `[-1]` |  |
| `output_format` | `"png"` | `["png"]` |  |

## text2image_seedream_5.0_pro

Tool: `text_to_image`. Model: Seedream 5.0 Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"1K"` | `["1K","2K","1520x2688","752x1344","2688x1520","1344x752","2048x2048","1024x1024","2304x1728","1152x864","1728x2304","864x1152","2448x1632","1200x800","1632x2448","800x1200","3072x1312","1504x640"]` | Auto (resolution="1K") → "1K"; Auto (resolution="2K") → "2K"; 9:16 (resolution="2K") → "1520x2688"; 9:16 (resolution="1K") → "752x1344"; 16:9 (resolution="2K") → "2688x1520"; 16:9 (resolution="1K") → "1344x752"; 1:1 (resolution="2K") → "2048x2048"; 1:1 (resolution="1K") → "1024x1024"; 4:3 (resolution="2K") → "2304x1728"; 4:3 (resolution="1K") → "1152x864"; 3:4 (resolution="2K") → "1728x2304"; 3:4 (resolution="1K") → "864x1152"; 3:2 (resolution="2K") → "2448x1632"; 3:2 (resolution="1K") → "1200x800"; 2:3 (resolution="2K") → "1632x2448"; 2:3 (resolution="3K") → "800x1200"; 21:9 (resolution="2K") → "3072x1312"; 21:9 (resolution="1K") → "1504x640"; Unspecified label context defaults: {"resolution":"2K"} |
| `width` | `"1024"` | `["1024"]` |  |
| `height` | `"1024"` | `["1024"]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `-1` | `[-1]` |  |
| `output_format` | `"png"` | `["png"]` |  |

## text2image_soul_character

Tool: `text_to_image`. Model: ToMoviee Image Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `dimensions` | `"848x1264"` | `["848x1264","1024x1024","1264x848","768x1376","1376x768"]` | UI meaning: ratio; 2:3 → "848x1264"; 1:1 → "1024x1024"; 3:2 → "1264x848"; 9:16 → "768x1376"; 16:9 → "1376x768" |
| `strength_model` | `0` | `[0]` |  |

## text2image_tomoviee_2.0

Tool: `text_to_image`. Model: ToMoviee Image 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `dimensions` | `"576x1024"` | `["576x1024","1024x576","1024x1024","1024x768","768x1024"]` | UI meaning: ratio; 9:16 → "576x1024"; 16:9 → "1024x576"; 1:1 → "1024x1024"; 4:3 → "1024x768"; 3:4 → "768x1024" |
| `batch_size` | `4` | `[1,2,3,4]` |  |

## text2image_tomoviee_4.0

Tool: `text_to_image`. Model: ToMoviee Image 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"9:16"` | `["1:1","9:16","16:9","4:3","3:4"]` |  |
| `resolution` | `"480p"` | `["480p","720p","1080p","2k","4k"]` | 480P → "480p"; 720P → "720p"; 1K → "1080p"; 2K → "2k"; 4K → "4k" |

## text2image_wan_2.7

Tool: `text_to_image`. Model: Wan 2.7. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `enable_sequential` | `true` | `[true,false]` |  |
| `size` | `"800*1424"` | `["800*1424","1536*2720","1424*800","2720*1536","1024*1024","2048*2048","1152*864","2304*1728","864*1152","1728*2304","1248*832","2496*1664","832*1248","1664*2496"]` | 9:16 (resolution="1K") → "800*1424"; 9:16 (resolution="2K") → "1536*2720"; 16:9 (resolution="1K") → "1424*800"; 16:9 (resolution="2K") → "2720*1536"; 1:1 (resolution="1K") → "1024*1024"; 1:1 (resolution="2K") → "2048*2048"; 4:3 (resolution="1K") → "1152*864"; 4:3 (resolution="2K") → "2304*1728"; 3:4 (resolution="1K") → "864*1152"; 3:4 (resolution="2K") → "1728*2304"; 3:2 (resolution="1K") → "1248*832"; 3:2 (resolution="2K") → "2496*1664"; 2:3 (resolution="1K") → "832*1248"; 2:3 (resolution="2K") → "1664*2496"; Unspecified label context defaults: {"resolution":"1K"} |
| `n` | `1` | `[1]` |  |
| `thinking_mode` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `0` | `[0]` |  |

## text2image_wan_2.7_pro

Tool: `text_to_image`. Model: Wan 2.7 Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `enable_sequential` | `false` | `[true,false]` |  |
| `size` | `"800*1424"` | `["800*1424","1536*2720","1424*800","2720*1536","1024*1024","2048*2048","1152*864","2304*1728","864*1152","1728*2304","1248*832","2496*1664","832*1248","1664*2496"]` | 9:16 (resolution="1K") → "800*1424"; 9:16 (resolution="2K") → "1536*2720"; 16:9 (resolution="1K") → "1424*800"; 16:9 (resolution="2K") → "2720*1536"; 1:1 (resolution="1K") → "1024*1024"; 1:1 (resolution="2K") → "2048*2048"; 4:3 (resolution="1K") → "1152*864"; 4:3 (resolution="2K") → "2304*1728"; 3:4 (resolution="1K") → "864*1152"; 3:4 (resolution="2K") → "1728*2304"; 3:2 (resolution="1K") → "1248*832"; 3:2 (resolution="2K") → "2496*1664"; 2:3 (resolution="1K") → "832*1248"; 2:3 (resolution="2K") → "1664*2496"; Unspecified label context defaults: {"resolution":"1K"} |
| `n` | `1` | `[1]` |  |
| `thinking_mode` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |
| `seed` | `0` | `[0]` |  |

## image2video_gemini_omni_flash

Tool: `image_to_video`. Model: Gemini Omni Flash. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16"]` |  |
| `duration_s` | `"3s"` | `["3s","5s","8s","10s"]` | UI meaning: duration |

## image2video_gemini_omni_flash_reference_image

Tool: `reference_to_video`. Model: Gemini Omni Flash. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16"]` |  |
| `duration_s` | `"3s"` | `["3s","5s","8s","10s"]` | UI meaning: duration |

## image2video_happyhorse_1.0

Tool: `image_to_video`. Model: HappyHorse 1.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720P"` | `["720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"16:9"` | `["16:9"]` |  |
| `seed` | `0` | `[0]` |  |

## image2video_happyhorse_1.0_reference_image

Tool: `reference_to_video`. Model: HappyHorse 1.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720P"` | `["720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"16:9"` | `["16:9","9:16","1:1","3:4","4:3"]` |  |
| `seed` | `0` | `[0]` |  |

## image2video_happyhorse_1.5

Tool: `image_to_video`. Model: HappyHorse 1.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720P"` | `["720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"16:9"` | `["16:9"]` |  |
| `seed` | `0` | `[0]` |  |

## image2video_happyhorse_1.5_reference_image

Tool: `reference_to_video`. Model: HappyHorse 1.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720P"` | `["720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"16:9"` | `["16:9","9:16","1:1","3:4","4:3","21:9"]` |  |
| `seed` | `0` | `[0]` |  |

## image2video_kling_2.5_turbo

Tool: `image_to_video`. Model: Kling 2.5 Turbo. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `resolution` | `"std"` | `["std","pro"]` | 720P → "std"; 1080P → "pro" |

## image2video_kling_2.5_turbo_head_and_tail

Tool: `image_to_video`. Model: Kling 2.5 Turbo. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `resolution` | `"pro"` | `["pro"]` | 1080P → "pro" |

## image2video_kling_2.6

Tool: `image_to_video`. Model: Kling 2.6. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration_string` | `"5"` | `["5","10"]` | UI meaning: duration; 5s → "5"; 10s → "10" |
| `sound` | `"on"` | `["on","off"]` | UI meaning: generate_audio; On → "on"; Off → "off" |
| `mode` | `"pro"` | `["pro"]` |  |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |

## image2video_kling_3.0

Tool: `image_to_video`. Model: Kling 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `sound` | `"on"` | `["on","off"]` | UI meaning: generate_audio; True → "on"; False → "off" |
| `duration_string` | `"3"` | `["3","5","8","10","15"]` | UI meaning: duration; 5s → "5"; 8s → "8"; 10s → "10"; 15s → "15" |
| `mode` | `"4k"` | `["std","pro","4k"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro"; 4K → "4k" |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `multi_shots` | `false` | `[true,false]` | True → true; False → false |
| `shot_type` | `"intelligence"` | `["intelligence"]` |  |

## image2video_kling_3.0_fast

Tool: `image_to_video`. Model: Kling 3.0 Turbo. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## image2video_kling_3.0_head_and_tail

Tool: `image_to_video`. Model: Kling 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration_string` | `"5"` | `["5","8","10","15"]` | UI meaning: duration; 5s → "5"; 8s → "8"; 10s → "10"; 15s → "15" |
| `sound` | `"on"` | `["on","off"]` | UI meaning: generate_audio; True → "on"; False → "off" |
| `mode` | `"std"` | `["std","pro"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro" |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |

## image2video_kling_3.0_omni_reference_image

Tool: `reference_to_video`. Model: Kling 3.0 Omni. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `sound` | `"on"` | `["on","off"]` | UI meaning: generate_audio; True → "on"; False → "off" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"16:9"` | `["9:16","16:9","1:1"]` |  |
| `mode` | `"4k"` | `["std","pro","4k"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro"; 4K → "4k" |

## image2video_kling_motion_control_2.6

Tool: `motion_control`. Model: Kling Motion Control. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `is_bgm` | `false` | `[true,false]` |  |
| `keep_original_sound` | `"yes"` | `["yes"]` |  |
| `mode` | `"std"` | `["std","pro"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro" |
| `orientation` | `"video"` | `["video"]` |  |

## image2video_kling_o1

Tool: `image_to_video`. Model: Kling O1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `mode` | `"std"` | `["std","pro"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro" |

## image2video_kling_o1_head_and_tail

Tool: `image_to_video`. Model: Kling O1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `resolution` | `"540p"` | `["540p"]` |  |
| `mode` | `"std"` | `["std","pro"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro" |

## image2video_kling_o1_reference_image

Tool: `reference_to_video`. Model: Kling O1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1"]` |  |
| `mode` | `"std"` | `["std","pro"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro" |

## image2video_media_1.0

Tool: `image_to_video`. Model: ToMoviee Video 2.0 Pro. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `seed1` | `0` | `[0]` |  |
| `seed2` | `0` | `[0]` |  |

## image2video_minimax_02

Tool: `image_to_video`. Model: Hailuo 02. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `watermark` | `false` | `[true,false]` |  |
| `duration` | `6` | `[6,10]` | 6s → 6; 10s → 10 |
| `prompt_extend` | `false` | `[true,false]` |  |
| `resolution` | `"768P"` | `["768P","1080P"]` |  |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"duration":[6],"resolution":["768P","1080P"]},{"duration":[10],"resolution":["768P"]}]
```

## image2video_minimax_2.3

Tool: `image_to_video`. Model: Hailuo 2.3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `watermark` | `false` | `[true,false]` |  |
| `duration` | `6` | `[6,10]` | 6s → 6; 10s → 10 |
| `prompt_extend` | `false` | `[true,false]` |  |
| `resolution` | `"768P"` | `["768P","1080P"]` |  |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"duration":[6],"resolution":["768P","1080P"]},{"duration":[10],"resolution":["768P"]}]
```

## image2video_minimax_h3_head_and_tail_switch

Tool: `image_to_video`. Model: MiniMax H3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","2k"]` | 768P → "480p"; 2K → "2k" |
| `duration` | `5` | `[5,15]` | 5s → 5; 15s → 15 |
| `ratio` | `"auto"` | `["auto"]` |  |

## image2video_minimax_h3_max

Tool: `image_to_video`. Model: MiniMax H3 Max. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"768P"` | `["480P","768P"]` |  |
| `duration` | `5` | `[5,15]` | 5s → 5; 15s → 15 |
| `ratio` | `"adaptive"` | `["adaptive"]` |  |

## image2video_minimax_h3_reference_image_switch

Tool: `reference_to_video`. Model: MiniMax H3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","2k"]` | 768P → "480p"; 2K → "2k" |
| `duration` | `5` | `[5,15]` | 5s → 5; 15s → 15 |
| `ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","21:9"]` |  |

## image2video_minimax_h3_switch

Tool: `image_to_video`. Model: MiniMax H3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","2k"]` | 768P → "480p"; 2K → "2k" |
| `duration` | `5` | `[5,15]` | 5s → 5; 15s → 15 |
| `ratio` | `"auto"` | `["auto"]` |  |

## image2video_seedance_2.0_mini

Tool: `image_to_video`. Model: Seedance 2.0 Mini. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## image2video_seedance_2.0_mini_head_and_tail

Tool: `image_to_video`. Model: Seedance 2.0 Mini. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |

## image2video_seedance_2.5

Tool: `image_to_video`. Model: Seedance 2.5. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |

## image2video_seedance_2.5_head_and_tail

Tool: `image_to_video`. Model: Seedance 2.5. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |
| `aspect_ratio` | `"adaptive"` | `["adaptive"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |

## image2video_seedance2.0_fast

Tool: `image_to_video`. Model: Seedance 2.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## image2video_seedance2.0_fast_head_and_tail

Tool: `image_to_video`. Model: Seedance 2.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |

## image2video_seedance2.0_fast_reference_image

Tool: `reference_to_video`. Model: Seedance 2.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |

## image2video_seedance_2.0_mini_reference_image

Tool: `reference_to_video`. Model: Seedance 2.0 Mini. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |

## image2video_seedance_2.5_reference_image

Tool: `reference_to_video`. Model: Seedance 2.5. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |

## image2video_tomoviee4_head_and_tail_switch

Tool: `image_to_video`. Model: ToMoviee Video 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"2K"` | `["2K","768P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `ratio` | `"21:9"` | `["21:9"]` |  |

## image2video_tomoviee4_reference_image_switch

Tool: `reference_to_video`. Model: ToMoviee Video 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"768P"` | `["2K","768P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `ratio` | `"adaptive"` | `["adaptive"]` |  |

## image2video_tomoviee4_switch

Tool: `image_to_video`. Model: ToMoviee Video 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"2K"` | `["2K","768P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `ratio` | `"adaptive"` | `["adaptive"]` |  |

## image2video_tomoviee_2.0

Tool: `image_to_video`. Model: ToMoviee Video 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"original"` | `["original"]` |  |
| `duration` | `5` | `[5]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |

## image2video_tomoviee_2.0_fast

Tool: `image_to_video`. Model: ToMoviee Video 2.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| — | — | No configurable options | — |

## image2video_tomoviee_2.5

Tool: `image_to_video`. Model: Seedance 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"4k"` | `["480p","720p","1080p","4k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 4K → "4k" |

## image2video_tomoviee_2.5_head_and_tail

Tool: `image_to_video`. Model: Seedance 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"4k"` | `["480p","720p","1080p","4k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 4K → "4k" |

## image2video_tomoviee_2.5_reference_image

Tool: `reference_to_video`. Model: Seedance 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"4k"` | `["480p","720p","1080p","4k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 4K → "4k" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |

## image2video_tomoviee_3.0

Tool: `image_to_video`. Model: ToMoviee Video 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| — | — | No configurable options | — |

## image2video_tomusic_1_0

Tool: `image_audio_to_video`. Model: ToMusic 1.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"16:9"` | `["adaptive","9:16","16:9","1:1"]` | Auto → "adaptive" |

## image2video_veo_3.1

Tool: `image_to_video`. Model: Google Veo 3.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9"]` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |

## image2video_veo_3.1_fast

Tool: `image_to_video`. Model: Google Veo 3.1 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9"]` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |

## image2video_veo_3.1_lite

Tool: `image_to_video`. Model: Google Veo 3.1 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9"]` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |

## image2video_veo_3.1_lite_head_and_tail

Tool: `image_to_video`. Model: Google Veo 3.1 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `sample_count` | `1` | `[1]` |  |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9"]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |

## image2video_veo_3_fast

Tool: `image_to_video`. Model: Google Veo 3 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `8` | `[8]` | 8s → 8 |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `aspect_ratio` | `"16:9"` | `["16:9"]` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |

## image2video_vidu_2.0

Tool: `image_to_video`. Model: Vidu 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4,8]` | 4s → 4; 8s → 8 |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"duration":[4],"resolution":["720p","1080p"]},{"duration":[8],"resolution":["720p"]}]
```

## image2video_vidu_2.0_head_and_tail

Tool: `image_to_video`. Model: Vidu 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4,8]` | 4s → 4; 8s → 8 |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"duration":[4],"resolution":["720p","1080p"]},{"duration":[8],"resolution":["720p"]}]
```

## image2video_vidu_2.0_reference_image

Tool: `reference_to_video`. Model: Vidu 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `4` | `[4]` |  |
| `resolution` | `"720p"` | `["720p"]` |  |

## image2video_vidu_q1

Tool: `image_to_video`. Model: Vidu Q1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5]` | 5s → 5 |
| `resolution` | `"1080p"` | `["1080p"]` | 1080P → "1080p" |

## image2video_vidu_q1_head_and_tail

Tool: `image_to_video`. Model: Vidu Q1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5]` | 5s → 5 |
| `resolution` | `"1080p"` | `["1080p"]` | 1080P → "1080p" |

## image2video_vidu_q2

Tool: `image_to_video`. Model: Vidu Q2. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `duration` | `8` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `movement_amplitude` | `"auto"` | `["auto"]` |  |

## image2video_vidu_q3

Tool: `image_to_video`. Model: Vidu Q3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `bgm` | `false` | `[true,false]` |  |
| `resolution` | `"720p"` | `["540p","720p","1080p","2K"]` | 540P → "540p"; 720P → "720p"; 1080P → "1080p" |
| `duration` | `8` | `[4,8,12,16]` |  |
| `is_audio` | `true` | `[true,false]` | True → true; is_fasle → false |
| `off_peak` | `false` | `[true,false]` |  |
| `seed` | `0` | `[0]` |  |

## image2video_wan_2.2

Tool: `image_to_video`. Model: Wan 2.2. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5]` | 5s → 5 |
| `resolution` | `"1080P"` | `["1080P"]` |  |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `seed` | `0` | `[0]` |  |
| `prompt_extend` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |

## image2video_wan_2.5

Tool: `image_to_video`. Model: Wan 2.5. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `resolution` | `"480P"` | `["480P","720P","1080P"]` |  |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `seed` | `0` | `[0]` |  |
| `prompt_extend` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |

## image2video_wan_2.6

Tool: `image_to_video`. Model: Wan 2.6. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[5,10,15]` | 5s → 5; 10s → 10; 15s → 15 |
| `generate_audio` | `true` | `[true,false]` | True → true; False → false |
| `prompt_extend` | `true` | `[true,false]` |  |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `watermark` | `false` | `[true,false]` |  |
| `resolution` | `"720P"` | `["720P","1080P"]` |  |
| `seed` | `-1` | `[-1]` |  |
| `shot_type` | `"multi"` | `["multi","single"]` | True → "multi"; False → "single" |

## image2video_wan_3.0

Tool: `image_to_video`. Model: Wan 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480P"` | `["480P","720P","1080P"]` |  |
| `ratio` | `"1:1"` | `["adaptive","16:9","9:16","4:3","3:4","1:1"]` | Auto → "adaptive" |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |

## image2video_wan_3.0_head_and_tail

Tool: `image_to_video`. Model: Wan 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480P"` | `["480P","720P","1080P"]` |  |
| `ratio` | `"1:1"` | `["adaptive","16:9","9:16","4:3","3:4","1:1"]` | Auto → "adaptive" |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |

## image2video_wan_3.0_reference_image

Tool: `reference_to_video`. Model: Wan 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480P"` | `["480P","720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |
| `generate_audio` | `true` | `[true,false]` |  |
| `aspect_ratio` | `"adaptive"` | `["adaptive","16:9","9:16","4:3","3:4","1:1"]` | Auto → "adaptive" |

## text2image_gemini_omni_flash

Tool: `text_to_video`. Model: Gemini Omni Flash. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16"]` |  |
| `duration_s` | `"3s"` | `["3s","5s","8s","10s"]` | UI meaning: duration |

## text2video_happyhorse_1.0

Tool: `text_to_video`. Model: HappyHorse 1.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"1080P"` | `["720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"16:9"` | `["9:16","16:9","1:1","3:4","4:3"]` |  |
| `seed` | `0` | `[0]` |  |

## text2video_happyhorse_1.5

Tool: `text_to_video`. Model: HappyHorse 1.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"1080P"` | `["720P","1080P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |
| `ratio` | `"16:9"` | `["16:9","9:16","1:1","3:4","4:3","21:9"]` |  |
| `seed` | `0` | `[0]` |  |

## text2video_kling_2.5_turbo

Tool: `text_to_video`. Model: Kling 2.5 Turbo. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `cfg_scale` | `0` | `[0]` |  |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16","1:1"]` |  |
| `resolution` | `"std"` | `["std","pro"]` | 720P → "std"; 1080P → "pro" |

## text2video_kling_2.6

Tool: `text_to_video`. Model: Kling 2.6. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `mode` | `"pro"` | `["pro"]` |  |
| `sound` | `"on"` | `["on","off"]` | UI meaning: generate_audio; On → "on"; Off → "off" |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1"]` |  |
| `duration_string` | `"5"` | `["5","10"]` | UI meaning: duration; 5s → "5"; 10s → "10" |
| `cfg_scale` | `0.5` | `[0.5]` |  |

## text2video_kling_3.0

Tool: `text_to_video`. Model: Kling 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `sound` | `"on"` | `["on","off"]` | UI meaning: generate_audio; True → "on"; False → "off" |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1"]` |  |
| `duration_string` | `"5"` | `["5","8","10","15"]` | UI meaning: duration; 5s → "5"; 8s → "8"; 10s → "10"; 15s → "15" |
| `mode` | `"4k"` | `["std","pro","4k"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro"; 4K → "4k" |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `multi_shots` | `true` | `[true,false]` | True → true; False → false |
| `shot_type` | `"intelligence"` | `["intelligence"]` |  |

## text2video_kling_3.0_fast

Tool: `text_to_video`. Model: Kling 3.0 Turbo. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16","1:1"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## text2video_kling_o1

Tool: `text_to_video`. Model: Kling O1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1"]` |  |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `mode` | `"std"` | `["std","pro"]` | UI meaning: resolution; 720P → "std"; 1080P → "pro" |

## text2video_minimax_2.3

Tool: `text_to_video`. Model: Hailuo 2.3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `prompt_extend` | `false` | `[true,false]` |  |
| `resolution` | `"768P"` | `["768P","1080P"]` |  |
| `duration` | `6` | `[6,10]` | 6s → 6; 10s → 10 |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"duration":[6],"resolution":["768P","1080P"]},{"duration":[10],"resolution":["768P"]}]
```

## text2video_minimax_h3_max

Tool: `text_to_video`. Model: MiniMax H3 Max. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"768P"` | `["480P","768P"]` |  |
| `duration` | `5` | `[5,15]` | 5s → 5; 15s → 15 |
| `ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","21:9"]` |  |

## text2video_minimax_h3_switch

Tool: `text_to_video`. Model: MiniMax H3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480p"` | `["480p","2k"]` | 768P → "480p"; 2K → "2k" |
| `duration` | `5` | `[5,15]` | 5s → 5; 15s → 15 |
| `ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","21:9"]` |  |

## text2video_seedance_2.0_mini

Tool: `text_to_video`. Model: Seedance 2.0 Mini. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## text2video_seedance_2.5

Tool: `text_to_video`. Model: Seedance 2.5. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive","21:9","16:9","4:3","1:1","3:4","9:16"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p","1080p"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p" |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |

## text2video_seedance2.0_fast

Tool: `text_to_video`. Model: Seedance 2.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"480p"` | `["480p","720p"]` | 480P → "480p"; 720P → "720p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## text2video_tomoviee4_switch

Tool: `text_to_video`. Model: ToMoviee Video 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"2K"` | `["2K","768P"]` |  |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |
| `ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4","21:9"]` |  |

## text2video_tomoviee_2.0

Tool: `text_to_video`. Model: ToMoviee Video 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `duration` | `5` | `[5]` |  |
| `aspect_ratio` | `"16:9"` | `["16:9"]` |  |

## text2video_tomoviee_2.5

Tool: `text_to_video`. Model: Seedance 2.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "adaptive" |
| `resolution` | `"4k"` | `["480p","720p","1080p","4k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p" |
| `duration` | `5` | `[5,8,10,15]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15 |

## text2video_veo_3.1

Tool: `text_to_video`. Model: Google Veo 3.1. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `seed` | `-1` | `[-1]` |  |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16"]` |  |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |

## text2video_veo_3.1_fast

Tool: `text_to_video`. Model: Google Veo 3.1 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `seed` | `-1` | `[-1]` |  |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16"]` |  |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |

## text2video_veo_3.1_lite

Tool: `text_to_video`. Model: Google Veo 3.1 Lite. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `seed` | `-1` | `[-1]` |  |
| `aspect_ratio` | `"16:9"` | `["16:9","9:16"]` |  |
| `duration` | `4` | `[4,6,8]` | 4s → 4; 6s → 6; 8s → 8 |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `generate_audio` | `true` | `[true,false]` | True → true; False → false |

## text2video_veo_3_fast

Tool: `text_to_video`. Model: Google Veo 3 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `seed` | `-1` | `[-1]` |  |
| `aspect_ratio` | `"16:9"` | `["16:9"]` |  |
| `duration` | `8` | `[8]` | 8s → 8 |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `person_generation` | `"allow_adult"` | `["allow_adult"]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `sample_count` | `1` | `[1]` |  |
| `generate_audio` | `true` | `[true,false]` | On → true; Off → false |

## text2video_vidu_q3

Tool: `text_to_video`. Model: Vidu Q3. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720p"` | `["540p","720p","1080p","2K"]` | 540P → "540p"; 720P → "720p"; 1080P → "1080p" |
| `aspect_ratio` | `"9:16"` | `["9:16","16:9","1:1","4:3","3:4"]` |  |
| `bgm` | `false` | `[true,false]` |  |
| `is_audio` | `true` | `[true,false]` | True → true; is_fasle → false |
| `seed` | `0` | `[0]` |  |
| `duration` | `8` | `[4,8,12,16]` | 4s → 4; 8s → 8; 12s → 12; 16s → 16 |
| `off_peak` | `false` | `[true,false]` |  |

## text2video_wan_2.5

Tool: `text_to_video`. Model: Wan 2.5. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `seed` | `0` | `[0]` |  |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `duration` | `5` | `[5,10]` | 5s → 5; 10s → 10 |
| `size` | `"1280*720"` | `["1280*720","720*1280","960*960","1088*832","832*1088"]` | 16:9 → "1280*720"; 9:16 → "720*1280"; 1:1 → "960*960"; 4:3 → "1088*832"; 3:4 → "832*1088" |
| `prompt_extend` | `false` | `[true,false]` |  |
| `watermark` | `false` | `[true,false]` |  |

## text2video_wan_2.6

Tool: `text_to_video`. Model: Wan 2.6. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"720P"` | `["720P","1080P"]` |  |
| `size` | `"1280*720"` | `["1280*720","1920*1080","720*1280","1080*1920","960*960","1440*1440","1088*832","1632*1248","832*1088","1248*1632"]` | 16:9 (resolution="720P") → "1280*720"; 16:9 (resolution="1080P") → "1920*1080"; 9:16 (resolution="720P") → "720*1280"; 9:16 (resolution="1080P") → "1080*1920"; 1:1 (resolution="720P") → "960*960"; 1:1 (resolution="1080P") → "1440*1440"; 4:3 (resolution="720P") → "1088*832"; 4:3 (resolution="1080P") → "1632*1248"; 3:4 (resolution="720P") → "832*1088"; 3:4 (resolution="1080P") → "1248*1632"; Unspecified label context defaults: {"resolution":"720P"} |
| `negative_prompt` | `""` | `{"kind":"text","minLength":0,"maxLength":1500}` |  |
| `generate_audio` | `true` | `[true,false]` | True → true; False → false |
| `prompt_extend` | `true` | `[true,false]` |  |
| `shot_type` | `"multi"` | `["multi","single"]` | True → "multi"; False → "single" |
| `seed` | `0` | `[0]` |  |
| `duration` | `5` | `[5,10,15]` | 5s → 5; 10s → 10; 15s → 15 |
| `watermark` | `false` | `[true,false]` |  |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"resolution":["720P"],"size":["1280*720","720*1280","960*960","1088*832","832*1088"]},{"resolution":["1080P"],"size":["1920*1080","1080*1920","1440*1440","1632*1248","1248*1632"]}]
```

## text2video_wan_3.0

Tool: `text_to_video`. Model: Wan 3.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `resolution` | `"480P"` | `["480P","720P","1080P"]` |  |
| `ratio` | `"adaptive"` | `["adaptive","16:9","9:16","4:3","3:4","1:1"]` | Auto → "adaptive" |
| `duration` | `5` | `[5,8,10,15,20,25,30]` | 5s → 5; 8s → 8; 10s → 10; 15s → 15; 20s → 20; 25s → 25; 30s → 30 |

## image2video_kling_4.0

Tool: `image_to_video`. Model: Kling 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `10` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |

## image2video_kling_4.0_head_and_tail

Tool: `image_to_video`. Model: Kling 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `10` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |

## image2video_kling_4.0_reference_image

Tool: `reference_to_video`. Model: Kling 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `10` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `aspect_ratio` | `"adaptive"` | `["adaptive","9:16","16:9","1:1","21:9"]` | Auto → "adaptive" |

## image2video_tomoviee_3.0_fast

Tool: `image_to_video`. Model: ToMoviee Video 3.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `aspect_ratio` | `"auto"` | `["auto","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "auto" |
| `resolution` | `"480p"` | `["480p","720p","1080p","2k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 2K → "2k" |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"resolution":["480p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["720p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["1080p"],"duration":[3,4,5,6,7,8,9,10]},{"resolution":["2k"],"duration":[3,4,5]}]
```

## image2video_tomoviee_3.0_fast_head_and_tail

Tool: `image_to_video`. Model: ToMoviee Video 3.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `aspect_ratio` | `"auto"` | `["auto","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "auto" |
| `resolution` | `"480p"` | `["480p","720p","1080p","2k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 2K → "2k" |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"resolution":["480p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["720p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["1080p"],"duration":[3,4,5,6,7,8,9,10]},{"resolution":["2k"],"duration":[3,4,5]}]
```

## image2video_tomoviee_3.0_fast_reference_image

Tool: `reference_to_video`. Model: ToMoviee Video 3.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `resolution` | `"480p"` | `["480p","720p","1080p","2k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 2K → "2k" |
| `aspect_ratio` | `"auto"` | `["auto","21:9","16:9","4:3","1:1","3:4","9:16"]` | Auto → "auto" |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"resolution":["480p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["720p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["1080p"],"duration":[3,4,5,6,7,8,9,10]},{"resolution":["2k"],"duration":[3,4,5]}]
```

## text2video_kling_4.0

Tool: `text_to_video`. Model: Kling 4.0. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `ratio` | `"9:16"` | `["9:16","16:9","1:1","21:9"]` | UI meaning: aspect_ratio |
| `resolution` | `"720p"` | `["720p","1080p"]` | 720P → "720p"; 1080P → "1080p" |
| `duration` | `10` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |

## text2video_tomoviee_3.0_fast

Tool: `text_to_video`. Model: ToMoviee Video 3.0 Fast. Status: active.

| request.options field | Default | Allowed values / range | UI meaning and label mappings |
| --- | --- | --- | --- |
| `duration` | `5` | `[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]` |  |
| `resolution` | `"480p"` | `["480p","720p","1080p","2k"]` | 480P → "480p"; 720P → "720p"; 1080P → "1080p"; 2K → "2k" |
| `aspect_ratio` | `"auto"` | `["auto","9:16","16:9","1:1","4:3","3:4","21:9"]` | Auto → "auto" |

Coupled option branches (choose one complete branch; other fields retain their own allowed values):

```json
[{"resolution":["480p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["720p"],"duration":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]},{"resolution":["1080p"],"duration":[3,4,5,6,7,8,9,10]},{"resolution":["2k"],"duration":[3,4,5]}]
```
