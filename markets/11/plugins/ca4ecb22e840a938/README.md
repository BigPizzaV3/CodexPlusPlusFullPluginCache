# ChatGPT 플러그인 패키지

OpenAI 플러그인 심사에 올리는 ZIP의 원본이다. 대시보드에서 내려받은 제출본을 기준으로 삼고, 문서가 요구하는 구조로 맞췄다.

```
plugin/
├── plugin.json     패키지 메타데이터 (루트)
├── mcp.json        MCP 서버 연결 (루트)
├── REVIEW.md       심사용 테스트 케이스
└── assets/
    ├── icon.png    composerIcon
    └── logo.png    logo
```

대시보드 제출본은 `.codex-plugin/plugin.json` 한 파일뿐이었다. 그 경로는 문서상 호환용 대체 경로이고, 정식 위치는 루트의 `plugin.json`이다. MCP 서버 연결(`mcp.json`)도 빠져 있었다.

## 업로드

`plugin.json`과 `mcp.json`이 압축 루트에 있어야 한다.

```bash
cd plugin && zip -r ../chyeon-plugin.zip . -x '.*'
```

## 바꿀 때 주의

- `name`은 바꾸지 않는다. 대시보드가 발급한 패키지 식별자다.
- 기능이나 문구를 바꾸면 `version`을 올린다.
- MCP 서버 코드만 고치는 변경은 ZIP을 다시 올릴 필요가 없다. 배포 후 재스캔을 요청하면 된다.
- `mcp.json`의 url이 운영 주소인지 확인한다. 알파 주소로 제출하면 반려된다.
