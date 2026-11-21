# Himalayas tools

Every tool on the hosted Himalayas MCP (`https://mcp.himalayas.app/mcp/chatgpt`), with its parameters. Allowed values are listed in parentheses. "Read-only" tools never change anything. For every other tool, confirm with the user before calling it.

Job, company and salary tools work without signing in. Every other tool uses the Himalayas account the user connected through OAuth; employer tools need an employer account.

### `get_jobs`: Browse remote jobs
Read-only. Params: `page` integer, `country` string, `worldwide` boolean

### `search_jobs`: Search remote jobs
Read-only. Params: `keyword` string, `page` integer, `country` string, `exclude_worldwide` boolean, `worldwide` boolean, `experience` (entry-level|mid-level|senior|manager|director|executive), `type` (full-time|part-time|contractor|temporary|intern|volunteer|other), `salary_min` number, `salary_max` number, `currency` (USD|AUD|EUR|JPY|GBP|CAD|CHF|CNY|HKD|NZD|SGD|SEK|KRW|NOK|INR|MXN|TWD|ZAR|BRL|IDR|PHP|THB|CLP|CZK|DKK|HUF|ILS|TRY|PLN), `salary_required` boolean, `markets` string, `benefits` string, `companies` string, `sort` (relevant|recent|salaryAsc|salaryDesc)

### `get_job_details`: Get job details
Read-only. Params: `company_slug` string, `job_slug` string

### `get_apply_link`: Get apply link
Changes, removes or sends; always confirm. Params: `company_slug` string, `job_slug` string

### `generate_application_documents`: Tailor resume and cover letter
Changes, removes or sends; always confirm. Params: `company_slug` string, `job_slug` string, `documents` array

### `get_new_matches`: Get new job matches
Changes, removes or sends; always confirm. Params: none

### `skip_job`: Skip job
Changes, removes or sends; always confirm. Params: `company_slug` string, `job_slug` string, `reason` (job_closed|needs_account|location_or_visa_restricted|pay_too_low|wrong_timezone|not_really_remote|wrong_seniority|wrong_role|not_interested|other), `detail` string

### `get_related_jobs`: Get related jobs
Read-only. Params: `company_slug` string, `job_slug` string

### `get_companies`: Browse remote companies
Read-only. Params: `page` integer, `country` string, `worldwide` boolean

### `search_companies`: Search remote companies
Read-only. Params: `keyword` string, `page` integer, `country` string, `worldwide` boolean, `benefits` string, `tech_stack` string, `sort` (relevant|recent|jobs|nameAToZ|nameZToA)

### `get_company_details`: Get company details
Read-only. Params: `company_slug` string

### `get_remote_work_statistics`: Get remote work statistics
Read-only. Params: `record` (jobs|companies), `type` (skills|categories|countries|industries), `country` string

### `get_salary_data`: Get salary data
Read-only. Params: `job_title` string, `seniority` string, `country` string

### `get_correct_country_name`: Resolve country name
Read-only. Params: `country_string` string

### `submit_feedback`: Send feedback to Himalayas
Adds data; confirm first. Params: `type` (missing_capability|bug|unclear_documentation|unexpected_response|unhelpful_error|performance|other), `goal` string, `message` string, `endpoint` string, `outcome` (blocked|degraded|completed), `workaround` boolean, `workaround_description` string, `expected` string, `suggestion` string, `request_id` string, `session_id` string, `agent` object, `evidence` object, `metadata` object

### `get_my_profile`: Get my profile
Read-only. Params: none

### `save_job`: Save job to tracker
Changes, removes or sends; always confirm. Params: `title` string, `company_name` string, `status` (seen|saved|applied|interviewing|negotiation|hired|archived), `base_salary` number, `max_salary` number, `currency` string, `excitement` number, `notes` string, `app_link` string, `himalayas_link` string

### `get_saved_jobs`: Get saved jobs
Read-only. Params: none

### `update_job_status`: Update job status
Changes, removes or sends; always confirm. Params: `id` number, `status` (seen|saved|applied|interviewing|negotiation|hired|archived), `excitement` number, `notes` string, `outcome` (rejected|no_response|withdrawn|didnt_apply|clear), `reason` (job_closed|needs_account|location_or_visa_restricted|pay_too_low|wrong_timezone|not_really_remote|wrong_seniority|wrong_role|not_interested|other), `detail` string

### `remove_saved_job`: Remove saved job
Changes, removes or sends; always confirm. Params: `id` number

