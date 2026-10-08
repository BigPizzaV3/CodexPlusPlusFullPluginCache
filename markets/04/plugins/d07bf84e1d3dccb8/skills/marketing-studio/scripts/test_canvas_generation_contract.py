import json
import re
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[3]
CANVAS_SKILL_ROOT = PLUGIN_ROOT / "skills" / "operate-topview-canvas"
WORKFLOWS_ROOT = PLUGIN_ROOT / "skills" / "canvas-agent-workflows"
SKILL_PATH = CANVAS_SKILL_ROOT / "SKILL.md"
FIXTURE_PATH = CANVAS_SKILL_ROOT / "canvas-generation-contract.fixture.json"
MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
API_PATH = CANVAS_SKILL_ROOT / "references" / "canvas-mcp-api.md"
PLANNING_PATH = CANVAS_SKILL_ROOT / "references" / "generation-planning.md"
ORCHESTRATION_PATH = WORKFLOWS_ROOT / "references" / "orchestration-runtime.md"
STAGE_MACHINE_PATH = WORKFLOWS_ROOT / "references" / "generation-stage-machine.md"
GENERATION_TOOLS = [
    "get_topview_canvas_generation_capabilities",
    "submit_topview_canvas_generation_task",
    "refresh_topview_canvas_generation_task",
]

NEGATION_MARKERS = (
    "not ",
    "no ",
    "**not**",
    "*not*",
    "do not",
    "must not",
    "勿",
    "不要",
    "不传",
    "不用",
    "无需",
    "不得",
    "不应",
    "禁止",
    "不再",
    "forbid",
    "observational",
    "仅观测",
    "仅供观测",
    "无",
)


def _snippet_has_negation(snippet: str) -> bool:
    normalized = re.sub(r"\*+", "", snippet.lower())
    return any(
        marker in snippet.lower() or marker in normalized
        for marker in NEGATION_MARKERS
    )


