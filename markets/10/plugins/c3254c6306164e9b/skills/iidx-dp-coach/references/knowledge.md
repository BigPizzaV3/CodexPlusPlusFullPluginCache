# 오소리 IIDX DP 코치 — Knowledge 참고 문서

커스텀 GPT 의 Knowledge 에 업로드하는 참고 문서다. Instructions 에는 "어떻게 행동할지" 규칙만 두고, 여기에는 **용어 정의·필드 상세·판단 예시·금지사항의 이유**를 둔다. Instructions 와 이 문서가 충돌하면 Instructions 의 행동 규칙이 우선한다.

2026-10-05 SkillEvidence 계약과 `instructions.md` v4에 맞춘 문서다. 웹 API 배포와 GPT의 Actions 스키마·Instructions·Knowledge 갱신은 별개다. 새 도구나 필드가 실제 응답에 없으면 구형 배포·설정 여부를 확인하고 값을 만들어 채우지 않는다.

용어·수치 정의의 정리본은 `glossary-knowledge.md`다. 이 문서와 세부 설명이 겹치면 해당 문서의 절을 함께 참고한다.

---

## BP 결측과 0의 구분

* `bp: null`은 BP 정보가 없다는 뜻이다. 0으로 채우거나 미스가 없었다고 해석하지 않는다.
* `bp: 0`은 저장된 숫자 0이다. 원본은 보존하되, 이 값 하나만으로 미스 없는 완주나 FULL COMBO를 단정하지 않는다. 실제 램프를 함께 확인한다.
* 특히 `FAILED`와 BP 0이 함께 있으면 신뢰하기 어려운 기록으로 취급한다. 기존 HC/EXH BP 추천 필터는 이 조합을 제외한다. API가 원본값을 보여주는 것과 그 값을 코칭 근거로 신뢰하는 것은 별개다.
* HC는 BP 70 이상, EXH는 BP 30 이상을 기존 엔진이 제외한다. 개별 BP null은 0으로 바꾸지 않고 통과시키며, 후보 전체에 BP가 없으면 BP 필터를 생략한다. 따라서 추천됐다는 사실만으로 BP 조건을 충족했다고 말하지 않는다.
* recent의 `delta_bp`는 그날 BP - 직전 잔존 BP로 음수가 감소다. 둘 중 하나라도 null이면 변화량도 null이다. FAILED+BP 0처럼 신뢰하기 어려운 값이 끼면 음수여도 개선이라고 단정하지 않는다.

## 1. 두 개의 실력 축 — ★ 와 r★

오소리는 플레이어 실력을 **서로 다른 두 축**으로 본다. 하나로 합치거나 대체하면 안 된다.

### 1.1 `star_estimate` (★) — 클리어 실력 축

* 곡을 **클리어(램프 갱신)** 하는 능력의 연속 척도.
* 기준점: **★0 = 게임레벨 11 막 시작, ★1 = 게임레벨 12 막 EASY 클리어**. 값이 12를 넘어도 된다.
* `est_ec` / `est_hc` / `est_exh`(곡을 EASY / HARD / EX-HARD 클리어하는 데 필요한 실력 ★)와 **같은 축**이다.
* 추천 API의 `base_star`는 웹의 추천 기준값이다. `native_star` 우선이지만 표시 별값이 0.5 이상 2 미만이면 표시값을 쓰며, native가 없으면 표시값을 쓴다. `star_estimate`와 항상 같은 값은 아니다.
* `native_star` = 추천 난이도 산정용(래칫 없음). 표시 별값과 구분한다.
* ★ ↔ 段位 대략(하한, Supabase DP 유저 실측): **★4.2 ≈ 十段 / ★6.4 ≈ 中伝 / ★9.7 ≈ 皆伝**. 실제 段位는 `profile` 의 `dp.rank`(예 `"十段"`, `rank_int:10`). 단위인정 과제곡·게이지·판단 규칙은 별도 Knowledge `dan-knowledge.md` 를 근거로 한다.

### 1.2 `r_star` (r★) — 스코어 실력 축

* 곡에서 **높은 점수(등급)** 를 내는 능력. 클리어와는 별개 축이다.
* `star_estimate` 와 r★ 의 차이 자체가 성향이다: `star_estimate` > r★ → 램프(클리어) 지향, r★ > `star_estimate` → 스코어 지향. 단 두 값은 다른 축이라 숫자 차이만으로 과도하게 결론내지 말고 recent 와 함께 본다.

### 1.3 절대 섞지 말 것

* 클리어 질문에 r★ 를, 스코어 질문에 `ec/hc/exh` 를 판단 근거로 끌어오지 않는다.
* 램프가 EX-HARD 라고 r★ 가 높다고 말할 수 없고, 점수가 높다고 클리어 실력이 높다고 말할 수 없다.

---

## 2. 곡의 등급별 r★ — `r_star.a / aa / aaa / maxm`

`getSong` 과 `getRecent` 응답의 곡별 필드.

* `r_star.a` = 그 곡에서 **A(66.7%)** 점수를 내는 데 필요한 스코어 실력 r★.
* `r_star.aa` = **AA(77.8%)** 필요 r★.
* `r_star.aaa` = **AAA(88.9%)** 필요 r★.
* `r_star.maxm` = **MAX−(94.4%)** 필요 r★. 실측이 없으면 추정치(estimated)일 수 있다.
* 값이 `null` 인 등급은 그 곡에 대해 아직 산출되지 않은 것 — 없는 값으로 두고 다른 등급으로 설명한다.

### 읽는 법

플레이어 `r_star` 와 곡의 목표 등급 r★ 를 직접 비교한다.

* **곡 `r_star.aaa` < 플레이어 `r_star`** → 그 곡 AAA 는 현재 스코어 실력권 안. 안정화·정확도 연습 대상.
* **곡 `r_star.aaa` ≈ 플레이어 `r_star`** → 현재 실력에 딱 맞는 적정 점수 연습.
* **곡 `r_star.aaa` 가 플레이어보다 조금 높음** → 성장용 도전.
* **곡 `r_star.aaa` 가 크게 높음** → 지금 점수 연습 대상으로는 과하다(목표로만).

예: 플레이어 r★ 5.8, 어떤 곡의 AAA r★ 6.1 → "현재 표시 r★보다 조금 위. AAA 를 내면 표시 r★ 이상의 성과."

---

## 3. `getRecent` 의 r★ 필드

날짜별 질문은 `getRecentDates` → `getRecent date=YYYY-MM-DD` 순으로 조회한다. 날짜 목록은 최대 366개, 날짜 상세는 최대 400행이며 `truncated`가 true이면 일부만 반환된 것이다. 날짜 미지정 recent는 기본 20/최대 50행이다.

`history=ok`는 hist를 읽었다는 뜻이며 전체 플레이가 보존됐다는 보장이 아니다. 같은 곡·난이도·버전·스타일의 하루 갱신행만 남고 오래된 기록은 압축으로 누락될 수 있다. 날짜 누락은 미플레이를 뜻하지 않는다. `history=absent`는 404 미생성, `error`는 조회·파싱 오류다. 둘 다 날짜·곡만 남고 그날 성적·직전값은 null이며 현재값으로 대체하지 않는다. `history_error`와 `reason`을 함께 읽는다.

`prev_*`는 같은 곡·난이도·버전·스타일의 date순 직전 잔존행이다. `delta_ex`/`delta_bp`는 이 두 잔존 기록의 차이이며 연속 두 플레이의 차이는 아니다. 그날 등급은 그날 성적으로 계산하지만 곡별 요구 r★와 플레이어 r★는 조회 시점 값이다. `r_star_delta_vs_player`를 과거 대비 r★ 상승량으로 말하지 않는다.

| 필드 | 의미 |
|---|---|
| `player_r_star` | 응답 최상단. 조회 시점 플레이어의 r★. |
| (row) `grade` | 해당 날짜의 잔존 성적에서 계산한 등급(`A`/`AA`/`AAA`/`MAX-` 또는 그 아래 `B`~`F`). |
| (row) `r_star` | 그 곡의 `{a, aa, aaa, maxm}` 등급별 필요 r★. |
| (row) `achieved_r_star` | **실제 달성 등급에 대응하는 곡 r★.** 예: AAA 를 냈으면 그 곡의 `r_star.aaa`. 달성 등급이 A 미만이거나 해당 등급 r★ 가 `null` 이면 `null`. |
| (row) `r_star_delta_vs_player` | `achieved_r_star − player_r_star`. |

### `r_star_delta_vs_player` 부호 해석

* **양수** → 현재 표시 r★보다 높은 난이도의 스코어 성과(고점 또는 성장 신호).
* **0 부근** → 현재 스코어 실력에 딱 맞는 대표 성과.
* **음수** → 현재 r★보다 낮은 난이도의 성과(안정권).

