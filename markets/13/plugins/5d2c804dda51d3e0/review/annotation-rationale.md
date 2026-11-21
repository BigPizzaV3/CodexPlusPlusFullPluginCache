# SwitchBot public tool annotation review

Scope: 235 public Devices MCP tools: four reads and 231 fixed device actions.

Status: reviewed SOURCE CANDIDATE. The remote MCP endpoint must be deployed before it advertises these annotations. Uploading this ZIP does not update tools/list. No submission for review is authorized.

All four MCP hints are explicit booleans. Account/catalog scope is closed except the image upload that accepts an external image URL. Device controls remain destructive because they overwrite settings, stop/cancel work or cause irreversible physical/media effects. Incidental request logs are separate from the business operation.

References: https://developers.openai.com/plugins/plugin-guidelines#correct-annotation and https://developers.openai.com/plugins/plan/tools#plan-safety-annotations . Public guidance no longer requires justifications, but the review email and task request ask for them. Each tool includes grounds in the namespaced _meta field com.switchbot/annotationJustifications and in this report.

Code evidence: internal/home/public_tools.go (fixed actions, ownership/model/scope checks); queries.go (reads); parameters.go (URL-capable image sources and relative timers); client.go (GET/POST paths); catalog.json (command behavior); annotation_policy.go (classification). No real device actions are executed by the exporter or mock tests.

Non-idempotent classifications for IR, latch pulses, robot jobs and media/session actions conservatively avoid promising safe replay. They do not claim repeated physical effects were measured on every model and firmware.

