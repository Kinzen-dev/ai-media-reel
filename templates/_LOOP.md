# AUTONOMOUS TEMPLATE LOOP — runbook

GOAL: while King sleeps, continuously produce genuinely-great, verified web-design TEMPLATES
for his future-project library. He will review them all when he wakes.

## IRON RULES
1. NEVER STOP. After each batch is verified + cataloged, immediately launch the next batch.
   The loop is driven by Workflow-completion notifications: build batch -> (notified) ->
   verify -> catalog -> deploy -> launch next batch -> ... until King returns and interrupts.
2. GREAT ONLY, NEVER SLOPPY. Every template must pass real verification (not agent self-report):
   - screenshot PC @1440 + Mobile @390 (qa-harness, real browser)
   - measure FPS (headed, real GPU)
   - I LOOK at every screenshot and judge: award-level on desktop? mobile not over-cropped + readable?
     FPS healthy (>~50)? If any fail -> fix (Edit or a fix agent) -> re-verify. Only catalog when truly good.
3. STATE LIVES IN FILES (repo = memory, survives context summarization):
   - `_manifest.json` : every template produced { slug,title,archetype,whenToUse,signature,pc,mobile,fps,status }
   - `_backlog.json`  : archetype fuel (todo ideas). Pull strongest first; mark consumed.
   - this runbook.
   If my context was reset: read this file + `_manifest.json` + `_backlog.json`, then continue the loop.

## PER-ITERATION ALGORITHM
1. Read `_manifest.json` (done) and `_backlog.json` (todo). Pick the next 4-5 strongest todo archetypes
   NOT already in the manifest. If backlog has < 4 todo, FIRST run a research agent (WebSearch/WebFetch
   on fresh Awwwards/FWA/Codrops directions) to append new distinct archetypes to `_backlog.json`.
2. Launch a Workflow: build the batch in parallel (build -> verify-and-fix each), writing
   self-contained HTML to `showcase/templates/<slug>.html`, reusing `../assets/` as demo content.
   Constraints: distinct + award-level + mobile-friendly (no landscape over-crop on phones) +
   performant + prefers-reduced-motion + first-line TEMPLATE comment + content in a top DATA array.
3. On completion: run qa-harness to capture PC + Mobile screenshots + FPS for each new template. LOOK.
4. Quality gate per template (judge the screenshots, not the agent's word):
   pass = desktop genuinely wow + mobile clean/readable + FPS healthy. Else fix -> re-verify, or
   mark `status:"needs-rework"` (do not present as done).
5. Append passing templates to `_manifest.json`. Regenerate `templates/index.html` (visual picker:
   thumbnail + title + when-to-use + open link, incl. v2/v3/v4 + tools tier-list) and the vault index
   `_knowledge/Resources/award-web-templates/README.md`. Commit + deploy to the live Pages site.
6. LAUNCH THE NEXT BATCH. Do not end the turn without the next Workflow launched.

## STATE (update each batch; _manifest.json is the source of truth)
- 68 templates LIVE + cataloged (originals v2/v3/v4 + batches 1-13). Deploy = rsync showcase/templates/ -> /tmp/reel-deploy/templates/ then commit+push (Kinzen-dev).
- Batch 14 IN FLIGHT (wf, build+verify): ascii-rasterizer, kinetic-broken-grid, anchor-annotated-index, magnetic-grid-snap, horizontal-parallax-shader (1 WebGL).
- Batch 15 fuel (in `_backlog-refresh.json`, NOT built): gravity-image-trail, ripple-click-canvas, depth-map-tilt, procedural-bezier-ribbon, noise-displacement-hover, typewriter-reveal-grid (+ page-morph-barba WebGL). Refresh again when it runs low.
- Rate-limit recovery drill (happened twice): builds land on disk even when the verify stage is rate-limited -> check disk + re-run `_verify-workflow.js` on the existing slugs, then qa-harness + judge + catalog as normal.
- SVG gotcha (cost 3 failed fixes on blind-mask-wipe, found by DOM probe): fill/stroke = var(--x) as an SVG presentation attribute does NOT resolve -> shape invisible; use hex or element.style. Lesson now in _batch-workflow verify prompt.
- Recurring defect to watch: build agents make a title-only hero and hide the signature below the fold. Workflow now has a "FIRST-VIEWPORT SIGNATURE at scroll=0" rule (build + verify). Judge every thumbnail for it.
- WebGL gotcha (cost me a long debug on dithered-lo-fi): GLSL ES 1.0 local float[] with dynamic index returns 0 on ANGLE -> all-paper; use a LUT texture + preserveDrawingBuffer:true for screenshot-stable thumbs. _batch-workflow verify prompt now warns about this.
- Verify-only (no rebuild) workflow = `_verify-workflow.js` (for files that built but missed their verify pass, e.g. a rate-limited batch).

## QUALITY NOTES
- Reuse real assets in ../assets/ so templates render + look wow.
- Two-color discipline by default (near-black + ONE accent; media brings color) unless the archetype
  specifies its own palette (e.g. museum=warm, press=light editorial).
- Commit fully to ONE paradigm per template. Never fall back to a generic dark card grid.
- Mobile is a first-class gate (King flagged it). Verify at 390px every time.

## CONTEXT ADAPTATION (learned mid-run)
- The main loop's context bloats with images; after many batches the API rejects new image reads
  ("exceed max for many-image requests"). When that happens, DELEGATE the visual gate to a
  FRESH-CONTEXT subagent each batch: give it the PC + Mobile screenshot paths and ask for a demanding
  PASS / NEEDS-FIX verdict per template. The main loop still measures FPS itself + orchestrates +
  fixes whatever the judge flags. This keeps the visual ground-truth gate intact.
- Thumbnails live at `_thumbs/<slug>.png` resized to <=1280px (smaller = better catalog load + readable).
  The verify harness `~/Projects/_qa-harness/mediagen-tpl-verify.mjs` now uses deviceScaleFactor:1.
- A verify agent may kill the local server (port 8765); restart it (idempotent) at the start of each
  verify pass: `cd showcase && python3 -m http.server 8765 &`.
