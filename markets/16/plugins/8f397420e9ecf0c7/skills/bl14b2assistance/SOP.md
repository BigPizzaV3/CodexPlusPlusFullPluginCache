# SOP

Version: v2.10
Revision date: 2026-11-06
Content status: Authoritative BL14B2 reference content.
Structure status: Independent reference document with its own navigation index; shared assistant behavior is maintained in the skill entrypoint.
Applies to: BL14B2 users and AI-assisted guidance

## Internal Topic Index

Internal navigation only. Use the named Reference passages; do not output this table or its identifiers to users. Related terms route a question and do not assert that the terms are synonymous.

| Names and related query terms | Explanation reference | Operation reference or coverage |
| --- | --- | --- |
| Optics; Auto Optics; Si(311); rocking curve; Δθ; mechanical stress; 光学调整; 摇摆曲线; 机械应力; ロッキングカーブ | Introduction 1.2 | SOP 1.2, 1.2.6 |
| Energy Calibration; 能量校准 | Introduction 2.2 | SOP 2.2 |
| Auto Amp Tune; gain; amplifier; overflow; 增益 | Introduction 3.2 | SOP 3.2, 3.2.8 |
| WorkStation; encoder; theta; 编码器 | Introduction 4.2 | SOP 4.2 |
| Transmission; 透过法; 透過法 | Introduction 5.2.1 | SOP 5.2.1.0 |
| Fluorescence; 19SSD; DSP; ROI; SCA; Total; ICR; beam size; sample size; 荧光; 光斑; 光斑大小; 样品大小; ビームサイズ; 試料サイズ | Introduction 5.2.2, 7.2.2.1 | SOP 5.2.2.1, 5.2.2.3, 5.2.2.4 |
| Grazing incidence; 掠入射 | Introduction 5.2.2, 7.2.3 | SOP 5.2.2.2 |
| CEY; Conversion Electron Yield; 电子产额 | Introduction 5.2.3, 7.2.4 | SOP 5.2.3.0, 5.2.3.2 |
| QXAFS; dwell; Loop; Stop Loop; 快速扫描 | Introduction 6.2.1 | SOP 6.2.1, 6.2.1.1, 6.2.1.2 |
| Step XAFS; step scan; 步进扫描 | Introduction 6.2.2 | SOP 6.2.2 |
| QXAFS–Step energy conversion; 能量轴转换 | Introduction 6.2.1.1 | Staff-provided method; no executable conversion SOP |
| Sample requirements; pellet; BN; SiC; 样品制备 | Introduction 7.2, 13.2 | SOP 7.2 |
| JIN; XAFS Absorption Calculation Assistant; 吸收计算助手 | Introduction 7.2.6 | Name and public access link only; no detailed software SOP |
| PM16C; motor; 电机 | Introduction 8.2 | SOP 8.2 |
| 4D slit; 狭缝 | Introduction 9.2 | SOP 9.2 |
| MBS; DSS; shutter; 快门 | Introduction 10.2 | SOP 10.2 |
| Cryostat; low temperature; 低温; cooling water | Introduction 11.2 | SOP 11.2, 11.2.4 |
| HummingBird; Hummingbird; sample changer; 自动换样 | Introduction 12.2 | SOP 12.2 |
| In-situ cell; quartz cell; high pressure; 原位池 | Introduction 13.2 | SOP 13.2 |
| High-pressure sample holder; powder loading; quartz film; 高圧ホルダー; 粉末充填 | Introduction 13.2.2.1, 13.2.2.2 | SOP 13.2.2 |
| Preformed pellet; areal-density uniformity; pellet retention; ペレット保持 | Introduction 13.2.2.2 | Staff confirmation for pellet retention; SOP 13.2.2 covers powder loading only |
| High-pressure gas compatibility; NH3; NO; corrosion; 高圧ガス適合性 | Introduction 13.2.2.3, 15.2.4, 15.2.5 | Prior staff confirmation; no gas-specific high-pressure operating SOP |
| Reaction products; condensation; cooling; 凝縮; 冷却 | Introduction 13.2.2.4 | Planning guidance only; no condensation-control SOP |
| Heating pattern; PID; GAIN; PTN; STEP; 加热 | Introduction 14.2 | SOP 14.2 |
| Gas; MFC; PV; SV; N2 dilution; 气体; 流量 | Introduction 15.2 | SOP 15.2.1, 15.2.3 |
| Alarm; gas leak; 报警; 泄漏 | Introduction 15.2.5 | SOP 15.2.2 |
| Form 25; cylinder; 高压气体容器申请 | Introduction 15.2 | Contact information in Introduction 15.2 |
| QXAFS monitor; Beamchat; camera; 日志; 相机 | Introduction 16.2 | SOP 6.2.1, 6.2.1.1 for documented QXAFS checks |
| Standard sample list; reference sample; standard foil; BL01B1 standard samples; 标准样品; 标准样品列表; 標準試料; 標準試料リスト | Introduction 17.2 | Reference list only; no SOP |

Existing Reference section identifiers (such as 1.2) are retained for continuity. The removed AI-facing sections (such as 1.1) are not missing reference content.

## Contents

- Chapter 1: Optics(Energy) Adjustment
- Chapter 2: Energy Calibration
- Chapter 3: Auto Amp Tune
- Chapter 4: WorkStation and Encoder Value Correction
- Chapter 5: Measurement Method
- Chapter 6: Measurement Mode
- Chapter 7: Sample Requirement
- Chapter 8: Operation of PM16C
- Chapter 9: Operation of 4D slit
- Chapter 10: Operation of MBS/DSS
- Chapter 11: Cryostat Experiment
- Chapter 12: HummingBird Automatic Measurement
- Chapter 13: In-situ Cells Provided by BL14B2
- Chapter 14: In-situ Cell Heating Controller
- Chapter 15: BL14B2 Gas Supply System

## 1. Optics(Energy) Adjustment

### 1.2. Reference
#### 1.2.0. Pre-conditions

Before starting optics adjustment, confirm ALL of the following:

1. Hutch safety conditions are satisfied:
   - Door closed
   - Interlock enabled
   - No person inside the hutch
2. Standard sample installed
3. The SPring-8 light source is operating normally
4. All hardware systems are functioning normally, and no unrelated software is running on the control PC
5. The 19SSD fluorescence detector is in the protected state

Do not proceed unless all conditions above are satisfied.

#### 1.2.1. Starting the Optics Program

1. Open [BL14B2 Control2.vi] on PC desktop.
2. Select “Auto Optics” from the menu window.
3. Click the Run button to open [Optics_Auto_090405.vi].
4. Click the Run button inside [Optics_Auto_090405.vi].

Initialization begins automatically.

During initialization:
- The indicator lamp flashes.
- When initialization is completed, the lamp turns green.
- The monochromator crystal plane is read automatically.

Confirm that the crystal plane is displayed correctly in [Select Net Plane].

#### 1.2.2. Input Parameter Selection

1. Select the absorption edge to be measured.
2. Select the crystal plane:
   - Si(111)
   - Si(311)

The Setup area displays recommended values automatically, including:
- Monochromator Bragg angle
- Mirror angle
- TC Slit1 height
- TC Slit2 height
- Ion chamber gas mixture ratio

##### 1.2.2.1. (Optional) Manual Parameter Input

If the recommended values need to be modified:

1. Press the “manual” button.
2. Yellow fields become editable white fields.
3. Input the required values manually.

#### 1.2.3. Auto / Manual Operation Mode

1. Select either “Auto” or “Manual” mode to execute the optics adjustment sequence.

After confirming all values:

2. Press the Start OK button.
3. Confirm the settings again in the popup confirmation window.
4. Press OK to begin optics adjustment.

If problems are found before execution:
- Press the Stop button.
- Restart from initialization.

##### 1.2.3.1. (Optional) Manual Scan Sequence

If manual scanning is necessary, the following scan sequence is executed during optics adjustment:

