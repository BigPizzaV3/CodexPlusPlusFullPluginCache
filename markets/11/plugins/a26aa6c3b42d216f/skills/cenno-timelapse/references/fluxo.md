# Fluxo de domínio — Timelapse R06

Aplicar com 00_CENNO_COMUM.md e as adaptações de SKILL.md.

# Cenno | Timelapse R06 — 10 shots / 9 takes

## Missão e contagem fixa
Use só 07_TIMELAPSE_KNOWLEDGE.md R06. Autoria: evento final→desmontagem→pátio livre. FIXAR 10 SHOTS / 9 TAKES. S01 é imagem original; gerar no máximo 9 novos estados previstos. SHOT=imagem; TAKE=transição entre duas imagens consecutivas. Só pedido explícito do usuário muda total.

## Sequência única
S01 evento completo, iluminado, público e telas conforme referência.
S02 telões apagados, cerca de 50% do público inicial permanece; toda cenografia/estrutura intacta, iluminação ambiente/operacional suficiente.
S03 público zero; cenografia/estruturas completas; entram staff/EPI, caminhões, cases/carrinhos e logística.
S04 toda cenografia maior E leve retirada em todas as zonas; lonas removidas; estruturas expostas 100%. Equipamentos/telas dependentes retirados antes de seus suportes.
S05 estruturas restantes 75%; S06 50%; S07 25%; S08 0% de estruturas montadas, ainda com peças/cases/equipes/veículos.
S09 cases/carga retirados; últimos trabalhadores fazem limpeza/toques finais e saída.
S10 pátio livre, sem temporários/pessoas/equipamentos/veículos do evento. Preservar permanentes.
25% aplica-se APENAS às estruturas expostas de S04, quatro retiradas até zero. Não aplicar quartos à cenografia, lonas, técnica ou a cada zona separadamente. Palco, entrada, FOH/house mix e tendas progridem juntos nos mesmos shots, sem desaparecer inteiros por descuido. 

## Conversa, prompt e geração
Desde o início, usar o idioma do usuário; prompts integrais em inglês. Uma pergunta/assunto por mensagem; opções NUMERADAS em linhas separadas, última descrição livre. Reusar decisões, não reiniciar etapas. Analisar imagem final e propor tabela fixa com passagem de tempo; resolver só ambiguidade material.
Depois de CADA prompt de imagem perguntar: “Quer gerar esta imagem aqui no chat?” 1 Sim, gerar aqui; 2 Não, só o prompt e continuar; 3 Ajustar antes; 4 Prefiro descrever. Renderizar alternativas em linhas separadas e aguardar. Não gerar próxima automaticamente após aprovação anterior.
MODO CHAT: escolher 1 → gerar/conferir/apresentar → perguntar SEMPRE “Esta imagem está aprovada?” com opções 1 Aprovada; 2 Corrigir; 3 Prefiro descrever. Esperar aceite antes de próxima geração. Rejeição corrige só esse shot e depois pede aceite novamente. Só imagem aprovada vira pai real. 
MODO SÓ PROMPTS: opção 2 ou pedido explícito permite continuar texto/lote sem upload/aceite externo nem repetir convite de geração. Registrar resultado externo não verificado; não dizer imagem aprovada nem perguntar aceite do que não viu. Não gerar mídia.

## Herança e honestidade
FINAL_REFERENCE é original. No chat, editar pai aprovado; fora, prompt usa resultado externo anterior esperado, sem fingir que foi visto ou bloquear redação. Nomes sugeridos não são arquivos recebidos. Para voltar a gerar no chat, obter pai real.
Registrar ID/versão/pai real ou esperado, arquivo/status, zonas/logística/tempo. Corrigir dependentes nas mesmas 10 posições. 

## Trabalho e preservação
Separar permanente de temporário. Travar câmera/posição/lente/crop/perspectiva/horizonte/formato; sem zoom/pan/tilt/voo automáticos. 
S03–S08: equipes com coletes/EPI, caminhões, cases e logística por zona. Na animação, peças grandes chegam em caminhão e são içadas por caminhão-guindaste/Munck ou grua, com sustentação visível; equipe posiciona/fixa antes de soltar. Pequenas peças são levadas por pessoas/carrinhos. Nada se monta sozinho: origem→transporte→içamento apoiado→posicionamento→fixação→liberação. Suporte antes da carga; lona depois da armação. Sem travessias, morphing ou flutuação. S09 equipe residual; S10 vazio.
CONTINUIDADE entre takes: registrar cada veículo/equipamento/carga por identidade visual, posição/orientação, trajeto, estado e ação pendente. Mesmo arquivo/versão do shot é End de um e Start do seguinte. Caminhão só entra/sai por trajeto visível; não some, muda aparência ou reaparece em outro lugar no corte. Cargas/equipes/cases permanecem até ação de instalação/transporte/saída. Repetir estado de continuidade nos dois prompts adjacentes. Rever primeiros/últimos quadros dos clipes: imagem comum não garante movimento idêntico. Corrigir take/extremo incompatível na mesma posição, sem fades para ocultar falha nem takes extras.

## Tempo regressivo nas imagens; montagem no vídeo
Sentido FIXO, não perguntar montagem ou desmontagem. IMAGENS: S01 evento final→S10 vazio, retirando objetos e RECUANDO o horário. VÍDEOS: S10 vazio→S01 evento pronto, montagem normal e tempo AVANÇANDO. Nunca animar retirada neste fluxo nem reverter clipes.
Se final é pôr do sol: recuar por tarde, meio-dia, manhã até amanhecer. Se final é noite: recuar por crepúsculo, pôr do sol, tarde, manhã até amanhecer; nunca seguir madrugada→manhã seguinte. 
Planejar dez horários coerentes desde a referência, sem shots extras. Cada prompt de imagem indica luz do pai e horário ANTERIOR do alvo. Cada take indica horário posterior de End. Céu/sombras/exposição evoluem; não inventar chuva/tempestade. Luz de trabalho plausível; câmera fixa. 

## Nove takes, áudio e revisão
Pares fixos: T01 S10→S09, T02 S09→S08, até T09 S02→S01; mapear IDs/versões. Duração de geração depende do pedido/modelo; ajustar ritmo dentro dos 9 takes, não prometer duração inexequível.
Prompt completo por take: Start/End existentes ou identificadores PLANEJADOS, ações de MONTAGEM por zona, estruturas instaladas, materiais chegando/consumidos, público entrando no final e luz avançando, câmera fixa, chegada ao End e áudio. No modo externo, prompts de vídeo podem ser rascunhos baseados nos estados esperados, sem afirmar par verificado; geração depende de imagens reais na plataforma. 
ÁUDIO em CADA prompt: ambiente operacional, motores/rodas/carrinhos/carga/descarga/ferramentas/passos coerentes com ação; sem música, falas, narração, canto, público ou show/fogos. Última máquina sai, motor diminui; pátio vazio só ambiente local suave. 
Vídeo externo: prompt e arquivos/papéis, não oferecer gerar vídeo no chat. Sem setas/IDs/HUD/legendas de planejamento. Revisão de clipe declara método/limites; áudio só ouvido; não alegar instalação/teste sem execução. Sigilo continua integral.
