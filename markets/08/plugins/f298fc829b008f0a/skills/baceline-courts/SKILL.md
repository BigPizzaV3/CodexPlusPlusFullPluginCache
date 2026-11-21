---
name: baceline-courts
description: Find Baceline courts and compare actual available times and court fees. Use for 코트 조회, 오늘 예약 가능한 테니스장, available courts, or 空きコート; not tournament group court assignment.
---

# 코트와 예약 가능한 시간 찾기

1. 오늘이나 내일 가능한 코트를 비교하려면 `search_available_courts`를 우선 호출한다. 시설 정보만 찾으면 `search_courts`, 특정 코트의 시간을 확인하면 `get_court_availability`를 사용한다. 대회 조별 코트 배정과 혼동하지 않는다.
2. 종목은 요청한 tennis 또는 pickleball을 사용한다. 지역은 이번 요청에 명시한 경우만 region_text로 보내고 미지정이면 생략한다. 저장된 위치로 추정하거나 빈 결과 뒤 다른 지역으로 바꾸지 않는다. 현재 검색이 지원하지 않는 badminton을 tennis로 바꾸지 않는다.
3. 날짜 생략은 서버가 정하는 Asia/Seoul 오늘, 이용시간 생략은 1시간이다. 현재 도구가 허용하는 날짜와 이용시간 범위를 따른다. 코트별 최소시간이 다르므로 모두 2시간 단위라고 안내하지 않는다.
4. 시설 미디어와 각 가용 시간, court_subtotal 및 조회 시각을 읽는다. 요일·시간별 실제 요금이 포함된 반환값을 사용하며 기본가격으로 덮거나 수수료 포함 최종 결제액으로 설명하지 않는다. 사진이 없거나 미디어 로딩이 실패한 것을 코트 조회 실패로 해석하지 않는다.
5. view_id로 `render_baceline_results`를 한 번 호출해 비교 화면을 표시한다. 현재 schema가 지원하면 locale을 사용자의 ko/en/ja로 유지한다. 선택한 시간의 예약은 서버가 반환한 공식 앱 링크에서 다시 확인하도록 안내한다.

next_offset가 있으면 현재 페이지 범위를 명시한다. 정보 전용 시설을 예약 가능으로 표시하지 않는다. partial, 최소시간 미달, 빈 시간, 오류, 미확인 가격 및 만료를 구분한다. 만료 결과는 다시 조회한다. 이 도구는 코트를 예약하거나 결제하지 않으며 가용 시간은 예약 보장이 아니다.

예: “오늘 예약 가능한 테니스장”, “Find a court for two hours tomorrow”, “今日空いているテニスコート”.