class CanvasGenerationContractTest(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = SKILL_PATH.read_text(encoding="utf-8")
        self.api = API_PATH.read_text(encoding="utf-8")
        self.planning = PLANNING_PATH.read_text(encoding="utf-8")
        self.orchestration = ORCHESTRATION_PATH.read_text(encoding="utf-8")
        self.stage_machine = STAGE_MACHINE_PATH.read_text(encoding="utf-8")
        self.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.generation_section = self.skill.split(
            "## Generate media into a Canvas", 1
        )[1].split("## Timeline", 1)[0]
        self.efficiency = self.fixture["agentEfficiency"]

    def test_fixture_exposes_generation_tools(self) -> None:
        self.assertEqual(GENERATION_TOOLS, list(self.fixture["tools"]))

    def test_skill_uses_capability_submit_refresh_in_order(self) -> None:
        # Order is defined by the Capability-bound flow; approval-mode prose may
        # mention submit earlier as the paid-entry choke point.
        flow_section = self.generation_section.split(
            "### Capability-bound submit flows", 1
        )[1]
        positions = [flow_section.index(name) for name in GENERATION_TOOLS]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("Do **not** call `topview_get_generation_config`", self.generation_section)
        self.assertRegex(
            self.generation_section,
            r"Do \*\*not\*\* call .*`topview_generate_image`",
        )
        self.assertNotIn("submit_topview_canvas_scene_generation_task", self.skill)
        self.assertIn("generationKind=scene_storyboard", self.generation_section)
        self.assertNotIn("sceneGenerationKind", self.skill)
        self.assertNotIn("submissionTool=", self.skill)

    def test_copyable_submit_example_matches_fixture(self) -> None:
        examples = re.findall(
            r"```json\n(\{.*?\})\n```", self.generation_section, flags=re.DOTALL
        )
        self.assertEqual(1, len(examples))
        self.assertEqual(
            self.fixture["tools"]["submit_topview_canvas_generation_task"]["arguments"],
            json.loads(examples[0]),
        )

    def test_typed_input_and_media_ref_rules_are_documented(self) -> None:
        for required_text in (
            "capabilityVersion",
            "inputRoles",
            "`inputs`",
            "mention.shortCode",
            "mediaRef",
            "commandId",
        ):
            self.assertIn(required_text, self.generation_section)
        self.assertIn("parametersSchema", self.generation_section)
        self.assertIn("do not hard-require `parametersSchema`", self.generation_section)
        for required_text in (
            "pending_projection",
            "projection_failed",
            "consistencyStatus",
        ):
            self.assertIn(required_text, self.skill)

    def test_scene_storyboard_fixture_is_server_derived(self) -> None:
        scenario = self.fixture["scenarios"]["sceneStoryboard"]
        arguments = scenario["arguments"]
        self.assertEqual("scene_storyboard", arguments["generationKind"])
        self.assertEqual("node_scene_…", arguments["sceneNodeId"])
        for forbidden in scenario["forbiddenArguments"]:
            self.assertNotIn(forbidden, arguments)
        self.assertIn("REFERENCE_MEDIA_PENDING", self.skill)
        self.assertIn("sceneNodeId", self.generation_section)

    def test_observational_revision_and_get_mcp_tools_cache(self) -> None:
        self.assertEqual(
            "observational_response_only",
            self.efficiency["revisionPolicy"],
        )
        self.assertTrue(self.efficiency["forbidExpectedRevision"])
        self.assertTrue(self.efficiency["forbidFieldsRevisionFilter"])
        self.assertTrue(self.efficiency["forbidFieldsEnvironmentFilter"])
        self.assertTrue(self.efficiency["forbidMaxRevisionCursor"])
        self.assertTrue(self.efficiency["observationalRevision"])
        self.assertFalse(self.efficiency["getStateBeforeEveryWrite"])
        self.assertFalse(self.efficiency["maxReturnedRevisionAfterWave"])
        self.assertEqual(
            "once_per_server_tool_schema",
            self.efficiency["getMcpToolsPerSession"],
        )
        self.assertIn("Observational revision only", self.skill)
        self.assertIn("Revision 仅观测", self.api)
        self.assertIn("GetMcpTools cache", self.skill)
        self.assertIn("at most once per session", self.skill)

    def test_paid_generation_approval_mode_gate(self) -> None:
        self.assertEqual(
            "ask_on_first_submit",
            self.efficiency["paidGenerationApprovalMode"],
        )
        self.assertEqual(
            ["confirm_each_submit", "autonomous"],
            self.efficiency["paidGenerationApprovalModes"],
        )
        self.assertTrue(self.efficiency["forbidPaidSubmitBeforeApprovalMode"])
        self.assertIn("Paid generation approval mode", self.generation_section)
        self.assertIn("confirm_each_submit", self.generation_section)
        self.assertIn("autonomous", self.generation_section)
        self.assertIn("paid generation approval mode gate", self.generation_section)
        self.assertIn("confirm_each_submit", self.api)
        self.assertIn("autonomous", self.api)
        for text in (self.generation_section, self.api):
            self.assertIn("Ask Question", text)
            self.assertIn("逐步请求审批", text)
            self.assertIn("自动推进完成", text)
            self.assertIn("Request approval step by step", text)
            self.assertIn("Automatically proceed to completion", text)
        self.assertIn(
            "Do not ask the user to type an internal mode ID",
            self.generation_section,
        )
        self.assertIn("不要让用户输入模式 id", self.api)
        self.assertIn("paid generation approval mode", self.orchestration.lower())
        self.assertIn("confirm_each_submit", self.orchestration)
        # Negatively forbid positive teaching of old Canvas revision CAS.
        for text in (self.skill, self.api, self.orchestration, self.stage_machine):
            for match in re.finditer(
                r"(?i)Revision chaining|链式传递|chain(?:ed|ing)?(?: the)? revisions?",
                text,
            ):
                start = max(0, match.start() - 96)
                snippet = text[start : match.end() + 24]
                self.assertTrue(
                    _snippet_has_negation(snippet),
                    msg=f"positive revision-chaining teaching: {match.group(0)!r}",
                )
            # Positive "send/require expectedRevision" without nearby negation.
            for match in re.finditer(r"(?i)expectedRevision", text):
                start = max(0, match.start() - 64)
                snippet = text[start : match.end() + 48]
                # Timeline ETag path is allowed to mention REVISION_CONFLICT separately.
                lowered = snippet.lower()
                if "expectedtimelineetag" in lowered or (
                    "timeline" in lowered and "etag" in lowered
                ):
                    continue
                self.assertTrue(
                    _snippet_has_negation(snippet),
                    msg=f"positive expectedRevision teaching: {text[match.start()-40:match.end()+40]!r}",
                )
        self.assertNotRegex(
            self.skill,
            r"(?i)re-read state before each write/refresh",
        )
        self.assertNotRegex(
            self.orchestration,
            r"(?i)re-read .*get_topview_canvas_state.*before dependent",
        )
        self.assertNotIn(
            "before dependent stages",
            self.orchestration,
        )

    def test_user_facing_canvas_updates_are_name_first_and_text_nodes_are_visible(self) -> None:
        self.assertIn("Canvas name and the created or changed node names", self.skill)
        self.assertIn("do not lead a user-facing update with raw IDs", self.skill)
        self.assertIn("TextNode visibility contract", self.skill)
        self.assertIn("title-only TextNode", self.skill)
        self.assertIn('backgroundColor: "#1A1A1A"', self.skill)
        self.assertIn('color: "#FFFFFF"', self.skill)
        self.assertIn("`title` 仅元数据；可见正文是非空 `content`", self.api)

    def test_capabilities_summary_and_identity_rules(self) -> None:
        caps = self.fixture["tools"]["get_topview_canvas_generation_capabilities"]
        self.assertEqual([], caps["arguments"]["include"])
        self.assertIn("taskType", caps["arguments"])
        for field in ("requiredParameters", "defaults", "parameterEnums", "inputRoles"):
            self.assertIn(field, caps["summaryFields"])
        self.assertIn("include=[]", self.skill)
        self.assertIn('include=["schema"]', self.skill)
        self.assertIn("inputRoles", self.skill)
        self.assertIn("inputRoles", self.planning)
        self.assertIn("inputRoles", self.api)
        self.assertIn("canvas_node", self.generation_section)
        self.assertIn("Do **not** require or read Agent-facing `assetId`", self.skill)
        self.assertIn("assetId", self.efficiency["forbiddenAgentFields"])
        self.assertIn("canvas_asset", self.efficiency["forbiddenAgentFields"])
        self.assertIn("PARAMETER_VALIDATION_FAILED", self.skill)
        self.assertIn("PARAMETER_VALIDATION_FAILED", self.api)

    def test_deprecated_canvas_asset_wire_compat_agent_forbidden(self) -> None:
        self.assertIn("wire-level deprecated", self.api)
        self.assertIn("canvas_asset", self.api)
        self.assertIn("Agent 禁止使用", self.api)
        self.assertIn("canvas_asset", self.skill)
        self.assertIn("Do **not** use deprecated wire `canvas_asset`", self.skill)

    def test_safe_parallel_policy_and_efficiency_flags(self) -> None:
        self.assertFalse(self.efficiency["parallelSameCanvasWrites"])
        self.assertFalse(self.efficiency["parallelSameTargetWrites"])
        self.assertTrue(self.efficiency["preferParallelIndependentTools"])
        self.assertTrue(self.efficiency["waitAllParallelWave"])
        self.assertFalse(self.efficiency["maxReturnedRevisionAfterWave"])
        self.assertTrue(self.efficiency["requirePreplannedGeometryForParallelCreate"])
        self.assertFalse(self.efficiency["sameCanvasRefreshSerial"])
        self.assertTrue(self.efficiency["parallelRefreshAfterSerialSubmit"])
        self.assertTrue(self.efficiency["slimRefreshByDefault"])
        self.assertTrue(self.efficiency["stateFilters"])
        self.assertTrue(self.efficiency["backgroundGenerationConcurrent"])
        for field in (
            "nodes.basic",
            "nodes.geometry",
            "nodes.identity",
            "nodes.generation",
            "nodes.hierarchy",
            "webUrl",
        ):
            self.assertIn(field, self.efficiency["stateProjectionFields"])
        self.assertNotIn("environment", self.efficiency["stateProjectionFields"])
        self.assertNotIn("report environment", self.skill)

        for text in (self.skill, self.stage_machine, self.orchestration, self.api):
            self.assertIn("Safe Parallel Policy", text)
            self.assertRegex(text, r"(?i)wait-all")
            self.assertRegex(text, r"(?i)distinct.*commandId|commandId.*distinct")
            self.assertRegex(text, r"(?i)consistencyStatus=projected|projected")
            # max(revision) may appear only as forbidden / do-not language.
            for match in re.finditer(r"(?i)max\(revision", text):
                start = max(0, match.start() - 72)
                snippet = text[start : match.end() + 40]
                self.assertTrue(
                    _snippet_has_negation(snippet),
                    msg=f"positive max(revision) cursor teaching: {match.group(0)!r}",
                )
            # fields=["environment"] may appear only as forbidden / do-not language.
            for match in re.finditer(r'fields=\["environment"\]', text):
                start = max(0, match.start() - 72)
                snippet = text[start : match.end() + 40]
                self.assertTrue(
                    _snippet_has_negation(snippet),
                    msg=f'positive fields=["environment"] teaching: {match.group(0)!r}',
                )

        # Ban positive unconditional parallel-write claims and obsolete shared-latest language.
        for text in (self.skill, self.stage_machine, self.orchestration, self.api):
            self.assertNotRegex(
                text,
                r"(?i)(?<!not )(?<!no )(?<!ban )always parallel.{0,20}(?:create|submit|write)"
                r"|parallelSameCanvasWrites.?=.?true",
            )
            # Positive "unconditional parallel write" without a nearby ban/negation.
            for match in re.finditer(
                r"(?i)unconditional.{0,40}parallel.{0,20}write",
                text,
            ):
                start = max(0, match.start() - 48)
                snippet = text[start : match.end() + 24].lower()
                self.assertTrue(
                    any(
                        marker in snippet
                        for marker in (
                            "not ",
                            "no ",
                            "ban",
                            "must not",
                            "do not",
                            "禁止",
                            "不要",
                        )
                    ),
                    msg=f"unconditional parallel-write claim without negation: {match.group(0)!r}",
                )
            self.assertNotRegex(
                text,
                r"(?i)(?:or the )?shared latest successful revision"
                r"|chaining each poll.?s `lastRevision` \(or the shared",
            )
            self.assertNotRegex(
                text,
                r"(?i)Serial write vs parallel refresh",
            )
        self.assertNotRegex(
            self.skill,
            r"(?i)batch\s+(submit|mutation|write|create)",
        )
        self.assertNotIn("one revision cursor", self.skill)
        self.assertNotIn("one revision cursor", self.stage_machine)
        # Must not demand blanket serial refresh.
        self.assertNotIn("串行 create/submit/refresh", self.api)
        self.assertNotIn("Serial create / submit / refresh", self.skill)
        self.assertNotIn("Serial create / submit / refresh", self.stage_machine)

    def test_layout_state_filters_and_slim_refresh_language(self) -> None:
        layout_path = CANVAS_SKILL_ROOT / "references" / "node-layout.md"
        layout = layout_path.read_text(encoding="utf-8")
        for text in (self.skill, self.api, layout):
            self.assertRegex(text, r"(?i)layout:\s*\{\s*x")
            self.assertRegex(
                text,
                r"(?i)forbidden.{0,40}(?:nodeId|parentId|sceneNodeId)"
                r"|(?:nodeId|parentId|sceneNodeId).{0,40}forbidden",
            )
            self.assertRegex(text, r"(?i)\(0,\s*0\)|0,0")
            self.assertRegex(text, r"(?i)no BFF auto|无.*BFF.*自动避让|no.*BFF auto-avoidance")
        for text in (self.skill, self.api):
            # fields=["revision"] only allowed as forbidden guidance.
            for match in re.finditer(r'fields=\["revision"\]', text):
                start = max(0, match.start() - 64)
                snippet = text[start : match.end() + 40]
                self.assertTrue(
                    _snippet_has_negation(snippet),
                    msg="positive fields=[revision] teaching",
                )
            self.assertRegex(text, r"(?i)nodes\.basic|nodes\.geometry|nodes\.identity")
            self.assertRegex(
                text,
                r"(?i)project|裁剪|投影",
            )
            self.assertRegex(text, r"(?i)do \*\*not\*\* claim `sinceRevision`|不要.*sinceRevision|无.*sinceRevision")
            self.assertRegex(text, r"(?i)slim")
            self.assertIn('include=["state"]', text)
            self.assertRegex(
                text,
                r"(?i)do not pass `include`|勿传 include|不要传 `include`"
                r"|omit include|omit or `?include=\[\]`?"
                r"|omit 或 include=\[\]|不传或 `include=\[\]`|omit/`include=\[\]`|omit 或 `include=\[\]`",
            )

    def test_scenecard_does_not_require_get_state_per_card(self) -> None:
        scene_section = self.skill.split("## Create a SceneCard", 1)[1].split(
            "## Generate media into a Canvas", 1
        )[0]
        self.assertIn("first SceneCard", scene_section)
        self.assertIn("geometry is stale", scene_section)
        self.assertNotRegex(
            scene_section,
            r"(?i)Read the latest state and compute layout",
        )
        self.assertIn("Do **not** call `get_state` before every subsequent card", scene_section)

    def test_manifest_version_is_generation_contract_release(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertRegex(
            manifest["version"],
            r"^1\.0\.1(?:-build\.\d{14})?$",
        )


if __name__ == "__main__":
    unittest.main()
