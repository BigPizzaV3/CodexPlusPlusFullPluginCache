# Tool 선택표

| 사용자 의도 | 위젯 Tool | 데이터 Tool | 위젯 내부 선택 Tool(app-only) |
|---|---|---|---|
| 사용자에게 보여줄 요금제 목록·추천·선택 | `getPricePlans` | 사용 금지 | — |
| 명시적인 텍스트 전용 또는 비노출 내부 요금제 판단 | — | `getPricePlansData` | — |
| 기존 선택명·자연어 요약을 근거로 누락 코드 복구 | 사용 금지 | 아래 복구용 `*Data` 대응표 | 사용 금지 |
| 혜택 중심 탐색 | `getBenefitList` | `getBenefitListData` | — |
| 사용자가 확정한 특정 요금제의 혜택을 화면에서 확인·선택 | `getBenefits` | — | `selectPlanAndBenefit` |
| 요금제명 등으로 후보 요금제를 찾는 중 혜택을 내부 검증 | — | `getBenefitsData` | — |
| SIM 타입 | `getSimTypes` | `getSimTypesData` | `selectSimType` |
| 유심 배송/보유 유심 | `getUsimTypes` | `getUsimTypesData` | `selectSimType(USIM|ONE_CHIP)` |
| 가입 유형 | `getJoinTypes` | `getJoinTypesData` | `selectJoinType` |
| 개통 방식 | `getActivationTypes` | `getActivationTypesData` | `selectActivationType` |
| 전체 선택을 요약한 뒤 사용자가 개통 진행에 동의 | — | — | `createSignupHandoff` |

화면에서 사용자가 직접 선택해야 하면 위젯 Tool을 호출하고, 사용자가 명시적으로 텍스트로만 또는 위젯
없이 요청했거나 비노출 내부 판단용 데이터만 필요하면 `*Data` Tool을 호출한다. 최초 조회에는
`selectionSnapshot`을 생략하거나 빈 객체로 전달할 수 있다.
그 뒤 GPT가 호출하는 모든 조회 Tool과 위젯 내부 선택 Tool에는 현재 유효한 전체
`selectionSnapshot`을 전달한다. 호출 전 기존 유효한 모든 필드·값·타입을 대조하고, 누락되면 정상
응답에서 먼저 보충한 뒤 호출한다. 일반 진행은 이 검사를 통과한 `nextToolArguments`를 사용한다.
사용자 변경·초기화는 지정 범위에 반영하고 이전 인자를 그대로 재사용하지 않는다. 아직 미선택인
필드를 미리 요구하지 않는다. 누락 복구 중에는 아래 예외를 적용하며, Data 응답의 빈/부분 snapshot으로
기존 선택을 덮어쓰지 않는다. 다음 Tool 안내보다 호출 전 누락 방지가 우선한다.

## 누락 코드 복구용 Data 조회

기존 선택의 실제 코드를 찾는 비노출 내부 조회에는 사용자의 별도 "위젯 없이" 요청 없이도
`*Data` Tool을 사용한다. 이는 새 선택·추천·화면 표시가 아니며, 완료 후 재조회 금지의 예외다.
호출 전 정상 응답에서 보충하는 것으로 해결되지 않거나 호출 후 누락이 확인된 때만 복구 절차를
적용한다. 복구 우선순위는 정확한 이전 응답 → 기존 선택명과 Data 결과의 유일한 일치 → 부족한
항목만 사용자 확인·재선택 순이다. 복구용 Data 조회에는 아직 모르는 코드를 추측하지 않고 확인된
유효 선택값을 모두 전달할 수 있다. 정상 상태에는 예방용 재조회를 추가하지 않는다.
상세 기준은 `error-handling.md`를 따른다.

| 기존 선택 근거 | 코드 확인 Tool |
|---|---|
| 요금제명·월정액·상품 조건 | `getPricePlansData` (maxCount 없이 조회) |
| 확정 요금제의 혜택·사은품·스마트기기 상세 | 확인한 `pricePlanCode`로 `getBenefitsData` |
| eSIM·유심 구분 | `getSimTypesData` |
| 유심 배송·보유 유심 | `getUsimTypesData` |
| 신규가입·번호이동 | `getJoinTypesData` |
| 셀프개통·상담사 개통 | `getActivationTypesData` |

