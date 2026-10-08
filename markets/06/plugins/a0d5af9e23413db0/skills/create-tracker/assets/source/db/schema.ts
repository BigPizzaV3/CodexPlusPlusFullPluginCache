import { sql } from "drizzle-orm";
import { index, integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const fixtureProgress = sqliteTable("fixture_progress", {
  fixtureId: text("fixture_id").primaryKey(),
  status: text("status").notNull().default("not-started"),
  updatedAt: text("updated_at").notNull().default(sql`CURRENT_TIMESTAMP`),
});

export const fixtureStatusHistory = sqliteTable("fixture_status_history", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  fixtureId: text("fixture_id").notNull(),
  previousStatus: text("previous_status").notNull(),
  newStatus: text("new_status").notNull(),
  changedAt: text("changed_at").notNull().default(sql`CURRENT_TIMESTAMP`),
}, table => [index("idx_fixture_status_history_fixture_id").on(table.fixtureId)]);

export const trackerNotes = sqliteTable("tracker_notes", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  content: text("content").notNull(),
  system: text("system"),
  floor: text("floor"),
  createdAt: text("created_at").notNull().default(sql`CURRENT_TIMESTAMP`),
  updatedAt: text("updated_at").notNull().default(sql`CURRENT_TIMESTAMP`),
}, table => [index("idx_tracker_notes_updated_at").on(table.updatedAt)]);

export const trackerManagers = sqliteTable("tracker_managers", {
  email: text("email").primaryKey(),
  addedBy: text("added_by").notNull(),
  createdAt: text("created_at").notNull().default(sql`CURRENT_TIMESTAMP`),
});

export const fixtureHistoryClears = sqliteTable("fixture_history_clears", {
  fixtureId: text("fixture_id").primaryKey(),
  clearedAt: text("cleared_at").notNull().default(sql`CURRENT_TIMESTAMP`),
  clearedBy: text("cleared_by").notNull(),
});

export const progressReports = sqliteTable("progress_reports", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  periodType: text("period_type").notNull(),
  periodStart: text("period_start").notNull(),
  periodEnd: text("period_end").notNull(),
  summaryJson: text("summary_json").notNull(),
  createdAt: text("created_at").notNull().default(sql`CURRENT_TIMESTAMP`),
  createdBy: text("created_by").notNull(),
}, table => [index("idx_progress_reports_created_at").on(table.createdAt)]);
