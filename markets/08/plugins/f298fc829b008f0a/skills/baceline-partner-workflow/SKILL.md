---
name: baceline-partner-workflow
description: Guide a Baceline partner through the tennis Tour lifecycle from creation to registration, seeding, group draw, group courts and bracket operations, executing only exposed authorized tools. Use for 대회 전체 운영, manage my Tour workflow, or 大会運営; not ordinary public event search.
---

# 파트너 테니스 대회 전체 흐름

사용자가 어느 단계에 있는지 확인하고 그 단계부터 이어 간다. 대회 생성, 참가 접수와 결제 확인, 시드 생성, 조편성, 조별 경기장·코트, 본선 대진표 설정, 경기 진행 및 정산을 서로 구분한다. 단계 순서 자체가 권한이나 실행 승인은 아니다. 현재 지원 범위는 [기능 연결표](references/capabilities.md)를 읽는다.

현재 운영 대상은 테니스다. 대회의 sport_type과 단식·복식·단체전 tournament_type은 다른 축이다. 배드민턴과 피클볼의 운영 규칙을 테니스로 대체하지 않는다. 대회 이름만으로 종목이나 관리 권한을 추정하지 않는다.

1. 대회 생성 단계는 `ask_tournament_questions`로 실제 역할과 scope를 먼저 확인한다. 기존 draft 답을 유지하고 서버 next_question을 묻는다. 필요하면 `attach_tournament_image`, 준비 후 `preview_tournament_event`를 호출한다. 최종 view_id를 `render_baceline_results`로 표시한다. 최종 생성은 사용자가 카드 버튼을 누를 때만 앱이 처리한다. 모델이 `create_tournament_event`를 직접 호출하지 않는다.
2. 기존 대회 운영 요청은 현재 노출된 관리 도구와 정확한 대회 권한을 확인한다. 공개 `search_tournaments`/`get_tournament` 결과를 담당 대회의 비공개 운영 정보로 사용하지 않는다. 관리 도구가 없으면 “현재 이 단계는 ChatGPT에서 실행할 수 없음”을 안내하고 서버가 반환한 공식 관리 링크가 있을 때 연결한다. 경로와 대회 ID를 추정해서 링크를 만들지 않는다.
3. 실제 관리 도구가 제공된 단계에서만 해당 입력과 결과 계약을 따른다. 시드와 조편성은 최종 팀 배치, 조별 코트는 조에 연결할 대회 코트, 본선 설정은 bracket_setup의 설정을 각각 미리 보여줘야 한다. “이렇게 만들까요?” 확인 뒤 보인 결과를 저장하는 지원 경로만 사용한다. 조별 코트 배정은 시설 예약이나 개별 경기 시간표가 아니다.
4. 참가 확정, 팀 등록과 PG 결제 완료는 서로 다른 사실이다. 실제 결제 조회 도구가 없으면 납부 여부를 판단하지 않는다. 정원은 팀 단위로 읽고, 확인되지 않은 결제액·시드·진출·조 배치를 만들지 않는다.
5. 저장은 도구가 반환한 실제 영수증과 재조회 결과로 확인한다. 잠금, 원천 변경과 만료를 우회하거나 자동으로 기존 조·경기를 삭제하지 않는다. 미구현 단계는 완료로 올리지 않는다.

연결 만료·scope 부족과 파트너 자격 부족을 구분한다. PARTNER_REQUIRED에 재연결을 반복시키지 않는다. 비밀번호·OTP·PG key를 채팅에 받지 않는다. UI와 설명은 같은 ko/en/ja 언어를 유지하고 원본 이름·요강·금액은 바꾸지 않는다. 현재 schema가 지원할 때 locale을 전달한다.

예: “내 테니스 대회를 만들고 접수부터 조편성과 코트 배정까지 운영하고 싶어”, “Guide my tennis Tour operations”, “テニス大会の作成から運営まで進めたい”. 스킬 등록 자체는 아직 연결되지 않은 운영 기능의 구현이나 공개를 뜻하지 않는다.
