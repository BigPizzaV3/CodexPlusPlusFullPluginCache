# File and Text Processing Patterns

## Purpose

Use this file for `find`, `grep`, `sed`, `awk`, `xargs`, sorting, filesystem traversal, and bulk file operations.

# 1. Never parse `ls`

Do not use:

```bash
for f in $(ls ...)
```

Filenames can contain whitespace and special characters.

Prefer:
- shell globs when sufficient;
- `find -exec`;
- NUL-delimited pipelines where supported.

# 2. `find -exec`

Safe bulk execution pattern:

```bash
find /path -type f -name '*.log' -exec some_command -- {} +
```

Advantages:
- preserves filenames as arguments;
- avoids whitespace parsing;
- batches multiple paths.

Use `{} \;` only when one invocation per result is required.

# 3. NUL-delimited traversal

GNU and many modern systems support:

```bash
find /path -type f -print0 |
  xargs -0 some_command
```

NUL delimiters safely preserve spaces, quotes, and newlines in filenames.

Do not assume every non-GNU utility supports every NUL-related flag; label portability.

# 4. `grep`

For searching content, define:
- literal vs regex;
- case sensitivity;
- recursion;
- binary-file behavior;
- filename output.

Use fixed-string mode when regex interpretation is unwanted.

# 5. `sed`

Use for line-oriented transformations when the format is truly line-oriented.

Be careful with:
- in-place editing;
- GNU vs BSD/macOS syntax;
- binary/NUL content;
- multi-line structured formats.

Prefer new output + validation for important files.

# 6. `awk`

Good for:
- whitespace/simple delimiter records;
- field calculations;
- aggregation;
- simple reports.

Do not use plain `awk -F,` as a general CSV parser when quoted commas or embedded newlines are possible.

# 7. Sorting

Set/consider locale when byte/lexical ordering matters.

For deterministic pipelines, document sort keys and tie-breakers.

Do not assume a prior command’s output order is stable unless guaranteed.

# 8. Counts

Common distinctions:
- lines;
- records;
- bytes;
- files;
- matches.

Choose the metric that matches the user’s intent.

A newline count is not always a record count for structured data.

# 9. Filenames from user input

Quote paths.

Avoid building shell commands by concatenating untrusted filenames into command strings.

Prefer positional arguments or `find -exec`.

# 10. Bulk modifications

For rename/move/delete:
1. generate a preview list;
2. inspect collisions;
3. verify count/scope;
4. execute separately;
5. validate result.

Do not combine discovery and destructive action into one block for high-risk tasks.
