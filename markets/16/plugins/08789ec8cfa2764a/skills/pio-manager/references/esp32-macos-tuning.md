# ESP32 macOS Port Conflicts & Config Tuning

When configuring ESP32 and ESP32-S3 devices running on macOS inside PlatformIO, developers often encounter kernel-level port exceptions. This reference synthesizes the required `.ini` configurations and debugging steps to ensure stability.

## 1. `platformio.ini` Configurations for Native USB
For modern ESP32 variants (like ESP32-S3) leveraging their internal Native USB PHY, standard Serial configs will fail. You MUST inject the following into the environment:

```ini
; 1. NATIVE USB SUPPORT
; Initialize the USB CDC stack so logs don't go to the unpopulated physical RX/TX pins
-D ARDUINO_USB_MODE=1
-D ARDUINO_USB_CDC_ON_BOOT=1

; 2. HARDWARE IDENTITY RESTORATION
; Prevent the device from assuming the generic Espressif "JTAG" identity (303A:1001)
; Replace these with your board's factory Vendor and Product IDs.
-D USB_VID=0x2341
-D USB_PID=0x0070

; 3. macOS MONITOR STABILITY
; Keep standard serial monitors from aggressively dropping the DTR/RTS lines
; and forcing the board into a hard-reset bootloop when opening the terminal.
monitor_dtr = 0
monitor_rts = 0

; 4. USB BOOTLOADER BRIDGING
; Exploit the 1200bps touch feature to cleanly flip the chip into JTAG mode.
; This bypasses the standard DTR hardware reset which crashes native macOS endpoints.
upload_protocol = esptool
board_upload.use_1200bps_touch = yes
board_upload.wait_for_upload_port = yes
```

## 2. Hardware Identity Diagnostics
If an environment auto-detect fails, or you are compiling against an unknown clone board, extract the exact HWIDs (VID & PID) using these tools:
- **PIO Agent:** Use `pio-agent devices` for discovery and `pio-agent target-resolve` for the selected project and environment. VID/PID is a discovery hint, not a unique physical identity or permission to flash.
- **macOS System Info:** Open *System Information* -> *Hardware* -> *USB*. The Vendor and Product ID will be listed in hex.

## 3. Resolving macOS Specific Port Anomalies
If the hardware connection drops unexpectedly or errors during the `pio` task pipeline, diagnose against these documented failure states:

*   **`[Errno 16] Resource busy` upon upload**:
    **Cause:** The port's file descriptor is locked by a lingering VSCode serial monitor process, OR competing macOS driver extensions (Legacy OEM vs Apple DriverKit) are colliding.
    **Fix:** Enable `platformio-ide.autoCloseSerialMonitor = true` in VSCode. Run CLI tracking `kextstat | grep -i silabs` or `kextstat | grep -i wch` to see if legacy kernel extensions are loaded. If so, unload them (e.g. `sudo kextunload /Library/Extensions/SiLabsUSBDriver.kext`) to allow DriverKit full control.
*   **`[Errno 6] Device not configured` or Monitor fails to open after flash**:
    **Cause:** PlatformIO's task pipeline attempts to seize the `/dev/cu.*` node *before* the macOS USB enumeration finishes digesting the hardware reconnect.
    **Fix:** Set `platformio-ide.reopenSerialMonitorDelay = 2000` to buffer the OS delay.
*   **Port suffix drifts uncontrollably (e.g. `usbserial-0001` -> `0002`)**:
    **Cause:** Counterfeit USB bridge chips lacking unique embedded serial numbers. macOS sees rapid disconnects and increments the node to avoid descriptor collisions.
    **Fix:** Re-resolve the target binding after re-enumeration. Continue only if the stable fingerprint still matches the approved physical target; stop on ambiguity. Do not use a wildcard upload port to choose among devices.
*   **PlatformIO targets the wrong board in a wildcard setup**:
    **Fix:** Remove ambiguous wildcard selection within the user's authorized configuration scope, then resolve one explicit environment and physical target through PIO Agent. Do not bypass target checks with a VID/PID-only selector or project hook.
