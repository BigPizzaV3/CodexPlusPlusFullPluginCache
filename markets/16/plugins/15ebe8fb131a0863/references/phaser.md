# Phaser 2D development reference

Official documentation: https://www.phaser.io/oss/docs/ and https://www.phaser.io/oss/docs/phaser/getting-started/installation

Current official docs cover Phaser 4 and highlight the difference from Phaser 3. Use versioned API reference for actual installed package. Phaser is a 2D framework; do not claim native built-in 3D renderer/physics.

Recommended implementation order: create verified project scaffold -> Boot/Menu scene -> Player input and state -> Physics/collisions -> Objective and feedback -> Win/lose and restart -> Touch and responsive sizes if applicable -> Tests.

Build with project scripts after checking package.json and actual dependencies. Phaser Arcade Physics configuration, scene lifecycle and texture generation require version-specific verification. Avoid copying old Arcade API without checking. Use a browser to verify key events, collisions, console errors and visibility/focus behavior.