1. Monochromator Rocking Curve Scan
2. Experimental Hutch 4D Slit Horizontal Scan
3. Optics Moving
4. Monochromator Rocking Curve Scan
5. 1st Mirror Vertical Scan
6. 2nd Mirror Vertical Scan
7. TC Slit2 Vertical Scan
8. Experimental Hutch Stage Vertical Scan
9. Experimental Hutch 4D Slit Horizontal Scan
10. Slit Moving

#### 1.2.4. Completion Conditions

Optics adjustment is considered complete when:

- The Run button becomes active.
- The Stop button becomes inactive.
- All step indicators in the right column are green.

After completion:
1. Close all scan windows.
2. Confirm Current Amp output values.
3. Disable DSS if necessary.

#### 1.2.5. (Optional) Manual Interruption

If any of the following problems occur, immediately stop the program using Manual interruption mode and contact the responsible BL staff:

1. Any abnormal mechanical sound during optics movement
2. Beam abort during optics adjustment
3. Incorrect instrument connection
4. Incorrect optics settings requiring restart

Procedure:

1. Switch [Auto] to [Manual] during operation.
2. After the current process finishes, click [No] to stop the remaining sequence.
3. Restart optics adjustment if necessary.

#### 1.2.6. (Optional) Monochromator Rocking Curve Scan

This procedure may be used when Si(311) is used and users are particularly concerned about changes in the absolute value of "μT". Introduction.md, Section 1.2 explains the background.

##### 1.2.6.0. Preconditions

Before starting the rocking curve scan, confirm ALL of the following:

1. Hutch safety conditions are satisfied:
   - Door closed
   - Interlock enabled
   - No person inside the hutch
2. The SPring-8 light source is operating normally
3. All hardware systems are functioning normally, and no unrelated software is running on the control PC

Do not proceed unless all conditions above are satisfied.

##### 1.2.6.1. Executing the Rocking Curve Scan

1. Open [BL14B2 Control2.vi].
2. Select [rocking curve.vi], and click the Run button (white arrow) to open the [rocking curve.vi] window.
3. Open DSS.
4. Click the Run button (white arrow) in [rocking curve.vi].

The rocking curve scan is executed automatically.

The scan is complete when the arrow of the Run button changes from black to white.

5. Close the [rocking curve.vi] window.
6. Close DSS.

##### 1.2.6.2. Failure / Escalation

Immediately stop and contact BL14B2 staff if:

1. The rocking curve scan fails.

---

## 2. Energy Calibration

### 2.2. Reference

#### 2.2.0. Preconditions

In the standard BL14B2 user workflow, perform this calibration after optics adjustment or a large energy change. It need not be repeated for each sample under the same unchanged optical condition. Introduction.md, Section 2.2 distinguishes this workflow from an experienced user's later reference-based data calibration.

Before starting energy calibration, confirm ALL of the following:

1. A reference XAFS spectrum has already been measured.
2. The reference spectrum contains a reliable calibration feature:
   - E0 (can be either a measured value or a theoretical value)
   - absorption edge
3. The monochromator crystal plane is known.

Do not proceed unless all conditions above are satisfied.

#### 2.2.1. Measure Reference Spectrum

1. Measure the XAFS spectrum of the standard sample for calibration.
2. Identify the E0 to be used for calibration using analysis software.

#### 2.2.2. Calibration

1. On analysis PC, open enc_reset.xlsx
2. Input the monochromator crystal plane used during measurement.
   Examples:
   - Si(111)
   - Si(311)
3. In "1 ref - Energy", input literature reference energy E0
4. In "2 now - Energy", input energy E0 of measured standard sample
5. In "3 present_th theta", input the theta value shown in encoder display
6. Get the calibrated theta value in "4 preset_theta theta".

#### 2.2.3. Preset encoder theta value

1. Open [BL14B2 Control2.vi] on PC desktop.
2. Select "θ Move” from the menu window.
3. Click the Run button to open [θ Move.vi].
4. Click the "Preset" tab, input the calibrated theta value in [Present Angle] and click Run button.

#### 2.2.4. Verification

After calibration:

1. Reconfirm the energy position using the reference spectrum.
2. Confirm that the measured edge position matches the expected reference value.

#### 2.2.5. Failure / Escalation

Immediately stop and contact BL staff if:

1. Encoder values behave abnormally.
2. θ Move fails to execute correctly.
3. Energy shifts remain inconsistent after correction.
4. Crystal-plane mismatch is suspected.
5. Unexpected monochromator behavior occurs.

---

## 3. Auto Amp Tune

### 3.2. Reference

#### 3.2.0. Preconditions

Before starting Auto Amp Tune, confirm ALL of the following:

1. Hutch safety conditions are satisfied:
   - Door closed
   - Interlock enabled
   - No person inside the hutch

2. Sample installed

3. The SPring-8 light source is operating normally

4. All hardware systems are functioning normally, and no unrelated software is running on the control PC

#### 3.2.1. Launch Auto Amp Tune

1. Open [BL14B2 Control2.vi] on the PC desktop.

2. Select “Auto Amp tune” from the menu window.

3. Click the Run button to open [Auto_AmpTune.vi].

4. Click the Run button inside [Auto_AmpTune.vi].

#### 3.2.2. Input Absorption Edge

1. In [Absorption Edge], input the absorption edge name for gain tuning.

Examples:
- Fe-K
- Mn-K
- Pt-L3

##### 3.2.2.1. Multiple Edge Input (Optional)

If multiple tuning conditions are required:

1. In [Absorption Edge], input multiple absorption edge names separated by “|”.

Examples:

- Fe-K|Fe-K:20
  - Gain tuning at:
    - Fe-K pre-edge
    - high-energy-side k = 20 Å⁻¹ region

- Mn-K|Fe-K|Fe-K:20
  - Gain tuning at:
    - Mn-K pre-edge
    - Fe-K pre-edge
    - Fe-K high-energy-side k = 20 Å⁻¹ region

#### 3.2.3. Confirm Gain Tune Angles

After entering the absorption edge:

1. Press the [Enter] key, or click somewhere on the [Auto_AmpTune.vi] panel.

2. Confirm that appropriate values are displayed in [gain tune angles].

Do not proceed unless valid gain tune angles are displayed.

#### 3.2.4. Start Auto Gain Tuning

1. Click the [tune] button.

2. Automatic gain tuning begins.

#### 3.2.5. Confirm Tuning Results

After tuning is completed:

1. Confirm that the following are displayed on the screen:
   - I0 gain
   - I1 gain
   - I0 Suppression value
   - I1 Suppression value

##### 3.2.5.1. Manual Amp Tuning (Optional)

If the user understands the effect of gain settings, manual amp tuning may be used.

1. After activating [Auto_AmpTune.vi], there is no need to input [Absorption Edge] or click the [tune] button.

2. The gain values can be changed directly in [I0 gain], [I1 gain], etc.  
   The gain value range is 6–9.

3. Confirm that the following are displayed on the screen:
   - I0 gain
   - I1 gain
   - I0 Suppression value
   - I1 Suppression value

#### 3.2.6. Completion

After gain adjustment is completed:

1. Click the [Quit] button.

2. Exit the program normally.

#### 3.2.7. Failure / Escalation

Refer to the Introduction section to identify and resolve the cause, then perform tuning again if:

1. Auto Amp Tune finishes within a few seconds, or cannot be executed.

#### 3.2.8. Amplifier Overflow During a Scan

1. If an overflow alarm sounds during a scan, do not change the amplifier gain while the mechanical scan is running. Counting is unavailable during overflow, but the mechanical scan continues.
2. Wait until the scan has finished. The alarm alone is not a reason to change gain during the scan, because doing so can cause a system bug.
3. After the scan has finished, adjust the amplifier gain using the applicable Auto Amp Tune or manual tuning procedure in this chapter.

---

## 4. WorkStation and Encoder Value Correction

### 4.2. Reference

#### 4.2.0. Preconditions

1. Ensure that all other software has been stopped.
2. When moving theta, ensure that the 19SSD will not suffer radiation damage.

#### 4.2.1. Open [θ Move.vi]

