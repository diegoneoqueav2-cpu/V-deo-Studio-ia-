---
name: video-director
description: Planeja e implementa vídeos animados usando Remotion, GitHub e renderização MP4 na nuvem.
---

# VIDEO-DIRECTOR

## Objetivo
Transformar pedidos em português em vídeos verticais de motion graphics com Remotion. Trabalhar de forma compatível com iPhone por meio do GitHub.

## Procedimento
1. Converter o pedido em roteiro com duração, cenas, movimentos, textos e transições.
2. Definir estilo visual e manter consistência de personagens, cores e enquadramentos.
3. Implementar cenas em componentes React/Remotion, usando animações baseadas em frames (spring, interpolate, Sequence).
4. Atualizar a composição em `src/root.tsx` se duração, fps ou resolução mudarem.
5. Evitar dependências externas e assets não licenciados. Não usar áudio ou vídeo remoto sem garantir disponibilidade e direitos.
6. Fazer commit dos arquivos no GitHub sem sobrescrever trabalho existente sem revisão.
7. Executar o workflow `Render VIDEO-DIRECTOR` e conferir o resultado antes de declarar sucesso.
8. Entregar o link do artefato MP4 e explicar como baixá-lo pelo iPhone.

## Padrões
- Formato padrão: 1080x1920, 30 fps, H.264 MP4.
- Estilo: profissional, minimalista, movimentos suaves, tipografia legível.
- Evitar animação rígida, textos cortados, transições abruptas e cenas sem ritmo.
- Não afirmar que o Remotion gera sozinho vídeo cinematográfico por IA, personagens orgânicos ou narração humana. Esses recursos exigem integrações adicionais.

## Render
`npm install && npm run render`

## Limites
Este arquivo é uma especificação de Skill para agentes compatíveis. Ele não instala automaticamente uma Skill nativa no ChatGPT, não aciona workflows sozinho e não adiciona geradores de vídeo externos.
