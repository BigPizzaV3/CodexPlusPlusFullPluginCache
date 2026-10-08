# 선택적 비공개 개인 캡슐 스키마

## 경계

이 파일은 **형식만 제공하는 공개 템플릿**이다. 실제 개인 캡슐은 플러그인, 공개 ZIP, 공개 저장소에 넣지 않는다. 새 계정의 사용자가 직접 제공한 값만 검증해 현재 대화의 `session` 범위에서 적용한다. 이 공개 스킬은 영구 저장 수단을 제공하거나 보장하지 않는다.

## 허용 스키마

```yaml
capsule_version: "1.0"
owner_assertion: "user-supplied; not identity-verified"
default_scope: "session"
preferences:
  - id: "pref-example-001"
    category: "language" # language | tone | detail | format | workflow | capability
    instruction: "Korean requests should receive natural Korean answers."
    trigger: "when the request is written in Korean"
    scope: "session"
    confidence: "confirmed" # confirmed | provisional
    provenance_type: "explicit-user-statement"
    sensitivity: "public-behavior" # public-behavior | private-low-risk
    portability: "portable"
    last_confirmed: "YYYY-MM-DD"
    expires_at: null
capabilities:
  windows_host: "unknown" # available | unavailable | unknown
  hancom_available: "unknown"
  local_shell_available: "unknown"
  ipad_client: "unknown"
style_examples:
  - id: "style-example-001"
    text: "[DE-IDENTIFIED SHORT EXAMPLE]"
    contains_personal_facts: false
excluded_categories_acknowledged:
  - "credentials"
  - "direct-identifiers"
  - "third-party-records"
  - "private-documents-and-urls"
  - "local-paths-and-device-identifiers"
```

## 검증 규칙

1. 필드가 허용 목록에 있는지 확인한다. 알 수 없는 필드는 적용하지 않고 사용자에게 돌려준다.
2. 각 선호는 한 문장 행동 규칙이어야 하며 개인 전기나 사건 기록이 아니어야 한다.
3. `provenance_type`은 `explicit-user-statement`, `user-approved-summary`, `de-identified-example` 중 하나만 허용한다.
4. 기본 범위와 실제 적용 범위는 모두 `session`이다. 이 스킬은 `project`나 `profile` 저장을 완료했다고 주장하지 않는다.
5. 모든 항목의 실제 적용 범위는 `session`이어야 한다. 재사용하려면 사용자가 다음 대화에 캡슐을 다시 제공하거나 자신이 직접 통제하는 플랫폼 기능을 별도로 사용해야 한다.
6. 기기 정보는 세부 사양·경로가 아니라 `available`, `unavailable`, `unknown` 능력 플래그만 허용한다.
7. 문체 예시는 짧고 익명화되어야 하며 이름, 기관, 과목, 날짜, 연락처, 링크, 제3자 사실을 포함하지 않는다.
8. `privacy-boundaries.md`의 절대 제외 항목이 하나라도 있으면 해당 항목을 제거하고 캡슐을 적용하지 않는다.
9. 서로 충돌하면 먼저 사실·개인정보·안전·무결성 경계를 적용하고, 그 안에서 현재 요청과 명시적 확인을 우선한다. 최근 확인일은 같은 provenance와 confidence를 가진 항목끼리만 보조 기준으로 사용한다.

## 적용과 삭제

- 캡슐을 적용할 때 어떤 범위에서 몇 개 규칙을 사용했는지만 알려줄 수 있다. 민감한 원문을 반복 출력하지 않는다.
- 사용자가 캡슐을 삭제하거나 무시하라고 하면 즉시 현재 작업에서 제외한다.
- 캡슐을 자동으로 외부 서비스, 파일, 다른 대화, 공개 온톨로지로 복사하지 않는다.
- 공개 플러그인이 이전 계정의 캡슐을 알고 있거나 복구할 수 있다고 주장하지 않는다.
