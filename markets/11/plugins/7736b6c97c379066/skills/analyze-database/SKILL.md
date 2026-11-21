---
name: analyze-database
description: Explore what is inside a VPNDetection database and analyze it - its columns and what a row means, a first look from its sample rows, and in Codex, counts and lookups over a downloaded copy. Use when someone asks what a database contains, wants example rows, or wants numbers from the data such as counts by provider, how much of a network is covered, or whether an address or range is in it.
---

# Analyze a VPNDetection database

1. Find the database with `list_databases` and use its `versions[].id` (`vpn_ip_v1`, not `vpn_ip`). Every family it lists can be described, whatever its `standing`.
2. Call `database_metadata`. It gives the columns per format with their types and descriptions, including the allowed values of enum columns, a few sample rows, the row count, the build date and each file's size.
3. Explain the columns in plain words and show the sample rows as a table. Say what one row means for this database, for example one address range and the provider it belongs to.
4. The sample is a handful of rows picked at random when the database is built. It shows the shape of the data and is never enough to count from, so do not draw totals, shares or rankings from it. The row count is the only whole-dataset figure the metadata gives: `sample_entries` and `sample_size` describe the separate evaluation sample file, not the database or these rows.
5. For real numbers, work on a full copy, which needs a `licensed` family. The `open` ones are licensed to every organization from the start and free under CC BY-SA 4.0. In Codex, with the `vpndetection` CLI installed and signed in (`vpndetection login`), tell the person the file size from step 2, then download and query it locally:

   ```console
   vpndetection db download vpn_ip_v1 vpn_ip_v1.csv.gz
   duckdb -c "SELECT provider, count(*) AS ranges FROM 'vpn_ip_v1.csv.gz' GROUP BY 1 ORDER BY 2 DESC LIMIT 20"
   ```

   The CLI verifies the checksum before it finishes. Use whatever the person has for the query, whether that is duckdb, sqlite or pandas, and base column names on the metadata rather than guessing.
6. Outside Codex there is no terminal to download into. Answer what the metadata and samples can, and say that counting needs a downloaded copy.

To check single addresses rather than the database as a whole, `lookup_ip` and `lookup_ips` answer from the same data without a download.
