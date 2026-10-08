from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
AD_CREATION_SKILL = PLUGIN_ROOT / "skills" / "ads-manager-ad-creation" / "SKILL.md"
AD_CREATION_REFERENCES = PLUGIN_ROOT / "skills" / "ads-manager-ad-creation" / "references"
GENERATED_IMAGE = AD_CREATION_REFERENCES / "generated-image.md"
IMAGE_ASSET_CONTRACT = PLUGIN_ROOT / "shared-references" / "image-asset-contract.md"


def test_generation_prompt_requests_artwork_instead_of_rendered_ad() -> None:
    contract = IMAGE_ASSET_CONTRACT.read_text(encoding="utf-8")
    prompt = contract.split("For a generated ad creative:", 1)[1].split("## Semantic preflight", 1)[
        0
    ]

    assert "edge-to-edge source artwork" in prompt
    assert "do not render any surrounding frame, interface, or placement" in prompt
    assert "do not ask to make an ad or name an advertising platform" in prompt
    assert "The connector-rendered ad preview owns" in prompt
    assert "Asset type: Ads Manager ad creative image" not in prompt
    assert "Use case: product-mockup" not in prompt


def test_generated_creatives_fail_closed_on_semantic_violations() -> None:
    contract = IMAGE_ASSET_CONTRACT.read_text(encoding="utf-8")
    preflight = contract.split("## Semantic preflight for generated ad creatives", 1)[1].split(
        "## Deterministic validation", 1
    )[0]

    assert "Accept it only when every check passes" in preflight
    assert "no nested ad, ad card, browser, device, feed, chat, search result" in preflight
    assert "Treat a failed or uncertain check as a failed candidate" in preflight
    assert "Do not present it for approval" in preflight
    assert "Use `$imagegen` once more" in preflight
    assert "If the corrected result still fails, stop the automatic loop" in preflight
    assert "Never weaken the checks" in preflight


def test_changed_generated_result_repeats_semantic_preflight_before_every_use() -> None:
    contract = IMAGE_ASSET_CONTRACT.read_text(encoding="utf-8")
    deterministic = contract.split("## Deterministic validation", 1)[1]

    assert "every repaired, re-exported, or regenerated result" in deterministic
    assert "before rerunning deterministic validation" in deterministic
    assert "presenting it for approval, previewing it, or uploading it" in deterministic


def test_ad_creation_orders_semantic_and_deterministic_validation() -> None:
    skill = AD_CREATION_SKILL.read_text(encoding="utf-8")
    generated_flow = GENERATED_IMAGE.read_text(encoding="utf-8")

    assert "Keep image generation and ad rendering separate" in skill
    assert "Translate “make an ad” into the desired subject and scene" in skill
    assert "Inspect the exact result with the shared semantic preflight" in generated_flow
    assert "Show only a candidate that passed the preflight" in skill
    assert "Passing that validator never proves semantic compliance" in generated_flow
    assert "If the corrected result still fails, stop the automatic loop" in generated_flow
    assert "After any repair, re-export, or regeneration prompted by a deterministic failure" in (
        generated_flow
    )
    assert "return to step 3 and repeat the full semantic preflight" in generated_flow


def test_chat_card_copy_never_becomes_a_text_only_ad() -> None:
    skill = AD_CREATION_SKILL.read_text(encoding="utf-8")

    assert "Never present a copy-only `chat_card` as a completed ad" in skill
    assert "Incomplete draft — image required" in skill
    assert "a title, body, CTA, or destination never substitutes" in skill
    assert "explicitly say that no ad or preview is complete yet" in skill
    assert "offer a direct public image URL, an attachment" in skill
    assert "do not proceed to preview, account resolution for a write" in skill
    assert "never call it a completed ad, rendered preview, or ready-to-save draft" in skill


def test_preview_failure_never_becomes_a_text_mockup() -> None:
    skill = AD_CREATION_SKILL.read_text(encoding="utf-8")

    assert "Never substitute ASCII or Unicode box art" in skill
    assert "a Markdown ad card, a prose reconstruction" in skill
    assert "call `preview_existing_ad`" in skill
    assert "never treat metadata as visual proof" in skill
    assert "reconstruct the ad with text or prose" in skill


def test_write_confirmation_uses_contextual_affirmation_not_a_magic_word() -> None:
    skill = AD_CREATION_SKILL.read_text(encoding="utf-8")
    confirmation = skill.split("## 7. Obtain One Full Write Confirmation", 1)[1].split(
        "## 8. Upload and Create", 1
    )[0]

    assert "Interpret approval by meaning and context" in confirmation
    assert "Do not require the literal word `Accept`" in confirmation
    for affirmation in ("“okay,”", "“sure,”", "“do it,”", "“I accept”"):
        assert affirmation in confirmation
    assert "directly answers the complete proposal" in confirmation
    assert "a reply that requests or introduces a change does not authorize a write" in (
        confirmation
    )
    assert "obtain fresh affirmative approval" in confirmation
