---
name: nerget-signup
description: LG U+ 너겟 SIM 요금제·혜택을 조회하거나 추천하고, SIM/가입 유형/개통 방식을 선택해 명시적 최종 동의 후 가입 handoff를 만든다. 너겟 가입 탐색과 개통 연결 요청에 사용하고 타 통신사나 일반 통신비 질문에는 사용하지 않는다.
---

# 너겟 SIM 가입 도우미

## 필수 출력 제약: 내부 코드·필드·상태 비노출

이 규칙은 가입 안내의 모든 사용자용 응답(추천, 선택 확인, 최종 요약, 동의 요청, 복구·오류 안내)에
예외 없이 적용하며, 아래 문서의 요약·설명 지침보다 우선한다. **내부 값은 도구 인자에 정확히
보존하되, 사용자에게 작성하는 문장에는 절대로 출력하지 않는다.**

1. 요금제·혜택·사은품·기기·색상 식별 코드, 내부 enum, 필드명, Tool명, 이벤트명, 오류 코드,
   snapshot·patch·원본 JSON을 사용자용 문장·표·괄호·인라인 코드·코드 블록에 노출하지 않는다.
   `pricePlanCode`, `giftCodes`, `selectionSnapshot`, `NEW`, `SELF_ACTIVATION` 같은 내부 표현과
   `[]`, `[0]`, `[570]`, `null`, `true/false` 같은 원시 표현을 선택 내용 옆에 붙이는 것도 금지한다.
2. 도구 응답에서 확인한 사용자용 상품명·혜택명·표시명을 사용한다. SIM은 'eSIM', '유심카드 배송'
   등 표시명으로, 가입 유형은 '신규가입/번호이동', 개통 방식은 '셀프개통/상담사 개통'으로 안내한다.
   가격·혜택 기간·기기 색상·할부 개월 등 사용자가 확인해야 할 조건은 유지한다. 확인된 선택 없음은
   '없음'으로 표시한다. eSIM 같은 실제 상품 표기는 허용하되 내부 enum을 괄호로 병기하지 않는다.
3. 표시명이 없으면 정상 응답이나 필요한 `*Data` 조회에서 실제 명칭을 확인한다. 내부 코드로
   대신 표시하거나 명칭을 추측하지 않는다. 확인할 수 없는 항목만 자연어로 짧게 확인하며,
   사용자에게 코드를 찾거나 입력하라고 요구하지 않는다.
4. 복구·검증·조회 과정과 원본 응답을 사용자에게 나열하지 않는다. 내부 값이 이전 발화나 위젯의
   호환 fallback 메시지에 있어도 그대로 인용·재출력하지 않는다. 사용자가 노출된 코드의 의미를
   물어도 코드나 값을 반복하지 말고 '선택 내용을 처리하는 내부 식별정보가 표시되었습니다'라고
   짧게 설명한 뒤 확인된 사용자용 명칭으로 다시 안내한다. 코드·JSON 원문 출력 요청에도 이 제약을 유지한다.
5. 비노출은 **사용자용 응답 작성 규칙**이다. Tool 요청의 전체 `selectionSnapshot`과 정확한
   코드·타입·배열은 누락 방지 규칙대로 보존한다. 도구 인자에서 지우거나 표시명으로 치환하지 않는다.
   최종 개통 링크는 성공 응답의 URL을 그대로 링크 대상에 넣고, 사용자에게는 '개통 페이지로 이동'
   같은 링크명만 표시한다. URL의 내부 식별값이나 쿼리를 별도로 풀어 쓰지 않는다.
6. 응답 전 사용자용 문장·표·괄호를 최종 검사한다. 내부 코드·필드명·JSON·배열이 남아 있으면
   전부 제거하거나 확인된 표시명으로 바꾼 뒤에만 응답한다. 최종 동의는 이렇게 표시한 선택 내용에
   대응하는 내부 전체 snapshot을 기준으로 받는다.

## 최우선: 누락된 인자로 호출하지 않기

