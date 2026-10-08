---
name: beam-pipelines
description: |
  **Required for Beam pipeline tools: create_beam_config, deploy_beam_pipeline, etc.**
  **Beam** is Allium's custom real-time data pipeline product, built on top of
  [Allium Datastreams](https://app.allium.so/build/datastreams). It lets you tap into
  any of Allium's real-time blockchain data streams — covering 80+ chains — and apply
  your own filters and JavaScript transformations before delivering the results to
  Kafka, SNS, or other destinations.

  Common use cases: real-time alerts on contract events, custom data feeds filtered
  to specific wallets or protocols, and streaming enriched data to your own pipeline.

  Browse available data streams at [app.allium.so/build/datastreams](https://app.allium.so/build/datastreams).
  To get access or learn more, reach out to support@allium.so.

  Read this skill for detailed configuration guides and examples.
gate: app__custom_transforms
---

# Beam Pipeline Configuration Guide

## What is Beam?

Beam is Allium's custom real-time data pipeline product, built on top of [Allium Datastreams](https://app.allium.so/build/datastreams). It lets you tap into any of Allium's real-time blockchain data streams — covering 80+ chains — and apply your own filters and transformations before delivering the results to your preferred destination.

```text
Source (any Allium Datastream) → Transforms (filter/transform) → Sinks (Kafka, SNS, and more)
```

With Beam, you can:

- **Filter** high-volume blockchain streams down to just the events you care about (specific contracts, addresses, event signatures)
- **Transform** data in-flight using JavaScript to parse, enrich, or reshape records before delivery
- **Deliver** processed data to Kafka topics or SNS (with more sink types coming soon) for consumption by your applications

Browse the full catalog of available data streams at [app.allium.so/build/datastreams](https://app.allium.so/build/datastreams).

**Common use cases:**

- Real-time alerts on contract events (e.g., large token transfers, liquidations)
- Custom data feeds filtered to specific wallet addresses or protocols
- Live monitoring and anomaly detection for DeFi activity
- Streaming enriched trade data to your own analytics pipeline

**Interested in Beam?** Reach out to <support@allium.so> to get access.

## Quick Start Workflow

1. **Create config** → `create_beam_config`
2. **Deploy pipeline** → `deploy_beam_pipeline`
3. **Verify deployment** → `get_beam_deployment_stats`

Always check deployment stats after deploying to confirm workers are healthy.

After deploying, you'll receive:

- **Kafka connection credentials** (bootstrap server, username, password)
- **Consumer code snippets** in Python and TypeScript, ready to copy-paste
- A **UI link** to manage your pipeline at `app.allium.so/build/beam/{config_id}`

**Updating a pipeline:** Just call `deploy_beam_pipeline` again after updating the config.
Deployment is idempotent and applies changes in place with zero downtime.
Do NOT teardown before redeploying—that causes unnecessary downtime.

## Configuration Reference

### Source

Beam sources connect to Allium's Datastreams. You select a chain and entity type to stream.

```json
{
  "chain": "polygon",
  "entity": "log",
  "is_zerolag": false
}
```

| Field        | Required | Description                              |
| ------------ | -------- | ---------------------------------------- |
| `chain`      | Yes      | Blockchain to source data from           |
| `entity`     | Yes      | Entity type to stream (see table below)  |
| `is_zerolag` | No       | Low-latency source mode (default: false) |

#### Supported Chains & Entities

Check the [Datastreams catalog](https://app.allium.so/build/datastreams) for the latest availability, or reach out to <support@allium.so> to request a specific chain or entity.

### Transforms

Two transform types are available. You can chain multiple transforms together — data flows through them in order.

#### redis_set_filter

Filter data by matching field values against a set. Only records whose extracted field value exists in your set will pass through.

```json
{
  "type": "redis_set_filter",
  "set_values": ["0x1234...", "0x5678..."],
  "filter_expr": "root = this.address"
}
```

| Field         | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `set_values`  | Array of values to match against                             |
| `filter_expr` | Bloblang expression to extract the field value for filtering |

**Important:** When filtering by addresses, labels, or symbols, use **lowercase** values.
This is how these values are normalized in our system.

**Bloblang `filter_expr` examples:**

```bloblang
root = this.address        # Filter by contract address
root = this.topic0         # Filter by first topic (event signature)
root = this.from_address   # Filter by sender address
```

**Log entity field reference:**

| Field          | Description                                |
| -------------- | ------------------------------------------ |
| `address`      | Contract address that emitted the log      |
| `topic0`       | First topic (usually event signature hash) |
| `topic1`       | Second topic (first indexed parameter)     |
| `topic2`       | Third topic (second indexed parameter)     |
| `topic3`       | Fourth topic (third indexed parameter)     |
| `from_address` | Transaction sender                         |
| `to_address`   | Transaction recipient                      |
| `data`         | Non-indexed event data                     |

#### v8

Transform data using JavaScript. Your function receives each record and can modify, enrich, or reshape it. Return `null` to drop a record.

```json
{
  "type": "v8",
  "script": "function transform(record) { return record; }"
}
```

| Field    | Description                                |
| -------- | ------------------------------------------ |
| `script` | JavaScript code that processes each record |

### Sinks

Sinks define where your processed data is delivered.

```json
{
  "type": "kafka",
  "name": "my-output-topic"
}
```

| Field  | Description                                            |
| ------ | ------------------------------------------------------ |
| `type` | Output type: `kafka` or `sns` (more sinks coming soon) |
| `name` | Topic name suffix for the output                       |

**Kafka sinks:** After deployment, you'll receive connection credentials and ready-to-use consumer code snippets in Python and TypeScript.

**SNS sinks:** Delivers data to an SNS topic. Reach out to <support@allium.so> if you need help setting up SNS delivery or are interested in other sink types.

## Quick Start Examples

### Example 1: Filter Logs by Contract Address

Stream logs from specific contract addresses using `redis_set_filter`:

```json
{
  "name": "USDC Transfer Monitor",
  "description": "Monitor USDC transfers on Polygon",
  "source": {
    "chain": "polygon",
    "entity": "log"
  },
  "transforms": [
    {
      "type": "redis_set_filter",
      "set_values": [
        "0x3c499c542cef5e3811e1192ce70d8cc03d5c3359"
      ],
      "filter_expr": "root = this.address"
    }
  ],
  "sinks": [
    {
      "type": "kafka",
      "name": "usdc-logs"
    }
  ]
}
```

### Example 2: Transform Log Data with JavaScript

Parse and enrich log data using a v8 transform:

```json
{
  "name": "DEX Trade Parser",
  "description": "Parse DEX swap events and extract trade details",
  "source": {
    "chain": "polygon",
    "entity": "log"
  },
  "transforms": [
    {
      "type": "redis_set_filter",
      "set_values": [
        "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
      ],
      "filter_expr": "root = this.topic0"
    },
    {
      "type": "v8",
      "script": "function transform(record) { record.parsed = true; return record; }"
    }
  ],
  "sinks": [
    {
      "type": "kafka",
      "name": "dex-trades"
    }
  ]
}
```

### Example 3: Monitor ERC-20 Transfers on Base

Track token transfers on Base using the `erc20_token_transfer` entity:

```json
{
  "name": "Base Token Transfer Tracker",
  "description": "Monitor ERC-20 token transfers on Base",
  "source": {
    "chain": "base",
    "entity": "erc20_token_transfer"
  },
  "transforms": [
    {
      "type": "redis_set_filter",
      "set_values": [
        "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913"
      ],
      "filter_expr": "root = this.address"
    }
  ],
  "sinks": [
    {
      "type": "kafka",
      "name": "base-usdc-transfers"
    }
  ]
}
```

### Example 4: Multiple Contract Addresses

Monitor multiple contracts in a single pipeline:

```json
{
  "name": "Multi-Token Monitor",
  "description": "Monitor USDC and USDT on Polygon",
  "source": {
    "chain": "polygon",
    "entity": "log"
  },
  "transforms": [
    {
      "type": "redis_set_filter",
      "set_values": [
        "0x3c499c542cef5e3811e1192ce70d8cc03d5c3359",
        "0xc2132d05d31c914a87c6611c10748aeb04b58e8f"
      ],
      "filter_expr": "root = this.address"
    }
  ],
  "sinks": [
    {
      "type": "kafka",
      "name": "stablecoin-logs"
    }
  ]
}
```

## Tool Reference

### Configuration Management

| Tool                 | Description                                         |
| -------------------- | --------------------------------------------------- |
| `create_beam_config` | Create a new pipeline configuration                 |
| `get_beam_config`    | Get full details of a config by ID                  |
| `list_beam_configs`  | List all your pipeline configurations               |
| `update_beam_config` | Update an existing configuration                    |
| `delete_beam_config` | Delete a configuration (also tears down deployment) |

### Deployment

| Tool                        | Description                               |
| --------------------------- | ----------------------------------------- |
| `deploy_beam_pipeline`      | Deploy a config to Kubernetes             |
| `teardown_beam_pipeline`    | Remove deployed infrastructure            |
| `get_beam_deployment_stats` | Check deployment status and worker health |

### Web Interface

Every pipeline has a management page at `app.allium.so/build/beam/{config_id}`.
The UI URL is returned by `create_beam_config`, `deploy_beam_pipeline`, and `get_beam_deployment_stats`.

## Consuming Your Data

After deploying a Beam pipeline with a Kafka sink, the `deploy_beam_pipeline` tool returns everything you need to start consuming:

- **Kafka connection credentials**: bootstrap server, username, and password
- **Code snippets**: Ready-to-use consumer code in Python (`confluent-kafka`) and TypeScript (`kafkajs`)
- **Topic names**: Automatically generated as `beam.{config_id}.{sink_name}`

Just copy the provided code snippet, install the relevant Kafka client library, and start receiving data.

## Monitoring

### Checking Deployment Health

After deploying, use `get_beam_deployment_stats` to verify:

```json
{
  "config_id": "abc123",
  "status": "deployed",
  "workers_health": {
    "total_workers": 2,
    "healthy_workers": 2,
    "unhealthy_workers": 0,
    "crashing_workers": 0,
    "oom_killed_workers": 0
  }
}
```

### Worker Health Fields

| Field                | Description                  |
| -------------------- | ---------------------------- |
| `total_workers`      | Number of worker pods        |
| `healthy_workers`    | Workers running normally     |
| `unhealthy_workers`  | Workers not ready            |
| `crashing_workers`   | Workers in crash loop        |
| `oom_killed_workers` | Workers killed due to memory |

## Troubleshooting

### Unhealthy Workers

If `unhealthy_workers > 0`:

1. Check if the pipeline config is valid
2. Verify source data is available
3. Update the config and redeploy (no teardown needed)

### OOM Killed Workers

If `oom_killed_workers > 0`:

1. Simplify transforms to reduce memory usage
2. Add more aggressive filtering earlier in the pipeline
3. Contact <support@allium.so> for resource limit adjustments

### Crashing Workers

If `crashing_workers > 0`:

1. Check v8 script for syntax errors
2. Verify filter expressions are valid
3. Review transform logic for runtime errors

## Best Practices

1. **Filter early**: Apply `redis_set_filter` before `v8` transforms to reduce data volume
2. **Start simple**: Begin with basic filtering, add transforms incrementally
3. **Monitor after deploy**: Always check `get_beam_deployment_stats` after deployment
4. **Test transforms**: Validate v8 scripts handle edge cases
5. **Use descriptive names**: Clear names help track multiple pipelines
6. **Lowercase addresses/labels/symbols**: Use lowercase when filtering by these values
7. **Redeploy, don't teardown**: When updating, just redeploy—it's idempotent with zero downtime
