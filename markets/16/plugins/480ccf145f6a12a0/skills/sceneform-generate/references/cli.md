# The sceneform CLI

The CLI runs the same steps as the MCP tools and adds `--wait` and `--out`.
The craft references apply unchanged: the prompt you pass is the prompt the
model reads.

```sh
sceneform options image --query "text rendering"
sceneform generate image --prompt "A ceramic mug on oak, soft window light" --option flux_2:text-to-image --out ./out --name 'mug.{ext}'
sceneform library "product on beach"
sceneform elements
```

## Spending

When the account cannot pay, the CLI prints the quote and exits with code 2;
run `sceneform confirm <action_ref> --wait --out ./out` once it can. To check
with the user first, pass `--max-credits <n>` without `--yes`: the CLI prints
the quote and exits with code 2. With `--yes --max-credits <n>` the CLI asks
for a quote first and confirms it only when it fits the cap; `--yes` without
a cap is refused. Prefer this for unattended runs:

```sh
sceneform generate video --prompt "Slow dolly-in, steam rising" --start ./out/mug.png --yes --max-credits 40 --out ./out
```

## Inputs and outputs

- `--ref`, `--start`, `--end`, `--video`, `--audio`, and `--image` accept a
  local path or an `asset_ref`; the CLI uploads files for you. `--ref` also
  takes a `persona_ref`, `product_ref`, or `element_ref`.
- To name a local file in the prompt with `@{ref:…}`, upload it first: pass
  the printed `asset_ref` to both the mention and `--ref`.

```sh
sceneform upload ./front.png
sceneform generate image --prompt "The jacket from @{ref:media_abc123} on a model in a rainy street" --ref media_abc123 --out ./out
```
- Always use `--out` to save outputs; the CLI downloads them and names each
  file `{index}-{ref}.{ext}` unless `--name` sets a pattern. It refuses to
  replace an existing file unless you pass `--overwrite`. A waited
  operation that fails exits 1 with `reason: "operation_failed"`.
- `--project` and `--folder` file results; `sceneform projects` and
  `sceneform folders` list them and `--create` makes one.
- `sceneform reshoot` changes who or what appears in a clip.
- `not_logged_in`: run `sceneform login`, which prints a code to approve in
  any browser.
- `sceneform whoami` shows the balance.