| Tool | Read only | Destructive | Idempotent | Open world |
| --- | --- | --- | --- | --- |
| add_water_for_humi_physical_floor_cleaning_robot_s10 | false | true | false | false |
| back_home_physical_kata_friends | false | true | false | false |
| brightness_down_ir_light | false | true | false | false |
| brightness_up_ir_light | false | true | false | false |
| cancel_custom_physical_weather_station | false | true | true | false |
| change_param_physical_floor_cleaning_robot_s10 | false | true | true | false |
| change_param_physical_robot_vacuum_cleaner_k10_pro_combo | false | true | true | false |
| change_param_physical_robot_vacuum_cleaner_k11 | false | true | true | false |
| change_param_physical_robot_vacuum_cleaner_k20_plus_pro | false | true | true | false |
| channel_add_ir_tv | false | true | false | false |
| channel_sub_ir_tv | false | true | false | false |
| child_lock_physical_kata_friends | false | true | true | false |
| close_delay_physical_battery_circulator_fan | false | true | false | false |
| close_down_physical_blind_tilt | false | true | true | false |
| close_physical_garage_door | false | true | false | false |
| close_up_physical_blind_tilt | false | true | true | false |
| custom_page_physical_weather_station | false | true | true | false |
| custom_quote_physical_weather_station | false | true | true | false |
| deadbolt_physical_smart_lock | false | true | false | false |
| deadbolt_physical_smart_lock_lite | false | true | false | false |
| deadbolt_physical_smart_lock_pro | false | true | false | false |
| deadbolt_physical_smart_lock_pro_wifi | false | true | false | false |
| deadbolt_physical_smart_lock_ultra | false | true | false | false |
| disable_motion_detection_physical_video_doorbell | false | true | true | false |
| dock_physical_floor_cleaning_robot_s10 | false | true | false | false |
| dock_physical_robot_vacuum_cleaner_k10_pro_combo | false | true | false | false |
| dock_physical_robot_vacuum_cleaner_k11 | false | true | false | false |
| dock_physical_robot_vacuum_cleaner_k20_plus_pro | false | true | false | false |
| dock_physical_robot_vacuum_cleaner_s1 | false | true | false | false |
| enable_motion_detection_physical_video_doorbell | false | true | true | false |
| fast_forward_ir_dvd | false | true | false | false |
| fully_open_physical_blind_tilt | false | true | true | false |
| get_device_info | true | false | true | false |
| get_device_status | true | false | true | false |
| high_speed_ir_fan | false | true | false | false |
| list_devices | true | false | true | false |
| lock_physical_lock_vision | false | true | true | false |
| lock_physical_lock_vision_pro | false | true | true | false |
| lock_physical_smart_lock | false | true | true | false |
| lock_physical_smart_lock_lite | false | true | true | false |
| lock_physical_smart_lock_pro | false | true | true | false |
| lock_physical_smart_lock_pro_wifi | false | true | true | false |
| lock_physical_smart_lock_ultra | false | true | true | false |
| low_speed_ir_fan | false | true | false | false |
| middle_speed_ir_fan | false | true | false | false |
| mode_physical_kata_friends | false | true | true | false |
| next_ir_dvd | false | true | false | false |
| next_physical_ai_art_frame | false | true | false | false |
| night_latch_unlock_physical_smart_lock_pro_wifi | false | true | false | false |
| open_physical_garage_door | false | true | false | false |
| pause_ir_dvd | false | true | false | false |
| pause_physical_curtain | false | true | true | false |
| pause_physical_floor_cleaning_robot_s10 | false | true | true | false |
| pause_physical_robot_vacuum_cleaner_k10_pro_combo | false | true | true | false |
| pause_physical_robot_vacuum_cleaner_k11 | false | true | true | false |
| pause_physical_robot_vacuum_cleaner_k20_plus_pro | false | true | true | false |
| pause_physical_roller_shade | false | true | true | false |
| picture_taking_physical_kata_friends | false | true | false | false |
| play_ir_dvd | false | true | false | false |
| press_physical_bot | false | true | false | false |
| previous_ir_dvd | false | true | false | false |
| previous_physical_ai_art_frame | false | true | false | false |
| rewind_ir_dvd | false | true | false | false |
| search_device_models | true | false | true | false |
| set_brightness_physical_candle_warmer_lamp | false | true | true | false |
| set_brightness_physical_ceiling_light | false | true | true | false |
| set_brightness_physical_color_bulb | false | true | true | false |
| set_brightness_physical_floor_lamp | false | true | true | false |
| set_brightness_physical_permanent_outdoor_lights | false | true | true | false |
| set_brightness_physical_rgbic_neon_rope_light | false | true | true | false |
| set_brightness_physical_rgbic_neon_wire_rope_light | false | true | true | false |
| set_brightness_physical_rgbicww_floor_lamp | false | true | true | false |
| set_brightness_physical_rgbicww_strip_light | false | true | true | false |
| set_brightness_physical_strip_light | false | true | true | false |
| set_brightness_physical_strip_light_3 | false | true | true | false |
| set_channel_ir_tv | false | true | false | false |
| set_child_lock_physical_air_purifier_voc | false | true | true | false |
| set_child_lock_physical_humidifier2 | false | true | true | false |
| set_color_light_brightness_physical_rgbicww_ceiling_light | false | true | true | false |
| set_color_light_rgb_physical_rgbicww_ceiling_light | false | true | true | false |
| set_color_physical_color_bulb | false | true | true | false |
| set_color_physical_floor_lamp | false | true | true | false |
| set_color_physical_permanent_outdoor_lights | false | true | true | false |
| set_color_physical_rgbic_neon_rope_light | false | true | true | false |
| set_color_physical_rgbic_neon_wire_rope_light | false | true | true | false |
| set_color_physical_rgbicww_floor_lamp | false | true | true | false |
| set_color_physical_rgbicww_strip_light | false | true | true | false |
| set_color_physical_strip_light | false | true | true | false |
| set_color_physical_strip_light_3 | false | true | true | false |
| set_color_temperature_physical_ceiling_light | false | true | true | false |
| set_color_temperature_physical_color_bulb | false | true | true | false |
| set_color_temperature_physical_floor_lamp | false | true | true | false |
| set_color_temperature_physical_permanent_outdoor_lights | false | true | true | false |
| set_color_temperature_physical_rgbicww_floor_lamp | false | true | true | false |
| set_color_temperature_physical_rgbicww_strip_light | false | true | true | false |
| set_color_temperature_physical_strip_light_3 | false | true | true | false |
| set_main_light_brightness_physical_rgbicww_ceiling_light | false | true | true | false |
| set_main_light_color_temp_physical_rgbicww_ceiling_light | false | true | true | false |
| set_manual_mode_temperature_physical_smart_radiator_thermostat | false | true | true | false |
| set_mode_physical_air_purifier_voc | false | true | true | false |
| set_mode_physical_humidifier | false | true | true | false |
| set_mode_physical_humidifier2 | false | true | true | false |
| set_mode_physical_relay_switch_1 | false | true | true | false |
| set_mode_physical_relay_switch_1_pm | false | true | true | false |
| set_mode_physical_relay_switch_2_pm | false | true | true | false |
| set_mode_physical_smart_radiator_thermostat | false | true | true | false |
| set_mop_washing_or_drying_physical_floor_cleaning_robot_s10 | false | true | false | false |
| set_mute_ir_dvd | false | true | false | false |
| set_night_light_mode_physical_battery_circulator_fan | false | true | true | false |
| set_night_light_mode_physical_battery_circulator_fan_2_pro | false | true | true | false |
| set_oscillation_physical_battery_circulator_fan | false | true | true | false |
| set_position_physical_blind_tilt | false | true | true | false |
| set_position_physical_curtain | false | true | true | false |
| set_position_physical_relay_switch_2_pm | false | true | true | false |
| set_position_physical_roller_shade | false | true | true | false |
| set_suction_level_physical_robot_vacuum_cleaner_s1 | false | true | true | false |
| set_temperature_mode_fan_and_power_ir_air_conditioner | false | true | false | false |
| set_vertical_oscillation_physical_battery_circulator_fan | false | true | true | false |
| set_volume_physical_floor_cleaning_robot_s10 | false | true | true | false |
| set_volume_physical_robot_vacuum_cleaner_k10_pro_combo | false | true | true | false |
| set_volume_physical_robot_vacuum_cleaner_k11 | false | true | true | false |
| set_volume_physical_robot_vacuum_cleaner_k20_plus_pro | false | true | true | false |
| set_wind_mode_physical_battery_circulator_fan | false | true | true | false |
| set_wind_mode_physical_battery_circulator_fan_2_pro | false | true | true | false |
| set_wind_speed_physical_battery_circulator_fan | false | true | true | false |
| set_wind_speed_physical_battery_circulator_fan_2_pro | false | true | true | false |
| snapshots_physical_kata_friends | false | true | false | false |
| start_clean_physical_floor_cleaning_robot_s10 | false | true | false | false |
| start_clean_physical_robot_vacuum_cleaner_k10_pro_combo | false | true | false | false |
| start_clean_physical_robot_vacuum_cleaner_k11 | false | true | false | false |
| start_clean_physical_robot_vacuum_cleaner_k20_plus_pro | false | true | false | false |
| start_physical_robot_vacuum_cleaner_s1 | false | true | false | false |
| stop_ir_dvd | false | true | false | false |
| stop_physical_robot_vacuum_cleaner_s1 | false | true | true | false |
| swing_ir_fan | false | true | false | false |
| talk_physical_kata_friends | false | true | false | false |
| timer_ir_fan | false | true | false | false |
| toggle_physical_battery_circulator_fan | false | true | false | false |
| toggle_physical_candle_warmer_lamp | false | true | false | false |
| toggle_physical_ceiling_light | false | true | false | false |
| toggle_physical_color_bulb | false | true | false | false |
| toggle_physical_floor_lamp | false | true | false | false |
| toggle_physical_permanent_outdoor_lights | false | true | false | false |
| toggle_physical_plug_mini_eu | false | true | false | false |
| toggle_physical_plug_mini_us | false | true | false | false |
| toggle_physical_relay_switch_1 | false | true | false | false |
| toggle_physical_relay_switch_1_pm | false | true | false | false |
| toggle_physical_relay_switch_2_pm | false | true | false | false |
| toggle_physical_rgbic_neon_rope_light | false | true | false | false |
| toggle_physical_rgbic_neon_wire_rope_light | false | true | false | false |
| toggle_physical_rgbicww_ceiling_light | false | true | false | false |
| toggle_physical_rgbicww_floor_lamp | false | true | false | false |
| toggle_physical_rgbicww_strip_light | false | true | false | false |
| toggle_physical_strip_light | false | true | false | false |
| toggle_physical_strip_light_3 | false | true | false | false |
| turn_off_color_light_physical_rgbicww_ceiling_light | false | true | true | false |
| turn_off_ir_air_conditioner | false | true | false | false |
| turn_off_ir_dvd | false | true | false | false |
| turn_off_ir_fan | false | true | false | false |
| turn_off_ir_light | false | true | false | false |
| turn_off_ir_tv | false | true | false | false |
| turn_off_main_light_physical_rgbicww_ceiling_light | false | true | true | false |
| turn_off_physical_air_purifier_voc | false | true | true | false |
| turn_off_physical_battery_circulator_fan | false | true | true | false |
| turn_off_physical_battery_circulator_fan_2_pro | false | true | true | false |
| turn_off_physical_blind_tilt | false | true | true | false |
| turn_off_physical_bot | false | true | false | false |
| turn_off_physical_candle_warmer_lamp | false | true | true | false |
| turn_off_physical_ceiling_light | false | true | true | false |
| turn_off_physical_color_bulb | false | true | true | false |
| turn_off_physical_curtain | false | true | true | false |
| turn_off_physical_floor_lamp | false | true | true | false |
| turn_off_physical_humidifier | false | true | true | false |
| turn_off_physical_humidifier2 | false | true | true | false |
| turn_off_physical_permanent_outdoor_lights | false | true | true | false |
| turn_off_physical_plug | false | true | true | false |
| turn_off_physical_plug_mini_eu | false | true | true | false |
| turn_off_physical_plug_mini_us | false | true | true | false |
| turn_off_physical_relay_switch_1 | false | true | true | false |
| turn_off_physical_relay_switch_1_pm | false | true | true | false |
| turn_off_physical_relay_switch_2_pm | false | true | true | false |
| turn_off_physical_rgbic_neon_rope_light | false | true | true | false |
| turn_off_physical_rgbic_neon_wire_rope_light | false | true | true | false |
| turn_off_physical_rgbicww_ceiling_light | false | true | true | false |
| turn_off_physical_rgbicww_floor_lamp | false | true | true | false |
| turn_off_physical_rgbicww_strip_light | false | true | true | false |
| turn_off_physical_smart_radiator_thermostat | false | true | true | false |
| turn_off_physical_strip_light | false | true | true | false |
| turn_off_physical_strip_light_3 | false | true | true | false |
| turn_on_color_light_physical_rgbicww_ceiling_light | false | true | true | false |
| turn_on_ir_air_conditioner | false | true | false | false |
| turn_on_ir_dvd | false | true | false | false |
| turn_on_ir_fan | false | true | false | false |
| turn_on_ir_light | false | true | false | false |
| turn_on_ir_tv | false | true | false | false |
| turn_on_main_light_physical_rgbicww_ceiling_light | false | true | true | false |
| turn_on_physical_air_purifier_voc | false | true | true | false |
| turn_on_physical_battery_circulator_fan | false | true | true | false |
| turn_on_physical_battery_circulator_fan_2_pro | false | true | true | false |
| turn_on_physical_blind_tilt | false | true | true | false |
| turn_on_physical_bot | false | true | false | false |
| turn_on_physical_candle_warmer_lamp | false | true | true | false |
| turn_on_physical_ceiling_light | false | true | true | false |
| turn_on_physical_color_bulb | false | true | true | false |
| turn_on_physical_curtain | false | true | true | false |
| turn_on_physical_floor_lamp | false | true | true | false |
| turn_on_physical_humidifier | false | true | true | false |
| turn_on_physical_humidifier2 | false | true | true | false |
| turn_on_physical_permanent_outdoor_lights | false | true | true | false |
| turn_on_physical_plug | false | true | true | false |
| turn_on_physical_plug_mini_eu | false | true | true | false |
| turn_on_physical_plug_mini_us | false | true | true | false |
| turn_on_physical_relay_switch_1 | false | true | true | false |
| turn_on_physical_relay_switch_1_pm | false | true | true | false |
| turn_on_physical_relay_switch_2_pm | false | true | true | false |
| turn_on_physical_rgbic_neon_rope_light | false | true | true | false |
| turn_on_physical_rgbic_neon_wire_rope_light | false | true | true | false |
| turn_on_physical_rgbicww_ceiling_light | false | true | true | false |
| turn_on_physical_rgbicww_floor_lamp | false | true | true | false |
| turn_on_physical_rgbicww_strip_light | false | true | true | false |
| turn_on_physical_smart_radiator_thermostat | false | true | true | false |
| turn_on_physical_strip_light | false | true | true | false |
| turn_on_physical_strip_light_3 | false | true | true | false |
| unlock_physical_lock_vision | false | true | false | false |
| unlock_physical_lock_vision_pro | false | true | false | false |
| unlock_physical_smart_lock | false | true | false | false |
| unlock_physical_smart_lock_lite | false | true | false | false |
| unlock_physical_smart_lock_pro | false | true | false | false |
| unlock_physical_smart_lock_pro_wifi | false | true | false | false |
| unlock_physical_smart_lock_ultra | false | true | false | false |
| upload_image_physical_ai_art_frame | false | true | false | true |
| volume_add_ir_dvd | false | true | false | false |
| volume_add_ir_tv | false | true | false | false |
| volume_sub_ir_dvd | false | true | false | false |
| volume_sub_ir_tv | false | true | false | false |

