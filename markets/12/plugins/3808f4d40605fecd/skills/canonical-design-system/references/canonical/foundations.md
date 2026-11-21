# Foundations

This file carries the package foundation layer: modes, semantic color variables, text styles, and resolved number tokens by mode. Other AI Ready files resolve through this foundation layer before rendering or exporting.

## Canonical Foundation Data

```yaml
modes:
  -
    isDefault: true
    modeId: "light"
    name: "Light"
  -
    modeId: "dark"
    name: "Dark"
numberTokensByMode:
  dark:
    -
      boundTokenRef: "size.0"
      category: "semantics.border.weight"
      defaultValue: 0
      isOverridden: false
      targetTokenRef: "size.0"
      tokenRef: "border.width.0"
      unit: "px"
      value: 0
    -
      boundTokenRef: "size.1"
      category: "semantics.border.weight"
      defaultValue: 1
      isOverridden: false
      targetTokenRef: "size.1"
      tokenRef: "border.width.1"
      unit: "px"
      value: 1
    -
      boundTokenRef: "size.1.5"
      category: "semantics.border.weight"
      defaultValue: 1.5
      isOverridden: false
      targetTokenRef: "size.1.5"
      tokenRef: "border.width.1.5"
      unit: "px"
      value: 1.5
    -
      boundTokenRef: "size.2"
      category: "semantics.border.weight"
      defaultValue: 2
      isOverridden: false
      targetTokenRef: "size.2"
      tokenRef: "border.width.2"
      unit: "px"
      value: 2
    -
      boundTokenRef: "size.4"
      category: "semantics.border.weight"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "border.width.4"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.0.5"
      category: "semantics.border.weight"
      defaultValue: 0.5
      isOverridden: false
      targetTokenRef: "size.0.5"
      tokenRef: "border.width.hairline"
      unit: "px"
      value: 0.5
    -
      boundTokenRef: "size.16"
      category: "semantics.icon.gap"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "icon.gap.lg"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.12"
      category: "semantics.icon.gap"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "icon.gap.md"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.8"
      category: "semantics.icon.gap"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "icon.gap.sm"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.20"
      category: "semantics.icon.gap"
      defaultValue: 20
      isOverridden: false
      targetTokenRef: "size.20"
      tokenRef: "icon.gap.xl"
      unit: "px"
      value: 20
    -
      boundTokenRef: "size.4"
      category: "semantics.icon.gap"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "icon.gap.xs"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.24"
      category: "semantics.icon.gap"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "icon.gap.xxl"
      unit: "px"
      value: 24
    -
      boundTokenRef: "size.12"
      category: "semantics.icon.size"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "icon.size.12"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.128"
      category: "semantics.icon.size"
      defaultValue: 128
      isOverridden: false
      targetTokenRef: "size.128"
      tokenRef: "icon.size.128"
      unit: "px"
      value: 128
    -
      boundTokenRef: "size.16"
      category: "semantics.icon.size"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "icon.size.16"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.20"
      category: "semantics.icon.size"
      defaultValue: 20
      isOverridden: false
      targetTokenRef: "size.20"
      tokenRef: "icon.size.20"
      unit: "px"
      value: 20
    -
      boundTokenRef: "size.24"
      category: "semantics.icon.size"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "icon.size.24"
      unit: "px"
      value: 24
    -
      boundTokenRef: "size.32"
      category: "semantics.icon.size"
      defaultValue: 32
      isOverridden: false
      targetTokenRef: "size.32"
      tokenRef: "icon.size.32"
      unit: "px"
      value: 32
    -
      boundTokenRef: "size.48"
      category: "semantics.icon.size"
      defaultValue: 48
      isOverridden: false
      targetTokenRef: "size.48"
      tokenRef: "icon.size.48"
      unit: "px"
      value: 48
    -
      boundTokenRef: "size.56"
      category: "semantics.icon.size"
      defaultValue: 56
      isOverridden: false
      targetTokenRef: "size.56"
      tokenRef: "icon.size.56"
      unit: "px"
      value: 56
    -
      boundTokenRef: "size.64"
      category: "semantics.icon.size"
      defaultValue: 64
      isOverridden: false
      targetTokenRef: "size.64"
      tokenRef: "icon.size.64"
      unit: "px"
      value: 64
    -
      boundTokenRef: "size.8"
      category: "semantics.icon.size"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "icon.size.8"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.9999"
      category: "semantics.border.radius"
      defaultValue: 9999
      isOverridden: false
      targetTokenRef: "size.9999"
      tokenRef: "radius.full"
      unit: "px"
      value: 9999
    -
      boundTokenRef: "size.12"
      category: "semantics.border.radius"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "radius.large"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.8"
      category: "semantics.border.radius"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "radius.medium"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.0"
      category: "semantics.border.radius"
      defaultValue: 0
      isOverridden: false
      targetTokenRef: "size.0"
      tokenRef: "radius.none"
      unit: "px"
      value: 0
    -
      boundTokenRef: "size.4"
      category: "semantics.border.radius"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "radius.small"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.12"
      category: "semantics.border.radius"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "radius.tile"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.16"
      category: "semantics.border.radius"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "radius.xlarge"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.2"
      category: "semantics.border.radius"
      defaultValue: 2
      isOverridden: false
      targetTokenRef: "size.2"
      tokenRef: "radius.xsmall"
      unit: "px"
      value: 2
    -
      boundTokenRef: "size.24"
      category: "semantics.border.radius"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "radius.xxlarge"
      unit: "px"
      value: 24
    -
      category: "foundation.size"
      defaultValue: 0
      isOverridden: false
      tokenRef: "size.0"
      unit: "px"
      value: 0
    -
      category: "foundation.size"
      defaultValue: 0.5
      isOverridden: false
      tokenRef: "size.0.5"
      unit: "px"
      value: 0.5
    -
      category: "foundation.size"
      defaultValue: 1
      isOverridden: false
      tokenRef: "size.1"
      unit: "px"
      value: 1
    -
      category: "foundation.size"
      defaultValue: 1.5
      isOverridden: false
      tokenRef: "size.1.5"
      unit: "px"
      value: 1.5
    -
      category: "foundation.size"
      defaultValue: 100
      isOverridden: false
      tokenRef: "size.100"
      unit: "px"
      value: 100
    -
      category: "foundation.size"
      defaultValue: 1020
      isOverridden: false
      tokenRef: "size.1020"
      unit: "px"
      value: 1020
    -
      category: "foundation.size"
      defaultValue: 104
      isOverridden: false
      tokenRef: "size.104"
      unit: "px"
      value: 104
    -
      category: "foundation.size"
      defaultValue: 108
      isOverridden: false
      tokenRef: "size.108"
      unit: "px"
      value: 108
    -
      category: "foundation.size"
      defaultValue: 112
      isOverridden: false
      tokenRef: "size.112"
      unit: "px"
      value: 112
    -
      category: "foundation.size"
      defaultValue: 116
      isOverridden: false
      tokenRef: "size.116"
      unit: "px"
      value: 116
    -
      category: "foundation.size"
      defaultValue: 12
      isOverridden: false
      tokenRef: "size.12"
      unit: "px"
      value: 12
    -
      category: "foundation.size"
      defaultValue: 120
      isOverridden: false
      tokenRef: "size.120"
      unit: "px"
      value: 120
    -
      category: "foundation.size"
      defaultValue: 124
      isOverridden: false
      tokenRef: "size.124"
      unit: "px"
      value: 124
    -
      category: "foundation.size"
      defaultValue: 128
      isOverridden: false
      tokenRef: "size.128"
      unit: "px"
      value: 128
    -
      category: "foundation.size"
      defaultValue: 16
      isOverridden: false
      tokenRef: "size.16"
      unit: "px"
      value: 16
    -
      category: "foundation.size"
      defaultValue: 192
      isOverridden: false
      tokenRef: "size.192"
      unit: "px"
      value: 192
    -
      category: "foundation.size"
      defaultValue: 2
      isOverridden: false
      tokenRef: "size.2"
      unit: "px"
      value: 2
    -
      category: "foundation.size"
      defaultValue: 20
      isOverridden: false
      tokenRef: "size.20"
      unit: "px"
      value: 20
    -
      category: "foundation.size"
      defaultValue: 200
      isOverridden: false
      tokenRef: "size.200"
      unit: "px"
      value: 200
    -
      category: "foundation.size"
      defaultValue: 24
      isOverridden: false
      tokenRef: "size.24"
      unit: "px"
      value: 24
    -
      category: "foundation.size"
      defaultValue: 28
      isOverridden: false
      tokenRef: "size.28"
      unit: "px"
      value: 28
    -
      category: "foundation.size"
      defaultValue: 32
      isOverridden: false
      tokenRef: "size.32"
      unit: "px"
      value: 32
    -
      category: "foundation.size"
      defaultValue: 36
      isOverridden: false
      tokenRef: "size.36"
      unit: "px"
      value: 36
    -
      category: "foundation.size"
      defaultValue: 4
      isOverridden: false
      tokenRef: "size.4"
      unit: "px"
      value: 4
    -
      category: "foundation.size"
      defaultValue: 40
      isOverridden: false
      tokenRef: "size.40"
      unit: "px"
      value: 40
    -
      category: "foundation.size"
      defaultValue: 44
      isOverridden: false
      tokenRef: "size.44"
      unit: "px"
      value: 44
    -
      category: "foundation.size"
      defaultValue: 48
      isOverridden: false
      tokenRef: "size.48"
      unit: "px"
      value: 48
    -
      category: "foundation.size"
      defaultValue: 52
      isOverridden: false
      tokenRef: "size.52"
      unit: "px"
      value: 52
    -
      category: "foundation.size"
      defaultValue: 56
      isOverridden: false
      tokenRef: "size.56"
      unit: "px"
      value: 56
    -
      category: "foundation.size"
      defaultValue: 60
      isOverridden: false
      tokenRef: "size.60"
      unit: "px"
      value: 60
    -
      category: "foundation.size"
      defaultValue: 64
      isOverridden: false
      tokenRef: "size.64"
      unit: "px"
      value: 64
    -
      category: "foundation.size"
      defaultValue: 68
      isOverridden: false
      tokenRef: "size.68"
      unit: "px"
      value: 68
    -
      category: "foundation.size"
      defaultValue: 72
      isOverridden: false
      tokenRef: "size.72"
      unit: "px"
      value: 72
    -
      category: "foundation.size"
      defaultValue: 750
      isOverridden: false
      tokenRef: "size.750"
      unit: "px"
      value: 750
    -
      category: "foundation.size"
      defaultValue: 76
      isOverridden: false
      tokenRef: "size.76"
      unit: "px"
      value: 76
    -
      category: "foundation.size"
      defaultValue: 8
      isOverridden: false
      tokenRef: "size.8"
      unit: "px"
      value: 8
    -
      category: "foundation.size"
      defaultValue: 80
      isOverridden: false
      tokenRef: "size.80"
      unit: "px"
      value: 80
    -
      category: "foundation.size"
      defaultValue: 84
      isOverridden: false
      tokenRef: "size.84"
      unit: "px"
      value: 84
    -
      category: "foundation.size"
      defaultValue: 88
      isOverridden: false
      tokenRef: "size.88"
      unit: "px"
      value: 88
    -
      category: "foundation.size"
      defaultValue: 92
      isOverridden: false
      tokenRef: "size.92"
      unit: "px"
      value: 92
    -
      category: "foundation.size"
      defaultValue: 96
      isOverridden: false
      tokenRef: "size.96"
      unit: "px"
      value: 96
    -
      category: "foundation.size"
      defaultValue: 9999
      isOverridden: false
      tokenRef: "size.9999"
      unit: "px"
      value: 9999
    -
      boundTokenRef: "size.0"
      category: "semantics.spacing"
      defaultValue: 0
      isOverridden: false
      targetTokenRef: "size.0"
      tokenRef: "space.0"
      unit: "px"
      value: 0
    -
      boundTokenRef: "size.1"
      category: "semantics.spacing"
      defaultValue: 1
      isOverridden: false
      targetTokenRef: "size.1"
      tokenRef: "space.1"
      unit: "px"
      value: 1
    -
      boundTokenRef: "size.100"
      category: "semantics.spacing"
      defaultValue: 100
      isOverridden: false
      targetTokenRef: "size.100"
      tokenRef: "space.100"
      unit: "px"
      value: 100
    -
      boundTokenRef: "size.104"
      category: "semantics.spacing"
      defaultValue: 104
      isOverridden: false
      targetTokenRef: "size.104"
      tokenRef: "space.104"
      unit: "px"
      value: 104
    -
      boundTokenRef: "size.108"
      category: "semantics.spacing"
      defaultValue: 108
      isOverridden: false
      targetTokenRef: "size.108"
      tokenRef: "space.108"
      unit: "px"
      value: 108
    -
      boundTokenRef: "size.112"
      category: "semantics.spacing"
      defaultValue: 112
      isOverridden: false
      targetTokenRef: "size.112"
      tokenRef: "space.112"
      unit: "px"
      value: 112
    -
      boundTokenRef: "size.116"
      category: "semantics.spacing"
      defaultValue: 116
      isOverridden: false
      targetTokenRef: "size.116"
      tokenRef: "space.116"
      unit: "px"
      value: 116
    -
      boundTokenRef: "size.12"
      category: "semantics.spacing"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "space.12"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.120"
      category: "semantics.spacing"
      defaultValue: 120
      isOverridden: false
      targetTokenRef: "size.120"
      tokenRef: "space.120"
      unit: "px"
      value: 120
    -
      boundTokenRef: "size.124"
      category: "semantics.spacing"
      defaultValue: 124
      isOverridden: false
      targetTokenRef: "size.124"
      tokenRef: "space.124"
      unit: "px"
      value: 124
    -
      boundTokenRef: "size.128"
      category: "semantics.spacing"
      defaultValue: 128
      isOverridden: false
      targetTokenRef: "size.128"
      tokenRef: "space.128"
      unit: "px"
      value: 128
    -
      boundTokenRef: "size.16"
      category: "semantics.spacing"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "space.16"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.192"
      category: "semantics.spacing"
      defaultValue: 192
      isOverridden: false
      targetTokenRef: "size.192"
      tokenRef: "space.192"
      unit: "px"
      value: 192
    -
      boundTokenRef: "size.2"
      category: "semantics.spacing"
      defaultValue: 2
      isOverridden: false
      targetTokenRef: "size.2"
      tokenRef: "space.2"
      unit: "px"
      value: 2
    -
      boundTokenRef: "size.20"
      category: "semantics.spacing"
      defaultValue: 20
      isOverridden: false
      targetTokenRef: "size.20"
      tokenRef: "space.20"
      unit: "px"
      value: 20
    -
      boundTokenRef: "size.24"
      category: "semantics.spacing"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "space.24"
      unit: "px"
      value: 24
    -
      boundTokenRef: "size.28"
      category: "semantics.spacing"
      defaultValue: 28
      isOverridden: false
      targetTokenRef: "size.28"
      tokenRef: "space.28"
      unit: "px"
      value: 28
    -
      boundTokenRef: "size.32"
      category: "semantics.spacing"
      defaultValue: 32
      isOverridden: false
      targetTokenRef: "size.32"
      tokenRef: "space.32"
      unit: "px"
      value: 32
    -
      boundTokenRef: "size.36"
      category: "semantics.spacing"
      defaultValue: 36
      isOverridden: false
      targetTokenRef: "size.36"
      tokenRef: "space.36"
      unit: "px"
      value: 36
    -
      boundTokenRef: "size.4"
      category: "semantics.spacing"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "space.4"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.40"
      category: "semantics.spacing"
      defaultValue: 40
      isOverridden: false
      targetTokenRef: "size.40"
      tokenRef: "space.40"
      unit: "px"
      value: 40
    -
      boundTokenRef: "size.48"
      category: "semantics.spacing"
      defaultValue: 48
      isOverridden: false
      targetTokenRef: "size.48"
      tokenRef: "space.48"
      unit: "px"
      value: 48
    -
      boundTokenRef: "size.52"
      category: "semantics.spacing"
      defaultValue: 52
      isOverridden: false
      targetTokenRef: "size.52"
      tokenRef: "space.52"
      unit: "px"
      value: 52
    -
      boundTokenRef: "size.56"
      category: "semantics.spacing"
      defaultValue: 56
      isOverridden: false
      targetTokenRef: "size.56"
      tokenRef: "space.56"
      unit: "px"
      value: 56
    -
      boundTokenRef: "size.60"
      category: "semantics.spacing"
      defaultValue: 60
      isOverridden: false
      targetTokenRef: "size.60"
      tokenRef: "space.60"
      unit: "px"
      value: 60
    -
      boundTokenRef: "size.64"
      category: "semantics.spacing"
      defaultValue: 64
      isOverridden: false
      targetTokenRef: "size.64"
      tokenRef: "space.64"
      unit: "px"
      value: 64
    -
      boundTokenRef: "size.68"
      category: "semantics.spacing"
      defaultValue: 68
      isOverridden: false
      targetTokenRef: "size.68"
      tokenRef: "space.68"
      unit: "px"
      value: 68
    -
      boundTokenRef: "size.72"
      category: "semantics.spacing"
      defaultValue: 72
      isOverridden: false
      targetTokenRef: "size.72"
      tokenRef: "space.72"
      unit: "px"
      value: 72
    -
      boundTokenRef: "size.76"
      category: "semantics.spacing"
      defaultValue: 76
      isOverridden: false
      targetTokenRef: "size.76"
      tokenRef: "space.76"
      unit: "px"
      value: 76
    -
      boundTokenRef: "size.8"
      category: "semantics.spacing"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "space.8"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.80"
      category: "semantics.spacing"
      defaultValue: 80
      isOverridden: false
      targetTokenRef: "size.80"
      tokenRef: "space.80"
      unit: "px"
      value: 80
    -
      boundTokenRef: "size.84"
      category: "semantics.spacing"
      defaultValue: 84
      isOverridden: false
      targetTokenRef: "size.84"
      tokenRef: "space.84"
      unit: "px"
      value: 84
    -
      boundTokenRef: "size.88"
      category: "semantics.spacing"
      defaultValue: 88
      isOverridden: false
      targetTokenRef: "size.88"
      tokenRef: "space.88"
      unit: "px"
      value: 88
    -
      boundTokenRef: "size.92"
      category: "semantics.spacing"
      defaultValue: 92
      isOverridden: false
      targetTokenRef: "size.92"
      tokenRef: "space.92"
      unit: "px"
      value: 92
    -
      boundTokenRef: "size.96"
      category: "semantics.spacing"
      defaultValue: 96
      isOverridden: false
      targetTokenRef: "size.96"
      tokenRef: "space.96"
      unit: "px"
      value: 96
  light:
    -
      boundTokenRef: "size.0"
      category: "semantics.border.weight"
      defaultValue: 0
      isOverridden: false
      targetTokenRef: "size.0"
      tokenRef: "border.width.0"
      unit: "px"
      value: 0
    -
      boundTokenRef: "size.1"
      category: "semantics.border.weight"
      defaultValue: 1
      isOverridden: false
      targetTokenRef: "size.1"
      tokenRef: "border.width.1"
      unit: "px"
      value: 1
    -
      boundTokenRef: "size.1.5"
      category: "semantics.border.weight"
      defaultValue: 1.5
      isOverridden: false
      targetTokenRef: "size.1.5"
      tokenRef: "border.width.1.5"
      unit: "px"
      value: 1.5
    -
      boundTokenRef: "size.2"
      category: "semantics.border.weight"
      defaultValue: 2
      isOverridden: false
      targetTokenRef: "size.2"
      tokenRef: "border.width.2"
      unit: "px"
      value: 2
    -
      boundTokenRef: "size.4"
      category: "semantics.border.weight"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "border.width.4"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.0.5"
      category: "semantics.border.weight"
      defaultValue: 0.5
      isOverridden: false
      targetTokenRef: "size.0.5"
      tokenRef: "border.width.hairline"
      unit: "px"
      value: 0.5
    -
      boundTokenRef: "size.16"
      category: "semantics.icon.gap"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "icon.gap.lg"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.12"
      category: "semantics.icon.gap"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "icon.gap.md"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.8"
      category: "semantics.icon.gap"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "icon.gap.sm"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.20"
      category: "semantics.icon.gap"
      defaultValue: 20
      isOverridden: false
      targetTokenRef: "size.20"
      tokenRef: "icon.gap.xl"
      unit: "px"
      value: 20
    -
      boundTokenRef: "size.4"
      category: "semantics.icon.gap"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "icon.gap.xs"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.24"
      category: "semantics.icon.gap"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "icon.gap.xxl"
      unit: "px"
      value: 24
    -
      boundTokenRef: "size.12"
      category: "semantics.icon.size"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "icon.size.12"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.128"
      category: "semantics.icon.size"
      defaultValue: 128
      isOverridden: false
      targetTokenRef: "size.128"
      tokenRef: "icon.size.128"
      unit: "px"
      value: 128
    -
      boundTokenRef: "size.16"
      category: "semantics.icon.size"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "icon.size.16"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.20"
      category: "semantics.icon.size"
      defaultValue: 20
      isOverridden: false
      targetTokenRef: "size.20"
      tokenRef: "icon.size.20"
      unit: "px"
      value: 20
    -
      boundTokenRef: "size.24"
      category: "semantics.icon.size"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "icon.size.24"
      unit: "px"
      value: 24
    -
      boundTokenRef: "size.32"
      category: "semantics.icon.size"
      defaultValue: 32
      isOverridden: false
      targetTokenRef: "size.32"
      tokenRef: "icon.size.32"
      unit: "px"
      value: 32
    -
      boundTokenRef: "size.48"
      category: "semantics.icon.size"
      defaultValue: 48
      isOverridden: false
      targetTokenRef: "size.48"
      tokenRef: "icon.size.48"
      unit: "px"
      value: 48
    -
      boundTokenRef: "size.56"
      category: "semantics.icon.size"
      defaultValue: 56
      isOverridden: false
      targetTokenRef: "size.56"
      tokenRef: "icon.size.56"
      unit: "px"
      value: 56
    -
      boundTokenRef: "size.64"
      category: "semantics.icon.size"
      defaultValue: 64
      isOverridden: false
      targetTokenRef: "size.64"
      tokenRef: "icon.size.64"
      unit: "px"
      value: 64
    -
      boundTokenRef: "size.8"
      category: "semantics.icon.size"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "icon.size.8"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.9999"
      category: "semantics.border.radius"
      defaultValue: 9999
      isOverridden: false
      targetTokenRef: "size.9999"
      tokenRef: "radius.full"
      unit: "px"
      value: 9999
    -
      boundTokenRef: "size.12"
      category: "semantics.border.radius"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "radius.large"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.8"
      category: "semantics.border.radius"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "radius.medium"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.0"
      category: "semantics.border.radius"
      defaultValue: 0
      isOverridden: false
      targetTokenRef: "size.0"
      tokenRef: "radius.none"
      unit: "px"
      value: 0
    -
      boundTokenRef: "size.4"
      category: "semantics.border.radius"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "radius.small"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.12"
      category: "semantics.border.radius"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "radius.tile"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.16"
      category: "semantics.border.radius"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "radius.xlarge"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.2"
      category: "semantics.border.radius"
      defaultValue: 2
      isOverridden: false
      targetTokenRef: "size.2"
      tokenRef: "radius.xsmall"
      unit: "px"
      value: 2
    -
      boundTokenRef: "size.24"
      category: "semantics.border.radius"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "radius.xxlarge"
      unit: "px"
      value: 24
    -
      category: "foundation.size"
      defaultValue: 0
      isOverridden: false
      tokenRef: "size.0"
      unit: "px"
      value: 0
    -
      category: "foundation.size"
      defaultValue: 0.5
      isOverridden: false
      tokenRef: "size.0.5"
      unit: "px"
      value: 0.5
    -
      category: "foundation.size"
      defaultValue: 1
      isOverridden: false
      tokenRef: "size.1"
      unit: "px"
      value: 1
    -
      category: "foundation.size"
      defaultValue: 1.5
      isOverridden: false
      tokenRef: "size.1.5"
      unit: "px"
      value: 1.5
    -
      category: "foundation.size"
      defaultValue: 100
      isOverridden: false
      tokenRef: "size.100"
      unit: "px"
      value: 100
    -
      category: "foundation.size"
      defaultValue: 1020
      isOverridden: false
      tokenRef: "size.1020"
      unit: "px"
      value: 1020
    -
      category: "foundation.size"
      defaultValue: 104
      isOverridden: false
      tokenRef: "size.104"
      unit: "px"
      value: 104
    -
      category: "foundation.size"
      defaultValue: 108
      isOverridden: false
      tokenRef: "size.108"
      unit: "px"
      value: 108
    -
      category: "foundation.size"
      defaultValue: 112
      isOverridden: false
      tokenRef: "size.112"
      unit: "px"
      value: 112
    -
      category: "foundation.size"
      defaultValue: 116
      isOverridden: false
      tokenRef: "size.116"
      unit: "px"
      value: 116
    -
      category: "foundation.size"
      defaultValue: 12
      isOverridden: false
      tokenRef: "size.12"
      unit: "px"
      value: 12
    -
      category: "foundation.size"
      defaultValue: 120
      isOverridden: false
      tokenRef: "size.120"
      unit: "px"
      value: 120
    -
      category: "foundation.size"
      defaultValue: 124
      isOverridden: false
      tokenRef: "size.124"
      unit: "px"
      value: 124
    -
      category: "foundation.size"
      defaultValue: 128
      isOverridden: false
      tokenRef: "size.128"
      unit: "px"
      value: 128
    -
      category: "foundation.size"
      defaultValue: 16
      isOverridden: false
      tokenRef: "size.16"
      unit: "px"
      value: 16
    -
      category: "foundation.size"
      defaultValue: 192
      isOverridden: false
      tokenRef: "size.192"
      unit: "px"
      value: 192
    -
      category: "foundation.size"
      defaultValue: 2
      isOverridden: false
      tokenRef: "size.2"
      unit: "px"
      value: 2
    -
      category: "foundation.size"
      defaultValue: 20
      isOverridden: false
      tokenRef: "size.20"
      unit: "px"
      value: 20
    -
      category: "foundation.size"
      defaultValue: 200
      isOverridden: false
      tokenRef: "size.200"
      unit: "px"
      value: 200
    -
      category: "foundation.size"
      defaultValue: 24
      isOverridden: false
      tokenRef: "size.24"
      unit: "px"
      value: 24
    -
      category: "foundation.size"
      defaultValue: 28
      isOverridden: false
      tokenRef: "size.28"
      unit: "px"
      value: 28
    -
      category: "foundation.size"
      defaultValue: 32
      isOverridden: false
      tokenRef: "size.32"
      unit: "px"
      value: 32
    -
      category: "foundation.size"
      defaultValue: 36
      isOverridden: false
      tokenRef: "size.36"
      unit: "px"
      value: 36
    -
      category: "foundation.size"
      defaultValue: 4
      isOverridden: false
      tokenRef: "size.4"
      unit: "px"
      value: 4
    -
      category: "foundation.size"
      defaultValue: 40
      isOverridden: false
      tokenRef: "size.40"
      unit: "px"
      value: 40
    -
      category: "foundation.size"
      defaultValue: 44
      isOverridden: false
      tokenRef: "size.44"
      unit: "px"
      value: 44
    -
      category: "foundation.size"
      defaultValue: 48
      isOverridden: false
      tokenRef: "size.48"
      unit: "px"
      value: 48
    -
      category: "foundation.size"
      defaultValue: 52
      isOverridden: false
      tokenRef: "size.52"
      unit: "px"
      value: 52
    -
      category: "foundation.size"
      defaultValue: 56
      isOverridden: false
      tokenRef: "size.56"
      unit: "px"
      value: 56
    -
      category: "foundation.size"
      defaultValue: 60
      isOverridden: false
      tokenRef: "size.60"
      unit: "px"
      value: 60
    -
      category: "foundation.size"
      defaultValue: 64
      isOverridden: false
      tokenRef: "size.64"
      unit: "px"
      value: 64
    -
      category: "foundation.size"
      defaultValue: 68
      isOverridden: false
      tokenRef: "size.68"
      unit: "px"
      value: 68
    -
      category: "foundation.size"
      defaultValue: 72
      isOverridden: false
      tokenRef: "size.72"
      unit: "px"
      value: 72
    -
      category: "foundation.size"
      defaultValue: 750
      isOverridden: false
      tokenRef: "size.750"
      unit: "px"
      value: 750
    -
      category: "foundation.size"
      defaultValue: 76
      isOverridden: false
      tokenRef: "size.76"
      unit: "px"
      value: 76
    -
      category: "foundation.size"
      defaultValue: 8
      isOverridden: false
      tokenRef: "size.8"
      unit: "px"
      value: 8
    -
      category: "foundation.size"
      defaultValue: 80
      isOverridden: false
      tokenRef: "size.80"
      unit: "px"
      value: 80
    -
      category: "foundation.size"
      defaultValue: 84
      isOverridden: false
      tokenRef: "size.84"
      unit: "px"
      value: 84
    -
      category: "foundation.size"
      defaultValue: 88
      isOverridden: false
      tokenRef: "size.88"
      unit: "px"
      value: 88
    -
      category: "foundation.size"
      defaultValue: 92
      isOverridden: false
      tokenRef: "size.92"
      unit: "px"
      value: 92
    -
      category: "foundation.size"
      defaultValue: 96
      isOverridden: false
      tokenRef: "size.96"
      unit: "px"
      value: 96
    -
      category: "foundation.size"
      defaultValue: 9999
      isOverridden: false
      tokenRef: "size.9999"
      unit: "px"
      value: 9999
    -
      boundTokenRef: "size.0"
      category: "semantics.spacing"
      defaultValue: 0
      isOverridden: false
      targetTokenRef: "size.0"
      tokenRef: "space.0"
      unit: "px"
      value: 0
    -
      boundTokenRef: "size.1"
      category: "semantics.spacing"
      defaultValue: 1
      isOverridden: false
      targetTokenRef: "size.1"
      tokenRef: "space.1"
      unit: "px"
      value: 1
    -
      boundTokenRef: "size.100"
      category: "semantics.spacing"
      defaultValue: 100
      isOverridden: false
      targetTokenRef: "size.100"
      tokenRef: "space.100"
      unit: "px"
      value: 100
    -
      boundTokenRef: "size.104"
      category: "semantics.spacing"
      defaultValue: 104
      isOverridden: false
      targetTokenRef: "size.104"
      tokenRef: "space.104"
      unit: "px"
      value: 104
    -
      boundTokenRef: "size.108"
      category: "semantics.spacing"
      defaultValue: 108
      isOverridden: false
      targetTokenRef: "size.108"
      tokenRef: "space.108"
      unit: "px"
      value: 108
    -
      boundTokenRef: "size.112"
      category: "semantics.spacing"
      defaultValue: 112
      isOverridden: false
      targetTokenRef: "size.112"
      tokenRef: "space.112"
      unit: "px"
      value: 112
    -
      boundTokenRef: "size.116"
      category: "semantics.spacing"
      defaultValue: 116
      isOverridden: false
      targetTokenRef: "size.116"
      tokenRef: "space.116"
      unit: "px"
      value: 116
    -
      boundTokenRef: "size.12"
      category: "semantics.spacing"
      defaultValue: 12
      isOverridden: false
      targetTokenRef: "size.12"
      tokenRef: "space.12"
      unit: "px"
      value: 12
    -
      boundTokenRef: "size.120"
      category: "semantics.spacing"
      defaultValue: 120
      isOverridden: false
      targetTokenRef: "size.120"
      tokenRef: "space.120"
      unit: "px"
      value: 120
    -
      boundTokenRef: "size.124"
      category: "semantics.spacing"
      defaultValue: 124
      isOverridden: false
      targetTokenRef: "size.124"
      tokenRef: "space.124"
      unit: "px"
      value: 124
    -
      boundTokenRef: "size.128"
      category: "semantics.spacing"
      defaultValue: 128
      isOverridden: false
      targetTokenRef: "size.128"
      tokenRef: "space.128"
      unit: "px"
      value: 128
    -
      boundTokenRef: "size.16"
      category: "semantics.spacing"
      defaultValue: 16
      isOverridden: false
      targetTokenRef: "size.16"
      tokenRef: "space.16"
      unit: "px"
      value: 16
    -
      boundTokenRef: "size.192"
      category: "semantics.spacing"
      defaultValue: 192
      isOverridden: false
      targetTokenRef: "size.192"
      tokenRef: "space.192"
      unit: "px"
      value: 192
    -
      boundTokenRef: "size.2"
      category: "semantics.spacing"
      defaultValue: 2
      isOverridden: false
      targetTokenRef: "size.2"
      tokenRef: "space.2"
      unit: "px"
      value: 2
    -
      boundTokenRef: "size.20"
      category: "semantics.spacing"
      defaultValue: 20
      isOverridden: false
      targetTokenRef: "size.20"
      tokenRef: "space.20"
      unit: "px"
      value: 20
    -
      boundTokenRef: "size.24"
      category: "semantics.spacing"
      defaultValue: 24
      isOverridden: false
      targetTokenRef: "size.24"
      tokenRef: "space.24"
      unit: "px"
      value: 24
    -
      boundTokenRef: "size.28"
      category: "semantics.spacing"
      defaultValue: 28
      isOverridden: false
      targetTokenRef: "size.28"
      tokenRef: "space.28"
      unit: "px"
      value: 28
    -
      boundTokenRef: "size.32"
      category: "semantics.spacing"
      defaultValue: 32
      isOverridden: false
      targetTokenRef: "size.32"
      tokenRef: "space.32"
      unit: "px"
      value: 32
    -
      boundTokenRef: "size.36"
      category: "semantics.spacing"
      defaultValue: 36
      isOverridden: false
      targetTokenRef: "size.36"
      tokenRef: "space.36"
      unit: "px"
      value: 36
    -
      boundTokenRef: "size.4"
      category: "semantics.spacing"
      defaultValue: 4
      isOverridden: false
      targetTokenRef: "size.4"
      tokenRef: "space.4"
      unit: "px"
      value: 4
    -
      boundTokenRef: "size.40"
      category: "semantics.spacing"
      defaultValue: 40
      isOverridden: false
      targetTokenRef: "size.40"
      tokenRef: "space.40"
      unit: "px"
      value: 40
    -
      boundTokenRef: "size.48"
      category: "semantics.spacing"
      defaultValue: 48
      isOverridden: false
      targetTokenRef: "size.48"
      tokenRef: "space.48"
      unit: "px"
      value: 48
    -
      boundTokenRef: "size.52"
      category: "semantics.spacing"
      defaultValue: 52
      isOverridden: false
      targetTokenRef: "size.52"
      tokenRef: "space.52"
      unit: "px"
      value: 52
    -
      boundTokenRef: "size.56"
      category: "semantics.spacing"
      defaultValue: 56
      isOverridden: false
      targetTokenRef: "size.56"
      tokenRef: "space.56"
      unit: "px"
      value: 56
    -
      boundTokenRef: "size.60"
      category: "semantics.spacing"
      defaultValue: 60
      isOverridden: false
      targetTokenRef: "size.60"
      tokenRef: "space.60"
      unit: "px"
      value: 60
    -
      boundTokenRef: "size.64"
      category: "semantics.spacing"
      defaultValue: 64
      isOverridden: false
      targetTokenRef: "size.64"
      tokenRef: "space.64"
      unit: "px"
      value: 64
    -
      boundTokenRef: "size.68"
      category: "semantics.spacing"
      defaultValue: 68
      isOverridden: false
      targetTokenRef: "size.68"
      tokenRef: "space.68"
      unit: "px"
      value: 68
    -
      boundTokenRef: "size.72"
      category: "semantics.spacing"
      defaultValue: 72
      isOverridden: false
      targetTokenRef: "size.72"
      tokenRef: "space.72"
      unit: "px"
      value: 72
    -
      boundTokenRef: "size.76"
      category: "semantics.spacing"
      defaultValue: 76
      isOverridden: false
      targetTokenRef: "size.76"
      tokenRef: "space.76"
      unit: "px"
      value: 76
    -
      boundTokenRef: "size.8"
      category: "semantics.spacing"
      defaultValue: 8
      isOverridden: false
      targetTokenRef: "size.8"
      tokenRef: "space.8"
      unit: "px"
      value: 8
    -
      boundTokenRef: "size.80"
      category: "semantics.spacing"
      defaultValue: 80
      isOverridden: false
      targetTokenRef: "size.80"
      tokenRef: "space.80"
      unit: "px"
      value: 80
    -
      boundTokenRef: "size.84"
      category: "semantics.spacing"
      defaultValue: 84
      isOverridden: false
      targetTokenRef: "size.84"
      tokenRef: "space.84"
      unit: "px"
      value: 84
    -
      boundTokenRef: "size.88"
      category: "semantics.spacing"
      defaultValue: 88
      isOverridden: false
      targetTokenRef: "size.88"
      tokenRef: "space.88"
      unit: "px"
      value: 88
    -
      boundTokenRef: "size.92"
      category: "semantics.spacing"
      defaultValue: 92
      isOverridden: false
      targetTokenRef: "size.92"
      tokenRef: "space.92"
      unit: "px"
      value: 92
    -
      boundTokenRef: "size.96"
      category: "semantics.spacing"
      defaultValue: 96
      isOverridden: false
      targetTokenRef: "size.96"
      tokenRef: "space.96"
      unit: "px"
      value: 96
textStyles:
  -
    category: "foundation.typography.body"
    fontFamily: "Inter"
    fontSize: 10
    fontWeight: 400
    letterSpacing: 0
    lineHeight: 16
    name: "Type/XS"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.xs"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.xs"
    tokenRef: "font.body.xsmall"
  -
    category: "foundation.typography.body"
    fontFamily: "Inter"
    fontSize: 12
    fontWeight: 400
    letterSpacing: 0
    lineHeight: 20
    name: "Type/SM"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.sm"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.sm"
    tokenRef: "font.body.small"
  -
    category: "foundation.typography.body"
    fontFamily: "Inter"
    fontSize: 14
    fontWeight: 400
    letterSpacing: 0
    lineHeight: 20
    name: "Type/MD"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.md"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.md"
    tokenRef: "font.body.medium"
  -
    category: "foundation.typography.body"
    fontFamily: "Inter"
    fontSize: 16
    fontWeight: 400
    letterSpacing: 0
    lineHeight: 24
    name: "Type/Base"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.base"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.base"
    tokenRef: "font.body"
  -
    category: "foundation.typography.body"
    fontFamily: "Inter"
    fontSize: 19
    fontWeight: 600
    letterSpacing: 0
    lineHeight: 28
    name: "Type/LG"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.lg"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.lg"
    tokenRef: "font.body.large"
  -
    category: "foundation.typography.header"
    fontFamily: "Inter"
    fontSize: 23
    fontWeight: 500
    letterSpacing: -0.02
    lineHeight: 28
    name: "Type/XL"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.xl"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.xl"
    tokenRef: "font.heading.xsmall"
  -
    category: "foundation.typography.header"
    fontFamily: "Inter"
    fontSize: 28
    fontWeight: 500
    letterSpacing: -0.02
    lineHeight: 32
    name: "Type/2XL"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.2xl"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.2xl"
    tokenRef: "font.heading.small"
  -
    category: "foundation.typography.header"
    fontFamily: "Inter"
    fontSize: 33
    fontWeight: 700
    letterSpacing: -0.02
    lineHeight: 40
    name: "Type/3XL"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.3xl"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.3xl"
    tokenRef: "font.heading.medium"
  -
    category: "foundation.typography.header"
    fontFamily: "Inter"
    fontSize: 40
    fontWeight: 700
    letterSpacing: -0.02
    lineHeight: 48
    name: "Type/4XL"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.4xl"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.4xl"
    tokenRef: "font.heading.large"
  -
    category: "foundation.typography.header"
    fontFamily: "Inter"
    fontSize: 48
    fontWeight: 700
    letterSpacing: -0.02
    lineHeight: 56
    name: "Type/5XL"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.5xl"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.5xl"
    tokenRef: "font.heading.xlarge"
  -
    category: "foundation.typography.header"
    fontFamily: "Inter"
    fontSize: 57
    fontWeight: 700
    letterSpacing: -0.02
    lineHeight: 68
    name: "Type/6XL"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "type.6xl"
      alpyResourceType: "text-style"
      alpyRevision: 0
    styleId: "type.6xl"
    tokenRef: "font.heading.xxlarge"
variables:
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.50"
    type: "color"
    valuesByMode:
      dark: "#D5DCE8"
      light: "#D5DCE8"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.100"
    type: "color"
    valuesByMode:
      dark: "#B7C5E1"
      light: "#B7C5E1"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.200"
    type: "color"
    valuesByMode:
      dark: "#92AEE0"
      light: "#92AEE0"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.300"
    type: "color"
    valuesByMode:
      dark: "#6C95E5"
      light: "#6C95E5"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/400"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.400"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.400"
    type: "color"
    valuesByMode:
      dark: "#4079EE"
      light: "#4079EE"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/500"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.500"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.500"
    type: "color"
    valuesByMode:
      dark: "#0A4FDF"
      light: "#0A4FDF"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/600"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.600"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.600"
    type: "color"
    valuesByMode:
      dark: "#134CC8"
      light: "#134CC8"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/700"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.700"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.700"
    type: "color"
    valuesByMode:
      dark: "#0B3A9D"
      light: "#0B3A9D"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/800"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.800"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.800"
    type: "color"
    valuesByMode:
      dark: "#062770"
      light: "#062770"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/primary/900"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.primary.900"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.primary.900"
    type: "color"
    valuesByMode:
      dark: "#031643"
      light: "#031643"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.50"
    type: "color"
    valuesByMode:
      dark: "#E6EDE5"
      light: "#E6EDE5"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.100"
    type: "color"
    valuesByMode:
      dark: "#C7DAC8"
      light: "#C7DAC8"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.200"
    type: "color"
    valuesByMode:
      dark: "#A6C6A5"
      light: "#A6C6A5"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.300"
    type: "color"
    valuesByMode:
      dark: "#7FB581"
      light: "#7FB581"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/400"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.400"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.400"
    type: "color"
    valuesByMode:
      dark: "#52A457"
      light: "#52A457"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/500"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.500"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.500"
    type: "color"
    valuesByMode:
      dark: "#058625"
      light: "#058625"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/600"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.600"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.600"
    type: "color"
    valuesByMode:
      dark: "#197C2A"
      light: "#197C2A"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/700"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.700"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.700"
    type: "color"
    valuesByMode:
      dark: "#156221"
      light: "#156221"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/800"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.800"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.800"
    type: "color"
    valuesByMode:
      dark: "#0F4817"
      light: "#0F4817"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/secondary/900"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.secondary.900"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.secondary.900"
    type: "color"
    valuesByMode:
      dark: "#0D2E10"
      light: "#0D2E10"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.50"
    type: "color"
    valuesByMode:
      dark: "#E8E2D5"
      light: "#E8E2D5"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.100"
    type: "color"
    valuesByMode:
      dark: "#E2D3B5"
      light: "#E2D3B5"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.200"
    type: "color"
    valuesByMode:
      dark: "#E1C590"
      light: "#E1C590"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.300"
    type: "color"
    valuesByMode:
      dark: "#E5BA65"
      light: "#E5BA65"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/400"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.400"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.400"
    type: "color"
    valuesByMode:
      dark: "#EFB035"
      light: "#EFB035"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/500"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.500"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.500"
    type: "color"
    valuesByMode:
      dark: "#FCA701"
      light: "#FCA701"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/600"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.600"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.600"
    type: "color"
    valuesByMode:
      dark: "#CD8801"
      light: "#CD8801"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/700"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.700"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.700"
    type: "color"
    valuesByMode:
      dark: "#9E6800"
      light: "#9E6800"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/800"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.800"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.800"
    type: "color"
    valuesByMode:
      dark: "#6F4900"
      light: "#6F4900"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/tertiary/900"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.tertiary.900"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.tertiary.900"
    type: "color"
    valuesByMode:
      dark: "#3F2A00"
      light: "#3F2A00"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.50"
    type: "color"
    valuesByMode:
      dark: "#F1F1F1"
      light: "#F1F1F1"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.100"
    type: "color"
    valuesByMode:
      dark: "#CECECE"
      light: "#CECECE"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.200"
    type: "color"
    valuesByMode:
      dark: "#A1A1A1"
      light: "#A1A1A1"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.300"
    type: "color"
    valuesByMode:
      dark: "#767676"
      light: "#767676"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/400"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.400"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.400"
    type: "color"
    valuesByMode:
      dark: "#5C5C5C"
      light: "#5C5C5C"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/500"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.500"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.500"
    type: "color"
    valuesByMode:
      dark: "#333333"
      light: "#333333"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/600"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.600"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.600"
    type: "color"
    valuesByMode:
      dark: "#2E2E2E"
      light: "#2E2E2E"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/700"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.700"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.700"
    type: "color"
    valuesByMode:
      dark: "#242424"
      light: "#242424"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/800"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.800"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.800"
    type: "color"
    valuesByMode:
      dark: "#1C1C1C"
      light: "#1C1C1C"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/neutral/900"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.neutral.900"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.neutral.900"
    type: "color"
    valuesByMode:
      dark: "#151515"
      light: "#151515"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/warning/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.warning.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.warning.50"
    type: "color"
    valuesByMode:
      dark: "#E8E2D6"
      light: "#E8E2D6"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/warning/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.warning.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.warning.100"
    type: "color"
    valuesByMode:
      dark: "#FFBD4F"
      light: "#FFBD4F"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/warning/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.warning.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.warning.200"
    type: "color"
    valuesByMode:
      dark: "#AE6D00"
      light: "#AE6D00"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/warning/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.warning.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.warning.300"
    type: "color"
    valuesByMode:
      dark: "#402800"
      light: "#402800"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/danger/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.danger.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.danger.50"
    type: "color"
    valuesByMode:
      dark: "#ECDFDF"
      light: "#ECDFDF"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/danger/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.danger.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.danger.100"
    type: "color"
    valuesByMode:
      dark: "#EF4444"
      light: "#EF4444"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/danger/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.danger.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.danger.200"
    type: "color"
    valuesByMode:
      dark: "#B80808"
      light: "#B80808"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/danger/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.danger.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.danger.300"
    type: "color"
    valuesByMode:
      dark: "#4D0000"
      light: "#4D0000"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/info/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.info.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.info.50"
    type: "color"
    valuesByMode:
      dark: "#DEE4EC"
      light: "#DEE4EC"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/info/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.info.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.info.100"
    type: "color"
    valuesByMode:
      dark: "#3B82F6"
      light: "#3B82F6"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/info/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.info.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.info.200"
    type: "color"
    valuesByMode:
      dark: "#0449BA"
      light: "#0449BA"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/info/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.info.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.info.300"
    type: "color"
    valuesByMode:
      dark: "#001D4C"
      light: "#001D4C"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/success/50"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.success.50"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.success.50"
    type: "color"
    valuesByMode:
      dark: "#DCFCE7"
      light: "#DCFCE7"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/success/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.success.100"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.success.100"
    type: "color"
    valuesByMode:
      dark: "#86EFAC"
      light: "#86EFAC"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/success/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.success.200"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.success.200"
    type: "color"
    valuesByMode:
      dark: "#22C55E"
      light: "#22C55E"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/success/300"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.success.300"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.success.300"
    type: "color"
    valuesByMode:
      dark: "#166534"
      light: "#166534"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/black-and-white/black"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.black-and-white.black"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.black-and-white.black"
    type: "color"
    valuesByMode:
      dark: "#000000"
      light: "#000000"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/black-and-white/white"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.black-and-white.white"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.black-and-white.white"
    type: "color"
    valuesByMode:
      dark: "#FFFFFF"
      light: "#FFFFFF"
  -
    category: "foundation.color.palette"
    collectionName: "Foundations"
    kind: "value"
    name: "foundation/color/palette/black-and-white/transparent"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "foundation.color.palette.black-and-white.transparent"
      alpyResourceType: "palette-shade"
      alpyRevision: 0
    tokenId: "foundation.color.palette.black-and-white.transparent"
    type: "color"
    valuesByMode:
      dark: "#00000000"
      light: "#00000000"
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/0"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.0"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.0"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/0.5"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.0.5"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.0.5"
    type: "number"
    valuesByMode:
      dark: 0.5
      light: 0.5
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/1"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.1"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.1"
    type: "number"
    valuesByMode:
      dark: 1
      light: 1
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/1.5"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.1.5"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.1.5"
    type: "number"
    valuesByMode:
      dark: 1.5
      light: 1.5
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.100"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.100"
    type: "number"
    valuesByMode:
      dark: 100
      light: 100
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/1020"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.1020"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.1020"
    type: "number"
    valuesByMode:
      dark: 1020
      light: 1020
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/104"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.104"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.104"
    type: "number"
    valuesByMode:
      dark: 104
      light: 104
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/108"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.108"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.108"
    type: "number"
    valuesByMode:
      dark: 108
      light: 108
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/112"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.112"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.112"
    type: "number"
    valuesByMode:
      dark: 112
      light: 112
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/116"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.116"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.116"
    type: "number"
    valuesByMode:
      dark: 116
      light: 116
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/12"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.12"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.12"
    type: "number"
    valuesByMode:
      dark: 12
      light: 12
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/120"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.120"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.120"
    type: "number"
    valuesByMode:
      dark: 120
      light: 120
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/124"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.124"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.124"
    type: "number"
    valuesByMode:
      dark: 124
      light: 124
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/128"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.128"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.128"
    type: "number"
    valuesByMode:
      dark: 128
      light: 128
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/16"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.16"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.16"
    type: "number"
    valuesByMode:
      dark: 16
      light: 16
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/192"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.192"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.192"
    type: "number"
    valuesByMode:
      dark: 192
      light: 192
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/2"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.2"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.2"
    type: "number"
    valuesByMode:
      dark: 2
      light: 2
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/20"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.20"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.20"
    type: "number"
    valuesByMode:
      dark: 20
      light: 20
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/200"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.200"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.200"
    type: "number"
    valuesByMode:
      dark: 200
      light: 200
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/24"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.24"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.24"
    type: "number"
    valuesByMode:
      dark: 24
      light: 24
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/28"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.28"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.28"
    type: "number"
    valuesByMode:
      dark: 28
      light: 28
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/32"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.32"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.32"
    type: "number"
    valuesByMode:
      dark: 32
      light: 32
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/36"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.36"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.36"
    type: "number"
    valuesByMode:
      dark: 36
      light: 36
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/4"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.4"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.4"
    type: "number"
    valuesByMode:
      dark: 4
      light: 4
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/40"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.40"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.40"
    type: "number"
    valuesByMode:
      dark: 40
      light: 40
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/44"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.44"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.44"
    type: "number"
    valuesByMode:
      dark: 44
      light: 44
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/48"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.48"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.48"
    type: "number"
    valuesByMode:
      dark: 48
      light: 48
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/52"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.52"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.52"
    type: "number"
    valuesByMode:
      dark: 52
      light: 52
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/56"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.56"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.56"
    type: "number"
    valuesByMode:
      dark: 56
      light: 56
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/60"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.60"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.60"
    type: "number"
    valuesByMode:
      dark: 60
      light: 60
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/64"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.64"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.64"
    type: "number"
    valuesByMode:
      dark: 64
      light: 64
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/68"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.68"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.68"
    type: "number"
    valuesByMode:
      dark: 68
      light: 68
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/72"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.72"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.72"
    type: "number"
    valuesByMode:
      dark: 72
      light: 72
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/750"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.750"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.750"
    type: "number"
    valuesByMode:
      dark: 750
      light: 750
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/76"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.76"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.76"
    type: "number"
    valuesByMode:
      dark: 76
      light: 76
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/8"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.8"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.8"
    type: "number"
    valuesByMode:
      dark: 8
      light: 8
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/80"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.80"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.80"
    type: "number"
    valuesByMode:
      dark: 80
      light: 80
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/84"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.84"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.84"
    type: "number"
    valuesByMode:
      dark: 84
      light: 84
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/88"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.88"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.88"
    type: "number"
    valuesByMode:
      dark: 88
      light: 88
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/92"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.92"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.92"
    type: "number"
    valuesByMode:
      dark: 92
      light: 92
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/96"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.96"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.96"
    type: "number"
    valuesByMode:
      dark: 96
      light: 96
  -
    category: "foundation.size"
    collectionName: "Foundations"
    kind: "value"
    name: "size/9999"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "size.9999"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "size.9999"
    type: "number"
    valuesByMode:
      dark: 9999
      light: 9999
  -
    aliasByMode:
      dark: "size.0"
      light: "size.0"
    category: "semantics.border.weight"
    collectionName: "Themes"
    kind: "alias"
    name: "border/width/0"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "border.width.0"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "border.width.0"
    type: "number"
  -
    aliasByMode:
      dark: "size.1"
      light: "size.1"
    category: "semantics.border.weight"
    collectionName: "Themes"
    kind: "alias"
    name: "border/width/1"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "border.width.1"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "border.width.1"
    type: "number"
  -
    aliasByMode:
      dark: "size.1.5"
      light: "size.1.5"
    category: "semantics.border.weight"
    collectionName: "Themes"
    kind: "alias"
    name: "border/width/1.5"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "border.width.1.5"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "border.width.1.5"
    type: "number"
  -
    aliasByMode:
      dark: "size.2"
      light: "size.2"
    category: "semantics.border.weight"
    collectionName: "Themes"
    kind: "alias"
    name: "border/width/2"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "border.width.2"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "border.width.2"
    type: "number"
  -
    aliasByMode:
      dark: "size.4"
      light: "size.4"
    category: "semantics.border.weight"
    collectionName: "Themes"
    kind: "alias"
    name: "border/width/4"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "border.width.4"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "border.width.4"
    type: "number"
  -
    aliasByMode:
      dark: "size.0.5"
      light: "size.0.5"
    category: "semantics.border.weight"
    collectionName: "Themes"
    kind: "alias"
    name: "border/width/hairline"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "border.width.hairline"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "border.width.hairline"
    type: "number"
  -
    aliasByMode:
      dark: "size.16"
      light: "size.16"
    category: "semantics.icon.gap"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/gap/lg"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.gap.lg"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.gap.lg"
    type: "number"
  -
    aliasByMode:
      dark: "size.12"
      light: "size.12"
    category: "semantics.icon.gap"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/gap/md"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.gap.md"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.gap.md"
    type: "number"
  -
    aliasByMode:
      dark: "size.8"
      light: "size.8"
    category: "semantics.icon.gap"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/gap/sm"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.gap.sm"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.gap.sm"
    type: "number"
  -
    aliasByMode:
      dark: "size.20"
      light: "size.20"
    category: "semantics.icon.gap"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/gap/xl"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.gap.xl"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.gap.xl"
    type: "number"
  -
    aliasByMode:
      dark: "size.4"
      light: "size.4"
    category: "semantics.icon.gap"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/gap/xs"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.gap.xs"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.gap.xs"
    type: "number"
  -
    aliasByMode:
      dark: "size.24"
      light: "size.24"
    category: "semantics.icon.gap"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/gap/xxl"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.gap.xxl"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.gap.xxl"
    type: "number"
  -
    aliasByMode:
      dark: "size.12"
      light: "size.12"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/12"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.12"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.12"
    type: "number"
  -
    aliasByMode:
      dark: "size.128"
      light: "size.128"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/128"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.128"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.128"
    type: "number"
  -
    aliasByMode:
      dark: "size.16"
      light: "size.16"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/16"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.16"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.16"
    type: "number"
  -
    aliasByMode:
      dark: "size.20"
      light: "size.20"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/20"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.20"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.20"
    type: "number"
  -
    aliasByMode:
      dark: "size.24"
      light: "size.24"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/24"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.24"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.24"
    type: "number"
  -
    aliasByMode:
      dark: "size.32"
      light: "size.32"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/32"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.32"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.32"
    type: "number"
  -
    aliasByMode:
      dark: "size.48"
      light: "size.48"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/48"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.48"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.48"
    type: "number"
  -
    aliasByMode:
      dark: "size.56"
      light: "size.56"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/56"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.56"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.56"
    type: "number"
  -
    aliasByMode:
      dark: "size.64"
      light: "size.64"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/64"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.64"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.64"
    type: "number"
  -
    aliasByMode:
      dark: "size.8"
      light: "size.8"
    category: "semantics.icon.size"
    collectionName: "Themes"
    kind: "alias"
    name: "icon/size/8"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "icon.size.8"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "icon.size.8"
    type: "number"
  -
    aliasByMode:
      dark: "size.9999"
      light: "size.9999"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/full"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.full"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.full"
    type: "number"
  -
    aliasByMode:
      dark: "size.12"
      light: "size.12"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/large"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.large"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.large"
    type: "number"
  -
    aliasByMode:
      dark: "size.8"
      light: "size.8"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/medium"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.medium"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.medium"
    type: "number"
  -
    aliasByMode:
      dark: "size.0"
      light: "size.0"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/none"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.none"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.none"
    type: "number"
  -
    aliasByMode:
      dark: "size.4"
      light: "size.4"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/small"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.small"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.small"
    type: "number"
  -
    aliasByMode:
      dark: "size.12"
      light: "size.12"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/tile"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.tile"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.tile"
    type: "number"
  -
    aliasByMode:
      dark: "size.16"
      light: "size.16"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/xlarge"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.xlarge"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.xlarge"
    type: "number"
  -
    aliasByMode:
      dark: "size.2"
      light: "size.2"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/xsmall"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.xsmall"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.xsmall"
    type: "number"
  -
    aliasByMode:
      dark: "size.24"
      light: "size.24"
    category: "semantics.border.radius"
    collectionName: "Themes"
    kind: "alias"
    name: "radius/xxlarge"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "radius.xxlarge"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "radius.xxlarge"
    type: "number"
  -
    aliasByMode:
      dark: "size.0"
      light: "size.0"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/0"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.0"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.0"
    type: "number"
  -
    aliasByMode:
      dark: "size.1"
      light: "size.1"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/1"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.1"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.1"
    type: "number"
  -
    aliasByMode:
      dark: "size.100"
      light: "size.100"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/100"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.100"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.100"
    type: "number"
  -
    aliasByMode:
      dark: "size.104"
      light: "size.104"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/104"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.104"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.104"
    type: "number"
  -
    aliasByMode:
      dark: "size.108"
      light: "size.108"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/108"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.108"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.108"
    type: "number"
  -
    aliasByMode:
      dark: "size.112"
      light: "size.112"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/112"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.112"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.112"
    type: "number"
  -
    aliasByMode:
      dark: "size.116"
      light: "size.116"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/116"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.116"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.116"
    type: "number"
  -
    aliasByMode:
      dark: "size.12"
      light: "size.12"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/12"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.12"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.12"
    type: "number"
  -
    aliasByMode:
      dark: "size.120"
      light: "size.120"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/120"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.120"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.120"
    type: "number"
  -
    aliasByMode:
      dark: "size.124"
      light: "size.124"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/124"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.124"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.124"
    type: "number"
  -
    aliasByMode:
      dark: "size.128"
      light: "size.128"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/128"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.128"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.128"
    type: "number"
  -
    aliasByMode:
      dark: "size.16"
      light: "size.16"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/16"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.16"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.16"
    type: "number"
  -
    aliasByMode:
      dark: "size.192"
      light: "size.192"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/192"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.192"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.192"
    type: "number"
  -
    aliasByMode:
      dark: "size.2"
      light: "size.2"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/2"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.2"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.2"
    type: "number"
  -
    aliasByMode:
      dark: "size.20"
      light: "size.20"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/20"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.20"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.20"
    type: "number"
  -
    aliasByMode:
      dark: "size.24"
      light: "size.24"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/24"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.24"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.24"
    type: "number"
  -
    aliasByMode:
      dark: "size.28"
      light: "size.28"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/28"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.28"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.28"
    type: "number"
  -
    aliasByMode:
      dark: "size.32"
      light: "size.32"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/32"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.32"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.32"
    type: "number"
  -
    aliasByMode:
      dark: "size.36"
      light: "size.36"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/36"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.36"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.36"
    type: "number"
  -
    aliasByMode:
      dark: "size.4"
      light: "size.4"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/4"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.4"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.4"
    type: "number"
  -
    aliasByMode:
      dark: "size.40"
      light: "size.40"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/40"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.40"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.40"
    type: "number"
  -
    aliasByMode:
      dark: "size.48"
      light: "size.48"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/48"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.48"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.48"
    type: "number"
  -
    aliasByMode:
      dark: "size.52"
      light: "size.52"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/52"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.52"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.52"
    type: "number"
  -
    aliasByMode:
      dark: "size.56"
      light: "size.56"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/56"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.56"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.56"
    type: "number"
  -
    aliasByMode:
      dark: "size.60"
      light: "size.60"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/60"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.60"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.60"
    type: "number"
  -
    aliasByMode:
      dark: "size.64"
      light: "size.64"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/64"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.64"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.64"
    type: "number"
  -
    aliasByMode:
      dark: "size.68"
      light: "size.68"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/68"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.68"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.68"
    type: "number"
  -
    aliasByMode:
      dark: "size.72"
      light: "size.72"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/72"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.72"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.72"
    type: "number"
  -
    aliasByMode:
      dark: "size.76"
      light: "size.76"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/76"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.76"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.76"
    type: "number"
  -
    aliasByMode:
      dark: "size.8"
      light: "size.8"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/8"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.8"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.8"
    type: "number"
  -
    aliasByMode:
      dark: "size.80"
      light: "size.80"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/80"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.80"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.80"
    type: "number"
  -
    aliasByMode:
      dark: "size.84"
      light: "size.84"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/84"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.84"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.84"
    type: "number"
  -
    aliasByMode:
      dark: "size.88"
      light: "size.88"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/88"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.88"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.88"
    type: "number"
  -
    aliasByMode:
      dark: "size.92"
      light: "size.92"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/92"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.92"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.92"
    type: "number"
  -
    aliasByMode:
      dark: "size.96"
      light: "size.96"
    category: "semantics.spacing"
    collectionName: "Themes"
    kind: "alias"
    name: "space/96"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "space.96"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "space.96"
    type: "number"
  -
    category: "foundation.typography.body"
    collectionName: "Foundations"
    kind: "value"
    name: "font/body/xsmall"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.body.xsmall"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.body.xsmall"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 10
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 16
      light:
        fontFamily: "Inter"
        fontSize: 10
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 16
  -
    category: "foundation.typography.body"
    collectionName: "Foundations"
    kind: "value"
    name: "font/body/small"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.body.small"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.body.small"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 12
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 20
      light:
        fontFamily: "Inter"
        fontSize: 12
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 20
  -
    category: "foundation.typography.body"
    collectionName: "Foundations"
    kind: "value"
    name: "font/body/medium"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.body.medium"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.body.medium"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 14
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 20
      light:
        fontFamily: "Inter"
        fontSize: 14
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 20
  -
    category: "foundation.typography.body"
    collectionName: "Foundations"
    kind: "value"
    name: "font/body"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.body"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.body"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 16
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 24
      light:
        fontFamily: "Inter"
        fontSize: 16
        fontWeight: 400
        letterSpacing: 0
        lineHeight: 24
  -
    category: "foundation.typography.body"
    collectionName: "Foundations"
    kind: "value"
    name: "font/body/large"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.body.large"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.body.large"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 19
        fontWeight: 600
        letterSpacing: 0
        lineHeight: 28
      light:
        fontFamily: "Inter"
        fontSize: 19
        fontWeight: 600
        letterSpacing: 0
        lineHeight: 28
  -
    category: "foundation.typography.header"
    collectionName: "Foundations"
    kind: "value"
    name: "font/heading/xsmall"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.heading.xsmall"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.heading.xsmall"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 23
        fontWeight: 500
        letterSpacing: -0.02
        lineHeight: 28
      light:
        fontFamily: "Inter"
        fontSize: 23
        fontWeight: 500
        letterSpacing: -0.02
        lineHeight: 28
  -
    category: "foundation.typography.header"
    collectionName: "Foundations"
    kind: "value"
    name: "font/heading/small"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.heading.small"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.heading.small"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 28
        fontWeight: 500
        letterSpacing: -0.02
        lineHeight: 32
      light:
        fontFamily: "Inter"
        fontSize: 28
        fontWeight: 500
        letterSpacing: -0.02
        lineHeight: 32
  -
    category: "foundation.typography.header"
    collectionName: "Foundations"
    kind: "value"
    name: "font/heading/medium"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.heading.medium"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.heading.medium"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 33
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 40
      light:
        fontFamily: "Inter"
        fontSize: 33
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 40
  -
    category: "foundation.typography.header"
    collectionName: "Foundations"
    kind: "value"
    name: "font/heading/large"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.heading.large"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.heading.large"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 40
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 48
      light:
        fontFamily: "Inter"
        fontSize: 40
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 48
  -
    category: "foundation.typography.header"
    collectionName: "Foundations"
    kind: "value"
    name: "font/heading/xlarge"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.heading.xlarge"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.heading.xlarge"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 48
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 56
      light:
        fontFamily: "Inter"
        fontSize: 48
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 56
  -
    category: "foundation.typography.header"
    collectionName: "Foundations"
    kind: "value"
    name: "font/heading/xxlarge"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "font.heading.xxlarge"
      alpyResourceType: "type-token"
      alpyRevision: 0
    tokenId: "font.heading.xxlarge"
    type: "typography"
    valuesByMode:
      dark:
        fontFamily: "Inter"
        fontSize: 57
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 68
      light:
        fontFamily: "Inter"
        fontSize: 57
        fontWeight: 700
        letterSpacing: -0.02
        lineHeight: 68
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.500"
      light: "foundation.color.palette.primary.500"
    category: "border"
    collectionName: "Themes"
    description: "Primary brand border color for focused outlines, selected controls, and branded emphasis strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-one/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-one.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-one.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.900"
    category: "border"
    collectionName: "Themes"
    description: "Highest-emphasis primary brand border color for maximum-strength branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-one/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-one.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-one.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.400"
      light: "foundation.color.palette.primary.700"
    category: "border"
    collectionName: "Themes"
    description: "Strong primary brand border color for high-emphasis branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-one/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-one.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-one.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.900"
      light: "foundation.color.palette.primary.50"
    category: "border"
    collectionName: "Themes"
    description: "Lowest-emphasis primary brand border color for soft branded outlines and quiet branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-one/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-one.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-one.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.700"
      light: "foundation.color.palette.primary.300"
    category: "border"
    collectionName: "Themes"
    description: "Medium-emphasis primary brand border color for visible branded outlines and supporting branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-one/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-one.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-one.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.800"
      light: "foundation.color.palette.primary.100"
    category: "border"
    collectionName: "Themes"
    description: "Low-emphasis primary brand border color for secondary branded outlines and muted branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-one/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-one.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-one.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.500"
      light: "foundation.color.palette.tertiary.500"
    category: "border"
    collectionName: "Themes"
    description: "Tertiary brand border color for selected controls, branded focus alternatives, and branded emphasis strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-three/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-three.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-three.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.300"
      light: "foundation.color.palette.tertiary.900"
    category: "border"
    collectionName: "Themes"
    description: "Highest-emphasis tertiary brand border color for maximum-strength branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-three/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-three.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-three.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.400"
      light: "foundation.color.palette.tertiary.700"
    category: "border"
    collectionName: "Themes"
    description: "Strong tertiary brand border color for high-emphasis branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-three/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-three.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-three.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.900"
      light: "foundation.color.palette.tertiary.50"
    category: "border"
    collectionName: "Themes"
    description: "Lowest-emphasis tertiary brand border color for soft branded outlines and quiet branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-three/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-three.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-three.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.700"
      light: "foundation.color.palette.tertiary.300"
    category: "border"
    collectionName: "Themes"
    description: "Medium-emphasis tertiary brand border color for visible branded outlines and supporting branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-three/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-three.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-three.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.800"
      light: "foundation.color.palette.tertiary.100"
    category: "border"
    collectionName: "Themes"
    description: "Low-emphasis tertiary brand border color for secondary branded outlines and muted branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    kind: "alias"
    name: "color/border/brand/color-three/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-three.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-three.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.500"
      light: "foundation.color.palette.secondary.500"
    category: "border"
    collectionName: "Themes"
    description: "Secondary brand border color for selected controls, branded focus alternatives, and branded emphasis strokes. Do not use for text, fills, icons, neutral borders, or functional feedback."
    kind: "alias"
    name: "color/border/brand/color-two/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-two.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-two.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.300"
      light: "foundation.color.palette.secondary.900"
    category: "border"
    collectionName: "Themes"
    description: "Highest-emphasis secondary brand border color for maximum-strength branded outlines, prominent branded strokes, and secondary pressed borders. Do not use for text, fills, icons, neutral borders, or functional feedback."
    kind: "alias"
    name: "color/border/brand/color-two/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-two.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-two.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.400"
      light: "foundation.color.palette.secondary.700"
    category: "border"
    collectionName: "Themes"
    description: "Strong secondary brand border color for high-emphasis branded outlines, prominent branded strokes, and secondary hover borders. Do not use for text, fills, icons, neutral borders, or functional feedback."
    kind: "alias"
    name: "color/border/brand/color-two/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-two.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-two.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.900"
      light: "foundation.color.palette.secondary.50"
    category: "border"
    collectionName: "Themes"
    description: "Lowest-emphasis secondary brand border color for soft branded outlines and quiet branded strokes. Do not use for text, fills, icons, neutral borders, or functional feedback."
    kind: "alias"
    name: "color/border/brand/color-two/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-two.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-two.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.700"
      light: "foundation.color.palette.secondary.300"
    category: "border"
    collectionName: "Themes"
    description: "Medium-emphasis secondary brand border color for visible branded outlines and supporting branded strokes. Do not use for text, fills, icons, neutral borders, or functional feedback."
    kind: "alias"
    name: "color/border/brand/color-two/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-two.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-two.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.800"
      light: "foundation.color.palette.secondary.100"
    category: "border"
    collectionName: "Themes"
    description: "Low-emphasis secondary brand border color for secondary branded outlines, muted branded strokes, and secondary disabled borders. Do not use for text, fills, icons, neutral borders, or functional feedback."
    kind: "alias"
    name: "color/border/brand/color-two/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.brand.color-two.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.brand.color-two.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.100"
      light: "foundation.color.palette.danger.200"
    category: "border"
    collectionName: "Themes"
    description: "Danger border color for error, destructive, and critical feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    kind: "alias"
    name: "color/border/functional/danger"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.functional.danger"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.functional.danger"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.100"
      light: "foundation.color.palette.info.200"
    category: "border"
    collectionName: "Themes"
    description: "Info border color for informational feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    kind: "alias"
    name: "color/border/functional/info"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.functional.info"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.functional.info"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.200"
      light: "foundation.color.palette.success.300"
    category: "border"
    collectionName: "Themes"
    description: "Success border color for completed, positive, and confirmed feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    kind: "alias"
    name: "color/border/functional/success"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.functional.success"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.functional.success"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.200"
      light: "foundation.color.palette.warning.200"
    category: "border"
    collectionName: "Themes"
    description: "Warning border color for caution, attention, and recoverable issue feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    kind: "alias"
    name: "color/border/functional/warning"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.functional.warning"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.functional.warning"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.300"
      light: "foundation.color.palette.neutral.300"
    category: "border"
    collectionName: "Themes"
    description: "Border color for input fields and form controls. Do not use for text, fills, icons, functional feedback, brand emphasis, or non-input containers."
    kind: "alias"
    name: "color/border/input"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.input"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.input"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.200"
      light: "foundation.color.palette.neutral.200"
    category: "border"
    collectionName: "Themes"
    description: "Border color for disabled interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    kind: "alias"
    name: "color/border/interaction/disabled"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.interaction.disabled"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.interaction.disabled"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.500"
      light: "foundation.color.palette.primary.500"
    category: "border"
    collectionName: "Themes"
    description: "Border color for focused interactive elements and focus outlines. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    kind: "alias"
    name: "color/border/interaction/focused"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.interaction.focused"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.interaction.focused"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.700"
    category: "border"
    collectionName: "Themes"
    description: "Border color for hovered interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    kind: "alias"
    name: "color/border/interaction/hover"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.interaction.hover"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.interaction.hover"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.900"
      light: "foundation.color.palette.primary.900"
    category: "border"
    collectionName: "Themes"
    description: "Border color for pressed interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    kind: "alias"
    name: "color/border/interaction/pressed"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.interaction.pressed"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.interaction.pressed"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.600"
    category: "border"
    collectionName: "Themes"
    description: "Border color for selected interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    kind: "alias"
    name: "color/border/interaction/selected"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.interaction.selected"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.interaction.selected"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.500"
      light: "foundation.color.palette.neutral.500"
    category: "border"
    collectionName: "Themes"
    description: "Primary neutral border color for visible outlines, separators, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    kind: "alias"
    name: "color/border/neutral/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.neutral.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.neutral.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.300"
      light: "foundation.color.palette.neutral.900"
    category: "border"
    collectionName: "Themes"
    description: "Highest-emphasis neutral border color for maximum-strength outlines, separators, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    kind: "alias"
    name: "color/border/neutral/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.neutral.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.neutral.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.400"
      light: "foundation.color.palette.neutral.700"
    category: "border"
    collectionName: "Themes"
    description: "Strong neutral border color for high-emphasis outlines, separators, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    kind: "alias"
    name: "color/border/neutral/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.neutral.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.neutral.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.900"
      light: "foundation.color.palette.neutral.50"
    category: "border"
    collectionName: "Themes"
    description: "Lowest-emphasis neutral border color for very quiet dividers, outlines, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    kind: "alias"
    name: "color/border/neutral/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.neutral.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.neutral.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.500"
      light: "foundation.color.palette.neutral.300"
    category: "border"
    collectionName: "Themes"
    description: "Medium-emphasis neutral border color for standard dividers, outlines, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    kind: "alias"
    name: "color/border/neutral/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.neutral.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.neutral.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.800"
      light: "foundation.color.palette.neutral.100"
    category: "border"
    collectionName: "Themes"
    description: "Low-emphasis neutral border color for quiet dividers, outlines, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    kind: "alias"
    name: "color/border/neutral/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.neutral.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.neutral.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.white"
      light: "foundation.color.palette.black-and-white.white"
    category: "border"
    collectionName: "Themes"
    description: "Border color for strokes on strong colored surfaces. Do not use for text, fills, icons, normal neutral borders, brand borders, or functional feedback."
    kind: "alias"
    name: "color/border/onColor"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.border.onColor"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.border.onColor"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.100"
      light: "foundation.color.palette.danger.200"
    category: "functional"
    collectionName: "Themes"
    description: "Danger color for error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/danger"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.danger"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.danger"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.200"
      light: "foundation.color.palette.danger.100"
    category: "functional"
    collectionName: "Themes"
    description: "Soft danger color for medium-emphasis error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/danger/soft"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.danger.soft"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.danger.soft"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.50"
      light: "foundation.color.palette.danger.300"
    category: "functional"
    collectionName: "Themes"
    description: "Strong danger color for high-emphasis error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/danger/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.danger.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.danger.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.300"
      light: "foundation.color.palette.danger.50"
    category: "functional"
    collectionName: "Themes"
    description: "Lowest-emphasis danger color for soft error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/danger/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.danger.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.danger.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.100"
      light: "foundation.color.palette.info.200"
    category: "functional"
    collectionName: "Themes"
    description: "Info color for informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/info"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.info"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.info"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.200"
      light: "foundation.color.palette.info.100"
    category: "functional"
    collectionName: "Themes"
    description: "Soft info color for medium-emphasis informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/info/soft"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.info.soft"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.info.soft"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.50"
      light: "foundation.color.palette.info.300"
    category: "functional"
    collectionName: "Themes"
    description: "Strong info color for high-emphasis informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/info/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.info.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.info.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.300"
      light: "foundation.color.palette.info.50"
    category: "functional"
    collectionName: "Themes"
    description: "Lowest-emphasis info color for soft informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/info/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.info.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.info.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.100"
      light: "foundation.color.palette.success.200"
    category: "functional"
    collectionName: "Themes"
    description: "Success color for completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/success"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.success"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.success"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.200"
      light: "foundation.color.palette.success.100"
    category: "functional"
    collectionName: "Themes"
    description: "Soft success color for medium-emphasis completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/success/soft"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.success.soft"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.success.soft"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.50"
      light: "foundation.color.palette.success.300"
    category: "functional"
    collectionName: "Themes"
    description: "Strong success color for high-emphasis completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/success/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.success.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.success.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.300"
      light: "foundation.color.palette.success.50"
    category: "functional"
    collectionName: "Themes"
    description: "Lowest-emphasis success color for soft completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/success/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.success.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.success.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.100"
      light: "foundation.color.palette.warning.200"
    category: "functional"
    collectionName: "Themes"
    description: "Warning color for caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/warning"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.warning"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.warning"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.200"
      light: "foundation.color.palette.warning.100"
    category: "functional"
    collectionName: "Themes"
    description: "Soft warning color for medium-emphasis caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/warning/soft"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.warning.soft"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.warning.soft"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.50"
      light: "foundation.color.palette.warning.300"
    category: "functional"
    collectionName: "Themes"
    description: "Strong warning color for high-emphasis caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/warning/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.warning.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.warning.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.300"
      light: "foundation.color.palette.warning.50"
    category: "functional"
    collectionName: "Themes"
    description: "Lowest-emphasis warning color for soft caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    kind: "alias"
    name: "color/functional/warning/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.functional.warning.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.functional.warning.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.500"
    category: "icon"
    collectionName: "Themes"
    description: "Accent icon color for emphasized neutral UI icons. Do not use for text, fills, borders, brand icons, functional status icons, or interaction states."
    kind: "alias"
    name: "color/icon/accent"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.accent"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.accent"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.500"
    category: "icon"
    collectionName: "Themes"
    description: "Default strong Color One brand icon color for primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-one/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-one.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-one.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.50"
      light: "foundation.color.palette.primary.900"
    category: "icon"
    collectionName: "Themes"
    description: "Highest-emphasis Color One brand icon color for primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-one/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-one.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-one.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.100"
      light: "foundation.color.palette.primary.700"
    category: "icon"
    collectionName: "Themes"
    description: "High-emphasis Color One brand icon color for primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-one/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-one.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-one.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.900"
      light: "foundation.color.palette.primary.50"
    category: "icon"
    collectionName: "Themes"
    description: "Lowest-emphasis Color One brand icon color for subtle primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-one/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-one.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-one.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.500"
      light: "foundation.color.palette.primary.300"
    category: "icon"
    collectionName: "Themes"
    description: "Medium-emphasis Color One brand icon color for subtle primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-one/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-one.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-one.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.700"
      light: "foundation.color.palette.primary.100"
    category: "icon"
    collectionName: "Themes"
    description: "Low-emphasis Color One brand icon color for subtle primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-one/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-one.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-one.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.300"
      light: "foundation.color.palette.tertiary.500"
    category: "icon"
    collectionName: "Themes"
    description: "Default strong Color Three brand icon color for tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-three/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-three.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-three.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.50"
      light: "foundation.color.palette.tertiary.900"
    category: "icon"
    collectionName: "Themes"
    description: "Highest-emphasis Color Three brand icon color for tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-three/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-three.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-three.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.100"
      light: "foundation.color.palette.tertiary.700"
    category: "icon"
    collectionName: "Themes"
    description: "High-emphasis Color Three brand icon color for tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-three/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-three.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-three.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.900"
      light: "foundation.color.palette.tertiary.50"
    category: "icon"
    collectionName: "Themes"
    description: "Lowest-emphasis Color Three brand icon color for subtle tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-three/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-three.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-three.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.500"
      light: "foundation.color.palette.tertiary.300"
    category: "icon"
    collectionName: "Themes"
    description: "Medium-emphasis Color Three brand icon color for subtle tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-three/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-three.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-three.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.700"
      light: "foundation.color.palette.tertiary.100"
    category: "icon"
    collectionName: "Themes"
    description: "Low-emphasis Color Three brand icon color for subtle tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-three/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-three.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-three.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.300"
      light: "foundation.color.palette.secondary.500"
    category: "icon"
    collectionName: "Themes"
    description: "Default strong Color Two brand icon color for secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-two/strong/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-two.strong.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-two.strong.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.50"
      light: "foundation.color.palette.secondary.900"
    category: "icon"
    collectionName: "Themes"
    description: "Highest-emphasis Color Two brand icon color for secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-two/strong/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-two.strong.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-two.strong.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.100"
      light: "foundation.color.palette.secondary.700"
    category: "icon"
    collectionName: "Themes"
    description: "High-emphasis Color Two brand icon color for secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-two/strong/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-two.strong.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-two.strong.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.900"
      light: "foundation.color.palette.secondary.50"
    category: "icon"
    collectionName: "Themes"
    description: "Lowest-emphasis Color Two brand icon color for subtle secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-two/subtle/one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-two.subtle.one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-two.subtle.one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.500"
      light: "foundation.color.palette.secondary.300"
    category: "icon"
    collectionName: "Themes"
    description: "Medium-emphasis Color Two brand icon color for subtle secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-two/subtle/three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-two.subtle.three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-two.subtle.three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.700"
      light: "foundation.color.palette.secondary.100"
    category: "icon"
    collectionName: "Themes"
    description: "Low-emphasis Color Two brand icon color for subtle secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    kind: "alias"
    name: "color/icon/brand/color-two/subtle/two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.brand.color-two.subtle.two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.brand.color-two.subtle.two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.200"
      light: "foundation.color.palette.danger.200"
    category: "icon"
    collectionName: "Themes"
    description: "Danger icon color for error, destructive, and critical status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    kind: "alias"
    name: "color/icon/danger"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.danger"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.danger"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.100"
      light: "foundation.color.palette.neutral.900"
    category: "icon"
    collectionName: "Themes"
    description: "Default icon color for standard UI icons. Do not use for text, fills, borders, brand accents, functional status icons, or interaction states."
    kind: "alias"
    name: "color/icon/default"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.default"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.default"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.200"
      light: "foundation.color.palette.neutral.200"
    category: "icon"
    collectionName: "Themes"
    description: "Gray disabled icon color for unavailable UI icons. Use only when a gray disabled icon is required. Do not use for text, fills, borders, enabled icons, brand-disabled icons, functional status icons, or interaction states."
    kind: "alias"
    name: "color/icon/disabled"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.disabled"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.disabled"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.200"
      light: "foundation.color.palette.info.200"
    category: "icon"
    collectionName: "Themes"
    description: "Info icon color for informational status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    kind: "alias"
    name: "color/icon/info"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.info"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.info"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.200"
      light: "foundation.color.palette.primary.200"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for disabled interaction state. Do not use for text, fills, borders, enabled icons, hover icons, pressed icons, selected icons, brand icons, or functional status icons."
    kind: "alias"
    name: "color/icon/interaction/disabled"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.interaction.disabled"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.interaction.disabled"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.500"
      light: "foundation.color.palette.primary.500"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for focused interaction state. Do not use for text, fills, borders, default icons, hover icons, pressed icons, selected icons, disabled icons, brand icons, or functional status icons."
    kind: "alias"
    name: "color/icon/interaction/focused"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.interaction.focused"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.interaction.focused"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.700"
      light: "foundation.color.palette.primary.700"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for hover interaction state. Do not use for text, fills, borders, default icons, pressed icons, selected icons, disabled icons, brand icons, or functional status icons."
    kind: "alias"
    name: "color/icon/interaction/hover"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.interaction.hover"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.interaction.hover"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.900"
      light: "foundation.color.palette.primary.900"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for pressed interaction state. Do not use for text, fills, borders, default icons, hover icons, selected icons, disabled icons, brand icons, or functional status icons."
    kind: "alias"
    name: "color/icon/interaction/pressed"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.interaction.pressed"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.interaction.pressed"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.600"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for selected interaction state. Do not use for text, fills, borders, default icons, hover icons, pressed icons, disabled icons, brand icons, or functional status icons."
    kind: "alias"
    name: "color/icon/interaction/selected"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.interaction.selected"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.interaction.selected"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.black"
      light: "foundation.color.palette.black-and-white.white"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for icons on inverse or dark neutral surfaces. Do not use for text, fills, borders, brand icons, functional status icons, or normal light surfaces."
    kind: "alias"
    name: "color/icon/inverse"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.inverse"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.inverse"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.white"
      light: "foundation.color.palette.black-and-white.white"
    category: "icon"
    collectionName: "Themes"
    description: "Icon color for icons, checkmarks, and dots on strong colored fills. Do not use for text, fills, borders, standalone brand icons, functional status icons, or normal neutral surfaces."
    kind: "alias"
    name: "color/icon/onColor"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.onColor"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.onColor"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.300"
      light: "foundation.color.palette.neutral.400"
    category: "icon"
    collectionName: "Themes"
    description: "Lower-emphasis icon color for secondary UI icons. Do not use for text, fills, borders, brand icons, functional status icons, or interaction states."
    kind: "alias"
    name: "color/icon/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.500"
      light: "foundation.color.palette.neutral.300"
    category: "icon"
    collectionName: "Themes"
    description: "Lowest-emphasis icon color for decorative or very low-emphasis UI icons. Do not use for text, fills, borders, brand icons, functional status icons, or interaction states."
    kind: "alias"
    name: "color/icon/subtlest"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.subtlest"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.subtlest"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.200"
      light: "foundation.color.palette.success.200"
    category: "icon"
    collectionName: "Themes"
    description: "Success icon color for positive, completed, and confirmed status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    kind: "alias"
    name: "color/icon/success"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.success"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.success"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.200"
      light: "foundation.color.palette.warning.200"
    category: "icon"
    collectionName: "Themes"
    description: "Warning icon color for caution, attention, and recoverable issue status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    kind: "alias"
    name: "color/icon/warning"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.icon.warning"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.icon.warning"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.500"
    category: "shades"
    collectionName: "Themes"
    description: "Primary brand emphasis shade for filled UI states, accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-one/strong-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-one.strong-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-one.strong-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.50"
      light: "foundation.color.palette.primary.900"
    category: "shades"
    collectionName: "Themes"
    description: "Highest-emphasis primary brand shade for maximum-strength fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-one/strong-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-one.strong-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-one.strong-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.100"
      light: "foundation.color.palette.primary.700"
    category: "shades"
    collectionName: "Themes"
    description: "Strong primary brand shade for high-contrast fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-one/strong-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-one.strong-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-one.strong-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.900"
      light: "foundation.color.palette.primary.50"
    category: "shades"
    collectionName: "Themes"
    description: "Lowest-emphasis primary brand shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-one/subtle-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-one.subtle-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-one.subtle-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.500"
      light: "foundation.color.palette.primary.300"
    category: "shades"
    collectionName: "Themes"
    description: "Medium-emphasis primary brand shade for visible fills, supporting accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-one/subtle-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-one.subtle-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-one.subtle-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.700"
      light: "foundation.color.palette.primary.100"
    category: "shades"
    collectionName: "Themes"
    description: "Low-emphasis primary brand shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-one/subtle-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-one.subtle-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-one.subtle-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.300"
      light: "foundation.color.palette.tertiary.500"
    category: "shades"
    collectionName: "Themes"
    description: "Tertiary brand emphasis shade for filled UI states, accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-three/strong-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-three.strong-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-three.strong-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.50"
      light: "foundation.color.palette.tertiary.900"
    category: "shades"
    collectionName: "Themes"
    description: "Highest-emphasis tertiary brand shade for maximum-strength fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-three/strong-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-three.strong-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-three.strong-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.100"
      light: "foundation.color.palette.tertiary.700"
    category: "shades"
    collectionName: "Themes"
    description: "Strong tertiary brand shade for high-contrast fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-three/strong-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-three.strong-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-three.strong-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.900"
      light: "foundation.color.palette.tertiary.50"
    category: "shades"
    collectionName: "Themes"
    description: "Lowest-emphasis tertiary brand shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-three/subtle-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-three.subtle-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-three.subtle-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.500"
      light: "foundation.color.palette.tertiary.300"
    category: "shades"
    collectionName: "Themes"
    description: "Medium-emphasis tertiary brand shade for visible fills, supporting accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-three/subtle-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-three.subtle-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-three.subtle-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.700"
      light: "foundation.color.palette.tertiary.100"
    category: "shades"
    collectionName: "Themes"
    description: "Low-emphasis tertiary brand shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-three/subtle-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-three.subtle-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-three.subtle-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.300"
      light: "foundation.color.palette.secondary.500"
    category: "shades"
    collectionName: "Themes"
    description: "Secondary brand emphasis shade for filled UI states, accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-two/strong-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-two.strong-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-two.strong-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.50"
      light: "foundation.color.palette.secondary.900"
    category: "shades"
    collectionName: "Themes"
    description: "Highest-emphasis secondary brand shade for maximum-strength fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-two/strong-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-two.strong-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-two.strong-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.100"
      light: "foundation.color.palette.secondary.700"
    category: "shades"
    collectionName: "Themes"
    description: "Strong secondary brand shade for high-contrast fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-two/strong-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-two.strong-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-two.strong-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.900"
      light: "foundation.color.palette.secondary.50"
    category: "shades"
    collectionName: "Themes"
    description: "Lowest-emphasis secondary brand shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-two/subtle-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-two.subtle-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-two.subtle-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.500"
      light: "foundation.color.palette.secondary.300"
    category: "shades"
    collectionName: "Themes"
    description: "Medium-emphasis secondary brand shade for visible fills, supporting accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-two/subtle-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-two.subtle-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-two.subtle-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.700"
      light: "foundation.color.palette.secondary.100"
    category: "shades"
    collectionName: "Themes"
    description: "Low-emphasis secondary brand shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/brand/color-two/subtle-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.brand.color-two.subtle-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.brand.color-two.subtle-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.300"
      light: "foundation.color.palette.neutral.500"
    category: "shades"
    collectionName: "Themes"
    description: "Primary neutral emphasis shade for filled UI states, neutral accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/neutral/strong-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.neutral.strong-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.neutral.strong-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.50"
      light: "foundation.color.palette.neutral.900"
    category: "shades"
    collectionName: "Themes"
    description: "Highest neutral emphasis shade for maximum-strength fills and neutral accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/neutral/strong-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.neutral.strong-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.neutral.strong-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.100"
      light: "foundation.color.palette.neutral.700"
    category: "shades"
    collectionName: "Themes"
    description: "Strong neutral emphasis shade for high-contrast fills and neutral accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/neutral/strong-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.neutral.strong-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.neutral.strong-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.900"
      light: "foundation.color.palette.neutral.50"
    category: "shades"
    collectionName: "Themes"
    description: "Lowest-emphasis neutral shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/neutral/subtle-one"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.neutral.subtle-one"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.neutral.subtle-one"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.500"
      light: "foundation.color.palette.neutral.300"
    category: "shades"
    collectionName: "Themes"
    description: "Medium-emphasis neutral shade for visible fills, separators-as-fill, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/neutral/subtle-three"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.neutral.subtle-three"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.neutral.subtle-three"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.700"
      light: "foundation.color.palette.neutral.100"
    category: "shades"
    collectionName: "Themes"
    description: "Low-emphasis neutral shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    kind: "alias"
    name: "color/shades/neutral/subtle-two"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shades.neutral.subtle-two"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shades.neutral.subtle-two"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.50"
      light: "foundation.color.palette.neutral.900"
    category: "shadow"
    collectionName: "Themes"
    description: "Deep shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    kind: "alias"
    name: "color/shadow/deep"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shadow.deep"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shadow.deep"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.200"
      light: "foundation.color.palette.neutral.400"
    category: "shadow"
    collectionName: "Themes"
    description: "Medium shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    kind: "alias"
    name: "color/shadow/medium"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shadow.medium"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shadow.medium"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.300"
      light: "foundation.color.palette.neutral.200"
    category: "shadow"
    collectionName: "Themes"
    description: "Soft shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    kind: "alias"
    name: "color/shadow/soft"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shadow.soft"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shadow.soft"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.100"
      light: "foundation.color.palette.black-and-white.black"
    category: "shadow"
    collectionName: "Themes"
    description: "Strong shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    kind: "alias"
    name: "color/shadow/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.shadow.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.shadow.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.black"
      light: "foundation.color.palette.black-and-white.white"
    category: "surface"
    collectionName: "Themes"
    description: "Default canvas and component surface color for containers. Do not use for text, borders, functional colors, icons, system colors, or interaction states."
    kind: "alias"
    name: "color/surface/canvas"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.surface.canvas"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.surface.canvas"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.900"
      light: "foundation.color.palette.neutral.50"
    category: "surface"
    collectionName: "Themes"
    description: "Surface color for disabled interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    kind: "alias"
    name: "color/surface/interaction/disabled"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.surface.interaction.disabled"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.surface.interaction.disabled"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.800"
      light: "foundation.color.palette.neutral.100"
    category: "surface"
    collectionName: "Themes"
    description: "Surface color for focused interactive areas when the focus state needs a surface treatment. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    kind: "alias"
    name: "color/surface/interaction/focused"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.surface.interaction.focused"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.surface.interaction.focused"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.800"
      light: "foundation.color.palette.neutral.100"
    category: "surface"
    collectionName: "Themes"
    description: "Surface color for hovered interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    kind: "alias"
    name: "color/surface/interaction/hover"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.surface.interaction.hover"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.surface.interaction.hover"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.900"
      light: "foundation.color.palette.primary.900"
    category: "surface"
    collectionName: "Themes"
    description: "Surface color for pressed interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    kind: "alias"
    name: "color/surface/interaction/pressed"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.surface.interaction.pressed"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.surface.interaction.pressed"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.700"
      light: "foundation.color.palette.neutral.200"
    category: "surface"
    collectionName: "Themes"
    description: "Surface color for selected interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    kind: "alias"
    name: "color/surface/interaction/selected"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.surface.interaction.selected"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.surface.interaction.selected"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.black"
      light: "foundation.color.palette.black-and-white.black"
    category: "system"
    collectionName: "Themes"
    description: "Absolute black utility color for system-level fallbacks and hard black requirements. Do not use for normal text, fills, borders, icons, brand colors, functional feedback, or interaction states."
    kind: "alias"
    name: "color/system/black"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.system.black"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.system.black"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.transparent"
      light: "foundation.color.palette.black-and-white.transparent"
    category: "system"
    collectionName: "Themes"
    description: "Transparent utility color for intentionally invisible fills, borders, or cleared backgrounds. Do not use for text, icons, brand colors, functional feedback, or interaction states."
    kind: "alias"
    name: "color/system/transparent"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.system.transparent"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.system.transparent"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.white"
      light: "foundation.color.palette.black-and-white.white"
    category: "system"
    collectionName: "Themes"
    description: "Absolute white utility color for system-level fallbacks, hard white requirements, and hard-white inverse surface requirements. Do not use for normal text, normal fills, borders, icons, brand colors, functional feedback, or non-inverse interaction states."
    kind: "alias"
    name: "color/system/white"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.system.white"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.system.white"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.200"
      light: "foundation.color.palette.neutral.700"
    category: "text"
    collectionName: "Themes"
    description: "Default text color for readable body copy, labels, and standard UI text. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    kind: "alias"
    name: "color/text/body"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.body"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.body"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.300"
      light: "foundation.color.palette.neutral.300"
    category: "text"
    collectionName: "Themes"
    description: "Muted text color for low-emphasis copy, helper text, placeholders, and disabled-adjacent text. Do not use for fills, borders, icons, links, functional feedback, brand accents, or primary readable text."
    kind: "alias"
    name: "color/text/body/muted"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.body.muted"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.body.muted"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.400"
      light: "foundation.color.palette.neutral.400"
    category: "text"
    collectionName: "Themes"
    description: "Lower-emphasis text color for supporting copy and secondary UI text. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    kind: "alias"
    name: "color/text/body/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.body.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.body.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.500"
    category: "text"
    collectionName: "Themes"
    description: "Default Color One brand text for branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-one/accent"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-one.accent"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-one.accent"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.200"
      light: "foundation.color.palette.primary.700"
    category: "text"
    collectionName: "Themes"
    description: "High-emphasis Color One brand text for strong branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-one/accent/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-one.accent.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-one.accent.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.400"
      light: "foundation.color.palette.primary.400"
    category: "text"
    collectionName: "Themes"
    description: "Low-emphasis Color One brand text for subtle branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-one/accent/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-one.accent.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-one.accent.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.300"
      light: "foundation.color.palette.tertiary.500"
    category: "text"
    collectionName: "Themes"
    description: "Default Color Three brand text for tertiary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-three/accent"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-three.accent"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-three.accent"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.200"
      light: "foundation.color.palette.tertiary.700"
    category: "text"
    collectionName: "Themes"
    description: "High-emphasis Color Three brand text for tertiary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-three/accent/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-three.accent.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-three.accent.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.tertiary.400"
      light: "foundation.color.palette.tertiary.400"
    category: "text"
    collectionName: "Themes"
    description: "Low-emphasis Color Three brand text for tertiary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-three/accent/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-three.accent.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-three.accent.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.300"
      light: "foundation.color.palette.secondary.500"
    category: "text"
    collectionName: "Themes"
    description: "Default Color Two brand text for secondary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-two/accent"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-two.accent"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-two.accent"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.200"
      light: "foundation.color.palette.secondary.700"
    category: "text"
    collectionName: "Themes"
    description: "High-emphasis Color Two brand text for secondary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-two/accent/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-two.accent.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-two.accent.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.400"
      light: "foundation.color.palette.secondary.400"
    category: "text"
    collectionName: "Themes"
    description: "Low-emphasis Color Two brand text for secondary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    kind: "alias"
    name: "color/text/brand/color-two/accent/subtle"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.brand.color-two.accent.subtle"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.brand.color-two.accent.subtle"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.200"
      light: "foundation.color.palette.danger.200"
    category: "text"
    collectionName: "Themes"
    description: "Danger text color for error, destructive, and critical status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/danger"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.danger"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.danger"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.danger.300"
      light: "foundation.color.palette.danger.300"
    category: "text"
    collectionName: "Themes"
    description: "Strong danger text color for high-emphasis error, destructive, and critical status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/danger/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.danger.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.danger.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.200"
      light: "foundation.color.palette.info.200"
    category: "text"
    collectionName: "Themes"
    description: "Info text color for informational messages and status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/info"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.info"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.info"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.info.300"
      light: "foundation.color.palette.info.300"
    category: "text"
    collectionName: "Themes"
    description: "Strong info text color for high-emphasis informational messages and status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/info/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.info.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.info.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.200"
      light: "foundation.color.palette.success.200"
    category: "text"
    collectionName: "Themes"
    description: "Success text color for positive, completed, and confirmed status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/success"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.success"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.success"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.success.300"
      light: "foundation.color.palette.success.300"
    category: "text"
    collectionName: "Themes"
    description: "Strong success text color for high-emphasis positive, completed, and confirmed status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/success/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.success.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.success.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.200"
      light: "foundation.color.palette.warning.200"
    category: "text"
    collectionName: "Themes"
    description: "Warning text color for caution, attention, and recoverable issue labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/warning"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.warning"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.warning"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.warning.300"
      light: "foundation.color.palette.warning.300"
    category: "text"
    collectionName: "Themes"
    description: "Strong warning text color for high-emphasis caution, attention, and recoverable issue labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    kind: "alias"
    name: "color/text/functional/warning/strong"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.functional.warning.strong"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.functional.warning.strong"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.50"
      light: "foundation.color.palette.neutral.900"
    category: "text"
    collectionName: "Themes"
    description: "Text color for primary headings and high-emphasis titles. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    kind: "alias"
    name: "color/text/heading"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.heading"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.heading"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.white"
      light: "foundation.color.palette.black-and-white.white"
    category: "text"
    collectionName: "Themes"
    description: "Heading text color for headings on strong colored surfaces. Do not use for fills, borders, icons, links, standalone brand accents, functional text, or normal neutral surfaces."
    kind: "alias"
    name: "color/text/heading/onColor"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.heading.onColor"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.heading.onColor"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.white"
      light: "foundation.color.palette.black-and-white.white"
    category: "text"
    collectionName: "Themes"
    description: "Text color for text on inverse or dark neutral surfaces. Do not use for fills, borders, icons, links, functional feedback, brand accents, or normal light surfaces."
    kind: "alias"
    name: "color/text/inverse"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.inverse"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.inverse"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.300"
      light: "foundation.color.palette.primary.500"
    category: "text"
    collectionName: "Themes"
    description: "Default link text color for inline and navigational links. Do not use for body text, fills, borders, icons, or non-link text."
    kind: "alias"
    name: "color/text/link"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.link"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.link"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.200"
      light: "foundation.color.palette.primary.200"
    category: "text"
    collectionName: "Themes"
    description: "Disabled link text color. Do not use for enabled links, body text, fills, borders, or icons."
    kind: "alias"
    name: "color/text/link/disabled"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.link.disabled"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.link.disabled"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.200"
      light: "foundation.color.palette.primary.700"
    category: "text"
    collectionName: "Themes"
    description: "Link text color for hover state. Do not use for default, pressed, visited, disabled, fills, borders, or icons."
    kind: "alias"
    name: "color/text/link/hover"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.link.hover"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.link.hover"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.500"
      light: "foundation.color.palette.black-and-white.white"
    category: "text"
    collectionName: "Themes"
    description: "Link text color for inverse or on-color surfaces. Do not use for standard surface links, body text, fills, borders, or icons."
    kind: "alias"
    name: "color/text/link/inverse"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.link.inverse"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.link.inverse"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.primary.400"
      light: "foundation.color.palette.primary.900"
    category: "text"
    collectionName: "Themes"
    description: "Link text color for pressed state. Do not use for default, hover, visited, disabled, fills, borders, or icons."
    kind: "alias"
    name: "color/text/link/pressed"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.link.pressed"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.link.pressed"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.secondary.300"
      light: "foundation.color.palette.secondary.700"
    category: "text"
    collectionName: "Themes"
    description: "Link text color for visited links. Do not use for default links, body text, fills, borders, or icons."
    kind: "alias"
    name: "color/text/link/visited"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.link.visited"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.link.visited"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.black-and-white.white"
      light: "foundation.color.palette.black-and-white.white"
    category: "text"
    collectionName: "Themes"
    description: "Text color for readable text on strong colored surfaces. Do not use for fills, borders, icons, links, standalone brand accents, functional text, or normal neutral surfaces."
    kind: "alias"
    name: "color/text/onColor"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.onColor"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.onColor"
    type: "color"
  -
    aliasByMode:
      dark: "foundation.color.palette.neutral.200"
      light: "foundation.color.palette.neutral.700"
    category: "text"
    collectionName: "Themes"
    description: "Text color for secondary headings and section titles. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    kind: "alias"
    name: "color/text/subheading"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "color.text.subheading"
      alpyResourceType: "semantic-token"
      alpyRevision: 0
    tokenId: "color.text.subheading"
    type: "color"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-2xs layer 1."
    kind: "value"
    name: "Shadow/2XS/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xs.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xs.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 1.95
      light: 1.95
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-2xs layer 1."
    kind: "value"
    name: "Shadow/2XS/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xs.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xs.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 1.95
      light: 1.95
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-2xs layer 1."
    kind: "value"
    name: "Shadow/2XS/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xs.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xs.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 2.6
      light: 2.6
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-2xs layer 1."
    kind: "value"
    name: "Shadow/2XS/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xs.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xs.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-2xs layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/2XS/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xs.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xs.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#CECECE26"
      light: "#00000026"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-xs layer 1."
    kind: "value"
    name: "Shadow/XS/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xs.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xs.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-xs layer 1."
    kind: "value"
    name: "Shadow/XS/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xs.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xs.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 1
      light: 1
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-xs layer 1."
    kind: "value"
    name: "Shadow/XS/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xs.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xs.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 4
      light: 4
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-xs layer 1."
    kind: "value"
    name: "Shadow/XS/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xs.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xs.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-xs layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/XS/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xs.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xs.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#CECECE29"
      light: "#00000029"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-sm layer 1."
    kind: "value"
    name: "Shadow/SM/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-sm.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-sm.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-sm layer 1."
    kind: "value"
    name: "Shadow/SM/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-sm.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-sm.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 2
      light: 2
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-sm layer 1."
    kind: "value"
    name: "Shadow/SM/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-sm.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-sm.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 8
      light: 8
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-sm layer 1."
    kind: "value"
    name: "Shadow/SM/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-sm.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-sm.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-sm layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/SM/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-sm.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-sm.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#A1A1A133"
      light: "#5C5C5C33"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-md layer 1."
    kind: "value"
    name: "Shadow/MD/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-md.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-md.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-md layer 1."
    kind: "value"
    name: "Shadow/MD/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-md.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-md.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 3
      light: 3
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-md layer 1."
    kind: "value"
    name: "Shadow/MD/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-md.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-md.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 8
      light: 8
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-md layer 1."
    kind: "value"
    name: "Shadow/MD/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-md.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-md.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-md layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/MD/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-md.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-md.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#CECECE3D"
      light: "#0000003D"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-lg layer 1."
    kind: "value"
    name: "Shadow/LG/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-lg.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-lg.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-lg layer 1."
    kind: "value"
    name: "Shadow/LG/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-lg.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-lg.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 5
      light: 5
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-lg layer 1."
    kind: "value"
    name: "Shadow/LG/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-lg.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-lg.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 15
      light: 15
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-lg layer 1."
    kind: "value"
    name: "Shadow/LG/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-lg.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-lg.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-lg layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/LG/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-lg.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-lg.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#CECECE59"
      light: "#00000059"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-xl layer 1."
    kind: "value"
    name: "Shadow/XL/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xl.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xl.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-xl layer 1."
    kind: "value"
    name: "Shadow/XL/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xl.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xl.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 8
      light: 8
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-xl layer 1."
    kind: "value"
    name: "Shadow/XL/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xl.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xl.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 24
      light: 24
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-xl layer 1."
    kind: "value"
    name: "Shadow/XL/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xl.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xl.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-xl layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/XL/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-xl.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-xl.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#76767633"
      light: "#A1A1A133"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-2xl layer 1."
    kind: "value"
    name: "Shadow/2XL/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xl.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xl.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-2xl layer 1."
    kind: "value"
    name: "Shadow/2XL/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xl.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xl.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 7
      light: 7
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-2xl layer 1."
    kind: "value"
    name: "Shadow/2XL/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xl.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xl.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 29
      light: 29
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-2xl layer 1."
    kind: "value"
    name: "Shadow/2XL/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xl.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xl.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-2xl layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/2XL/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-2xl.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-2xl.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#A1A1A133"
      light: "#5C5C5C33"
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware x for shadow-3xl layer 1."
    kind: "value"
    name: "Shadow/3XL/Layer 1/X"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-3xl.layer.1.x"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-3xl.layer.1.x"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware y for shadow-3xl layer 1."
    kind: "value"
    name: "Shadow/3XL/Layer 1/Y"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-3xl.layer.1.y"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-3xl.layer.1.y"
    type: "number"
    valuesByMode:
      dark: 48
      light: 48
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware blur for shadow-3xl layer 1."
    kind: "value"
    name: "Shadow/3XL/Layer 1/Blur"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-3xl.layer.1.blur"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-3xl.layer.1.blur"
    type: "number"
    valuesByMode:
      dark: 100
      light: 100
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware spread for shadow-3xl layer 1."
    kind: "value"
    name: "Shadow/3XL/Layer 1/Spread"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-3xl.layer.1.spread"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-3xl.layer.1.spread"
    type: "number"
    valuesByMode:
      dark: 0
      light: 0
  -
    category: "semantics.shadow"
    collectionName: "Themes"
    description: "Mode-aware alpha-bearing color for shadow-3xl layer 1; derived from its canonical semantic color token and opacity."
    kind: "value"
    name: "Shadow/3XL/Layer 1/Color"
    ownership:
      alpyLibraryId: "lib_alpy_builtin"
      alpyResourceId: "shadow-3xl.layer.1.color"
      alpyResourceType: "variable"
      alpyRevision: 0
    tokenId: "shadow-3xl.layer.1.color"
    type: "color"
    valuesByMode:
      dark: "#F1F1F126"
      light: "#15151526"
```

## Resolution Algorithm

1. Resolve the explicit mode first: light or dark.
2. For color variables, read the semantic variable by tokenId and valuesByMode.
3. For typography, read the text style by tokenRef or styleId and use the full tuple together.
4. For spacing, radius, stroke, elevation, and sizing, read resolved numberTokensByMode by tokenRef.
5. Use the resolved value in the active mode.
6. If a requested foundation value is absent, stop and report the missing binding.

## Rules

- Resolve foundation values from canonical bindings only.
- Keep light and dark values explicit; do not use a silent fallback mode.
- Do not derive missing foundation values from rendered UI, screenshots, or Figma state.
- Generated package data contains active values with user overrides already materialized.
