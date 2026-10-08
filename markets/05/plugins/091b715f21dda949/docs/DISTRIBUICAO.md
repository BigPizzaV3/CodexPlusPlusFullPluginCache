# Distribuição para alunos — decisões e caminhos

Documento interno. O guia do aluno é `INSTALACAO-ALUNO.md`.

## Publicar não é obrigatório

Publicar em diretório público (o roteiro de `PUBLICACAO.md`) é uma decisão de
marketing, não um requisito técnico. Exige identidade de desenvolvedor verificada,
repositório público, casos de teste e revisão externa.

Nada disso é necessário para entregar o kit a aluno pago. Os caminhos abaixo não
passam por revisão de ninguém.

## Caminhos por ambiente

| Ambiente | Artefato | Esforço do aluno | Aprovação |
|---|---|---|---|
| Claude — app de computador | `dist/gestao-agil-2.plugin` | arrastar e clicar | nenhuma |
| Claude — navegador | `dist/skills-claude-web/*.zip` | 1 upload por habilidade | nenhuma |
| ChatGPT | link dos 6 GPTs | abrir o link | nenhuma |
| Claude Code / Codex / Cursor | `instalar.sh` / `instalar.ps1` | rodar um comando | nenhuma |
| Marketplace no GitHub | `.claude-plugin/marketplace.json` | 1 comando no terminal | nenhuma |

## O gargalo do navegador

No claude.ai o aluno sobe um `.zip` por habilidade. Trinta uploads é barreira real
para gestor não técnico. Duas saídas:

1. Recortar por trilha. Entregar 5 ou 6 habilidades por módulo do curso, no momento
   em que cada trilha começa. O aluno instala pouco e usa o que instalou.
2. Empurrar o aluno para o aplicativo de computador, onde o `.plugin` resolve em
   um clique, e tratar o navegador como exceção.

## Marketplace no GitHub

Serve aluno que usa terminal. O comando é `/plugin marketplace add` apontando para
o repositório, seguido de `/plugin install gestao-agil-2@mindmaster`.

Decisão pendente antes de divulgar: repositório público significa que qualquer
pessoa instala as 30 habilidades do curso pago sem comprar. Repositório privado
protege o conteúdo, mas obriga o aluno a ter conta no GitHub com acesso concedido,
o que reintroduz atrito justamente com quem se quer proteger.

Enquanto isso não for decidido, distribua por arquivo: `.plugin` e `.zip` são
entregues por área de membros, e o controle de acesso fica na plataforma do curso,
não no GitHub.

## Atualização de versão

Ao mudar qualquer habilidade:

1. Suba o número em `VERSION` e em `.claude-plugin/plugin.json`.
2. Rode `python3 scripts/atualizar_checksums.py`.
3. Gere de novo o `.plugin` e os `.zip` da pasta `dist/`.
4. Republique na área de membros e avise a turma.

Quem instalou por arquivo não recebe atualização automática. Quem instalou por
marketplace recebe. É a diferença prática entre os dois caminhos.