## add_water_for_humi_physical_floor_cleaning_robot_s10

Refill the humidifier water tank on one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Refill the humidifier water tank on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## back_home_physical_kata_friends

Command Kata to return home on one physical Kata Friends owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Command Kata to return home on one physical Kata Friends. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## brightness_down_ir_light

Brightness down on one ir Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Brightness down on one ir Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## brightness_up_ir_light

Brightness up on one ir Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Brightness up on one ir Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## cancel_custom_physical_weather_station

Revert to default quote display on one physical WeatherStation owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Revert to default quote display on one physical WeatherStation. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## change_param_physical_floor_cleaning_robot_s10

Change parameters mid-run on one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Change parameters mid-run on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## change_param_physical_robot_vacuum_cleaner_k10_pro_combo

Change parameters mid-run on one physical Robot Vacuum Cleaner K10+ Pro Combo owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Change parameters mid-run on one physical Robot Vacuum Cleaner K10+ Pro Combo. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## change_param_physical_robot_vacuum_cleaner_k11

Change parameters mid-run on one physical Robot Vacuum Cleaner K11+ owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Change parameters mid-run on one physical Robot Vacuum Cleaner K11+. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## change_param_physical_robot_vacuum_cleaner_k20_plus_pro

Change parameters mid-run on one physical Robot Vacuum Cleaner K20 Plus Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Change parameters mid-run on one physical Robot Vacuum Cleaner K20 Plus Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## channel_add_ir_tv

Channel up on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Channel up on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## channel_sub_ir_tv

Channel down on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Channel down on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## child_lock_physical_kata_friends

Toggle child lock on one physical Kata Friends owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle child lock on one physical Kata Friends. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## close_delay_physical_battery_circulator_fan

Auto-off timer in seconds on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Compatibility: The legacy gray/converter path rejects closeDelay. Other upstream paths are not certified; this note does not block explicit execution.

