---
name: zim-seedance-25
description: "Prepare prompts e planos para Seedance 2.5 no Zim, com referências por papel, beats, câmera, áudio e validação do contrato real de execução."
---

# Zim · Seedance 2.5

Use especificamente para Seedance 2.5. Não substitua por uma versão 2.0, outro modelo ou outro canal sem uma escolha explícita. Reconheça `/seedance-25` e `/seedance-2.5` como intenções textuais.

## Escolha a tarefa primeiro

Diferencie geração nova, primeiro/último quadro, múltiplas referências, edição e extensão. Leia [contrato do Zim](references/contrato-zim.md) para distinguir as capacidades da interface das ferramentas MCP. Um vídeo existente que deve ser alterado não é texto para `gerar_video`.

Para escrever apenas um prompt, não execute ferramentas pagas. Para gerar, consulte os schemas/catálogos atuais e a cotação da operação final. Preserve modelo, duração, resolução e referências aprovadas. Não inclua parâmetros técnicos na prosa como se eles configurassem o arquivo.

## Compile um pedido legível

Use [estrutura do prompt](references/estrutura.md). Cada prompt precisa funcionar sozinho: referências reais e seus papéis, acontecimento, primeiro estado, câmera, luz, beats, atuação, áudio e último estado. Omita seções irrelevantes. Não acrescente detalhes para preencher cabeçalhos.

Use os tokens que a superfície atual suporta e que correspondem à ordem real dos arquivos. Não invente tags para fotos ausentes. Referência de identidade, figurino, produto, local, performance e som são papéis diferentes. Uma referência não deve contaminar os atributos controlados por outra.

Escolha uma ação central e uma linguagem de câmera coerente. Se houver vários cortes, declare-os e distribua tempo; não peça simultaneamente plano contínuo e montagem de múltiplos planos. Preserve fala e texto de cena literalmente no idioma aprovado.

Leia [física, continuidade e revisão](references/revisao.md) para cenas com objetos, mãos, deslocamentos ou mudanças de enquadramento. Use [exemplos](references/exemplos.md) para calibrar o nível de detalhe.

## Forma de entrega

Se o pedido é por prompt: entregue o prompt pronto, os parâmetros separados e o mapa de referências quando existir. Se precisa de uma decisão, destaque só a decisão pendente. Use inglês técnico para a direção quando adequado à rota; preserve português em diálogo e textos aprovados. Não traduza automaticamente para chinês por suposição de desempenho; o adaptador do servidor cuida de adequações específicas do canal.

Se o pedido é por execução: passe a proposta à ferramenta compatível, cote e execute somente com autorização suficiente. O resultado em processamento deve ser acompanhado pelo ID; não regere por timeout. Verifique arquivo, referências, duração e qualidade visual antes de afirmar conclusão artística.

Instruções explícitas do usuário prevalecem sobre defaults editoriais. Prompt não garante identidade, grafia, física ou sincronização; revise o resultado e altere a variável que causou o problema.