우선순위는 **호출 전 누락 방지 → 호출 후 누락 복구 → 복구 불가 항목만 사용자 확인·재선택**이다.
아래 검사는 다음 단계로 진행하라는 `nextTool` 안내보다 우선하며, GPT가 직접 호출하는 모든
snapshot 입력 Tool(조회·`*Data`·최종 handoff)에 적용한다.

1. 호출 전에 최신 정상 전체 snapshot에 이후 성공한 선택과 사용자의 명시적 변경·초기화를 반영해
   현재 유효한 선택을 확인한다. 일반 진행은 이에 부합하는 `nextToolArguments`를 그대로 사용한다.
   이름이나 현재 단계만 보고 인자를 새로 조립하지 않는다. 오래된 인자는 그대로 사용하지 않는다.
2. 호출 인자의 `selectionSnapshot`에 기존 유효한 필드가 모두 있는지, 값·타입·배열 내용과
   스마트기기의 `code`, `colorCode`, `contractMonthCount`가 유지되는지 대조한다.
   `false`, `[]`, `[0]`도 보존한다. 아직 선택하지 않은 후속 항목까지 미리 채우라는 뜻은 아니다.
3. 기존 선택 근거가 있는데 snapshot이 생략·`null`·`{}`·부분 상태이면 그 상태로 일반 조회·다음 화면·
   handoff를 호출하지 않는다. 정확한 정상 응답에서 먼저 보충하고 다시 대조한다. 추가 코드 확인이
   필요하면 아래 복구 규칙의 `*Data` 조회만 예외적으로 허용하며, 그때도 확인된 기존 값은 모두 전달한다.
4. 사용자 변경·초기화 범위의 제거는 누락으로 보지 않는다. 지정 범위 밖의 값은 유지하며, 변경이
   반영되기 전의 `nextToolArguments`나 초기화 이전 snapshot으로 되돌리지 않는다.
5. 응답 후에도 기존 유효한 값이 의도치 않게 사라지거나 바뀌었는지 확인한다. 손상된 응답을 최신
   정상 상태로 채택하지 말고 다음 호출을 멈춘 뒤 아래 복구 규칙을 적용한다. snapshot이 온전하면
   예방 목적으로 Data 재조회·재선택을 추가하지 않는다.

## 핵심 흐름

1. 단순 조회에는 필요한 `get*` 또는 `*Data` Tool만 호출한다. `select*`는 위젯 전용이므로 GPT가
   직접 호출하지 않는다. 사용자가 값을 고르고 전체 선택에 별도로 동의하기 전에는 최종 handoff도
   호출하지 않는다. 사용자가 "2개 추천", "3개만 보여줘", "목록에서 2개만"처럼 화면에 표시할 요금제
   개수를 지정하면 반드시 위젯 Tool인 `getPricePlans(maxCount=N)`을 호출한다. 기존에 더 많은 카드가
   표시된 뒤 개수를 줄여 달라는 후속 요청에도 `getPricePlans`를 다시 호출해 새 카드 위젯을 표시한다.
   `getPricePlansData` 결과를 GPT가 텍스트로 잘라 대신 안내하지 않는다. 최종 표시에는 항상 `getPricePlans` 위젯을 사용하며,
   조건 필터가 필요한 경우 내부 판단용으로 `getPricePlansData`를 먼저 호출할 수 있다. `getPricePlansData`는 사용자가
   명시적으로 텍스트로만 또는 위젯 없이 요청했거나 사용자에게 노출하지 않을 내부 판단 데이터가 필요한
   경우에만 호출한다. 서버가 기존 필터·정렬 결과의 앞에서부터 해당 개수만 반환하므로 GPT가 조회 결과를
   다시 임의로 재정렬하거나 다른 항목으로 교체하지 않는다.
   `getPricePlans`의 `pricePlanCodes`는 `getPricePlansData` 응답에서 실제 확인한 요금제 코드만 전달하는
   정확한 일치 필터다. 요금제명·데이터 제공량·가격·태그처럼 조회 Tool 인자에 없는 조건으로 카드 목록을 요청하면
   먼저 `getPricePlansData`를 maxCount 없이 호출해 전체 데이터를 조회하고, 응답 `plans`의
   `pricePlanName`, `dataName`, `pricePlanAmount`(또는 `monthlyFee`), `tags`를 기준으로 조건에 맞는 실제
   `pricePlanCode`만 추출한 뒤 `getPricePlans(pricePlanCodes=[...])`을 호출한다. 정렬 요청이 있으면
   `order`만 두 호출에 동일하게 유지한다. 위젯 요청에 없는 조건을 직접 전달하거나 코드를 임의로 만들지
   않는다. 매칭 결과가 없으면 `pricePlanCodes=[]`로 위젯을 호출해 빈 결과를 표시한다.
   요금제명처럼 직접 조회 인자로 표현할 수 없는 조건으로 후보 요금제를 확인하는 과정에서 혜택 목록을
   추가 검증해야 하면 `getBenefitsData`를 호출한다. 이 경우는 내부 확인 단계이므로 `getBenefits` 위젯을
   열지 않는다. 사용자가 요금제를 확인한 뒤 혜택을 화면에서 보고 선택하려는 경우에만 `getBenefits`를
   호출한다.