- readOnlyHint=false: Auto-off timer in seconds on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: A relative auto-off timer is scheduled from the time of each call; repeating it can move the deadline.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## close_down_physical_blind_tilt

Close down on one physical Blind Tilt owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Close down on one physical Blind Tilt. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## close_physical_garage_door

Close the garage door on one physical Garage Door Opener owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Close the garage door on one physical Garage Door Opener. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Can actuate a physical button or garage-door mechanism again; the tool does not verify the device's current mode/state or suppress duplicate actuation.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## close_up_physical_blind_tilt

Close up on one physical Blind Tilt owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Close up on one physical Blind Tilt. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## custom_page_physical_weather_station

Set a custom page text on one physical WeatherStation owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set a custom page text on one physical WeatherStation. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## custom_quote_physical_weather_station

Set a custom quote on the display on one physical WeatherStation owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set a custom quote on the display on one physical WeatherStation. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## deadbolt_physical_smart_lock

Disengage the deadbolt or latch on one physical Smart Lock owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disengage the deadbolt or latch on one physical Smart Lock. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## deadbolt_physical_smart_lock_lite

Disengage the deadbolt or latch on one physical Smart Lock Lite owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disengage the deadbolt or latch on one physical Smart Lock Lite. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## deadbolt_physical_smart_lock_pro

Disengage the deadbolt or latch on one physical Smart Lock Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disengage the deadbolt or latch on one physical Smart Lock Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## deadbolt_physical_smart_lock_pro_wifi

Disengage the deadbolt or latch on one physical Smart Lock Pro Wifi owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disengage the deadbolt or latch on one physical Smart Lock Pro Wifi. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## deadbolt_physical_smart_lock_ultra

Disengage the deadbolt or latch on one physical Smart Lock Ultra owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disengage the deadbolt or latch on one physical Smart Lock Ultra. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## disable_motion_detection_physical_video_doorbell

Disable motion detection on one physical Video Doorbell owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disable motion detection on one physical Video Doorbell. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## dock_physical_floor_cleaning_robot_s10

Return to dock on one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Return to dock on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## dock_physical_robot_vacuum_cleaner_k10_pro_combo

Return to dock on one physical Robot Vacuum Cleaner K10+ Pro Combo owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Return to dock on one physical Robot Vacuum Cleaner K10+ Pro Combo. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## dock_physical_robot_vacuum_cleaner_k11

Return to dock on one physical Robot Vacuum Cleaner K11+ owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Return to dock on one physical Robot Vacuum Cleaner K11+. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## dock_physical_robot_vacuum_cleaner_k20_plus_pro

Return to dock on one physical Robot Vacuum Cleaner K20 Plus Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Return to dock on one physical Robot Vacuum Cleaner K20 Plus Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## dock_physical_robot_vacuum_cleaner_s1

Return to dock on one physical Robot Vacuum Cleaner S1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Return to dock on one physical Robot Vacuum Cleaner S1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## enable_motion_detection_physical_video_doorbell

Enable motion detection on one physical Video Doorbell owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Enable motion detection on one physical Video Doorbell. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## fast_forward_ir_dvd

Fast forward on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Fast forward on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## fully_open_physical_blind_tilt

Open fully on one physical Blind Tilt owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Open fully on one physical Blind Tilt. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## get_device_info

Read descriptive metadata and known status-field meanings for one owned device. Does not read live status or execute controls. Catalog metadata is not firmware certification.

- readOnlyHint=true: Checks ownership and returns inventory and built-in descriptive model/status-field metadata; no live-status or control request is sent. No device, user content, setting, or stateful job is changed.

- destructiveHint=false: Retrieval only: nothing is deleted, overwritten, cancelled, or sent as a device action.

- idempotentHint=true: Repeating the same read creates no additional business effect; returned inventory/status may naturally change over time. Internal request logging does not change the tool's business operation.

- openWorldHint=false: Confined to the authenticated user's bounded private inventory or the built-in catalog. The service's use of HTTPS does not make the entity scope open-ended.

## get_device_status

Read current cloud status of one device owned by the user. Missing fields are unknown. Infrared remotes have no real state channel. This does not change device settings.

- readOnlyHint=true: Checks ownership and reads stored cloud status for that user's one physical device; it does not send a refresh or control command. No device, user content, setting, or stateful job is changed.

- destructiveHint=false: Retrieval only: nothing is deleted, overwritten, cancelled, or sent as a device action.

- idempotentHint=true: Repeating the same read creates no additional business effect; returned inventory/status may naturally change over time. Internal request logging does not change the tool's business operation.

- openWorldHint=false: Confined to the authenticated user's bounded private inventory or the built-in catalog. The service's use of HTTPS does not make the entity scope open-ended.

## high_speed_ir_fan

High speed on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: High speed on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## list_devices

List the current user's physical devices and infrared remotes with exact IDs and types. Missing location or cloud-service fields are unknown. This only reads inventory.

- readOnlyHint=true: Reads only the authenticated user's physical-device and infrared-remote inventory. No device, user content, setting, or stateful job is changed.

- destructiveHint=false: Retrieval only: nothing is deleted, overwritten, cancelled, or sent as a device action.

- idempotentHint=true: Repeating the same read creates no additional business effect; returned inventory/status may naturally change over time. Internal request logging does not change the tool's business operation.

- openWorldHint=false: Confined to the authenticated user's bounded private inventory or the built-in catalog. The service's use of HTTPS does not make the entity scope open-ended.

## lock_physical_lock_vision

Lock the door on one physical Lock Vision owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Lock Vision. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## lock_physical_lock_vision_pro

Lock the door on one physical Lock Vision Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Lock Vision Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## lock_physical_smart_lock

Lock the door on one physical Smart Lock owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Smart Lock. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## lock_physical_smart_lock_lite

Lock the door on one physical Smart Lock Lite owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Smart Lock Lite. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## lock_physical_smart_lock_pro

Lock the door on one physical Smart Lock Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Smart Lock Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## lock_physical_smart_lock_pro_wifi

Lock the door on one physical Smart Lock Pro Wifi owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Smart Lock Pro Wifi. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## lock_physical_smart_lock_ultra

Lock the door on one physical Smart Lock Ultra owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Lock the door on one physical Smart Lock Ultra. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## low_speed_ir_fan

Low speed on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Low speed on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## middle_speed_ir_fan

Medium speed on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Medium speed on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## mode_physical_kata_friends

Set the operating mode on one physical Kata Friends owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set the operating mode on one physical Kata Friends. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## next_ir_dvd

