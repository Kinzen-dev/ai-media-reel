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
- Batch 35 DONE + cataloged (psychedelic-60s-poster, digital-memorial-tribute, masterclass-course-pdp, chord-diagram-hero, scroll-timeline-chapter-nav - recovered via verify-only, all PASS -> 176 live).
- ROUND-3 BOLD AUDIT `wtgdshms0` DONE: 49 wow finds (most wow5/wow4, ~all capture-safe + no-WebGL). FULL FUEL in `tasks/wtgdshms0.output` (reconstruct briefs from each finding's signature+whyDistinct at build time). Prioritized wow5 not yet built: luxury-brand-game-narrative-shell, hyperpop-chromatic-overload, spatial-perspective-type-wall, flow-field-still-portrait, moire-op-art-svg-field, game-map-room-grid-navigation. Strong wow4: gravity-image-cascade, five-chapter-sound-world, ease-reverse-clip-menu, nuclear-dark-studio-minimal, zinegeist-collage, dynamic-cursor-mask-reveal, preloader-morphs-into-hero, video-to-cards-flip, future-medieval-illuminated, ransom-note-zine, y2k-chrome-aqua, gothic-horror-editorial, digital-rococo-baroque, ben-day-pop-couture, blackletter-variable-clash, chrome-mercury-letterpress, torn-paper-cutout-type, css-voxel-data-city, css-terrain-heightmap, superformula-svg, l-system-botanical, generative-woven-textile, semantic-zoom-universe, architectural-blueprint-hotspot, vertical-elevator-floors, leporello-accordion-book, interactive-site-map-world. (DROP pannable-infinite-moodboard + blender-cloth = WebGL-dependent.)
- Batch 36 IN FLIGHT `wob6hm5cd` (boldest wow5, 5-axis): ai-detective-narrative-hero, acid-rave-flyer, inflatable-balloon-type-hero, svg-ferrofluid-field-lines, oracle-card-draw-navigation.
- ROUND-4 MARKET AUDIT `wvsoph0ny` DONE: 71 market template directions (71/71 capture-safe, 2 webgl), all 6 clusters. Curated into `_backlog-markets-round4.json` (best-site-per-market + signature). Strongest (strength-5) per cluster: insurtech-conversational-quote, wealth-management-lifestyle-asset, neobank-b2b-product-mosaic / mental-health-calm-canvas, supplement-3d-product-stage, humanoid-robotics-character / luxury-fashion-editorial-commerce, beauty-skincare-ritual-editorial, cpg-food-brand-bold-color, ev-automotive-cinematic-hero / museum-collection-explorer, music-festival-poster-grid, (game-studio = webgl, skip) / luxury-resort-cinematic-stillness, destination-region-explorer, architecture-firm-project-grid, creative-agency-reel-case-study / ai-ml-enterprise-authority, cloud-devops-blueprint-grid, cybersecurity-controlled-dark, hardware-iot-scroll-reveal, developer-api-centered-proof. DROP webgl: jewelry-watches-webgl-scene, game-studio-world-portal (or no-WebGL variant).
- TWO FUEL POOLS now: `wtgdshms0.output` (49 bold/wow) + `_backlog-markets-round4.json` (71 market). Alternate so batches stay varied (some bold-art + some market-vertical + a generative + a platform each batch).
- Batch 36 DONE + cataloged (ai-detective-narrative-hero, acid-rave-flyer, inflatable-balloon-type-hero, svg-ferrofluid-field-lines, oracle-card-draw-navigation - all PASS, both make-or-break cleared -> 181 live). New slugs added to _categorize.py SLUG_CAT.
- Batch 37 DONE + cataloged (wealth-management-lifestyle-asset, cybersecurity-threat-graph, hyperpop-chromatic-overload, moire-op-art-field, game-map-room-nav - all PASS -> 186 live).
- DASH-SCAN CHANGE: the rg-via-rtk shim mangles byte-class output (false 297-match on wealth template). Use the PYTHON codepoint scan instead (bad={0x2012,0x2013,0x2014,0x2015,0x2212,0x2500,0x2501}); it is rtk-immune and ground truth.
- Batch 38 DONE + cataloged (supplement-3d-product-stage, museum-collection-explorer, developer-api-code-hero, spatial-perspective-type-wall, future-medieval-illuminated - all PASS -> 191 live).
- Batch 39 DONE + cataloged (luxury-resort-cinematic-stillness, beauty-skincare-ritual-editorial, flow-field-still-portrait, gothic-horror-editorial, chrome-mercury-letterpress - all PASS -> 196 live).
- Batch 40 DONE + cataloged (generative-woven-textile-hero, css-voxel-data-city, ev-automotive-cinematic-hero, mental-health-calm-canvas PASS first time; ben-day-pop-couture flagged by judge = photo hero broke the flat-ink register -> fix agent swapped it to an inline-SVG Lichtenstein crying-girl portrait -> re-judged PASS -> 201 live). MILESTONE SUMMARY delivered to King at 201.
- Category spread @201: Interaction&Motion 43, Design Movements 31, Generative 23, Editorial 22, PagePurpose 22, Platform-Primitive 18, Industry Verticals 18, 3D&Spatial 17, Document Artifacts 7.
- Batch 41 DONE + cataloged (l-system-botanical-canvas, vertical-elevator-floors, cpg-food-brand-bold-color, cloud-devops-blueprint-grid PASS first time; digital-rococo-baroque NEEDS-FIX = scrollwork too pale/low-contrast -> fix agent deepened gold gradient + dark medallion halo + stronger relief + thicker strokes -> re-judged PASS -> 206 live).
- Batch 42 FAILED ENTIRELY (WEEKLY limit, resets 6pm Bangkok; 0 built). PARKED for the award lane: architecture-firm-project-grid, pro-sports-club-hero, ai-ml-enterprise-authority, semantic-zoom-universe, torn-paper-cutout-type. Re-run these when we return to the award lane.

## LANE SWITCH 2026-06-29 (King): YIMWHAN BACKOFFICE
King wants the next batches as BACKOFFICE ADMIN + OWNER dashboard DESIGN IDEAS for Yimwhan-AI-production (the AI voice+LINE assistant for a dental clinic). Build MANY distinct design directions, many batches, until King finds one he likes -> then RETURN to the award lane (resume the bold+market pools + parked batch 42). These admin templates still go in the library (new category: add an "admin" bucket to _categorize.py ORDER + SLUG_CAT, display name "Admin & Backoffice").
- QA UPGRADE (King updated /qa-loop): fold `vlint.mjs` into the gate. Per batch, after qa-harness screenshots, also run `cd ~/Projects/_qa-harness && node vlint.mjs http://localhost:8765/templates/<slug>.html --viewports=1440x900,390x844 --severity=MED` (server = `cd showcase && python3 -m http.server 8765`). vlint catches deterministic geometry (overflow-x, overlap, occluded-interactive, heading-occluded, broken-image) that taste-only judging misses - critical for DENSE admin UIs. Then still do the faithful screenshot + fresh visual judge (taste). Never declare clean from vlint alone.
- Batch 43 DONE + cataloged (admin-owner-overview, admin-case-inbox, admin-bookings-calendar, admin-handoff-liveops, admin-analytics-report - all PASS the UPGRADED gate -> 211 live). New "Admin & Backoffice" category added to _categorize.py ORDER + index.html ORDER, LIVE on the gallery (King requested the separate category). Weekly limit IS RESET (batch built fine). vlint caught real geometry bugs (bookings provList 3437px mobile overflow, an occluded filter tab, a live-anim overflow) - 3 templates needed a geometry fix, all -> HIGH:0 MED:0. Judge's strongest picks: admin-case-inbox + admin-handoff-liveops.
- HEADLESS QA DEFAULT (King 2026-06-29, browser popups disrupting his parallel work): mediagen-tpl-verify.mjs now launches HEADLESS by default (prints "[qa mode: ...]"). Toggle: `touch ~/Projects/media-gen-research-2026-06-19/.qa-headed` (or env QA_HEADED=1) to WATCH live; remove to go quiet. Subagent verify prompt in _batch-workflow.js now forces chromium.launch({headless:true}). EMPIRICAL A/B (admin-owner-overview, verified per King's "must check if quality differs"): screenshots + vlint geometry IDENTICAL headed vs headless (the ~9% pixel diff = font AA + animation-frame phase, not real render diff); only FPS differs (headed 241 real-GPU vs headless 121 software-rendered, both >>50 gate). So headless costs nothing for the real QA gates; FPS becomes a conservative under-estimate -> spot-check headed only if a template looks heavy/janky. RECORD real-GPU FPS in the manifest (from the headed first-pass), not the headless 121.
- DEPLOY CLONE GOTCHA: /tmp/reel-deploy is wiped on reboot (/tmp). Re-create: `git clone git@github-ktpz:Kinzen-dev/ai-media-reel.git /tmp/reel-deploy` (branch=main, Pages serves main root /templates/), then `git config user.name/email` to Kinzen-dev / ktpz.dev@gmail.com + `git remote set-url origin git@github-ktpz:Kinzen-dev/ai-media-reel.git`, then rsync + commit + push origin main.
- Batch 44 BUILT (admin-patient-profile, admin-ai-config, admin-owner-dark-bento, admin-live-activity, admin-multiclinic-rollup), subagents ran HEADLESS (popup fix works). vlint geometry: live-activity CLEAN; PENDING FIX (deferred to avoid overload while batch 45 builds): patient HIGH6, ai-config HIGH2, owner-dark-bento HIGH1+MED10, multiclinic HIGH1. NOT yet cataloged - fix the 4 -> re-vlint 0 -> judge all 5 -> catalog (admin) -> deploy. owner-dark-bento 51fps headless (~100 headed; glass-blur; fine per conservative-floor rule).
- AESTHETIC REFINEMENT (King 2026-06-29): for the backoffice batches do a run of LIVING-NOTE / hand-drawn / handwritten (ลายเส้น ลายมือ ลายเขียน) / MINIMAL / CLEAN designs for SEVERAL batches, THEN move to other wow backoffice styles. Tech: Google handwriting font (Caveat/Shantell Sans/Kalam) + clean body; hand-drawn SVG wobble via inline feTurbulence+feDisplacementMap (no roughjs); warm paper/cream + ink + one muted accent; sketch charts; whitespace. Still REAL usable admin, gentle/human register.
- Batch 44 DONE + cataloged (5 standard admin -> 216). Batch 45 DONE + cataloged (5 living-note -> 221; case-inbox needed a desktop-legibility fix -> PASS). Admin & Backoffice category = 15 (5 standard dense + 5 living-note hand-drawn). All on the live gallery. The brief's GEOMETRY guard cut vlint failures hard (batch 45 came out far cleaner than batch 44). Judge favorites: standard = dark-bento + live-activity; living-note = daily-brief + bookings.
- Batch 46 DONE + cataloged (5 living-note: handoff, analytics-sketch, ai-config, live-feed, week-review -> 226). Living-note backoffice SUITE COMPLETE (10 screens). Admin & Backoffice = 20 (10 standard + 10 living-note). Judge faves: analytics (xkcd wobble) + week-review.
- CATALOG GOTCHA (caught + fixed): `_categorize.py` OVERWRITES each entry's category from SLUG_CAT, so any new slug NOT in SLUG_CAT gets keyword-fallback-misbucketed even if you set category inline in the manifest. RULE: add new slugs to _categorize.py SLUG_CAT BEFORE running it in the catalog step (batch 46 shipped misbucketed for one commit, then fixed).
- Batch 47 DONE + cataloged (5 living-note FLAVORS of owner-overview -> 231). Judge ranking for a real owner backoffice: graphpaper #1 (grid+fineliner = data reads like instrumentation), watercolor #2, monoline #3, bujo (geometry-fixed), kraft (mobile-chart-fixed: displacement filter was smearing downscaled hairlines -> non-scaling-stroke + lifted label contrast). Admin & Backoffice = 25 (10 standard + 10 living-note suite + 5 living-note flavors). LIVING-NOTE EXPLORATION DONE (3 batches).
- Batch 48 DONE + cataloged (5 wow backoffice styles -> 236). Judge ranking: neo-brutalist #1 (owner usability - giant numbers + red signaling read instantly), glass-aurora #2 (demo/prospect wow), editorial #3, bloomberg #4, terminal #5. glass-aurora real-GPU 241fps headed (headless 20-29 = software backdrop-blur; the headed spot-check validated it - good reminder the headless FPS rule holds). glass-aurora geometry-fixed (oversized abs-pos aurora blobs DON'T clip via overflow/contain in this Chromium -> converted to box-fitting radial-gradient background layers; blur preserved). Admin & Backoffice = 30.
- Batch 49 DONE + cataloged (4 PASS: dark-luxe, claymorphism, swiss-grid, organic-blob -> 240). Judge ranking: swiss-grid #1 (most legible/authoritative), dark-luxe #2, organic-blob #3, claymorphism #4. spatial-depth NEEDS-FIX (faint KPI text + weak depth) -> fixed (text -> near-white, translateZ spread 82->180px + downward shadows + static rotateX(6deg) tilt so float reads at scroll=0, vlint 0/0) -> re-judge + catalog -> 241. Admin & Backoffice = 34 (+spatial = 35).
- Batch 50 IN FLIGHT `wjxnl1bin` (5 MORE wow styles): y2k-chrome, blueprint-schematic, risograph, neumorphism (WATCH text contrast - neumorphism's classic weakness), duotone-bold. Slugs pre-added to SLUG_CAT.
- spatial-depth depth needed 2 fix rounds: translateZ/perspective does NOT show in a flat scroll=0 thumbnail; the fix that works = SHADOW-elevation tiers (bigger/softer downward shadow = floats higher) + translateY/scale stagger. LESSON for any "depth/float/3D-layer" template in a thumbnail-driven library: fake elevation with shadows+stagger, do not rely on perspective Z.
- Batch 50 DONE + cataloged (5 wow styles -> 246, Admin & Backoffice = 40). Judge: blueprint #1, neumorphism #2 (beat its contrast trap), duotone #3, riso #4, y2k-chrome #5 (faint chrome numerals - if King picks Y2K, darken KPI fill). y2k+blueprint geometry-fixed.
- 2026-06-30 CHECKPOINT (AskUserQuestion): asked King the next move now that the dashboard-style menu is exhaustive (26 treatments). King chose "KEEP GENERATING MORE DASHBOARD STYLES." So: continue producing fresh distinct dashboard registers, batch after batch, until he picks one. (Do NOT switch to applying-across-screens or the award lane until King says.)
- Batch 51 DONE + cataloged (art-deco, memphis, cyberpunk-hud, retro-mac-system, isometric-illustration -> 251, Admin & Backoffice = 45). Judge: retro-mac-system #1, isometric #2, cyberpunk #3, art-deco #4, memphis #5. memphis geometry-fixed (3px tilted-block overflow -> padding:0 5px on grid rows preserving Memphis shadows). retro-mac output confirmed clean (no Arabic, dash-clean).
- Batch 52 DONE + cataloged (vaporwave-synthwave, bauhaus, holographic-foil, transit-signage, notion-blocks -> 256, Admin & Backoffice = 50). Live + CI green (sha e42aab4). vlint caught real bugs the build agents missed: holographic HIGH16+MED16 (foil ::before sheen at inset:-40% inflated scrollWidth/Height -> inset:0 + bg-position sweep; perf 37->120), bauhaus HIGH1 (heading span), transit MED1. Judge taste-fixes (geometry-clean but failed taste): holographic low-contrast pastel-on-pastel -> opaque plates + jewel-ink chart; vaporwave off-brand sports-car block -> on-brand "today's highlights" panel + lifted sublabel contrast; notion KPI row buried under hero photo+paragraph -> compacted hero so KPI database row peeks at scroll=0. Headed FPS: vaporwave 241, holographic 120 (honest catalog values; light 3 = 240). bauhaus uses U+2212 MINUS for negative deltas (correct math glyph, NOT a banned dash; judge misread at thumb scale).
- STYLE IDEAS still unused for future batches: gradient-mesh-vibrant, art-nouveau, glassmorphism-light, brutalist-mono, paper-cut-layered, retro-terminal-amber, comic/ben-day, data-noir, sticker-collage, magazine-broadsheet, minimal-monochrome-huge-type, pixel-arcade, gov-civic-clean, spreadsheet-raw, kanban-board. (consumed since batch 51: vaporwave/synthwave, bauhaus-grid, holographic-foil, transit-signage, notion-blocks.)
- OWNER-OVERVIEW now has ~25 style treatments (5 living-note flavors + 20 wow styles across batches 48-52) for King to pick a backoffice STYLE from. Once he picks one, apply it across the suite screens. Keep producing wow styles until King says he found it, THEN return to the AWARD LANE (parked batch-42: architecture-firm-project-grid, pro-sports-club-hero, ai-ml-enterprise-authority, semantic-zoom-universe, torn-paper-cutout-type + bold pool wtgdshms0.output + market pool _backlog-markets-round4.json).
- PAUSED 2026-06-30 (King): "เดี๋ยวจบ batch นี้แล้ว break ก่อน...พักก่อนค่อยลุยกันต่อทีหลัง" - batch 52 finished, cataloged, deployed, CI green. LOOP PARKED here; do NOT launch batch 53 until King says resume. On resume: keep generating more distinct owner-dashboard styles (his standing pick) from the STYLE IDEAS bank, batch after batch, until he names a favorite; then apply it across all backoffice screens; eventually return to the award lane.
- HEADED-FPS-SPOTCHECK pattern (validated): for a backdrop-filter/heavy template that reads low FPS in headless, run ONE `QA_HEADED=1 node mediagen-tpl-verify.mjs <slug>` to get the real-GPU number before worrying (it pops one window briefly). glass-aurora 29 headless -> 241 headed.

## RESUMED 2026-07-02 (King): TWO ALTERNATING LANES + WOW MANDATE + MODEL SPLIT
- King resumed the loop with TWO lanes, ALTERNATED batch by batch until he says brake:
  (A) YIMWHAN BACKOFFICE: continue owner-dashboard style treatments (his 2026-06-30 standing pick).
  (B) VESPERWERK COMPANY SITE: Vesperwerk = King's newly REGISTERED company (real!). Logo received
      (gold 8-point vesper star + charcoal serif VESPERWERK caps, quiet-luxury). Recreated as
      `showcase/assets/vesperwerk-star.svg` (two-facet gold, eye-verified vs the real logo; Playfair
      Display = closest wordmark face). Canonical brand + FIXED site copy spec (English, premium
      software+AI studio, Yimwhan as flagship case) = `showcase/templates/_VESPERWERK-BRAND.md`;
      every vesperwerk-* build agent reads it so King compares REGISTERS of the same site.
      ASSUMPTIONS FLAGGED to King: English copy, positioning wording, hello@vesperwerk.com placeholder.
- WOW MANDATE (King 2026-07-02): every idea/design must be genuinely wow, NEVER AI slop; pull max
  model capability. Anti-slop clause now goes in every brief + judge prompt; judge grades register
  commitment hard.
- QA stays headless (King works in parallel; already the harness default). /qa-loop layers = the gate:
  qa-harness shots + vlint + fresh judge + FPS (headless conservative-floor rule; headed spot-check only).
- MODEL SPLIT (King asked for max-quality-per-token, 2026-07-02): BUILD agents = Fable 5 (wow origin;
  session model, no override). VERIFY agents = Sonnet 5 effort:high (checklist/geometry; set in
  _batch-workflow.js - taste still gated by judge). JUDGE = Fable (1/batch, cheap, taste-critical).
  RESEARCH scouts = Sonnet (proven by the 60-direction audit). Mechanical fix agents = Sonnet;
  register/taste fixes = Fable. Pricing basis: Fable $10/$50 vs Sonnet 5 $3/$15 per MTok (intro $2/$10
  to Aug 2026). PENDING A/B: one backoffice batch with Sonnet 5 BUILDERS judged blind vs Fable batch;
  if wow holds, backoffice builders may drop to Sonnet (Vesperwerk lane stays Fable regardless).
- Batch 53 DONE + cataloged + DEPLOYED (lane A -> 261 live, Admin = 55). 5/5 first-time PASS through
  the full gate (FPS 74-121 headless, vlint 0/0 x5, dash CLEAN x5, fresh judge zero fixes). Judge
  ranking: minimal-mono-type #1 (instant-read KPIs + gallery-stopping), data-noir #2 (pure wow pick),
  paper-cut #3, gov-civic #4, glass-light #5. FIRST BATCH with Sonnet-5 verify agents: caught 3 real
  mobile-chart bugs, fixed them, geometry 0/0 - the model split holds quality. Contact email CONFIRMED
  by King: kittipong.k@vesperwerk.com (spec updated). Deploy commit also ships the new Vesperwerk
  gallery category + copies vesperwerk-star.svg into the live /assets/ (batch 54 templates reference it).
- VESPERWERK AUDIT DONE `wm6lzl5af`: 51 registers across 6 lenses, 8 wow-5. FULL FUEL saved to
  `_backlog-vesperwerk.json` (lane-B backlog). Wow-5 not yet built: engraved-plate-ledger,
  nautical-almanac, type-specimen-atlas, star-chart(planisphere), instrument-faceplate + strong-4s
  (bas-relief-emblem, gold-thread-wayfinding, mono-ink-restraint, maison-editorial, foil-seal-invitation,
  departures-board, observatory-instrument, riso-nocturne, art-deco-grand-hotel, geist-console,
  patent-plate, poster-crop, manuscript-quarterly...). Dedup note: swiss/specimen/datasheet families
  overlap - pick one member per family per batch.
- Batch 54 IN FLIGHT `wgu1drpwm` (lane B, first 5 Vesperwerk registers, 5 different lenses):
  vesperwerk-uranometria-engraving, vesperwerk-celestial-complication, vesperwerk-swiss-grid-serif,
  vesperwerk-spec-sheet-instrument, vesperwerk-bilingual-epigraph. Slugs pre-added to SLUG_CAT under
  NEW category "vesperwerk" ("Vesperwerk Site") - added to _categorize.py ORDER + index.html ORDER.
  Batch 55 = lane A again (alternate).
- STYLE IDEAS bank for lane A after batch 53: gradient-mesh-vibrant, art-nouveau, brutalist-mono,
  retro-terminal-amber, comic/ben-day, sticker-collage, magazine-broadsheet, pixel-arcade,
  spreadsheet-raw, kanban-board (+ paper-cut/data-noir/gov-civic/minimal-mono/glass-light consumed).
- BUILD-BRIEF GEOMETRY GUARD: admin/data-dense templates keep tripping vlint (element overflow) despite agent self-checks - admin/living-note briefs now bake in "GEOMETRY (vlint-checked): min-width:0 on flex children; truncate/wrap; no element wider than container; zero page overflow at 390+1440". ALWAYS run vlint in the gate. Keep producing backoffice until King picks a favorite, THEN return to award lane (parked batch-42 award set + bold/market pools).
- /loop-me note: King typed /loop-me but it is a workflow-spec GRILLING skill (not "keep the factory looping"); his explicit "keep building batches" instruction wins, so NOT grilling. Flagged to King.
- PATTERN (2 fixes in a row, both committed-aesthetic): bold/ornate templates sometimes under-deliver on REGISTER on first build (photo-not-comic; pale-not-ornate). The fresh judge catches it; a focused contrast/commitment fix agent + re-judge resolves it. Keep judging for register strength, not just "are the parts present". ~5% need one fix; still 0 parked.
- FUEL CONSUMED so far - bold: ai-detective, acid-rave, inflatable-balloon, svg-ferrofluid, oracle-card, hyperpop, moire-op-art, game-map-room (8 of 49). market: wealth-management, cybersecurity (2 of 71). LOTS left. King (2026-06-23) wants BOTH bold AND broad market coverage -> keep alternating; surface a milestone summary as the count climbs (~200).
- After cataloging each batch run `python3 _categorize.py` (auto-buckets; add new slugs to SLUG_CAT to lock). Catalog -> deploy -> next batch.

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