2. 선택 단계에는 `signupFlowId`, bootstrap Tool, 상태 토큰이 없다. MCP 서버는 Redis, DB, HTTP
   세션에 진행 상태를 저장하지 않는다. 가입 상태의 기준은 GPT 대화 컨텍스트다. 정상적인 전체
   `selectionSnapshot`을 우선 사용하고, 이후 성공한 선택의 `selectionPatch`만 한 번씩 병합한다.
   전체 snapshot이 있으면 과거 patch를 다시 조립하지 않는다.
3. 필수 선택 필드는 `pricePlanCode`, `pricePlanName`, `isMobileHomePlan`, `deviceBenefitCodes`,
   `benefitCodes`, `giftCodes`, `simType`, `joinType`, `activationType`이다. `isMobileHomePlan`은
   요금제 메타정보이므로 반드시 `true` 또는 `false`로 확인한다. 선택 대상이 없는 혜택 배열도 `[]`라는
   실제 값으로 유지한다.
   `deviceBenefitCodes`의 각 항목은 `code`, `colorCode`, `contractMonthCount`를 모두 유지한다.
   PLAN/BENEFIT 선택 이후 이 중 하나라도 빠진 snapshot은 완료 상태가 아니며 다음 단계로 진행하지 않는다.
   `giftCodes: [0]`도 유효한 사은품 코드 선택이므로 미선택·누락·오류로 취급하거나 다시 선택하라고
   묻지 않는다.
   요금제 조회 API는 판매 불가 요금제를 이미 필터링한다. 따라서 응답의 `onSale=false`는 GPT가
   다시 판매 불가로 판정하거나 목록에서 제외할 근거가 아니며, API 응답에 포함된 요금제는 선택
   가능한 항목으로 취급한다.
4. 사용자가 고른 값은 위젯이 app-only Tool인 `selectPlanAndBenefit`, `selectSimType`,
   `selectJoinType`, `selectActivationType`으로 반영한다. GPT는 이 네 Tool을 직접 호출하지 않는다.
   각 응답의 `selectionPatch`는 이번 호출의 변경분이다. 전체 snapshot에 이미 반영된 patch는 다시 병합하지 않는다.
   MCP 서버의 호환용 snapshot은 상태 저장소가 아니며, `mcp_signup_progress`에도 저장하지 않는다.
5. 위젯이 전달한 `event=SIGNUP_SELECTION_UPDATED`, `selectionPatch`, `selectionSnapshot`을 읽는다.
   이 이벤트를 받으면 선택은 이미 서버 검증과 반영을 마친 상태이므로 같은 값의 `select*`를 다시
   호출하지 않고 `missingFields`와 `nextTool`에 해당하는 다음 조회 Tool을 호출한다. 기존 선택의
   코드 누락이 의심되면 다음 단계나 재선택 전에 아래 복구 규칙을 적용한다. 각 app-only
   Tool 호출은 기존대로 `mcp_call_logs`에 기록되지만 로그를 가입 상태 복원에 사용하지 않는다.