Next track on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Next track on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## next_physical_ai_art_frame

Switch to the next image on one physical AI Art Frame owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Switch to the next image on one physical AI Art Frame. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## night_latch_unlock_physical_smart_lock_pro_wifi

Unlock the night latch (EU) on one physical Smart Lock Pro Wifi owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the night latch (EU) on one physical Smart Lock Pro Wifi. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## open_physical_garage_door

Open the garage door on one physical Garage Door Opener owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Open the garage door on one physical Garage Door Opener. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Can actuate a physical button or garage-door mechanism again; the tool does not verify the device's current mode/state or suppress duplicate actuation.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_ir_dvd

Pause on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Pause on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_physical_curtain

Stop movement on one physical Curtain owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Stop movement on one physical Curtain. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_physical_floor_cleaning_robot_s10

Pause cleaning on one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Pause cleaning on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_physical_robot_vacuum_cleaner_k10_pro_combo

Pause cleaning on one physical Robot Vacuum Cleaner K10+ Pro Combo owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Pause cleaning on one physical Robot Vacuum Cleaner K10+ Pro Combo. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_physical_robot_vacuum_cleaner_k11

Pause cleaning on one physical Robot Vacuum Cleaner K11+ owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Pause cleaning on one physical Robot Vacuum Cleaner K11+. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_physical_robot_vacuum_cleaner_k20_plus_pro

Pause cleaning on one physical Robot Vacuum Cleaner K20 Plus Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Pause cleaning on one physical Robot Vacuum Cleaner K20 Plus Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## pause_physical_roller_shade

Stop movement on one physical Roller Shade owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Stop movement on one physical Roller Shade. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## picture_taking_physical_kata_friends

Toggle picture taking on one physical Kata Friends owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle picture taking on one physical Kata Friends. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Controls capture or communication on the robot; repeated activation can have additional media/session effects and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## play_ir_dvd

Play on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Play on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## press_physical_bot

Press the button (momentary) on one physical Bot owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Press the button (momentary) on one physical Bot. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## previous_ir_dvd

Previous track on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Previous track on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## previous_physical_ai_art_frame

Switch to the previous image on one physical AI Art Frame owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Switch to the previous image on one physical AI Art Frame. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## rewind_ir_dvd

Rewind on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Rewind on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## search_device_models

Search device model names, aliases, descriptions and known status fields in a versioned catalog. Returns descriptive reference data only, not control commands or executable schemas. Does not query owned devices, read live status, or certify firmware compatibility. total counts returned results.

- readOnlyHint=true: Searches the embedded, versioned device catalog; it neither queries arbitrary URLs nor executes device operations. No device, user content, setting, or stateful job is changed.

- destructiveHint=false: Retrieval only: nothing is deleted, overwritten, cancelled, or sent as a device action.

- idempotentHint=true: Repeating the same read creates no additional business effect; returned inventory/status may naturally change over time. Internal request logging does not change the tool's business operation.

- openWorldHint=false: Confined to the authenticated user's bounded private inventory or the built-in catalog. The service's use of HTTPS does not make the entity scope open-ended.

## set_brightness_physical_candle_warmer_lamp

Set brightness percentage on one physical Candle Warmer Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical Candle Warmer Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_ceiling_light

Set brightness percentage on one physical Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_color_bulb

Set brightness percentage on one physical Color Bulb owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical Color Bulb. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_floor_lamp

Set brightness percentage on one physical Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_permanent_outdoor_lights

Set brightness (0-100) on one physical Permanent Outdoor Lights owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness (0-100) on one physical Permanent Outdoor Lights. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_rgbic_neon_rope_light

Set brightness percentage on one physical RGBIC Neon Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical RGBIC Neon Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_rgbic_neon_wire_rope_light

Set brightness percentage on one physical RGBIC Neon Wire Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical RGBIC Neon Wire Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_rgbicww_floor_lamp

Set brightness percentage on one physical RGBICWW Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical RGBICWW Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_rgbicww_strip_light

Set brightness percentage on one physical RGBICWW Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical RGBICWW Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_strip_light

Set brightness percentage on one physical Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_brightness_physical_strip_light_3

Set brightness percentage on one physical Strip Light 3 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set brightness percentage on one physical Strip Light 3. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_channel_ir_tv

Switch to a specific channel on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Switch to a specific channel on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_child_lock_physical_air_purifier_voc

Disable / enable child lock on one physical Air Purifier VOC owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Disable / enable child lock on one physical Air Purifier VOC. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_child_lock_physical_humidifier2

Enable or disable child lock on one physical Humidifier2 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Enable or disable child lock on one physical Humidifier2. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_light_brightness_physical_rgbicww_ceiling_light

Set color light brightness on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color light brightness on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_light_rgb_physical_rgbicww_ceiling_light

Set color light RGB color on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color light RGB color on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_color_bulb

Set RGB color, e.g. "255:0:0" on one physical Color Bulb owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical Color Bulb. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_floor_lamp

Set RGB color, e.g. "255:0:0" on one physical Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_permanent_outdoor_lights

Set RGB color on one physical Permanent Outdoor Lights owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color on one physical Permanent Outdoor Lights. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_rgbic_neon_rope_light

Set RGB color, e.g. "255:0:0" on one physical RGBIC Neon Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical RGBIC Neon Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_rgbic_neon_wire_rope_light

Set RGB color, e.g. "255:0:0" on one physical RGBIC Neon Wire Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical RGBIC Neon Wire Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_rgbicww_floor_lamp

Set RGB color, e.g. "255:0:0" on one physical RGBICWW Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical RGBICWW Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_rgbicww_strip_light

Set RGB color, e.g. "255:0:0" on one physical RGBICWW Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical RGBICWW Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_strip_light

Set RGB color, e.g. "255:0:0" on one physical Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_physical_strip_light_3

Set RGB color, e.g. "255:0:0" on one physical Strip Light 3 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set RGB color, e.g. "255:0:0" on one physical Strip Light 3. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_ceiling_light

Set color temperature (Kelvin) on one physical Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature (Kelvin) on one physical Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_color_bulb

Set color temperature (Kelvin) on one physical Color Bulb owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature (Kelvin) on one physical Color Bulb. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_floor_lamp

Set color temperature (Kelvin) on one physical Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature (Kelvin) on one physical Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_permanent_outdoor_lights

Set color temperature in Kelvin on one physical Permanent Outdoor Lights owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature in Kelvin on one physical Permanent Outdoor Lights. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_rgbicww_floor_lamp

