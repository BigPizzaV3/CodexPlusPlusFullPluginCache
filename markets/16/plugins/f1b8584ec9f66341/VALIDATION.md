# Validação da release 1.1.3

**Origem:** `diggia-assistente-gestao-projetos-v1.1.2-lge-2.10.2(1).zip` (fornecido pelo usuário)

| Checagem | Resultado |
|---|---|
| Integridade CRC do ZIP de origem | PASS |
| Identidade e nova versão semântica | PASS — `diggia-assistente-gestao-projetos` / `1.1.3` |
| `defaultPrompt` preservado byte a byte como string Unicode | PASS |
| `review.prompts` alinhado ao defaultPrompt | PASS |
| Sete Skills e referências: conteúdo inalterado | PASS |
| Frontmatter das Skills, incluindo identificadores | PASS |
| JSON e JSONL com parse válido | PASS |
| YAML de referências e casos com parse válido | PASS |
| Ícone PNG quadrado, tamanho e caminho | PASS |
| Nome e descrições dentro dos limites de listagem | PASS |
| ZIP com diretório raiz único | PASS |
| Testes comportamentais (14 casos descritos) | NOT_RUN |
| Compatibilidade funcional em ChatGPT | NOT_VERIFIED |
| Aceitação pelo Developer Portal / revisão pública | NOT_VERIFIED |

**Escopo:** atualização documental do manifesto e metadados de release; não foi modificado o comportamento das sete Skills. Os campos do `plugin.json` que não dizem respeito a esta atualização foram preservados, incluindo categoria, recursos, endpoints e identidade. Nenhum teste de runtime é inferido a partir de verificações estáticas.