1. Open [BL14B2 Control2.vi] on the PC desktop.
2. Select “θ Move” from the menu window.
3. Click the button to open [θ Move.vi].
For a calibrated encoder preset, use Section 2.2.3. For reading, movement, or WorkStation-based presetting, select the corresponding procedure in Sections 4.2.2–4.2.4.

#### 4.2.2. (Optional) Read WorkStation and Encoder Values

1. Click the “Operation” tab and select:
   - “Encoder Display”
   - “Encoder Board”
   - or “Work Station”

2. Click [Read].

3. Click the Run button to read the corresponding value.

#### 4.2.3. (Optional) Move WorkStation and Encoder Values

1. Click the “Operation” tab and select “Encoder Display”.
2. Input the target value into [Destination] and click [Move].
3. Click the Run button to execute the movement.

#### 4.2.4. (Optional) Preset WorkStation and Encoder Values

1. Read the “Work Station” value.
2. Click the “Preset” tab and input the “Work Station” theta value into [Present Angle].
3. Click the Run button to preset the Encoder value to the WorkStation value.

---

## 5. Measurement Method

### 5.2. Reference

##### 5.2.1.0. Transmission Mode Preconditions

These are preparation and measurement-readiness requirements, not a sequential instruction to install or align a sample after closing the hutch. The hutch safety conditions must be satisfied before measurement.

1. Hutch safety conditions are satisfied:
   - Door closed
   - Interlock enabled
   - No person inside the hutch
2. Ensure that the SPring-8 light source is operating normally.
3. Ensure that all hardware systems are functioning normally, and that no unrelated software is running on the control PC.
4. Ensure that the 19SSD detector is not exposed to X-rays.
5. Install the sample, and confirm that the sample is located at the center of the X-ray beam path using the rear red laser.
6. Confirm that the sample size is larger than the default beam size, which is 5 mm in width and 1 mm in height.
7. If necessary, adjust the beam width using the 4D slit. The adjustable width range is 0.5–5 mm. The beam height remains unchanged.
8. Check whether the GAIN value needs to be adjusted.

##### 5.2.1.1. Transmission Mode Scan Mode

1. Select QXAFS or Step XAFS.

##### 5.2.2.0. Fluorescence Mode Preconditions

These are preparation and measurement-readiness requirements, not a sequential instruction to install or align a sample after closing the hutch. The hutch safety conditions must be satisfied before measurement.

1. Hutch safety conditions are satisfied:
   - Door closed
   - Interlock enabled
   - No person inside the hutch
2. Ensure that the SPring-8 light source is operating normally.
3. Ensure that all hardware systems are functioning normally, and that no unrelated software is running on the control PC.
4. For a general sample, keep the incident X-ray beam at an angle of 45° to the sample surface.
5. Confirm that the sample is located on the X-ray beam path using the rear red laser.
6. If alignment using the rear red laser is not possible, the front green laser may be used. However, since the green laser is less stable, it is recommended to calibrate it once using the red laser before use.
7. Check whether the GAIN value needs to be adjusted.
8. Ensure that the high voltage for the 19SSD is connected, and that the Pb cover in front of the 19SSD has been opened.

##### 5.2.2.1. Fluorescence Mode ROI Setup

1. Before confirming the ROI, make sure that the current sample is a standard sample. This ensures that the fluorescence signal from the target element can be observed.
2. In the same experiment, the ROI for each target element needs to be set only once. If the ROI has already been confirmed, skip [Fluorescence Mode ROI Setup].
3. Ensure that the 19SSD is at the farthest position from the sample and that the 4D slit width is set to the minimum. In [PM16C Move.vi], the position of channel “Detector X” should be -50.
4. Confirm that the current monochromator angle, namely the value shown on the encoder, corresponds to an energy above the absorption edge of the target element. If not, move the monochromator angle using [Theta Move.vi].
5. Open [DSP Tools.exe] on the desktop, and open [ROI Setting].
6. Open DSS, click [Start Measurement], and close DSS after the signal appears.
7. Observe the signal peaks displayed in the software. Hold down the left mouse button and drag to the right to enlarge the signal region. To cancel the zoom, hold down the left mouse button and drag to the left.
8. Input the absorption edge name into [Absorption Edge Name]. Use the following format:
   - Fe-K
   - Pt-L3
9. Click [Get ROI], and confirm that the ROI range corresponding to the selected absorption edge is displayed on the signal plot.
10. Confirm whether the current ROI range fully covers the target signal region.
11. If the current ROI range is not appropriate, select [lower] and double-click the left side of the signal peak. Then select [upper] and double-click the right side of the signal peak.
12. Confirm that the ROI range has been updated correctly.
13. Using the same procedure, confirm and correct the ROI ranges for ch1–ch19, corresponding to detector elements 1–19.
14. Click [Put ROI] to overwrite the previous ROI ranges with the corrected ones, and confirm again that the ROI ranges for all channels are correct.

##### 5.2.2.2. Sample Position Adjustment for Grazing-Incidence Fluorescence Mode

1. This section is used only for sample position adjustment in grazing-incidence fluorescence measurements.
2. Mount the sample on the sample stage for grazing-incidence geometry.
3. Ensure that the 19SSD is at the farthest position from the sample and that the 4D slit width is set to the minimum.
4. In [PM16C Move.vi], adjust the height of the 19SSD using channel “Detector Z”.
5. In [PM16C Move.vi], confirm the values of “Sample Lin.” and “Sample Theta”, and move both values to 0.
6. Set the width of the 4D slit to 5 mm.
7. In [PM16C Move.vi], adjust “Sample Lin.” using the rear red laser so that the sample surface is approximately covered by the red laser, and record the current “Sample Lin.” value.
8. The sample position in the x direction can be adjusted manually using the sample stage.
9. Open DSS.
10. Based on the recorded “Sample Lin.” value, perform a scan using channel “Sample Lin.” in [PM16C Scan.vi], with the current “Sample Lin.” value as the scan center.
11. The following scan conditions may be used as a reference:
   - Measure Start: current value - 0.25
   - Start position: current value - 0.2
   - Step: 0.02
   - Dest. position: current value + 0.2
12. Confirm that [Counter] is set to “Tuji counter”, and that [19SSD Counter] is set to “DSP”.
13. Input the absorption edge information into [19SSD Edge]. For example:
   - Fe-K
14. If the fluorescence signal is not required for the scan, set [19SSD Counter] to “no use”.
15. Click the white Run arrow to start the window, then click [Start] and select [OK] to begin the scan.
16. After the scan is finished, read the x coordinate of the middle of the signal jump position in the transmission signal “I1”. This position corresponds to the sample blocking approximately half of the X-ray beam.
17. In [PM16C Move.vi], move channel “Sample Lin.” to the coordinate obtained above.
18. Select channel “Sample Theta” in [PM16C Scan.vi], and perform a scan using the current “Sample Theta” value as the scan center.
19. The following scan conditions may be used as a reference:
   - Measure Start: current value - 3.5
   - Start position: current value - 3
   - Step: 0.1
   - Dest. position: current value + 3
20. Confirm the current theta value shown on the encoder, and ensure that the current energy is above the absorption edge of the target element. If necessary, move theta.
21. Confirm that DSS is still open.
22. Click the white Run arrow to start the window, then click [Start] and select [OK] to begin the scan.
23. After the scan is finished, read the peak position in the fluorescence signal “SDD”, and record the x coordinate of the SDD peak.
24. In general, the peak of the fluorescence signal “SDD” appears near the signal jump position of “I1”, but slightly higher.
25. The actual sample position may be set to the SDD peak x coordinate +0.4–0.5.
26. If the fluorescence signal cannot be observed, or if the signal is too weak, gradually move the 19SSD closer to the sample using channel “Detector X” in [PM16C Move.vi].
27. If the “I1” signal jump can be observed but the fluorescence signal “SDD” still cannot be observed, check the sample and the current theta value shown on the encoder.
28. If there is no problem with the sample or the theta value, it may be concluded that the sample cannot be measured by grazing-incidence fluorescence mode.
29. In [PM16C Move.vi], move channel “Sample Theta” to the calculated coordinate.
30. Repeat the “Sample Lin.” scan, and confirm that the center position of the “I1” signal jump no longer changes.
31. Finally, perform a precise scan of “Sample Theta” using the following scan conditions as a reference:
   - Measure Start: current value - 3.5
   - Start position: current value - 3
   - Step: 0.1
   - Dest. position: current value + 3

