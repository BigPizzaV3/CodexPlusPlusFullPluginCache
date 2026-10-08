# Image — Parameter Reference

Parameter reference for every PDF4me **image** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

Most endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`. A few image endpoints use unusual field names or query-string selectors; those exceptions are called out in their sections.

Docs index: https://docs.pdf4me.com/pdf4me-api/image/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [Watermarks and overlays](#watermarks-and-overlays)
  - [AddImageWatermarkToImage](#addimagewatermarktoimage)
  - [AddTextWatermarkToImage](#addtextwatermarktoimage)
- [Convert and optimize](#convert-and-optimize)
  - [CompressImage](#compressimage)
  - [ConvertImageFormat](#convertimageformat)
  - [CreateImages](#createimages)
- [Crop, flip, resize, and rotate](#crop-flip-resize-and-rotate)
  - [CropImage](#cropimage)
  - [FlipImage](#flipimage)
  - [ResizeImage](#resizeimage)
  - [RotateImageByExifData](#rotateimagebyexifdata)
  - [RotateImage](#rotateimage)
- [Metadata and extraction](#metadata-and-extraction)
  - [GetImageMetadata](#getimagemetadata)
  - [ImageExtractText](#imageextracttext)
  - [RemoveEXIFTagsFromImage](#removeexiftagsfromimage)

---

## Quick index — pick the right endpoint

| User intent                                              | Action                     |
| -------------------------------------------------------- | -------------------------- |
| Add an image logo or watermark on top of an image        | `AddImageWatermarkToImage` |
| Add a text watermark or label to an image                | `AddTextWatermarkToImage`  |
| Compress or reduce the file size of an image             | `CompressImage`            |
| Convert an image from one format to another              | `ConvertImageFormat`       |
| Convert a PDF page to an image or generate a thumbnail   | `CreateImages`             |
| Crop an image by removing borders or extracting a region | `CropImage`                |
| Flip an image horizontally or vertically                 | `FlipImage`                |
| Read technical properties or metadata from an image      | `GetImageMetadata`         |
| Extract text from an image using OCR                     | `ImageExtractText`         |
| Resize an image to exact dimensions or a percentage      | `ResizeImage`              |
| Auto-rotate an image using its EXIF orientation          | `RotateImageByExifData`    |
| Rotate an image by a specific angle                      | `RotateImage`              |
| Strip EXIF metadata from an image for privacy            | `RemoveEXIFTagsFromImage`  |

---

## Watermarks and overlays

### AddImageWatermarkToImage

`POST /api/v2/AddImageWatermarkToImage` — overlays a watermark image on top of a source image with placement, opacity, offset, and rotation control.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/add-image-watermark-to-image.md

**Supported inputs:** common raster image formats such as JPG, PNG, BMP, GIF, and TIFF.

| JSON Key               | Type          | Required | Allowed values / notes                                                                                               |
| ---------------------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `docName`              | string        | Yes      | Source image filename with extension, e.g. `photo.jpg`.                                                              |
| `docContent`           | base64 string | Yes      | Base64 of the source image.                                                                                          |
| `WatermarkFileName`    | string        | Yes      | Watermark image filename with extension, e.g. `logo.png`.                                                            |
| `WatermarkFileContent` | base64 string | Yes      | Base64 of the watermark image.                                                                                       |
| `Position`             | string        | Yes      | `topright`, `topleft`, `bottomright`, `bottomleft`, `centralhorizontal`, `diagonal`, `centralvertical`, or `custom`. |
| `Opacity`              | number        | No       | 0.0 = transparent, 1.0 = opaque. Default `1.0`.                                                                      |
| `HorizontalOffset`     | integer       | No       | Horizontal offset in pixels. Default `0`.                                                                            |
| `VerticalOffset`       | integer       | No       | Vertical offset in pixels. Default `0`.                                                                              |
| `PositionX`            | number        | No       | Exact X coordinate when `Position` is `custom`. Default `0`.                                                         |
| `PositionY`            | number        | No       | Exact Y coordinate when `Position` is `custom`. Default `0`.                                                         |
| `Rotation`             | number        | No       | Rotation angle in degrees. Default `0`.                                                                              |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>",
  "WatermarkFileName": "logo.png",
  "WatermarkFileContent": "<base64>",
  "Position": "diagonal",
  "Opacity": 0.5,
  "PositionX": 0,
  "PositionY": 0,
  "Rotation": 0
}
```

**Notes:** Use `Position: "custom"` only when you also provide `PositionX` and `PositionY`. For corner and center placements, offsets are usually easier than raw coordinates.

---

### AddTextWatermarkToImage

`POST /api/v2/AddTextWatermarkToImage` — overlays text onto an image with control over font, color, styling, opacity, rotation, and placement.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/add-text-watermark-to-image.md

