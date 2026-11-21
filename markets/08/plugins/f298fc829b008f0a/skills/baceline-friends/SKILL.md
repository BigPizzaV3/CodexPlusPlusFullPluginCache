---
name: baceline-friends
description: List the connected user's approved Baceline friends and read a selected friend's public match records. Use for 내 친구 목록, friend results, or 友達の試合結果; not arbitrary people search or creating friend requests.
---

# 친구와 친구 경기

1. 친구 목록 요청은 `get_my_friends`를 호출한다. 특정 친구 경기 요청도 아직 승인된 친구를 식별하지 못했다면 먼저 이 목록을 사용한다. 이름으로 식별할 때 next_cursor가 남으면 다음 페이지도 확인하며, 첫 페이지의 한 명을 유일한 후보로 단정하지 않는다. 전체 범위를 확인하지 못하면 현재 조회 범위를 알리고 사용자가 표시된 후보를 선택하게 한다. 동명이인은 반환된 후보 중 사용자에게 선택받는다.
2. 승인된 목록에서 선택한 실제 ID만 `get_friend_match_results`의 friend_profile_id로 전달한다. 사용자 이름을 UUID로 만들거나 임의 계정 ID를 넣지 않는다. 서버 권한 검사가 최종 판단이다. 친구 ID는 도구 입력에만 쓰고 불필요하게 답변에 노출하지 않는다.
3. 결과는 선택한 친구 기준이다. 친구의 승패를 본인의 승패로 바꾸지 않는다. 단체전 명단과 실제 출전 슬롯, 미확정 점수와 날짜를 구분한다. next_cursor는 같은 친구와 필터로만 이어 간다.
4. view_id로 `render_baceline_results`를 한 번 호출한다. 지원되는 locale을 사용자의 ko/en/ja로 유지하며 원본 이름과 점수는 바꾸지 않는다.

연결이 필요하면 호스트 인증 흐름을 따른다. 차단·삭제 계정이나 승인되지 않은 사람의 기록은 우회 조회하지 않는다. 빈 결과와 조회 실패를 구분한다. 친구 추가·요청 전송 도구는 현재 없으므로 수행했다고 말하지 않는다. 새 경기 파트너를 찾는 요청은 친구찾기 모집글 검색·생성 절차와 구분한다.

예: “내 친구의 최근 경기”, “Show my friend's match results”, “友達の最近の試合を見せて”.