32. After the scan is finished, read the peak position in the fluorescence signal “SDD”, and record the x coordinate of the SDD peak.
33. Set the actual sample position to the SDD peak x coordinate +0.4–0.5.
34. In [PM16C Move.vi], move channel “Sample Theta” to the calculated coordinate.
35. Close DSS.

##### 5.2.2.3. SSD Intensity Control in Fluorescence Mode

Count-rate limits in this section apply to Total (ICR), not ROI (SCA), and are expressed in cps. DSP Tools uses a default counting interval of 1 s, so accumulated cnts are numerically equal to the average rate in cps at that setting. If the interval changes, divide counts by the interval in seconds before comparing with a cps limit.

Before intensity adjustment, confirm the applicable Total limit for the current SPring-8 bunch mode: approximately 100000 cps for longer bunch spacing or 60000 cps for shorter bunch spacing. If the applicable limit is unclear, confirm it with BL14B2 staff before increasing intensity. Introduction.md, Section 5.2.2 explains the two statistics and bunch-mode dependence.

1. Replace the sample with the one to be measured.
2. Ensure that the 19SSD is at the farthest position from the sample and that the 4D slit width is set to the minimum.
3. Open [DSP Tools.exe] on the desktop, and open [SSD Intensity Monitor].
4. Open DSS, click [Start Measurement], and check the counts in the ROI column and the Total column after the signal appears.
5. If the average count rate in the Total column exceeds the applicable bunch-mode limit, or detector overflow occurs, immediately close DSS. The applicable limit is approximately 100000 cps for longer bunch spacing or 60000 cps for shorter bunch spacing; do not always use 100000 cps as the limit.
6. If the signal is too strong, place a filter in front of the 19SSD or re-adjust the sample conditions.
7. Carefully and gradually increase the 4D slit size, and slowly move the 19SSD closer to the sample.
8. After each adjustment, click [Start Measurement] again and check the counts in the ROI column and the Total column.
9. Aim to increase the ROI (SCA) count rate as far as possible while keeping Total (ICR) below the applicable overflow limit. Around 70000 cps in Total is a general operational reference, not a mandatory target. When the applicable limit is approximately 60000 cps, keep Total below that limit rather than increasing it to 70000 cps.
10. When moving the 19SSD, be extremely careful not to let the 19SSD collide with the sample stage. The window material of the 19SSD is Be. If the Be window is broken, highly toxic powder may be generated.
11. When controlling the 19SSD movement using [PM16C Move.vi], always monitor the camera image and be prepared to stop the movement immediately.
12. If remote operation feels unsafe, enter the hutch and manually move the 19SSD closer to the sample.
13. After the experiment, make sure to return the 19SSD to its original position.
14. After adjusting the 4D slit, reacquire the GAIN value if necessary.

##### 5.2.2.4. Fluorescence Mode Scan Mode

1. Select QXAFS or Step XAFS.
2. If the measured spectrum is obviously distorted, try reducing the beam width (horizontal width of the 4D slit; see Section 9.2.1) and check whether the spectrum improves.

##### 5.2.3.0. CEY Mode Preconditions

1. Wait until the staff has completed the setup of the sample cell and the related detector wiring.
2. Confirm that the current amplifier for I1 is in local mode and that zero check is enabled. If not, switch it to local mode and enable zero check.
3. In [PM16C Move.vi], use channel “Sample Lin.” and channel “Sample Theta” to adjust theta to 5–10°, and place the sample on the X-ray beam path.
4. Check the sample position using the red laser.
5. Flow He at 300 ccm for 20 s, observe whether the Kapton film on the window rises, and confirm whether the cell cover is properly closed.
6. Apply high voltage to the electrode. Turn on section A of [ORTEC 660], confirm that the voltage is 0, and press [RESET].
7. Slowly turn the knob until the voltage reaches -500 V. At this stage, high voltage is applied to the cell. Do not touch the cell manually.
8. Activate [Auto Amp Tune].
9. Confirm that the current monochromator angle, namely the value shown on the encoder, corresponds to an energy above the absorption edge of the target element. If not, move the monochromator angle using [Theta Move.vi].
10. Leave the hutch and open DSS.
11. Select an appropriate 4D slit size, and adjust the GAIN value of the current amplifier so that the CEY signal is within the range of -0.5 to -10.
12. Read the values of channel “Sample Lin.” and channel “Sample Theta” in [PM16C Move.vi].
13. Based on these values, perform scans using channel “Sample Theta” and channel “Sample Lin.” in [PM16C Scan.vi], and obtain the “Sample Lin.” and “Sample Theta” values where the signal intensity is the highest.
14. Use [PM16C Move.vi] to move the sample to the corresponding position.

##### 5.2.3.1. CEY Mode Scan Mode

1. Select QXAFS or Step XAFS.

##### 5.2.3.2. Sample Exchange in CEY Mode

1. Stop the He gas flow.
2. Make sure to reduce the voltage of [ORTEC 660] to 0.
3. Make sure to switch the I1 current amplifier hardware to local mode and enable zero check mode.
4. Note that if [Auto Amp Tune] is activated, the current amplifier will automatically enter remote mode and zero check will be disabled.
5. Open the cell cover and replace the sample.

---

## 6. Measurement Mode

### 6.2. Reference

#### 6.2.1. Quick XAFS (QXAFS) Measurement Mode

1. Ensure that all other software has been stopped, that no person is inside the hutch, and that the DSS interlock key is enabled.
2. Open [BL14B2 Control.vi], select [QXAFS MADOCA], and click the white Run arrow.
3. Click the white Run arrow in [QXAFS.vi].
4. Select [Data Holder Path]. This setting determines the server location where the data will be stored. After selecting the path, confirm in the browser-based [QXAFS monitor] that the path has been updated. If it has not been updated, select the path again.
5. Input [File Name] and [Comment]. Do not use special symbols, full-width characters, or spaces. After inputting them, confirm in the browser-based [QXAFS monitor] that the file name and related information have been updated. If they have not been updated, input them again.
6. Under [Control], select [Manual], and select the corresponding absorption edge under [edge].
7. Input the pre-edge distance in [preoffset] in eV, and input the post-edge distance in [K] in Å^-1. Confirm in [Scat start] and [End] that the theta angles have been updated to the corresponding pre-edge and post-edge positions. If the scan range exceeds the allowed upper limit, [Start] becomes gray. In this case, adjust the scan range again.
8. Input the [Dwell] time. For fluorescence mode, the dwell time must be at least 11 ms (≥11 ms; 11 ms is included). If the dwell time is outside the allowed range, [Start] becomes gray. In this case, set the dwell time again.
9. After inputting the scan range and [Dwell], the total time required for one loop is displayed. Since a loop cannot be forcibly stopped once it starts, for samples that require long measurement times, reduce the dwell time and increase the number of loops. The number of repeated measurements can be input in [Loop]. Between loops, the measurement can be stopped using [Stop Loop].
10. Select the required measurement method, such as [Transmission], [FY (19SSD)], or [CEY], and then select the corresponding counter. For example:
   - [trans]; uses the I0 and I1 ion chamber detectors
   - [trans + std]; uses the I0, I1, and I2 ion chamber detectors
   - [FY]; uses the I0 ion chamber detector and the 19SSD
   - [FY + trans]; uses the I0 and I1 ion chamber detectors and the 19SSD
11. Confirm [measure Dark]. If it is ON, the dark current will be measured again at the beginning of the measurement. If it is OFF, the previously measured dark current values will be used.
12. If the data format needs to be changed, set [Data Convert] to ON, and then confirm the appropriate [File format].
13. Click [Start] to begin the measurement. The software will then ask the user to select the data storage location on the user drive. This drive is different from the first server path, so the folder path must be created again if necessary.
14. After confirming the storage location, do not change the file name. Click [OK].
15. The graph in the software will be plotted only after one loop has been completed.
16. Once a loop starts, the loop must not be forcibly terminated. Only the start of the next loop can be stopped.
17. After all measurements are completed, DSS will close automatically, the red [Finish] lamp on the QXAFS GUI will turn ON, and the black Run arrow at the top of the GUI will turn white, indicating that the program has ended.