Set color temperature (Kelvin) on one physical RGBICWW Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature (Kelvin) on one physical RGBICWW Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_rgbicww_strip_light

Set color temperature (Kelvin) on one physical RGBICWW Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature (Kelvin) on one physical RGBICWW Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_color_temperature_physical_strip_light_3

Set color temperature (Kelvin) on one physical Strip Light 3 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set color temperature (Kelvin) on one physical Strip Light 3. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_main_light_brightness_physical_rgbicww_ceiling_light

Set main light brightness on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set main light brightness on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_main_light_color_temp_physical_rgbicww_ceiling_light

Set main light color temperature (K) on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set main light color temperature (K) on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_manual_mode_temperature_physical_smart_radiator_thermostat

Target temperature in manual mode on one physical Smart Radiator Thermostat owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Target temperature in manual mode on one physical Smart Radiator Thermostat. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_air_purifier_voc

mode: 1=normal 2=auto 3=sleep 4=pet; fanGear only when mode=1 on one physical Air Purifier VOC owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: mode: 1=normal 2=auto 3=sleep 4=pet; fanGear only when mode=1 on one physical Air Purifier VOC. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_humidifier

Set preset or target humidity on one physical Humidifier owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set preset or target humidity on one physical Humidifier. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_humidifier2

mode: 1=lv4 2=lv3 3=lv2 4=lv1 5=humidity 6=sleep 7=auto 8=drying on one physical Humidifier2 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: mode: 1=lv4 2=lv3 3=lv2 4=lv1 5=humidity 6=sleep 7=auto 8=drying on one physical Humidifier2. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_relay_switch_1

Switch operating mode on one physical Relay Switch 1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Switch operating mode on one physical Relay Switch 1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_relay_switch_1_pm

Switch operating mode on one physical Relay Switch 1PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Switch operating mode on one physical Relay Switch 1PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_relay_switch_2_pm

Per-channel mode (see Relay Switch 1 modes) on one physical Relay Switch 2PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Per-channel mode (see Relay Switch 1 modes) on one physical Relay Switch 2PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mode_physical_smart_radiator_thermostat

Operating mode on one physical Smart Radiator Thermostat owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Operating mode on one physical Smart Radiator Thermostat. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mop_washing_or_drying_physical_floor_cleaning_robot_s10

Wash or dry the robot's mop, or stop its current mop maintenance cycle. value = 1 starts mop washing, 2 starts drying, and 3 stops self-cleaning. This does not start a floor-cleaning session. Applies to one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: 1=wash mop | 2=dry | 3=terminate self-clean on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_mute_ir_dvd

Toggle mute on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Toggle mute on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_night_light_mode_physical_battery_circulator_fan

Night-light mode on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Night-light mode on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_night_light_mode_physical_battery_circulator_fan_2_pro

Night-light mode on one physical Battery Circulator Fan 2 Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Night-light mode on one physical Battery Circulator Fan 2 Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_oscillation_physical_battery_circulator_fan

Enable or disable the fan head's automatic side-to-side movement. value = on enables horizontal oscillation; value = off stops horizontal oscillation. This changes horizontal oscillation only, not fan power, speed or vertical oscillation. Compatibility is verified for the legacy gray/converter path only. Applies to one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set horizontal oscillation; verified for the legacy gray/converter path only on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_position_physical_blind_tilt

Tilt direction + angle (0=closed, 100=open) on one physical Blind Tilt owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Tilt direction + angle (0=closed, 100=open) on one physical Blind Tilt. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_position_physical_curtain

Move to a position on one physical Curtain owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Move to a position on one physical Curtain. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_position_physical_relay_switch_2_pm

Move the roller shade connected to a Relay Switch 2PM to the target position percentage. value is an integer from 0 to 100. The relay must already be configured in roller-shade-pair mode. This moves the shade; it does not change the relay mode or independently switch a channel on or off. Applies to one physical Relay Switch 2PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Roller-shade-pair mode only on one physical Relay Switch 2PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_position_physical_roller_shade

Move to a position on one physical Roller Shade owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Move to a position on one physical Roller Shade. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_suction_level_physical_robot_vacuum_cleaner_s1

Set the robot vacuum's suction strength. value selects the level: 0 = Quiet, 1 = Standard, 2 = Strong, 3 = Max. Applies to one physical Robot Vacuum Cleaner S1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: 0=Quiet 1=Standard 2=Strong 3=Max on one physical Robot Vacuum Cleaner S1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_temperature_mode_fan_and_power_ir_air_conditioner

Apply the air conditioner's target temperature, operating mode, fan speed and power together in one infrared command. value is a comma-separated string: temperature,mode,fan,power. Temperature is 16-30; mode is 0 or 1 = auto, 2 = cool, 3 = dry, 4 = fan, 5 = heat; fan is 1 = auto, 2 = low, 3 = medium, 4 = high; power is on or off. Example: 26,2,3,on. Applies to one ir Air Conditioner owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: mode: 0/1=auto 2=cool 3=dry 4=fan 5=heat; fan: 1=auto 2=low 3=mid 4=high on one ir Air Conditioner. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_vertical_oscillation_physical_battery_circulator_fan

Enable or disable the fan head's automatic up-and-down movement. value = on enables vertical oscillation; value = off stops vertical oscillation. This changes vertical oscillation only, not fan power, speed or horizontal oscillation. Compatibility is verified for the legacy gray/converter path only. Applies to one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set vertical oscillation; verified for the legacy gray/converter path only on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_volume_physical_floor_cleaning_robot_s10

Set voice volume on one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set voice volume on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_volume_physical_robot_vacuum_cleaner_k10_pro_combo

Set voice volume on one physical Robot Vacuum Cleaner K10+ Pro Combo owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set voice volume on one physical Robot Vacuum Cleaner K10+ Pro Combo. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_volume_physical_robot_vacuum_cleaner_k11

Set voice volume on one physical Robot Vacuum Cleaner K11+ owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set voice volume on one physical Robot Vacuum Cleaner K11+. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_volume_physical_robot_vacuum_cleaner_k20_plus_pro

Set voice volume on one physical Robot Vacuum Cleaner K20 Plus Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Set voice volume on one physical Robot Vacuum Cleaner K20 Plus Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_wind_mode_physical_battery_circulator_fan

Wind mode on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Wind mode on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_wind_mode_physical_battery_circulator_fan_2_pro

Wind mode on one physical Battery Circulator Fan 2 Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Wind mode on one physical Battery Circulator Fan 2 Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_wind_speed_physical_battery_circulator_fan

