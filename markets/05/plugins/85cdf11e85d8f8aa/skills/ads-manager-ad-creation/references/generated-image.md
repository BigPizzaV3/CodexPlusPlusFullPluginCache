# Generated Image Details

Use when the user explicitly chooses image generation.

Before applying this workflow, read and follow the [shared image asset contract](_shared/image-asset-contract.md) for `ad-creative`.

3. Inspect the exact result with the shared semantic preflight before showing it as a candidate. A generated image that contains nested ad or platform UI, promotional overlays, invented facts, or unsafe framing fails even when its file properties are valid.
4. On the first semantic failure, call `$imagegen` once more with the same confirmed brief and an explicit correction naming the observed violation, then repeat the full preflight. If the corrected result still fails, stop the automatic loop, explain the unmet check, and offer a simplified regeneration brief, a user-provided image, or an approved website image; never relax the contract.
5. When a local path is available, run the shared `ad-creative` validator after semantic preflight; when it is not, do not claim deterministic validation ran. Passing that validator never proves semantic compliance. After any repair, re-export, or regeneration prompted by a deterministic failure, return to step 3 and repeat the full semantic preflight before rerunning the validator or showing, previewing, or uploading the result.
