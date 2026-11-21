<!-- Generated from program/self-compass.json · 0.3.0 · sha256:f60f773e9f694fce07bec142d9dbf230b7369f56b4854b726707421f45b74369 -->
# 재개와 초안 계약

스키마 self-compass.session.v1, programVersion 0.3.0. sessionId와 baseRevision은 현재 체크포인트와 정확히 같아야 한다. 다른 대화의 파일이나 오래된 초안은 반영하지 않는다. 앱 없이 대화할 때도 실제 발언만 원응답으로 기록하고, 확인되지 않은 기억을 보충하지 않는다.

체크포인트 필수 항목: schemaVersion, programVersion, sessionId, baseRevision, stage(scope/explore/synthesis/review/paused), resumeStage(중단 전 단계), scope, stop, responses, claims, outputs, heldQuestionIds, nextQuestionId, unresolved, analysisPerformed:false, corrections. 중단은 stage:paused/stop:true/nextQuestionId:null로 남긴다. 재개는 사용자 요청 뒤 resumeStage에서 시작하며 이미 답함·모름·건너뜀·제외·보류한 질문을 강요하지 않는다.

질문 은행의 questionId와 실제 기록 id를 분리한다. 같은 질문의 여러 응답은 서로 다른 id로 보존한다. 은행 밖 맞춤 후속 질문·자발 경험에는 questionId:conversation:<고유값>, question:{kind:followup/experience,text:실제 질문,source:질문 출처}를 기록한다. 등록된 질문만 기록하도록 제한하지 않는다. 미지의 근거 참조는 거부하고 실제 저장된 응답 id만 참조한다. 질문·출처·원응답·정정 이력·버전을 내부에서 검증한다. ChatGPT 저장 후보에서 등록 질문의 답변을 추가할 때는 questionId, language, askedQuestion(실제로 물은 문장)을 함께 보내며 해당 언어의 등록 원문과 정확히 같아야 한다. 문장을 바꿨다면 question:{kind:followup,text:실제 질문}으로 보내고 questionId/askedQuestion은 보내지 않는다. 질문 원문이나 버전 검증을 제거하거나 등록 원문으로 바꿔 제출하지 않는다.

응답: id, questionId, source, raw(첫 발언), current(현재 발언), revision, status(blank/unknown/skipped/excluded/answered), history:[{revision,current,status,reason}]. 근거: responseId, revision, quote(해당 current의 정확한 부분 문자열). 주장: id, text, origin(external_draft/user_authored), support[], counter[], scope, alternatives[], unknowns[], review(unreviewed/accepted/edited/rejected/uncertain), stale, revision, history:[{revision,text,review}]. 보고서/로드맵: id, kind(report/option/action), text, claimIds[], refs[], held, stale. 정정: targetId, kind(response/claim/exclusion), reason, atRevision.

외부 초안은 아래 claims/outputs 필드만 제안한다. 원응답을 수정하는 초안은 만들지 않는다. 앱은 출처 external_draft/검토 unreviewed/초기 revision 1과 빈 이력을 붙인다. 선언된 사용자 수용이나 인증은 신뢰하지 않는다. 중복·미지 ID·깨진 참조·제외/이전 revision·틀린 인용을 거부한다. 로컬에서는 검증→미리보기→선택 반영이며 의존 해석도 함께 선택한다. 대화에서도 반영할 항목을 사용자와 확인한다. 세션 baseRevision을 변경할 때마다 올려 오래된 초안을 구분한다.

원응답 정정은 revision을 올리고 이전 값을 보존한다. 해석 정정/거절은 원응답을 고치지 않는다. 연결 주장·출력만 stale로 표시하고 확인 전 현재 결과로 제시하지 않는다. 새 버전 근거를 다시 확인한 수정 해석은 새 ID로 제안하여 옛 주장을 보존한다. 충분하면 핵심 종합 후 종료하며 미확인 상세를 채우지 않는다.

제외 응답은 전달용에서 ID/questionId/revision/status:excluded와 빈 raw/current/history, source:excluded 자리표시자만 남긴다. 맞춤 질문 메타데이터의 원문·출처도 전달 제외로 비운다. 해당 응답의 지지/반례를 쓰는 주장과 연결 출력은 생략한다. 제외 자료가 섞일 수 있는 scope/unresolved/정정 자유문도 비운다. 다른 응답의 재언급은 미리보기에서 확인한다. 로컬 전체 백업에는 원문·이력이 남는다. 외부 사본은 자동 삭제되지 않는다.

아래는 실제 사람과 무관한 유효 예시다. 사용자의 실제 세션 ID·버전·근거로 교체하며 예시 문장을 개인 근거로 쓰지 않는다. 초안 1MiB, 체크포인트 2MiB 이하. 스키마·참조 통과는 해석의 진실성·권리·전문가 효과 인증이 아니다.

## 체크포인트 예시

```json
{
  "schemaVersion": "self-compass.session.v1",
  "programVersion": "0.3.0",
  "sessionId": "fictional-session-001",
  "baseRevision": 2,
  "stage": "explore",
  "resumeStage": "explore",
  "scope": "삶의 일상 이해",
  "stop": false,
  "responses": [
    {
      "id": "SC01",
      "questionId": "SC01",
      "source": "conversation",
      "raw": "삶의 일상 이해",
      "current": "삶의 일상 이해",
      "revision": 1,
      "status": "answered",
      "history": []
    }
  ],
  "claims": [],
  "outputs": [],
  "heldQuestionIds": [],
  "nextQuestionId": "SC02",
  "unresolved": [],
  "analysisPerformed": false,
  "corrections": [
    {
      "targetId": "SC01",
      "kind": "response",
      "reason": "사용자 기록",
      "atRevision": 2
    }
  ]
}
```

## 외부 초안 예시

```json
{
  "schemaVersion": "self-compass.draft.v1",
  "programVersion": "0.3.0",
  "sessionId": "fictional-session-001",
  "baseRevision": 2,
  "claims": [
    {
      "id": "C1",
      "text": "현재 범위는 삶의 일상 이해다.",
      "support": [
        {
          "responseId": "SC01",
          "revision": 1,
          "quote": "삶의 일상 이해"
        }
      ],
      "counter": [],
      "scope": "현재 대화 목표",
      "alternatives": [
        "나중에 범위가 바뀔 수 있음"
      ],
      "unknowns": [
        "실제 장면은 아직 없음"
      ]
    }
  ],
  "outputs": [
    {
      "id": "O1",
      "kind": "report",
      "text": "현재 목표를 확인했다. 개인적 패턴은 아직 미확인이다.",
      "claimIds": [
        "C1"
      ],
      "refs": [],
      "held": false
    }
  ]
}
```
