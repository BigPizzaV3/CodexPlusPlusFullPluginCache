# Ficha de submissão — Diretório de plug-ins da Anthropic

Status: pronta para envio. Ainda não submetida.

Envio em https://platform.claude.com/plugins/submit (qualquer conta Console serve;
não exige Team ou Enterprise). Quem tem Team ou Enterprise também pode enviar pelo
admin do claude.ai.

## Tipo

Somente habilidades. Sem MCP, sem hooks, sem agentes, sem autenticação externa.

## Informações públicas

- Nome: Gestão Ágil 2.0
- Identificador: `gestao-agil-2`
- Desenvolvedor: MindMaster Treinamentos
- Categoria: Productivity (confirmar a lista oferecida no formulário)
- Repositório: https://github.com/Mindmaster-code/gestao-agil-skills
- Site: https://mindmaster.com.br/
- Suporte: https://github.com/Mindmaster-code/gestao-agil-skills/issues
- Privacidade: https://github.com/Mindmaster-code/gestao-agil-skills/blob/main/PRIVACY.md
- Termos: https://github.com/Mindmaster-code/gestao-agil-skills/blob/main/TERMS.md
- Licença: uso pessoal, profissional interno e educacional liberado; revenda e
  redistribuição exigem autorização. Texto em `LICENSE.md`.

## Descrição curta

Trinta habilidades para aplicar o método Gestão Ágil 2.0 a um caso real da sua empresa.

## Descrição longa

Gestão Ágil 2.0 traz o método usado por gestores brasileiros fora de TI para
diagnosticar problemas, conectar objetivos e iniciativas, organizar o fluxo de
trabalho, conduzir ciclos e desenvolver o time.

Cada habilidade cobre uma parte do método: Relatório A3, causa raiz, OKR Canvas,
Backlog 2D, Kanban Canvas, plano do ciclo, retrospectiva, PDCA, POP, quadro de
delegação, PDI, entre outras. Uma delas, "me mostra", transforma qualquer situação
de gestão em um artefato visual em HTML.

Tudo em português simples. Termo técnico sempre acompanhado de explicação curta.
Você descreve a situação em linguagem comum e o método é aplicado ao seu contexto,
não a um exemplo genérico.

## Prompts de exemplo

1. Nossa entrega no prazo caiu de 82% para 61% em oito semanas. Monta um Relatório A3.
2. Tenho 14 iniciativas e 6 pessoas. Me ajuda a priorizar e montar o próximo ciclo.
3. Me mostra visualmente onde este processo trava e qual decisão ele pede.

## Verificação antes do envio

Rodar na pasta do repositório, no terminal da sua máquina. São dois comandos,
não um:

```bash
claude plugin validate .claude-plugin/marketplace.json
claude plugin validate .claude-plugin/plugin.json
```

Atenção: `claude plugin validate .` sozinho valida apenas o marketplace. Como os
dois manifestos moram na mesma pasta, o validador trata o diretório como
marketplace e não olha o plugin. Aponte para cada arquivo.

Conferência manual já realizada, com 0 erros e 0 avisos:

- `plugin.json` é JSON válido e tem o campo `name`
- `name` em kebab-case e `version` em semver
- nenhum campo desconhecido no manifesto
- caminho de habilidades sem escape de pasta
- 30 habilidades, todas com `SKILL.md`
- todas com `name` e `description` no frontmatter
- `LICENSE.md`, `README.md`, `SUPPORT.md`, `PRIVACY.md` e `TERMS.md` presentes

## O que a Anthropic exige

- Repositório público. Atendido: o repositório é público.
- Canal de suporte e contato. Atendido: issues do repositório, descrito em `SUPPORT.md`.
- Política de privacidade quando há coleta de dados. Não se aplica: o plug-in não
  coleta nem envia dados. `PRIVACY.md` registra isso.
- Conformidade com a política de uso da Anthropic.

## Depois do envio

- Triagem automática roda em todo envio e em toda atualização.
- O selo "Anthropic Verified" é revisão manual adicional e opcional. A documentação
  não garante concessão.
- O prazo de análise não é publicado. A documentação diz apenas que varia com a fila.
- Publicado o plug-in, cada commit no repositório propaga sozinho. Não é preciso
  reenviar o formulário.
- Suba `version` no `plugin.json` a cada alteração relevante, senão o aluno não
  recebe a atualização.
- A Anthropic reserva o direito de remover um plug-in do diretório. O processo para
  o autor pedir despublicação não está documentado.

## Idioma da listagem

Decidido: português.

O diretório é global e uma listagem em português alcança menos gente do que uma em
inglês. A escolha é deliberada: o público do método é o gestor brasileiro fora de TI,
e as habilidades respondem em português. Uma listagem em inglês traria instalações de
quem não é o público e não converte.

Consequência prática: os campos `description` do manifesto e do marketplace estão em
português com acentuação correta, e a descrição enviada no formulário segue o mesmo
idioma.

Se mais adiante fizer sentido alcançar fora do Brasil, o caminho é traduzir as
habilidades primeiro e a listagem depois, nunca o contrário.

## Decisões em aberto

- Se vale publicar o kit completo ou um recorte de entrada, mantendo o kit inteiro
  como entrega do curso. Ver `DISTRIBUICAO.md`.
