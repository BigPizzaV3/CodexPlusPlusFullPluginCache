"""Regression checks for the partner-feedback requirements."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ecvc-financing-readiness"


def read(relative_path: str) -> str:
    return (SKILL / relative_path).read_text(encoding="utf-8")


def main() -> None:
    questionnaire = read("references/questionnaire.md")
    framework = read("references/readiness-framework.md")
    index = read("references/data-room-index.md")
    experience = read("references/experience-design.md")
    skill = read("SKILL.md")

    required_questionnaire_terms = (
        "leased or owned offices, labs, warehouses, facilities, or other real estate",
        "jurisdictions for qualification/registration review",
        "Pending or threatened litigation",
        "Pending or registered patents, trademarks, and copyrights",
        "held personally by founders",
        "Website, app, user, customer, or subscription terms",
        "Optional pitch-deck upload",
        "Still to answer",
    )
    for term in required_questionnaire_terms:
        assert term in questionnaire, f"Missing questionnaire requirement: {term}"

    assert "10. Financing materials" not in index
    assert "Do not create a financing-materials folder" in index
    assert "Target raise, expected structure, and timing recorded" not in framework
    assert "Projections and proposed use of financing proceeds" not in framework
    assert "Step X of 7" in skill and "Step X of 7" in experience
    assert "Seven horizontal category bars" in experience
    assert "Render the title exactly once" in experience

    categories: list[tuple[str, int, int]] = []
    active_name = ""
    active_target = 0
    active_items = 0
    for line in framework.splitlines():
        category = re.fullmatch(r"\| \*\*(.+)\*\* \| \*\*(\d+)\*\* \|", line)
        item = re.fullmatch(r"\| (?!\*\*)(.+) \| (\d+) \|", line)
        if category:
            if active_name:
                categories.append((active_name, active_target, active_items))
            active_name, active_target, active_items = category.group(1), int(category.group(2)), 0
        elif item and active_name:
            active_items += int(item.group(2))
    if active_name:
        categories.append((active_name, active_target, active_items))

    assert [target for _, target, _ in categories] == [20, 20, 25, 10, 15, 5, 5]
    assert all(target == items for _, target, items in categories), categories
    assert sum(target for _, target, _ in categories) == 100

    print("Partner-feedback regression checks passed.")


if __name__ == "__main__":
    main()
