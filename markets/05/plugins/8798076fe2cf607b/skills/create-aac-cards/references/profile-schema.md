# Student profile schema

When the host provides writable profile storage, store one UTF-8 Markdown file per pseudonym within the current session or workspace. Otherwise keep the profile in the current conversation and do not promise persistence across chats. Use a filesystem-safe alias for the filename and never request a real name, diagnosis, age, or medical history by default.

## Fields

| Field | Question | Default |
|---|---|---|
| `alias` | 사용할 가명을 알려 주세요. | A new filesystem-safe pseudonym is required. |
| `visual_style` | 어떤 그림 형태를 잘 알아보나요? | 사실적이지만 단순한 삽화 |
| `visual_complexity` | 어느 정도의 시각적 복잡도를 처리할 수 있나요? | 핵심 대상 하나와 최소 배경 |
| `concept_range` | 어떤 범위의 개념을 이해하나요? | 구체적인 사물과 행동 |
| `sensory_constraints` | 피해야 할 색·무늬·감각 요소가 있나요? | 고대비·번쩍임·복잡한 무늬 피하기 |
| `card_size_constraints` | 카드 크기나 배치에 필요한 조건이 있나요? | A4 페이지당 4장 |

Ask one question at a time. Accept `Unknown` or `모름` for any field except `alias`; retain that response in the file and apply the default while generating cards.

## File format

```markdown
---
alias: sample-student
visual_style: 사실적이지만 단순한 삽화
visual_complexity: 핵심 대상 하나와 최소 배경
concept_range: 구체적인 사물과 행동
sensory_constraints: 고대비·번쩍임·복잡한 무늬 피하기
card_size_constraints: A4 페이지당 4장
---
```

Before saving, confirm the target does not exist. If it exists, ask for a new alias or an explicit overwrite decision.
