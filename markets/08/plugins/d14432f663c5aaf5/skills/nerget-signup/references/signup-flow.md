# Stateless 가입 선택과 최종 handoff

## 사용자용 표시와 내부 상태의 분리

이 문서의 코드·필드·JSON 예시는 Tool 입출력과 내부 검증을 위한 것으로 사용자용 응답 예시가 아니다.
`SKILL.md`의 필수 출력 제약을 우선 적용한다. 사용자에게는 확인된 상품명·혜택명·SIM 표시명·가입
유형·개통 방식과 가격·기간·색상·할부 조건만 요약하며, 내부 코드·필드명·enum·배열은 병기하지 않는다.
내부 snapshot은 원래 코드와 타입을 모두 보존하고, 사용자용 요약과 대응하는지 내부에서 대조한다.

## Selection snapshot

선택 중에는 `mcp_signup_progress` row와 `signupFlowId`가 없다. MCP 서버도 선택 상태를 Redis, DB,
HTTP 세션에 저장하지 않으며 상태 토큰을 발급하지 않는다. 선택 상태는 GPT 대화 컨텍스트에서
관리한다. 정상적인 전체 `selectionSnapshot`을 우선 사용하고, 이후 성공한 선택의 patch만 한 번씩
병합한다. 전체 snapshot에 이미 반영된 patch는 다시 조립하지 않는다.

snapshot의 필수 선택 필드는 다음과 같다.

- `pricePlanCode`
- `pricePlanName`
- `isMobileHomePlan`: `true | false`
- `deviceBenefitCodes`: `{code, colorCode, contractMonthCount}` 배열
- `benefitCodes`: 일반 혜택 코드 배열
- `giftCodes`: 숫자 사은품 코드 배열
- `simType`: `USIM | ONE_CHIP | ESIM`
- `joinType`: `NEW | MNP`
- `activationType`: `GENERAL | SELF_ACTIVATION`

최초 조회에는 snapshot을 생략하거나 빈 객체로 전달할 수 있다. snapshot은 위젯 호환을 위한
입출력 값이며 서버 가입 상태 저장본이 아니다.

일반 진행의 우선순위는 호출 전 누락 방지 → 호출 후 복구 → 복구 불가 항목만 사용자 확인이다.
호출 전 현재 유효한 기존 필드·값·타입이 전체 인자에 보존되는지 확인한다. `nextToolArguments`도
이 검사를 통과한 경우에만 그대로 사용한다. 사용자 변경·초기화는 해당 범위에만 반영하며 이전
인자로 되돌리지 않는다. 아직 미선택인 필드는 요구하지 않는다. 누락된 인자로 일반 진행하지 말고
정상 응답에서 먼저 보충한다. 추가 코드 확인이 필요한 복구용 `*Data`만 확인된 선택값을 전부
전달하는 조건으로 예외 허용한다. 응답이 상태를 유실하면 채택하지 않고 복구한다.

`select*`는 `_meta.ui.visibility=["app"]`인 위젯 전용 Tool이며 서버 저장 상태를 조회하지 않는다.
GPT는 직접 호출하지 않는다. 위젯 호출은 이번 선택 patch와 위젯 호환용 snapshot을 반환한다.

- `event=SIGNUP_SELECTION_UPDATED`
- `selectionPatch`: 이번 호출에서 반영한 값
- `selectionSnapshot`: 이번 patch까지 병합된 전체 선택
- `missingFields`, `readyForConfirmation` (호환용 안내값)

선택 성공 후 위젯은 표준 `ui/update-model-context`의 `structuredContent`와 `content` 텍스트 양쪽에
`selectionSnapshot`, `selectionPatch`, `missingFields`, `completedSteps`, `missingSteps`, `nextTool`,
`planBenefitComplete`을 정확히 전달한다. 이어지는 `ui/message`는 사용자가 읽을 짧은 문장만 담는다.
`planBenefitComplete=true`이면 `selectionSnapshot`을 최신 상태의 기준으로 사용하고, 사용자가
요금제·혜택 변경을 명시하지 않은 한 `getPricePlans`, `getPricePlansData`, `getBenefits`,
`getBenefitsData`를 다시 호출하지 않는다. 단, 기존 선택 코드의 복구를 위한 비노출 `*Data` 조회는
예외다. 일반 진행은 호출 전 검사를 통과한 `nextToolArguments`를 사용하며 다른 단계 조회에서도 전체 snapshot을
유지한다. 기존 선택 근거가 있는데 `planBenefitComplete=false`이거나 `missingFields`에 이미 선택한
항목이 나타나면 복구를 먼저 시도한다. 복구 불가 또는 실제 미선택 항목만 새로 선택하며 상세 절차는
`error-handling.md`를 따른다.