자연어는 선택 대조 근거이며 코드 자체가 아니다. 요약과 실제 사용자 선택이 충돌하거나 조건이
부족하면 임의로 매칭하지 않는다. 응답의 실제 코드와 필드 타입을 유지하고, Data 조회를 성공한
선택 이벤트로 간주하지 않는다. 복구 중 선택 위젯·`select*` 호출은 금지한다. 실제 재선택이 필요할
때만 해당 위젯을 표시하고 사용자 선택에 따라 위젯이 app-only `select*`를 호출한다.

요금제명처럼 `getPricePlans` 인자에 없는 조건으로 요금제 후보를 찾은 뒤 해당 요금제인지 확인하기 위해
혜택 목록을 조회하는 경우에도 `getBenefitsData`를 사용한다. 이는 후보 검증을 위한 내부 데이터 조회이므로
혜택 위젯을 표시하지 않는다. 사용자가 특정 요금제의 혜택을 실제로 보고 선택하려는 단계에서만
`getBenefits`를 사용한다.

## 사용자 발화 기준

아래는 사용자 발화 예시가 정의된 T만의 호출 기준이다. 예시가 없는 후속 화면(T2, T4, T6,
T8-2, T9)은 이 목록에 포함하지 않는다.

### T1. 요금제 탐색 → `getPricePlans`

다음과 같이 요금제 카드 목록·추천·조건 검색을 요청하면 `getPricePlans`를 호출한다.

1. 요금제 추천해줘
2. 요금제 전체 보여줘
3. 가장 저렴한 요금제 보여줘
4. 무제한 요금제 알려줘
5. 5G 요금제 알려줘
6. 인기 요금제 알려줘
7. 가성비 좋은 요금제 추천해줘
8. 가장 많이 쓰는 요금제가 뭐야?
9. 너겟 요금제 보여줘
10. 유플러스 온라인 요금제 알려줘
11. 너겟 요금제에 대해 알려줘
12. 요금제 중에서 월 5만 원 이하로 추천해줘
13. 데이터를 많이 쓰는 사람에게 맞는 요금제 추천해줘
14. 데이터를 적게 쓰는 사람에게 맞는 요금제 추천해줘
15. 데이터 100GB 이상 요금제 보여줘
16. 4만 원대 요금제 모아서 보여줘
17. 월 3만 원부터 5만 원 사이의 요금제 보여줘
18. 6만 원대 무제한 요금제 보여줘
19. 데이터 소진 후에도 계속 사용할 수 있는 요금제 알려줘
20. 약정 없이 가입할 수 있는 요금제 알려줘
21. 월 35,000원을 넘지 않는 저렴한 요금제 찾아줘
22. 요금제를 가격순으로 보여줘
23. 요금제를 데이터가 많은 순서로 보여줘
24. 데이터 제공량 대비 요금이 저렴한 상품 찾아줘
25. 테더링을 많이 사용할 때 적합한 요금제 추천해줘
26. 가족끼리 데이터를 공유할 수 있는 요금제 찾아줘
27. 데이터 50GB 이하인 요금제 알려줘
28. 가장 비싼 요금제 보여줘

표시 목적의 발화는 최종적으로 `getPricePlans` 위젯으로 표시하며 `getPricePlansData`로 텍스트 목록을
대신 만들지 않는다. 조건 필터가 필요하면 내부 판단용으로 `getPricePlansData`를 먼저 호출할 수 있다.
정렬 요청은 `order`, 표시 개수 요청은 `maxCount`로 변환한다.

요금제명, 데이터 제공량, 가격, 태그 등 `getPricePlans` 인자로 직접 표현할 수 없는 조건으로 카드 목록을 요청하면
먼저 `getPricePlansData`를 maxCount 없이 호출한다. 응답의 `plans`에서 조건에 맞는 실제
`pricePlanName`, `dataName`, `pricePlanAmount`(또는 `monthlyFee`), `tags`를 확인해 `pricePlanCode`만
추출한 뒤 `getPricePlans(pricePlanCodes=[...])`을 호출해 위젯을 표시한다. 정렬 요청이 있으면 `order`만
두 호출에 동일하게 전달하고, GPT가 요금제명을 코드로 사용하거나 코드를 임의 생성하지 않는다. 매칭되는
요금제가 없으면 `pricePlanCodes=[]`를 전달한다.
후보 요금제가 조건에 맞는지 혜택 목록으로 추가 확인해야 하는 경우에는 각 후보에 대해
`getBenefitsData(pricePlanCode=..., planName=...)`를 사용하며, 이 확인 단계에서 `getBenefits`를 호출해
혜택 위젯을 표시하지 않는다. 최종적으로 사용자가 특정 요금제의 혜택을 보고 선택할 때만 `getBenefits`를
호출한다.

