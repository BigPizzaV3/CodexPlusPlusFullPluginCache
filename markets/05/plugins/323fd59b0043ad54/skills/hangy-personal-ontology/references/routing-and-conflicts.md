# 전문 스킬 라우팅 및 충돌 규칙

## 라우팅 원칙

한 요청에 필요한 가장 좁은 전문 스킬을 선택한다. 이 온톨로지는 공통 행동을 정하고 전문 작업을 대신하지 않는다. 코어→전문 스킬은 단방향이며, 전문 스킬이 직접 선택된 경우 코어를 다시 호출하지 않고 자체 공통 불변조건을 따른다.

같은 대화에서 여러 스킬 활성화를 지원하지 않는 호스트에서는 선택된 스킬만 사용하고, 실행하지 않은 스킬을 사용했다고 주장하지 않는다.

| 요청 유형 | 우선 전문 스킬 | 핵심 결과 |
|---|---|---|
| 장기기억·망각 방지 복습 | `forgetting-prevention-review` | 자유회상 후 누락·왜곡만 재학습 |
| 자소서·지원동기·활동계획 | `hangy-application-essay-writer` | 검증된 사실 기반 제출용 글 또는 보완 안내 |
| 교수·수업 이메일 | `hangy-course-email-writer` | 제목부터 서명까지 복사 가능한 메일 |
| Figma 기반 PPT | `hangy-figma-ppt-workflow` | 편집 가능한 PPT와 전 슬라이드 QA 또는 정확한 대안 |
| Windows 앱·CLI 설치 | `hangy-install-and-verify` | 설치·실행·재실행 증거 |
| 한국 대학 입시 | `hangy-korean-admissions-consultant` | 사실 장부, 지원자격 게이트, 근거 있는 지원 조합 |
| 일반 한국어 작성·첨삭 | `hangy-natural-korean-document-editing` | 사실·의도·격식을 보존한 자연스러운 글 |
| 실제 문서 파일 수정 | `hangy-safe-document-edit` | 원본 보존 사본, 최소 diff, 재열기·렌더 QA |
| 여러 자료 기반 글쓰기 | `hangy-source-grounded-writing` | 출처 층이 분명한 즉시 사용 산출물 |
| 토큰·컨텍스트 절약 | `hangy-token-efficient-context` | 다른 작업을 대체하지 않는 효율화 overlay |
| 세로 숏폼 영상 | `hangy-viral-short-remotion` | 검증된 영상 또는 소스 기반 편집 청사진 |
| 대화·작업에서 스킬 추출 | `hangy-workflow-curator` | 비식별화한 반복 절차와 검증된 스킬 |
| 개념을 단계적으로 완전 이해 | `infinite-concept-explainer` | 비유→원리→적용→teach-back |
| 비공개 커플 기록 제품 설계 | `love-journal-design-report` | 구현 가능한 개인정보 중심 설계서 |
| MiriCanvas 디자인 수정 | `miricanvas-editor` | 범위 통제된 실제 편집과 시각 확인 |
| 설명 속 오개념 찾기 | `misconception-detection` | 질문을 통한 표현 실수·오개념 분리 |
| 일반 웹 자동화·테스트 | `playwright-cli` | 허용된 브라우저 실행 또는 테스트 계획 |
| 강의 자료 기반 15문제 시험 | `university-exam-practice` | 형식 확인→15문제→제출 후 채점 |
| 강의안 구조화·시험 대비 | `university-lecture-note-study` | 페이지 근거가 있는 개념 지도 |
| 녹음과 강의안 대조 | `university-lecture-recording-analysis` | 시간대별 추가 설명·강조·시험 신호 |

## 조합 순서

- **자료→글→파일**: `hangy-source-grounded-writing`으로 근거를 정리하고 해당 글쓰기 스킬로 내용을 만든 뒤, 실제 파일 수정이 승인되었을 때만 `hangy-safe-document-edit`로 반영한다.
- **자소서 파일 수정**: 내용 판단은 `hangy-application-essay-writer`, 문체 정리는 필요할 때 `hangy-natural-korean-document-editing`, 파일 작업은 마지막에 `hangy-safe-document-edit`가 맡는다.
- **교수 이메일 다듬기**: `hangy-course-email-writer`를 우선한다. 일반 문체 스킬은 사실·형식을 바꾸지 않는 보조 역할이다.
- **강의 학습 흐름**: 강의안 구조화 → 녹음 대조 → 시험 → 오개념 탐지 → 망각 방지 복습 순으로 이어질 수 있다. 사용자가 원하는 단계만 실행하고 뒤 단계를 자동으로 시작하지 않는다.
- **오개념 탐지와 개념 설명**: `내 설명에서 오개념을 찾아줘` 또는 `질문으로 스스로 발견하게 해줘`가 주목적이면 `misconception-detection`을 먼저 적용하고, 진단이 끝난 뒤에만 `infinite-concept-explainer`로 교정 설명한다. `가르쳐줘` 또는 `완전히 이해할 때까지 설명해줘`가 주목적이면 잘못된 주장이 포함되어 있어도 `infinite-concept-explainer`를 바로 적용한다. 둘 다 요청했으면 사용자가 지정한 순서를 따르고, 순서가 없으면 진단 후 설명으로 진행한다.
- **MiriCanvas 편집**: `miricanvas-editor`가 변경 범위와 검증을 결정한다. `playwright-cli`는 허용된 호스트에서 하위 실행 수단일 뿐이며 쿠키·로컬 저장소·인증정보를 추출하지 않는다.
- **토큰 절약**: `hangy-token-efficient-context`는 입력과 도구 출력을 줄이는 overlay다. 결과를 책임지는 전문 스킬의 사실성·QA를 생략하지 않는다.
- **워크플로우 추출**: 사용자가 스킬화나 온톨로지 갱신을 요청했을 때만 `hangy-workflow-curator`를 사용한다. 작업 원문이나 개인정보를 새 스킬에 복사하지 않는다.

## 충돌 해결

- 내용 정확성과 파일 안전이 충돌하면 먼저 정확한 내용을 확정하고 사본에 반영한다.
- 자연스러운 문체와 사실 보존이 충돌하면 사실 보존을 우선한다.
- 간결성과 필수 근거·안전 경계가 충돌하면 필수 근거와 경계를 남긴다.
- 자동 실행과 호스트·권한 한계가 충돌하면 실행을 멈추고 가능한 부분과 미완료 부분을 구분한다.
- 전문 스킬의 도메인별 개수·순서·QA 규칙은 온톨로지의 일반 기본값보다 우선한다.
- 현재 사용자 요청이 저장된 선호와 다르면 사실·개인정보·안전 경계를 통과한 현재 요청을 따른다.

## 일반 fallback

정확히 맞는 전문 스킬이 없으면 이 온톨로지의 응답·근거·개인정보·완료 규칙만 적용해 작업한다. 억지로 유사 스킬을 끼워 넣지 않는다. 필요한 기능이 외부 연결이나 로컬 런타임에 의존하면 현재 능력을 확인한 뒤 가능한 대안만 제시한다.
