# Adaptação Verifica VRA 2.4.0 para ChatGPT

Origem: pacote `verifica-vra_gemini_google_docs_v2_4_0.zip` recebido do usuário em 27/10/2026. Mantidos, sem revalidar o mérito, a skill VRA original 2.4.0, schema e contrato de análise, modelo de relatório, fixtures e suíte de testes.

## Mudanças
- Manifesto Agent Plugins 1.0 e `SKILL.md` portável em `skills/verifica-vra`.
- Adaptação explícita de P0/P1, formatos e criação/verificação de Google Doc nativo por conector autorizado.
- Fallback para relatório integral editável em Markdown quando não houver escrita em Docs.
- Gerador de segmentos imprime instruções para ChatGPT e preserva indicadores de leitura `NOT_VERIFIED`.
- Mantido o texto original Gemini em `references/historico/SKILL_original_gemini_v2_4_0.md`.

## Limites de validação
Testes de fonte/script são testes locais e não comprovam auditoria documental real, Google Docs criado, fidelidade de registros em 441 páginas ou independência do validador. Requer teste de aceitação operacional com VRA preenchida e autos reais sob controle institucional.