### T3. 혜택 탐색 → `getBenefitList`

특정 요금제를 먼저 고르지 않고 혜택을 기준으로 탐색하면 `getBenefitList`를 호출한다.
혜택명이 포함되어도 특정 요금제 코드가 없는 발화는 `getBenefits`가 아니라 `getBenefitList` 대상이다.

1. 요금제 혜택 좀 알려줘
2. 받을 수 있는 혜택이 뭐가 있어?
3. 요금제에 가입하면 어떤 혜택을 받을 수 있어?
4. 너겟에서 제공하는 혜택을 정리해줘
5. 이용할 수 있는 혜택을 전부 보여줘
6. 혜택 목록을 한눈에 보고 싶어
7. 사람들이 많이 선택하는 혜택은 뭐야?
8. 넷플릭스 혜택이 들어간 요금제가 있어?
9. 유튜브 프리미엄 혜택을 받을 수 있는 요금제 알려줘
10. 티빙 이용권을 주는 요금제 알려줘
11. 디즈니플러스 혜택이 있는 요금제가 있어?
12. 음악 스트리밍 혜택이 있는 요금제 보여줘
13. 원하는 혜택을 골라서 쓸 수 있는 요금제가 있어?
14. 선택할 수 있는 제휴 혜택을 알려줘
15. 태블릿이나 스마트기기 혜택이 있는 요금제가 있어?
16. 기기 구매 혜택을 받을 수 있는 요금제 보여줘
17. 구글 AI 서비스를 이용할 수 있는 요금제가 있어?

### T5. SIM 유형 선택 → `getSimTypes`

가입 과정에서 eSIM·USIM 중 하나를 고르거나 관련 선택 화면을 요청하면 `getSimTypes`를 호출한다.
비교·방법을 묻는 발화라도 가입 선택을 위한 화면이 필요한 경우에는 동일하게 처리한다.

1. 요금제에 가입하려는데 이심으로 신청하고 싶어.
2. 통신 요금제를 유심으로 가입하고 싶어.
3. 요금제 가입할 때 이심으로 진행할게.
4. 요금제에 가입하려는데 유심 말고 이심으로 하고 싶어.
5. 요금제에 가입하려는데 가지고 있는 유심을 사용할 수 있어?
6. 통신 요금제를 실물 유심으로 신청하고 싶어.
7. 요금제에 가입하면서 유심을 새로 받고 싶어.
8. 이심으로 요금제에 가입하면 바로 개통할 수 있어?
9. 이심으로 요금제를 개통하려면 어떻게 해야 해?
10. 요금제에 가입할 때 이심으로 선택해 줘.
11. 실물 유심을 배송받아서 요금제를 개통하고 싶어.
12. 지금 이심을 사용하고 있는데 새 요금제도 이심으로 가입하고 싶어.
13. 이미 유심을 사용하고 있는데, 듀얼로 쓰려면 새 요금제는 이심으로 가입하면 돼?
14. 유심 배송을 기다리기 싫은데 이심으로 바로 개통할 수 있어?
15. 실물 유심을 끼우지 않고 이심으로 요금제에 가입하고 싶어.
16. 요금제에 가입하려는데 핸드폰을 자주 바꾸면 이심이 좋아, 유심이 좋아?
17. 핸드폰을 자주 바꾸는 편이라 새 요금제는 유심으로 가입하고 싶어.

### T7. 가입 유형 선택 → `getJoinTypes`

기존 번호를 유지하는 번호이동 또는 새 번호를 받는 신규가입을 고르면 `getJoinTypes`를 호출한다.

1. 요금제에 가입하려는데 쓰던 번호를 그대로 사용하고 싶어.
2. 통신 요금제를 번호이동으로 가입하고 싶어.
3. 요금제에 가입하면서 새로운 번호를 받고 싶어.
4. 통신 요금제를 신규가입으로 신청하고 싶어.
5. 지금 쓰는 번호는 그대로 유지하고 통신사만 바꾸고 싶어.
6. 다른 통신사에서 사용하던 번호 그대로 요금제에 가입할 수 있어?
7. 요금제에 가입하려는데 지금 번호 말고 새 번호를 받고 싶어.
8. 번호를 하나 더 만들고 싶은데 신규가입으로 신청하면 돼?
9. 지금 다른 통신사를 이용하고 있는데 번호이동으로 가입하면 돼?
10. 기존 번호는 계속 사용하면서 새로운 번호를 하나 더 만들고 싶어.

