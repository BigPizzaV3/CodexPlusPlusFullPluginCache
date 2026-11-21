# Palette

This file carries the package palette settings, active shade values by mode, palette roles, contrast model, and palette profiles. Semantic tokens should normally be used first, but the primitive palette values are fully listed here for exact resolution.

## Canonical Palette Data

```yaml
colorContrastModels:
  - "WCAG 2.2 AA"
  - "WCAG 2.2 AAA"
  - "APCA"
  - "OKLCH guidance"
colorProfiles:
  -
    id: "tailwind"
    label: "50-900 (Tailwind)"
    shadeLabels:
      - "50"
      - "100"
      - "200"
      - "300"
      - "400"
      - "500"
      - "600"
      - "700"
      - "800"
      - "900"
  -
    id: "material"
    label: "100-500 (Material)"
    shadeLabels:
      - "100"
      - "200"
      - "300"
      - "400"
      - "500"
  -
    id: "carbon"
    label: "10-100 (Carbon)"
    shadeLabels:
      - "10"
      - "20"
      - "30"
      - "40"
      - "50"
      - "60"
      - "70"
      - "80"
      - "90"
      - "100"
  -
    id: "open-color"
    label: "0-9 (Open Color)"
    shadeLabels:
      - "0"
      - "1"
      - "2"
      - "3"
      - "4"
      - "5"
      - "6"
      - "7"
      - "8"
      - "9"
  -
    id: "ant-design"
    label: "1-10 (Ant Design)"
    shadeLabels:
      - "1"
      - "2"
      - "3"
      - "4"
      - "5"
      - "6"
      - "7"
      - "8"
      - "9"
      - "10"
  -
    id: "bootstrap"
    label: "100-900 (Bootstrap)"
    shadeLabels:
      - "100"
      - "200"
      - "300"
      - "400"
      - "500"
      - "600"
      - "700"
      - "800"
      - "900"
  -
    id: "atlassian"
    label: "100-1000 (Atlassian)"
    shadeLabels:
      - "100"
      - "200"
      - "300"
      - "400"
      - "500"
      - "600"
      - "700"
      - "800"
      - "900"
      - "1000"
  -
    id: "untitled-ui"
    label: "25-950 (Untitled UI)"
    shadeLabels:
      - "25"
      - "50"
      - "100"
      - "200"
      - "300"
      - "400"
      - "500"
      - "600"
      - "700"
      - "800"
      - "900"
      - "950"
  -
    id: "base-uber"
    label: "50-700 (Base Uber)"
    shadeLabels:
      - "50"
      - "100"
      - "200"
      - "300"
      - "400"
      - "500"
      - "600"
      - "700"
  -
    id: "fluent"
    label: "10-160 (Fluent)"
    shadeLabels:
      - "10"
      - "20"
      - "30"
      - "40"
      - "50"
      - "60"
      - "70"
      - "80"
      - "90"
      - "100"
      - "110"
      - "120"
      - "130"
      - "140"
      - "150"
      - "160"
colorRoleLabels:
  - "Primary"
  - "Secondary"
  - "Tertiary"
  - "System"
  - "Warning"
  - "Danger"
  - "Info"
  - "Success"
colorRoles:
  -
    id: "primary"
    label: "Primary"
  -
    id: "secondary"
    label: "Secondary"
  -
    id: "tertiary"
    label: "Tertiary"
  -
    id: "system"
    label: "System"
  -
    id: "warning"
    label: "Warning"
  -
    id: "danger"
    label: "Danger"
  -
    id: "info"
    label: "Info"
  -
    id: "success"
    label: "Success"
defaultContrastModel: "WCAG 2.2 AA"
defaultProfileLabel: "50-900 (Tailwind)"
palettesByMode:
  dark:
    -
      group: "brand"
      name: "Primary"
      paletteId: "palette.primary"
      role: "primary"
      shades:
        -
          hex: "#D5DCE8"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#B7C5E1"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#92AEE0"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#6C95E5"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#4079EE"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#0A4FDF"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#134CC8"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#0B3A9D"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#062770"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#031643"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "primary"
    -
      group: "brand"
      name: "Secondary"
      paletteId: "palette.secondary"
      role: "secondary"
      shades:
        -
          hex: "#E6EDE5"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#C7DAC8"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#A6C6A5"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#7FB581"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#52A457"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#058625"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#197C2A"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#156221"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#0F4817"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#0D2E10"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "secondary"
    -
      group: "brand"
      name: "Tertiary"
      paletteId: "palette.tertiary"
      role: "tertiary"
      shades:
        -
          hex: "#E8E2D5"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#E2D3B5"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#E1C590"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#E5BA65"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#EFB035"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#FCA701"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#CD8801"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#9E6800"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#6F4900"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#3F2A00"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "tertiary"
    -
      group: "system"
      name: "Neutral"
      paletteId: "palette.neutral"
      role: "system"
      shades:
        -
          hex: "#F1F1F1"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#CECECE"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#A1A1A1"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#767676"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#5C5C5C"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#333333"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#2E2E2E"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#242424"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#1C1C1C"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#151515"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "neutral"
    -
      group: "system"
      name: "Warning"
      paletteId: "palette.warning"
      role: "warning"
      shades:
        -
          hex: "#E8E2D6"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#FFBD4F"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#AE6D00"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#402800"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "warning"
    -
      group: "system"
      name: "Danger"
      paletteId: "palette.danger"
      role: "danger"
      shades:
        -
          hex: "#ECDFDF"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#EF4444"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#B80808"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#4D0000"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "danger"
    -
      group: "system"
      name: "Info"
      paletteId: "palette.info"
      role: "info"
      shades:
        -
          hex: "#DEE4EC"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#3B82F6"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#0449BA"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#001D4C"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "info"
    -
      group: "system"
      name: "Success"
      paletteId: "palette.success"
      role: "success"
      shades:
        -
          hex: "#DCFCE7"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#86EFAC"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#22C55E"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#166534"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "success"
    -
      group: "system"
      name: "Black & White"
      paletteId: "palette.black-and-white"
      role: "system"
      shades:
        -
          hex: "#000000"
          isOverridden: false
          label: "black"
          shadeId: "black"
        -
          hex: "#FFFFFF"
          isOverridden: false
          label: "white"
          shadeId: "white"
        -
          hex: "#00000000"
          isOverridden: false
          label: "transparent"
          shadeId: "transparent"
      slug: "black-and-white"
  light:
    -
      group: "brand"
      name: "Primary"
      paletteId: "palette.primary"
      role: "primary"
      shades:
        -
          hex: "#D5DCE8"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#B7C5E1"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#92AEE0"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#6C95E5"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#4079EE"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#0A4FDF"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#134CC8"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#0B3A9D"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#062770"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#031643"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "primary"
    -
      group: "brand"
      name: "Secondary"
      paletteId: "palette.secondary"
      role: "secondary"
      shades:
        -
          hex: "#E6EDE5"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#C7DAC8"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#A6C6A5"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#7FB581"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#52A457"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#058625"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#197C2A"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#156221"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#0F4817"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#0D2E10"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "secondary"
    -
      group: "brand"
      name: "Tertiary"
      paletteId: "palette.tertiary"
      role: "tertiary"
      shades:
        -
          hex: "#E8E2D5"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#E2D3B5"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#E1C590"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#E5BA65"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#EFB035"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#FCA701"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#CD8801"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#9E6800"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#6F4900"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#3F2A00"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "tertiary"
    -
      group: "system"
      name: "Neutral"
      paletteId: "palette.neutral"
      role: "system"
      shades:
        -
          hex: "#F1F1F1"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#CECECE"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#A1A1A1"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#767676"
          isOverridden: false
          label: "300"
          shadeId: "300"
        -
          hex: "#5C5C5C"
          isOverridden: false
          label: "400"
          shadeId: "400"
        -
          hex: "#333333"
          isOverridden: false
          label: "500"
          shadeId: "500"
        -
          hex: "#2E2E2E"
          isOverridden: false
          label: "600"
          shadeId: "600"
        -
          hex: "#242424"
          isOverridden: false
          label: "700"
          shadeId: "700"
        -
          hex: "#1C1C1C"
          isOverridden: false
          label: "800"
          shadeId: "800"
        -
          hex: "#151515"
          isOverridden: false
          label: "900"
          shadeId: "900"
      slug: "neutral"
    -
      group: "system"
      name: "Warning"
      paletteId: "palette.warning"
      role: "warning"
      shades:
        -
          hex: "#E8E2D6"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#FFBD4F"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#AE6D00"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#402800"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "warning"
    -
      group: "system"
      name: "Danger"
      paletteId: "palette.danger"
      role: "danger"
      shades:
        -
          hex: "#ECDFDF"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#EF4444"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#B80808"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#4D0000"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "danger"
    -
      group: "system"
      name: "Info"
      paletteId: "palette.info"
      role: "info"
      shades:
        -
          hex: "#DEE4EC"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#3B82F6"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#0449BA"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#001D4C"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "info"
    -
      group: "system"
      name: "Success"
      paletteId: "palette.success"
      role: "success"
      shades:
        -
          hex: "#DCFCE7"
          isOverridden: false
          label: "50"
          shadeId: "50"
        -
          hex: "#86EFAC"
          isOverridden: false
          label: "100"
          shadeId: "100"
        -
          hex: "#22C55E"
          isOverridden: false
          label: "200"
          shadeId: "200"
        -
          hex: "#166534"
          isOverridden: false
          label: "300"
          shadeId: "300"
      slug: "success"
    -
      group: "system"
      name: "Black & White"
      paletteId: "palette.black-and-white"
      role: "system"
      shades:
        -
          hex: "#000000"
          isOverridden: false
          label: "black"
          shadeId: "black"
        -
          hex: "#FFFFFF"
          isOverridden: false
          label: "white"
          shadeId: "white"
        -
          hex: "#00000000"
          isOverridden: false
          label: "transparent"
          shadeId: "transparent"
      slug: "black-and-white"
```

## Resolution Algorithm

1. Prefer semantic-tokens.md for UI intent decisions.
2. When a primitive shade is explicitly requested, resolve mode, paletteId, and shadeId in palettesByMode.
3. Use the hex value in palettesByMode as the active package value.
4. Do not synthesize missing hex values or interpolate new shade ids.

## Rules

- Use palette values through semantic tokens unless a component contract explicitly asks for a primitive shade.
- Preserve shade labels and exact active hex values.
- Do not invent, adjust, darken, lighten, or rename hex values.
- Generated package data contains active palette values with user overrides already materialized.
