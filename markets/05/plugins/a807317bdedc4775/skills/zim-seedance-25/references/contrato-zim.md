# Seedance 2.5: superfície de escrita e superfície de execução

Verificação de integração: 19/09/2026. Os limites vivos da plataforma prevalecem sobre este retrato.

## Interface do Zim

O estúdio declara modos de texto, primeiro/último quadro, múltiplas referências, edição e extensão. No retrato consultado, geração nova oferece 4–30 segundos, resoluções 480p/720p/1080p e referências por modalidade. Multi-referência admite até 30 imagens, 10 vídeos e 10 áudios; vídeo e áudio possuem também limites de duração somada. Confirme a validação do modo antes de executar.

Os tokens da interface são `@imageN`, `@videoN` e `@audioN`. Só mencione tokens vinculados a arquivos reais, na ordem correta. O adaptador pode traduzir nomes e sintaxe para o fornecedor: o usuário não deve ter de gerenciar essa tradução.

## MCP atual

`gerar_video` é geração nova e usa a chave de motor `seedance25`. Seu esquema atual recebe prompt, referências de imagem, duração, resolução, proporção e imagem inicial; não aceita automaticamente todos os campos multimodais presentes na interface.

Para edição de vídeo existente, use a porta `editar_video` e seu planejamento/cotação. Para funções específicas, consulte Clone, Mirage e Ângulos. Não invente campo de vídeo de entrada em `gerar_video`. Para extensão, primeiro descubra se a conexão expõe uma ferramenta compatível; a existência do modo no site não prova existência no MCP.

O prompt de `gerar_video` tem limite de 4.000 caracteres no esquema consultado. Compacte a direção sem perder a ação e os vínculos de referência; não corte texto literal ou invariantes ao acaso. Não copie um limite de outro canal para esta ferramenta.

## Fonte técnica consultada

A documentação primária da rota de referência Seedance 2.5 confirma campos separados para imagens, vídeos e áudios, seleção do tipo de tarefa, duração, resolução e áudio: https://docs.crun.ai/models/seedance/2-5/reference-to-video . Isso descreve essa rota do fornecedor, não uma garantia de que todo cliente Zim exponha os mesmos campos.

Não envie chaves, nomes de canais internos ou custos de fornecedor no prompt ou na resposta ao cliente. Use a API do Zim e a cotação da conta.