### `prev_*`/`delta_*`로 의미 있는 변화만 짚기

* `delta_ex`/`delta_bp`가 **정확히 0(또는 둘 다 null)이면 그 곡은 "직전과 변화 없음"으로 한 줄 요약**하고 더 파고들지 않는다. 값이 없다고 굳이 현재값으로 메워 변화를 만들어내지 않는다.
* **0이 아닌 곡만** 방향(개선/저하)과 크기를 짚어 의미 있게 다룬다. 여러 곡 중 일부만 변화가 있으면 그 일부를 중심으로 이야기하고 나머지는 "동일" 로 뭉쳐 요약한다.
* 변화가 있다고 해서 전부 강조하지도 않는다 — `history=absent/error`나 FAILED+BP 0처럼 신뢰하기 어려운 값이 만든 변화는 위 BP 결측 규칙을 따른다.

### 성장 판단

* 최근 여러 곡에서 `r_star_delta_vs_player` 양수가 **반복** → 스코어 실력이 실제로 상승 중일 가능성이 높다. 전체 실력/스코어 성장 분석에서 반드시 언급한다.
* 한 곡에서만 크게 양수 → **고점 기록**으로 구분하고 "성장 확정" 이라고 단정하지 않는다.
* recent 가 대부분 현재 r★보다 낮은 목표 위주라면 높은 점수가 많이 보여도 "현재 r★ 이상으로 성장" 이라고 하지 않는다.
* 램프와 분리: EASY 상태 곡이어도 AAA 를 냈으면 AAA r★ 기준으로 평가. EX-HARD 곡이어도 점수가 낮으면 높은 r★ 성과가 아니다.

---

## 4. 전체 실력 2축 분석 — 예시

질문: "내 실력 분석해줘"

1. **현재 위치** — 段位(`profile.dp.rank`), `star_estimate`, `r_star`, 최근 실제 소화 `zasa` 대(recent).
2. **클리어 실력** — 최근 HARD/EX-HARD 를 안정적으로 붙이는 `zasa`, `getShelf.skill_line.hc/exh.hardest_cleared`. `star_estimate` 는 클리어 축으로 해석.
3. **스코어 실력** — 현재 `r_star`, recent 곡들의 `achieved_r_star` 와 `r_star_delta_vs_player`. 현재 r★ 이상 성과가 반복되는지 / 상승세인지, 안정권인지, 고점 한두 곡인지.
4. **두 축의 균형** — `star_estimate` 대비 r★ 가 높으면 스코어 지향, 낮으면 램프 지향. recent 로 확인.
5. **패턴 강점·약점** — `getAnalysis` 의 `report`. 필요하면 `features=full`.
6. **다음 할 일** — 지금 실력에서 가장 효율적인 연습 방향.

목표가 클리어 또는 스코어 하나로 명확하면 관련 없는 축은 생략한다.

### 클리어 질문 예시

"이 곡 하드 가능?" → `getSong` 의 `est_hc`(또는 추천 row 의 `hc`)와 플레이어 `star_estimate` 비교 + recent 의 비슷한 `zasa` 대 HARD 성과. r★ 얘기는 하지 않는다(사용자가 점수도 물으면 보조로만).

### 스코어 질문 예시

"이 곡 AAA 가능?" → 플레이어 `r_star` vs 곡 `r_star.aaa` + recent 의 유사 `r_star_delta_vs_player` 성과. HC/EXH 필요 ★ 로 가능성을 판단하지 않는다.

---

## 5. 세부 패턴 데이터 — analysis 기본 제공 / song `features=full`

### 5.1 왜 있나

`getAnalysis` 기본 응답에는 대표 10축 `dp_feature_scores` 와 세부축 전체 `features` 블록이 함께 온다. 분석의 `features=full` 은 구형 호출 호환용 no-op 이며 생략해도 결과가 같다. 반면 `getSong` 기본 응답의 `pattern_percentiles` 는 **대표 10축**(NOTES, CHORD, PEAK, CHARGE, SCRATCH, SOF-LAN, PHRASE, JACK, TRILL, RAND)뿐이므로, 곡의 왼손/오른손·계단류·계마·HSTAIR 같은 세부 패턴에는 `getSong features=full` 이 필요하다.

### 5.2 `getAnalysis` 기본 응답 → `features` 블록

| 필드 | 의미 |
|---|---|
| `canonical_count` | 이 유저 축의 정본 개수(현재 **37**). |
| `available_count` | 그중 이 유저가 실제 보유한 축 수. |
| `missing` | 이 유저 데이터에 **아직 없는 축**. 구형 업로드는 `HANDS` 가 없는 등 36축만 있을 수 있다. **0 이 아니라 "미측정" 이다** — 0 으로 해석 금지. |
| `scores` | 축별 **절대 스코어**(곡 피처 백분위 × 실제 EX점수율의 상위 30곡 가중합). 높을수록 그 패턴의 절대 성과가 높다. |
| `max_score_by_feat` | 축별 **이론 최대 스코어**(정본). 축마다 스케일이 크게 달라(NOTES ~1647 vs SOF-LAN ~990) `scores` 원값끼리는 축 간 비교가 안 된다 — 굳이 축 간 비교가 필요하면 `scores[k] / max_score_by_feat[k]` 를 쓴다. |
| `feature_version` | 피처 정의 버전. 백필 전후 데이터 진단용. |

### 5.2A 전체 표본 신뢰도와 피처별 근거의 구분

`getAnalysis.sample`은 분석 전체의 표본 메타이며, 각 피처의 표본 수나 신뢰도가 아니다.

| 필드 | 해석 |
|---|---|
| `n_charts` | persona 분석에 사용된 전체 채보 수. 특정 피처의 기여곡 수가 아니다. |
| `confidence` | 덤프에 저장된 전체 표본 신뢰도. `low`/`medium`/`high` 또는 `null`. |
| `confidence_definition` | 응답 시점의 신뢰도 경계와 결측 정책. 문서의 수치보다 실제 응답을 우선한다. |
| `note` | 표본 크기·선곡 편향에 관한 주의사항. |

현재 정의는 300곡 미만 low, 300~999곡 medium, 1000곡 이상 high다. 다만 재덤프 전에는 `confidence`가 null일 수 있다. null을 low로 바꾸거나 `n_charts`만 보고 API가 주지 않은 등급을 대신 붙이지 않는다.

전체 confidence가 high여도 KEIMA 같은 개별 축의 근거가 충분하다는 뜻은 아니다. 축별 신뢰도·기여곡 목록은 반환된 경우에만 사용한다. `features.missing`은 값이 없는 축을 구분할 뿐, 값이 있는 축의 표본 충실도를 보장하지 않는다. 곡 수·상대순위·기여곡을 추측해 제시하지 않는다.

### 5.3 사용자 canonical feature = 37축

대표 10 + 좌/우 세부 22 + HSTAIR 4 + HANDS 1.

* 대표 10: `NOTES` `CHORD` `PEAK` `CHARGE` `SCRATCH` `SOF-LAN` `PHRASE` `JACK` `TRILL` `RAND`
* 계단 좌/우: `STAIR_UP_L` `STAIR_UP_R` `STAIR_DN_L` `STAIR_DN_R`
* 건반별 밀도 좌/우: `K1_L` `K1_R` … `K7_L` `K7_R` (14축)
* `DOUBLE_STAIR_L` `DOUBLE_STAIR_R` (겹계단)
* `KEIMA_L` `KEIMA_R` (계마 — 건반을 건너뛰는 배치)
* HSTAIR(양손계단): `HSTAIR_ONEHAND` `HSTAIR_SYNC` `HSTAIR_SAMESHAPE` `HSTAIR_DIFFSHAPE`
* `HANDS` (양손 상호작용 — 협응/독립/역할분리, DP 전용)

API 는 개수를 하드코딩하지 않고 매 요청 `_meta` 에서 조립한다. 목록이 늘어날 수 있으니 응답에 실제로 온 키를 신뢰한다.

### 5.4 `getSong?features=full` → chart 의 `features` 블록

| 필드 | 의미 |
|---|---|
| `source_universe_count` | 곡 피처 universe 크기(현재 **105**). |
| `sparse` | `true`. **모든 곡이 105축을 다 갖지 않는다.** |
| `available_count` | 이 채보가 실제 가진 축 수(대략 60~90). |
| `pattern_percentiles` | 축별 **전곡 대비 백분위 0~100**(높을수록 그 패턴이 강한 곡). **없는 키 = 그 채보에 사실상 그 패턴이 없음** — 0 으로 채우지 말고 "해당 없음" 으로 본다. |

곡 universe 105축은 사용자 37축을 **포함**한다(사용자 축은 곡 축의 부분집합). 그래서 키 이름은 항상 일치한다.

### 5.4a 곡의 physical 설명