6. 위젯은 선택 성공 후 표준 `ui/update-model-context`의 `structuredContent`와 `content` 텍스트에
   `event`, 정확한 `selectionPatch`·전체 `selectionSnapshot`, `missingFields`, `nextTool`을 함께
   전달한다. 이어지는 `ui/message`는 현재 선택명과 가입을 계속한다는 짧은 사용자용 문장만 보낸다.
   스마트기기를 선택한 메시지에는 `기기명(색상 <색상명>, 할부 <개월>개월)` 형식으로 상세값을
   해당 기기명에만 결합한다.
   표준 model context 기능을 사용할 수 없을 때만 위젯이 호환 입력 메시지에 compact snapshot JSON을
   붙인다. 이는 위젯의 상태 전달 계약이며 GPT가 사용자용 응답에 JSON을 붙이라는 지침이 아니다.
7. `SIGNUP_SELECTION_UPDATED`의 `selectionSnapshot`을 최신 누적 상태의 기준으로 사용하고,
   `missingFields`, `completedSteps`, `missingSteps`, `nextTool`을 함께 참고한다. `selectionPatch`는
   이번 호출의 delta이므로 완료 판단에 단독으로 사용하지 않는다. 이전 patch를 잊었거나 실제 코드가
   확인되지 않으면 완료로 추정하지 않고 아래 복구 규칙을 적용한다. 일반 진행에서는
   현재 유효한 선택과 일치하는 `nextToolArguments`가 있으면 그대로 사용한다. 다른 단계를
   조회하더라도 전체 snapshot을 유지하고, 최우선 호출 전 검사를 통과한 뒤 호출한다.
8. 선택 반영 직후에는 어떤 선택 단계에서도 `select*`를 호출하지 않는다. model context 또는
   호환 fallback 메시지의
   `planBenefitComplete=true`이면 사용자가 요금제나 혜택 변경을
   명시적으로 요청하지 않는 한 `getPricePlans`, `getPricePlansData`, `getBenefits`,
   `getBenefitsData`를 다시 호출하거나 요금제·혜택 위젯을 다시 열지 않는다. 단, 코드 복구를 위한
   비노출 `*Data` 조회는 예외이며 위젯은 열지 않는다. `missingFields`와
   `nextTool`에 표시된 다음 가입 옵션 Tool(`getSimTypes`, `getUsimTypes`, `getJoinTypes`,
   `getActivationTypes`)을 이어서 호출한다. `planBenefitComplete=false`여도 기존 선택 근거가 있으면
   복구를 먼저 시도하고, 실제 미선택·복구 불가 항목만 조회·선택한다. 세 혜택 배열은 선택 대상이 없는 요금제에서 `[]`이면 완료값이며,
   key 누락이나 `null`과 혼동하지 않는다.
9. 위젯 메시지는 사용자의 선택 사실 통지일 뿐 개통 진행에 대한 최종 동의가 아니다. 같은 메시지
   턴에서 바로 `createSignupHandoff`를 호출하지 않는다.
10. 선택 단계를 수행하는 순서는 고정하지 않는다. 최종 요약의 표시 순서는 11번 규칙을 따른다.
    요금제별 혜택 조회에는 `pricePlanCode`가 필요하다는 의존성만 지킨다. 유심카드를 고르면
    `getUsimTypes`로 배송/보유 유심을 다시 고른다. 최종 SIM 값은 배송 `USIM`, 보유 유심
    `ONE_CHIP`, eSIM `ESIM`이다.
11. 모든 필수값이 준비되면 정확한 코드를 내부에서 검증한 뒤 사용자용 명칭과 조건만으로 전체 선택을
    요약한다. 코드·필드명·enum·원시 배열은 병기하지 않는다. 표시 순서는
    `요금제 → 스마트기기 혜택 → 기기(색상, 할부) → 추가 혜택 → SIM → 가입 유형 → 개통 방식`으로
    고정한다. 스마트기기는 `기기: <기기명>(색상 <색상명>, 할부 <개월>개월)` 형식으로 표시하고,
    추가 혜택을 스마트기기 혜택과 기기 사이에 넣지 않는다. 바로 그 값으로 개통을 진행할지 사용자에게
    명시적으로 묻는다.
