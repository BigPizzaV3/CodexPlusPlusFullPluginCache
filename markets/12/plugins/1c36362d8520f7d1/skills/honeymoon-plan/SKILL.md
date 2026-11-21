---
name: honeymoon-plan
description: 신혼여행 설문, 여행지 추천, 여행 일정, 여행 취향, 저장된 허니문 추천을 보거나 설문을 저장할 때 사용한다. Use for a WeddingFlow honeymoon survey and its saved destination or schedule. Do not use for the overall wedding budget or dress rental.
---

# WeddingFlow honeymoon survey

Answer in Korean. Saved recommendations come from the survey record returned by WeddingFlow. Do not present a destination, price, or itinerary as saved unless the tool returned it.

## Tools

| Intent | Tool |
| --- | --- |
| My surveys | `get_api_v1_honeymoon_survey` |
| One survey | `get_api_v1_honeymoon_survey_by_survey_id` |
| Shared survey | `get_api_v1_honeymoon_survey_open_by_survey_uuid` |
| Save a survey | `post_api_v1_honeymoon_survey` |

The shared lookup uses `path_params.survey_uuid`. Do not guess a UUID.

## What the user can set

Read existing surveys before creating another one. Confirm the answers, then send only these fields in `body`:

- `start_date`: `YYYY-MM-DD`
- `nights`: integer
- `budget`: integer won
- `experience_or_relax`: experience-focused or rest-focused, in the user's words
- `famous_or_unique`: famous places or unique places
- `priority`: list of preferences such as food, shopping, rest, activities, hotel stay, scenery, short flight, culture, language, and safety

Do not send `destination`, `recommend`, `schedule`, `expected_cost`, `precautions`, `end_date`, or any model-cost field. Those are produced by WeddingFlow. After a successful save, read the survey again and summarize only the fields that came back.

Do not retry a failed POST. Wedding-budget totals are a different skill; mention that skill if the user wants the honeymoon line of the overall budget changed.

If authorization is required, use the host OAuth flow. Never ask for a token.
