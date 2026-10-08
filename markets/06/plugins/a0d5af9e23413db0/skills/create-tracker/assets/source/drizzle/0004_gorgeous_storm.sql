CREATE TABLE `progress_reports` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`period_type` text NOT NULL,
	`period_start` text NOT NULL,
	`period_end` text NOT NULL,
	`summary_json` text NOT NULL,
	`created_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
	`created_by` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_progress_reports_created_at` ON `progress_reports` (`created_at`);