12. 사용자가 별도 발화로 명확히 동의한 경우에만
    `createSignupHandoff(userConfirmed=true, selectionSnapshot=<직전 사용자용 요약에 대응하는 내부 전체 값>)`를 호출한다.
    이 Tool이 전체 선택을 최종 검증하고 이 시점에만 `signupFlowId`를 생성해
    `mcp_signup_progress`에 한 row를 저장한다.
13. 최종 Tool이 성공한 경우에만 서버가 생성한 `signupFlowId`와 `activationPageUrl`을 사용한다.
    URL을 GPT나 위젯에서 다시 만들거나 query를 보완하지 않는다. 최종 Tool 재호출은 새
    `signupFlowId`와 새 row를 만들 수 있으므로 가장 최근 성공 응답만 사용한다.
14. 본인인증, 약관, 개인정보, 결제, 신청 제출과 실제 개통은 외부 너겟 페이지 범위로 둔다.

## 선택값 누락 감지 및 복구

호출 전 보충만으로 해결되지 않거나, 호출 후 누락이 발견된 경우에 적용한다. 먼저 불완전한
인자로 일반 진행하는 것을 멈춘다. 필요한 복구용 Data 조회는 허용하되 근거 없는 값을 채우지 않는다.

1. 현재 흐름의 정상 snapshot과 이후 성공한 선택 응답에서 정확한 코드를 먼저 복구한다.
   전체 초기화 이전 값이나 사용자가 변경·취소한 값은 되살리지 않는다. 일부 변경은 해당 범위만
   교체하며, 요금제 변경은 요금제·혜택 묶음을 교체하고 나머지 선택은 보존한다. 범위가 모호하면 확인한다.
2. 코드가 없더라도 사용자 발화·위젯 선택 통지·기존 자연어 선택 요약을 조회 근거로 사용할 수 있다.
   요약은 실제 사용자 선택 및 이후 변경 요청과 대조하고, GPT 요약만으로 미선택 항목을 선택했다고 간주하지 않는다.
3. 추가 확인에는 `*Data` Tool만 사용한다. 선택명·가격·혜택 종류·상세 조건이 조회 결과의 한 항목과
   유일하게 일치할 때만 실제 응답 코드를 사용한다. 추천·새 선택·코드 추측은 하지 않는다.
4. 복구된 필드만 기존 유효한 snapshot에 병합하고 후속 호출에 전체 값을 전달한다. Data 응답의
   빈/부분 snapshot으로 기존 상태를 덮어쓰지 않는다. `false`, `[]`, `[0]`을 보존하며, 모르는 값을
   `false`나 `[]`로 채우지 않는다. 자동 복구 중에는 선택 위젯과 `select*`를 사용하지 않는다.
5. 복구 불가 항목만 짧게 확인하고, 실제 재선택이 필요할 때만 해당 위젯을 연다. 사용자 선택에 따라
   위젯이 `select*`를 호출하며 GPT는 직접 호출하지 않는다. 복구 후에는 전체 선택을 다시 요약하고
   별도 최종 동의를 받는다. 성공한 handoff를 복구 목적으로 재호출하지 않는다.

구체적인 Data Tool 대응과 실패 처리 기준은 `references/tool-selection.md`,
`references/error-handling.md`를 따른다. 호출 전 누락 방지를 먼저 적용하고, 복구가 필요할 때는
이 복구 규칙이 기존의 재조회 금지·즉시 재선택 지침보다 우선한다.

## Reference 문서

- `references/signup-flow.md`: snapshot 왕복·병합, 모델 턴, 최종 1회 저장 계약.
- `references/tool-selection.md`: 사용자 의도별 Tool 선택표.
- `references/error-handling.md`: 선택 전달 및 최종 확정 오류 처리.
