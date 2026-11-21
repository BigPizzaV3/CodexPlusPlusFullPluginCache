# dan-knowledge.md — beatmania IIDX DP 단위인정 참고 지식

최종 조사일: 2026-09-11 (JST/KST 기준)  
대상: **DOUBLE PLAY (DP)**  
범위: **beatmania IIDX INFINITAS (2024-03-13 개편 이후)** 및 **beatmania IIDX 33 SPARKLE SHOWER 현행 단위인정**, 八段~皆伝  
목적: 오소리 IIDX DP 코치가 단위 목표/합격 가능성/과제곡 대비를 설명할 때 사용하는 보조 Knowledge.

> 중요: 곡 목록은 현행/지정 버전에 종속된다. 버전 업데이트로 교체될 수 있으므로 이후 작품 또는 INFINITAS 개편 후에는 다시 검증한다.
> 게이지의 세부 수치는 KONAMI 공식 문서가 공개한 완전한 수치표가 아니라, 장기간 커뮤니티 실측·정리에서 일치하는 값을 정리한 것이다. 공식 확인 범위와 실측 범위를 구분해서 사용한다.

---

## 1. 단위인정 기본 구조

KONAMI 공식 SPARKLE SHOWER 안내상 段位認定은 **전 4 STAGE의 정해진 코스**를 연속 플레이하여 실력을 판정하는 모드다. 모든 플레이어가 같은 조건으로 플레이하도록 일부 옵션이 제한된다.

단위인정에서는 일반적인 STANDARD의 클리어 게이지와 다른 **段位ゲージ(단위 게이지)**를 사용한다. 게이지는 곡 사이에 이어지며, 4곡 도중 한 번이라도 0%가 되면 그 시점에서 실패한다. 끝까지 0%가 되지 않고 완주하면 합격한다.

### 코칭 시 해석 원칙

* 단위 합격은 단순히 각 곡의 EASY/HARD 램프와 동일하지 않다.
* 4곡을 **한 게이지로 이어서 버티는 능력**, 즉 회복 구간에서 복구하고 위험 구간에서 저게이지 보정을 활용해 생존하는 능력이 중요하다.
* 따라서 “이 곡 HARD 가능 → 단위에서도 안전” 또는 “FAILED → 단위에서 불가능”처럼 자동 변환하지 않는다.
* 특히 BP만으로 단위 합격을 단정하지 않는다. 같은 BP라도 BAD/POOR 구성, 미스가 몰리는 위치, 회복 가능한 구간, 곡 시작 게이지가 다르면 결과가 크게 달라진다.
* 단위 코스에서는 **곡별 종료 게이지와 다음 곡 진입 게이지**가 중요하다. 가능하면 실제 단위 리절트/영상/구간별 게이지를 우선한다.

---

## 2. 단위 게이지 수치

아래 값은 IIDX 커뮤니티에서 장기간 실측·정리된 **비공식 실측값**이며, **단위인정 전용 게이지**다. EASY/NORMAL/HARD/EX-HARD 등 일반 클리어 게이지는 증감량도 클리어 조건도 다르다 — `gauge-knowledge.md` 를 따로 본다. 두 게이지를 같은 수치로 섞어 계산하지 마라.

| 판정 | 단위 게이지 (DAN) | EX단위 게이지 (EX-DAN) |
|---|---:|---:|
| PGREAT | +0.16% | +0.16% |
| GREAT | +0.16% | +0.16% |
| GOOD | +0.04% | +0.04% |
| BAD | -1.5% | -3.0% |
| 공(空) POOR | -1.5% | -3.0% |
| 미스/놓침 POOR | -2.5% | -5.0% |
| 저게이지(30%) 보정 | **있음** | **없음** |

둘 다 100%에서 시작하고 게이지가 0% 미만이 되면 그 시점에 종료된다. **EX단위는 감소량이 정확히 2배이고 저게이지 보정도 없어** 일반 단위와 같은 기준으로 판단하면 안 된다.

### 30% 보정

잔여 게이지가 **대략 30% 이하의 저게이지 영역**에 들어가면 미스에 의한 감소량이 절반 수준으로 줄어드는, 통칭 **30% 보정**이 있다. **이 보정은 일반 단위에만 있고 EX단위에는 없다.**

보정 적용 시 실측값 기준으로 대략:

* BAD / 공POOR: -1.5% → 약 -0.75%
* 미스POOR: -2.5% → 약 -1.25%

주의:
* 커뮤니티 자료 중에는 내부 발동 경계를 표시 30%가 아니라 약 1/3(33.3% 부근)으로 설명하는 경우도 있다.
* 공식 문서가 내부 임계값을 공개한 것은 아니므로 코칭에서는 **“약 30% 이하에서 감소량 반감”**으로 표현한다.
* 표시 게이지는 2% 단위처럼 보이지만 내부 계산은 더 세밀하게 이루어진다고 알려져 있어, 화면 숫자만으로 정확한 한 노트 단위 계산을 역산하지 않는다.

