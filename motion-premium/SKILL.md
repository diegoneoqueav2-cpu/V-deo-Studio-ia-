---
name: motion-premium
description: Default production workflow for premium motion graphics, reference reconstruction and UI animation.
---
# Motion Premium
Use this workflow by default for motion projects unless user requests another style. Preserve existing projects. Never claim a render is complete without verifying it.
1. Inspect reference video frame by frame, map timestamps, camera, cursor, click reactions, object transforms, lighting, typography and audio cues. Preserve reference choreography when requested.
2. Create editable scene graph with persistent object IDs, parent transforms and overlapping actions. Use Blender for actual 3D geometry and lighting; use layered compositing for UI when appropriate. Do not default to Pillow-only flat animation.
3. Use custom Bezier easing, anticipation, spring overshoot, inertia, velocity-dependent motion blur, perspective, depth of field, soft shadows, bloom and coordinated focus. Use morphing only when supported by compatible geometry.
4. Cursor clicks must trigger target compression, highlight, ripple and subsequent transition. Maintain continuity between scenes.
5. Preserve original logos/photos; do not invent replacement imagery. Use 1080x1920 at 30 fps by default.
6. Render short preview, inspect frames and transitions against reference, correct source, then render MP4 and archive editable source. No patching rendered video unless explicitly requested.
7. Save approved techniques and reference metadata for reuse. Distinguish actual 3D from simulated depth.
