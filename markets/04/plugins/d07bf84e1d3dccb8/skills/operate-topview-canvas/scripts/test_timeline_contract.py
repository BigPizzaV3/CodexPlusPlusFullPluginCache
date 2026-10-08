import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[3]
API_PATH = PLUGIN_ROOT / "skills" / "operate-topview-canvas" / "references" / "canvas-mcp-api.md"
RECIPE_PATH = PLUGIN_ROOT / "skills" / "canvas-agent-workflows" / "references" / "recipes" / "timeline.md"
SKILL_PATH = PLUGIN_ROOT / "skills" / "operate-topview-canvas" / "SKILL.md"
WORKFLOW_ROOT = PLUGIN_ROOT / "skills" / "canvas-agent-workflows" / "references" / "workflows"


class TimelineContractTest(unittest.TestCase):
    def test_append_only_safety_gate_is_documented(self) -> None:
        api = API_PATH.read_text(encoding="utf-8")
        recipe = RECIPE_PATH.read_text(encoding="utf-8")
        skill = SKILL_PATH.read_text(encoding="utf-8")

        for text in (api, recipe, skill):
            self.assertIn("append_clip", text)
            self.assertNotIn("update_topview_canvas_timeline", text)
        self.assertIn("空稿", api)
        self.assertIn("empty", recipe)
        self.assertIn("exactly matches", skill)

    def test_operation_edit_and_metadata_retry_are_documented(self) -> None:
        api = API_PATH.read_text(encoding="utf-8")
        recipe = RECIPE_PATH.read_text(encoding="utf-8")
        skill = SKILL_PATH.read_text(encoding="utf-8")

        for text in (api, recipe, skill):
            self.assertIn("edit_topview_canvas_timeline", text)
            self.assertIn("MEDIA_INFO_PENDING", text)
            self.assertIn("commandId", text)
        self.assertIn("`operationResults[]`", api)
        self.assertIn("`createdClipIds[]`", api)
        self.assertNotIn("`split_clip`", api)
        self.assertNotIn("`detach_clip_audio`", api)
        self.assertNotIn("`set_aspect_ratio`", api)
        self.assertIn("`hiddenVisualTrackIds[]`", api)
        self.assertIn("`all_segments` 携带该参数会返回 400", api)
        self.assertIn("完全相同", api)
        self.assertIn("identical", skill)

    def test_timeline_recipe_is_linked_from_video_workflows(self) -> None:
        for name in ("short-film.md", "ecommerce-product-video.md", "social-media-video.md"):
            text = (WORKFLOW_ROOT / name).read_text(encoding="utf-8")
            self.assertIn("[recipes/timeline.md](../recipes/timeline.md)", text)

    def test_workspace_open_is_a_single_ui_action(self) -> None:
        skill = SKILL_PATH.read_text(encoding="utf-8")

        self.assertIn("Browser-native Canvas opening", skill)
        self.assertIn("use only `open_topview_canvas_workspace`", skill)
        self.assertIn("Do not call both", skill)

    def test_browser_plugin_uses_one_authorized_link_and_host_browser(self) -> None:
        skill = SKILL_PATH.read_text(encoding="utf-8")

        self.assertIn("Browser-native Canvas opening", skill)
        self.assertIn("call exactly one of `open_topview_canvas`", skill)
        self.assertIn("use an available host Browser/navigation capability", skill)
        self.assertIn("clickable Markdown fallback", skill)
        self.assertIn("never assemble or guess a Canvas URL", skill)
        self.assertIn("does not expose iframe-only helpers", skill)


if __name__ == "__main__":
    unittest.main()