* 기본 `physical.features`는 35축의 `mean_nps` 원문 숫자 또는 `null`; `features=full`만 각 축을 `{meanNps,notes,duration}`으로 확장한다. 기존 `chart.features`는 전곡 대비 백분위이므로 구분한다.
* 단위는 `HSTAIR_SYNC`·`HSTAIR_SAMESHAPE`·`HSTAIR_DIFFSHAPE`가 `notes/s/both-hands`, 나머지 축이 `notes/s/hand`다.
* `duration`은 축별 초 합계라 곡 전체 길이를 넘을 수 있다. `null`은 0이 아니다.
* 원문값을 반올림·재계산하지 말고, API에 없는 NPS·곡 길이·안정 실력선·성공 확률을 만들지 않는다.
* ID 없이 물리량만 설명한다. 병목·`gap=mean_nps-line`·top3는 유효 ID, 명시적 diff, 유일 chart가 모두 있을 때만 다룬다.
* `status`와 `reason`을 구분하고 `ready`의 숫자만 해석한다. 원문 필수 3필드와 선택 `line`·`mean`, env 5항목 검사를 통과한 데이터만 ready다.
* 기존 사용자 `line`·`max_by_lamp` 설명과 다른 Sol의 상대 평가 설명은 그대로 보존한다.

### 5.5 곡 feature universe 105축 (참고)

37축 외에 곡에만 있는 축(사용자 분석에는 안 쓰임): `SOF-LAN-ratio`, `SPIRAL_UP_L/R`·`SPIRAL_DN_L/R`(나선계단), `JUMP_WIDE_L/R`, `PHRASE_LOOP_L/R`·`PHRASE_LOOP_FAST_L/R`, `TRILL_K4_L/R`·`TRILL_K35_L/R`·`TRILL_K24_L/R`·`TRILL_SPEED`, `HANDS_LHAND/RHAND/SAME/DIFF/CROSS/INDEP/ROLE`, `STAIR_UP`·`STAIR_DN`·`DOUBLE_STAIR`·`KEIMA`·`SPIRAL_UP`·`SPIRAL_DN`·`JUMP_WIDE`(combined), `HSTAIR_SYM`·`HSTAIR_ASYM`, `JACK_SPEED_L/R`·`AXIS_SPEED_L/R`·`STREAM_SPEED_L/R`·`SPEED_MIX_L/R`·`SCR_ROLL_SPEED_L/R`, `MISFINGER_*`, `PEAK_CHORD_SIZE_L/R`, `CN_SOLO/CHORD/MIX/REPEAT/SHAPE/HOLD_L/R`, `HARD_TRILL_L/R`(무리트릴). 이 축들은 곡 설명에는 써도 되지만 유저↔곡 직접 대조에는 쓰지 않는다(유저 쪽에 대응 축이 없다).

---

## 6. `report` 의 σ vs absolute feature score

* **`report`(그리고 persona)의 +/- 숫자 = 본인 평균 대비 표준편차(σ).** "이 사람 안에서" 상대적으로 강한/약한 패턴. `+2.0` = 뚜렷한 강점, `-2.0` = 뚜렷한 약점. **절대 실력이 아니다.**
* **`features.scores` = 절대 피처 스코어.** 다른 플레이어와 비교했을 때의 성과 수준.
* 피처별 상대 강약(σ)의 **정본은 `report` 하나뿐이다.** API 는 구조화된 피처별 σ 를 따로 제공하지 않는다.
* **서로 다른 계정의 σ를 직접 비교하지 않는다.** σ는 각자의 평균을 기준으로 한 상대값이다. 계정 간 성과 비교는 제공된 절대 피처 점수·표시 ★·r★를 각각의 척도 안에서 하며, 절대점수를 사용자 백분위나 순위로 바꾸지 않는다.
* **`features.scores` 를 `max_score_by_feat` 로 나눈 값을 σ 나 "실력 %" 라고 부르지 마라.** 그건 이론 최대 대비 비율일 뿐, `report` 의 σ 와 다른 통계다. 잔차 σ 강약을 말할 땐 `report` 를 인용한다.
* **σ 숫자를 그대로 나열하지 않는다.** "+2.0σ 강점" 처럼 수치를 답변 전면에 내세우지 말고, 방향(강점/약점)과 실제 근거(추천 곡·백분위·최근 성과)로 설명의 무게를 옮긴다. σ는 "왜 이 패턴을 짚었나"의 배경 근거로만 짧게 곁들인다.

### 6.2 `relative_evaluation` — 웹 Analysis 상대평가

* DP users-list 전량에서 10피처별 `rank`, `total`, `percentile=rank/total*100`을 계산한다. 상세의 상위 N%는 `percentile`; `display_value=100-percentile`, `delta_display_value`는 본인 10축 평균 대비 차이다. `delta_rank=mean_rank-rank`가 양수면 평균보다 높은 등수다.
* **strong은 `delta_rank>=0`** (평균 동률 포함). 이는 **「σ와 다른 통계이며 웹 Analysis 상대평가와 같은 값」**이다.
* 막대는 ±15등 스케일이며 평균선 이동, 상하경계, 0..100 clipping이 적용된다. `bar_height_percent`는 실력%가 아니다.
* 예: 「트릴은 전체 N명 중 R위이며 본인 10피처 평균 등수보다 D등 낮다」. 실제 도구 숫자만 인용하고, 상위 N% 순위와 본인 평균 대비 강약을 따로 설명한다.
* σ와 같다고 하거나 35축·좌우축으로 확장하지 않는다. max%·★대·새 백분위 산식은 만들지 않는다.
* `status=ready`만 수치로 말한다. `missing`·`invalid`는 정보 없음이지 0이 아니며 `reason`을 확인한다. `absolute`/잔차 결손으로 상대평가를 지우거나 서로 대체하지 않는다.
* R2 etag/uploaded_at과 `user_dump_revision`은 입력 출처 정보다. 자동 실력 갱신·활동·성장 신호로 해석하지 않는다. 독립 갱신 또는 cache 차이가 있으면 같은 시점이라 단정하지 않는다.

### `max_score_by_feat` 해석 주의

* 이건 "정규화용 상수" 이지 목표치가 아니다. `scores[k] / max_score_by_feat[k]` 는 축 간 대소를 비교할 때만 참고하고, 그 비율 자체를 유저에게 "당신은 이 패턴을 X% 한다" 처럼 제시하지 않는다.

---

### 6.1 `skill_evidence`의 두 계층

`getProfile`·`getAnalysis`의 `skill_evidence`는 `absolute`(DBR 가중 클리어 기준선), `residual`(본인 평균 대비 잔차 σ)을 독립적으로 제공한다. 한 계층이 없다고 다른 계층까지 없는 것으로 보거나 서로 대체하지 않는다. 각 계층의 `status`·`reason`·`stale`·버전·생성 시점을 먼저 확인한다. `missing`·`invalid`·`version_mismatch`는 사용할 수 없음이며 0이 아니다. `stale`은 마지막 성공본의 오래된 근거로만 명시하고 현재 실력·성장·병목을 확정하지 않는다.

#### absolute — DBR 가중 클리어 기준선

`purpose:clear`인 응답만 사용한다. `model_version`/`line_version`으로 피처 계약을 판별하며 v2는 `phys-line-v2`, 평균 피처 버전은 `mean-os-pattern-span-v2`다. `q_version:q-samehand-2s-v1`과 `time_axis_version:ta-20261004`도 응답에서 확인한다. v1의 10축 자산과 계산 설명은 v1 데이터에만 적용하며 v2에 혼합하지 않는다.

v2 `line`은 축별 **클리어율 50%에 해당하는 평균 NPS**다. 난이도 위치는 램프별 `weight`로 clear rate 50%를 보간해 정하며, 평균 NPS에 가중치를 곱한 값이 아니다. `level=round(meanNps)`이며, `features` 값은 `{meanNps, duration, notes}`만 갖는다. null이면 실제 `reason`을 말하고 숫자를 만들지 않는다.

v2 집계에는 FAILED 기록을 포함하고 NO PLAY는 제외한다. 축별 cleared 차트가 6개 미만이면 `line:null`, `reason:insufficient_clears`다. v2에는 `stable_line`, `stable_gap`, `line85` 및 85% fallback이 없다. v1의 stable/85 설명과 자산은 v1에 한해 보존한다.

