# Motion Pro production modules
Existing cinematic workflow is independent. New modules are opt-in.
- director.py script.txt plan.json: heuristic scene plan, review before rendering.
- speech.py narration.wav words.json: CPU transcription with word timestamps; downloads model on first use.
- characters.py: rigged GLB import, existing actions and facial shape key animation. Requires compatible rig and authored animations.
- catalog.json: source directory only; no commercial assets downloaded. Record source, license and permission before adding any asset. Never commit private client files to this public repository.
- Delivery: GitHub Actions artifacts are downloadable by authorized users; automatic attachment to ChatGPT is not implemented.