### `update_profile`: Update profile
Changes, removes or sends; always confirm. Params: `first_name` string, `last_name` string, `username` string, `bio` string, `intro` string, `location` string, `career_search_status` (actively_searching|open_to_roles|closed_to_roles), `career_primary_role` string, `career_base_salary` number, `career_max_salary` number, `career_description` string, `career_working_permits` array, `career_skill_list` array, `career_compensation` (no_equity|open_to_compensation|equity_important), `twitter` string, `linkedin` string, `github` string, `dribbble` string, `behance` string, `website` string, `portfolio` string, `contact_email` string, `email_visible` boolean, `visibility` (public_profile|unsearchable_profile|private_profile), `career_interested_role_list` array, `seniority` array, `career_company_size` object, `career_salary_country` (USD|AUD|EUR|JPY|GBP|CAD|CHF|CNY|HKD|NZD|SGD|SEK|KRW|NOK|INR|MXN|TWD|ZAR|BRL|IDR|PHP|THB|CLP|CZK|DKK|HUF|ILS|TRY|PLN)

### `add_experience`: Add work experience
Adds data; confirm first. Params: `title` string, `company_name` string, `employment_type` (Full Time|Part Time|Self Employed|Freelance|Contractor|Temporary|Intern|Apprenticeship|Volunteer|Other), `description` string, `location` string, `start_date` string, `end_date` string, `current_job` boolean, `experience_skill_list` string

### `add_education`: Add education
Adds data; confirm first. Params: `school` string, `degree` string, `field` string, `start_year` number, `end_year` number, `description` string, `current` boolean, `grade` string, `activities` string

### `update_experience`: Update work experience
Changes, removes or sends; always confirm. Params: `id` number, `title` string, `company_name` string, `employment_type` (Full Time|Part Time|Self Employed|Freelance|Contractor|Temporary|Intern|Apprenticeship|Volunteer|Other), `description` string, `location` string, `start_date` string, `end_date` string, `current_job` boolean, `experience_skill_list` array, `sort_order` number

### `delete_experience`: Delete work experience
Changes, removes or sends; always confirm. Params: `id` number

### `update_education`: Update education
Changes, removes or sends; always confirm. Params: `id` number, `school` string, `degree` string, `field` string, `start_year` number, `end_year` number, `description` string, `current` boolean, `grade` string, `activities` string, `sort_order` number

### `delete_education`: Delete education
Changes, removes or sends; always confirm. Params: `id` number

### `update_email_preferences`: Update email preferences
Changes, removes or sends; always confirm. Params: `job_matches` boolean, `job_match_frequency` (daily|weekly), `job_reminders` boolean, `application_followups` boolean, `message_notifications` boolean, `job_post_updates` boolean, `job_post_reminders` boolean, `marketing_emails` boolean

### `update_account`: Update account time zone
Changes, removes or sends; always confirm. Params: `time_zone` string

### `list_documents`: List resumes and cover letters
Read-only. Params: `type` (resume|cover_letter)

### `get_document`: Get resume or cover letter
Read-only. Params: `type` (resume|cover_letter), `id`

### `update_document`: Update resume or cover letter
Changes, removes or sends; always confirm. Params: `type` (resume|cover_letter), `id`, `title` string, `content` string

### `delete_document`: Delete resume or cover letter
Changes, removes or sends; always confirm. Params: `type` (resume|cover_letter), `id`

### `import_profile`: Import profile from LinkedIn or resume
Changes, removes or sends; always confirm. Params: `linkedin_url` string, `resume_text` string, `mode` (append_only|replace_all)

### `update_profile_photo`: Update profile photo
Changes, removes or sends; always confirm. Params: `kind` (avatar|cover_photo), `image_url` string

### `list_interviews`: List interview practice
Read-only. Params: none

### `get_interview_results`: Get interview practice results
Read-only. Params: `id` number, `company_slug` string, `job_slug` string

### `get_interview_practice_link`: Get interview practice link
Read-only. Params: `company_slug` string, `job_slug` string, `application_link` string

### `list_saved_answers`: List saved application answers
Read-only. Params: none

### `update_saved_answer`: Update saved application answer
Changes, removes or sends; always confirm. Params: `id` number, `answer` string

### `delete_saved_answer`: Delete saved application answer
Changes, removes or sends; always confirm. Params: `id` number

### `list_notifications`: List notifications
Read-only. Params: none