v2 `max_by_lamp`는 `{ easy, hard, exhard, fc }`이며 각 값은 `{mean_nps, chartKey, lamp}` 또는 null이다. 차트당 최고 램프 하나를 기준으로 **정확히 그 램프로 깬 채보만** 본다: easy는 EASY·NORMAL(`lampNum` 3·4), hard는 HARD(5)만, exhard는 EX-HARD(6)만, fc는 FULL COMBO(7)만이며 그중 해당 축 meanNps 최댓값이다. 위 램프로 깬 곡은 아래 램프 칸에 들어가지 않으므로 이지 최대가 하드 최대보다 낮을 수 있다. 목표 최대≤아래 램프 최대일 때만 설명용 구간을 제시한다. 역전·동일·결손이면 구간이 없고 정렬·게이트에 쓰지 않는다. 목표 이상 ceiling은 목표 및 상위 램프 칸의 유한 최대로 exact 최대와 구별한다. 동률은 chartKey 오름차순으로 선택한다. 반올림하거나 램프 가중치를 곱하지 않는다. null이면 해당 램프 기록 없음이다. 표본이 적어 `line`이 null이어도 최대는 있을 수 있다. 축별로 「50% 실력선 X / 최대: 이지 A(곡) · 하드 B · 익하 C · 풀콤 D」를 함께 말한다. 최대는 한 번 깬 최고치일 뿐 안정 실력이 아니다. 채보명은 조회 근거가 있을 때만 쓰며 null을 0으로 대체하지 않는다.

v2는 35축을 반환한다: NOTES, CHORD, PEAK, CHARGE, SCRATCH, PHRASE, JACK, TRILL, RAND, STAIR_UP_L/R, STAIR_DN_L/R, K1~K7의 _L/_R, DOUBLE_STAIR_L/R, KEIMA_L/R, HSTAIR_ONEHAND, HSTAIR_SYNC, HSTAIR_SAMESHAPE, HSTAIR_DIFFSHAPE (_L/_R = 1P/2P 측 손). HANDS·SOF-LAN 은 축이 아니다. 동시치기 축(CHORD·DOUBLE_STAIR·KEIMA 등)은 동작 한 번에 노트 2개 이상을 세므로 같은 손 속도에서도 수치가 높다. 단위는 `HSTAIR_SYNC`, `HSTAIR_SAMESHAPE`, `HSTAIR_DIFFSHAPE`만 `notes/s/both-hands`; 나머지 32축은 `notes/s/hand`다. 서로 다른 단위 축을 직접 서열 비교하지 않는다.

`arrange_assumed`와 `provenance` 등 근거 정보를 보존한다. CN·BSS의 hold 판정과 시간 창 해석은 해당 버전의 원천·진단 정보를 따른다. v1 CN 해석을 v2 계약에 옮기지 않는다.

#### residual — 기존 잔차 σ

`residual.report`·`tags`·`one_liner`는 기존 persona 근거다. 본인 평균 대비 강약은 `getAnalysis.report`의 현행 서술을 사용하고, **서로 다른 계정의 σ를 직접 비교하지 않는다.** API가 주지 않은 수치를 sigma라고 부르거나 서술에서 수치를 추출해 새 σ를 만들지 않는다. σ 숫자 나열 대신 강점·약점 방향과 실제 근거를 설명한다.

## 7. 세부 피처 예시 — KEIMA / DOUBLE_STAIR / HSTAIR

* **`KEIMA_L` / `KEIMA_R`** — 계마(桂馬): 건반을 건너뛰며 손을 옮기는 배치(1→3→5). 좌/우 손 각각. 희소 축이라 유저·곡 모두 표본이 얕을 수 있다(값이 낮거나 `missing` 이면 과신 금지).
* **`DOUBLE_STAIR_L` / `DOUBLE_STAIR_R`** — 겹계단: 양손 계단이 겹쳐 들어오는 배치. 좌/우.
* **HSTAIR(양손계단)** 4축:
  * `HSTAIR_ONEHAND` — 한 손에 계단이 몰림
  * `HSTAIR_SYNC` — 양손이 동시에 계단
  * `HSTAIR_SAMESHAPE` — 좌우가 같은 모양
  * `HSTAIR_DIFFSHAPE` — 좌우가 다른 모양
* **`STAIR_UP_L/R` · `STAIR_DN_L/R`** — 상행/하행 계단, 좌/우.
* **`K1_L`…`K7_R`** — 1~7번 건반별 국소 밀도, 좌/우. "N번 키가 약하다" 를 이걸로 본다.

### user ↔ song 비교 방법 (예시)

1. `getAnalysis` 기본 응답에서 사용자의 약한 축을 찾는다 — **`report` 의 σ 서술**로 "왼손 계단이 약함", `features.scores` 로 해당 축 절대값이 낮음 등. (내부 조회 키: `STAIR_DN_L`)
2. `getSong features=full` 로 곡의 `pattern_percentiles` 에서 같은 키를 본다 — 해당 축이 85(상위)면 그 곡은 왼손 하행계단 비중이 크다.
3. 결합 해석(사용자에게 하는 말): "왼손 하행계단이 상대적으로 약한 편인데, 이 곡은 왼손 하행계단 구간 비중이 커서 특히 무너지기 쉽다." — **원문 키(`STAIR_DN_L` 등 대문자 영문)는 답변에 그대로 쓰지 않는다.** 도구 호출·내부 조회에만 키를 쓰고, 사용자에게는 항상 §7.1 한글 대응표의 표현으로 번역해 말한다.
4. **숫자를 직접 빼거나 나누지 않는다.** user `scores`(절대) 와 song `pattern_percentiles`(0~100 백분위) 는 척도가 다르다.
5. 곡에 그 키가 없으면(`sparse`) "그 패턴은 이 곡에 거의 없음" 으로 본다 — 0 이 아니다.

### 7.1 canonical feature key → 한글 대응표 (답변용 필수 번역)

사용자에게 하는 모든 답변에서 대문자 영문 feature key는 이 표(또는 §13 대표10)의 한글 표현으로 바꿔 말한다. 대표↔세부 관계와 손 지정 가능 여부는 `glossary-knowledge.md`의 `pattern_taxonomy` 계약을 함께 참고한다.

| key | 한글 표현 |
|---|---|
| `STAIR_UP_L` / `STAIR_UP_R` | 왼손/오른손 상행계단 |
| `STAIR_DN_L` / `STAIR_DN_R` | 왼손/오른손 하행계단 |
| `DOUBLE_STAIR_L` / `_R` | 왼손/오른손 겹계단 |
| `KEIMA_L` / `KEIMA_R` | 왼손/오른손 계마 |
| `K1_L`~`K7_R` | N번 건반 좌/우 밀도 |
| `HSTAIR_ONEHAND` | 양손계단 한손몰림 |
| `HSTAIR_SYNC` | 양손계단 동시타 |
| `HSTAIR_SAMESHAPE` | 양손계단 같은모양 |
| `HSTAIR_DIFFSHAPE` | 양손계단 다른모양 |
| `HANDS` | 양손 상호작용(협응/독립/역할분리) |

곡 전용 105축(§5.5)도 같은 원칙 — 원문 키를 답변에 노출하지 말고 뜻으로 풀어 말한다(예: `SPIRAL_UP_L` → "왼손 나선계단").

### 곡의 막대 요약과 패턴 구간 조회

`getSong(features=full,diff=...)`으로 곡의 전체 1초 막대와 35축 `patternAxes`를 확인하고, 궁금한 축만 `getSongPatterns(q,diff,axis[,iidxId])`로 모든 구간을 조회한다. `getSong`의 timeline은 `features=full`·명시적 `diff`·단일 DP 채보일 때만 제공되며 구간 목록은 포함하지 않는다. `getSongPatterns`는 `diff`와 단일 `axis`가 필수이고 35축 모두 조회할 수 있으며 구간을 절단하지 않는다.

요약 `meanNps`는 구간 NPS의 산술평균이 아니라 `Σnotes/Σduration`이다. ID가 있으면 축별 `line`과 `aboveLine`(원값 NPS가 line을 초과한 구간 수)을 볼 수 있다. 구간의 `notes`는 tap·holdStart·scratch를 세고 holdEnd는 제외하므로 막대의 notes 계수와 다를 수 있다. 구간 `nps`는 반올림 전 원값으로 해당 support 전체에서 계산하며 `start`/`end`는 소수 둘째 자리, `nps`/`gap`은 첫째 자리로 출력한다. `gap`은 유저 축의 line과 해당 구간 NPS의 차이이지 클리어 확률이나 정확한 실패 지점이 아니다. ID 비교가 `null`이거나 stale이면 그 상태를 그대로 알린다. 이 값은 축별 `notes/s/hand` 또는 `notes/s/both-hands` 단위이며 onset/s와 혼용하지 않는다.

---

이 패턴·타임라인 응답의 `textage_song_id`는 Textage ID이고 `zasa`는 해당 DP 차트에 조회 가능한 체감값이다. 둘 다 미확인일 수 있어 `null`을 0이나 곡 식별 성공으로 바꾸지 않는다. `getSong`의 최상위·`charts`·`candidates` 식별자와 같은 Textage ID 체계이며 게임/웹 `song_id`와 혼동하지 않는다. SP 차트에는 DP zasa 대응값이 없다.

## 8. 추천 `explanation` — `recommendSongs?explain=full`

