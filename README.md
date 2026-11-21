# VIDEO-DIRECTOR

Estúdio de motion graphics com Remotion e renderização MP4 pelo GitHub Actions.

## Como renderizar pelo iPhone
1. Abra a aba **Actions** deste repositório.
2. Selecione **Render VIDEO-DIRECTOR** e toque em **Run workflow**.
3. Aguarde a execução terminar.
4. Abra a execução e baixe o artefato **video-director-mp4** (ZIP contendo `video.mp4`).

A execução é feita na nuvem pelo GitHub Actions; não é necessário manter o iPhone ligado.

## Desenvolvimento local (opcional)
```bash
npm install
npm run studio
npm run render
```

O vídeo de demonstração é uma animação vertical 1080x1920 com títulos e elementos gráficos. Para editar as frases, altere `src/Video.tsx`. A skill `SKILL.md` orienta como planejar novas cenas. **Não há geração cinematográfica por IA nem voz sintetizada nesta versão inicial.**
