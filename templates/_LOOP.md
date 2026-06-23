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
- 2026-06-23 RESUMED (King reviewed the categorized gallery, found it useful, said go long after BOLD/wow ideas). Gallery now has 9 categories + jump-nav + live filter + localStorage favorites (star per card, Favorites pill). Library = 171 cataloged.
- IN FLIGHT: (a) batch-35 RECOVERY verify-only `wnii9ax3a` on the 5 files that built before the session limit (psychedelic-60s-poster, digital-memorial-tribute, masterclass-course-pdp, chord-diagram-hero, scroll-timeline-chapter-nav) -> on completion qa-harness+dash-scan+judge+catalog -> 176. (b) ROUND-3 BOLD AUDIT `wtgdshms0` (`_audit-workflow-3.js`, wow-biased: award-now / signature-moment / maximal-artdir / expressive-type / generative-spectacle / radical-structure) -> synthesize bold fuel for batch 36+. After cataloging the categorize step is `python3 _categorize.py` (auto-buckets; add new slugs to its SLUG_CAT to lock).

- 111 templates LIVE + cataloged, 0 PARKED. The earlier "saturated at ~106" call was WRONG (under-research): a 6-lens idea-space audit (2026-06-21) found 32 genuinely-NEW distinct directions. The library is saturated on INTERACTION MECHANICS but was barely touched on PAGE PURPOSE / CONTENT DOMAIN. (Rule banked: never claim a ceiling from a narrow search - see CLAUDE.md + memory feedback_research_breadth_before_certainty.) Deploy = rsync showcase/templates/ -> /tmp/reel-deploy/templates/ then commit+push (Kinzen-dev).
- Batch 23 DONE + cataloged (5 page-purpose types, all PASS first time -> 116). Batch 24 DONE + cataloged (linkinbio-glass-stack, recipe-howto-card, interactive-timeline, multistep-onboarding-form, token-stream-canvas - all PASS first time, ZERO fixes -> 121 live). PATTERN HOLDING: page-purpose templates pass first-time at a far higher rate than interaction-mechanic ones did, because they lean on layout/IO/anchor-positioning (capture-safe) not GPU/Houdini/WebGL (capture-fragile). Batches 23+24 = 10/10 first-time. The "saturated" call was doubly wrong: this axis is both NOVEL and LOWER-RISK.
- Batch 25 DONE + cataloged (cmd-k-portfolio, annotated-case-study, stat-annual-report, changelog-diff-timeline, frutiger-aero-revival - all PASS, Frutiger Aero gloss/bevel landed -> 126 live). Batches 23+24+25 = 15/15 page-purpose PASS first-time.
- HALFWAY (15/32) reached. TWO workflows now IN FLIGHT IN PARALLEL:
  - Batch 26 BUILD (wp3t8c7a8): silent-luxury-restraint, broadsheet-newspaper, la-carta-restaurant-character, split-master-detail, radial-hub-menu.
  - BROAD 6-LENS AUDIT (w757bjyrv) DONE. RESULT: 60 NEW distinct directions, ~all capture-safe + zero-WebGL. The space was emphatically NOT saturated - decisively validates King's research-breadth pushback. Synthesized + deduped + curated into `_backlog-refresh-2.json`: 34 build-ready entries (full briefs, mix of vertical / design-movement / platform-primitive / web-artifact / generative-static / 2026-award) + 26 named lower-priority. Dropped only view-transition-portfolio-nav (cross-document MPA breaks the single-self-contained-file rule).