##### 6.2.1.1. Troubleshooting When Quick XAFS (QXAFS) Measurement Mode Does Not End Automatically

Normally, after a QXAFS scan is completed, DSS closes automatically, the red [Finish] lamp on the QXAFS GUI turns ON, and the black Run arrow at the top of the GUI turns white, indicating that the program has ended.
However, if there is an error in the data path or file name format, or if the file path or file name in the GUI is not consistent with those in the browser-based [QXAFS monitor], a bug may occur.
The symptom is as follows:
- DSS closes automatically, and the page log shows “measurement complete”, but the green [Waiting] lamp on the QXAFS GUI remains ON and does not change to the red [Finish] lamp. The Run arrow at the top of the GUI also remains black, indicating that the program is still running.
In this case, confirm the following:
- Whether there is an error in the file path or file name in the QXAFS GUI.
- Whether the file path or file name in the QXAFS GUI is inconsistent with those in the browser-based [QXAFS monitor].
- Whether the encoder value is still changing.
- Whether DSS has been closed.
- Whether the log on the [QXAFS] page shows that theta has returned, the settings have been restored, and the final message is “measurement complete”.
Only after confirming that the scan has ended, theta has returned to its initial matched position, DSS has closed, the log shows restored settings and “measurement complete”, and the non-ending state is caused by the path or filename problem, click the red circle on the QXAFS GUI to terminate [QXAFS.vi].
Close the current window and reopen it. The measurement can then be performed normally.

##### 6.2.1.2. Terminating QXAFS Before Theta Movement Starts

1. Confirm that theta movement for the scan has not started. A theta value that has merely stopped changing after movement is not sufficient evidence for this branch.
2. If the pre-movement state is confirmed and program termination is required, use the red circle on the QXAFS GUI to terminate [QXAFS.vi].
3. If theta movement has started, do not use this branch. Wait for scan completion and return to the initial matched position; for the documented non-ending state, use Section 6.2.1.1.

#### 6.2.2. Step Measurement Mode

1. Ensure that all other software has been stopped, that no person is inside the hutch, and that the DSS interlock key is enabled.
2. Open [BL14B2 Control.vi], select [XAFS Measure new], and click the white Run arrow.
3. In the launched [XAFS Measure.vi], click the white Run arrow at the top to start the program.
4. Input [Sample Name].
5. Select [Counter setting], such as [Transmission] or [Fluorescence (19SSD)].
6. Set the step scan parameters, including the absorption edge, the pre-edge [preoffset] in eV, and the post-edge [K] in Å^-1. If a parameter file has already been prepared, use [Read] to load it directly. The parameter file can be created using [XASparam.exe] on the desktop.
7. If necessary, modify the parameter values. For example, perform a test measurement with a very small number of points, such as 5 points in the first step region and 10 points in the second step region.
8. Click [file copy] and select the BL14 server drive location where the data will be saved.
9. Click [OK] to start the measurement.
10. After starting the measurement, select the data storage location on the user drive again.
11. After the measurement is completed, the window will ask whether to return the monochromator theta to the initial position or specified position. Click [OK] to confirm. If [Cancel] is clicked, the monochromator will not move, and the measurement will end.
12. Unlike Quick XAFS Measurement Mode, Step Measurement Mode can be interrupted by clicking [Stop].

---

## 7. Sample Requirement

### 7.2. Reference

This chapter does not define a universal sample preparation procedure.

Sample preparation depends strongly on:

- sample composition
- sample concentration
- sample quantity
- sample processability
- selected measurement method
- selected experimental environment

Before preparing samples, users should complete the following compatibility evaluation workflow:

1. Determine the measurement method according to Chapter 5 of the Introduction file.
2. Determine the measurement mode according to Chapter 6 of the Introduction file if relevant.
3. Select the experimental environment.
4. Check sample dimensional requirements according to Chapter 7 of the Introduction file.
5. Confirm compatibility with the selected sample holder or experimental setup.
6. Consult BL14B2 staff if compatibility is uncertain.

Users should consult BL14B2 staff when:

- sample dimensions exceed documented recommended limits
- sample mounting compatibility is uncertain
- sample thickness exceeds recommended values
- a user-defined experimental environment will be installed
- safety compatibility is unclear

Because sample preparation is sample-dependent, users should refer to the corresponding Introduction Reference Layer for detailed requirements.

For the high-pressure transmission cell, refer to Introduction Sections 13.2.2.1 and 13.2.2.2 for holder dimensions and sample compatibility, and to SOP Section 13.2.2 for powder loading under staff guidance.

---

## 8. Operation of PM16C

### 8.2. Reference

#### 8.2.1. Operation of PM16C Read/Move

Steps 1–8 read the position. Continue to Steps 9–16 only when movement is intended.

1. Open "BL14B2 Control2.vi".
2. Select:
   - PM16C Move
3. Click the white Run button.
4. Select the desired motor channel.
5. Select the position unit:
   - mm
   - degree
6. Select:
   - Read
7. Click the white Run button.
8. Confirm the current motor position shown in:
   - Present Position
9. Select:
   - Move
10. Enter the target position in:
    - Input Position
11. Click the white Run button.
12. Confirm motor motion using:
    - Present Position
    - CCD camera (if available)
13. Do not change the motor channel during movement.
14. Wait until motion is completed.
15. Confirm that the Run button changes from black to white.
16. If movement must be interrupted:
    - Press the Stop button inside PM16C Move.
    - Do not use the LabVIEW red stop button.

##### 8.2.1.1. Recovery from Physical Limit Error

If the motor reaches a physical limit before reaching the commanded position:

Example:

- Commanded position: 10
- Physical limit reached at: 5

In this situation:

- Present Position may continue changing.
- The motor may stop moving physically.

Recovery procedure:

1. Press Stop.
2. Turn off motor power.
3. Enter the actual physical limit position.
   Example:
   - Input Position = 5
4. Execute Move.
5. Allow the software position to update until it matches the actual motor position.
6. Turn on motor power.
7. Verify normal operation.

#### 8.2.2. Operation of PM16C Scan

1. Open "BL14B2 Control2.vi".
2. Select:
   - PM16C San
3. Click the white Run button.
4. Select the desired motor channel.
5. Select the:
   - mm/degree
6. Read the current motor position using PM16C Move.
7. Configure the scan range.
   - Start Position
   - Dest. Position
8. Set:
   - Measure Start
   slightly lower than Start Position.
9. Configure scan parameters as required.
   Examples:
   - Step
   - Dwell Time
10. For fluorescence measurements:
    - Set 19SSD Counter = DSP
    - Enter the Absorption Edge
    - Verify that the current angle can generate fluorescence signal
11. Open DSS.
12. Start the scan using the white Run button.
13. Wait until the scan finishes.
14. Confirm that the Run button changes from black to white.
15. Close DSS.
16. Read the desired position from the scan result.
17. Use PM16C Move to move to the selected position.

#### Operational Notes

- Always read the current motor position before movement.
- Always verify movement direction before large motions.
- Never change channels while a motor is moving.
- Use the PM16C Stop button for emergency stops.
- Do not use the LabVIEW red stop button as a motor stop command.
- PM16C Scan does not automatically control DSS.
- DSS must be opened and closed manually.
- For fluorescence scans, 19SSD Counter must be set to DSP.
- For fluorescence scans, the Absorption Edge must be entered correctly.

---

## 9. Operation of 4D slit

### 9.2. Reference

#### 9.2.1. Operation of 4D slit Read/Move

Steps 1–7 read the slit settings. Continue to Steps 8–14 only when movement is intended.

1. Open "BL14B2 Control2.vi".
2. Select:
   - 4D slit Move
3. Click the white Run button.
4. In "4D slit Move.vi" Select the position unit:
   - mm
5. Select:
   - Read