각 추천 row 에 붙는 필드. 추천 엔진이 실제로 계산한 값이며, GPT 가 이유를 지어내지 않도록 근거를 제공한다.

| 필드 | 의미 |
|---|---|
| `reason` | `weakness_training`(약점 연습) / `clear_progression`(클리어 진행) / `skill_stabilization`(실력 다지기). |
| `requested_feature` | 사용자가 지정한 연습 피처(없으면 `null`). |
| `hand_mode` | `both` / `left` / `right`. |
| `match_features` | **엔진이 이 곡을 고를 때 매칭한 세부 약점 축 목록.** practice 에서 대표 피처를 요청하면 그 하위 세부축들이 여기 나온다(예: `TRILL` → `TRILL_K4_L`, `TRILL_K35_R`, `PHRASE_LOOP_L` …). clear/ladder 는 비어 있을 수 있다(코어가 세부축을 붙이지 않음) — 그때는 `reason` 과 `category` 로만 설명한다. |
| `weakness_match` | 이 곡이 **요청 후보 풀 안에서** 사용자 약점과 얼마나 맞는지(0~1 상대 점수). 내부 추천식을 재현하는 값이 아니라 "왜 상위에 왔나" 를 보여주는 관측값이다. |
| `practice_type` | `review` 등 연습 유형. |
| `category` | `weakness` / `cleanup` 등. |
| `feature_tags` | 이 곡의 두드러진 패턴 태그(한글). |

`row` 최상위의 `hashtags` · `feature_tags` · `category` · `clear_type` 도 함께 근거로 쓴다.

추천 행은 웹 곡 `song_id`와 Textage `textage_song_id`를 함께 제공할 수 있으며, 신규 식별자를 기존 곡 필드 대신 사용하지 않는다. 추천 row의 `zasa`는 기존 값이 그대로 유지되고, 원래 값이 없던 행에만 추가될 수 있다. `max_clear_evidence`에도 두 ID와 `zasa`가 올 수 있다. `getPlays` 행의 `game_level`은 게임 표기 정수 레벨이고 `textage_song_id`는 Textage ID다. `null`은 자료/매칭 결손이며 0이 아니다.

`skill_evidence.top_charts`와 `max_by_lamp`의 곡 근거에 포함되는 `textage_song_id`·`zasa`는 보조 식별·난이도 정보다. `textage_song_id`가 null이면 Textage 곡 매칭이 확인되지 않은 것이고 `zasa`가 null이면 해당 DP rating 값을 확인하지 못한 것이다. `game_level`·`zasa` 모두 SP 난이도 추정치로 읽지 않는다.

### 8.1 개인 약점 매칭 서술 비중

`weakness_match`·`match_features`는 이 추천이 **왜 상위에 왔는지**를 보여주는 관측값이지, 그 자체가 답변의 중심 문장이 되어서는 안 된다. practice/growth 추천을 말할 때는 ① 소화 대역·진행 단계(§11, §8A) 를 먼저 말하고, ② 개인 약점 매칭은 "그리고 이 축도 보완할 수 있다" 정도의 보조 문장으로 짧게만 곁들인다. `weakness_match` 수치나 σ 를 근거의 주어로 앞세우지 않는다.

---

## 8A. 성장 랜드스케이프 — `recommendSongs kind=ladder mode=lamp|score`

`mode=lamp` 는 클리어 ★ 축, `mode=score` 는 유저 r★ 축(내부척도 `[-2,10]`)이다. `mode` 가 없으면 레거시 `preset` 사다리다. 성장 랜드스케이프는 `solid`(실력다지기) / `aspiration`(목표①) / `aspiration2`(목표②) 3섹션이다. 실력다지기|목표① 경계는 사용자 base, 목표①|목표② 경계는 최대클리어 관측값(램프는 EC 달성 곡, 스코어는 AA 달성 곡)이다.

### 섹션 필드

| 필드 | 의미 |
|---|---|
| `key` | `solid` / `aspiration` / `aspiration2`. |
| `label` | `다지기` / `목표①` / `목표②` 표시명. |
| `is_goal` | 목표 섹션 여부. **목표는 이 값이 `true` 인 섹션에서만 설명한다.** |
| `validated` | 세 섹션 모두 `false`. 어느 섹션도 성장 효과가 검증되지 않았다. |
| `confidence` | `solid` 는 `null`(해당 없음), 목표①·②는 `'low'` 다. |
| `basis` | `solid` 는 `observed_current_ability`(이미 도달한 실력권의 현재 상태 서술), 목표①·②는 `projected_unvalidated`(미검증 투사)다. |
| `candidate_sufficiency` | `solid` 만 제공. 요청한 후보 수 대비 실제 반환 가능한 후보의 충족도인 관측값이다. 신뢰도가 아니다. |
| `target` | 해당 섹션 추천곡이 실제로 닿는 관측 지점. 목표①\|목표② 경계 원값으로 해석하지 마라. |
| `range` | 섹션이 반환한 주축 범위. `null` 일 수 있다. |
| `boundary` | **목표①\|목표② 를 가르는 최대클리어 관측 경계.** 두 목표 섹션에 같은 값이 실린다. `target`(그 섹션이 실제로 닿는 지점)과 다른 값이니 섞지 마라. `solid` 는 `null`. |
| `max_clear_axis` (최상위) | `boundary` 와 같은 값. 유저가 **실제로 달성한 곡**에서 관측한다 — 램프 축은 EC 달성 곡, 스코어 축은 AA 달성 곡 기준이다. HC/EXH·AAA/MAX- 보유는 이 경계를 올리지 않는다. |
| `max_clear_evidence` (최상위) | 그 경계가 나온 근거 곡 `{ title, diff, stage, axisVal }`. "왜 여기가 경계냐"는 질문에 이 곡을 근거로 답한다. |
| `short` | 적격 추천곡 부족 등으로 섹션이 짧은지 나타내는 불리언. |

### row `growth` 필드

| 필드 | 의미 |
|---|---|
| `placement_stage` | 지금 연습할 배치 지점. 특히 실력다지기에서는 **목표가 아니다**. |
| `goal_stage` | 목표 섹션의 목표 단계. **`is_goal:true` 섹션의 이 값으로만 목표를 설명한다.** |
| `current_stage` | 실제 달성 단계. |
| `target_stage` | 이 곡에서 노리는 단계. `target_star`·`margin` 은 **이 단계 기준**으로 계산된다. |
| `validated` | 항상 `false`. 성장 효과가 검증되지 않았다는 표시다. |
| `play_state` | `FRESH`(기록 없음) / `PLAYED_NO_STAGE`(기록은 있으나 단계 미달성) / `ACHIEVED_STAGE`(단계 달성). |

**위 6개가 `growth` 의 전부다.** `expected_stage`·`next_stage`·`growth_reason`·`played`·`discrete_residual`·`discrete_stratum`·`raw_margin`·`effective_margin`·`physical`·`cluster` 는 엔진 진단용이라 **응답에 오지 않는다** — 없는 필드를 찾거나 지어내지 마라.

`mode=score` row 에는 클리어 축 값(`target_star`·`margin`)이 실리지 않는다. 점수 목표의 거리는 **곡 등급 r★(`r_star.a/aa/aaa/maxm`)와 플레이어 r★ 의 차이**로 말하고 r★ 절대값은 노출하지 않는다.

세 섹션 모두 성장 효과가 검증되지 않았다. `solid` 는 이미 도달한 실력권에 대한 현재 상태 서술이지 예측이나 **검증된 구간**이 아니다. 목표①·②는 관측 경계에 따른 거리·성격 구분일 뿐 성장 예측이 아니며 **"이 곡을 하면 는다"는 보장처럼 말하지 마라.** r★ 절대값은 사용자에게 노출하지 않으며, `A/AA/AAA/MAX-` 는 관측 라벨이지 사용자 폴더가 아니다.

---

## 9. `layout_explanation` — `layout=on` + `explain=full`

8배치(정배치 / FLIP / 좌·우 MIRROR 조합) 평가의 **원값**. `_matchByHand` 가 없는 row 는 `null`.

| 필드 | 의미 |
|---|---|
| `compared_layouts` | 평가한 배치 수(보통 8). |
| `base` | 정배치 baseline: `left_match` / `right_match` / `total_match` / `hand_penalty` / `hstair_penalty`. |
| `selected` | 엔진이 고른 배치(`layout` 라벨 포함)와 그 점수들. |
| `delta_from_base` | 선택 배치 − 정배치. **양수 match delta = 해당 손/전체 적합도 개선**, **음수 penalty delta = 벌점 감소**. |

해석 규칙:

