CREATE TABLE `fixture_history_clears` (
	`fixture_id` text PRIMARY KEY NOT NULL,
	`cleared_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
	`cleared_by` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `tracker_managers` (
	`email` text PRIMARY KEY NOT NULL,
	`added_by` text NOT NULL,
	`created_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL
);

