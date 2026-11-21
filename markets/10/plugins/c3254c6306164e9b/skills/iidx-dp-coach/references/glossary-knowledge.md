# 오소리 IIDX DP 코치 — Glossary Knowledge

이 문서는 `/api/glossary` 응답의 정적 용어 사전을 Knowledge 검색용 Markdown으로 재구성한 것이다. JSON 키를 그대로 나열하지 않고 검색 가능한 제목과 설명으로 정리했다. `knowledge.md`에 이미 있는 상세 정의는 중복하지 않고 해당 절을 참조한다.

## 핵심 오해 방지

### `game_level`·`zasa`·`star_estimate` — 곡 레벨과 플레이어 실력

사용자가 “몇 레벨 / N렙 / level”이라고 하면 곡의 **게임 레벨(`game_level`, 보통 11·12)** 또는 **`zasa`**를 뜻한다. `star_estimate`(★)는 플레이어 실력 지표이지 곡 레벨이 아니다. “12레벨 곡”을 ★12로 해석하지 않는다. 자세한 정의는 `knowledge.md` §1.1 및 §12를 참조한다.

### `star_estimate`(★)와 `r_star`(r★)를 섞지 말 것

`star_estimate`(★)는 클리어 실력 축이고, `r_star`(r★)는 점수 실력 축이다. 둘 다 곡 레벨이 아니며 서로 대체하거나 같은 값처럼 해석하지 않는다. `star_estimate`·`est_ec`/`est_hc`/`est_exh`와 `r_star`를 섞어 클리어 가능성이나 점수 가능성을 단정하지 않는다. 상세는 `knowledge.md` §1–§2를 참조한다.

### `r_star.a`·`aa`·`aaa`·`maxm` — 등급별 점수 실력

곡의 A(66.7%), AA(77.8%), AAA(88.9%), MAX−(94.4%)에 필요한 스코어 실력 r★다. 플레이어 `r_star`와 직접 비교한다. `null`은 해당 등급을 산출하지 못한 것이므로 다른 등급 값으로 메우지 않는다. 상세는 `knowledge.md` §2를 참조한다.

## 이미 `knowledge.md`에 있는 중복 정의의 정본 위치

다음 glossary 항목은 내용이 중복되므로 이 문서에서 재기록하지 않는다. 아래 절이 glossary 내용의 참조 위치다.

| Glossary 항목 | 상세 정본 |
|---|---|
| `bp`, `delta_bp`, FAILED+BP 0 | `knowledge.md` 「BP 결측과 0의 구분」 |
| `star_estimate`, `native_star`, `r_star`, `est_ec/hc/exh` | `knowledge.md` §1.1–§1.3 |
| `r_star.a/aa/aaa/maxm`, `achieved_r_star` | `knowledge.md` §2–§3 |
| `features.scores`, `max_score_by_feat`, `missing`, `pattern_percentiles` | `knowledge.md` §5.2–§5.5 |
| `dp_feature_scores`, report의 `σ` | `knowledge.md` §6 |
| 대표 패턴 10축과 세부 패턴 키 | `knowledge.md` §7, §13 |
| `series`, `in_ac`, `in_inf` | `knowledge.md` §10 |
| `score_rate`, `target_star`, `score_offset`, `zasa` | `knowledge.md` §11–§12 |

## `dan_reference` — 단위인정과 ★ 하한

Supabase DP 유저 실측의 각 단위 취득자 하위 10% `star_estimate`(하한)다. “그 별값을 넘으면 해당 단위권”이라는 참고치일 뿐 합격 보장이 아니다. 十段 약 ★4.2, 中伝 약 ★6.4, 皆伝 약 ★9.7이다. 과제곡·게이지·판단은 `dan-knowledge.md`를 근거로 한다.

## `titles` — 성향 리포트 헤드라인 배지

헤드라인 맨 앞에 붙는 전 유저 상위권 배지다.

### `만능형`

곡 유형 강약이 고르게 퍼져 뚜렷한 약점이 없고, 저실력대가 아닌 유형.

### `스코어링마스터`