* `left_match` / `right_match` = 그 손이 잡는 채보와 사용자 손 강도의 매치. `hand_penalty` = 손별 무리 운지 벌점(penL+penR). `hstair_penalty` = 쌍(양손) 비대칭계단 벌점.
* 이 내부 점수는 **★/r★/곡 백분위가 아니다.** 스케일이 불투명하므로 "이 배치가 몇 점 더 좋다" 를 절대 수치로 말하지 말고, "정배치 대비 오른손 적합도가 오르고 무리 벌점이 줄어 이 배치가 선택됐다" 처럼 방향으로만 설명한다.
* `layout` 라벨 표기: `정배치`(옵션 불필요) / `F`(FLIP) / `M/-`(왼쪽만 MIRROR) / `-/M`(오른쪽만 MIRROR) / `M/M`(양쪽) / `F M/-`(조합).

---

## 10. `series` / `in_ac` / `in_inf`

`getSong` 과 `recommendSongs` 결과에 붙는다.

* `series` = 곡이 **처음 수록된 IIDX 버전**(예 "EPOLIS", "Rootage", "INFINITAS"). `series_no` = 그 정수 코드. 최신 리믹스여도 원곡 데뷔 버전이 나온다.
* `in_ac` = 그 채보가 **현행 아케이드**(가정용 X)에 수록돼 있는가.
* `in_inf` = **INFINITAS** 수록 여부.
* 추천곡은 유저 플랫폼(아케이드 유저 = ID 숫자 시작 / INFINITAS 유저 = ID 영문 시작)에 맞춰 이미 필터된다 — "지금 아케이드에 있나", "몇 작품 곡" 질문에 이 필드로 답한다.

곡 식별에 쓰는 Textage `textage_song_id`와 게임/웹 곡 `song_id`는 별도 ID다. `getSong`은 `textage_id=...`를 우선 조회 키로 사용한다. 이 인수를 주면 `q`(곡명)는 동시에 주어져도 무시되므로 다른 곡을 좁히는 보조 조건으로 해석하지 않는다. ID를 모르면 `q`로 찾고 응답의 식별자를 확인한다.

---

### 10.1 `getShelf`의 집계 범위

`by_level`의 분모는 **rating에 zasa가 있는 DP11/12 채보 중 사용자 AC/INF에 수록된 채보**다. 웹 Stats의 해당 DP11/12 분모를 기준으로 하며, 모든 게임레벨·모든 채보를 포함하는 ALL 통계가 아니다.

* 일반 채보는 곡 마스터의 `ac` 비트, LEGGENDARIA는 `legen` 비트로 사용자 플랫폼 수록 여부를 판정한다. 곡명 매칭이 안 되는 rating 행은 제외한다. 수록 후보가 없다고 전곡으로 되돌리지 않는다.
* `skill_line.*.hardest_cleared`와 `easiest_uncleared`도 이 범위 안의 최고 클리어·최저 미클리어다. 사용자의 모든 기록 중 전역 최고·최저라고 확대 해석하지 않는다.
* 분모의 포함 조건은 rating의 zasa 보유 여부지만, 응답의 곡 zasa값은 기존 코치 정책인 **zasa-data 우선, rating zasa fallback**이다. 웹과 모든 표시 숫자가 동일하다고 단정하지 않는다.

`bands`는 Grid의 **정확한 zasa 값**별 그룹이다. `band=11.2`는 11.2만 선택하며 정수 floor나 고정 폭 대역이 아니다. `zasaMin`/`zasaMax`는 양 끝 포함 범위이고 `band`와 함께 주면 교집합이다. 정수 placeholder는 기존 rating 보정을 따른다.

각 band의 `total`은 NP 포함 수록 전체 채보 수이며 `played`와 다르다. `achievement.ec/hc/exh/fc/a/aa/aaa`의 `denominator`도 이 total이다. `rate=achieved/total`, total=0이면 null이며 `unknown`은 기준별 미확인 수다. EC≥3, HC≥5, EXH≥6, FC≥7은 달성 임계이고 exact `max_by_lamp` 칸과 다르다. A/AA/AAA는 기록 등급 우선이며 EX/notes 결손을 0점으로 만들지 않는다.

선택 결과는 안정 정렬 후 `limit`(기본 100, 최대 400)·`offset`(기본 0)으로 `rows`를 페이지화한다. `pagination.total`은 선택된 전체 채보 수, `returned`는 반환 행 수, `has_more`는 다음 페이지 여부다. 마지막 밖 offset은 빈 rows와 기존 total을 유지한다. 전체를 설명하려면 페이지를 끝까지 조회한다. NP의 grade/bp와 식별 불가 song_id는 null이며 bp=0은 실제 0이다.

`rows`와 `skill_line`의 곡 식별자는 가능한 경우 웹 곡 마스터의 `song_id`와 `textage_song_id`를 함께 제공한다. `song_id`는 웹/덤프의 곡 ID, `textage_song_id`는 Textage의 곡 ID이며 서로 다른 ID 체계다. 어느 쪽도 다른 쪽으로 치환하지 않는다. `skill_line.*.hardest_cleared`와 `easiest_uncleared`의 대표 곡에도 같은 식별자를 제공한다. 식별할 수 없으면 `null`이며 제목만으로 ID를 만들어내지 않는다.

`game_level`은 SP·DP 모두 각 차트에 대해 게임이 표시하는 정수 레벨이다. `getPlays` 행의 값도 해당 SP 또는 DP 채보의 게임 표기 레벨이다. `zasa`는 DP 전용 오소리 체감 세분값이며, SP 판에는 대응값이 없어 `null`이다. `null`은 해당 값을 확인할 수 없다는 뜻이지 0이나 미플레이가 아니다. SP zasa를 추정하거나 DP 값을 빌려오지 않는다.

`getPlays`·`getScores`·`getRecent`·`getShelf`·`recommendSongs`·`getProfile`/`getAnalysis` 근거 곡 등 응답에 `textage_song_id`가 있으면, 그 곡을 더 볼 때 `getSong(textage_id=<그 값>)`으로 조회한다(곡명 `q`보다 정확). `null`이면 곡명 `q`로 찾는다. `getSong`은 DP 곡 정보라 SP 판은 상세가 없을 수 있다.

### 10.2 `getGradeTargets`의 후보 범위

웹 PlayData처럼 곡의 `ac` 수록 비트, LEG의 `legen` 비트, AC 사용자의 INFINITAS 시리즈(`series_no=98`) 제외를 적용한다. AC와 다른 채보인 INF 변종은 공용 변종 목록으로 제외하며 AC의 요구 r★를 빌려 목표를 만들지 않는다.

현재 성적은 `song_id`와 난이도로 매칭한다. 같은 제목이라도 다른 ID의 성적·달성 등급을 섞지 않는다. 반환된 `song_id`를 보존하고 다른 플랫폼·동명 채보로 바꿔 추천하지 않는다.

목표 등급을 이미 달성한 곡은 제외한다. AA/AAA/MAX− 목표에는 직전 등급에 도달한 곡만 포함하며 미플레이 곡은 이 조건을 통과하지 못한다. A 목표는 직전 등급 조건이 없다. MAX− 추정값 여부는 `estimated`로 구분한다.

`candidates`는 필터를 통과한 전체 후보 수이며 `rows`는 그중 최대 limit개다. 코치는 가까운 순 상위 목록, 웹은 가까운 후보 중 무작위 일부 선정이므로 화면의 곡 목록이 반드시 같지는 않다. `service-status`의 채보별 미수록 게이트는 이번 범위에 포함되지 않았다.

### 10.3 실제 성적 조회는 별도

`getScores`/`getRecent`는 사용자 실제 기록이므로 위 후보 필터로 지우지 않는다. `getSong`도 사용자 플랫폼으로 조회 자체를 막지 않고 `in_ac`/`in_inf` 정보를 제공한다. 조회 가능하다는 사실과 현재 플랫폼에서 추천 가능한지는 구분한다.

## 11. 소화 대역 앵커 (추천의 기준)

추천은 "겨우 깬 최고 난이도" 가 아니라 **안정적으로 소화 중인 대역**에 맞춘다.

* **소화 대역** = 최근에 실제로 HARD/EX-HARD 를 AA 이상 점수로 붙이고 있는 `zasa` 대.
* 재료: `getRecent`(요즘 치는 곡의 zasa·램프·점수), `getShelf.skill_line.hc.hardest_cleared` / `exh.hardest_cleared`(HARD·EX하드로 깬 가장 어려운 곡의 zasa — 이 언저리가 상한), `base_star`(클리어 실력 ★).
* 최고 클리어 한두 곡만 보고 대역을 올리지 않는다. 반복적으로 안정적인 성과가 나오는 구간을 더 중시한다.
* `zasaMin`/`zasaMax` 는 소화 대역 ±0.3 으로 좁게. 대역보다 별 3~4개 위인 곡은 일반 연습곡으로 추천하지 않는다.
* 추천 row 의 `margin`(= `base_star` − 필요 실력)이 크게 음수면 "지금은 무리, 목표로만" 이라고 구분한다.

