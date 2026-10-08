# AAC Card Maker

`aac-card-maker`는 학생의 시각 프로필에 맞춘 AAC 그림과 편집 가능한 A4 인쇄용 HTML을 만드는 플러그인입니다. `create-aac-cards` 스킬이 프로필 선택, 이미지 프롬프트, 업로드 이미지 대체 흐름과 HTML 생성을 안내합니다.

## ChatGPT에서 사용하기

공개 승인을 받은 뒤에는 ChatGPT의 앱/플러그인 디렉터리에서 `AAC Card Maker`를 검색해 추가하면 됩니다. 일반 사용자는 이 저장소를 복제하거나 GitHub 마켓플레이스를 등록할 필요가 없습니다.

이 패키지는 외부 서버 없이 동작하는 `skills-only` 플러그인입니다. 공개 ChatGPT 환경에서는 이미지 생성 기능이 없을 때 로컬 Windows 경로를 입력하지 말고 PNG, JPG, GIF, WebP 또는 SVG 이미지를 업로드해 주세요. 호스트가 휴대용 파일/코드 실행을 제공하면 `scripts/build-aac-html.py`를 사용하고, HTML이 생성된 경우에만 다운로드 가능한 결과를 보고합니다.

프로필은 현재 세션 또는 호스트가 제공하는 작업공간 범위에서만 유지됩니다. 이 패키지는 사용자 간 또는 대화 간 프로필 저장 서버를 제공하지 않습니다.

## 개발자: 공개 제출 및 업데이트