요금제나 혜택을 다시 선택하면 요금제와 세 혜택 배열 묶음을 새 값으로 교체하고 SIM·가입 유형·개통
방식은 보존한다. 선택 대상이 없는 혜택 배열은 `[]`로 전달한다. `selectPlanAndBenefit`은 선택값을
즉시 검증하지만 `select*`는 최종 가입 유효성을 확정하거나 `mcp_signup_progress`를 쓰지 않는다.
선택된 요금제의 `pricePlanName`과 `isMobileHomePlan`은 반드시 실제 값으로 전달하며, 세 혜택 배열은
선택 대상이 없을 때 `[]`일 수 있다.
모든 `@McpTool` 요청과 응답은 감사 목적인
`mcp_call_logs`에 기록되지만, 로그를 다음 선택 복원이나 완료 판단에 사용하지 않는다.

## 새 위젯 인스턴스와 모델 턴

각 `ui://` 화면은 새 인스턴스로 열릴 수 있으므로 위젯 로컬 메모리를 화면 간 상태 저장소로 사용하지
않는다. 선택 성공 후 위젯은 정확한 상태를 `ui/update-model-context`로 먼저 전달한 뒤 다음
`ui/message`를 한 번 보낸다.

`너겟 가입 위젯에서 <현재 선택명>을 선택했습니다. 요금제 가입을 계속 진행합니다.`

model context가 다음 모델 턴의 상태 기준이다. 호환 어댑터는 `setWidgetState`를 model context로
간주하지 않는다. 표준 기능을 사용할 수 없거나 갱신이 거절된 경우에만 위 짧은 메시지에 정확한 전체
snapshot, patch, 누락 필드와 다음 Tool을 담은 compact JSON을 붙여 fallback한다.
이는 위젯에서 모델로 전달하는 호환 입력이며, GPT는 이 JSON을 사용자용 응답에 복사하거나 덧붙이지 않는다.

`SIGNUP_SELECTION_UPDATED`를 받았다는 것은 해당 위젯이 이미 `select*` 응답을 반영했다는 뜻이다.
GPT는 같은 값뿐 아니라 어떤 `select*`도 다시 호출하지 않는다. 상태에 없는 항목이 있으면 기존 선택
근거를 확인해 필요한 `*Data` 조회로 먼저 복구한다. 실제 미선택 또는 복구 불가 항목에만 사용자
확인·선택을 요청한다. 모두 있으면
요금제·혜택·SIM·가입 유형·개통 방식의 코드를 내부에서 검증하고, 사용자용 명칭과 조건만 요약해 그 내용으로
진행할지 묻는다. 표시 순서는 `요금제 → 스마트기기 혜택 → 기기(색상, 할부) → 추가 혜택 →
SIM → 가입 유형 → 개통 방식`으로 유지하고, 추가 혜택을 스마트기기 혜택과 기기 사이에 넣지 않는다.
위젯 메시지 자체나 모호한 반응을 최종 동의로 해석하지 않는다.

## 최종 검증과 1회 저장

복구로 구성한 snapshot은 서버가 최종 검증한 상태가 아니다. 복구 후에는 전체 선택을 다시 요약하고
별도 명시적 동의를 받는다. 기존 handoff 성공 이력이 있으면 복구 목적으로 다시 생성하지 않는다.

사용자가 전체 선택을 확인한 뒤 별도 발화로 명시적으로 동의한 경우에만 다음 인자로
`createSignupHandoff`를 호출한다.

- `userConfirmed=true`
- `selectionSnapshot=<직전 사용자용 요약에 대응하는 내부 전체 snapshot>`

서버는 이 호출에서 요금제·혜택·SIM·가입 유형·개통 방식을 모두 최종 검증한다. 검증에 성공하면
이때만 `signupFlowId`를 생성하고 `mcp_signup_progress`에 한 row를 저장한다. 성공 URL에는
`gptEntryId={signupFlowId}`가 포함되므로 응답의 `activationPageUrl`을 그대로 사용한다.

최종 Tool을 다시 호출하면 새 row와 새 `signupFlowId`가 만들어질 수 있다. 따라서 외부 페이지
이동에는 가장 최근 성공 응답의 `activationPageUrl`만 사용한다.
