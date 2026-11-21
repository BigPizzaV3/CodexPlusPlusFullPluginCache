---
name: self-compass
description: Explore life experiences through concrete scenes, evidence and counterexamples; review interpretations, correct records, pause and resume in English or Korean. Use for Self Compass conversations, not as a validated psychological test or a request for career recommendations.
---

<!-- Generated from program/self-compass.json · 0.3.0 · sha256:f60f773e9f694fce07bec142d9dbf230b7369f56b4854b726707421f45b74369 -->

# Self Compass 0.3.0

## Conversation flow

Follow the user's chosen language. When record tools are unavailable, read the chosen language reference: [program.en.json](references/program.en.json) for English or [program.json](references/program.json) for Korean. When tools are available, use get_program instead; do not read the same full program twice. Read and follow reviewStatus, rules, interviewPolicy and synthesisPolicy from that source. Both use the same question IDs and version. Never translate or rewrite stored responses, historical questions, corrections or evidence quotes when switching language. New questions can use the selected localization.

Start with SC01, one main question at a time. Select relevant scenes, explain the choice briefly, and follow interviewPolicy; do not impose all questions. Keep custom follow-ups, unsolicited experiences and multiple answers as separate records. Offer a synthesis when requested or sufficient, using synthesisPolicy. Distinguish observations, counterexamples, alternatives and unknowns; detailed roadmaps and actions are optional. Preserve original responses and correction history, mark only dependent claims and outputs for review, and ask about conflicts instead of overwriting.

Pause questions when asked. Resume from visible records and corrections without repeating answers or requiring files. Do not claim access to invisible history or long-term memory. Only when changing conversations, show the selected handover and privacy scope. JSON, IDs and revisions are internal, never a user task. Word and the local app are optional tools. A skill does not itself install an integration, run an AI analysis or save records. Actual account activation is separately unverified.

When record tools are available, first call get_resume with language en or ko and includeInterpretations:false for continuing questions. Read get_program once per version/language with questionIds:[nextQuestionId], or SC01 when absent. Fetch additional questions only when needed. Before synthesis, roadmap or correction, call get_resume with includeInterpretations:true and read all relevant original evidence. Use list_responses with excludeResponseIds from the resume and includeText:false to find older evidence, then read_response for verbatim text and corrections. Never infer omitted records from an index or replace evidence with summaries. Use questionId only for an actual prompt exactly matching get_program in the selected language, and include language and askedQuestion with that exact text in each bank add. For an adapted prompt, use question:{kind:followup,text:actual prompt} without questionId/askedQuestion; preserve it verbatim rather than replacing it or marking a bank question complete. Show the exact selected text and destination before asking permission to send a temporary save candidate. Final storage requires the confirmation screen's consent and a saved receipt; a prepared candidate is not saved. Never collect the whole conversation, bypass blocked requests or silently translate quotes. Read [session-contract.md](references/session-contract.md) for internal validation and exclusion rules.

This is a development draft, not a validated psychological test. The selected program source contains the mandatory limitations and safety rules; read them before proceeding.

## 한 대화의 진행

시작 요청을 받으면 program.json의 SC01로 이해하고 싶은 삶의 범위를 먼저 묻는다. 첫 응답에 보고서나 전체 설문을 제시하지 않는다. 필요한 영역을 실제 경험에 맞춰 고르고 선택 이유를 짧게 말한 뒤 한 번에 주요 질문 하나를 묻는다. 질문 은행은 선택 자료다. 맞춤 후속 질문의 실제 문장과 출처, 자발적인 추가 경험, 같은 질문의 여러 답변도 각각 보존한다. 등록되지 않았다는 이유로 경험을 버리지 않는다.

사용자가 충분하다고 하거나 정리를 요청하면 program.json의 interviewPolicy와 synthesisPolicy를 따라 핵심 종합을 제시한다. 근거 발언, 적용 범위, 반례·다른 설명, 미확인 부분을 구분하며 원응답을 해석으로 바꾸지 않는다. 자세한 로드맵과 행동은 선택이다. 내용의 타당성·저작권·전문가 효과를 자동 인증하지 않는다.

정정 요청은 어느 발언·해석을 바꾸는지 필요한 부분만 확인하고, 원응답과 이전 내용을 보존한다. 관련 해석·로드맵만 재확인 대상으로 표시하고 수정안을 사용자와 확인한다. 새로운 자료는 추가한다. 충돌하는 발언을 조용히 교체하지 않는다.

‘잠시 중단’에는 질문을 멈추고 다음에 이어갈 지점을 짧게 알려준다. 같은 대화에서 ‘이어서 하자’라고 하면 보이는 이전 기록과 정정에서 이어가고, 이미 답한 내용을 다시 쓰거나 파일을 주고받도록 요구하지 않는다. 보이지 않는 과거 대화·장기 기억을 복원했다고 주장하지 않는다. 새 대화로 옮기는 경우에만 필요한 기록을 사람이 읽을 수 있게 확인하고 사용자가 선택한 사본으로 이어간다. 전달하지 않을 경험과 이전 정정도 확인한다.

JSON·ID·버전·체크포인트 종류는 내부 구현 계약이다. 일반 사용자에게 JSON 작성·수정·형식 오류 해결을 맡기지 않는다. Word와 로컬 앱은 선택 도구이고 설치·npm 실행·반복 다운로드/업로드를 진행 조건으로 삼지 않는다. 실제 계정에 스킬이 설치·활성화된 것은 별도로 확인해야 한다.

질문·모듈·후속 질문·보고서의 같은 버전은 [program.json](references/program.json)에 있다. 필요한 영역만 읽고 질문을 실제 기록에 맞춰 선택한다. 재개·외부 초안의 내부 형식과 처리 규칙은 [session-contract.md](references/session-contract.md)를 읽는다. 스킬을 불러왔다고 앱이나 계정에서 자동 분석·저장·설치가 실행되지는 않는다.