**Supported inputs:** common raster image formats.

| JSON Key         | Type          | Required | Allowed values / notes                                                                                               |
| ---------------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `docName`        | string        | Yes      | Source image filename with extension.                                                                                |
| `docContent`     | base64 string | Yes      | Base64 of the source image.                                                                                          |
| `WatermarkText`  | string        | Yes      | Text string to render as the watermark.                                                                              |
| `TextPosition`   | string        | Yes      | `topright`, `topleft`, `bottomright`, `bottomleft`, `centralhorizontal`, `diagonal`, `centralvertical`, or `custom`. |
| `TextFontFamily` | string        | Yes      | Font family, e.g. `Arial`, `Times New Roman`.                                                                        |
| `IsUnderline`    | boolean       | Yes      | `true` to underline the text.                                                                                        |
| `IsItalic`       | boolean       | Yes      | `true` to italicize the text.                                                                                        |
| `TextFontSize`   | integer       | No       | Font size in points. Default `30`.                                                                                   |
| `TextColour`     | string        | No       | Hex color code or color name. Default `"#b4351a"`.                                                                   |
| `IsBold`         | boolean       | No       | `true` to bold the text. Default `false`.                                                                            |
| `Opacity`        | number        | No       | 0.0 = transparent, 1.0 = opaque. Default `1`.                                                                        |
| `RotationAngle`  | number        | No       | Text rotation in degrees. Default `0`.                                                                               |
| `PositionX`      | number        | No       | Exact X coordinate when `TextPosition` is `custom`. Default `272.0`.                                                 |
| `PositionY`      | number        | No       | Exact Y coordinate when `TextPosition` is `custom`. Default `0`.                                                     |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>",
  "WatermarkText": "CONFIDENTIAL",
  "TextPosition": "diagonal",
  "TextFontFamily": "Arial",
  "TextFontSize": 40,
  "TextColour": "#FF0000",
  "IsBold": true,
  "IsUnderline": false,
  "IsItalic": false,
  "Opacity": 0.6,
  "RotationAngle": 0,
  "PositionX": 272.0,
  "PositionY": 0
}
```

**Notes:** When `TextPosition` is not `custom`, `PositionX` and `PositionY` usually do not matter. Use a lower opacity for watermark-style overlays and full opacity for labels or badges.

---

## Convert and optimize

### CompressImage

`POST /api/v2/CompressImage` — compresses an image to reduce file size with selectable output format and compression profile.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/compress-image.md

**Supported inputs:** JPG, PNG, and WebP.

| JSON Key           | Type          | Required | Allowed values / notes                                               |
| ------------------ | ------------- | -------- | -------------------------------------------------------------------- |
| `docName`          | string        | Yes      | Source image filename with extension, e.g. `photo.jpg`.              |
| `docContent`       | base64 string | Yes      | Base64 of the source image. Docs note JPG, PNG, or WebP up to 50 MB. |
| `imageType`        | string        | Yes      | Output format: `JPG`, `PNG`, or `WebP`.                              |
| `compressionLevel` | string        | Yes      | `Max`, `Medium`, or `Low`.                                           |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>",
  "imageType": "JPG",
  "compressionLevel": "Medium"
}
```

**Notes:** `Max` prioritizes file size reduction, while `Low` preserves more quality. If output format matters, set `imageType` explicitly rather than assuming it will follow the input extension.

---

### ConvertImageFormat

`POST /api/v2/ConvertImageFormat` — converts an image from one raster format to another.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/convert-image-format.md

**Supported inputs:** BMP, GIF, JPG, PNG, and TIFF.