Fan speed on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Fan speed on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## set_wind_speed_physical_battery_circulator_fan_2_pro

Fan speed on one physical Battery Circulator Fan 2 Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Fan speed on one physical Battery Circulator Fan 2 Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## snapshots_physical_kata_friends

Toggle snapshot mode on one physical Kata Friends owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle snapshot mode on one physical Kata Friends. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Controls capture or communication on the robot; repeated activation can have additional media/session effects and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## start_clean_physical_floor_cleaning_robot_s10

Begin a cleaning session on one physical Floor Cleaning Robot S10 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Begin a cleaning session on one physical Floor Cleaning Robot S10. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## start_clean_physical_robot_vacuum_cleaner_k10_pro_combo

Begin a cleaning session on one physical Robot Vacuum Cleaner K10+ Pro Combo owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Begin a cleaning session on one physical Robot Vacuum Cleaner K10+ Pro Combo. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## start_clean_physical_robot_vacuum_cleaner_k11

Begin a cleaning session on one physical Robot Vacuum Cleaner K11+ owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Begin a cleaning session on one physical Robot Vacuum Cleaner K11+. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## start_clean_physical_robot_vacuum_cleaner_k20_plus_pro

Begin a cleaning session on one physical Robot Vacuum Cleaner K20 Plus Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Begin a cleaning session on one physical Robot Vacuum Cleaner K20 Plus Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## start_physical_robot_vacuum_cleaner_s1

Start cleaning on one physical Robot Vacuum Cleaner S1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Start cleaning on one physical Robot Vacuum Cleaner S1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Dispatches a robot cleaning or navigation action; another accepted request can start or restart work and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## stop_ir_dvd

Stop on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Stop on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## stop_physical_robot_vacuum_cleaner_s1

Stop cleaning on one physical Robot Vacuum Cleaner S1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Stop cleaning on one physical Robot Vacuum Cleaner S1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## swing_ir_fan

Toggle swing on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Toggle swing on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## talk_physical_kata_friends

Toggle talk mode on one physical Kata Friends owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle talk mode on one physical Kata Friends. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Controls capture or communication on the robot; repeated activation can have additional media/session effects and is not deduplicated.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## timer_ir_fan

Toggle timer on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Toggle timer on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_battery_circulator_fan

Toggle power on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Compatibility: The legacy gray/converter path rejects toggle. Other upstream paths are not certified; this note does not block explicit execution.

- readOnlyHint=false: Toggle power on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_candle_warmer_lamp

Toggle power on one physical Candle Warmer Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Candle Warmer Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_ceiling_light

Toggle power on one physical Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_color_bulb

Toggle power on one physical Color Bulb owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Color Bulb. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_floor_lamp

Toggle power on one physical Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_permanent_outdoor_lights

Toggle power on one physical Permanent Outdoor Lights owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Permanent Outdoor Lights. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_plug_mini_eu

Toggle power on one physical Plug Mini (EU) owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Plug Mini (EU). Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_plug_mini_us

Toggle power on one physical Plug Mini (US) owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Plug Mini (US). Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_relay_switch_1

Toggle power on one physical Relay Switch 1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Relay Switch 1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_relay_switch_1_pm

Toggle power on one physical Relay Switch 1PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Relay Switch 1PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_relay_switch_2_pm

Toggle channel 1 or 2 on one physical Relay Switch 2PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle channel 1 or 2 on one physical Relay Switch 2PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_rgbic_neon_rope_light

Toggle power on one physical RGBIC Neon Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical RGBIC Neon Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_rgbic_neon_wire_rope_light

Toggle power on one physical RGBIC Neon Wire Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical RGBIC Neon Wire Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_rgbicww_ceiling_light

Toggle power on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_rgbicww_floor_lamp

Toggle power on one physical RGBICWW Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical RGBICWW Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_rgbicww_strip_light

Toggle power on one physical RGBICWW Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical RGBICWW Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_strip_light

Toggle power on one physical Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## toggle_physical_strip_light_3

Toggle power on one physical Strip Light 3 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Toggle power on one physical Strip Light 3. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: The catalog defines a momentary, relative, toggle, sequence, or maintenance action. Repeating it can produce an additional physical effect.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_color_light_physical_rgbicww_ceiling_light

Turn off the ambient color light on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Turn off the ambient color light on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_ir_air_conditioner

Power off on one ir Air Conditioner owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power off on one ir Air Conditioner. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_ir_dvd

Power off on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power off on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_ir_fan

Power off on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power off on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_ir_light

Power off on one ir Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power off on one ir Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_ir_tv

Power off on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power off on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_main_light_physical_rgbicww_ceiling_light

Turn off the main light only on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Turn off the main light only on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_air_purifier_voc

Power off on one physical Air Purifier VOC owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Air Purifier VOC. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_battery_circulator_fan

Power off on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_battery_circulator_fan_2_pro

Power off on one physical Battery Circulator Fan 2 Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Battery Circulator Fan 2 Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_blind_tilt

Power off on one physical Blind Tilt owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Blind Tilt. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_bot

Power off on one physical Bot owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Bot. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Can actuate a physical button or garage-door mechanism again; the tool does not verify the device's current mode/state or suppress duplicate actuation.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_candle_warmer_lamp

Power off on one physical Candle Warmer Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Candle Warmer Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_ceiling_light

Power off on one physical Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_color_bulb

Power off on one physical Color Bulb owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Color Bulb. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_curtain

Power off on one physical Curtain owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Curtain. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_floor_lamp

Power off on one physical Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_humidifier

Power off on one physical Humidifier owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Humidifier. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_humidifier2

Power off on one physical Humidifier2 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Humidifier2. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_permanent_outdoor_lights

Power off on one physical Permanent Outdoor Lights owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Permanent Outdoor Lights. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_plug

Power off on one physical Plug owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Plug. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_plug_mini_eu

Power off on one physical Plug Mini (EU) owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Plug Mini (EU). Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_plug_mini_us

Power off on one physical Plug Mini (US) owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Plug Mini (US). Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_relay_switch_1

Power off on one physical Relay Switch 1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Relay Switch 1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_relay_switch_1_pm

Power off on one physical Relay Switch 1PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Relay Switch 1PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_relay_switch_2_pm

Turn off channel 1 or 2 on one physical Relay Switch 2PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Turn off channel 1 or 2 on one physical Relay Switch 2PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_rgbic_neon_rope_light

Power off on one physical RGBIC Neon Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical RGBIC Neon Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_rgbic_neon_wire_rope_light

