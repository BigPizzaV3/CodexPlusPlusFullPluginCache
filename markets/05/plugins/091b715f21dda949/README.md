# Gestão Ágil 2.0 — habilidades e plug-in

Este repositório distribui 30 habilidades do Gestão Ágil 2.0 em um único plug-in e
mantém os instaladores por pasta para ambientes compatíveis.

O plug-in é somente de habilidades: não inclui MCP, Apps, Actions, conectores nem
autenticação externa.

## Plug-in Gestão Ágil 2.0

O aluno instala o plug-in uma vez e usa as habilidades dentro do Projeto do seu
caso real. O conteúdo está organizado pedagogicamente em seis trilhas:

1. Diagnóstico e A3;
2. Estratégia e objetivos;
3. Iniciativas e ciclos;
4. Operação e fluxo;
5. Melhoria e inovação;
6. Liderança e times.

A relação completa entre trilhas e habilidades está em [docs/TRILHAS.md](docs/TRILHAS.md).

No ChatGPT, digite `@` e escolha o plug-in ou uma habilidade. No Codex, cite uma
habilidade com `$`, como `$ga2-relatorio-a3`. Também é possível pedir o resultado
em linguagem comum e deixar o ambiente selecionar a habilidade adequada.

> Status: publicado no diretório público de plug-ins. A versão atual está indicada em
> [VERSION](VERSION).

Para gerar o arquivo de distribuição:

```bash
python3 scripts/empacotar_plugin.py
```

Os dez casos de validação e regressão estão em
[tests/plugin-submission-cases.json](tests/plugin-submission-cases.json). O roteiro
de piloto e publicação está em [docs/PUBLICACAO.md](docs/PUBLICACAO.md).

## Instalação das habilidades por pasta

O pacote também funciona com Claude, Codex, Cursor, OpenCode e ambientes que leem
pastas no formato `SKILL.md`.

## O que uma habilidade faz

Uma habilidade ensina o assistente a aplicar uma parte do método. Por exemplo:

- montar um A3;
- encontrar a causa raiz;
- criar um OKR;
- organizar um Kanban;
- conduzir uma revisão ou retrospectiva;
- explicar uma situação com um artefato HTML.

As habilidades usam português simples. Todo termo técnico aparece com uma explicação curta.

### macOS ou Linux

Instalar em todos os ambientes conhecidos:

```bash
./instalar.sh --todos
```

Instalar em um ambiente específico:

```bash
./instalar.sh --claude
./instalar.sh --codex
./instalar.sh --cursor
./instalar.sh --opencode
./instalar.sh --agents
```

Instalar em uma pasta escolhida:

```bash
./instalar.sh --destino /caminho/para/skills
```

### Windows

Abra o PowerShell nesta pasta e execute:

```powershell
.\instalar.ps1 -Todos
```

Também existem as opções `-Claude`, `-Codex`, `-Cursor`, `-OpenCode`, `-Agents`
e `-Destino "C:\caminho\skills"`.

### Atualizar

Baixe a versão nova e rode o instalador outra vez. O instalador guarda a versão anterior
em `.ga2-backup` antes de substituir qualquer skill.

## Usar as habilidades

Depois de instalar, reinicie o assistente. Peça pela tarefa em linguagem comum:

```text
Monta um A3 para este problema.
Me mostra onde este fluxo trava.
Organiza estas ações em um plano com dono e data.
```

O ambiente decide qual skill usar. Você também pode citar o nome, como `$ga2-relatorio-a3`.

## Ambientes com artefato visual

`ga2-me-mostra` sempre gera HTML.

- Claude usa Artifact quando esse recurso estiver disponível.
- Codex e GPT usam o artefato ou a visualização disponível na sessão.
- Cursor usa sua visualização ou prévia disponível.
- Outros ambientes usam o recurso equivalente.
- Sem recurso visual, a skill salva o HTML e mostra um resumo no terminal ou no chat.

O recurso disponível no ambiente prevalece sobre o nome do modelo.

## Conteúdo e privacidade

O pacote não contém credenciais, caminhos de servidores, dados de alunos ou rotinas internas
da MindMaster. Os exemplos usam situações didáticas.

## Versão

A versão atual está em [VERSION](VERSION). A integridade dos arquivos está registrada em
`SHA256SUMS.txt`.