- Batch 26 DONE + cataloged (silent-luxury-restraint, broadsheet-newspaper, la-carta-restaurant-character, split-master-detail, radial-hub-menu - all PASS, all dash-clean -> 131 live). 20/20 page-purpose+art-direction PASS first-time across batches 23-26.
- Batch 27 DONE + cataloged (swiss-international-typographic, de-stijl-mondrian, api-docs-dark-sidebar, css-voxel-isometric, fintech-trust-stack - all PASS first-time incl high-risk css-voxel = real isometric diorama + de-stijl = real neoplasticism -> 136 live). Audit fuel passes first-time too. 25/25 across batches 23-27.
- Batch 28 DONE + cataloged (soviet-constructivist, conference-schedule-grid, devtools-live-code-hero, feturbulence-organic-hero, property-gradient-brand - all PASS first-time incl high-risk feturbulence = rich topographic field + property-gradient = vivid oklch -> 141 live). 30/30 since the audit.
- Batch 29 DONE + cataloged (mid-century-saul-bass, interactive-cv-print-replica, biotech-investor-brief, voronoi-skin-layout, native-carousel-filmstrip - all PASS; voronoi mobile = clean stacked-card fallback, native-carousel = visible numbered markers -> 146 live). 35/35 since the audit.
- Batch 30 DONE + cataloged (ukiyo-e-woodblock, uptime-status-page, property-developer-presales, variable-font-axis-playground, light-dark-adaptive-brand - all PASS first-time incl high-risk ukiyo-e woodblock craft + light-dark visible split -> 151 live, CROSSED 150). 40/40 since the audit.
- Batch 31 DONE + cataloged (art-deco-luxe, ticket-stub-pass, music-release-hub, neo-print-halftone-type, scroll-trigger-manifesto - all PASS; halftone dots survive downscale + scroll-driven hero settled both verified -> 156 live). 45/45 since the audit.
- Batch 32 DONE + cataloged (memphis-neo-postmodern, festival-lineup-poster, esports-team-roster, luxury-watch-callouts, mass-changelog-scroll-map - all PASS; esports mobile-render fix + horology callouts verified -> 161 live). 50/50 since the audit.
- Batch 33 DONE + cataloged (satirical-product-void, countdown-rsvp-launch, art-nouveau-organic, calendar-heatmap-data-hero, popover-invoker-glossary - all PASS; native Popover open-card + heatmap + Art Nouveau vines verified -> 166 live). 55/55 since the audit.
- Batch 34 DONE + cataloged (bauhaus-photogram, e-receipt-invoice, nuclear-authority-editorial, truchet-tile-generative, custom-highlight-reader - all PASS -> 171 live). 60/60 since the audit.
- Batch 35 IN FLIGHT (wf4tdwdsg): psychedelic-60s-poster, digital-memorial-tribute, masterclass-course-pdp, chord-diagram-hero, scroll-timeline-chapter-nav (5-axis spread).
- FUEL after batch 35: ~12 named left (container-query-mosaic, customizable-select, pricing-comparison-matrix, multi-chapter-audio, narrative-mystery, humanoid-companion, gamified-ecommerce, cultural-membership-map, circle-packing, css-folded-paper, web3-token-launch, luxury-travel, cause-progress) + older `_backlog-refresh.json` leftovers + 2 WebGL. RUN A 3RD BROAD AUDIT after ~batch 36-37 when build-ready drops to ~8 (research-breadth rule; hold ceiling loosely). NOTE: 50 templates since the audit (121->171) all first-time PASS; King will want a milestone summary on wake.
- Audit fuel remaining after batch 31 (in `_backlog-refresh-2.json`): memphis-neo-postmodern, festival-lineup-poster, countdown-rsvp-launch, esports-team-roster, satirical-product-void, luxury-watch-callouts, mass-changelog-scroll-map (7 ready) + 26 named lower-priority (art-nouveau, bauhaus-photogram, psychedelic-60s, popover-invoker, custom-highlight-reader, scroll-timeline-chapter-nav, container-query-mosaic, customizable-select, pricing-comparison-matrix, e-receipt, digital-memorial, nuclear-authority, multi-chapter-audio, narrative-mystery, humanoid-companion, gamified-ecommerce, cultural-membership-map, calendar-heatmap, chord-diagram, circle-packing, css-folded-paper, truchet-tile, web3-token-launch, luxury-travel, cause-progress, masterclass-pdp) + older `_backlog-refresh.json` leftovers + 2 WebGL. Keep mixing axes per batch.
- Batch 28+ FUEL: `_backlog-refresh-2.json` (34 ready, now -5 = 29 left incl. soviet-constructivist, mid-century-saul-bass, ukiyo-e-woodblock, art-deco-luxe, memphis, biotech-investor-brief, devtools-live-code-hero, property-developer-presales, conference-schedule-grid, festival-lineup-poster, interactive-cv, countdown-rsvp, uptime-status-page, scroll-trigger-manifesto, property-gradient-brand, native-carousel-filmstrip, light-dark-adaptive-brand, music-release-hub, ticket-stub-pass, voronoi-skin-layout, neo-print-halftone-type, esports-team-roster, feturbulence-organic-hero, variable-font-axis-playground, satirical-product-void, luxury-watch-callouts, mass-changelog-scroll-map) + 26 named lower-priority in same file + older `_backlog-refresh.json` leftovers + 2 WebGL. PICK DIVERSE batches (one per axis). King pre-authorized: keep the loop running through these without waiting for confirm.
- DASH-SCAN GATE: after each batch, before cataloging, run `rg -n '[\x{2012}\x{2013}\x{2014}\x{2015}\x{2500}\x{2501}]' <slug>.html` (UTF-8 aware per feedback_dash_scan_utf8). Build agents self-strip but verify; a visual-judge transcription showing a dash is NOT proof (batch 26 radial-hub flagged by judge but file was clean).
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
