# Introduction

Version: v2.14
Revision date: 2026-11-06
Content status: Authoritative BL14B2 reference content.
Structure status: Independent reference document with its own navigation index; shared assistant behavior is maintained in the skill entrypoint.
Applies to: BL14B2 users and AI-assisted guidance

## Internal Topic Index

Internal navigation only. Use the named Reference passages; do not output this table or its identifiers to users. Related terms route a question and do not assert that the terms are synonymous.

| Names and related query terms | Explanation reference | Operation reference or coverage |
| --- | --- | --- |
| Optics; Auto Optics; Si(311); rocking curve; Δθ; mechanical stress; 光学调整; 摇摆曲线; 机械应力; ロッキングカーブ | Introduction 1.2 | SOP 1.2, 1.2.6 |
| EXAFS k–E conversion; photoelectron wavenumber; 波数; 波数与能量转换 | Introduction Global Definitions: EXAFS k–E conversion | Mathematical conversion only; not QXAFS–Step correction |
| Absorption-edge energy; fluorescence-line energy; 吸收边; 荧光线能量 | Introduction 7.2.6 | JIN returned energy fields; not a detector-setting procedure |
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
| JIN; XAFS Absorption Calculation Assistant; 吸收计算助手 | Introduction 7.2.6 | Public access and connected calculation/atomic-energy tools; no equipment-control SOP |
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

- Global Definitions: absorption quantities and EXAFS k–E conversion
- Chapter 1: Optics(Energy) Adjustment
- Chapter 2: Energy Calibration
- Chapter 3: Auto Amp Tune
- Chapter 4: WorkStation and Encoder Value Correction
- Chapter 5: Measurement Method
- Chapter 6: Measurement Mode
- Chapter 7: Sample Requirements at BL14B2
- Chapter 8: Operation of PM16C
- Chapter 9: Operation of 4D Slit
- Chapter 10: Operation of MBS/DSS
- Chapter 11: Cryostat Experiment
- Chapter 12: HummingBird Automatic Measurement
- Chapter 13: In-situ Cells Provided by BL14B2
- Chapter 14: In-situ Cell Heating Controller
- Chapter 15: BL14B2 Gas Supply System
- Chapter 16: BL14B2 Intranet Web Tools
- Chapter 17: BL14B2 Standard Sample List

## Global Definitions

The following definitions apply throughout this GPT unless explicitly stated otherwise.

### MaxTotal μT

- "MaxTotal μT" refers to the total X-ray absorption of the complete sample evaluated at an energy on the post-edge side of the target absorption edge.
- It is equal to the sum of the μT contributions from the target element and all other elements evaluated at the same post-edge energy.
- The pre-edge μT must not be interpreted as the MaxTotal μT.

### ΔμT

- "ΔμT" refers to the absorption-edge jump of the target element.
- ΔμT is not equal to MaxTotal μT.

These definitions must be used consistently whenever discussing:

- transmission suitability
- sample preparation
- self-absorption
- measurement-method selection
- absorption-related calculations

### EXAFS k–E conversion

The nonrelativistic photoelectron wavenumber is k = sqrt(2 m_e (E - E0)) / hbar. Here E is incident photon energy, E0 is the chosen EXAFS energy origin, m_e is electron mass, and hbar is the reduced Planck constant. k is not the incident photon wavenumber.

With k in Å^-1 and energies in eV:

- ΔE = E - E0 = 3.80998211 k².
- k = sqrt((E - E0) / 3.80998211).
- E = E0 + 3.80998211 k².

With E and E0 in keV, E = E0 + 0.00380998211 k². Convert keV differences to eV before using the eV formula.

| k (Å^-1) | E - E0 (eV) |
| --- | --- |
| 10 | 380.998 |
| 12 | 548.637 |
| 14 | 746.756 |
| 16 | 975.355 |

These real-k formulas apply for E >= E0. Below E0, do not use an absolute value to create a positive EXAFS k. Distinguish a tabulated edge used provisionally for planning from a calibrated or fitted experimental E0. If E0 is unknown, report ΔE first; absolute E requires an explicitly identified E0. A neighboring higher-energy edge at E1 gives a nominal boundary k = sqrt((E1 - E0) / 3.80998211) with eV energies; usable data can end earlier. This conversion alone does not establish instrument limits or data quality, and is separate from QXAFS–Step energy-axis correction.