6. Click the white Run button.
7. Confirm the current motor position shown in:
   - Width Set
   - Heigh Set
8. Select:
   - Move
9. Enter the target position in:
    - Input Position
10. Click the white Run button.
11. Confirm motor motion using:
    - Present 
12. Wait until motion is completed.
13. Confirm that the Run button changes from black to white.
14. If movement must be interrupted:
    - Press the Stop button inside 4D slit Move.
    - Do not use the LabVIEW red stop button.

#### 9.2.2. Operation of 4D slit Scan

1. Open "BL14B2 Control2.vi".
2. Select:
   - 4D slit Scan
3. Click the white Run button.
4. Select the desired Axis channel.
   - horizontal
   - vertical
5. Select the:
   - mm
6. Read the current motor position using 4D slit Move.
7. Configure the scan range.
   - Start Position
   - Dest. Position

8. Set:
   - Measure Start
   slightly lower than Start Position.
   - Height mm
   - Width mm
9. Configure scan parameters as required.
   Examples:
   - Step
   - Preset(sec)
10. Open DSS.
11. Start the scan using the white Run button.
12. Wait until the scan finishes.
13. Confirm that the Run button changes from black to white.
14. Close DSS.
15. Read the desired position from the scan result.
16. Use 4D slit Move to move to the selected position.

#### Operational Notes

- Always read the current motor position before movement.
- Never change channels while a motor is moving.
- Use the 4D slit Stop button for emergency stops.
- Do not use the LabVIEW red stop button as a motor stop command.
- 4D slit Scan does not automatically control DSS.
- DSS must be opened and closed manually.

---

## 10. Operation of MBS/DSS

### 10.2. Reference

#### 10.2.1. Main Beam Shutter (MBS) Local Operation

1. Confirm that the key on the interlock control panel of the optics hutch is set to:
   - Enable
   This is normally the default condition.
   In general, users are not allowed to operate the interlock control panel of the optics hutch.
2. On the interlock control panel of the experimental hutch, select the tab at the bottom of the screen:
   - Optics Hutch
3. Find the MBS icon on the screen and click it.
4. Select:
   - Open
   - Close
5. Click:
   - Enter
6. Confirm on the screen that MBS has been opened or closed in the beam path.
7. Confirm the lamp status on the interlock control panel.
   If MBS is open:
   - the red "Running" lamp on the optics hutch interlock control panel is ON
   - the light-green "Ready" lamp on the experimental hutch interlock control panel stops flashing
   If MBS is closed:
   - the light-green "Ready" lamp on the optics hutch interlock control panel is ON
   - the light-green "Ready" lamp on the experimental hutch interlock control panel flashes

#### 10.2.2. Downstream Shutter (DSS) Local Operation

1. Confirm that the key on the interlock control panel of the experimental hutch is set to:
   - Enable
2. On the interlock control panel of the experimental hutch, select the tab at the bottom of the screen:
   - User
3. Find the DSS icon on the screen and click it.
4. Select:
   - Open
   - Close
5. Click:
   - Enter
6. Confirm on the screen that DSS has been opened or closed in the beam path.
7. Confirm the lamp status on the interlock control panel.
   If DSS is open:
   - the red "Running" lamp on the experimental hutch interlock control panel is ON
   If DSS is closed:
   - the light-green "Ready" lamp on the experimental hutch interlock control panel is ON

#### 10.2.3. Downstream Shutter (DSS) Remote Operation

1. Open [BL14B2 Control2.vi].
2. Select:
   - DSS
3. Click the white Run button.
4. In [DSS.vi], select:
   - Open
   - Close
5. Click the white Run button.

---

## 11. Cryostat Experiment

### 11.2. Reference

#### 11.2.1. Sample Stage and Cold Head Preparation for Cryostat Experiment

1. Determine the measurement method.
   - Transmission Measurement
   - Fluorescence Measurement
2. Receive training on how to use the corresponding cryostat sample stage.
3. Receive training on how to adjust the angle of the cryostat cold head.
   Basic angle selection:
   - 45°: fluorescence measurement
   - 90°: transmission measurement
   To change the cold head angle:
   - loosen the two knobs located above the cold head and below the vent valve
   - rotate the cold head
   - tighten the knobs again to fix the cold head angle
4. Receive training on how to install the sample stage.
   During sample stage installation:
   - In foil may be used to improve the contact area between the cold head and the sample stage and enhance thermal conduction.
   - Be careful with the temperature sensor wiring because the sensor wires are very thin.
   - Ensure that the temperature sensor wires do not block the X-ray beam path.
5. After installing the sample stage, select the appropriate cover.
   - transmission cover
   - fluorescence cover
6. Attach the cover and fix it with screws.

#### 11.2.2. Vacuum Evacuation and Cooling for Cryostat Experiment

1. Confirm that the following valves on the cryostat body are closed:
   - main vacuum valve
   - vent valve
2. Turn on the power switch of the vacuum pump.
3. On the control panel, press:
   - VP
4. On the control panel, press:
   - VALVE
   This opens the electronic vacuum valve.
5. When the vacuum gauge reading becomes lower than:
   - 5 × 10^0 Pa
   slowly open the main vacuum valve on the cryostat body.
6. When the vacuum gauge reading again becomes lower than:
   - 5 × 10^0 Pa
   press the following button on the control panel:
   - TMP
   This starts the turbomolecular pump.
7. When the vacuum gauge reading becomes lower than:
   - 2 × 10^-2 Pa
   turn on the refrigerator power.
   If an alarm occurs because the refrigerator operating time has exceeded 500 h:
   - press Alarm Reset to clear the alarm
   - notify BL14B2 staff to clean the filter
8. After the refrigerator has been turned on, turn on the compressor power.
   Cooling starts.
9. After cooling starts, turn on the power of the dedicated cryostat heater controller.
10. On the dedicated cryostat heater controller, press:
    - SETPOINT
    The cursor on the control panel moves to:
    - SetP
11. Enter the target temperature and press:
    - ENTER
    This changes the set temperature.
12. Press:
    - Heater Range
13. Use the up/down buttons to set the heater power to:
    - High
14. Confirm that the lamp to the left of:
    - ALL OFF
    is red.
    This indicates that the heater is operating.

#### 11.2.3. Measurement During Cryostat Experiment

1. Use the cryostat channels in PM16C Move and PM16C Scan to align the sample with the X-ray beam path.
2. Perform the measurement using the selected measurement method by QXAFS.
   - Transmission Measurement
   - Fluorescence Measurement

#### 11.2.4. Finishing Cryostat Experiment

##### 11.2.4.1. Stop the Dedicated Cryostat Heater Controller

1. Press [SETPOINT].
2. Set CHANNEL B (sample-holder temperature) to 300 K.
3. Press [HEATER RANGE], select [High], and press [ENTER].
4. When the cryostat temperature reaches 300 K, press [ALL OFF]. Confirm that the lamp to the left of [ALL OFF] goes out, indicating that the heater has stopped.

##### 11.2.4.2. Stop the Compressor

1. Press the compressor power switch to stop the compressor and cryostat cooling.
2. Keep cooling water circulating for 30 minutes after the compressor stops. The device that remains operating for this period is the cooling-water circulator.

##### 11.2.4.3. Stop the Vacuum Pumps

1. Press [Auto Operation] on the touch panel to switch to Hand Operation.
2. Press [VALBE] on the touch panel to close the electromagnetic vacuum valve.
3. Press [TMP] to stop the turbomolecular pump.
4. Confirm that the [DEC] lamp on the TMP power supply has gone out, then press [VP] to stop the scroll pump.
5. Set the vacuum-pump power switch to OFF. The vacuum-pump shutdown is complete.

##### 11.2.4.4. Stop the Cooling-Water Circulator

1. Confirm that the vacuum-pump shutdown is complete and that cooling water has continued circulating for 30 minutes after compressor shutdown.
2. Set the cooling-water circulator power switch to OFF.

##### 11.2.4.5. Remove or Exchange the Sample

1. Confirm that the cryostat temperature is sufficiently close to room temperature.
2. Confirm that vacuum can be safely released.
3. Remove or exchange the sample.