### `mark_notifications_read`: Mark notifications read
Changes, removes or sends; always confirm. Params: `id` number, `all` boolean

### `list_coach_chats`: List career coach chats
Read-only. Params: none

### `get_coach_chat`: Get career coach chat
Read-only. Params: `slug` string

### `list_headshots`: List headshots
Read-only. Params: none

### `use_headshot_as_profile_photo`: Use headshot as profile photo
Changes, removes or sends; always confirm. Params: `session_id` number, `image_id` number

### `get_headshots_link`: Get headshots link
Read-only. Params: none

### `update_tech_stack`: Update profile tech stack
Changes, removes or sends; always confirm. Params: `stacks` array

### `search_talent`: Search talent
Read-only. Params: `keyword` string, `country` string, `page` integer, `sort` (relevant|recent)

### `get_talent_profile`: Get talent profile
Read-only. Params: `talent_slug` string

### `get_company_profile`: Get company profile
Read-only. Params: none

### `update_company_profile`: Update company profile
Changes, removes or sends; always confirm. Params: `about` string, `summary` string, `ceo` string, `num_employees_range` (1-10|11-50|51-200|201-500|501-1000|1001-5000|5000+), `year_founded` number, `location_list` string, `twitter` string, `facebook` string, `linkedin` string, `instagram` string

### `get_company_perks`: Get company perks
Read-only. Params: none

### `add_company_perk`: Add company perk
Adds data; confirm first. Params: `title` string, `category` (Healthcare benefits|Retirement benefits|Paid parental leave|Equity benefits|Location independent salary|Profit sharing|4-day workweeks|Generous vacation|Paid vacation|Sabbaticals|Unlimited time off|Company meals|Wellness benefits|Home office budget|Co-working space budget|Commuter benefits|Pet-friendly office|Learning and development budget|Company events|Volunteer opportunities|Open source|Company credit card|Life insurance|Employee assistance program (EAP)|Flexible working hours|Disability insurance|Fertility benefits|Company retreats|Get paid in crypto|Miscellaneous), `description` string

### `remove_company_perk`: Remove company perk
Changes, removes or sends; always confirm. Params: `id` number

### `update_company_tech_stack`: Update company tech stack
Changes, removes or sends; always confirm. Params: `stacks` array

### `list_company_jobs`: List company jobs
Read-only. Params: `page` integer

### `show_company_job`: Get company job
Read-only. Params: `job_slug` string

### `create_company_job`: Create company job
Adds data; confirm first. Params: `title` string, `description` string, `employment_type` (Full Time|Part Time|Contractor|Temporary|Intern|Volunteer|Other), `seniority` array, `app_link_or_email` string, `valid_through` string, `base_salary` number, `max_salary` number, `salary_country` string, `category_list` string, `skill_list` string, `draft` boolean, `screening_questions` array

### `update_company_job`: Update company job
Changes, removes or sends; always confirm. Params: `job_slug` string, `title` string, `description` string, `employment_type` (Full Time|Part Time|Contractor|Temporary|Intern|Volunteer|Other), `seniority` array, `app_link_or_email` string, `valid_through` string, `base_salary` number, `max_salary` number, `salary_country` string, `category_list` string, `skill_list` string, `draft` boolean, `screening_questions` array

### `delete_company_job`: Delete company job
Changes, removes or sends; always confirm. Params: `job_slug` string

### `list_conversations`: List employer conversations
Read-only. Params: none

### `get_conversation`: Get employer conversation
Read-only. Params: `room_name` string, `talent_slug` string

### `start_conversation`: Start conversation with candidate
Changes, removes or sends; always confirm. Params: `talent_slug` string, `message` string

### `send_message`: Send message to candidate
Changes, removes or sends; always confirm. Params: `message` string, `room_name` string, `talent_slug` string

### `mark_message_read`: Mark employer message read
Changes, removes or sends; always confirm. Params: `message_id` number, `room_name` string, `talent_slug` string

### `delete_conversation`: Delete employer conversation
Changes, removes or sends; always confirm. Params: `room_name` string, `talent_slug` string

### `list_my_conversations`: List my inbox
Read-only. Params: none

### `get_my_conversation`: Get inbox conversation
Read-only. Params: `room_name` string

### `reply_to_message`: Reply in inbox
Changes, removes or sends; always confirm. Params: `room_name` string, `message` string

### `mark_my_message_read`: Mark inbox message read
Changes, removes or sends; always confirm. Params: `room_name` string, `message_id` number