| JSON Key             | Type          | Required | Allowed values / notes                 |
| -------------------- | ------------- | -------- | -------------------------------------- |
| `docName`            | string        | Yes      | Source image filename with extension.  |
| `docContent`         | base64 string | Yes      | Base64 of the source image.            |
| `CurrentImageFormat` | string        | Yes      | `BMP`, `GIF`, `JPG`, `PNG`, or `TIFF`. |
| `NewImageFormat`     | string        | Yes      | `BMP`, `GIF`, `JPG`, `PNG`, or `TIFF`. |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>",
  "CurrentImageFormat": "JPG",
  "NewImageFormat": "PNG"
}
```

---

### CreateImages

`POST /api/v2/CreateImages` — renders one or more PDF pages to images for previews, thumbnails, or downstream image workflows.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/create-image-from-pdf.md

**Supported inputs:** PDF.

> **Nested payload note:** this endpoint uses `docname` (lowercase `n`) and a nested `imageAction` object rather than a flat payload.

| JSON Key                            | Type              | Required | Allowed values / notes                                                                        |
| ----------------------------------- | ----------------- | -------- | --------------------------------------------------------------------------------------------- |
| `docname`                           | string            | Yes      | Source PDF filename, e.g. `document.pdf`.                                                     |
| `docContent`                        | base64 string     | Yes      | Base64 of the source PDF.                                                                     |
| `imageAction.ImageExtension`        | string            | Yes      | Output format: `JPG`, `JPEG`, `BMP`, `GIF`, `JB2`, `JP2`, `JPF`, `JPX`, `PNG`, `TIF`, `TIFF`. |
| `imageAction.WidthPixel`            | number            | Yes      | Output width in pixels. Height follows aspect ratio.                                          |
| `pageNrs`                           | string            | No       | Page selector string such as `"all"`, `"1,3,5"`, `"2-5"`, `"7-"`, or `"last"`. Default `"1"`. |
| `imageAction.PageSelection.PageNrs` | array of integers | No       | Alternative page selection array, e.g. `[1, 2]`.                                              |

**Example payload:**

```json
{
  "docname": "document.pdf",
  "docContent": "<base64>",
  "imageAction": {
    "WidthPixel": "800",
    "ImageExtension": "jpeg",
    "PageSelection": {
      "PageNrs": [1]
    }
  },
  "pageNrs": "1"
}
```

**Notes:** Prefer one page-selection style to avoid ambiguity. `WidthPixel` controls output size; use smaller values for thumbnails and larger values for web previews.

---

## Crop, flip, resize, and rotate

### CropImage

`POST /api/v2/CropImage?schemaVal=Border` — crops an image either by trimming border pixels or by extracting a rectangular region.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/crop-image.md

| JSON Key       | Type          | Required    | Allowed values / notes                                              |
| -------------- | ------------- | ----------- | ------------------------------------------------------------------- |
| `docName`      | string        | Yes         | Source image filename with extension.                               |
| `docContent`   | base64 string | Yes         | Base64 of the source image.                                         |
| `CropType`     | string        | Yes         | `Border` to trim edges or `Rectangle` to extract a region.          |
| `LeftBorder`   | integer       | Conditional | Required for `Border` mode. Pixels to remove from the left edge.    |
| `RightBorder`  | integer       | Conditional | Required for `Border` mode. Pixels to remove from the right edge.   |
| `TopBorder`    | integer       | Conditional | Required for `Border` mode. Pixels to remove from the top edge.     |
| `BottomBorder` | integer       | Conditional | Required for `Border` mode. Pixels to remove from the bottom edge.  |
| `UpperLeftX`   | integer       | Conditional | Required for `Rectangle` mode. X coordinate of the crop region.     |
| `UpperLeftY`   | integer       | Conditional | Required for `Rectangle` mode. Y coordinate of the crop region.     |
| `Width`        | integer       | Conditional | Required for `Rectangle` mode. Width of the crop region in pixels.  |
| `Height`       | integer       | Conditional | Required for `Rectangle` mode. Height of the crop region in pixels. |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>",
  "CropType": "Border",
  "LeftBorder": 10,
  "RightBorder": 20,
  "TopBorder": 20,
  "BottomBorder": 20,
  "UpperLeftX": 0,
  "UpperLeftY": 0,
  "Width": 0,
  "Height": 0
}
```

**Notes:** The docs say to send all crop fields and set unused ones to `0`. That is unusual but worth following exactly for this endpoint.

---

### FlipImage

`POST /api/v2/FlipImage` — flips an image horizontally or vertically.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/flip-image.md

> **Key-casing note:** this endpoint uses the Indonesian key `Jenis orientasi` exactly as shown.

| JSON Key          | Type          | Required | Allowed values / notes                |
| ----------------- | ------------- | -------- | ------------------------------------- |
| `docContent`      | base64 string | Yes      | Base64 of the source image.           |
| `docName`         | string        | Yes      | Source image filename with extension. |
| `Jenis orientasi` | string        | Yes      | `horizontal` or `vertical`.           |

**Example payload:**

```json
{
  "docContent": "<base64>",
  "docName": "photo.jpg",
  "Jenis orientasi": "horizontal"
}
```

---

### ResizeImage

`POST /api/v2/ResizeImage?schemaVal=Percentange` — resizes an image either by percentage or by explicit pixel dimensions.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/resize-image.md

> **Docs spelling note:** the query string is documented as `Percentange` with that spelling.

