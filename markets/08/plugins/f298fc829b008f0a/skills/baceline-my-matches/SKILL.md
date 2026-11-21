---
name: baceline-my-matches
description: Read the connected user's Baceline match records, partners, opponents and scores. Use for 내 경기 기록, my matches, or 自分の試合記録; not another person's records or unsupported career statistics.
---

# 내 경기 기록

1. `get_my_match_results`를 호출한다. 대회명이나 ID, 기간과 페이지 조건은 사용자가 요청한 것만 전달한다. 본인은 OAuth 연결로 서버가 정하며 profile ID, 이메일이나 이름으로 계정을 바꾸지 않는다.
2. 연결이나 scope가 필요하면 호스트의 계정 연결 안내를 따른다. 비밀번호와 OTP를 채팅으로 받거나 심사 계정으로 바꾸지 않는다. UNAUTHORIZED를 기록 없음으로 바꾸지 않는다.
3. 일반 경기의 파트너·상대와 단체전 팀 명단, games의 실제 출전 슬롯을 구분한다. 현재 팀 명단을 실제 출전으로 추정하지 않는다. 서버가 미확정으로 반환한 점수·승패·날짜는 그대로 구분한다. 기록된 시작·종료 시각이 없는 소요 시간을 만들지 않는다.
4. view_id로 `render_baceline_results`를 한 번 호출한다. 현재 정의가 지원하면 locale을 사용자 ko/en/ja로 유지한다. 원본 이름·점수·대회명은 바꾸지 않는다.

현재 범위는 서버가 반환하는 본인의 공개 대회 경기 기록이다. next_cursor가 있으면 전체 기록이 아니며 다음 페이지는 같은 조건으로 조회한다. 날짜 없는 경기 요청은 date_mode=undated를 사용하고 기간을 추정하지 않는다. 첫 페이지나 일부 공개 경기로 전체 커리어 승률을 만들지 않는다. 종목 필터 등 현재 schema에 없는 인자를 추가하지 않는다. 종목별 통계 시각화나 신청·결제 내역 도구가 없으면 아직 지원하지 않는다고 안내한다.

예: “내 복식 경기 기록 보여줘”, “Show my latest match scores”, “自分の試合結果を見せて”. 친구 경기 요청은 본인 조회로 바꾸지 말고 승인된 친구 조회 절차를 사용한다.
