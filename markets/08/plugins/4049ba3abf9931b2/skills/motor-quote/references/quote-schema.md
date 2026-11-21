# Quote submission reference

Use this reference only to validate and construct `submit_insurance_quote_request`. Ask users questions in natural language and translate their answers to these exact values.

## `car_basics`

| Field | Type | Rule |
| --- | --- | --- |
| `registration` | string | Confirmed UK registration supplied by the user. |
| `abi_code` | string | Copy `abi_code` from the confirmed `lookup_car_by_registration` result. Never invent it. |
| `registration_date` | `YYYY-MM-DD` or null | Copy `registration_date` from the confirmed lookup result. |
| `date_purchased` | `YYYY-MM-DD` | Date the customer bought or started to lease the car. Must be on or after the confirmed registration date and cannot be in the future. |

## `personal_details`

| Field | Type | Accepted values or rule |
| --- | --- | --- |
| `title` | string | `Mr`, `Mrs`, `Miss`, `Ms`, `Dr`, `Mx` |
| `first_name` | string | At least two characters and no digits. |
| `surname` | string | At least two characters and no digits. |
| `email` | string | Valid email address. |
| `date_of_birth` | `YYYY-MM-DD` | Customer must be at least 17 years old. |
| `address` | object | Copy the user-confirmed address lookup result using the fields below. |

Address fields:

- `organisation`: string; use an empty string when the lookup returns no value.
- `sub_premises`: string; use an empty string when the lookup returns no value.
- `house_name`: string; use an empty string when the lookup returns no value.
- `house_number`: string; use an empty string when the lookup returns no value.
- `street`: string.
- `postal_town`: string.
- `county`: string.
- `postcode`: valid UK postcode.

Do not construct an address from general knowledge. Use only a result returned by `lookup_address_by_postcode` and confirmed by the user.

## `about_you`

| Field | Type | Accepted values or rule |
| --- | --- | --- |
| `marital_status` | string | `Married`, `Single`, `LivingWithPartner`, `Widowed`, `Divorced`, `Separated` |
| `occupation` | string | Free-text job title supplied by the customer. |
| `other_vehicle_access` | string | `No`, `YesAccessTo`, `YesOwn`, `YesNamedDriver` |

Map natural answers such as "living with my partner", "I own another car", or "I'm a named driver on my partner's car" to the corresponding exact literal only when the meaning is unambiguous.

## `driving_history`

| Field | Type | Accepted values or rule |
| --- | --- | --- |
| `licence_type` | string | `FullUK`, `FullUKAuto`, `ProvisionalUK`, `FullECEEA`, `ProvisionalECEEA`, `IssuedOutsideUKECEEA`, `Other` |
| `licence_held_years` | integer | From 0 through 80. Combined with `licence_held_months`, it must not imply the customer held a licence before their 17th birthday. |
| `licence_held_months` | integer | From 0 through 11. Defaults to 0 when the customer has held the licence 5 or more years. Combined with `licence_held_years`, it must not imply the customer held a licence before their 17th birthday. |
| `ncd_years` | integer | From 0 through 20. |

## `cover_needs`

| Field | Type | Accepted values or rule |
| --- | --- | --- |
| `annual_mileage` | integer | From 0 through 200000. |
| `cover_start_date` | `YYYY-MM-DD` | Today through 30 days from today, inclusive. |

## Tool-result rules

- A vehicle lookup returns `make`, `model`, `abi_code`, and `registration_date`.
- An address lookup can return multiple address objects. Have the user select one result before submission.
- Preserve exact lookup values used by downstream systems.
- Never send display labels such as `Full UK` where the schema requires an internal literal such as `FullUK`.