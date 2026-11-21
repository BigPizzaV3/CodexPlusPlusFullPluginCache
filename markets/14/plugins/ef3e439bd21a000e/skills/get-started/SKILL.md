---
name: get-started
description: 세계로 네개로(3or4) 연결 뒤 처음 쓰는 법 — ChatGPT가 짠 일정 점검하기, 내 계획으로 저장하기, 계획 보고 고치기
---

# 세계로 네개로 시작하기

1. 회원이 일정을 짜 달라고 하거나 일정을 붙여 넣고 점검해 달라고 하면, 가는 날·돌아오는 날을 확인한 뒤 회원이 좋다고 하면 `create_plan_draft`로 내 계획에 저장한다(items에 day·name·time). 결과의 확인할 것(최대 3줄: 쉬는 날·여는 시각, 마지막 날 공항 가는 막차, 다녀온 여행자의 비추, 숙소 없는 밤)을 먼저 말하고 고칠 방법을 제안한다.
2. 회원이 저장해 달라고 하면 날짜별 일정을 `create_plan_draft` 한 번으로 저장한다(3or4 로그인 필요). 결과의 「내 계획 열기: 주소」와 확인할 것(최대 3줄)을 답 끝에 그대로 적는다. 못 찾은 장소 이름(not_found_names)은 저장되지 않았다고 알려 준다.
3. 저장된 계획은 `list_my_plans`·`get_plan`으로 열어 날짜별로 요약하고, 확인할 것과 열기 주소를 함께 보여 준다.
4. 고칠 때는 바꿀 내용을 먼저 보여 주고, 회원이 좋다고 하면 한 가지씩 고친다: 넣기 `add_place`, 시간·메모 `update_place`, 다른 날로 `move_place`, 빼기 `remove_place`, 도시 `set_place_city`, 숙소 `set_stay`, 제목·날짜 `update_plan_info`.
5. 도시의 회원 비추·조심할 곳은 `city_cautions`, 장소 하나의 후기는 `place_details`, 장소 찾기는 `search_places`로 본다. 3or4에 자료가 없는 도시는 없다고 말하고 후기를 지어내지 않는다.