### T8-1. 개통 유형 선택 → `getActivationTypes`

셀프개통·상담사개통을 고르거나 두 방식을 비교·추천받으려 하면 `getActivationTypes`를 호출한다.

1. 요금제 가입하려는데 셀프개통으로 하고 싶어.
2. 요금제 가입할 때 상담사 통해서 개통하고 싶어.
3. 내가 직접 개통해서 바로 사용하고 싶어.
4. 상담사 도움받아서 개통하려면 어떻게 해야 해?
5. 지금 바로 개통하고 싶은데 어떤 방식으로 해야 해?
6. 개통이 처음인데 상담사 도움받아서 진행할 수 있어?
7. 셀프개통으로 가입하려면 어떻게 하면 돼?
8. 셀프개통이랑 상담사개통 중에 어떤 게 더 빨라?
9. 내가 직접 하지 않고 상담사가 개통해 줬으면 좋겠어.
10. 기다리지 않고 직접 빠르게 개통하고 싶어.
11. 셀프개통으로 진행하면 개통까지 얼마나 걸려?
12. 상담사개통으로 신청하면 언제부터 개통이 진행돼?
13. 요금제에 가입하려는데 어떤 개통 방식을 선택해야 할지 모르겠어.
14. 혼자 개통하기 어려울 것 같은데 상담사개통으로 신청할 수 있어?
15. 오늘 바로 사용하려면 셀프개통이 나아, 상담사개통이 나아?

조회 Tool의 가입 관련 인자는 다음과 같다. `pricePlanCodes`는 위젯 Tool인 `getPricePlans`에만 존재하며,
`getPricePlansData`는 코드 필터 없이 전체 판단 데이터를 조회하는 용도로 유지한다. 가격·태그 조건은
응답 `plans[*].pricePlanAmount`/`monthlyFee`와 `plans[*].tags`로 GPT가 판단한다.

- `getPricePlans`: 선택적인 `order`, `pricePlanCodes`, `maxCount`, `selectionSnapshot`.
  `pricePlanCodes`는 `getPricePlansData` 응답에서 확인한 `pricePlanCode`의 정확한 일치 필터이며,
  빈 배열은 매칭 결과 없음이다. 사용자가 "2개 추천",
  "2개만 보여줘", "목록에서 2개만"처럼 표시 개수를 지정하면 반드시 `getPricePlans(maxCount=2)`를
  호출한다. 이미 10개 위젯을 표시한 후의 후속 요청도 동일하며, 응답은 기존 필터·정렬 결과의 앞에서부터
  제한된 새 카드 위젯이다. 이 요청에 `getPricePlansData`를 호출하거나 전체 결과 중 일부를 GPT가
  텍스트로 대신 나열하지 않는다.
- `getPricePlansData`: 선택적인 `order`, `maxCount`, `selectionSnapshot`.
- `getBenefitList`: 선택적인 `tag`, `selectedBenefitCode`, `selectionSnapshot`
- `getBenefits`: 필수 `pricePlanCode`, 선택적인 `planName`, `selectionSnapshot`
- `getSimTypes`, `getUsimTypes`, `getJoinTypes`, `getActivationTypes`: `selectionSnapshot`

요금제 목록 위젯에서 카드를 고른 시점에는 아직 가입 선택으로 확정하지 않는다. 위젯이 선택한
요금제의 `pricePlanCode`와 `planName`, 현재 전체 snapshot을 사용해 `getBenefits`를 직접 호출하고,
혜택 화면에서 확정할 때 위젯이 `selectPlanAndBenefit`으로 요금제·혜택 묶음을 한 번에 반영한다. SIM 목록에서
일반 유심카드를 고른 경우도 아직 `simType`을 확정하지 않고, 현재 전체 snapshot으로
`getUsimTypes`를 직접 호출한다. 배송 또는 보유 유심을 고른 뒤에 각각 `USIM` 또는 `ONE_CHIP`으로
위젯이 `selectSimType`을 호출한다. eSIM도 위젯이 `selectSimType(type=ESIM)`으로 바로 반영한다.