Formula reference: [Larch XAFS utilities: ktoe and etok](https://xraypy.github.io/xraylarch/xafs_utilities.html).

---

## 1. Optics(Energy) Adjustment

### 1.2. Reference

Optics (Energy) adjustment is one of the fundamental alignment procedures in synchrotron XAFS experiments.

Its main purposes include:

- Maintaining the stability of energy scans
- Balancing energy resolution and beam intensity according to experimental requirements
- Reducing harmonic contamination

The optics adjustment procedure typically involves positional adjustments of:

- DCM (Double Crystal Monochromator)
- mirrors
- slits
- sample stage

as well as initialization procedures for the detection system, including:

- ion chamber gas exchange
- presetting amplifier parameters

and other related settings.

In XAFS measurements, the X-ray energy is continuously scanned while measuring the change in absorption coefficient as a function of energy.

Since changing the X-ray energy requires changing the Bragg angle of the DCM, the beam position and beam trajectory also change accordingly. Therefore, related downstream components, including:

- downstream optics
- sample position
- detector position

must be adjusted appropriately to maintain stable beam alignment.

In addition, changing the X-ray energy also changes the conditions for harmonic generation. Therefore, mirror angles and related optical parameters must be adjusted to maintain effective harmonic suppression.

Furthermore, the absorption efficiency of ion chambers depends strongly on the X-ray energy. If the gas composition is not changed appropriately for the corresponding energy range, the ion chamber may not provide sufficient signal intensity.

Because the movable angular range of a monochromator crystal is physically limited, a single crystal plane cannot cover all energy regions.

Therefore, different crystal planes must be selected depending on the target energy range, such as:

- Si(111)
- Si(311)

At BL14B2, the approximate available energy ranges of the monochromator crystal planes are:

- Si(111): 4.3–37.7 keV
- Si(311): 8.3–72.3 keV

However, these values represent the approximate mechanical or operational coverage of each crystal plane.

When the target energy is close to the lower or upper boundary of the available range, the reflected X-ray intensity may decrease significantly.

Therefore, for stable XAFS measurements, it is generally recommended to use each crystal plane in the middle part of its available energy range rather than near the boundary.

When the target energy can be covered by both Si(111) and Si(311), the crystal plane should be selected based on the experimental requirements for:

- flux
- energy resolution
- measurement stability

Different crystal planes provide different characteristics in terms of:

- energy resolution
- reflected intensity (flux)

For example:

- Si(111) generally provides higher flux
- Si(311) generally provides higher energy resolution

As a result, depending on the experimental requirements for:

- flux
- energy resolution

it may also be necessary to switch the monochromator crystal plane during optics adjustment.

When Si(311) is used, the dynamical diffraction width is very narrow. Therefore, even slight mechanical instability may cause a large change in the "I0" intensity, resulting in a change in the absolute value of "μT" in the XAFS spectrum.

Large-angle movements of the monochromator, for example when the crystal plane is changed from Si(111) to Si(311) during optics adjustment, often accumulate mechanical stress. As a result, "Δθ" may gradually shift by a small amount.

This slow and slight shift is not noticeable with Si(111), but it can become significant with Si(311).

If users are particularly concerned about changes in the absolute value of "μT", they may try a monochromator rocking curve scan, or perform optics adjustment again without changing the target element, to release the stress. The rocking curve scan procedure is provided in SOP.md, Section 1.2.6.

At BL14B2, a complete optics adjustment typically requires approximately 30 minutes.

Since optics adjustment involves large movements of multiple motors, and the control system usually determines positions using encoder counts rather than directly measuring the true physical motor positions, discrepancies may gradually develop between:

- the actual motor position
- the encoder value

Such discrepancies become more significant after large motor movements.

Therefore, after optics adjustment, energy calibration must be performed to preset the encoder values and re-establish the correspondence between energy and encoder position.

Because optics adjustment requires considerable time and frequent adjustment may increase encoder-related errors, a full optics adjustment is not typically performed for every energy change.

Based on operational experience at BL14B2, the optical parameters obtained from a single optics adjustment are generally sufficient to support stable XAFS measurements within approximately:

- adjusted energy ±2 keV

In other words, if subsequent measurements remain within this energy range, a full optics adjustment is usually unnecessary.

If the energy range exceeds this range, a new optics adjustment is recommended.

It should be noted that:

“±2 keV” is not a strict physical boundary, but rather a recommended operational guideline based on practical experience at BL14B2.

Auto Optics Adjustment may also be used as a recovery method when the beam condition becomes abnormal after optical parameters or other optics-related settings have been changed inappropriately.

In simple terms, if unintended changes to optics-related settings cause:

- abnormal beam intensity
- unstable beam position
- poor beam alignment
- other abnormal beam conditions

the standard automatic optics-adjustment procedure can generally be used to restore the normal optical condition.

Therefore, users do not necessarily need to manually return every individual optical parameter to its previous value.

However, Auto Optics Adjustment does not complete the energy-axis correction.

Because the automatic adjustment involves substantial monochromator and optical-component movement, Energy Calibration must still be performed after the automatic optics adjustment has been completed.

If the beam condition cannot be restored by Auto Optics Adjustment, or if the cause of the abnormal condition is unclear, users should contact BL14B2 staff rather than repeatedly changing individual optical parameters.

---

## 2. Energy Calibration

### 2.2. Reference

Energy Calibration is one of the fundamental calibration procedures in synchrotron XAFS experiments.

Its main purposes are:
- Re-establishing the correspondence between energy and encoder position
- Ensuring the accuracy of the absorption edge position (E0)
- Improving energy reproducibility between different experiments

In XAFS measurements, the X-ray energy recorded in the experimental data is not usually measured directly.

Instead, the monochromator movement is read through the encoder, and the energy is calculated indirectly from the monochromator position.

Therefore:
- mechanical movement of the monochromator
- accumulated encoder errors
- large-scale optics movement
- long-term mechanical drift

may gradually produce discrepancies between:

- encoder position
and
- the actual physical angle

of the monochromator.

Such discrepancies typically appear in measured data as:

- shifts in absorption edge position
- disagreement between reference spectra and literature values
- poor energy reproducibility between measurements

Therefore, at BL14B2, Energy Calibration is recommended using the XAFS spectrum of a known reference sample.

By comparing:

- the known reference energy
and
- the currently measured energy

the encoder preset value is corrected accordingly.

The essential purpose of Energy Calibration is NOT:

- to change the actual X-ray energy

but rather:

- to correct the correspondence between the encoder and the true energy.

Large monochromator crystal movements can create a difference between the actual theta position and the encoder-recorded value. At BL14B2, the standard user workflow therefore requires Energy Calibration after a large energy change, including optics adjustment. This common requirement ensures that users with different levels of XAFS experience start with a calibrated energy axis.

Once calibration has been completed, it does not need to be repeated for each sample measured under the same unchanged optical condition. A new large energy change or optics adjustment requires calibration again under the standard workflow. Suspected energy-axis drift or a long period without calibration also warrants checking the calibration.

This operational requirement is distinct from a scientific requirement to perform an encoder preset for every experiment. Experienced XAFS users can measure a standard sample under the same conditions and later calibrate their sample data using their chosen reference and analysis criteria. That data-analysis approach does not itself preset the beamline encoder. General user guidance should still follow the standard BL14B2 workflow above rather than assume that a user will perform an independent calibration later.

During Energy Calibration:

- crystal plane
- reference energy
- current measured energy

must all be strictly correct.

In particular, selecting the wrong monochromator crystal plane may result in:

- incorrect encoder correction calculations
- preset failure
- severe energy-position errors

Therefore, calibration must be performed with extreme caution.

Energy Calibration does NOT improve:

- beam intensity
- optics alignment
- harmonic rejection

These are functions of optics adjustment.

The primary goals of Energy Calibration are only:

- correcting energy-axis accuracy
- ensuring energy reproducibility
- restoring consistency between encoder values and the true energy

Users applying their own data-analysis calibration must understand and document the reference, measurement conditions, and calibration method used.

---

## 3. Auto Amp Tune

### 3.2. Reference

Auto Amp Tune is an important procedure used to improve the signal-to-noise ratio (S/N) of gas ion chamber detectors in XAFS experiments.

Its primary purpose is to automatically optimize the following parameters for each ion chamber:

- ion chamber gain
- corresponding suppression current values

Because the electrical current signals generated by gas ion chambers are typically very weak and easily affected by noise, current-to-voltage amplification is necessary to stabilize the signal and improve subsequent signal processing performance.

In practice, the suppression current value is linked to the gain value.

Therefore, users generally only need to pay attention to the gain value itself.

The basic amplification relationship is approximately:

- Voltage = processed current signal × -10^(gain value)

If the gain is too low:

- the signal becomes too weak
- the signal-to-noise ratio deteriorates

If the gain is too high:

- amplifier saturation may occur
- the detector may no longer produce readable signals
- an overflow condition may occur

During overflow, an audible alarm sounds and valid counting is unavailable, but the mechanical scan continues. Overflow does not itself stop the scan. Changing the amplifier gain during scanning can cause a system bug, so the gain must not be changed until the scan has finished, even while the alarm is sounding. The corresponding operation guidance is in SOP.md, Section 3.2.8.

Therefore, appropriate gain adjustment is required before XAFS measurements.

At BL14B2, the available gain-value range is:

- 6 to 9

The ion-chamber current signal is converted to a negative voltage. Before amplification, its level is approximately -0.0001 V under the described conditions; this is an approximate example, not a fixed signal level.

The downstream counting electronics, such as the V2F, can accept a negative voltage down to -10 V. A voltage more negative than -10 V, such as -11 V, cannot be read correctly.

- Ideal amplified voltage range: -10 V ≤ V ≤ -1 V.
- Acceptable weaker-signal range: -1 V ≤ V ≤ -0.1 V, although S/N may be lower.
- A voltage below -10 V is outside the usable negative-voltage range.

The XAFS signal can vary substantially across the scan range, so the weaker-signal range may be necessary at some energies. Auto Amp Tune is used to obtain suitable gain conditions across the intended scan.

In XAFS measurements, ion chambers are used to measure X-ray intensity.

The electrical signals generated by ion chambers depend strongly on:

- X-ray energy
- beam intensity
  - including synchrotron source conditions
  - and beam size
- gas composition
- measurement mode
- sample absorption

As experimental conditions change, for example:

- changing energy
- changing beam size
- changing sample absorption

the output signal level of the ion chambers may also change significantly.

Therefore, whenever such experimental conditions change, re-adjustment of gain values is generally recommended.

At BL14B2, Auto Amp Tune automatically determines suitable gain and suppression conditions based on specified absorption-edge conditions.

Because X-ray absorption changes significantly around absorption edges, the detector signal intensity may vary greatly depending on energy.

As a result, a single gain condition is not always suitable for the entire energy range of a measurement.

To ensure that the amplified voltage remains below the amplifier saturation limit throughout the entire scan range, Auto Amp Tune typically determines gain conditions using two representative energy positions around the absorption edge:

- approximately 100 eV before the absorption edge
- a high-energy-side point corresponding to approximately:
  - X k Å⁻¹
  - where X is generally chosen to match the intended measurement k-range

Even during Auto Amp Tune, manual gain adjustment is still possible.

When the gain value is manually changed, the corresponding suppression current value is automatically adjusted together.

Users with sufficient technical understanding may also perform manual gain adjustment when necessary.

However, Auto Amp Tune does NOT:

- improve beam intensity
- improve optics alignment

The primary goals of Auto Amp Tune are only:

- stabilizing ion chamber signal intensity
- improving signal-to-noise ratio (S/N)
- reducing amplifier saturation risk

The important point is that users clearly understand:

- how gain conditions were determined
- which energy regions were used for tuning
- whether the resulting detector signals are physically reasonable

In addition, every time Auto Amp Tune is performed, special attention must be paid to the correct input format.  
If the input format is incorrect or an operational mistake is made, the specified measurement points may fail to be converted into the correct angular positions and therefore cannot be recognized by the system, causing Auto Amp Tune to fail.

Under normal conditions, Auto Amp Tune typically requires at least around 40 seconds to complete.  
If Auto Amp Tune finishes within only a few seconds, an error has almost certainly occurred.

Common causes of failure:
- The absorption edge format was entered incorrectly, so the angle position could not be interpreted.
- The encoder theta value differs too much from the actual theta value.  
  Reference: WorkStation and Encoder Value Correction Project.

---

## 4. WorkStation and Encoder Value Correction

### 4.2. Reference

At BL14B2, when changing the incident X-ray energy:

- The monochromator is moved using the WorkStation theta command.
- However, counting and position recognition are performed using the encoder theta value.

Because the following effects cannot be completely avoided:

- mechanical movement of the monochromator
- accumulated encoder errors
- large-scale optics movement
- long-term mechanical drift

the WorkStation theta value and the encoder theta value will inevitably differ.

When the difference is still small, the measured spectrum may show an obvious spectral shift.

However, when the difference becomes large, typically exceeding 0.1 degree, all theta-related movement commands will be disabled by the protection mechanism.

Therefore, when theta-related commands cannot be executed, such as:
- QXAFS cannot start
- Auto Amp Tune cannot start

the consistency between the WorkStation theta value and the encoder theta value should be checked.

In most cases, energy calibration is used to preset the encoder value and restore consistency between the WorkStation value and the encoder value.

Under normal operation, theta movement is generally performed based on the encoder value.

For a large WorkStation–encoder mismatch, the documented preset operation is provided in SOP.md, Section 4.2.4. Small differences are usually acceptable.

In addition, the encoder theta value has two branches:
- encoder display
- encoder board

In principle, these two values should be identical.  
When presetting is performed, both values are preset simultaneously.

---

## 5. Measurement Method

### 5.2. Reference

At BL14B2, several measurement methods are available depending on the experimental purpose and sample condition.

The commonly used measurement methods include:

- Transmission measurement
- Fluorescence measurement
  - Grazing-incidence X-ray fluorescence measurement
- Conversion electron yield (CEY) measurement

#### 5.2.1. Transmission Measurement

Transmission measurement is the most fundamental and commonly used XAFS measurement method.

In transmission measurements:

- the incident X-ray intensity is measured as "I0"
- the transmitted X-ray intensity after passing through the sample is measured as "I1"
- X-ray absorption is calculated from the attenuation of the transmitted beam

The absorption coefficient is generally expressed as:

μt = ln(I0 / I1)

where:

- "μ" is the absorption coefficient
- "t" is the sample thickness

The XAFS spectrum is obtained by observing how "μ" changes while the incident X-ray energy is scanned across the absorption edge.

Transmission measurement directly measures the attenuation of X-rays caused by absorption in the sample. Therefore, it is generally considered the most direct and reliable XAFS measurement method.

Under suitable sample conditions, high-quality QXAFS spectra up to "k = 20 Å⁻¹" can often be obtained within approximately 5 minutes.

The fastest single QXAFS transmission scan can be completed in approximately 30 seconds. However, in actual operation, additional time is required for mechanical motion such as monochromator angle recovery. Therefore, each measurement cycle typically requires an additional approximately 40 seconds.

Transmission measurements generally provide:

- stable spectra
- good reproducibility
- relatively high S/N
- relatively straightforward data interpretation
- reduced sensitivity to detector geometry
- reduced sensitivity to surface conditions

Because the transmitted beam is directly measured, transmission spectra are often considered the most reliable reference data for XAFS analysis.

The main difficulties of transmission measurement are associated with sample preparation and absorption conditions.

For transmission measurements, the sample absorption must remain within an appropriate range.

If the absorption is too weak:

- the absorption edge jump becomes too small
- spectral features become difficult to distinguish
- S/N deteriorates

If the absorption is too strong:

- transmitted intensity becomes too small
- counting statistics deteriorate
- noise increases

At BL14B2, transmission measurements generally become difficult when:

- "Δμt < 0.2"
- "MaxTotal μT > ~4"

For transmission measurements, the sample concentration and thickness must be spatially uniform so that the absorption "μt" remains consistent along all X-ray paths through the illuminated region.

In addition, the X-ray beam size must remain smaller than the sample size during measurement.

When these conditions cannot be satisfied through sample preparation, fluorescence measurement is generally recommended instead. For the beam-size condition in fluorescence measurements, see Section 5.2.2.

In practical transmission measurements, users mainly need to consider the following points:

- whether the sample completely covers the X-ray beam size
- whether suitable gain values are obtained for the incident energy, slit condition ("4D slits"), and sample absorption
- the effect of air absorption in low-energy regions

The sample position and beam coverage can be checked using the red alignment laser located downstream of Ion Chamber 2.

Transmission measurements use gas-filled ion chamber detectors:

- "I0"
- "I1"
- "I2"

These ion chambers differ in size and gas composition.

To maintain appropriate signal levels over different energy regions (typically within approximately `±2 keV` from the optics-adjusted energy):

- the gas absorption in "I0" is typically maintained at approximately 25%
- "I1" and "I2" use the same gas composition
- the gas absorption in "I1" is typically maintained at approximately 80%

During transmission measurements, samples may be placed both:

- between "I0" and "I1"
- between "I1" and "I2"

for simultaneous measurement.

However, because the intensity at "I2" is more difficult to control, samples placed between "I1" and "I2" are typically used only as reference samples.

Transmission measurement can also be performed simultaneously with other measurement methods. In practice, this means that "I1" and "I2" signals can be recorded and processed concurrently during other measurements.

#### 5.2.2. Fluorescence Measurement

Fluorescence measurement (Fluorescence XAFS) is one of the most commonly used XAFS measurement methods when transmission measurement cannot be performed under suitable conditions.

Unlike transmission measurements, fluorescence measurements do not directly measure the attenuation of transmitted X-rays. Instead, they detect the fluorescent X-rays emitted from the sample after X-ray absorption.

The fluorescence intensity can be expressed as:

$$
I_f(E)
=

I_0(E)
\cdot
\epsilon_f
\cdot
\frac{\Omega}{4\pi}
\cdot
\mu_a(E)
\cdot
\frac{
1-\exp\left[
-t
\left(
\frac{\mu_{tot}(E)}{\sin\theta_{in}}
+
\frac{\mu_{tot}(E_f)}{\sin\theta_{out}}
\right)
\right]
}{
\frac{\mu_{tot}(E)}{\sin\theta_{in}}
+
\frac{\mu_{tot}(E_f)}{\sin\theta_{out}}
}
$$

Unlike transmission measurements, the fluorescence intensity is influenced not only by the absorption coefficient of the target element, but also by:

- sample thickness
- total sample absorption
- incident angle
- fluorescence escape angle

Therefore, fluorescence measurements do not generally satisfy:

$$
\frac{I_f}{I_0}
\propto
\mu(E)
$$

Only under certain approximations can the fluorescence signal be regarded as approximately proportional to the absorption coefficient.

Typical examples include:

- dilute samples that are sufficiently thick to generate adequate fluorescence signal
- concentrated samples that are sufficiently thin to suppress self-absorption

As a result, fluorescence spectra are generally more difficult to interpret than transmission spectra.

One important phenomenon in fluorescence measurements is known as self-absorption.

Self-absorption occurs when fluorescent X-rays generated inside the sample are reabsorbed before escaping from the sample.

As indicated by the fluorescence equation, the effect becomes more significant when:

- the sample is thick
- the sample absorption is strong
- the incident and exit geometry are unfavorable

Self-absorption may cause:

- distortion of XAFS amplitudes
- loss of linearity between fluorescence intensity and absorption coefficient
- reduction of EXAFS oscillation amplitudes

Although various correction algorithms have been proposed, self-absorption remains one of the fundamental limitations of fluorescence measurements.

For this reason, transmission measurements are generally preferred whenever suitable sample conditions can be achieved.

BL14B2 recommends that, when geometrical effects are ignored and the material is homogeneous, the effect of self-absorption can be neglected if ΔμT / MaxTotal μT is below 0.025.

Compared with transmission measurements, however, fluorescence measurements are much less constrained by sample thickness and absorption conditions.

Therefore, fluorescence measurements are particularly useful for:

- dilute samples
- supported catalysts
- non-uniform samples
- small samples
- highly absorbing matrices
- trace-element measurements

where transmission measurements are difficult or impossible.

Unlike transmission measurements, fluorescence measurements do not require the X-ray beam size to be smaller than the sample size.

However, this applies only when the fraction of the incident X-ray intensity that illuminates the sample remains constant during the XAFS energy scan.

Under some optical conditions (energy ranges), for example when the DCM Bragg angle is below 5°, the mirrors may not focus the beam effectively. In particular, when a mechanical glitch occurs, the spatial intensity distribution of the incident beam may become unstable during the scan. As a result, the fraction of the incident X-ray intensity that illuminates the sample may change. For the effect of mirror reflection on the vertical intensity distribution of the X-ray beam, see Section 9.2.1.

In this case, if the sample is much smaller than the X-ray beam, the XAFS spectrum may be distorted even in fluorescence measurements.

The corresponding check is provided in SOP.md, Section 5.2.2.4.

Because fluorescence measurements rely entirely on fluorescent X-ray detection, proper detector signal processor (DSP) configuration is essential.

Important detector signal processor (DSP) settings include:

- ROI (Region of Interest) selection
- fluorescence count-rate control
- deadtime correction

The ROI defines the fluorescence energy window accepted by the detector.

The purpose of ROI selection is to separate:

- target fluorescence signals
- fluorescence from neighboring elements
- elastic scattering
- Compton scattering

Before actual measurements, a standard sample is typically measured to determine the appropriate ROI position.

Because detector gain and electronic response may vary slightly between measurements, the optimal ROI position may shift slightly and should be confirmed before each experiment.

At BL14B2, the fluorescence detector is 19-element Ge SSD detector. Fluorescence signals are processed using a DSP-based signal processing system.

The energy resolution of the DSP is approximately:

- 200–300 eV

As a result, fluorescence peaks from neighboring elements may partially overlap.

When two elements emit fluorescence signals with similar energies, the DSP may not be able to completely separate them.

This represents one of the intrinsic limitations of fluorescence measurements.

Another important detector effect is deadtime.

Deadtime occurs when the detector receives signals faster than they can be processed.

Under such conditions, part of the incoming signal is lost, resulting in non-linear detector response.

Deadtime is particularly important in XAFS measurements because fluorescence intensity often increases abruptly near the absorption edge.

If significant deadtime occurs, the measured XAFS spectrum may become distorted.

To maintain detector linearity, the fluorescence count rate is typically adjusted before measurements by:

- changing the 4D slit opening
- changing the detector distance
- inserting attenuation filters

DSP Tools displays two different count statistics:

| Display column | Signal | Meaning for intensity adjustment |
| --- | --- | --- |
| Total | ICR | Total input count rate; use this to control detector load and avoid overflow |
| ROI | SCA | Count rate within the selected region of interest; increase this as far as possible while keeping Total out of overflow |

The goal is to maximize the ROI signal while keeping Total below the overflow limit for the current SPring-8 bunch mode. Total and ROI are different quantities; the Total limits must not be applied to ROI as if they were the same signal.

DSP Tools uses a default counting interval of 1 s. The standard count-rate unit is cps (counts per second). At this interval, accumulated counts in cnts are numerically equal to the average rate in cps. If the interval changes, divide counts by the interval in seconds before comparing with a cps limit.

The Total (ICR) overflow limit depends on the electron-bunch spacing:

| Electron-bunch spacing | Total (ICR) overflow limit |
| --- | --- |
| Longer spacing | Approximately 100000 cps |
| Shorter spacing | Approximately 60000 cps |

Around 70000 cps in Total is a general operational reference used at BL14B2, not a universal maximum or a target that overrides the current bunch-mode limit. In a mode with an approximately 60000 cps limit, Total must remain below that limit rather than be raised to 70000 cps. The applicable limit must be confirmed for the current bunch mode; do not infer it merely from a generic single-bunch or multi-bunch label.

The intensity-adjustment procedure is provided in SOP.md, Section 5.2.2.3.

Deadtime-corrected fluorescence data are automatically generated by BL14B2 measurement software.

Additional deadtime correction may also be performed using:

- XAFS_DataConverter

In practical operation, fluorescence measurements often involve dilute samples and therefore generally require longer acquisition times than transmission measurements.

Typical QXAFS fluorescence measurements require approximately:

- 15 minutes

In addition, due to hardware limitations at BL14B2:

- dwell time must be set to at least 11 ms during QXAFS measurements (≥11 ms; 11 ms is included)

The DSP processing interval is approximately 10 ms. Acquisition at a 10 ms interval can readily cause network congestion, so the minimum dwell time is 11 ms.

For standard fluorescence measurements, the sample surface is typically positioned at approximately:

- 45° relative to the incident X-ray beam

This geometry provides a practical balance between:

- reduced self-absorption
- reduced scattering background

A specialized variation of fluorescence XAFS is grazing-incidence fluorescence measurement.

In this method, the incident angle is reduced to very small values, typically:

- 0–5°

Under these conditions, strong X-ray reflection occurs at the sample surface.

As a result, the X-ray penetration depth becomes very shallow and the fluorescence signal becomes highly surface sensitive.

Grazing-incidence fluorescence measurements are particularly useful for:

- thin films
- flat samples
- surface-sensitive studies

The effective probing depth is typically on the order of several tens of nanometers.

#### 5.2.3. Conversion Electron Yield (CEY) Measurement

Conversion Electron Yield (CEY) measurement is a surface-sensitive XAFS technique that detects electrons emitted from a sample after X-ray absorption.

Unlike transmission measurements, which detect transmitted X-rays, and fluorescence measurements, which detect fluorescent X-rays, CEY measurements detect the electrical current generated by emitted electrons escaping from the sample surface.

When an incident X-ray is absorbed by an atom, a core electron is excited and a core hole is created.

The subsequent relaxation processes may produce:

- photoelectrons
- Auger electrons
- secondary electrons

Some of these electrons can escape from the sample surface.

In CEY measurements, the emitted electrons are collected and converted into an electrical signal.

The measured electron yield is approximately proportional to the X-ray absorption coefficient:

$$
I_{CEY}
\propto
\mu(E)
$$

Therefore, CEY spectra are often qualitatively similar to transmission and fluorescence XAFS spectra.

However, because electrons have a very short escape depth inside condensed matter, only electrons generated near the sample surface can contribute to the detected signal.

As a result, CEY is inherently surface sensitive.

The effective probing depth of CEY is typically:

- up to several tens of nanometers

depending on:

- X-ray energy
- sample composition
- electron transport properties

Compared with fluorescence measurements, CEY generally provides much stronger surface sensitivity.

Therefore, CEY measurements are particularly useful for:

- surface oxidation studies
- surface reduction studies
- thin films
- surface-treated materials

where information from the near-surface region is desired.

Because CEY detects emitted electrons rather than transmitted or fluorescent X-rays, CEY measurements are generally much less affected by:

- self-absorption effects
- fluorescence overlap
- detector deadtime

However, CEY measurements have their own limitations.

Since emitted electrons must escape from the sample surface, CEY measurements generally require samples that are:

- electrically conductive
- sufficiently large to intercept the X-ray beam
- relatively flat

Poor electrical conductivity may cause surface charging during measurements.

Surface charging can distort the electron signal and degrade spectral quality.

For this reason, CEY measurements are often difficult for:

- insulating materials
- powders with poor electrical contact
- highly resistive oxides

unless special sample preparation methods are employed.

Because CEY is highly surface sensitive, the measured spectrum may differ significantly from transmission or fluorescence spectra if the surface composition differs from the bulk composition.

Therefore, CEY spectra should generally be interpreted as surface information rather than bulk information.

At BL14B2, CEY measurements are performed by collecting emitted electrons under a helium atmosphere.

The emitted electrons ionize the surrounding helium gas.

The generated ion pairs are then collected using an applied electric field and measured as an electrical current.

---

## 6. Measurement Mode

### 6.2. Reference

At BL14B2, two XAFS scan modes are available:

- Step XAFS
- Quick XAFS (QXAFS)

Both scan modes can be combined with:

- Transmission Measurement
- Fluorescence Measurement
- Conversion Electron Yield (CEY) Measurement

The difference between the two scan modes is not the measurement method itself, but the way the monochromator energy is scanned and how detector signals are recorded.

Because QXAFS and Step XAFS use different methods to associate detector counts with monochromator theta positions, the resulting energy axes are not necessarily identical.

In Step XAFS:

- the monochromator moves to a discrete position
- the monochromator stops
- detector counting is performed at that stationary position

In QXAFS:

- the monochromator moves continuously
- detector counts and encoder theta positions are recorded during motion
- the recorded counts are subsequently associated with the corresponding theta positions during data processing

Therefore, QXAFS data and Step XAFS data must not be assumed to be directly comparable solely because the same nominal energy range was entered.

When spectra obtained using the two scan modes need to be compared quantitatively, an appropriate energy-axis calibration or conversion should be performed.

As a result:

- Step XAFS provides slower but more flexible measurements.
- QXAFS provides significantly faster measurements.

The choice between Step XAFS and QXAFS depends primarily on the experimental objective and required time resolution.

#### 6.2.1. Quick XAFS (QXAFS) Measurement Mode 

Quick XAFS (QXAFS) is the standard fast-scanning mode at BL14B2.

In QXAFS measurements, the monochromator continuously moves throughout the scan while detector signals are recorded simultaneously.

Because the monochromator does not stop at individual energy points, QXAFS measurements are significantly faster than Step XAFS measurements.

QXAFS is particularly useful for:

- repeated measurements
- time-resolved measurements
- in-situ experiments
- kinetic studies

One important operational characteristic of QXAFS is that the scan must not be interrupted once the scan has started.

During a BL14B2 Step scan, theta and the corresponding settings of other internal monochromator optical components are adjusted together. The scan can therefore be stopped partway using the documented Step-scan Stop function.

During a QXAFS scan, only theta moves; the matching settings of the other internal monochromator components remain unchanged. After scanning, theta returns to its initial value to restore the matched optical condition.

Forced termination of the QXAFS program is permitted only in either of these states:

- theta movement for the scan has not yet started; or
- the scan has ended and theta has returned to its initial value, restoring the matched optical condition.

These are alternative conditions. A stationary theta value alone does not prove that recovery is complete. Do not forcibly terminate while scanning or while theta is returning. The corresponding procedures are in SOP.md, Sections 6.2.1.1 and 6.2.1.2.

For long-duration measurements, use of the loop function is recommended.

Although an individual scan cannot be interrupted safely, the measurement can be stopped between loops.

At the end of each loop, the monochromator automatically returns to its initial position.

For QXAFS measurements:

- minimum dwell time is generally 10 ms for S/N
- fluorescence measurements require dwell time ≥11 ms (11 ms is included)

Several safety checks are automatically performed before a scan starts.

The Start button may remain disabled when:

- scan parameters exceed allowed ranges
- encoder value and workstation value differ excessively

When scan parameters are entered correctly, the corresponding:

- start degree
- end degree

should be updated automatically in the GUI.

If these values are not updated, the input has not been accepted by the software.

Because the encoder memory capacity at BL14B2 is limited to 8191 points, the number of counting points within the selected range must not exceed 8191. At the same time, the energy interval between adjacent counting points should not be too large or too small, typically 0.2–0.5 eV. Therefore, the scan range has an upper limit. If this upper limit is exceeded, the “Start” button on the QXAFS scan operation interface will not be activated.

On the other hand, the moving speed of the monochromator theta axis is also limited, ranging from 15 pulses/s to 1500 pulses/s. This means that, once the energy range is determined, the total time required, calculated as the number of points × dwell time, is also subject to certain limits. Since the number of points is mainly determined by the scan range, if the dwell time is not set appropriately for the selected scan range, the “Start” button on the QXAFS scan operation interface will not be activated.

Before starting a QXAFS measurement, users should verify that:

- path
- name
- comment

shown in the QXAFS Monitor (Browser webpage) are identical to the values entered in the QXAFS GUI.

If inconsistencies exist, the values should be deleted and entered again.

Otherwise, data export may fail and the software may remain in the "waiting" state.

When entering a path for QXAFS measurements:

- the first path corresponds to the server data drive
- the second path corresponds to the user drive

Both paths must be specified correctly.

##### 6.2.1.1. Comparison Between QXAFS and Step XAFS Data

At present, QXAFS and Step XAFS data obtained at BL14B2 should not be compared directly without additional correction.

This is because the two scan modes use different methods to determine and associate the monochromator theta position with detector counting data.

When comparison between QXAFS and Step XAFS spectra is required, two approaches are available.

###### 6.2.1.1.1. Reference-Sample-Based Calibration

The same standard reference sample can be measured using both:

* QXAFS
* Step XAFS

The characteristic absorption-edge position or other appropriate spectral feature of the reference sample can then be used to calibrate the relative energy positions of the two datasets.

This method provides an experimental calibration based on the actual measurement conditions.

###### 6.2.1.1.2. Theoretical Energy-Axis Conversion

Users may contact BL14B2 staff for assistance.

BL14B2 staff can provide or use dedicated software that converts the QXAFS theta or energy axis based on theoretical calculations and the documented BL14B2 counting geometry.

This conversion must be performed using the approved staff-provided calculation method.

The correction requires the approved software and sufficient documented parameters.

This QXAFS–Step XAFS conversion is different from the routine Energy Calibration performed after optics adjustment.

* Routine Energy Calibration corrects the correspondence between the encoder position and the true X-ray energy.
* QXAFS–Step XAFS conversion corrects or reconciles differences originating from the different theta-position and counting-association methods used by the two scan modes.

#### 6.2.2. Step XAFS Measurement Mode

Step XAFS is the conventional scanning mode at BL14B2.

In Step XAFS measurements, the measurement cycle is repeated as follows:

- monochromator moves
- monochromator stops
- detector counts are collected
- counting stops
- monochromator moves to the next point

Because the monochromator remains stationary during counting, detector signals are directly associated with discrete energy points.

Unlike QXAFS, Step XAFS spectra are updated continuously during the measurement.

Therefore, users can monitor the spectrum in real time.

Another important advantage of Step XAFS is that the measurement can be stopped safely at any time using the Stop button provided in the Step XAFS GUI.

The LabVIEW emergency stop button should not be used for routine scan termination.

Step XAFS allows flexible configuration of:

- number of energy points
- counting time
- scan regions

However, because the monochromator must repeatedly start and stop during the measurement, Step XAFS generally requires substantially more time than QXAFS under otherwise identical acquisition conditions.

For this reason, Step XAFS is generally selected when operational flexibility and real-time monitoring are more important than measurement speed.

---

## 7. Sample Requirements at BL14B2

### 7.2. Reference

Sample preparation requirements are determined primarily by the selected measurement method.

The choice of measurement method depends on sample properties such as:

- sample quantity
- concentration
- sample processability
- sample homogeneity
- ability to adjust thickness or dilution

In addition to satisfying the physical requirements of each measurement method (Transmission, Fluorescence, Grazing-Incidence Fluorescence, and CEY), samples must also satisfy the mechanical and geometrical constraints imposed by the BL14B2 experimental environment.

#### 7.2.0. General Consideration: Absorption Condition and Mechanical Stability

When preparing samples for BL14B2 measurements, users should consider not only the absorption conditions, such as MaxTotal μT and Δμt, but also the mechanical stability and geometrical compatibility of the prepared sample.

In some cases, if sample preparation is based only on MaxTotal μT and Δμt, the required amount of target material may become very small.

This may result in samples that are:

- too thin
- too small in area
- mechanically unstable
- fragile
- difficult to mount in the required sample holder
- incompatible with the required sample dimensions

In such cases, an appropriate chemically stable filler material with relatively weak X-ray absorption may be mixed with the target sample.

Typical filler materials include:

- BN
- SiC

The purpose of adding filler material is to increase the total sample volume or thickness while maintaining suitable XAFS absorption conditions for the target element.

##### Reference filler thickness for preliminary preparation calculations

When a filler is used and its amount or thickness is neither specified nor determined by the supplied conditions, use a reference filler-equivalent thickness of 1 mm (0.1 cm). This reference applies to the selected filler, including BN, Al2O3, carbon black, or SiC; it does not establish that every filler is chemically or spectroscopically suitable. Carbon black is represented as C only for an explicitly stated pure-carbon approximation; known additives or impurities must be included when relevant.

The 1 mm refers to the filler alone at the stated density, not to the total thickness of the final mixture, nor a separate physical layer in a mixed pellet. For illuminated sample cross-sectional area A in cm² and filler reference density rho_f in g/cm³:

- Filler areal mass sigma_f = rho_f × 0.1 cm, in g/cm².
- Filler mass m_f = rho_f × A × 0.1 cm, in g.

Use the user's supplied applicable density when available. When filler density is not supplied, look up a reliable source for the selected material's stable form at room temperature and atmospheric pressure (approximately 20–25 °C and 1 atm), and use its cited material/true density as the reference for the 1 mm equivalent-thickness calculation. Record the material form or phase, density value, units, source, and reported temperature/pressure when available; do not imply that a source specifies conditions it does not report. A supported ambient material density is sufficient for a provisional calculation: missing measured packing density is not a reason to postpone it.

This reference is an equivalent solid-material thickness, not a prediction of the actual packed powder or pellet thickness. If the user supplies a particular phase, grade, or material form, preserve it rather than replacing it with another ambient phase. For carbon black or other materials without a unique crystalline density, use a reliable material-specific true/skeletal density or a documented range for the stated material; do not silently substitute graphite or diamond. Label a selected value from a reported range as a reference assumption. If no applicable density can be verified, report the specific gap and retain the conversion symbolically rather than fabricate a density. After the preliminary calculation, ask for actual density or packing conditions if needed to refine the physical preparation dimensions.

Explicit filler mass, areal mass, thickness, or conditions that determine its amount take precedence. A supplied total sample thickness is not a filler thickness and must not receive an extra 1 mm of filler. The reference is not a required preparation thickness or an override of holder/cell dimensions. If multiple fillers are mixed, 1 mm applies to their combined filler-equivalent volume, not independently to every component; their proportions and density basis must be stated.

Evaluate absorption for the complete sample, including the filler, at the relevant energies. Weak absorption must be checked for the selected energy range, not assumed from the filler name. If the 1 mm reference fails absorption or geometrical criteria, report that result and distinguish any revised proposal from the initial reference.


For example, if only several milligrams of Pt-containing material are available, the amount may be insufficient to prepare a pellet with:

- 10 mm diameter
- 1 mm thickness

which may be required for a BL14B2 in-situ cell.

In this case, an appropriate amount of BN may be mixed with the Pt-containing material to prepare a mechanically stable pellet with the required size.

For example, approximately 173.5 mg of BN can be used to prepare a pellet with:

- 10 mm diameter
- 1 mm thickness

based on the density of BN.

When using filler materials, users should confirm that:

- the filler material is chemically stable under the experimental conditions
- the filler material does not strongly absorb X-rays at the target absorption edge
- the final sample satisfies the required dimensions
- the final sample remains mechanically stable
- the MaxTotal μT and Δμt remain within acceptable ranges

#### 7.2.1. Transmission Measurement

##### 7.2.1.1. Atmospheric Measurements

- No specific sample size requirements.

##### 7.2.1.2. Gas-Phase In-situ Cell

Sample dimensions depend on the specific in-situ cell and its sample holder, not on the transmission measurement method alone. Select the cell first, then use the cell-specific specifications in Section 13.2. There is no common below-2-mm thickness requirement for all BL14B2 in-situ cells.

For the high-pressure transmission cell, see Sections 13.2.2.1 and 13.2.2.2 for holder dimensions, powder preparation, and preformed-pellet compatibility. The powder-loading procedure is provided in SOP.md, Section 13.2.2.

##### 7.2.1.3. Hummingbird Sample Changer

- Sample size should be smaller than 3 cm × 3 cm.
- Sample thickness is recommended to be less than 5 mm.

##### 7.2.1.4. Cryostat

- Transmission cryostat measurements accept pellets with diameters between 5 mm and 10 mm.
- When using 10 mm pellets, up to 15 samples can be mounted simultaneously.
- Sample thickness is recommended to be less than 1 mm.

#### 7.2.2. Fluorescence Measurement

##### 7.2.2.1. Atmospheric Measurements

- No specific sample size requirements.
- However, if the sample is much smaller than the X-ray beam, the XAFS spectrum may be distorted under some optical conditions. See Section 5.2.2.

##### 7.2.2.2. Gas-Phase In-situ Cell

Sample dimensions depend on the specific in-situ cell and its sample holder, not on the fluorescence measurement method alone. Select the cell first, then use the cell-specific specifications in Section 13.2. There is no common below-2-mm thickness requirement for all BL14B2 in-situ cells.

##### 7.2.2.3. Hummingbird Sample Changer

- Sample size should be smaller than 3 cm × 3 cm.
- Sample thickness is recommended to be less than 5 mm.

##### 7.2.2.4. Cryostat

- Only circular pellets with a diameter of 10 mm are accepted.
- Up to 15 samples can be mounted simultaneously.
- Sample thickness is recommended to be less than 1 mm.

#### 7.2.3. Grazing-Incidence Fluorescence Measurement

- Samples should preferably be thin-film specimens.
- Samples must be flat and uniformly distributed on a flat substrate.
- Recommended sample area is larger than 1 cm × 1 cm.
- Recommended substrate size is smaller than 5 cm × 5 cm.

#### 7.2.4. Conversion Electron Yield (CEY) Measurement

- Samples must be electrically conductive, or capable of being mounted on conductive carbon tape.
- The exposed sample area should fit within a circular region of approximately 5 cm diameter.
- Sample thickness should be less than 1 cm.

#### 7.2.5. User-Defined Experimental Environments

If users provide and install their own experimental environment, sample preparation only needs to satisfy the requirements of the user-provided setup.

However, users remain responsible for ensuring compatibility with BL14B2 safety regulations and available sample-stage space.

#### 7.2.6. XAFS Absorption Calculation Assistant — JIN

JIN is the XAFS Absorption Calculation Assistant. Users can access its AI version through the following link:

[XAFS Absorption Calculation Assistant — JIN](https://chatgpt.com/g/g-6a20e7ce75948191bb40df760bff6aa7-xafs-absorption-calculation-assistant-jin)

The connected JIN MCP provides two distinct tools:

| Tool | Purpose | Required information |
| --- | --- | --- |
| `absorption_calculation` | Sample absorption, transmission, and edge-jump calculations | Solid or solution model and relevant sample conditions |
| `atomic_energy_lookup` | Tabulated absorption-edge and selected fluorescence-line energies | Element symbol; optionally edge and line lists |

The atomic-energy lookup returns named entries in `edges` and `fluorescence_lines`, each with `energy_keV`. It accepts K, L1–L3, M1–M5 edge names and nine fluorescence-line names: Ka1, Ka2, Kb1, La1, La2, Lb1, Lb2, Lb3, Lg1. These correspond to Kα₁, Kα₂, Kβ₁, Lα₁, Lα₂, Lβ₁, Lβ₂, Lβ₃, Lγ₁. They are a selected set, not a complete emission-line list. Availability depends on the element and underlying data; unavailable requests are reported separately, and partial results may be returned. No sample mass, density, area, or thickness is needed for this lookup.

The absorption calculation also returns:

- `edge_energy_keV`: the tabulated target absorption-edge energy.
- `fluorescence.line_name` and `fluorescence.line_energy_kev`: one selected fluorescence line's name and energy in keV, when available. The selection is K -> Ka1, L1 -> Lb3, L2 -> Lb1, L3 -> La1; the fluorescence object may be null.
- `energy_keV`: the absorption evaluation energy, not necessarily the edge energy.
- `delta_muT_before_energy_keV` and `delta_muT_after_energy_keV`: actual edge-jump evaluation points, not additional absorption edges.

Tabulated atomic energies are planning references, not measurements of chemical shifts or calibrated experimental E0. Fluorescence energy alone does not determine an executable ROI-setting procedure.


---

## 8. Operation of PM16C

### 8.2. Reference

PM16C controls most motorized devices located in the BL14B2 experimental hutch.

Motor positions can be monitored and controlled using:

- PM16C Read/Move
- PM16C Scan

Typical controlled devices include:

- General-purpose sample stages
- Multi-axis sample stages
- 19SSD detector stages
- Cryostat stages
- Mirror stages
- Experimental table stages

Available motor groups include:

- General X
- General Z
- Sample Stage X
- Sample Stage Z
- Sample Theta
- Sample Line
- XAFS Stage Z
- Detector X
- Detector Z
- Cryostat X
- Cryostat Z
- Mirror Stage Z
- Mirror Theta

#### 8.2.1. Operation of PM16C Read/Move

Before moving a motor, the current motor position should always be read.

The displayed position is not updated continuously and should be refreshed before operation.

PM16C movements are performed using absolute coordinates by default.

Important operational notes:

- Only one channel should be controlled at a time.
- Do not switch to another channel while a motor is moving.
- If another channel is selected during motion, subsequent commands may be sent to the newly selected channel.

For motors moving in the Z direction:

- movement speed is typically much slower than X-direction motion.

Emergency stop procedure:

- Use the "Stop" button provided in PM16C.
- Do not use the LabVIEW red stop button.

The LabVIEW red stop button only terminates communication from LabVIEW and does not send a stop command to the motor controller.

Motor position values shown in PM16C may differ from the actual physical motor position.

When a motor reaches its physical limit:

- the displayed position may continue to change
- the motor may stop moving physically

If this situation occurs:

- immediately press "Stop"

When the software position reaches a configured motion limit:

- further movement commands may be disabled automatically.

Because rotation directions differ among channels:

- verify motor direction using a small test movement before performing large motions.

#### 8.2.2. Operation of PM16C Scan

PM16C Scan is used to perform motor scans while recording detector signals.

As with PM16C Move, software coordinates and actual motor positions may differ.

Scan errors may occur when:

- the motor reaches a physical limit
- the motor reaches a software motion limit

Unlike most XAFS measurement software, PM16C Scan does not automatically control DSS.

Users must manually:

- open DSS before measurements
- close DSS after measurements when necessary

Before starting a scan, detector settings must be verified.

Particular attention should be paid to counter selection.

For fluorescence measurements:

- [19SSD Counter] must be set to "DSP"

In addition:

- the absorption edge must be entered correctly

to ensure proper detector operation and data acquisition.

#### Operational Notes

- Always verify the current motor position before movement.
- Always confirm motion direction using a small test movement.
- Never switch channels while a motor is moving.
- Use the PM16C "Stop" button for emergency stops.
- Do not use the LabVIEW red stop button as a motor stop command.
- PM16C Scan does not automatically control DSS.
- Fluorescence scans require correct DSP counter selection and absorption-edge settings.

---

## 9. Operation of 4D Slit

### 9.2. Reference

The 4D slit is located upstream of ion chamber I0.

It controls the incident X-ray beam size using two directions:

- horizontal direction
- vertical direction

The 4D slit size directly affects the incident beam intensity measured by I0.

Therefore, whenever the 4D slit size is changed, the I0 intensity may also change. If necessary, the amplifier gain value should be checked and adjusted after changing the 4D slit size.

During 4D slit operation, including Read, Move, and Scan operations, users must not switch to another motor channel while the motor is moving or scanning.

If the channel is changed during operation, subsequent commands may be sent to the newly selected channel.

This caution is similar to PM16C motor operation.

#### 9.2.1. Operation of 4D Slit Read/Move

The adjustable horizontal width of the 4D slit is typically:

- 0.5–5 mm

The vertical height of the 4D slit is normally fixed at:

- 1 mm

In normal operation, the vertical height is generally not changed.

This is because the X-ray beam may move slightly in the vertical direction during energy or angle scans.

In addition, due to mirror reflection in the beam path, the vertical intensity distribution of the X-ray beam may vary depending on the mirror angle.

Therefore, the vertical slit size should not be set too small or too large.

When [4D Slit Move.vi] is launched, the current slit size is not automatically refreshed.

Before changing the slit size, users should use Read to confirm the current width and height values.

#### 9.2.2. Operation of 4D Slit Scan

In principle, after optics adjustment has been completed, the 4D slit position should already be optimized.

Therefore, 4D slit scan is not generally recommended during normal operation.

If no X-ray beam enters I0 even when the 4D slit is fully opened, users should contact BL14B2 staff rather than attempting to solve the problem by performing a 4D slit scan.

Such a situation usually indicates a problem with upstream optical alignment or other optical components.

A 4D slit scan cannot fundamentally solve this type of beam-position problem.

In this case, optics adjustment should be checked or performed again under staff guidance.

4D slit scan does not open DSS automatically.

4D slit scan does not support fluorescence scans.

---

## 10. Operation of MBS/DSS

### 10.2. Reference

MBS and DSS are two different shutters at BL14B2.

- MBS: Main Beam Shutter
- DSS: Downstream Shutter

They have different locations, operation permissions, and safety meanings.

#### 10.2.1. Main Beam Shutter (MBS)

MBS is the Main Beam Shutter.

It is located in the optics hutch.

Under normal operation, users are not allowed to directly operate MBS.

MBS can only be operated from the interlock control panel.

It cannot be operated remotely from the control PC.

Manual MBS operation may be required in the following cases:

1. When interrupting an automatic Hummingbird measurement.

   - The automatic program can only be interrupted by closing MBS.

2. When the SPring-8 light source is interrupted.

   - In this case, the central control room may take control of the BL14B2 MBS and forcibly close MBS during light-source adjustment.
   - After the light-source adjustment is completed, users need to open MBS manually.
   - The light-source status can be checked using the browser-based beam status information, such as Beam Chat or Beam State.

When MBS is closed, the light-green "Ready" lamp on the interlock control panel flashes.

During Auto Optics Adjustment, some steps may also involve automatic opening and closing of MBS.

Therefore, the light-green "Ready" lamp may also flash during Auto Optics Adjustment.

#### 10.2.2. Downstream Shutter (DSS)

DSS is the Downstream Shutter.

It is located in the experimental hutch.

Unlike MBS, DSS can be operated by users when necessary.

DSS can be operated using:

- the interlock control panel
- remote operation from the control PC

To operate DSS, the interlock key on the interlock control panel must be turned from:

- Disable

to:

- Enable

DSS operation is only allowed when the interlock key is in the Enable position.

The interlock key can be turned back to Disable only when DSS is closed.

If users try to turn the key to Disable while DSS is open, an alarm will be triggered.

When the interlock key is in the Disable position:

- DSS is closed
- DSS cannot be opened
- the light-green "Ready" lamp on the interlock control panel is ON
- the experimental hutch door can be opened

When DSS is open:

- the red "Running" lamp on the interlock control panel is ON
- the interlock key must not be operated
- the experimental hutch door must not be opened

#### 10.2.3. DSS Behavior in BL14B2 Software

At BL14B2, DSS behavior depends on the software or operation being performed.

Auto Optics Adjustment:

- DSS is opened automatically.
- DSS is not closed automatically after the adjustment.

QXAFS:

- DSS is opened automatically.
- DSS is closed automatically after measurement.

Auto Amp Tune:

- DSS is opened automatically.
- DSS is closed automatically after tuning.

Scan operations:

- DSS is not opened automatically.
- DSS is not closed automatically.

Therefore, for scan operations, users must manually control DSS when necessary.

---

## 11. Cryostat Experiment

### 11.2. Reference

At BL14B2, cryostat experiments provide a low-temperature measurement environment from approximately:

- 5 K to 300 K

Cryostat experiments can be used for:

- transmission measurements
- fluorescence measurements

However, the sample stages used for transmission measurements and fluorescence measurements are different.

Because changing the cryostat sample stage requires a significant amount of time, users must carefully select the appropriate sample stage before starting the experiment.

For example, recovering the cryostat from low temperature to room temperature may require several hours.

Therefore, when selecting the cryostat sample stage, users should consider both:

- the appropriate measurement method
- compatibility between the sample and the sample stage

Cryostat experiments at BL14B2 are performed only under vacuum conditions.

After a cryostat experiment, when warming the system from low temperature back to room temperature, the vacuum must not be released before the temperature becomes higher than the room dew point.

If the vacuum is released while the sample stage or cold head is still below the dew point, condensation may occur on the sample stage or cold head.

This must be avoided.

Before starting a cryostat experiment, the sample position on the cryostat sample stage should be adjusted locally or remotely.

The red alignment laser should be used to align the sample position with the X-ray beam path.

A particularly important point is that, when the temperature changes significantly, thermal expansion or contraction of the sample stage may cause the sample position to shift away from the X-ray beam path.

Therefore, if abnormal data are observed during cryostat measurements, users should consider performing a PM16C scan to locate the correct sample position again.

Because warming the cryostat from low temperature back to room temperature requires a long time, the cryostat may be moved away from the X-ray beam path during this waiting period if other measurements need to be performed.

In this case, users should record the current cryostat position before moving it.

If necessary, the cryostat can later be returned to the recorded position.

---

## 12. HummingBird Automatic Measurement

### 12.2. Reference

HummingBird is the automatic sample-exchange system at BL14B2.

Its operation is based on predefined SPEC macros.

Before users use HummingBird, the responsible BL14B2 staff must log in to the SPEC server.

The maximum number of samples that can be set in one HummingBird run is:

- 120 samples

HummingBird automatic measurement can perform:

- automatic sample exchange
- beam-size setting
- automatic gain-value adjustment
- automatic transmission measurement
- automatic fluorescence measurement
- automatic optimization of ROI intensity for fluorescence measurement

HummingBird can also perform non-measurement operations, such as:

- calibration of the robot arm position
- remote pickup of a selected sample
- remote return of a selected sample

For HummingBird automatic measurements, users need to enter the required parameters into a dedicated Excel file.

The general workflow is:

1. Enter measurement parameters in the dedicated Excel file.
2. Upload the Excel file to the server.
3. Execute the uploaded parameters using GUI/SPEC.

When filling in the Excel file, users must not use:

- spaces
- special symbols
- full-width characters

#### 12.2.1. Sample Requirements for HummingBird

Samples should be fixed at the center of a 5 cm × 5 cm frame.

The default beam size is:

- 5 mm × 1 mm

Because the robot arm moves to fixed positions after arm-position calibration, the sample must be placed at the correct position in the frame.

#### 12.2.2. Interruption of HummingBird Automatic Measurement

Once HummingBird enters continuous automatic measurement, it cannot be stopped by normal operation.

The only available way to force the program to stop is to close MBS.

Closing MBS prevents the next SPEC macro command from being executed.

However, closing MBS does not forcibly interrupt the command that is currently being executed.

Therefore, even if HummingBird is stopped by closing the MBS, users must wait until the current action has been completed. Whether the current action has finished can be checked by confirming that commands can be entered again in the SPEC command window.

#### 12.2.3. Automatic Gain Value Adjustment

Automatic gain value adjustment in HummingBird determines the energy positions for gain tuning based on absolute energy values stored in the database.

If the measured spectrum after energy calibration shows a significant deviation from the database energy position, automatic gain value adjustment in HummingBird may fail.

#### 12.2.4. Transmission and Fluorescence Measurements

HummingBird can perform both automatic transmission measurements and automatic fluorescence measurements.

However, it is not recommended to mix transmission and fluorescence measurements within the same sample list.

Transmission samples often generate strong fluorescence signals.

If such samples are measured in fluorescence mode, the 19SSD may be exposed to excessive fluorescence intensity and may be damaged.

#### 12.2.5. Fluorescence Measurement Using HummingBird

Before HummingBird fluorescence measurements, users must manually measure a standard sample and calibrate the ROI range in advance.

If automatic ROI intensity optimization is selected during measurement:

- the distance between the 19SSD and the sample may be optimized by scan
- the 4D slit size may be optimized by scan

As in normal fluorescence measurements, the dwell time for HummingBird fluorescence measurements must be at least:

- 11 ms (11 ms is included)

#### 12.2.6. Energy Range Limitation

The optical-condition limitation for HummingBird automatic measurements is the same as for normal measurements.

In general, after optics adjustment, samples can be measured within approximately:

- adjusted energy ±2 keV

as one energy range.

#### 12.2.7. Pre-Check Before Starting Automatic Measurement

Before starting HummingBird automatic measurement, users should remove vacuum tubes or other objects from the experimental table if necessary.　

Users should confirm that the robot arm will not collide with the current vacuum tubes or surrounding objects at the pickup positions, including:

- 90° position
- 45° position

After confirming the safety of the robot-arm position, users can set vacuum tubes back to improve S/N. 

When using SPEC to individually control sample pickup and sample return, the pickup position and return position must be the same.

After starting the HummingBird automatic continuous measurement sequence, users will still have one opportunity to confirm the sample list.

To avoid forced termination of the automatic measurement, users should complete all necessary checks before starting the continuous measurement.

---

## 13. In-situ Cells Provided by BL14B2

### 13.2. Reference

BL14B2 provides several gas-flow in-situ cells for XAFS measurements.

The available in-situ cells can be classified into:

- atmospheric-pressure in-situ cells
- high-pressure in-situ cells

If users want to use other types of in-situ cells, they must consult BL14B2 staff in advance.

#### 13.2.1. Atmospheric-Pressure In-situ Cells

Atmospheric-pressure in-situ cells are typically used under approximately atmospheric pressure plus about 0.1 MPa.

Currently, the commonly used atmospheric-pressure in-situ cells are:

- transmission-type in-situ cell with heating up to 1000 °C
- fluorescence-type quartz in-situ cell with a use temperature of 600 °C and a maximum temperature of 800 °C

##### 13.2.1.1. Transmission-Type In-situ Cell up to 1000 °C

This cell is used mainly for transmission measurements.

Sample requirements:

- circular pellet shape

Compatible sample sizes:

- φ7 mm × t1, 2, 5, 10, 15, 20 mm
- φ10 mm × t1, 2, 3, 5, 12, 20 mm

Because of factors such as gas flow, cooling conditions, and PID settings, the heater temperature and the actual sample temperature may differ slightly.

The temperature difference for this transmission-type in-situ cell can be checked in the following reference material:

- https://support.spring8.or.jp/BL/bl14b2/xafs/in-situ_02/Temp_Calib_trans_cell.pdf

##### 13.2.1.2. Fluorescence-Type Quartz In-situ Cell (600 °C Use Temperature; 800 °C Maximum)

This quartz cell is used mainly for fluorescence measurements. Its use temperature is 600 °C; its maximum temperature is 800 °C. These values describe different conditions and must not be treated as interchangeable.

Sample requirements:

- circular pellet shape

Compatible sample sizes:

- φ10 mm × t1 mm
- φ10 mm × t2 mm

If the sample dimensions satisfy the requirements, this cell can also be used for transmission measurements.

Because of factors such as gas flow, cooling conditions, and PID settings, the heater temperature and the actual sample temperature may differ slightly.

The temperature difference for this fluorescence-type in-situ cell can be checked in the following reference material:

- https://support.spring8.or.jp/BL/bl14b2/xafs/in-situ_02/Temp_Calib_fluo_cell.pdf

#### 13.2.2. High-Pressure In-situ Cell

Currently, the only high-pressure in-situ cell available at BL14B2 supports pressures up to approximately atmospheric pressure plus 0.9 MPa.

##### 13.2.2.1. Transmission-Type High-Pressure In-situ Cell up to 700 °C

This cell is used for transmission measurements under high-pressure conditions.

Sample preparation:

- Powder samples are packed into the holder and manually compacted. Preformed pellets may also be considered, subject to the retention considerations in Section 13.2.2.2.
- Load the sample into the holder on site under staff guidance. The powder-loading procedure is provided in SOP.md, Section 13.2.2.

Holder specifications and sample thickness:

- The specified holder is made of stainless steel, with an outer diameter of 10 mm and an inner diameter of 7 mm.
- Holders of different lengths are available. Adjust the sample thickness using the selected holder length as a guide.
- Sample thicknesses up to approximately 20 mm can be accommodated if the powder can be sufficiently compacted within the selected holder.
- This approximate thickness describes the sample-loading capacity; it is not a recommended thickness for every sample or a guarantee of suitable transmission XAFS absorption conditions. The absorption and mechanical considerations in Section 7.2.0 still apply.
- Users may bring their own holders, but must consult BL14B2 staff in advance and obtain confirmation of compatibility before use. Matching dimensions alone do not establish compatibility.

Because of factors such as gas flow, cooling conditions, and PID settings, the heater temperature and the actual sample temperature may differ slightly.

The temperature difference for this high-pressure transmission-type in-situ cell can be checked in the following reference material:

- https://support.spring8.or.jp/BL/bl14b2/xafs/in-situ_02/Temp_Calib_hp_trans_cell.pdf

##### 13.2.2.2. Sample Preparation and Pellet Compatibility

Powder is manually compacted inside the holder using a stainless-steel rod. Manual compaction does not normally produce the same degree of compression as mechanical pellet pressing.

Compared with manual compaction, mechanical pressing is expected to reduce voids and improve areal-density uniformity. However, the uniformity of the powder itself and of its distribution during loading is also important and may have a larger effect. Neither preparation method alone guarantees a sufficiently uniform sample or a satisfactory transmission XAFS spectrum.

Preformed pellets may be considered, but the current holder has no groove or mechanism for fixing a pellet in place. In particular, pellets approximately 1–2 mm thick may not remain stably retained inside the holder under gas flow. Confirm the proposed pellet dimensions and retention with BL14B2 staff before use; fitting inside the holder alone does not establish stable retention.

For powder loading, one quartz film is placed at the bottom of the holder before filling, and another is placed on top of the sample after filling to prevent powder from scattering under gas flow. Follow the loading sequence in SOP.md, Section 13.2.2.

##### 13.2.2.3. Gas Compatibility and Prior Consultation

The high-pressure in-situ apparatus is still at an early stage of introduction and development. A uniform list of permitted gas species has not yet been established; gas use is assessed for the specific experimental conditions. This does not mean that arbitrary gases may be used without prior confirmation.

The assessment considers:

- the safety characteristics of the gases, including applicable lower explosive limits
- the concentration limits and operating conditions of the gas abatement system
- the compatibility of the gases with apparatus materials under the intended temperature and pressure

For gases such as NH3 and NO, possible corrosion and other chemical effects on apparatus materials under high-temperature and high-pressure conditions must also be considered. Their use is not confirmed solely by the availability of a gas supply line or an MFC calibration entry.

Before planning their use, provide BL14B2 staff with the proposed gas composition, concentrations, temperature, and pressure. Staff will review apparatus compatibility and whether the proposed conditions can be accepted.

The general gas-system requirements in Section 15.2 continue to apply. In particular, use the applicable abatement-system concentration limits in Section 15.2.4, not the post-abatement detector alarm settings, when assessing gas-flow conditions.

##### 13.2.2.4. Condensation During Reaction and Cooling

When planning high-pressure experiments, consider changes in temperature and pressure, as well as the types and concentrations of reaction products. Products such as water may condense depending on these conditions.

This assessment must cover both the reaction conditions and the subsequent cooling of the gas after reaction. Considering only the hot reaction conditions is insufficient to evaluate possible condensation during cooling.

#### 13.2.3. Position Adjustment of In-situ Cells

When using an in-situ cell, the cell position may need to be adjusted.

If necessary, the motorized base under the in-situ cell can be connected to power.

The in-situ cell position can then be adjusted using:

- [PM16C Move.vi]
- [PM16C Scan.vi]

Typical motor channels:

- General X
- General Z

In general, after the in-situ cell position has been aligned once during an experiment, repeated position alignment is usually not required.

#### 13.2.4. Handling Notes for Atmospheric-Pressure In-situ Cells

Atmospheric-pressure in-situ cells and their holders are made of quartz.

Therefore, they must be handled carefully.

During in-situ cell experiments, some sample powder may scatter inside the in-situ cell or holder because of sample-preparation conditions.

After the experiment, users should check and clean the in-situ cell and holder if necessary.

#### 13.2.5. Sample Exchange for Atmospheric-Pressure In-situ Cells

The following describes the window arrangement, not a complete sample-exchange procedure. Purge conditions and the limits of the documented opening procedure are in SOP.md, Section 15.2.1.

When using an atmospheric-pressure in-situ cell, samples are exchanged by opening the downstream-side window.

When installing the window, the vent hole must face inward.

#### 13.2.6. Water-Cooling System

During heating experiments using an in-situ cell, an external water-cooling circulation system is connected to maintain the temperature near the window.

For the water-cooling circulation system:

- both inlet and outlet tubes have physical locks
- the inlet line has a valve

Users should confirm the status of these locks and valves before operation.

---

## 14. In-situ Cell Heating Controller

### 14.2. Reference

The atmospheric-pressure in-situ cells provided by BL14B2 support heating experiments and satisfy the gas-tightness requirements of the BL14B2 reaction gas supply system.

For heating experiments using these in-situ cells, the temperature can be controlled directly from the heating controller.

Before operating the heating controller, users must wait until BL14B2 staff has configured the parameters of PID NO.09 and the required GAIN settings.

Users create or edit heating patterns and select PID NO.09 for each STEP. Newly added STEPs may use a default PID selection, so every STEP must be checked. Selecting the staff-configured PID NO.09 is a user operation; editing its underlying PID parameters remains a staff operation.

#### 14.2.1. Heating Pattern

The heating controller can execute a stepwise heating pattern.

A heating pattern consists of multiple steps, each with a target temperature and a duration.

Example:

- Step 0: after heating starts, target temperature = 30 °C
- Step 1: target temperature = 30 °C, duration = 3 min
- Step 2: target temperature = 50 °C, duration = 2 min
- Step 3: target temperature = 50 °C, duration = 5 min
- Step 4: target temperature = 50 °C, end

In this example, the heating process is:

1. Heating starts and the temperature rises to 30 °C.
2. The temperature is held at 30 °C for 3 min.
3. The temperature is increased to 50 °C over 2 min.
4. The temperature is held at 50 °C for 5 min.
5. The pattern ends at 50 °C.

The heating system cannot perform active cooling.

After heating is stopped, the temperature decreases naturally.

Heating pattern operation includes:

- starting the pattern
- pausing the pattern at the current condition
- continuing the pattern
- skipping the current step
- cancelling the entire pattern

#### 14.2.2. Heating Controller Button Functions

The heating controller has two rows of button functions.
- Lower row: white background with black text
  - menu-control button functions
- Upper row: blue background with white text
  - execution-command button functions

The lower-row menu-control functions are the default functions.
They are used mainly for menu operation and heating-pattern setting.
To activate the upper-row execution-command functions, press:
- FNC

After the execution-command functions are activated, the "FNC" indicator appears in the upper-left area of the control panel.

#### 14.2.3. Lower-Row Menu-Control Buttons

The lower-row white-background buttons have the following functions.

1. MODE
   - switches between menu pages and execution pages
   - returns directly to the main menu page
2. SEL
   - enters subpages from the menu page
   - switches between subpages
3. Up / Down / Left / Right
   - moves the cursor in menu pages
   - changes numerical values
4. ENT
   - confirms and applies changed parameters in menu pages

#### 14.2.4. Upper-Row Execution-Command Buttons

These are function descriptions. For the documented execution sequence, see SOP.md, Section 14.2.3. A complete local/remote switching procedure is not specified there.

The upper-row blue-background buttons become active after pressing:
- FNC

The execution-command buttons have the following functions.
1. FNC
   - activates the upper-row execution-command functions
2. FNC + RUN
   - starts the selected heating pattern
3. FNC + STOP
   - pauses the heating pattern at the current condition
4. FNC + ADV
   - skips the current step
5. FNC + RESET
   - cancels the entire heating pattern
6. FNC + PTN
   - selects a preset heating pattern
   - the pattern can be changed using:
     - Up
     - Down
     - Left
     - Right
     - ENT
7. FNC + A/M
   - switches between local and remote operation modes

---

## 15. BL14B2 Gas Supply System

### 15.2. Reference

The BL14B2 gas supply system supplies reaction gases, controls flow, supports gas switching, and treats exhaust gas for in-situ XAFS experiments.

Official system information:

- https://support.spring8.or.jp/BL/bl14b2/xafs/in-situ_02/gas_system.html

Users must submit the gas-system application, "ガス設備利用申込み":

- https://support.spring8.or.jp/cgi-bin/applygas/index.cgi

The public system page requests submission at least one week before use. System use must also be included in the proposal and pass safety review.

Bringing a high-pressure gas cylinder requires a separate "高圧ガス容器持込事前申請書" (Form 25):

- https://user.spring8.or.jp/?p=22579

The responsible office for Form 25 is the JASRI Safety Office (高輝度光科学研究センター 安全管理室).

- Telephone: 050-3496-8898
- Email: safety@spring8.or.jp

Contact this office regarding the Form 25 application.

Experiments must be planned so that:

- at least two people are available at all times
- the responsible person remains on site
- students do not use the system alone

#### 15.2.1. Basic System Configuration

The system includes:

- gas cylinders and pressure regulators
- piping and valves
- mass flow controllers (MFCs)
- experimental gas paths
- exhaust lines
- dilution-gas supply
- gas abatement and exhaust-treatment equipment

User customization is normally limited to the experimental gas path and requires prior consultation with BL14B2 staff.

#### 15.2.2. BL14B2-Supplied and User-Provided Gases

BL14B2 provides the following gases:

- N2, Ar, CO, H2, O2, NO, and He

Availability and required quantities must be confirmed for each experiment. Large He consumption may require users to prepare their own He cylinder.

Gases not provided by BL14B2 must be prepared by the user, subject to acceptance by the beamline.

User-provided cylinders must have:

- a container capacity of 10 L
- a round handwheel-type main valve

Valve and connector compatibility must be confirmed before ordering.

Users are responsible for attending cylinder delivery and collection. In principle, delivery is arranged for the experiment start, and collection for the experiment end. Special arrangements require consultation with BL14B2 staff.

Nearby gas suppliers:

| Supplier | Telephone | Fax |
| --- | --- | --- |
| 株式会社 共和溶材 光都ガスセンター | 0791-58-2482 | 0791-58-2483 |
| タツミ産業株式会社 テクノポリスCSセンター | 0791-59-8070 | 0791-59-8075 |

These suppliers do not accept overseas orders. Overseas users should arrange orders through a collaborator in Japan, or consult BL14B2 staff if no such collaborator is available.

Gas delivery may take one month or longer after ordering. Early preparation is therefore necessary.

The cylinder installation capacity is:

- up to three flammable-gas cylinders
- up to two oxidizing-gas cylinders

One flammable-gas position is assigned to a sulfur-gas line. Compatibility must be confirmed before treating the three positions as interchangeable.

If more cylinders are required, removal and installation during the experiment may be necessary. This takes additional beamtime.

Typical preparation and shutdown times for transmission experiments using one reaction-gas cylinder are:

| Experiment | Preparation | Shutdown and cleanup |
| --- | --- | --- |
| Atmospheric pressure | 4–5 h | 2.5–3 h |
| High pressure | 6–7 h | 5–6 h |

These are planning estimates, not guaranteed durations.

#### 15.2.3. Customized Experimental Gas Environments

The following equipment is available:

- Two atmospheric-pressure mixed-gas inlet paths, A and B, with line assignments for two inert gases, three flammable gases, and two oxidizing gases.
- A high-pressure mixed-gas path with line assignments for two inert gases, two flammable gases, and two oxidizing gases.
- Two independent exhaust paths.
- A back-pressure control device up to approximately 9 bar above atmospheric pressure, consistent with the approximately 0.9 MPa gauge limit in Section 13. In principle, this is used only with the BL14B2 high-pressure in-situ cell.
- In-situ cells: https://support.spring8.or.jp/BL/bl14b2/xafs/in-situ_02/in-situ_cell.html
- Heating power supply and controller. Communication methods and interfaces require staff confirmation.
- EYELA Cool Ace CA-1112 cooling-water circulator. The connector is an ARAM 2222-22 (P3-3) plug; confirm the mating connector with staff.
- Pfeiffer Vacuum OmniStar GSD301 O1 quadrupole mass spectrometer.
- Electrical supplies: single-phase 100 V / 10 A, single-phase 200 V / 20 A, and three-phase 200 V / 20 A, with Japanese connector specifications. An earth-leakage circuit breaker is required.

The listed gas paths describe hardware connections. They do not authorize simultaneous mixing of arbitrary gases.

Gas connections use 1/8-inch and 1/4-inch Swagelok fittings. Users requiring other sizes must prepare compatible adapters and tubing after confirming the connections with staff.

User-provided gas paths must pass the required leak test before hazardous reaction gases are used. Users should check leak tightness before bringing their equipment, but this does not replace the required on-site test.

#### 15.2.4. Gas-Flow Ranges and Conversion Factors

Two separate checks are necessary:

- whether the selected MFC can provide the requested flow
- whether the complete gas supply and exhaust conditions are acceptable

The MFC flow ranges are shown below. Values are on the specified calibration-gas basis. The reference temperature and pressure for the flow unit must be confirmed before combining these values with other flow data.

Atmospheric-pressure lines:

| Gas line | Calibration gas | A line (ccm) | B line (ccm) |
| --- | --- | --- | --- |
| N2 | N2 | 10–500 | 10–500 |
| He | He | 10–500 | 10–500 |
| Oxidizing A | O2 | 4–200 | 2–100 |
| Oxidizing B | NO | 2–100 | 2–100 |
| Flammable A | H2 | 2–100 | 4–200 |
| Flammable B | CO | 2–100 | 2–100 |
| Flammable S | H2S | 2–100 | 2–100 |

High-pressure lines:

| Gas line | Calibration gas | Flow (ccm) |
| --- | --- | --- |
| N2 | N2 | 4–200 |
| He | He | 4–200 |
| Oxidizing A | O2 | 2–100 |
| Oxidizing B | NO | 2–100 |
| Flammable A | H2 | 2–100 |
| Flammable B | CO | 2–100 |

When the actual gas differs from the MFC calibration gas, use:

`MFC setting = requested actual gas flow × CF_calibration / CF_actual`

where:

- `CF_calibration` is the conversion factor of the calibration gas
- `CF_actual` is the conversion factor of the actual gas

For a premixed gas, calculate the effective conversion factor using all components:

`CF_mix = 100 / Σ(concentration_i [%] / CF_i)`

All component percentages must be included and must sum to 100%. Use a consistent volume/molar composition basis appropriate to the MFC conversion method; do not substitute mass percentages.

Conversion factors for the applicable MFCs:

| Gas | Formula | Conversion factor |
| --- | --- | --- |
| Nitrogen | N2 | 1.00 |
| Helium | He | 1.40 |
| Argon | Ar | 1.40 |
| Hydrogen | H2 | 1.00 |
| Oxygen | O2 | 0.99 |
| Carbon monoxide | CO | 1.00 |
| Carbon dioxide | CO2 | 0.74 |
| Nitric oxide | NO | 0.99 |
| Methane | CH4 | 0.74 |
| Ethane | C2H6 | 0.51 |
| Ethylene | C2H4 | 0.64 |
| Propane | C3H8 | 0.34 |
| Propylene | C3H6 | 0.40 |
| Butane | C4H10 | 0.32 |
| Air | Air | 1.00 |
| Hydrogen sulfide | H2S | 0.75 |

Abatement concentration and gas-flow planning:

Plan user gas composition and flow rates against the applicable concentration limits and operating conditions of the gas abatement system. Use the dilution flow and concentration basis specified for the selected gas path and abatement configuration. The default N2 dilution flow of 5 L/min applies only when it is confirmed as the applicable setting for the experiment.

The gas-detector alarm settings below are for monitoring the exhaust after it has passed through the abatement system. They are alarm thresholds, not allowable user-gas concentrations or flow-planning limits. Do not calculate the maximum reaction-gas flow by comparing a gas mixture diluted with 5 L/min N2 against these post-abatement alarm thresholds. If the applicable abatement concentration limit, dilution condition, or calculation basis is unclear, confirm it with BL14B2 staff before finalizing the gas-flow plan.

Any separate safety condition explicitly applicable to the selected gas path must be checked independently; it must not be inferred from the detector alarm settings.

Gas-detector alarm settings for post-abatement exhaust monitoring:

| Detected gas | Alarm setting |
| --- | --- |
| H2 and hydrocarbons | 1000 ppm |
| CO | 25 ppm |
| NO | 25 ppm |
| H2S | 10 ppm |

These values describe when the post-abatement gas detectors issue an alarm. They remain relevant to alarm recognition and response, but must not be used to set the user's reaction-gas flow limit. The gas-flow plan is governed by the applicable abatement-system concentration limits and any separately confirmed safety conditions.

#### 15.2.5. Safety Considerations

Safe use of the BL14B2 gas supply system depends on:

- leak-tight gas paths
- appropriate gas-flow and exhaust-treatment conditions
- inert-gas purging before opening a gas path or exchanging a sample
- functioning gas detectors and interlocks
- an understanding of alarm categories and emergency responsibilities

Purging replaces residual reaction gas in the experimental gas path with inert gas. It is required before opening the gas path or exchanging a sample after reaction-gas use.

The purge gas, flow rate, and duration are specified in SOP.md, Section 15.2.1. That section does not define a complete isolation, depressurization, or sample-opening sequence. Purging alone does not establish that a cell is ready to open; the applicable pressure, temperature, and isolation conditions must also be satisfied.

The gas supply system includes an interlock mechanism. Depending on the alarm category, the system may stop reaction-gas supply and notify beamline staff and safety personnel.

Automatic shutoff does not mean that residual gas has been removed or that the affected area is safe to enter. An alarm stopping or a flow reading returning to normal does not by itself establish that the experiment can restart.

The four alarm categories are:

| Category | Typical cause | Alarm indication | Reaction-gas supply response | Notification |
| --- | --- | --- | --- | --- |
| Gas leak | Gas detected by a leak detector | Red light, GAS LEAK sign, voice alarm, and rotating beacon | Automatically stopped by the interlock | Beamline staff and safety personnel are automatically notified |
| Severe fault | Temperature rise in the flammable-gas cylinder cabinet, indicating a possible fire | Red light, rotating beacon, and buzzer | Automatically stopped by the interlock | Beamline staff and safety personnel are automatically notified |
| Moderate fault | Abnormal supply or purge pressure, dilution or exhaust flow, ventilation or abatement failure, earthquake, power failure, or manual emergency shutoff | Yellow light, rotating beacon, and buzzer | Automatically stopped | Beamline staff and safety personnel are notified |
| Minor fault | Low N2 or He cylinder supply, gas-detector fault, or abatement replacement warning | Yellow light and buzzer | Reaction-gas cylinder main valves are not automatically emergency-closed for this category | A gas-detector fault triggers automatic notification to beamline staff and safety personnel; other faults require experimenter notification as specified in SOP.md, Section 15.2.2.4 |

The alarm category describes the abnormal condition and system response. A moderate or minor classification does not mean that the experiment may continue or that the alarm can be ignored.

##### 15.2.5.1. Emergency Responsibilities and Related SOP

Emergency response is shared among experimenters, the experiment's responsible person, BL14B2 staff, and safety personnel.

| Role | Responsibility |
| --- | --- |
| Experimenters | Recognize alarms and carry out the evacuation, notification, and experiment-stop actions specified for the alarm category in the SOP |
| Experiment's responsible person | Remain available on site and coordinate the experiment group's response with staff |
| BL14B2 staff | Provide beamline-specific guidance and coordinate follow-up and reporting |
| Safety personnel | Investigate hazardous conditions, arrange corrective action, and confirm whether the affected area is safe for re-entry |

Leak investigation, repairs, interlock recovery, re-entry, and experiment restart require the designated personnel and the applicable procedures. These responsibilities are not transferred to experimenters by the automatic operation of an interlock.

This Introduction section explains the alarm categories, system behavior, and division of responsibilities. The corresponding actions are provided in SOP.md:

| Situation | SOP section |
| --- | --- |
| Gas leak | 15.2.2.1 |
| Severe fault | 15.2.2.2 |
| Moderate fault | 15.2.2.3 |
| Minor fault | 15.2.2.4 |

SOP Section 15.2.2 specifies the supplied evacuation, notification, and response requirements. It does not provide detailed repair, interlock-reset, or complete equipment-restart procedures.

#### 15.2.6. Gas-Flow Control Program

Gas flow can be controlled using:

- MFC_multi_control_fixed2.vi

The displayed terms mean:

- SV (Set Value): the requested flow setting
- PV (Process Value): the reported flow readback

The software PV and SV may differ from the values shown by the MFC controller. Use the adjacent MFC controller display as the reference for instrument readings. When the gas differs from the calibration gas, the readback may still require the conversion described in Section 15.2.4.

During operation, users should periodically check whether PV follows SV and remains stable.

A sustained decrease in PV can indicate a blockage or another supply/control problem. It must not be treated as proof of a specific cause. Follow the applicable SOP to stop gas supply safely and contact BL14B2 staff. Do not raise pressure or flow settings to force gas through a suspected blockage.

---

## 16. BL14B2 Intranet Web Tools

### 16.2. Reference

During experiments at BL14B2, users can open several intranet tools from the browser bookmarks.

These tools support measurement checks and observation of the experimental environment.

#### 16.2.1. QXAFS monitor

QXAFS monitor displays measurement-related parameters, including:

- output-file directory
- output filename

Before each QXAFS measurement, users must confirm that the directory and filename displayed in the measurement program agree with QXAFS monitor.

If they differ, the discrepancy must be resolved before measurement. For path and filename re-entry and verification, see SOP.md, Section 6.2.1, Steps 4–5. Consult staff if the discrepancy persists.

Matching values confirm consistency between the displayed settings. They do not by themselves confirm that data have been written successfully.

#### 16.2.2. QXAFS Web Page

The QXAFS web page is a browser-based QXAFS operation interface.

Although it is not normally used as the main operation window in the workflow described here, it displays program logs during execution. Users can keep it open to review program activity during measurement.

For the documented QXAFS completion messages and non-ending state, see SOP.md, Section 6.2.1.1. For other unclear messages, provide the exact text to BL14B2 staff rather than assuming its meaning or changing settings based only on the log.

#### 16.2.3. Hutch Cameras

Two commonly used cameras show the hutch from:

- the side
- downstream of the beam

The views help users observe conditions inside the hutch during an experiment. They do not replace interlock information or the procedures required for hutch entry.

#### 16.2.4. Beamchat

Beamchat provides updates on the SPring-8 source condition.

If users miss an announcement, they can review the message log to check the reported source status. The message time should be checked when interpreting a past entry.

Source-status messages provide context for an interruption, but this section does not define beamline-specific restart actions. Restart follows the relevant SOP and staff guidance.

---

## 17. BL14B2 Standard Sample List

### 17.2. Reference

The BL14B2 standard sample list (BL14B2 標準試料リスト) is shown below. The list was confirmed on 2024-10-07 (2024.10.7 確認).

Samples marked "※" are owned by BL01B1 (BL01B1所有). For these samples, see the BL01B1 standard sample list (BL01B1 標準試料リスト):

- http://bl01b1.spring8.or.jp/tech/stdsample/standard.html

In the table, "－" means that no sample is listed for that column.

| Element | Edge | Foil | Pellet |
| --- | --- | --- | --- |
| Ca | K | － | CaCO3, Hydroxyapatite |
| Sc | K | － | － |
| Ti | K | 5 μm | Ti2O3, TiO2(rutile), TiO2(anatase), La2Ti2O7, BaTiO3, CaTiO3 |
| V | K | 10 μm | VO2, V2O5, VSi2, VB2, VC, VN, VOSO4·xH2O |
| Cr | K | 3 μm | Cr2O3, Cr2Te3, Cr(acac)3, CuCr2O4, ZnCr2O4 |
| Mn | K | 3 μm | MnO, MnO2, Mn2O3, MnSi, MnTe, KMnO4, Mn(acac)3, Li2MnO3, LiMn2O4, Li2Mn3NiO3, LiNi0.33Mn0.33Co0.33O2, C32H16MnN8 |
| Fe | K | 10 μm | α-Fe2O3, γ-Fe2O3, FeO, Fe3O4, α-FeOOH, LaFeO3, Fe3(PO4)2·8H2O, Fe(acac)3, FePO4, C32H16FeN8 |
| Co | K | 4 μm | CoO, Co3O4, CoS, CoSb, Co(acac)3, LiCoO2, LiNi0.8Co0.2O2, LiNi0.33Mn0.33Co0.33O2, C32H16CoN8 |
| Ni | K | 5 μm | NiO, Li2Mn3NiO3, LiNiO2, LiNi0.33Mn0.33Co0.33O2, LiNi0.8Co0.2O2, C32H16NiN8 |
| Cu | K | 8 μm | CuO, Cu2O, Cu(acac)2, C32H16CuN8 |
| Zn | K | 25 μm | ZnO, Zn(acac)2·xH2O, C32H16N8Zn |
| Ga | K | － | Ga2O3, GaN |
| Ge | K | － | Ge powder, GeO2, GeS |
| As | K | － | － |
| Se | K | － | － |
| Br | K | － | ※ |
| Kr | K | － | － |
| Rb | K | － | － |
| Sr | K | － | SrCO3, SrSi2 |
| Y | K | － | Y2O3 |
| Zr | K | 25 μm | ZrO2 |
| Nb | K | 25.4 μm | Nb2O5 |
| Mo | K | 25 μm | MoO2, MoO3, Mo2C |
| Tc | K | － | － |
| Ru | K | － | Ru powder, RuO2, RuCl2(p-cymene)2, Ru(acac)3 |
| Rh | K | 25 μm | Rh2O3 |
| Pd | K | 30 μm | PdO, PdS |
| Ag | K | 30 μm | Ag2O |
| Cd | K | 50 μm | － |
| In | K | 50 μm | In2O3 |
| Sn | K | 100 μm | SnO, SnO2, ジブチルスズ ((C4H9)2Sn), 酸化オクチルスズ (C8H18OSn) |
| Sb | K | 50 μm | Sb2S3, Sb2O3, Sb2O4, Sb2O5 |
| Sb | L | － | ※ |
| Te | K | － | ※ |
| Te | L | － | ※ |
| I | K | － | ※ |
| I | L | － | － |
| Xe | K | － | － |
| Xe | L | － | － |
| Cs | K | － | ※ |
| Cs | L | － | － |
| Ba | K | － | BaCl2, BaSi2, BaAl2O4, BaTiO3, BaCO3, BaSO4, BaF2 |
| Ba | L | － | BaO, BaAl2O4, BaTiO3, BaCO3, BaSO4, BaF2 |
| La | K | － | LaAl2, LaFeO3, La2Ti2O7, approx. La2(CO3)3, LaB6, La(OH)3 |
| La | L | － | LaAl2, LaFeO3, La2Ti2O7, approx. La2(CO3)3, LaB6, La(OH)3 |
| Ce | K | － | CeO2, CePO4, CeB6 |
| Ce | L | － | CeO2, CePO4, CeB6, Ce(CH3COO)3·H2O |
| Pr | K | － | PrAlO3 |
| Pr | L | － | － |
| Nd | K | － | Nd2(C2O4)3·10H2O |
| Nd | L | － | Nd2(C2O4)3·10H2O |
| Pm | K | － | － |
| Pm | L | － | － |
| Sm | K | ※ | ※ |
| Sm | L | － | Sm2O3 |
| Eu | K | － | EuS, Eu2O3, EuAlO3 |
| Eu | L | － | EuS, Eu2O3, EuCl3, SCA, EuAlO3 |
| Gd | K | ※ | ※ |
| Gd | L | － | ※ |
| Tb | K | ※ | TbAlO3 |
| Tb | L | － | Tb4O7 |
| Dy | K | － | Dy2O3 |
| Dy | L | － | Dy2O3 |
| Ho | K | － | － |
| Ho | L | － | Ho2O3 |
| Er | K | － | Er2O3 |
| Er | L | － | Er2O3 |
| Tm | K | － | － |
| Tm | L | － | － |
| Yb | K | － | Yb2O3, YbF3 |
| Yb | L | － | Yb2O3, YbF3 |
| Lu | K | － | ※ |
| Lu | L | － | － |
| Hf | K | － | － |
| Hf | L | － | HfO2 |
| Ta | K | ※ | Ta2O5, TaB2, TaB, TaC, TaN, TaSi2 |
| Ta | L | 5 μm | Ta2O5, TaB2, TaC, TaN, TaSi2 |
| W | K | ※ | WO2, WO3 |
| W | L | 4 μm | WO2, WO3 |
| Re | L | － | － |
| Os | L | － | － |
| Ir | L | 10 μm | Ir powder, IrO2, IrSi |
| Pt | L | 6 μm | Pt Black, PtO2, PtCl2, Pt acetyl acetone, Pt(acac)2 |
| Au | L | 5 μm | Au2O3, AuCl, KAuCl4, AuClPPh3 |
| Hg | L | － | － |
| Tl | L | － | － |
| Pb | L | 8 μm | Pb3O4 |
| Bi | L | 15 μm | Bi Powder, Bi2O3, (BiO)2CO3 |

---