### 회복 관점

PGREAT와 GREAT의 회복량은 동일하고, GOOD도 소량 회복한다. 따라서 단위 생존에서는 점수보다 **BAD/POOR를 줄이고, 쉬운 구간을 끊기지 않게 회복하는 것**이 중요하다.

예를 들어:
* 스코어가 낮아도 GREAT/GOOD로 계속 주워서 게이지를 유지하면 단위에는 유리할 수 있다.
* 반대로 EX SCORE가 높더라도 특정 발광 구간에서 POOR가 몰리면 단위게이지가 급락할 수 있다.
* 특히 미스POOR는 BAD/공POOR보다 감소량이 크므로 “아예 놓치는” 형태의 붕괴가 위험하다.

### BP와 단위 게이지의 관계

BP는 단위 대비 참고값이지 직접적인 게이지 계산식이 아니다.

BP만으로 다음을 단정하지 않는다:
* “BP 50이면 합격”
* “BP 100이면 불합격”
* “HARD 클리어했으니 단위에서 절대 안 죽음”

이유:
1. BP에는 BAD와 POOR가 섞인다.
2. 단위 게이지는 저게이지 보정이 있다.
3. 미스가 한 구간에 몰리는지 분산되는지가 중요하다.
4. 앞 곡에서 몇 %를 들고 진입했는지가 중요하다.
5. 곡 후반의 발광은 다음 곡으로 회복할 기회를 주지 않을 수 있다.

따라서 합격 가능성을 볼 때 우선순위는:
1. 실제 단위 플레이의 곡별 종료 게이지
2. 해당 과제곡 정배치/단위 옵션에서의 플레이 상태
3. BP와 미스 집중 구간
4. 일반 램프와 유사 난이도 처리력
순으로 본다.

---

# 3. DP 단위인정 과제곡 — INFINITAS

기준: **2024-03-13 업데이트 이후 개편 코스**.  
2024-03-13 이전 구 코스와 혼동하지 않는다.

## DP 八段 — INFINITAS 2024

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | Vector | ANOTHER | 10 | 1283 |
| 2nd | Digitank System | ANOTHER | 10 | 1175 |
| 3rd | Reflection Into the EDEN | ANOTHER | 10 | 1283 |
| FINAL | THE LAST STRIKER | ANOTHER | 10 | 1342 |

## DP 九段 — INFINITAS 2024

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | Caldwell 99 | ANOTHER | 11 | 1338 |
| 2nd | mosaic | ANOTHER | 11 | 1348 |
| 3rd | Arabian Rave Night | ANOTHER | 11 | 1605 |
| FINAL | Infinite cave | ANOTHER | 12 | 1525 |

## DP 十段 — INFINITAS 2024

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | KAMAITACHI | ANOTHER | 12 | 1662 |
| 2nd | リリーゼと炎龍レーヴァテイン | ANOTHER | 12 | 1848 |
| 3rd | EXUSIA | ANOTHER | 12 | 1980 |
| FINAL | Quakes | ANOTHER | 12 | 1613 |

## DP 中伝 — INFINITAS 2024

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | Holic | ANOTHER | 12 | 1136 |
| 2nd | 灼熱Beach Side Bunny | ANOTHER | 12 | 1692 |
| 3rd | ワルツ第17番 ト短調"大犬のワルツ" | ANOTHER | 12 | 2290 |
| FINAL | GuNGNiR | ANOTHER | 12 | 2175 |

## DP 皆伝 — INFINITAS 2024

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | GENOCIDE | ANOTHER | 12 | 1456 |
| 2nd | Bad Maniacs | ANOTHER | 12 | 1606 |
| 3rd | 共鳴遊戯の華 | ANOTHER | 12 | 2054 |
| FINAL | perditus†paradisus | ANOTHER | 12 | 2109 |

---

# 4. DP 단위인정 과제곡 — beatmania IIDX 33 SPARKLE SHOWER

기준: **SPARKLE SHOWER 현행 일반 단위인정**.  
`裏十段/裏中伝/裏皆伝`은 별도 코스이며 아래 일반 단위 목록에 포함하지 않는다.

## DP 八段 — SPARKLE SHOWER

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | NEEDLESS MY LOVE FOR YOU | ANOTHER | 10 | 1301 |
| 2nd | Infinity Mirror | ANOTHER | 10 | 1303 |
| 3rd | AMRITA -不滅ノ花- | ANOTHER | 11 | 1327 |
| FINAL | Space Time | ANOTHER | 11 | 1359 |

