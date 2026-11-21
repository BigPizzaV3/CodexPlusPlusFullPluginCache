# search_jobs filter fields

All fields below are optional and must be omitted unless the user explicitly states that criterion. Setting a filter narrows results — a filter inferred from context rather than stated by the user typically causes too-few or zero matches.

## working_time

| Value | Meaning | Set only when the user says |
|---|---|---|
| `PartTime` | Teilzeit | "Teilzeit" |
| `FullTime` | Vollzeit | "Vollzeit" |

Do not set based on job type assumptions (e.g. don't assume `FullTime` for a management role).

## work_experience

Binary only — the Stelr system has no finer grading.

| Value | Meaning | Set only when the user says |
|---|---|---|
| `WithoutWorkExperience` | Berufseinsteiger, Quereinsteiger | "Berufseinsteiger", "Quereinsteiger", "ohne Erfahrung" |
| `WithWorkExperience` | Erfahrene Fachkraft, Mid-Level, Senior | "erfahren", "Senior", "Mid-Level" |

Do not set `WithoutWorkExperience` just because someone describes themselves as a career changer for an unrelated reason — only on explicit experience-level mention.

## contract_types (array, OR-connected)

Set only when the user explicitly names a contract type. Do not assume `Permanent` because a role sounds like a typical full-time job.

Values: `Permanent`, `Temporary`, `Freelancer`, `Internship`, `Apprenticeship`, `MiniJob`, `WorkingStudent`, `Trainee`, `DualStudy`, `Volunteer`, `Thesis`, `Doctorate`, `PreparatoryYear`

Trigger words: "Praktikum" → `Internship`, "Ausbildung" → `Apprenticeship`, "Werkstudent" → `WorkingStudent`, "Freelancer"/"freiberuflich" → `Freelancer`, etc.

## home_office (array, OR-connected)

| Value | Meaning | Set only when the user says |
|---|---|---|
| `HomeOfficePossible` | Homeoffice möglich | "Homeoffice", "teilweise remote" |
| `HomeOfficeFull` | Vollständig remote | "vollständig remote", "100% Homeoffice" |

## management_levels (array, OR-connected)

Set only when the user explicitly mentions management responsibility (or its absence). Never infer from experience level, job title, or career stage — e.g. do not set `NoManagement` just because the user is a career changer.

Values: `NoManagement`, `TeamManagement`, `DepartmentManagement`, `BranchManagement`, `RegionalManagement`, `BusinessUnitManagement`, `GeneralManagement`

Roughly: keine Führung → `NoManagement`; Teamleitung → `TeamManagement`; Abteilungsleitung → `DepartmentManagement`; Niederlassungsleitung → `BranchManagement`; Regionalleitung → `RegionalManagement`; Bereichsleitung → `BusinessUnitManagement`; Geschäftsführung → `GeneralManagement`.