---

## 12. HummingBird Automatic Measurement

### 12.2. Reference

#### 12.2.1. User Operations When HummingBird Is Idle

1. When HummingBird is idle, users may exchange samples by themselves.

2. When HummingBird is idle, users may move HummingBird away from the X-ray beam path if other measurements need to be performed.

3. Before moving HummingBird, record the current HummingBird position at the edge of the experimental table.

4. Use the recorded position to return HummingBird to its original position when necessary.

#### 12.2.2. Preconditions Before User Operation

1. Before users operate HummingBird, wait until BL14B2 staff has completed the required SPEC login.

2. Wait until BL14B2 staff has completed the required HummingBird calibration.

#### 12.2.3. Pickup and Return of a Single Sample

A single sample can be picked up and returned using either SPEC commands or the [XAFS_HummingBird] GUI.

##### 12.2.3.1. Method 1: SPEC Command Operation

1. To pick up a sample, input the following command in the SPEC command window and press Enter:
   
   ```text
   load number
   ```
   Here, `number` is the sample position to be picked up.
   
   Examples:
   
   ```text
   load 1
   load 2
   ```
2. To return a sample to a specific position, input the following command in the SPEC command window and press Enter:

   ```text
   unload number
   ```

   Here, `number` is the sample position to which the sample should be returned.

   Examples:

   ```text
   unload 1
   unload 2
   ```
3. For fluorescence measurements under the 45° condition, use the following command to pick up a sample:

   ```text
   load_45 number
   ```
4. The return command is unchanged.

   ```text
   unload number
   ```

##### 12.2.3.2. Method 2: GUI Operation

1. In the [XAFS_HummingBird] GUI, click:
   - Individual Measurement
   The GUI should already have been opened during the previous staff operation.
2. In the popup window, enter the sample position.
3. Click:
   - OK
4. When the popup asks whether amp tune is required, select:
   - No
5. The robot arm picks up the sample automatically.
6. To return the sample, click:
   - Return Sample
#### 12.2.4. Continuous Automatic Measurement

1. Confirm that the samples have been placed in the sample holder.
2. Confirm that the sample holder has been fixed on HummingBird.
3. Confirm that the sample size is acceptable and will not interfere with robot-arm motion.
4. Exit the hutch.
5. Confirm that the interlock key is set to:
   - Enable
6. Fill in the dedicated Excel file for importing HummingBird parameters.
7. Refer to the comments in the column titles of the Excel file.
   These comments include:
   - input requirements
   - explanations
   - examples
8. Fill in the Excel file according to the standard format.
9. Confirm that the Excel macro is enabled.
10. After completing the Excel file, click:
   - Upload
11. After the upload is completed, click the following button in the [XAFS_HummingBird] GUI:
    - Continuous Measurement
12. After clicking [Continuous Measurement], the sample list is imported into the SPEC command window.
13. Confirm that the sample list is correct.
14. After confirming the sample list, click:
    - OK
15. After the measurement is completed, close the GUI window if necessary.
    Do not close the SPEC command window.

---

## 13. In-situ Cells Provided by BL14B2

### 13.2. Reference

#### 13.2.1. Position Adjustment of In-situ Cells

1. Confirm that no sample is installed in the in-situ cell.
2. Use the rear red laser to adjust the height of the in-situ cell manually.
3. Confirm that the in-situ cell window is at the same height as the red laser.
4. If the sample stage reaches the manual adjustment limit, connect the power supply for the Z-direction motor.
5. Use the following channel in [PM16C Move.vi] to continue height adjustment:
   - General Z
6. Adjust the horizontal position of the in-situ cell.
   If the X-direction motor is not powered:
   - manually rotate the knob at the end of the motor to move the in-situ cell
   If the X-direction motor is powered:
   - use the following channel in [PM16C Move.vi]:
     - General X
7. Confirm that the red laser enters from the rear side of the in-situ cell and exits from the front side.
8. Cover the red laser with its cover.
9. Exit the hutch.
10. Set the DSS interlock key to:
    - Enable
11. Open DSS.
12. Confirm that X-direction motor and Z-direction motor are powered. Use the following channels in [PM16C Move.vi] and [PM16C Scan.vi] to search for the position where I1 intensity becomes maximum:
    - General Z
    - General X
13. Move the in-situ cell to the position where I1 intensity is maximum.
14. After the in-situ cell position adjustment is completed, repeated position adjustment is generally not required during the same experiment.

#### 13.2.2. Powder Loading into the High-Pressure Cell Sample Holder

This procedure covers powder loading into the sample holder under staff guidance. It is not a complete procedure for cell installation, sealing, pressurization, depressurization, or opening.

Preconditions:

- Use the specified high-pressure-cell holder. Refer to Introduction Sections 13.2.2.1 and 13.2.2.2 for dimensions, sample thickness, and preparation considerations.
- For a user-provided holder, consult BL14B2 staff in advance and obtain confirmation of compatibility before use.
- Perform sample loading on site under staff guidance.

Loading sequence:

1. Place one quartz film at the bottom of the sample holder before adding powder.
2. Load the powder sample into the holder and compact it manually using a stainless-steel rod.
3. After filling, place one quartz film on top of the sample to prevent powder from scattering under gas flow.

Preformed pellets require separate confirmation of stable retention as described in Introduction Section 13.2.2.2. This powder-loading procedure does not define a pellet-fixing method.

---

## 14. In-situ Cell Heating Controller

### 14.2. Reference

#### 14.2.0. Initial Gain Confirmation

1. Turn on the heating controller.
2. Before starting heating, confirm that the GAIN setting matches the in-situ cell to be used.
   - Transmission-Type In-situ Cell up to 1000 °C: GAIN 0.52
   - Fluorescence-Type In-situ Cell up to 600 °C: GAIN 0.52
   - Transmission-Type High-Pressure In-situ Cell up to 700 °C: GAIN 0.54

#### 14.2.1. Pre-Operation Preparation for In-situ Cell Heating Controller

This preparation is generally performed by BL14B2 staff.
1. Press:
   - MODE
   to enter the menu screen.
2. Use the Up / Down buttons to confirm that MODE 0–11 do not display:
   - LocK
3. If "LocK" is displayed for any MODE, use the Left / Right buttons to cancel the lock for that MODE.
4. Use the Up / Down buttons to select:
   - MODE 1
5. Press:
   - SEL
   to enter the submenu of MODE 1.
6. In [FUNCTION KEY], confirm whether "LocK" is displayed.
7. If "LocK" is displayed, use the Left / Right buttons to cancel the lock.
8. Press:
   - ENT
   to confirm the setting.
9. Press:
   - MODE
   to return to the main menu.
10. The parameters of PID NO.09 are configured by BL14B2 staff. Users do not edit those underlying PID parameters.
11. Users select the configured PID NO.09 for every STEP as described in Section 14.2.2. Contact BL14B2 staff if the underlying PID parameters need attention.

#### 14.2.2. Setting an In-situ Cell Heating Pattern

Important note:

- After each setting value is changed, a "?" mark appears on the control panel.
- The changed value is not confirmed until [ENT] is pressed.
- Always press [ENT] to confirm each setting change.

1. Press:
   - MODE
   to enter the menu screen.
2. Use the Up / Down buttons to select:
   - MODE 2
3. Press:
   - SEL
   to enter the submenu of MODE 2.
4. Select the PTN to be created or modified.
   Example:
   - PTN 01
5. Press:
   - SEL
   to enter the setting menu of the selected PTN.
6. In the PTN setting menu, confirm that:
   - STEP = 00
   This indicates the initial starting condition.
7. Use the Left / Right buttons to move the cursor.
8. At SV or PV, use the Up / Down buttons to select the starting temperature condition.
   Examples:
   - SV XX °C
   - PV
9. At STEP, use the Up / Down buttons to move to the next STEP.
10. For each STEP, set the required values.
    - SV: target temperature
    - TIME: duration
11. The time format is:
    - h:min
12. The maximum time setting is:
    - 999:59