Power off on one physical RGBIC Neon Wire Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical RGBIC Neon Wire Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_rgbicww_ceiling_light

Power off on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_rgbicww_floor_lamp

Power off on one physical RGBICWW Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical RGBICWW Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_rgbicww_strip_light

Power off on one physical RGBICWW Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical RGBICWW Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_smart_radiator_thermostat

Power off on one physical Smart Radiator Thermostat owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Smart Radiator Thermostat. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_strip_light

Power off on one physical Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_off_physical_strip_light_3

Power off on one physical Strip Light 3 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power off on one physical Strip Light 3. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_color_light_physical_rgbicww_ceiling_light

Turn on the ambient color light on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Turn on the ambient color light on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_ir_air_conditioner

Power on on one ir Air Conditioner owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power on on one ir Air Conditioner. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_ir_dvd

Power on on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power on on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_ir_fan

Power on on one ir Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power on on one ir Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_ir_light

Power on on one ir Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power on on one ir Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_ir_tv

Power on on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Power on on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_main_light_physical_rgbicww_ceiling_light

Turn on the main light only on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Turn on the main light only on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_air_purifier_voc

Power on on one physical Air Purifier VOC owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Air Purifier VOC. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_battery_circulator_fan

Power on on one physical Battery Circulator Fan owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Battery Circulator Fan. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_battery_circulator_fan_2_pro

Power on on one physical Battery Circulator Fan 2 Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Battery Circulator Fan 2 Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_blind_tilt

Power on on one physical Blind Tilt owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Blind Tilt. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_bot

Power on on one physical Bot owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Bot. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Can actuate a physical button or garage-door mechanism again; the tool does not verify the device's current mode/state or suppress duplicate actuation.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_candle_warmer_lamp

Power on on one physical Candle Warmer Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Candle Warmer Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_ceiling_light

Power on on one physical Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_color_bulb

Power on on one physical Color Bulb owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Color Bulb. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_curtain

Power on on one physical Curtain owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Curtain. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_floor_lamp

Power on on one physical Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_humidifier

Power on on one physical Humidifier owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Humidifier. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_humidifier2

Power on on one physical Humidifier2 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Humidifier2. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_permanent_outdoor_lights

Power on on one physical Permanent Outdoor Lights owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Permanent Outdoor Lights. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_plug

Power on on one physical Plug owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Plug. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_plug_mini_eu

Power on on one physical Plug Mini (EU) owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Plug Mini (EU). Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_plug_mini_us

Power on on one physical Plug Mini (US) owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Plug Mini (US). Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_relay_switch_1

Power on on one physical Relay Switch 1 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Relay Switch 1. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_relay_switch_1_pm

Power on on one physical Relay Switch 1PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Relay Switch 1PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_relay_switch_2_pm

Turn on channel 1 or 2 on one physical Relay Switch 2PM owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Turn on channel 1 or 2 on one physical Relay Switch 2PM. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_rgbic_neon_rope_light

Power on on one physical RGBIC Neon Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical RGBIC Neon Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_rgbic_neon_wire_rope_light

Power on on one physical RGBIC Neon Wire Rope Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical RGBIC Neon Wire Rope Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_rgbicww_ceiling_light

Power on on one physical RGBICWW Ceiling Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical RGBICWW Ceiling Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_rgbicww_floor_lamp

Power on on one physical RGBICWW Floor Lamp owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical RGBICWW Floor Lamp. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_rgbicww_strip_light

Power on on one physical RGBICWW Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical RGBICWW Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_smart_radiator_thermostat

Power on on one physical Smart Radiator Thermostat owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Smart Radiator Thermostat. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_strip_light

Power on on one physical Strip Light owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Strip Light. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## turn_on_physical_strip_light_3

Power on on one physical Strip Light 3 owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Power on on one physical Strip Light 3. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=true: Sets the same absolute device state/setting (or stops movement) with the same arguments; repetition does not add a second relative action. This does not authorize automatic retry after an unknown outcome.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_lock_vision

Unlock the door on one physical Lock Vision owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Lock Vision. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_lock_vision_pro

Unlock the door on one physical Lock Vision Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Lock Vision Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_smart_lock

Unlock the door on one physical Smart Lock owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Smart Lock. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_smart_lock_lite

Unlock the door on one physical Smart Lock Lite owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Smart Lock Lite. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_smart_lock_pro

Unlock the door on one physical Smart Lock Pro owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Smart Lock Pro. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_smart_lock_pro_wifi

Unlock the door on one physical Smart Lock Pro Wifi owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Smart Lock Pro Wifi. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## unlock_physical_smart_lock_ultra

Unlock the door on one physical Smart Lock Ultra owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Unlock the door on one physical Smart Lock Ultra. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: May actuate a door latch again or extend an unlocking/auto-relock interval; no replay-suppression guarantee exists.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## upload_image_physical_ai_art_frame

Upload a new image from exactly one URL or base64 image source. on one physical AI Art Frame owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action.

- readOnlyHint=false: Upload a new image from exactly one URL or base64 image source. on one physical AI Art Frame. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Another accepted call uploads/processes an image again. A URL's content can change, and the backend does not expose an idempotency key.

- openWorldHint=true: Although the target frame is owned by the authenticated user, imageUrl accepts a caller-selected external source that may be fetched by the downstream image service. The tool therefore includes open-ended external entities; imageBase64 does not remove that capability.

## volume_add_ir_dvd

Volume up on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Volume up on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## volume_add_ir_tv

Volume up on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Volume up on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## volume_sub_ir_dvd

Volume down on one ir DVD owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Volume down on one ir DVD. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.

## volume_sub_ir_tv

Volume down on one ir TV owned by the user. Performs only this action. Device model and input are validated before sending. Acceptance does not prove physical execution; do not automatically repeat a timed-out action. Sends infrared through the linked hub; there is no receipt or state acknowledgment.

- readOnlyHint=false: Volume down on one ir TV. Sends a state-changing device command, not a read or dry-run preview.

- destructiveHint=true: The command can overwrite a current setting, stop/cancel an action, or cause an irreversible physical/media transmission. It is not a purely additive, non-destructive write; reversibility does not remove these effects.

- idempotentHint=false: Every call sends another infrared transmission through the hub. Learned remote behavior has no state acknowledgment or replay deduplication, so repeated physical effects are not guaranteed to be idempotent.

- openWorldHint=false: The server checks the authenticated user's inventory and exact device model before sending one fixed command to that owned device. No arbitrary recipient, scene, operation, or URL can be selected.
