# 通用空间镜头

Wandeo 0.6.0 的 `spatial` 字段提供确定性的 Three.js/WebGL 和 anatomy 等轴测场景，并可与同一镜头的录屏、视频、图片、SVG、字幕和图表混排。先运行 `project capabilities`，再按内容选择 2D、3D 或混合表达。`backend: "three"` 适合真实 GLB 和材质，`backend: "anatomy"` 适合结构、剖面、因果和解释型图解，`backend: "auto"` 根据是否有 anatomy 描述自动选择。

科普、机制、内部结构和原理解释优先执行 [Anatomy explainer](../../anatomy-explainer/SKILL.md)：先用上游原始 kit 编写完整对象、关系和状态模型，再进入镜头编排。精细等轴测 SVG 本身就可以形成有体积的技术插画；并不要求所有部件都使用真实 3D，也不以找到 GLB 为前提。用户明确选择的手法优先。

## 什么时候用 3D

- 用 3D 解释内部结构、空间尺度、路径、层次、拆解和因果关系。
- 用 2D 表达旁白、证据、数字、长文本和普通 UI。
- 混合镜头让 3D 建立空间关系，2D 字幕、标注、图表或网页录屏给出证据。
- 不为了“看起来高级”给普通字幕或简单 UI 添加 3D。

每个 3D 镜头在导演状态里记录目标对象、相机目标、主要动作和可观察结果。先建立空间关系，再添加文字和装饰。

## 资产和场景

`media import` 接受本地或公开 HTTPS 的 `.glb`/`.gltf`。导入返回稳定 `assetId`，同时记录节点、动画、材质、纹理、包围盒、外部依赖、来源 URL、版本和许可证。渲染只读取项目目录里的资产；不要在 `project.json` 或运行时写 CDN URL。

可组合的 `procedural.preset` 包括 `box`、`plane`、`sphere`、`cylinder`、`cone`、`line`、`curve`、`tube`、`arrow`、`gear`、`shaft`、`spring`、`ring`、`grid`、`axis`、`measurement`、`callout`、`particle-field`、`flow-field`、`exploded-assembly` 以及 `gear-train`、`molecule`、`solar-system`、`product-assembly` 示例 preset。它们适合抽象关系和快速验证，不能替代 anatomy-quality 的 authored figure。需要精细机械结构、可读剖面、多个连接件和可靠遮挡关系时，使用 pinned anatomy examples 的 authoring pattern 或导入真实 GLB/GLTF；不要把几个 procedural primitive 组合后宣称使用了 anatomy。

相机可以使用 perspective 或 orthographic 投影、near/far 裁剪和显式 keyframes。模型通过 `assetId`、`procedural` 或 `instanceOf` 之一进入 Three.js 场景；用 `parentId` 组合层次，用 `section` 的 `clip`/`slice` 表达剖面。模型 range 默认覆盖整个镜头。灯光、材质和注释都应该服务于可观察结果。anatomy 的首选作品路径是 `anatomy import` 注册自包含作品，用 `anatomyFigures` 和 `anatomy.figureId` 在多个镜头复用，以 `anatomy.view` 控制取景、模型时间和部件强调。旧的 `parts`、`groups`、`layers` 和 `keyframes` 描述仍可用，但不是完整原创作品的唯一接口。详见 [作品契约](../../anatomy-explainer/references/authored-figure.md)。

## 动画和审片

使用 `transform`、`camera`、`visibility`、`material`、`light`、`path` 和 `instance` 轨道。预置动作（`orbit`、`follow-path`、`explode`、`assemble`、`reveal-section`、`highlight`、`measure`、`flow`、`rotate`、`oscillate`、`pulse`、`morph`）由导演根据目标对象和结果展开。首版使用显式关键帧和确定性数学动画，不使用墙上时钟、`requestAnimationFrame` 或刚体物理。

先 `project validate`，再渲染局部 preview。`review` 至少抽取模型进入/退出、镜头切换、爆炸视图、重点标注和动画结果，并查看 full-size 与 `smallScreenFrames`。检查模型是否加载、相机是否裁剪、模型是否离开画面、标注是否被遮挡、动作是否过快，以及小屏上模型和标签是否可读。

WebGL 会使用固定 Three.js runtime 和 ANGLE/SwiftShader 参数。纯程序化 Three.js 镜头在 WebGL 不可用时使用 Canvas 2D 降级；含真实模型的镜头会返回明确诊断并停止把占位诊断当成合格成片。anatomy 调用固定提交的上游 SVG 几何、材质和运动 painter，同一几何可以栅格化到 Canvas 2D；验证使用上游端点、支撑、间隙和动态深度审计。记录 runtime 版本、backend、模型来源/许可证、相机、灯光、关键帧、质量配置和项目 revision。

For native anatomy use the actual observed backend in the render report, not the installed plugin version. See [anatomy](spatial-anatomy.md) for Z-up coordinates, axis-correct groups, real cut geometry, mixed model viewports and upstream audit constraints.
