# Ads from the sceneform CLI

```sh
sceneform ad-hooks
sceneform ad-templates
sceneform ad video --concept "Our coffee fits busy mornings" --hook interview
sceneform ad video --concept "Our coffee fits busy mornings" --type tv_spot --aspect-ratio 16:9 --resolution 1080p
sceneform ad static --concept "Our coffee fits busy mornings" --resolution 2K --website omit
sceneform ad-variants media_k57f3n2kq8r1s7t9v2w4y6z1a3b5c7d9 --headlines 4
sceneform ad-variants media_k57f3n2kq8r1s7t9v2w4y6z1a3b5c7d9 --resize 1:1,9:16
sceneform reshoot media_k97c2m4pq9r1s6t8v0w3y5z2a4b6c8d1 --ad --instruction "Put @Image1 in a sunny kitchen" --ref tq1gwy1tsqrtzgkz3qaxr68jeyfk2dne
sceneform carousel-recipes
sceneform carousel --concept "Five ways to improve your morning coffee" --recipe camera_roll
```

Creation commands start at once and print the operation or receipt with the
credits charged. When the account cannot pay they print the quote and exit
with code 2 instead; `sceneform confirm <action_ref>` starts it once it can.
To check with the user first, add `--max-credits <n>` without `--yes`: the
CLI prints the quote and exits with code 2. For a previously authorized
budget, add `--yes --max-credits <n>`: the CLI asks for a quote and confirms
it only within the cap; `--yes` without a cap is refused. Use
`sceneform op <operation_ref> --wait --out ./ads` for ads and
`sceneform carousel <carousel_ref> --wait --out ./slides` for carousels.
