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

## STANDING TASK (King, 2026-06-20): bank skill-ideas as the loop runs
After each batch, append any NEW design insight or loop-methodology insight to `_SKILL-IDEAS.md`
(two skill candidates: the loop itself + award-level frontend design). King will promote these to
real skills later via /promote-to-skill. Concrete + actionable bullets only; do not let it go stale.

## STATE (update each batch; _manifest.json is the source of truth)
- 111 templates LIVE + cataloged, 0 PARKED. The earlier "saturated at ~106" call was WRONG (under-research): a 6-lens idea-space audit (2026-06-21) found 32 genuinely-NEW distinct directions. The library is saturated on INTERACTION MECHANICS but was barely touched on PAGE PURPOSE / CONTENT DOMAIN. (Rule banked: never claim a ceiling from a narrow search - see CLAUDE.md + memory feedback_research_breadth_before_certainty.) Deploy = rsync showcase/templates/ -> /tmp/reel-deploy/templates/ then commit+push (Kinzen-dev).
- Batch 23 IN FLIGHT (wf, the NEW territory - page purposes, all CSS, thumbnail-safe): saas-dark-metric-hero, spec-table-hero, agent-chain-of-thought, pudding-scrollytell, configurator-hero.
- Batch 24+ fuel (in `_backlog-refresh.json`, 32 entries strongest-first, NOT built): link-in-bio, voice-transcript, token-stream, cmd-k-portfolio, split-master-detail, radial-hub, fixed-viewport, recipe-howto, annotated-case-study, multistep-onboarding-form, live-reaction-broadcast, interactive-timeline, stat-annual-report, broadsheet-newspaper, fashion-editorial, silent-luxury, frutiger-aero, changelog, semantic-zoom, culture-capsule, chaptered-deck, la-carta-restaurant, brutalist-utility, seriograph, viewfinder-ar + 2 WebGL (cinematic-single-room, terrain-map-navigation). King pre-authorized: keep the loop running through these without waiting for confirm.
- PARKED (files exist, NOT cataloged, do NOT re-attempt blindly):
  - `css-houdini-paint.html`: Houdini paint-worklet renders thin-hairline in thumbnail capture even though live+worklet are correct (capture-fragile API). 
  - `clip-path-morph-scroll.html`: clip-path:path() coords are fixed element-px, non-responsive, so the jagged path misaligns on a wide viewport (reads as a side panel). Needs a polygon()-% / SVG objectBoundingBox rewrite. See _SKILL-IDEAS.md.
- Batch 22 IN FLIGHT (wf, build+verify): slit-scan-temporal (Canvas2D), particle-image-morph (WebGL), gooey-metaball-merge (SVG goo). These are the LAST 3 genuinely-distinct, capture-safe paradigms a saturation-check refresh could find.
- SATURATION REACHED (~106 built): an honesty-first refresh agent verdict (2026-06-20) = the well is nearly dry; every major 2026 trend on Codrops/Awwwards/FWA/Godly is already built; next refresh expected to yield 0-2, mostly recombinations. After batch 22 (~109 templates), do NOT churn out variants-of-existing to hit a number - that violates the great-not-sloppy rule. Surface the natural endpoint to King and shift to polishing/curating the library, or retry the 2 parked (css-houdini-paint, clip-path-morph-scroll) with capture-safe approaches (e.g. SVG/Canvas border instead of Houdini; polygon()-% instead of path()).
- Novelty is getting harder at ~97 templates: refresh agents now honestly return fewer genuinely-distinct ideas. That's fine; lean on newer CSS primitives (@scope, @starting-style, anchor positioning, view-timeline, color-mix oklch, Custom Highlight API, container queries) and distinct input/data/craft mechanics.
- Session-limit note: King's own quota can hit ("resets <time> Bangkok") at the build stage; same recovery as a rate-limit (files on disk -> verify-only). Distinct from the transient Anthropic "Server is temporarily limiting" overload.
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