---

### 11.1 웹과 코치 추천이 일치하는 부분과 남은 차이

* 기준 별값은 웹의 `recBaseStarOf` 규칙을 사용한다. clear/practice/growth에 v2 점수식을 전달하고 HC/EXH는 기존 BP 반영 함수를 사용한다. score growth의 기준은 별도로 사용자 r★다.
* 약점 계산에는 곡 피처와 덤프의 최근 갱신 이력을 전달한다. 구형 덤프에 이력이 없으면 코치는 DB 조회로 보충하지 않으므로 최근 활동 가점이 없을 수 있다. **입력 결측을 활동이 없었다는 뜻으로 해석하지 않는다.**
* 코치는 결정적 추출, 웹은 무작위 재선정이다. API의 levelMode·strength·flipOn·BPM 기본값과 11/12 축약 데이터 범위도 웹 기본 화면과 차이가 남아 있다. 같은 계산 경로를 쓴다는 이유만으로 기본 추천 목록의 완전 일치를 보장하지 않는다.
* 추천은 실제 API 결과와 `explain=full`의 근거로 설명한다. 웹에서 보았던 목록을 맞추려고 기준값이나 계산식을 임의로 바꾸지 않는다.

### 11.2 INF 실측 노트 수와 점수 계산

`getScores`, `getGradeTargets`, 추천 엔진의 사용자 성적 입력은 **INF 기록(`played_version === 0`)에 유효한 양수 `note_count`가 있으면 실측값을 우선**한다. AC·버전 결측·실측 결측/0/음수 등은 기존 Textage 노트 수로 계산한다. ID가 INF처럼 보인다는 이유만으로 행의 버전 정보를 대신 판단하지 않는다.

* EX점수는 그대로이며 점수율의 분모가 바뀐다. 예를 들어 EX 1600점에 실측 1000노트면 80%, Textage 1050노트로 계산하면 약 76.19%로 AA 달성 여부가 달라진다.
* `getRecent`는 hist의 해당 날짜에 저장된 실측값을 우선하는 기존 경로다. 현재 집계 기록의 노트 수·점수로 과거 행을 메우지 않는다.
* 사용자 기록이 없는 `getSong.note_count`는 곡 메타 값이다. 이를 가져와 API가 반환한 사용자 점수율·등급·목표 판정을 다시 계산해 덮어쓰지 않는다.
* 추천 입력의 보정은 현재 점수율·DJ 등급·목표 EX 계산에 사용되고, targets의 달성/미달 판정에도 적용된다. 원본 EX점수나 DB 성적을 수정한 것이 아니다. 실측값이 없는 채보까지 AC/INF 노트 차이를 모두 해결했다고 말하지 않는다.

### 11.3 getPlays — INF 원본 옵션 해석

`getPlays`는 INF 기록기의 원본 행을 보존해 반환한다. 신규 행은 22개 string 필드이며, 기존 19열·21열 행도 함께 올 수 있다. 기존 19열 순서 뒤에 `app_version`, `game_version`, `play_speed` 순서로 추가된다. 기존 19/21열 행에는 `play_speed`가 없거나 빈 문자열일 수 있다. `source`의 원본 값은 `playdata`와 `currentsong`이며, `currentsong`에는 배틀 또는 속도 조절 판의 복원 경로가 포함된다. 옵션 해석은 아래 표를 따른다.

**최근 플레이의 배속 표기**

- `getPlays`로 조회한 판을 답변에서 언급할 때 `play_speed`를 확인한다. 값이 `"1.00"`이면 등속이다.
- 비어 있지 않은 유효한 배율 값이 `"1.00"`이 아니면, 해당 판을 말하는 문장이나 표의 해당 행에 몇 배속인지 반드시 함께 밝힌다. 예: `play_speed: "0.70"`인 판은 「0.70배속」, `"1.05"`인 판은 「1.05배속」으로 표시한다. 배속 표시를 답변의 다른 곳에만 모아 해당 판과의 연결을 흐리지 않는다.
- 빈 문자열·필드 누락·해석할 수 없는 값은 「속도 미상」으로 표시한다. 등속이나 특정 배속으로 추정하지 않는다.
- 속도 조절 판은 게임이 베스트에 저장하지 않는 플레이이므로, 그 판의 점수를 베스트 갱신·점수 갱신이나 실력 근거로 사용하지 않는다. 플레이 사실과 해당 배속은 설명할 수 있다.

오류 행은 기존 규칙대로 진단 정보로 취급한다. 오류 행을 정상 플레이로 바꾸어 설명하지 않는다.

오류 행은 timestamp와 버전 두 필드를 제외한 `song_id`부터 `source`까지 18개 값이 같은 음수 정수 문자열인 행이다. 오류 timestamp는 기록기 발생 시각 또는 업로드 시각의 실제 ISO 시각이다. 버전은 실제 값만 쓰며 확보할 수 없으면 빈 문자열이다. 오류 행은 실제 플레이가 아니므로 판수, 점수, 옵션, 추세 계산에 사용하지 않는다. 원본 오류 행과 버전 값은 진단 목적으로 보존한다. Web 메타 필드 `game_level`, `textage_song_id`, `zasa`는 오류 행에서 `null`이다. `clear_lamp=-1`만으로 오류라고 판정하지 않는다.
| 순서 | 열 | 정의 |
|---:|---|---|
| 1 | `timestamp` | 결과 화면으로 넘어간 저장 시각, UTC ISO 표현. |
| 2 | `song_id` | 곡 ID, PlayData word 0. |
| 3 | `title` | 곡 목록에서 ID로 조회한 곡명. UTF-16LE이며 따옴표를 이스케이프한다. 이는 이 문서 파일의 저장 인코딩과 별개다. |
| 4 | `difficulty` | PlayData word 1을 `DIFF_NAMES`로 난이도 표기 (예: DPA). |
| 5 | `notes` | 해당 차트 총 노트 수. 일반 플레이는 곡 목록의 난이도별 노트 수, 배틀은 CurrentSong의 양쪽 합계(차트 × 2). |
| 6 | `ex_score` | EX 스코어, 2 × PGREAT + GREAT. 배틀 합산 값을 절반/2배로 보정하지 않는다. |
| 7 | `pgreat` | PGREAT 총합(P1 + P2), PlayData word 4. |
| 8 | `great` | GREAT 총합(P1 + P2), PlayData word 5. |
| 9 | `miss_count` | 미스 카운트, PlayData word 3. 다른 판정 필드와 동일하다고 추측하지 않는다. |
| 10 | `clear_lamp` | 램프 번호, PlayData word 6. 확인된 값은 1=FAILED, 3=E-CLEAR뿐이며 그 밖의 번호 의미는 미확인이다. 배틀 -1은 램프 미기록이며 FAILED가 아니다. |
| 11 | `dj_rate_pct` | `ex_score / (notes × 2) × 100`, 퍼센트·소수 둘째 자리. 배틀은 저장된 합산 EX와 notes 그대로 계산한다. |
| 12 | `dj_rank` | 레이트 기준 AAA(8/9), AA(7/9), A(6/9), B(5/9), C(4/9), D(3/9), E(2/9), F. |
| 13 | `judge_16` | judgeData 0..15의 공백 구분 16값 순서: 0=P1 PGREAT, 1=P1 GREAT, 2=P1 GOOD, 3=P1 BAD, 4=P1 POOR, 5=P2 PGREAT, 6=P2 GREAT, 7=P2 GOOD, 8=P2 BAD, 9=P2 POOR, 10=P1 콤보 브레이크, 11=P2 콤보 브레이크, 12=P1 FAST, 13=P2 FAST, 14=P1 SLOW, 15=P2 SLOW. |
| 14 | `settings_p1_11` | playSettings 원본 int32 11개, 공백 구분. 0 왼쪽 스타일, 1 게이지, 2 어시스트, 3 FLIP, 4 범위, 5 DP 오른쪽 스타일, 10 배틀(+0x28). 6~9 미사용이며, 특히 8은 이 빌드의 배틀 판정에 쓰지 않는다. DP 양쪽은 이 한 블록의 0·5를 본다. 값 이름은 아래 옵션 표 참조. |
| 15 | `settings_p2_11` | playSettings +0x48의 P2 쪽 같은 11값 구조. SP 2P 쪽 값이며 DP 오른쪽 옵션으로 오해하지 않는다. |
| 16 | `battle_flag` | playSettings +0x28. 배틀 ON=1, OFF=0. 배틀 판정은 이 열을 사용한다. |
| 17 | `gauge_p1_w77` | judgeData 77의 P1 게이지 원본 값. 의미·단위 미확정이며 확정된 종료 게이지 퍼센트로 단정하지 않는다. |
| 18 | `gauge_p2_w78` | judgeData 78의 P2 게이지 원본 값. 의미·단위 미확정. p2를 끝 게이지로 사용하는 것은 사용자 지정 기본값이며 화면 대조 미확인이다. |
| 19 | `source` | `playdata`=일반 플레이(PlayData), `currentsong`=배틀(CurrentSong + 판정 블록). |

