# 행동 온톨로지 스키마

## 목적

온톨로지는 개인 전기를 저장하는 데이터베이스가 아니라, 반복해서 검증된 작업 행동을 추적 가능한 규칙과 관계로 표현하는 원장이다. 공개층은 특정인을 식별하지 않는 규칙만 담고, 선택적 개인 캡슐은 사용자가 새 계정에서 별도로 제공한다.

## 노드 형식

```yaml
- id: "B001"
  type: "behavior_rule"
  statement: "Lead with the outcome."
  trigger: "always"
  scope: "public"
  provenance: "user-approved recurring pattern"
  confidence: "high"
  sensitivity: "public-behavior"
  portability: "portable"
  last_reviewed: "YYYY-MM-DD"
  override_rule: "current explicit user request wins among compatible preferences; verified facts, privacy, safety, integrity, and domain invariants remain gates"
  verifies_with:
    - "response starts with the result"
```

필수 필드는 `id`, `type`, `statement`, `trigger`, `scope`, `provenance`, `confidence`, `sensitivity`, `portability`, `last_reviewed`, `override_rule`이다.

허용 `type`:

- `behavior_rule`: 응답 방식과 상호작용
- `evidence_rule`: 사실, 출처, 불확실성 처리
- `workflow`: 여러 단계의 작업 순서
- `qa_gate`: 완료 전 검증 조건
- `privacy_boundary`: 저장·출력·전송 금지 경계
- `routing_rule`: 요청과 전문 스킬 연결
- `capability_rule`: 호스트·도구 조건
- `integrity_rule`: 조작·우회·허위 완료 방지

## 관계 형식

```yaml
- from: "D001"
  relation: "precedes"
  to: "D002"
```

허용 관계:

- `precedes`: 먼저 수행해야 함
- `requires`: 통과 또는 존재가 필요함
- `routes_to`: 전문 스킬로 연결함
- `overrides`: 충돌 시 우선함
- `verifies`: 다른 규칙의 수행 여부를 검사함
- `excludes`: 함께 적용할 수 없음
- `supports`: 보조 행동임

## 승격·변경 규칙

1. 서로 다른 작업에서 반복 관찰되거나 사용자가 명시적으로 승인한 행동만 공개 노드 후보가 된다.
2. 단일 대화의 사건 사실, 이름, 기관, 일정, 제3자 정보는 규칙으로 승격하지 않는다.
3. 관찰된 선호와 설계자가 제안한 개선을 `provenance`로 구분한다.
4. 개인정보 스캔, 상충 검사, 대표 시나리오 평가를 통과한 뒤에만 `public-ontology.yaml`을 바꾼다.
5. 규칙을 바꾸면 `last_reviewed`와 관련 평가 사례를 함께 갱신한다.
6. 삭제는 해당 노드를 참조하는 관계와 라우팅을 먼저 확인한 뒤 수행한다.

## 정확성 경계

온톨로지 항목이 존재한다고 해서 모든 모델·호스트·도구에서 같은 문장을 생성하는 것은 아니다. 평가 대상은 명시된 행동과 금지 조건의 충족 여부다. 계정 기억, 워크스페이스 정책, 연결 권한, 개인 파일은 노드로 가장하거나 복제하지 않는다.
