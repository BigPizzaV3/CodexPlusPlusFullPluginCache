---
name: baceline-match-posts
description: Find a tennis partner through Baceline match posts or prepare a public match post with a confirmed preview. Use for 친구찾기 조회·생성, find a playing partner, or 練習相手募集; not adding a friend or reserving a court.
---

# 친구찾기 모집글 조회와 생성

조회와 새 글 생성을 사용자 의도에 맞게 구분한다. 조회 요청만으로 모집글을 만들지 않는다. 기존 공개 글 지원 종목은 현재 schema의 tennis/pickleball/badminton을 따르며 테니스 대회 운영 규칙을 다른 종목에 적용하지 않는다.

## 조회

`search_match_posts`에 요청한 종목·지역·날짜·상태를 전달하고 서버가 허용한 공개 범위만 읽는다. 목록은 모집 상태이며 코트 예약이나 참가 확정이 아니다. next_cursor가 있으면 현재 범위를 명시한다. 최종 view_id로 `render_baceline_results`를 한 번 호출한다.

## 생성

1. `ask_match_post_questions`로 서버가 요구하는 다음 질문을 확인한다. 기존 답을 유지하며 날짜·시간, 경기 방식, 모집 인원, 수준·비용과 코트 예약 여부를 확인한다.
2. 위치는 사용자가 제공한 검증된 주소·좌표 또는 서버에서 받은 location_id를 사용한다. 시설명만으로 좌표를 만들지 않는다. has_court_reserved를 근거 없이 true로 넣지 않는다. 테니스의 game_format을 다른 종목의 규칙으로 해석하지 않는다. 해당 종목에 입력 의미를 확인할 수 없으면 생성 대신 지원 범위를 안내한다.
3. `preview_match_post`로 공개 게시 내용과 한국 시간 일정을 확인하고 `render_baceline_results`로 표시한다. 공개 글이 되는 점을 분명히 알린다. 수정하면 새 preview를 만든다.
4. 사용자가 카드의 게시 버튼을 누르면 앱 전용 도구가 저장한다. 모델은 `publish_match_post`를 직접 호출하거나 preview_token을 공개하지 않는다. 실제 저장 결과가 없으면 게시 완료로 안내하지 않는다. 실패나 응답 유실 뒤 새 글을 중복 생성하지 않는다.

모든 질문·오류·카드 표시 언어는 사용자 ko/en/ja에 맞춘다. 현재 render schema가 locale을 지원할 때만 locale 인자를 전달한다. 원문 이름·장소·작성 내용을 임의 번역하지 않는다. 인증은 호스트 연결 흐름으로 처리하고 비밀번호와 OTP를 받지 않는다. 다른 계정으로 게시하거나 친구 요청, 예약, 참가 신청이나 결제가 완료됐다고 설명하지 않는다.

예: “토요일 테니스 친구찾기 글 찾아줘”, “Help me post a tennis partner request”, “テニスの練習相手を募集したい”.