`select*`는 `_meta.ui.visibility=["app"]`인 위젯 전용 Tool이다. 모델용 Tool 카탈로그에서 숨겨지며
GPT는 직접 호출하지 않는다. `selectPlanAndBenefit`은 요금제와 혜택을 즉시 검증하고, 모든 `select*`는 요청의
전체 snapshot에 이번 patch를 병합해 누적 snapshot을 응답한다. 선택 직후 위젯이 보낸
`SIGNUP_SELECTION_UPDATED`에는 이미 이번 patch가 반영되어 있으므로 같은 `select*`를 다시 호출하지
않는다. `missingFields`를 기준으로 다음 조회 Tool을 고르고, 해당 호출에도 전체 snapshot을 그대로
전달한다.

아래 인자 계약은 위젯 구현용이다. 위젯은 선택 Tool 요청에 `selectionPatch` wrapper를 만들지 않고,
실제 선택 인자와 기존 `selectionSnapshot`을 같은 최상위 arguments 객체에 넣는다.

- `selectPlanAndBenefit`: `planId`, `planName`, `isMobileHomePlan`(`true` 또는 `false`),
  `deviceBenefitCodesJson`, `benefitCodes`, `giftCodes`, `selectionSnapshot`. 스마트기기·일반 혜택·사은품
  선택 대상이 없으면 각각 빈 배열로 반영할 수 있다. `isMobileHomePlan`과 요금제명은 선택된 요금제
  정보이므로 생략하거나 `null`로 전달하지 않는다.
- `selectSimType`: `type`, `selectionSnapshot`
- `selectJoinType`: `type`, `selectionSnapshot`
- `selectActivationType`: `type`, `selectionSnapshot`

`selectionPatch`는 성공 응답에서 이번에 반영된 값만 확인하는 필드다.
`deviceBenefitCodesJson`은 객체 배열 자체가 아니라
`[{"code":"...","colorCode":"...","contractMonthCount":"..."}]` 형태를 JSON 문자열로
직렬화한 값이다. 스마트기기 혜택을 선택하지 않았다면 생략할 수 있다. `benefitCodes`와
`giftCodes`는 JSON 문자열이 아닌 실제 배열로 전달하며, 선택 없음은 `[]`로 전달한다.
숫자 `0`도 유효한 실제 사은품 코드다. 따라서 `giftCodes: [0]`은 선택 완료로 유지하고 재선택을
요구하지 않는다.

`createSignupHandoff`도 `deviceBenefitCodes`, `benefitCodes`, `giftCodes`의 빈 배열을 선택 없음의
정상값으로 허용한다. 다만 세 key 자체는 전체 snapshot에 존재해야 하며, `null` 또는 key 누락은
미완료로 처리한다. `isMobileHomePlan`은 최종 snapshot에서 `true` 또는 `false`여야 한다.

`SIGNUP_SELECTION_UPDATED`를 받으면 어떤 `select*`도 호출하지 않는다. model context 또는
호환 fallback 메시지 JSON의
`planBenefitComplete=true`이면 사용자가 요금제나
혜택을 바꾸겠다고 명시하지 않는 한 `getPricePlans`, `getPricePlansData`, `getBenefits`,
`getBenefitsData`를 다시 호출하지 않는다. 단, 누락 코드 복구용 비노출 Data 조회는 예외다.
기존 선택과 `missingFields`가 일치하면 `nextTool`을 참고해 다음 조회를 진행한다. 기존 선택 근거와
불일치하면 `planBenefitComplete`의 값과 무관하게 복구를 먼저 시도하고, 실제 미선택·복구 불가
항목만 확인·선택한다.

요금제 조회 응답은 API 단계에서 판매 불가 요금제가 제거된 결과다. 응답에 `onSale=false`가 있어도
GPT가 판매 불가로 재판정하거나 해당 요금제를 숨기지 말고, 조회 결과에 포함된 요금제는 선택 가능한
항목으로 안내한다.

최종 Tool은 사용자의 별도 명시적 동의 후에만 호출한다. 반드시 `userConfirmed=true`와 직전에
직전 사용자용 선택 요약에 대응하는 내부 전체 `selectionSnapshot`을 전달한다.
요약에는 사용자용 명칭과 조건만 표시하며, 코드·필드명·enum·원시 배열·JSON은 노출하지 않는다.