13. Repeat the same procedure until all STEP settings have been completed.
14. At the final STEP, move the cursor to TIME.
15. Use the Up / Down buttons to change the time setting from h:min to:
    - END
    - LINK00
16. LINK means that another PTN starts immediately after the current PTN ends.
    Example:
    - END/LINK01
    This means that PTN 01 will be executed immediately after the current PTN ends.
17. After creating or editing the pattern, enter every STEP screen again. Newly added STEPs may retain a default PID selection instead of NO.09.
18. Press SEL repeatedly to enter the PID setting subpage for each STEP.
19. Confirm that the PID setting is:
    - NO.09
20. If the selected PID number is not NO.09, use the Up / Down buttons to select NO.09. Do not edit the parameters stored in PID NO.09.
21. Press:
    - ENT
    to confirm the PID setting.
22. Press:
    - MODE
    to return to the main menu.
23. Press:
    - MODE
    again to enter the execution screen.

#### 14.2.3. Executing an In-situ Cell Heating Pattern

1. Press:
   - MODE
   to switch to the execution screen.
2. Press:
   - FNC
3. Press:
   - PTN
4. Confirm that the PTN value on the control panel starts blinking.
5. Use the Up / Down buttons to select the PTN to be executed.
6. Press:
   - ENT
   to confirm the selected PTN.
7. Use the following execution-command buttons as required.
   FNC:
   - activates the upper-row execution-command functions
   FNC + RUN:
   - starts the selected heating pattern
   FNC + STOP:
   - pauses the heating pattern at the current condition
   FNC + ADV:
   - skips the current step
   FNC + RESET:
   - cancels the entire heating pattern

---

## 15. BL14B2 Gas Supply System

### 15.2. Reference

#### 15.2.1. N2 Purge Before Opening the Gas Path

Before opening a gas path or exchanging a sample after reaction-gas use, apply the documented purge condition:

| Parameter | Required setting |
| --- | --- |
| Purge gas | N2 |
| Flow rate | 100 ccm |
| Duration | 15 min |

Use the approved gas-path configuration for the purge. This section does not specify valve sequencing, pressure release, temperature criteria, or verification that the system is ready to open. Obtain these instructions from BL14B2 staff or the approved procedure before opening the system.

#### 15.2.2. Response to Gas-System Alarms

This section specifies the responses to the four alarm categories described in Introduction.md, Section 15.2.5. Use the subsection corresponding to the identified alarm category.

- If the alarm category is unclear, do not guess or downgrade it. Follow the on-site emergency instructions and contact BL14B2 staff or safety personnel.
- Routine MFC software commands are not a substitute for alarm response.
- Experimenters must not enter the affected area to investigate leaks or carry out repairs. Investigation and corrective actions remain with the designated personnel.
- Re-entry, interlock recovery, and experiment restart require the designated personnel and applicable procedures. Do not restart solely because an alarm stops or a display returns to normal.
- This section does not specify detailed repair, interlock-reset, or complete equipment-restart steps. Obtain any required instructions from BL14B2 staff or safety personnel; do not infer missing steps.

Each subsection separates system behavior from experimenter actions and actions assigned to safety personnel and staff.

##### 15.2.2.1. Gas Leak

Automatic system response (for recognition):

- The interlock stops reaction-gas supply.
- Beamline staff and safety personnel are automatically notified.

Experimenter response:

1. If fire or injury occurs, contact the guard station using the documented internal emergency number, 119.
2. Warn nearby beamlines, passersby, and people in side rooms to leave the experimental hall. Evacuate without entering the affected area to investigate.
3. Notify the experiment's responsible person if absent, and report the situation to the Safety Office.

Safety-personnel and staff response:

- Entry and investigation are performed by two safety personnel equipped with breathing apparatus and portable gas detectors.
- Safety personnel inspect the area, investigate the leak, address necessary repairs, and check gas concentrations before granting permission to re-enter.
- Beamline staff subsequently report details to the Safety Office.

##### 15.2.2.2. Severe Fault

Automatic system response (for recognition):

- The interlock stops reaction-gas supply.
- Beamline staff and safety personnel are automatically notified.

Experimenter response:

1. If fire or injury occurs, contact the guard station using the documented internal emergency number, 119.
2. Warn nearby beamlines, passersby, and people in side rooms to leave the experimental hall. Evacuate without entering the affected area to investigate.
3. Notify the experiment's responsible person if absent, and report the situation to the Safety Office.

Safety-personnel and staff response:

- Entry and investigation are performed by two safety personnel equipped with breathing apparatus and portable gas detectors.
- Safety personnel inspect the area, investigate the cause, address necessary repairs, and check gas concentrations before granting permission to re-enter.
- Beamline staff subsequently report details to the Safety Office.

##### 15.2.2.3. Moderate Fault

Automatic system response (for recognition):

- Reaction-gas supply stops automatically.
- Beamline staff and safety personnel are notified.

Experimenter response:

1. Notify the experiment's responsible person if absent.
2. Follow the emergency manual for experiment-stop measures, including stopping cell heating where applicable. Do not enter an unsafe area to carry out these measures.
3. Wait for confirmation that the abnormal condition has been resolved and restart is permitted.

Safety-personnel and staff response:

- Safety personnel investigate the cause and check the equipment condition.
- If dilution N2 is depleted, cylinder replacement and verification are handled under the authorized procedure.
- Beamline staff subsequently report details to the Safety Office.

##### 15.2.2.4. Minor Fault

System response (for recognition):

- A buzzer sounds.
- A gas-detector fault triggers automatic notification to beamline staff and safety personnel.
- The reaction-gas cylinder main valve is not automatically emergency-closed for this category.

Experimenter response:

1. For faults other than the automatically notified gas-detector fault, contact beamline staff or safety personnel.
2. Notify the experiment's responsible person if absent.
3. Resume only after equipment condition and restart permission have been confirmed.

Safety-personnel response:

- Investigate the cause and address the problem before restart.

#### 15.2.3. Operation of MFC_multi_control_fixed2.vi

##### 15.2.3.1. Open the Program and Read the Current Status

1. Open MFC_multi_control_fixed2.vi from the desktop.
2. Click the white arrow on the toolbar to read the current status before editing the settings.

If the displayed gas-line assignment or current status is unclear, consult BL14B2 staff before changing values.

##### 15.2.3.2. Set or Start Gas Flow

Before setting a reaction-gas flow, use the gas composition, flow rates, dilution condition, and concentration limits approved for the applicable abatement-system configuration. The gas-detector alarm thresholds are for monitoring exhaust after abatement; they are not allowable user-gas concentrations or flow-planning limits. Do not derive a maximum reaction-gas flow from those alarm thresholds. If the applicable abatement conditions or their calculation basis are unclear, consult BL14B2 staff before entering or starting a flow.

1. Enter the required value in SV for the selected gas line. The unit is ccm.
   - The gas name displayed for the line is the MFC calibration gas.
   - If the connected gas differs from the calibration gas, calculate the corrected setting using the applicable conversion guidance before entering SV.
2. In Balve State, change Close to Open.
3. If required, repeat Steps 1 and 2 for other approved gas lines before writing the settings.
4. Click write next to ガス混合器.
5. Click the white arrow on the toolbar to execute the configured MFC commands.

##### 15.2.3.3. Stop Gas Flow and Close the Selected Line

1. Set SV to 0 for the selected gas line.
2. In Balve State, change Open to Close.
3. Click write next to ガス混合器.
4. Click the white arrow on the toolbar to execute the configured MFC commands.

This procedure closes the selected MFC-controlled line. It does not define cylinder shutdown, depressurization, purging, or complete system isolation.

##### 15.2.3.4. Verification and Escalation

Confirm the resulting status using the MFC controller readback. As described in Introduction, use the adjacent MFC controller display as the reference if software values disagree.

If the commanded state is not reflected, flow remains abnormal, or the readback is unclear, contact BL14B2 staff. Do not assume that a completed software command proves that flow has stopped or that the system is safe to open.

If an interlock alarm occurs, follow Section 15.2.2 and the approved emergency manual rather than attempting recovery through routine MFC commands.