이 저장소는 플러그인의 소스와 로컬 테스트용 패키지를 제공합니다. GitHub 저장소나 `.agents/plugins/marketplace.json`에 등록하는 것만으로 ChatGPT 공개 등록이 완료되지는 않습니다. 개발자는 OpenAI Platform의 [플러그인 제출 포털](https://developers.openai.com/plugins/deploy/submission)에서 `Skills only`로 제출하고, 검수 승인 후 Publish해야 합니다.

제출 시 사용할 자료는 다음과 같습니다.

- [개인정보처리방침](../../docs/public/privacy-policy.md)
- [이용약관](../../docs/public/terms-of-use.md)
- [지원 안내](../../docs/public/support.md)
- [제출용 시작 프롬프트](../../docs/submission/starter-prompts.md)
- [검수 테스트 케이스](../../docs/submission/test-cases.md)
- [릴리스 노트](../../docs/submission/release-notes.md)

## 개발자·테스트: Codex에서 GitHub로 설치

이 방법은 공개 ChatGPT 사용자를 위한 설치가 아니라, 개발자가 GitHub의 최신 소스를 Codex에서 직접 테스트할 때 사용합니다. Codex CLI에서 이 저장소를 플러그인 마켓플레이스로 등록합니다.

```text
codex plugin marketplace add jch4825/AACplugin --ref main
```

그다음 Codex를 실행해 `/plugins`를 입력하고 `Personal` 마켓플레이스에서 `aac-card-maker`를 설치합니다. Codex 데스크톱 앱에서는 앱을 다시 시작한 후 Plugins 화면에서 같은 플러그인을 설치합니다. 설치 후 새 작업을 시작해야 스킬이 활성화됩니다.

사용 예시:

```text
create-aac-cards 스킬을 사용해서 "물 마시기", "화장실", "쉬는 시간" AAC 카드를 만들어 줘.
기본 프로필을 사용하고 한 페이지에 카드 4개를 배치해 줘.
```

Codex 플러그인 설치와 마켓플레이스 구조는 [Codex Plugins](https://developers.openai.com/codex/plugins/)와 [Build plugins](https://developers.openai.com/codex/plugins/build)에서 확인할 수 있습니다.

## 개발자·테스트: Google Antigravity에서 설치

Antigravity는 이 저장소의 Codex 전용 `.codex-plugin/plugin.json`을 직접 설치하지 않습니다. 대신 플러그인에 포함된 `create-aac-cards` 폴더를 Agent Skill로 사용합니다.

먼저 저장소를 복제합니다.

```powershell
git clone https://github.com/jch4825/AACplugin.git
```

프로젝트 하나에서만 사용하려면 스킬 폴더를 해당 프로젝트의 `.agents/skills/` 아래에 복사합니다.

```powershell
New-Item -ItemType Directory -Force .\.agents\skills | Out-Null
Copy-Item -Recurse -Force `
  .\AACplugin\plugins\aac-card-maker\skills\create-aac-cards `
  .\.agents\skills\create-aac-cards
```

여러 프로젝트에서 공통으로 사용하려면 같은 폴더를 사용자 전역 경로인 `~/.gemini/config/skills/create-aac-cards`에 복사할 수 있습니다.

Antigravity에서 다음과 같이 요청합니다. HTML 빌더를 실행할 때는 복제한 저장소의 스크립트 경로를 함께 알려 줍니다.

```text
create-aac-cards 스킬을 사용해서 "도와주세요"와 "잠시 쉬고 싶어요" 카드를 만들어 줘.
AACplugin 저장소는 C:\경로\AACplugin에 있고 HTML 빌더는
C:\경로\AACplugin\plugins\aac-card-maker\scripts\build-aac-html.ps1에 있어.
```

Antigravity의 스킬 검색 위치와 플러그인 형식은 [Antigravity Skills](https://antigravity.google/docs/skills?app=antigravity-ide)와 [Antigravity Plugins](https://www.antigravity.google/docs/plugins)에서 확인할 수 있습니다.

## 수동으로 HTML 생성

플러그인 루트에서 카드 JSON과 출력 경로를 지정해 휴대용 Python 빌더를 실행합니다.

```powershell
python scripts/build-aac-html.py --InputJson examples/sample-cards.json --OutputHtml examples/sample-aac-cards.html
```

Windows/Codex 환경에서 Python 실행이 제공되지 않을 때는 기존 PowerShell 빌더를 사용할 수 있습니다.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build-aac-html.ps1 -InputJson examples/sample-cards.json -OutputHtml examples/sample-aac-cards.html
```

결과 HTML은 별도 서버 없이 열립니다. 그림 교체, 문구 수정, 카드 추가·복제·삭제·순서 변경, 페이지당 1·2·4·8개 배치, HTML 저장과 브라우저 인쇄를 지원합니다.

- `전체 글자 크기` 슬라이더는 모든 카드 문구를 한 번에 12~72px 범위에서 변경합니다.
- 편집 모드에서 `전체 글꼴`을 바꾸면 카드 전체의 기본 글꼴이 변경됩니다.
- 카드별 편집 도구에서 글꼴과 글자 크기를 따로 지정할 수 있으며, 값을 비우거나 `기본값`을 누르면 전체 설정을 따릅니다.
- `전체 카드에 적용`은 카드별 글꼴·크기 예외를 지우고 현재 전체 설정을 모든 카드의 기준으로 사용합니다.
- 편집 모드에서 그림을 더블 클릭하면 파란 테두리와 네 모서리 조절점이 나타납니다.
- 그림 본체를 드래그하면 위치가 바뀌고, 모서리를 드래그하면 비율을 유지하며 확대·축소됩니다.
- 카드의 그림 영역을 벗어난 부분은 잘리며, 글자 크기·위치·배율은 `HTML 저장` 결과에 유지됩니다.
- 선택 테두리와 조절점은 인쇄되지 않습니다.

Codex/Windows 사용에는 PowerShell 5.1 이상과 최신 Chrome 또는 Edge가 필요할 수 있습니다. ChatGPT 사용에는 호스트가 제공하는 파일 업로드 및 휴대용 코드 실행 기능을 사용합니다. Node.js, npm, 웹 서버, 데이터베이스, 외부 JavaScript 라이브러리, 별도 OpenAI API 키, 별도 PDF 프로그램은 필요하지 않습니다. 이미지 생성 기능과 브라우저의 PDF 저장은 선택 사항입니다.

## 개인정보와 파일 보호

- 학생 프로필에는 실명 대신 가명을 사용합니다.
- 진단명이나 의료정보를 기본 질문으로 수집하지 않습니다.
- 이미지와 결과물은 로컬 경로에서 처리합니다.
- 기존 프로필이나 HTML을 자동으로 덮어쓰지 않습니다.

## 예제

`examples/sample-cards.json`과 `examples/images/`에는 비식별 SVG 예시가 포함되어 있습니다. `examples/sample-aac-cards.html`을 브라우저에서 열어 전체 편집 흐름을 확인할 수 있습니다.
