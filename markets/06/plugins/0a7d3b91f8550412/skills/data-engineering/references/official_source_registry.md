# Official Source Registry

Use current primary documentation whenever behavior depends on a runtime, platform version, storage feature, scheduler API, or cloud service.

## OpenAI plugin packaging

- Package plugins: https://developers.openai.com/plugins/build/plugins
- Build skills: https://developers.openai.com/plugins/build/skills
- Submit plugins: https://developers.openai.com/plugins/deploy/submission
- Submission validation/errors: https://developers.openai.com/plugins/deploy/submission-errors

## Apache Spark / Structured Streaming

- Structured Streaming guide: https://spark.apache.org/docs/latest/streaming/index.html
- Structured Streaming migration guide: https://spark.apache.org/docs/latest/ss-migration-guide.html

## Databricks / Delta Lake

- Structured Streaming checkpoints:
  https://docs.databricks.com/aws/en/structured-streaming/checkpoints
- Production Structured Streaming considerations:
  https://docs.databricks.com/aws/en/structured-streaming/production
- Stateful Structured Streaming:
  https://docs.databricks.com/gcp/en/structured-streaming/stateful-streaming
- Delta MERGE:
  https://docs.databricks.com/gcp/en/delta/merge
- RocksDB state store:
  https://docs.databricks.com/aws/en/structured-streaming/rocksdb-state-store

## Apache Airflow

- DAG runs and backfills:
  https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html
- Stable REST API:
  https://airflow.apache.org/docs/apache-airflow/stable-rest-api-ref.html

## Usage rule

Do not freeze platform-specific behavior into the skill when it can change by runtime or product version.

For implementation decisions involving checkpoint compatibility, streaming state, Delta MERGE semantics, Airflow APIs, Spark optimizer behavior, Lakeflow, Auto Loader, clustering, or serverless compute, verify the exact current official documentation for the user's runtime/environment.
