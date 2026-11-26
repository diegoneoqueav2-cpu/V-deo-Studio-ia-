---
name: motion-master
description: Produce and revise premium advertising motion graphics from briefs and reference videos.
---
# Workflow
Inspect reference frames and timing before coding. Identify persistent objects, trajectories, typography, palette, camera, transitions and sound cues. Build a 3–5 second proof before a full campaign. Preserve approved source and revise source rather than patching video.
# Rendering
Use Remotion with frame-driven SVG/CSS transforms or Three.js for actual geometry. Use deterministic time, not wall-clock animations. Default vertical 1080x1920, 60fps. Render with FFmpeg or Remotion. Never claim a render exists without checking the file.
# Motion
Use the accompanying motion.mjs functions. Overlap actions; retain object identity across scenes. Use continuous trajectories and matched velocities at handoffs. Avoid independent slide entrances. Perspective requires changing orientation, depth and projected shadow together. Use compatible SVG path topology for morphs; otherwise explicitly describe the transition as a crossfade. For motion blur use temporal multisampling where feasible.
# Quality gate
Inspect rendered frames and playback before claiming quality. Verify duration, dimensions, fps, spelling, brand assets, safe margins, audio sync, and transition continuity. Disclose unimplemented effects. Archive approved styles only after explicit approval.
# Integration
Read this skill explicitly at the beginning of motion tasks. This repository file alone does not install or automatically activate a Codex skill. Existing motion-premium files remain available.