## DP 九段 — SPARKLE SHOWER

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | Ambush Ace | ANOTHER | 11 | 1477 |
| 2nd | ROCK女 feat. 大山愛未, Ken | ANOTHER | 11 | 1435 |
| 3rd | Yellow Sunrise | ANOTHER | 11 | 1493 |
| FINAL | ミッドナイト堕天使 | ANOTHER | 12 | 1552 |

## DP 十段 — SPARKLE SHOWER

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | invoker | ANOTHER | 12 | 1659 |
| 2nd | LASER CRUSTER | ANOTHER | 12 | 1721 |
| 3rd | Flying Castle | ANOTHER | 12 | 1889 |
| FINAL | シムルグの目醒め | ANOTHER | 12 | 1815 |

## DP 中伝 — SPARKLE SHOWER

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | Level 5 | ANOTHER | 12 | 1858 |
| 2nd | ワルツ第17番 ト短調"大犬のワルツ" | ANOTHER | 12 | 2290 |
| 3rd | 津軽雪 | ANOTHER | 12 | 2101 |
| FINAL | ∀ | ANOTHER | 12 | 1879 |

## DP 皆伝 — SPARKLE SHOWER

| STAGE | 곡 | 난이도 | Lv | Notes |
|---|---|---|---:|---:|
| 1st | EMERALDAS | ANOTHER | 12 | 1763 |
| 2nd | ピアノ独奏無言歌 "灰燼" | ANOTHER | 12 | 2174 |
| 3rd | 天空の夜明け | ANOTHER | 12 | 2261 |
| FINAL | quasar | ANOTHER | 12 | 1562 |

---

## 5. 단위 목표 분석 규칙

사용자가 “중전 가능?”, “십단 붙을까?”, “몇 %쯤 남길까?”처럼 단위 목표를 물으면 다음 순서로 본다.

### 5.1 현재 단위와 클리어 축

* `profile.dp.rank`
* `profile.dp.star` / `star_estimate`
* `getRecent`의 실제 HARD/EX-HARD 성과
* 필요시 `getShelf.skill_line`

단위는 클리어/생존 목표이므로 **r★를 직접 합격 근거로 사용하지 않는다.**

### 5.2 과제곡 개별 상태

각 과제곡에 대해 가능하면:
* `getSong` — 곡 자체의 zasa·필요 실력·패턴. 곡명으로 직접 조회된다.
* `getScores` — 본인 성적. **과제곡은 `title=곡명` 또는 `song_id=` 로 직접 지정해 조회한다**(반복 지정 가능 — 4곡을 한 번에). 곡을 지정하면 zasa 내림차순 400행 절단에 걸리지 않는다. 지정 없이 `level=12` 로만 받으면 실측상 zasa 12.2 근처에서 잘려 **八段~十段대 과제곡이 누락된다**(十段 1st `KAMAITACHI` = zasa 12.1 실측 누락).
  응답의 `requested.titles[]` 는 `song_count`(그 곡이 오소리에 있는가)와 `user_record_count`(내 기록이 있는가)를 따로 준다 — **"곡이 없음"과 "아직 안 쳤음"을 구분해 말해라.**
* `getRecent` — 최근 갱신된 과제곡만 잡힌다. 잔존 갱신 기록이라 과거에 친 곡은 안 나올 수 있다.

**과제곡 성적이 위 도구로 확인되지 않으면 "성적 미확인"으로 표시하고, 램프·BP·점수를 추측하지 마라.** 사용자가 직접 알려준 램프·BP·게이지 기록은 근거로 써도 된다.

곡의 단위 내 위험도를 설명할 때는:
* 단순 `zasa`만 보지 말고
* 사용자 패턴 약점과 과제곡의 실제 패턴을 `getAnalysis + getSong features=full`로 교차 확인한다.

### 5.3 단위 게이지 관점

다음처럼 표현한다.

좋은 표현:
* “이 곡은 일반 클리어 여부보다 후반 발광에서 게이지를 얼마나 남기는지가 중요하다.”
* “30% 부근부터 감소 보정이 있어 저공비행 자체가 즉시 실패를 뜻하지는 않는다.”
* “BP 수만으로 합격을 단정할 수 없고, 미스가 발광에 몰리는지와 곡 종료 게이지가 더 중요하다.”
* “2곡 종료 시 20~30%라도 다음 곡 초반에 회복 구간이 있다면 생존 여지가 있다.”

피해야 할 표현:
* “BP 70 이하면 중전 확정”
* “HARD 클리어니까 단위는 무조건 통과”
* “FAILED니까 단위에서도 절대 못 버팀”
* “AAA니까 단위게이지도 안정”
* 실제 단위 게이지 기록 없이 정확한 종료 %를 예언하는 것

### 5.4 코스 특성은 곡별로 판단