| JSON Key              | Type           | Required    | Allowed values / notes                                       |
| --------------------- | -------------- | ----------- | ------------------------------------------------------------ |
| `docName`             | string         | Yes         | Source image filename with extension.                        |
| `docContent`          | base64 string  | Yes         | Base64 of the source image.                                  |
| `ImageResizeType`     | string         | Yes         | `Percentage` or `Specific`.                                  |
| `ResizePercentage`    | decimal string | Conditional | Required for `Percentage` mode, e.g. `"50.0"` for 50%.       |
| `Width`               | integer        | Conditional | Required for `Specific` mode. Target width in pixels.        |
| `Height`              | integer        | Conditional | Required for `Specific` mode. Target height in pixels.       |
| `MaintainAspectRatio` | boolean        | Yes         | `true` to preserve proportions, `false` to allow stretching. |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>",
  "ImageResizeType": "Percentage",
  "ResizePercentage": "50.0",
  "Width": 0,
  "Height": 0,
  "MaintainAspectRatio": true
}
```

**Notes:** For `Percentage` mode, docs say to set `Width` and `Height` to `0`. For `Specific` mode, `ResizePercentage` can be `"0"`.

---

### RotateImageByExifData

`POST /api/v2/RotateImageByExifData` — auto-rotates an image based on its embedded EXIF orientation tag.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/rotate-image-by-exif-data.md

| JSON Key     | Type          | Required | Allowed values / notes                                  |
| ------------ | ------------- | -------- | ------------------------------------------------------- |
| `docName`    | string        | Yes      | Source image filename with extension, e.g. `photo.jpg`. |
| `docContent` | base64 string | Yes      | Base64 of the source image.                             |

**Example payload:**

```json
{
  "docName": "photo.jpg",
  "docContent": "<base64>"
}
```

---

### RotateImage

`POST /api/v2/RotateImage` — rotates an image by a specified angle with explicit control over background color and proportional scaling.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/rotate-image.md

> **Key-casing note:** this endpoint uses Indonesian field names exactly as shown below.

| JSON Key                  | Type          | Required | Allowed values / notes                                                                    |
| ------------------------- | ------------- | -------- | ----------------------------------------------------------------------------------------- |
| `Nama file`               | string        | Yes      | Source image filename with extension, e.g. `image.jpg`.                                   |
| `Konten file`             | base64 string | Yes      | Base64 of the source image.                                                               |
| `Warna latar`             | string        | Yes      | Background color for exposed corners, e.g. `white`, `black`, `transparent`, or `#FFFFFF`. |
| `Pembesaran proporsional` | boolean       | Yes      | `true` to preserve aspect ratio, `false` to allow distortion.                             |
| `Sudut rotasi`            | integer       | No       | Rotation angle in degrees. Default `0`.                                                   |

**Example payload:**

```json
{
  "Nama file": "photo.jpg",
  "Konten file": "<base64>",
  "Warna latar": "white",
  "Pembesaran proporsional": true,
  "Sudut rotasi": 90
}
```

---

## Metadata and extraction

### GetImageMetadata

`POST /api/v2/GetImageMetadata` — extracts technical properties and metadata from an image.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/get-image-metadata.md

> **Key-casing note:** the request keys are documented in Indonesian and should be used exactly as written.

| JSON Key        | Type          | Required | Allowed values / notes                                  |
| --------------- | ------------- | -------- | ------------------------------------------------------- |
| `Nama File PDF` | string        | Yes      | Source image filename with extension, e.g. `image.jpg`. |
| `Konten PDF`    | base64 string | Yes      | Base64 of the source image.                             |
| `Jenis Gambar`  | string        | Yes      | `jpg`, `png`, `bmp`, `gif`, or `tiff`.                  |

**Example payload:**

```json
{
  "Nama File PDF": "photo.jpg",
  "Konten PDF": "<base64>",
  "Jenis Gambar": "jpg"
}
```

**Notes:** Despite the key names including `PDF`, this endpoint is described as operating on image files, not PDFs.

---

### ImageExtractText

`POST /api/v2/ImageExtractText` — runs OCR on an image and returns extracted text output.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/image-extract-text.md

**Supported inputs:** JPG, PNG, BMP, and TIFF.

| JSON Key     | Type          | Required | Allowed values / notes                                 |
| ------------ | ------------- | -------- | ------------------------------------------------------ |
| `docName`    | string        | Yes      | Source image filename with extension, e.g. `scan.jpg`. |
| `docContent` | base64 string | Yes      | Base64 of the source image.                            |

**Example payload:**

```json
{
  "docName": "scan.jpg",
  "docContent": "<base64>"
}
```

---

### RemoveEXIFTagsFromImage

`POST /api/v2/RemoveEXIFTagsFromImage` — removes EXIF metadata such as GPS coordinates, timestamps, and device information from an image.

**Docs:** https://docs.pdf4me.com/pdf4me-api/image/remove-EXIF-tags-from-image.md

| JSON Key     | Type          | Required | Allowed values / notes                |
| ------------ | ------------- | -------- | ------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the source image.           |
| `docName`    | string        | Yes      | Source image filename with extension. |
| `imageType`  | string        | Yes      | Output format: `JPG` or `PNG`.        |

**Example payload:**

```json
{
  "docContent": "<base64>",
  "docName": "photo.jpg",
  "imageType": "JPG"
}
```

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/image/
