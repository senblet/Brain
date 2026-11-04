# Development — video made with code

How coding agents make short films without a video model: the picture is a
web page that can draw any instant, a headless browser captures every frame,
and the sound is written from the same timeline. Fits motion graphics,
explainers, lyric videos, hand-drawn and diagram styles, and social clips
(e.g. Reels for a catalogue); not photorealistic footage — for that,
practitioners have the agent drive a video model and do the editing itself.

**Tags:** as in the [README](../README.md#how-notes-are-written). Practice
documented in several public repositories (read 2026-11-04), most fully in
`lemo-opuscar`'s `TECHNIQUE.md`; no measurements behind the quality claims.
Which of the repos to use: [ai/skill-libraries.md](../ai/skill-libraries.md#video-with-code).

---

## The pipeline

```
timeline (one source of truth)
  ├─ picture:   page with render(t) → headless Chrome, frame by frame → video.mp4
  ├─ voice:     TTS per line → speech-to-text check → word timings
  ├─ music/sfx: written from the same cues
  └─ captions:  .srt + captions drawn in the page
mix → ffmpeg mux, loudness normalised → film.mp4
```

## The picture

- **MUST make every frame a pure function of time.** The page exposes
  `render(t)` and a duration; no `Date.now()`, no unseeded `Math.random()`
  (use a seeded hash), no state carried from the previous frame. Then any
  frame renders alone, in any order, on any worker, and a failed render
  resumes where it stopped.
- Signal readiness (fonts and images loaded) before capture starts.
- **Draw for the output size**: 1920×1080 by default; 1080×1920 for
  vertical social video, with the layout computed from the viewport, not
  stretched afterwards.
- One world-to-screen function for anything that follows a subject; never
  hand-type screen coordinates.
- Stepped animation ("on twos") is a style choice; keep camera and light
  smooth every frame — a stepped camera reads as lag.
- Fast capture: JPEG screenshots, one browser per worker, grain added in
  `ffmpeg` rather than drawn in the page (grain in the page makes frames
  incompressible).
- Motion blur, if wanted: average several sub-frames over a short shutter.
- Reserve the caption band: keep faces and key action out of it.

## One timeline drives everything

Sections, tempo, beats and hit points live in one file. The score, the
sound effects, the subtitles and the checks read the same numbers; a small
script compares each visual hit with its cue (aim for 0 ms).

## Sound

- Voice: the client's recording if there is one; otherwise TTS. **Check
  every line with speech-to-text** against the script and regenerate until
  it matches; spell numbers out for TTS, write them as digits in captions.
- Compress the voice first, then balance by loudness: voice clearly above
  the music (one practitioner uses ~10 dB).
- Synthesised scores get bass-heavy; measure energy per band after mixing.
- **Master to −14 LUFS** with a true-peak limit (two-pass loudness
  normalisation in `ffmpeg`), and check the final file's loudness and for
  blank frames before delivery.

## Working with the agent

- **Storyboard or treatment first**, then build shot by shot. Agents given
  only broad direction still produce coherent films; more requirements give
  more accurate ones, and higher reasoning effort gives more elaborate
  scenes (one practitioner's observation).
- **The agent reviews from output, not code:** contact sheets of a frame
  every 1–2 s, frame strips around key actions, then a full watch with
  sound. One repo adds a second model scoring each film against a rubric
  for two rounds; the judge runs separately from the maker
  ([ai/agent-workflows.md](../ai/agent-workflows.md#verification-is-the-point)).
- **Parallel chapters:** a written animation guide briefs subagents; each
  owns one chapter file; shared files are read-only — a bug in one is
  reported, not patched by the chapter's agent.
- Every on-screen text stays up long enough to read (a check can list the
  text visible at each instant).

## Assets and licences

- Only CC0, CC BY or OFL material, each credited with source and licence;
  "no known restrictions" is not a licence. Fonts self-hosted, never linked
  at render time. A film that states facts keeps a file with each claim's
  source and quoted wording.
- A repository with no licence (several popular demos) can be studied but
  not copied into client work.

## Sources

Read 2026-11-04, via RodmanAi's list,
`https://x.com/rodmanai/status/2117540681556328773`:
`https://github.com/lemomo-ai/lemo-opuscar` (MIT and CC BY 4.0;
`TECHNIQUE.md`, `DIRECTOR.md`) · `https://github.com/mexicat/pdoom-video`
(MIT) · `https://github.com/JohnHeibel/PDoomVideo` (no licence;
`ANIMATION_GUIDE.md`) · `https://github.com/JohnHeibel/ClaudeAnimationBase`
(MIT) · `https://github.com/Vincentwei1021/mg-styles-15` (MIT) ·
`https://github.com/yihui-dev/awesome-opus5-5-videos` (MIT) ·
`https://github.com/athemeroy/awesome-claude-5-5-videos` (CC BY 4.0) ·
`https://github.com/joeseesun/opus-video-prompts` (no licence).

Tooling here moves monthly; re-read when this file is more than six months
old.
