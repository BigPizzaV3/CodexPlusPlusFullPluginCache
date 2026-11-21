# Bulk ESM Atlas data

The [Biohub get-started guide](https://biohub.ai/esm/protein/get-started) publishes data under `s3://esm-protein-atlas/v1/` with CC-BY-4.0 licensing. It needs no credentials.

```bash
aws s3 sync --no-sign-request \
  s3://esm-protein-atlas/v1/clusters/indexes/secondary/cluster_members/ \
  /absolute/path/atlas-cluster-members
```

Use the narrowest dataset prefix. Cluster membership (~26 GB) is the recommended manageable starting point.

| Dataset | Published size | S3 source |
| --- | ---: | --- |
| Sequences | 2.20 TB | `s3://esm-protein-atlas/v1/sequences/` |
| Structures | 68.9 TB | `s3://esm-protein-atlas/v1/folds/` |
| SAE features | 306 TB | `s3://esm-protein-atlas/v1/sae/data_shards/` |
| SAE clusters | 26.0 GB | `s3://esm-protein-atlas/v1/clusters/indexes/secondary/cluster_members/` |
| HMM results | 653 MB | `s3://esm-protein-atlas/v1/clusters/data/representative_proteins.parquet` |
| Protein-to-accession indexes | 162 GB | `s3://esm-protein-atlas/v1/shared_indexes/` |
| Feature normalization | 192 KB | `s3://esm-protein-atlas/v1/normalization/max_idf_log10.pkl` |
| Full release | 377 TB | `s3://esm-protein-atlas/v1/` |

Use `aws s3 sync --no-sign-request` for prefixes and `aws s3 cp --no-sign-request` for the two single files. Do not silently widen a requested subset to the full release.

Atlas provides these downloads without charging the downloader for source transfer. Destination storage, downstream processing, third-party networks, or later egress may still cost money. Before a multi-gigabyte or multi-terabyte sync, estimate the selected prefix size and local or cloud storage impact, show the exact source and destination plus any available cost information, and ask a plain yes/no question. A small Atlas lookup is not authorization for a bulk transfer.

Thumbnails, MD5-keyed records, the full feature catalog, and batch record downloads are in the [Atlas API](https://biohub.ai/esm/protein/atlas/api-docs/api_reference.html).
