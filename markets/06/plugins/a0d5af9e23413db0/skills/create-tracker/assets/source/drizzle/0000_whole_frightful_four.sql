CREATE TABLE `fixture_progress` (
	`fixture_id` text PRIMARY KEY NOT NULL,
	`status` text DEFAULT 'not-started' NOT NULL,
	`updated_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL
);