어나더 이상 채보의 70% 이상을 MAX−권(94.4% 이상)으로 플레이하는 유형.

### `EX하드마스터`

12레벨 곡의 DP 90% 이상(SP 95% 이상)을 EX-HARD 이상으로 클리어하는 유형.

### `풀콤보마스터`

12레벨 곡의 DP 90% 이상(SP 95% 이상)을 풀콤보/퍼펙트로 클리어하는 유형.

## `patterns` — 대표 패턴 용어

기존 기본 패턴 10축과 DP 전용 양손 상호작용 축을 안내한다. 추천 `feature` 이름은 대문자 키이며, 세부축은 `pattern_taxonomy`를 따른다.

### 대표 10축과 `HANDS`

- `NOTES`: 밀도 — 전체 노트 밀도. 곡 길이로 인한 지구력과는 별개.
- `CHORD`: 동치 — 여러 버튼을 동시에 치는 화음.
- `PEAK`: 순간밀도 — 순간적으로 노트가 폭발하는 구간.
- `CHARGE`: 차지 — 롱노트(CN)·백스핀스크(BSS) 등 누르는 노트.
- `SCRATCH`: 스크래치 — 턴테이블.
- `SOF-LAN`: 소프란 — 곡 중 BPM이 바뀌는 변속 구간.
- `PHRASE`: 계단 — 인접 버튼이 연속으로 이어지는 배치.
- `JACK`: 연타(잭) — 같은 버튼을 빠르게 반복.
- `TRILL`: 트릴 — 두 버튼을 번갈아 치는 패턴.
- `RAND`: 난타 — 규칙 없이 흩어진 불규칙 배치.
- `HANDS`: 양손 상호작용 — 좌우 손의 협응·독립·역할분리(DP 전용 대표 피처).

각 대표피처에는 세부축이 있고, 세부 키도 `recommendSongs kind=practice`의 `feature` 인수에 그대로 넣을 수 있다. 별도 `subfeature` 인수는 없다.

## `layout_notation` — 추천 배치 표기

추천 row의 `layout`은 손과 패턴의 매치가 가장 좋은 옵션 배치다. 8배치(정배치/FLIP/좌우 MIRROR 조합)는 `recommend`에 `layout=on`을 줬을 때만 나온다. 엔진이 고른 표기가 추천 배치다.

- `정배치`: 1P/2P 원래 배치가 최선.
- `F`: FLIP — 1P/2P 채보를 통째로 맞바꿈.
- `M/-`: 왼쪽(1P)만 MIRROR.
- `-/M`: 오른쪽(2P)만 MIRROR.
- `M/M`: 양쪽 모두 MIRROR.
- `F M/-`: FLIP 후 왼쪽 MIRROR. 다른 조합도 같은 표기법.

## `layout_axes` — DP 좌우 강약

같은 채보가 좌우 손에 어떻게 나뉘는지에 따른 강약이며 persona report의 🧩 섹션이다.

- `계마`: 건반을 건너뛰며 옮기는 배치(桂馬, 1→3→5).
- `겹계단`: 양손 계단이 겹쳐 들어오는 배치.
- `한손계단/쌍계단/대칭계단/비대칭계단`: 양손 계단이 한 손 몰림/양손 동시/좌우 대칭/좌우 다른 모양.
- `오른나선/왼나선`: 한 손이 나선형으로 감아 올라가거나 내려오는 진행.
- `N번키 강/약`: 특정 건반(1~7번)의 상대 강약. report 세부줄의 +는 왼손 우세, −는 오른손 우세.

## `personal_diff` — 개인차

사람마다 갈리는 요소이며 persona에서는 raw 잔차를 유지하고 centering하지 않는다.

- `차지/스크/소프란`: 개인차가 큰 세 요소.
- `견제스크`: 스크래치와 건반을 번갈아 처리.
- `롤속도`: 스크래치 롤(연속 스크)의 속도대별 강약.
- `차지+견제 동반`: 롱노트를 누른 채 다른 것을 치는 계열.

## `speed_themes` — 속도 성향

헤드라인·요약에 등장하는 속도 성향이다.