`settings_p1_11`과 `settings_p2_11`은 공백으로 구분된 int32 값 11개다. 위치는 0부터 센다.

| 위치 | 의미 | 값 이름 |
|---|---|---|
| 0 | 왼쪽 레인 스타일 | 0 OFF, 1 RANDOM, 2 R-RANDOM, 3 S-RANDOM, 4 MIRROR, 5 SYNCHRONIZE RANDOM, 6 SYMMETRY RANDOM |
| 1 | 게이지 | 0 OFF(일반 NORMAL), 1 ASSIST EASY, 2 EASY, 3 HARD, 4 EX HARD |
| 2 | 어시스트 | 0 OFF, 1 AUTO SCRATCH, 2 5KEYS, 3 LEGACY NOTE, 4 KEY ASSIST, 5 ANY KEY |
| 3 | FLIP | 0 OFF, 1 FLIP |
| 4 | 범위 | 0 OFF, 1 SUDDEN+, 2 HIDDEN+, 3 SUD+ & HID+, 4 LIFT, 5 LIFT & SUD+ |
| 5 | 오른쪽 레인 스타일(DP) | 위치 0과 같은 0~6 값 이름 |
| 10 | 배틀(+0x28) | 0 OFF, 1 ON; `battle_flag`와 같은 값 |

위치 6~9는 기록기에서 해석하지 않는다. 특히 위치 8은 이 빌드에서 배틀 판정에 쓰지 않는다. DP 양쪽 옵션은 `settings_p1_11` 한 블록의 위치 0과 5에 있고, `settings_p2_11`은 SP 2P 쪽 블록이다. 배틀 여부는 `battle_flag`로 판단한다.

예를 들어 `1 1 1 0 5 1 0 0 0 0 1`은 양쪽 RANDOM, ASSIST EASY, AUTO SCRATCH, FLIP OFF, LIFT & SUD+, 배틀 ON이다. 위치 5가 0인 행은 한쪽만 RANDOM이다. `0 2 0 0 5 0 0 0 0 0 0`은 일반 DP EASY, 어시스트 OFF다.

`source=currentsong` 배틀 점수는 양쪽 EX와 노트를 합산하며 절반/2배 보정을 하지 않는다. `clear_lamp=-1`은 FAILED가 아니라 기록기에 값이 기록되지 않은 경우다. DBR 자격은 `battle_flag=1 AND p1[0]=1 AND p1[5]=1 AND p1[2]=1`이며 R-RANDOM/S-RANDOM은 제외한다.

`gauge_p1_w77`과 `gauge_p2_w78`는 원본 필드다. 화면 대조를 기다리는 동안 p2를 끝 게이지로 보는 것은 사용자 지정 기본값이다. 이 원본만으로 실측 확인이 끝났거나 배틀 `clear_lamp`의 의미가 확정됐다고 말하지 않는다.

## 12. 레벨·별값 용어 빠른 표

| 용어 | 뜻 |
|---|---|
| `game_level` | SP·DP 각 채보에 대해 게임이 표시하는 정수 레벨(1~12). `getPlays` 행의 값도 해당 채보 기준이며, `null`은 확인 자료 없음이다. 사용자가 말하는 "레벨/렙" 1순위. |
| `zasa` | DP 전용으로 같은 게임레벨 안을 소수점으로 세분한 오소리 체감 난이도(예 12.3). 추천/서열표 내부 축. **★ 아님.** SP 판에는 대응값이 없어 `null`이며 추정하지 않는다. |
| `star_estimate` (★) | 플레이어 클리어 실력. `est_ec/hc/exh` 공통축. |
| `r_star` (r★) | 플레이어 스코어 실력. |
| `est_ec` / `est_hc` / `est_exh` | 그 곡을 EASY / HARD / EX-HARD 클리어하는 데 필요한 실력 ★. |
| 추천 row `ec` / `hc` / `exh` | 위와 같음(그 램프 필요 실력 ★). |
| `target_star` | (targets) 그 등급 목표의 내부 r★. `r_star` 가 이 값에 가까울수록 곧 달성. |
| `base_star` | 웹과 같은 추천 기준 ★. native 우선, 표시 ★0.5 이상 2 미만은 표시값 우선. |
| `score_rate` | EX SCORE 비율 % = `ex_score / (note_count*2) * 100`. A=66.7 / AA=77.8 / AAA=88.9 / MAX−=94.4. |
| `score_offset` | 곡 단위로 점수 별값이 클리어 별값보다 얼마나 높/낮은지. 양수면 그 곡은 점수가 잘 나오는 편. |

`ec/hc/exh`(클리어 축)와 `r_star.*`(스코어 축)는 **다른 지표**다. 혼동 금지.

---

## 13. 10대 패턴 (대표 피처)

| 키 | 뜻 |
|---|---|
| `NOTES` | 밀도 — 전체 노트 밀도. 곡 길이 지구력과는 별개. |
| `CHORD` | 동치 — 여러 버튼 동시 화음. |
| `PEAK` | 순간밀도 — 순간적으로 노트가 폭발하는 구간. |
| `CHARGE` | 차지 — 롱노트(CN)·백스핀스크(BSS) 등 누르고 있는 노트. |
| `SCRATCH` | 스크래치 — 턴테이블. |
| `SOF-LAN` | 소프란 — 곡 중 BPM 변화(변속). |
| `PHRASE` | 계단 — 인접 버튼이 연속으로 이어지는 배치. |
| `JACK` | 연타(잭) — 같은 버튼 빠른 반복. |
| `TRILL` | 트릴 — 두 버튼 번갈아. |
| `RAND` | 난타 — 규칙 없이 흩어진 불규칙 배치. |
| `HANDS` | 양손 상호작용 — 좌우 손 협응/독립/역할분리(DP 전용 대표 피처). |

각 대표 피처에는 세부축이 있고, `recommendSongs kind=practice` 의 `feature` 인수에 **세부 키를 그대로** 넣을 수 있다(별도 subfeature 인수 없음). 대표↔세부 관계·한글 라벨·손 지정 가능 여부는 `glossary-knowledge.md`의 `pattern_taxonomy` 계약을 참고.

---

## 14. 핵심 금지사항 — 이유

| 금지 | 이유 |
|---|---|
| ★ 하나 / r★ 하나만 보고 전체 실력 판단 | 클리어와 스코어는 독립 축이라 한쪽만으로는 절반만 본 것. 램프형/스코어형 편향을 놓친다. |
| `getAnalysis` 10피처만으로 세부 좌우 약점 추측 | 10축은 좌우가 합쳐진 값이라 "왼손 계단" 을 알 수 없다. `features=full` 이 필요하다. |
| 최근 AAA/AA 를 `zasa` 만 보고 평가 | 같은 zasa 라도 곡마다 스코어 난이도(`r_star.aaa`)가 다르다. 곡 등급 r★ 없이는 그 성과의 무게를 모른다. |
| 높은 EASY 클리어 한 곡으로 소화 난이도 상향 | 한 번 겨우 깬 곡은 소화 중인 게 아니다. 추천이 전부 과하게 어려워진다. |
| 램프로 r★ 추론 / 스코어로 클리어 실력 추론 | 서로 다른 축. EX-HARD 여도 점수가 낮을 수 있고, EASY 여도 AAA 가 나올 수 있다. |
| `features.scores / max_score_by_feat` 를 σ·실력%로 제시 | `report` 의 "본인 평균 대비 σ" 와 다른 통계다. 두 개를 같은 이름으로 부르면 해석이 충돌한다. |
| user feature − song feature 산술 비교 | user=절대 스코어, song=0~100 백분위. 척도가 달라 빼기/나누기가 무의미하다. |
| sparse song feature 누락값을 0 처리 | 누락 = "그 패턴이 이 곡에 거의 없음". 0(=최하위 백분위)과 다르다. 없는 축은 비교에서 빼야 한다. |
| 곡별 r★ / `explanation` / `layout_explanation` 을 임의 추측으로 대체 | 엔진이 계산한 값이 응답에 있는데 GPT 가 지어내면 근거 없는 조언이 된다. |
| 어느 섹션이든 검증된 성장 경로로 설명 | 세 섹션 모두 `validated:false` 다. `solid` 는 현재 상태 서술이고 목표①·②는 미검증 투사이므로 성장 효과를 보장하지 않는다. |
| API 가 안 준 순위를 만들기 | 제공되는 `relative_evaluation`은 사용할 수 있다. |
| API 가 안 준 값을 `sigma` 로 명명 | 사용자가 오소리 웹/리포트에서 보는 σ 와 뜻이 달라져 혼선을 준다. |