과제곡의 위험 구간/회복 구간/패턴 성향을 설명하려면 해당 곡을 `getSong features=full`로 조회한다.  
Knowledge에 적혀 있지 않은 패턴 성향을 곡명이나 악명만으로 추측하지 않는다.

---

## 6. 버전 구분 및 갱신 정책

### INFINITAS

현재 이 문서의 코스는 **2024-03-13 개편 이후** 기준이다.  
그 이전 INFINITAS 단위 코스는 별도 구버전이며 섞지 않는다.

사용자가 단순히 “인피 중전”이라고 하면 이 최신 개편판을 기본으로 해석하되, 향후 INFINITAS 단위 개편이 확인되면 최신판을 우선한다.

### SPARKLE SHOWER

이 문서는 **beatmania IIDX 33 SPARKLE SHOWER 일반 DP 단위** 기준이다.

SPARKLE SHOWER에는 별도 `裏十段 / 裏中伝 / 裏皆伝`도 존재하지만, 사용자가 “뒷단위/裏”라고 명시하지 않는 한 일반 十段/中伝/皆伝과 섞지 않는다.

### 작품 변경 시

다음 IIDX 작품이 가동되면 SPARKLE SHOWER 목록을 “구작 코스”로 취급하고, 현행 작품의 과제곡을 새로 조사한다.

---

## 7. 출처 및 신뢰도

### 과제곡 목록

1. iidx.org — Infinitas (2024) Class Mode  
   https://iidx.org/dan/infinitas  
   INFINITAS 2024 DP 八段~皆伝의 곡/난이도/노트 수를 교차 확인.

2. iidx.org — Sparkle Shower Class Mode  
   https://iidx.org/dan/sparkleshower  
   SPARKLE SHOWER DP 八段~皆伝의 곡/난이도/노트 수를 교차 확인.

3. beatmania IIDX DP攻略 @ wiki — DP 각 단위 공략  
   https://w.atwiki.jp/bemani2dp/pages/247.html  
   각 현행/INFINITAS 코스 페이지와 개편 구분을 확인.

4. KONAMI 공식 beatmania IIDX 33 SPARKLE SHOWER HOW TO PLAY  
   https://p.eagate.573.jp/game/2dx/33/howto/mode/game_mode.html  
   段位認定이 전 4 STAGE 코스이며 일부 옵션이 제한됨을 공식 확인.

### 단위 게이지

5. beatmania IIDX SP攻略 @ wiki — 게임 사양 해설  
   https://w.atwiki.jp/bemani2sp/pages/4662.html  
   단위게이지의 4곡 연속 사용, GOOD 회복, BAD/POOR 감소량, 30% 보정 정리.

6. とりのげーむ小屋 — beatmaniaIIDXのゲージ増減量について  
   https://tri999.blog66.fc2.com/blog-entry-341.html  
   CS IIDX RED를 이용한 실측. PG/G +0.16, GOOD +0.04, BAD/공POOR -1.5, POOR -2.5 및 30% 미만 감소량 0.5배를 보고.

7. beatmaniaIIDXシリーズ基礎情報まとめ  
   https://purotora.com/bemani/bmIIdx00.html  
   단위게이지 증감량 및 30% 보정을 별도 표로 정리하여 위 실측과 교차 확인.

### 신뢰도 메모

* **코스 목록:** 높음. 복수 현행 자료에서 일치.
* **4곡 구조/옵션 제한:** 높음. KONAMI 공식 확인.
* **세부 게이지 수치:** 중~높음. 공식 수치표는 아니지만 장기간 독립 자료가 동일 값을 보고. 대조 출처 = iidx.org Compendium "Gauge Calculation and Timing Windows" (https://iidx.org/compendium/gauges_and_timing).
* **EX단위 수치:** 중~높음. 같은 출처의 EX-DAN 행 기준.
* **30% 보정 내부 임계점:** 중간. 사용자에게는 “약 30% 이하”로만 표현하고 30.0%/33.3%의 내부 경계를 확정적으로 말하지 않는다.

---

## 8. 빠른 참조 — 상위 DP 단위 보스

* INFINITAS 八段 FINAL: THE LAST STRIKER [A]
* INFINITAS 九段 FINAL: Infinite cave [A]
* INFINITAS 十段 FINAL: Quakes [A]
* INFINITAS 中伝 FINAL: GuNGNiR [A]
* INFINITAS 皆伝 FINAL: perditus†paradisus [A]

* SPARKLE SHOWER 八段 FINAL: Space Time [A]
* SPARKLE SHOWER 九段 FINAL: ミッドナイト堕天使 [A]
* SPARKLE SHOWER 十段 FINAL: シムルグの目醒め [A]
* SPARKLE SHOWER 中伝 FINAL: ∀ [A]
* SPARKLE SHOWER 皆伝 FINAL: quasar [A]