- `고속형`: 빠른 구간에서 오히려 성적이 오르는 반사신경형.
- `저속안정형`: 저속에서는 안정적이나 속도가 붙으면 흔들림.
- `스크롤약점`: 노트는 잘 치나 고BPM으로 화면이 빨라지면 약함.
- `물리속도약점`: 고BPM 스크롤에는 적응했으나 조밀한 고속 리듬에서 흔들림.
- `물리 노트속도`: 건반 노트가 실제 손에 닿는 속도(BPM×밀도). 화면 스크롤과 별개.

## `muri` — 무리배치 내성

정배치로 처리하기 어려운 운지에 대한 내성이다. “내성 강함”은 잘 버틴다는 뜻이다.

- `스크무리`: 스크래치와 먼 건반을 동시에 처리하는 DP 무리 운지.
- `무리트릴`: 약지·소지로 쳐야 하는 트릴.
- `데님`: 양손 겹밀도(지그재그 고밀도)(SP).
- `한손몰림`: 한 손에 노트가 몰리는 배치(SP).

## `style_tags` — 성향 태그

- `#램프지향`: 동레벨 대비 스코어율이 낮고 점수보다 클리어(램프)를 파는 성향.
- `#스코어지향`: 동레벨 대비 스코어율이 높고 점수를 파고드는 성향.
- `#OO↑ / #OO↓`: ↑는 강함, ↓는 약함.

## `how_to_read` — 리포트 읽는 순서

1. 맨 앞 칭호는 전 유저 상위권 배지이며, 있으면 먼저 본다.
2. 정체성은 지력계 주력 + 최대 약점(발목) + 개인차 강점으로 읽는다.
3. 🎯🎲⚡🛠✋ 섹션은 본인 평균 대비 상대 강약이며 숫자가 클수록 그 방향이 뚜렷하다.
4. 절대 실력이 아니라 “이 사람은 무엇을 상대적으로 잘/못하나”를 읽는다.
5. 약점·강점은 게임 노트레이더(6축)가 아니라 `analysis`의 `report`와 `dp_feature_scores`를 근거로 한다.

## `pattern_taxonomy` — 대표피처·세부피처 관계

이 블록은 엔진의 `PRACTICE_PARENTS`, `PRACTICE_SUBFEATS`, `PRACTICE_SUBFEATS_HIDDEN`, `SUBFEAT_MODES`, `SUBFEAT_MODES_HAND` 및 공유 라벨에서 조립된다. 그러므로 파일에 임의의 고정 목록을 만들어 엔진과 어긋나게 하지 않는다.

- `_note`: 대표피처↔세부피처 관계. 세부피처를 연습하려면 `feature` 인수에 세부 키를 그대로 넣고 별도 `subfeature` 인수는 쓰지 않는다.
- `_example`: `/api/{iidxId}/recommend?kind=practice&feature=DOUBLE_STAIR&strength=1&zasaMin=11.3&zasaMax=12.0`
- `_hand_mode`: `handMode=both|left|right`; 각 세부피처의 `supports_hand_mode`를 따른다. 쌍 축(both만)에 left/right를 주면 의미가 없다.
- `_visible`: `visible=false` 축은 표본·해석 문제 때문에 개별 지정보다 대표피처 전체 요청을 권한다.
- 각 대표피처에는 `label`, `supports_practice`, `subfeatures`가 있고, 각 세부피처에는 `key`, `label`, `visible`, `dims`, `hand_split`, `supports_hand_mode`, `axis_kind`가 있다. `dims`가 비어 있으면 `axis_kind`는 `filter`, 아니면 `score`다.
- `hand_split`은 차원명에 `_L`이 있는지로 표시되며, 손 분할 가능 여부 자체는 `supports_hand_mode` 선언을 따른다. `both`가 기본값이다.

## 적용 원칙

`_note`를 포함한 위 경고는 장식이 아니라 판단 경계다. 특히 **★는 곡 레벨이 아니며**, **`r_star`와 `star_estimate`를 섞지 말아야 한다**. 없는 값은 추측으로 채우지 않고, 상대 강약은 절대 실력으로 표현하지 않는다.
