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
- Batch 54 DONE + cataloged + DEPLOYED (lane B -> 266 live, Vesperwerk Site = 5, all builtBy Fable 5).
  Gate: FPS 120-121 x5, vlint 0/0 x5, dash CLEAN x5. Judge: 4/5 first-time PASS; bilingual-epigraph
  NEEDS-FIX (Thai read as neutral caption vs the Didone Latin) -> PROBED first (Trirong WAS loading;
  real cause = 22.7px/w500 next to a 90px wordmark = caption presence) -> fixed as a display line
  (Trirong 600 @ clamp 1.38-2.28rem + section glosses 600) -> re-judged PASS. LESSON: dual-script
  pairing fails on PRESENCE/hierarchy, not font choice - size the second script as display, not gloss.
  JUDGE SHIP-RANKING for King's real site: celestial-complication #1 (SHIP THIS: horology dial =
  "precision that cannot fail" + works as a real homepage), spec-sheet-instrument #2, swiss-grid-serif
  #3, uranometria #4 (most gorgeous artifact, reads decorative), bilingual-epigraph #5. Deploy also
  synced the full showcase/assets/ into the live repo.
- Batch 55 DONE but PARKED (Sonnet-5 builder A/B; NOT cataloged). Gate: FPS 100-121, vlint 0/0 x5,
  dash CLEAN x5. Blind judge at the raised (SOTD) bar: brutalist-mono 7/10 (strongest), others 6/10;
  broadsheet NEEDS-FIX (Thai headline mark collision, see lesson below - FIXED + eye-verified).
  A/B CONCLUSION: Sonnet register-hit-rate ~= Fable at the OLD bar, but the wow ceiling problem is
  the CONCEPT CLASS (static style-skins), not the builder. King ruled the whole backoffice lane
  "ยังไม่ว้าว ไม่ผ่านเกณฑ์" -> batch 55 stays OUT of the manifest (files on disk; catalog later only
  if King wants archives). Experiential batches use FABLE builders.
- THAI TYPOGRAPHY LESSON (banked into the verify prompt as rule 7): wrapping Thai display text with
  line-height ~1.1 makes the NEXT line's upper marks (อี+อ้ etc) collide into the previous line and
  read as stray marks under the baseline (judge saw "นัูดหมาย"; probes proved font + tracking + tnum
  all innocent - the collision was cross-LINE). Rule: Thai that can wrap needs line-height >= 1.35;
  never letter-space Thai. Root-caused via control renders, not guessing (3 A/B probes).
- KING CALIBRATION (2026-07-02, decisive): Vesperwerk batch = "ดูดีในระดับนึง" (ok). Backoffice lane =
  FAILED his bar. Reference artifact for WOW = ~/Projects/stardust (read + distilled). THE STARDUST
  FORMULA now mandatory per archetype, fitted to its category: (1) one continuous LIVING WORLD that
  transforms (not styled sections), (2) narrative arc w/ payoff, (3) the visitor is a PLAYER (cursor
  force, click events, scrubbing), (4) cinematic chrome + post (HUD, grain, camera), (5) engineering
  honesty (live counters, real instrumentation), (6) bilingual EN/TH soul, (7) an entrance ritual.
  King also asked (new): keep MANY STYLES coming for backoffice INCLUDING LUXURY registers.
- Batch 56 IN FLIGHT `wt8u4q9dl` (lane A EXPERIENTIAL, Fable builders, stardust formula baked into
  every brief; luxury included per King): private-bank-ledger (light-luxury living ledger),
  silvered-complication (light haute-horology, live day dial + crown scrub), mission-control-live
  (Canvas2D particle ops theater + cursor gravity + T+ scrubber), clinic-digital-twin (isometric
  living diorama, patients move through real schedule), solari-split-flap (heritage-luxury mechanical
  board, real 3D flap cascades). ALL have: live heartbeat + day scrubber + hover cross-highlight +
  populated boot state (scroll=0 strong) + reduced-motion = paused populated state. Gate additions:
  motion filmstrip (mediagen-tpl-motion.mjs) feeds the judge; judge bar = SOTD-class.
- Motion upgrade DONE + DEPLOYED on vesperwerk-celestial-complication (entrance assembly ~2.2s,
  scroll cascades, hallmark press-ins, hover micros; SMIL + js-anim class architecture so
  reduced-motion is inert-by-default). Filmstrip verified alive; FPS 121, vlint 0/0.
- HARNESS CHANGE: mediagen-tpl-verify.mjs waits bumped to 3900ms PC+mobile (entrance rituals run
  ~2-2.4s; capture must be post-assembly).

## RESUMED 2026-07-17 ~01:00 (King: "ลุยต่อตามลูป... ไม่ต้องหยุดถามอะไรผมแล้ว ลุยงานยาวๆ" + ultracode standing this session)
- NEW LANE DIRECTIVE (King, overrides "experiential batches use Fable builders" for this lane):
  VESPERWERK COMPANY SITES - very wow, unique, FUSE ideas from multiple award-winning sites per
  concept, many designs. MODEL SPLIT: Fable 5 (main loop) INVENTS + DESIGNS each batch's briefs;
  Opus 4.8 BUILDS (pass buildModel:'opus' per archetype in _batch-workflow args); verify = Sonnet;
  judge = fresh Fable. Catalog with builtBy "Opus 4.8". Do not stop; do not ask.
- Batch 57 IN FLIGHT `w1hq50d0c` (lane B Vesperwerk experiential, Opus builders, stardust formula
  in every brief, all capture-safe / no WebGL): vesperwerk-first-light-thread (single gold thread
  navigates the page, cursor bend, waypoint re-draw), vesperwerk-almanac-of-hours (LIVE Bangkok
  ephemeris, real solar-position math + Venus table, 24h scrubber sweeps whole-page palette),
  vesperwerk-atelier-faceplate (operable instrument panel: drag dial, listening waveform, power-on
  ritual), vesperwerk-grand-ascenseur (Deco brass elevator ride: working floor indicator, diagonal
  wipes, express-ride buttons), vesperwerk-vesper-particles (2200-particle living dusk morphing
  through 5 chapters, cursor force + click nova - MAKE-OR-BREAK, judge hardest).
- Batch 57 GATED (all 5 built + Sonnet-verified; rebuild run `wfs9d6h6a` recovered the 3 dropped:
  first-light-thread ok [knot-on-numeral legibility fixed], almanac-of-hours ok [lazy-load black-gap
  fixed], vesper-particles ok [HUD scrim added]). MY GATE x5: FPS 92-121 all >50 (particles 100/92
  expected), dash CLEAN x5, filmstrips + thumbs + mobile captured x5. vlint: real defect = thread HUD
  13px ellipsis-clip @390 (max-width 64vw->84vw, FIXED by main loop, re-lint CLEAN); rest probed
  by-design (tracked-wordmark nowrap overflow class: letter-spaced VESPERWERK extends past its
  centered column, docSW==vw, no glyph cut - BANKED as a false-positive class next to odometers).
  Fresh Fable judge `judge-batch57` running (SOTD bar + brand fit + particles scrutinized hardest).
- Batch 57 JUDGED (SOTD bar): 4 PASS + 1 NEEDS-FIX. JUDGE SHIP-RANKING for King's REAL site:
  almanac-of-hours #1 (SOTD-SUBMITTABLE TODAY: live computed ephemeris IS the brand), atelier-faceplate
  #2 (clearest "production systems that cannot fail" argument), grand-ascenseur #3 (most memorable,
  slightly themed), first-light-thread #4 (timeless but least showstopping; rail re-anchor polish),
  vesper-particles #5 NEEDS-FIX (hero star/rings/horizon read; 2 of 3 SERVICE constellations = soft
  blobs -> Fable fix agent: tighter targets + two-tier alpha + constellation hairlines + less bloom).
  Non-blocking polish dispatched (Sonnet): thread chapter-rail anchoring + faceplate scramble cap
  <=1.2s. 4 passes CATALOGED builtBy "Opus 4.8" -> 275 in manifest (Vesperwerk Site = 9). DEPLOY
  after particles re-judge (single push).
- Batch 57 DONE + cataloged + DEPLOYED (-> 276 live, Vesperwerk Site = 10, commit 696921f, all 5
  builtBy "Opus 4.8"). particles fix re-judged PASS (all 3 service glyphs read unaided: oscilloscope
  wave / iso cube / storefront; two-tier alpha + gold constellation hairlines landed). Thread rail
  re-anchored (fixed-width labels + gold hairline through dots; root cause = variable label width
  scattering dot x-positions). Faceplate scramble resolves ~500ms. NON-BLOCKING POLISH BANKED:
  particles @scroll33 fixed nav wordmark lightly overlaps "AI Systems" heading at one transient
  offset (judge: passes as-is; nudge heading top offset in a later sweep).
- OPUS 4.8 BUILDER VERDICT (first full batch): 5/5 shipped, 4/5 judge-PASS first time at the RAISED
  SOTD bar (vs Fable batch 56 = 4/5 first time at same bar). Opus + Fable-designed briefs + Sonnet
  verify + Fable judge = holding the bar. Judge: almanac-of-hours is SOTD-SUBMITTABLE TODAY.
- Batch 58 BUILT 10/10 `wmji327z4` (0 errors; sealed-invitation verify caught the SAME missing
  DOCTYPE/head wrapper quirk as grand-ascenseur - RECURRING OPUS BUILDER QUIRK, briefs now carry a
  STRUCTURE GUARD line). MY GATE x5: FPS 94-121 all >50, dash CLEAN x5, filmstrips + captures done.
  vlint: ledger + specimen CLEAN 0/0; monogram = 3D card front/back stack (by-design, docSW==vw);
  bas-relief = 13-19px medallion decorative overflow (judge to eyeball); sealed-invitation = rotated
  seal-half (by-design) + principles ol li overlapping 5-8px vertically (judge told to eyeball for
  text collision vs layered-paper). Fresh judge `judge-batch58` running.
- Batch 58 DONE + cataloged + DEPLOYED (-> 281 live, Vesperwerk Site = 15, commit 6970c8f, all 5
  builtBy "Opus 4.8"). JUDGE: 5/5 FIRST-TIME PASS at SOTD bar - "stronger on average than the
  ephemeris standout". SUBMIT-READY TODAY: bas-relief-light (#1, evening-star payoff = jury moment)
  + sealed-invitation (#2 ritual). Ship-rank for King's REAL site: bas-relief-light > engraved-ledger
  > sealed-invitation > monogram-card > specimen-lab. FLAGSHIP CANDIDATE = bas-relief-light. Judge
  tradeoff flag: invitation/card exclusivity framing is bold positioning, may read pretentious for a
  studio chasing customers 2-to-N (surface to King). Both lint flags confirmed by-design by eye.
  POLISH DISPATCHED (Sonnet): specimen-lab entrance wght-sweep breathing (judge's optional lift;
  lands with batch 59 deploy). BANKED minor: dark service-card sections in monogram + specimen are
  the least-committed surfaces batch-wide.
- Batch 59 GATED: build `w26s1ffqk` 4/5 + patent-plate build dropped (connection) but file COMPLETE
  on disk -> verify-only `wv86bsk29` ok (fixed REAL mobile defect: REV A stamp floated over the
  phone drawing at 390 -> static stacking). specimen-lab breathing polish DONE + verified (entrance
  wght 320->700->400 sweep, cancel-on-touch, RM static). MY GATE x5: FPS 102-123, dash CLEAN x5,
  captures + filmstrips done. vlint: planisphere CLEAN 0/0, patent 1 MED, mono-ink 1 MED, riso 2
  MED (plate offsets); terminator HIGHs probed = cHit/cDot hit-halo pairs (by-design) + ticker
  ellipsis false-positive (docSW==390, judge told to eyeball). Fresh judge `judge-batch59` running.
- Batch 59 JUDGED: 4 PASS (planisphere = new flagship candidate, terminator = best converter, riso +
  patent also submit-ready; FOUR of five submit-ready) + mono-ink NEEDS-FIX (scroll=0 gate: the
  traveling star reads as a static bullet at rest; hero measure too wide, rag loose) -> Fable
  craftsman agent `fix-monoink-rail` dispatched (margin-rail + ticks + tighter measure; canonical
  copy untouched). 4 passes CATALOGED builtBy "Opus 4.8" -> 285 (Vesperwerk Site = 19). SLUG_CAT
  extended for batches 59+60. Judge: batch matches-to-exceeds the bas-relief/almanac bar on its top 3.
- Batch 60 GATED (built 10/10 `w6op84131`, 0 errors): jeweled-vitrine NO EDITS NEEDED (WebGL painted
  first frame, 68-75fps headless, static SVG fallback verified); auction-lot verify fixed a REAL
  wheel-trap bug (preventDefault blocked native scroll in overflowing panels at short viewports);
  evening-service verify fixed a mobile ribbon overlap; observatory-log + field-notes clean. MY GATE:
  FPS 53-121 (vitrine 76/53 = software WebGL, above bar), dash CLEAN x5, captures + filmstrips done.
  vlint: observatory + evening-service CLEAN 0/0; vitrine = glass-pane bleed + tracked wordmark
  (by-design, docSW==vw); auction @390 = plates strip (by-design slide) + ellipsized colophon +
  Next-plate button confirmed hittable via elementFromPoint; field-notes = rotated polaroid. Fresh
  judge `judge-batch60` running (vitrine scrutinized hardest: jewelry-grade or FAIL).
- mono-ink re-judged PASS (rail sells the mechanic at rest; 7-line authored rag; dropcap clip
  confirmed invisible with this copy) -> CATALOGED -> 289 (Vesperwerk = 23). BATCH 59 COMPLETE 5/5.
  Optional nit banked: authored mobile hero breaks (lone "software" line at 390).
- Batch 60 JUDGED: 3 clean PASS (observatory-log + field-notes SUBMIT-READY; evening-service passes
  on craft; field-notes = best SMB-conversion fit) + 2 one-fix-away -> fix agents dispatched:
  vitrine mobile SVG jewel (Fable: kill blown white hotspot, antique facet shading) + auction-lot
  scroll-driven plate-flip (Sonnet: real document scroll height drives plates; wheel-hijack removed;
  makes the flip provable to the filmstrip harness). 3 passes CATALOGED -> Vesperwerk = 23 total so
  far. STRATEGIC NOTE for King (judge): brand tension = quiet-luxury prestige (vitrine /
  evening-service / auction) vs warm SMB conversion (field-notes); observatory-log wins pure wow
  either way. Lane submit-ready count now 10+ treatments.
- Batch 60 re-judges: vitrine mobile jewel PASS (facet-normal shading vs one key light killed the
  clip-art read) -> CATALOGED -> 290 (Vesperwerk = 24). auction-lot: flip MECHANIC PROVEN (5 distinct
  plates across scroll stops; scroll-track rework = real document height, native wheel/touch) but
  NEW mobile defect judged: Plate I clips its note mid-sentence + both CTAs behind the deck footer
  at 390 -> Sonnet fix agent `fix-auction-mobile-plate1` dispatched (fit or internal scroll; check
  all 5 plates + 390x700).
- ROUND-2 VESPERWERK AUDIT `w2yy1om48` launched (research-breadth rule: build-ready fuel dropped to
  ~4-6 < 8 threshold). Six NEW lenses blind to round 1: thai-cultural-craft (untouched home ground),
  cinema-title-sequence, voice-sound (the product IS voice AI), digital-native-artifacts,
  space-architecture, excluded-space (probe what the lane avoided: color/wit/illustration/photo/
  brutalism/info-density). Script: _audit-vesperwerk2.js. Batch 62 picks from its results.
- Batch 61 GATED (built 10/10 `wmlu5jv6k`, 0 errors, ZERO verify fixes needed - first all-clean
  batch; structure guard + accumulated brief lessons paying off). MY GATE x5: FPS 54-121 (bibliophile
  55/54 = heavy turbulence marbling in software render, above bar but the lane's closest - flag if a
  future judge sees sluggishness), dash CLEAN x5, captures + filmstrips done. vlint: broadsheet CLEAN
  0/0, bibliophile MEDs only; illuminated star-crown margin overhang + poster-crop stage-clipped
  letterform + insignia 3D face = all probed by-design (docSW==vw). Fresh judge `judge-batch61`
  running.
- DEPLOYED commit 8bad5f2 -> 294 live, Vesperwerk Site = 28. Includes: batch 59 complete 5/5,
  batch 60 complete 5/5 (auction mobile Plate I compacted, final re-judge PASS: "submit-ready on
  mobile"; vitrine jewel PASS), batch 61 passes 3/5 (broadsheet, poster-crop, bibliophile - all
  submit-ready), specimen breathing polish, all fixes. SLUG_CAT gap lesson: ALWAYS add new slugs
  to SLUG_CAT BEFORE running _categorize.py (batch-61 trio briefly fell to keyword fallback).
- Batch 61 remaining: illuminated-hours (ornament density fix `fix-illuminated-density`) +
  mission-insignia (embroidery register rescue `fix-insignia-embroidery`) both IN FLIGHT (Fable),
  re-judge + catalog + next deploy when done.
- ROUND-2 AUDIT DONE `w2yy1om48`: 47 NEW findings (10 strength-5, all capture-safe, only 1 webgl in
  the whole set) -> curated to `_backlog-vesperwerk2.json`. The lane space was emphatically NOT dry
  (research-breadth rule validated AGAIN). Strength-5 pool: benjarong-atelier, transcript-screenplay,
  liquid-ink-title, trace-diagram, shoji-ma (batch 62) + commit-log, api-console, numbers-station,
  isometric-atelier-plan, gallery-corridor (batch 63 fuel) + 25 strength-4.
- Batch 62 IN FLIGHT `wmsqcxmfv` (Vesperwerk VI, one per new lens, Opus builders): benjarong-atelier
  (five-enamel firing ritual, Thai craft flagship candidate), transcript-screenplay (the product AS
  the site: live Thai call log w/ waveform subtitles), liquid-ink-title (Kyle Cooper ink pour
  credits), trace-diagram (living systems topology, click-to-fire traces), shoji-ma (washi panels
  slide open on scroll, light-through-paper, final unobstructed star payoff). SLUG_CAT pre-added
  this time.
- Batch 61 COMPLETE 5/5: illuminated-hours re-judged PASS (worked margin border + burnished gold
  landed) -> cataloged; mission-insignia PASSED on ROUND-2 fix (judge-prescribed silhouette
  outline-stitch + matte sheen + deeper beds killed the coin read at thumb scale; "ship it, do NOT
  park") -> cataloged -> 296 (Vesperwerk = 30).
- Batch 62 GATED (built 10/10 `wmsqcxmfv`; benjarong verify fixed the SVG var()-in-presentation-attr
  gotcha AGAIN - the standing lesson holds; shoji verify fixed panel-opacity text bleed-through).
  MY GATE x5: FPS 80-122, dash CLEAN x5. vlint: benjarong + trace-diagram CLEAN 0/0 both viewports;
  transcript = ellipsized header (false-positive class); liquid-ink = decorative splash/fin-mark
  overflows (by-design); shoji-ma = REAL DEFECT probed (hero CTAs unclickable under .panel -
  elementFromPoint returned panel-frame at ALL scroll depths) -> Sonnet fix `fix-shoji-clicks`:
  root cause = .panel defaulted pointer-events:auto; one-line pointer-events:none fix, verified
  clickable at every depth both viewports, nudge intact (window-level listener), occluded findings
  GONE (revert-compare proof). Judge `judge-batch62` running (benjarong kitsch check hardest).
- Batch 63 IN FLIGHT `wt45pv7oy` (Vesperwerk VII, Opus builders): commit-log (story as git graph,
  branch fork + merge payoff), numbers-station (tune a brass frequency dial through five stations,
  numbers burst decodes the case), switchboard-exchange (brass PBX, cords drape + the 02:14 call
  connects = product echo), isometric-atelier-plan (enter rooms via camera push-ins, tabletop sway),
  gallery-corridor (single-point-perspective walk to the pendant star). SLUG_CAT pre-added.
- Batch 62 JUDGED: 4 PASS (transcript-screenplay = "strategically strongest of the WHOLE lane - it
  IS his product"; Thai dialogue verified natural/polite by a Thai-reading judge; trace-diagram #2;
  benjarong PASSED the kitsch check = "proud heritage, international restraint" but flagged as the
  bolder/more polarizing brand bet; liquid-ink pass w/ non-blocking gloss note) -> 4 CATALOGED ->
  300 IN MANIFEST (Vesperwerk = 34). shoji-ma NEEDS-FIX round 2 (borderline: hero bloom = corner
  lens-flare, paper texture invisible at thumb scale, CRESCENDO INVERTED - hero out-blooms the
  room-06 payoff) -> ROUND-3 fix `fix-shoji-round3` with HARD acceptance criteria incl. NUMERIC
  luminance check (hero 55-70% of payoff). RULE: if round 3 fails re-judge, PARK shoji-ma.
- Non-blocking polish notes banked (batch 62): benjarong = bring one fired medallion above the fold;
  liquid-ink = add specular gloss to settled ink + smooth entrance blobs.
- DEPLOYED commit a02cca3 -> 305 live, Vesperwerk = 39. Batch 62 closed (4 shipped + shoji parked);
  Batch 63 COMPLETE 5/5 ("strongest batch yet" - switchboard + gallery-corridor = new lane leaders;
  commit-log = sharpest identity fit for King's real site; isometric ink-weight fix re-judged PASS
  "SOTD-class now"). ELEVATION-NOTES POLICY PROVED OUT round 1: all 4 passes got judge-directed
  Fable elevations applied + verified (commit-log centered column + hash recede; numbers needle-first
  light hierarchy; switchboard entrance cord-reel + trunk hierarchy + parked plug; corridor CTA
  stroke + monotonic rooms + floor reflection). Notable: switchboard agent caught its own CSS
  transition-race (dashoffset transition snapped; rebuilt as @keyframes - BANK: SVG line-draw
  entrances should use keyframes, not transitions).
- Batch 64 DONE + DEPLOYED (-> 310 live, Vesperwerk = 44, commit d692587). FIRST FULL AD-PIPELINE
  BATCH: 5/5 shipped (4 first-time PASS + cabinet fixed once [espresso carcass + seeded oak figure
  + milled brass] and re-judged "SOTD-class"). JUDGE FLOOR CHECK CONFIRMED THE HYPOTHESIS: "average
  visibly higher - the pipeline's fingerprint" - lai-rot-nam (FABLE-BUILT via concept-risk routing)
  = batch standout + premium-not-kitsch; soft-brutalism = judge's #1 pick for King's REAL site.
  AD stage caught 2 real scroll=0 defects verify missed (lai-rot-nam fragmenting hero card +
  unreadable text override) = the stage pays for itself. Elevation notes applied to all passes; AD
  agent correctly SKIPPED the blueprint-blue note (palette discipline over trope).
- TOKEN MEASUREMENT (King-requested, FINAL): batch 64 workflow = 1,700,725 vs baselines 62 = 1.20M /
  63 = 1.25M -> RAW +39% (above the +25-35% prediction). BUT post-judge spend collapsed: batch 63
  needed 7 post-judge agents + re-judges; batch 64 needed 2 (1 fix + 1 combined elevation pass).
  ALL-IN cost per shipped template ~ parity or slightly better, with a visibly higher floor.
  VERDICT REPORTED TO KING: keep the 3-stage pipeline.
- Batch 65 GATED (built 15/15 `wrhqr6mjc`, 1.65M tokens - pipeline cost stable; AD stage caught
  TOOL-CALL LEAKAGE text corrupting the ramakien DOM + corrected a stage-2 FALSE CLAIM: the gold
  sky band only spanned the first 1440px on desktop [flex container never grew; width:max-content
  fix] - BANK: verify agents' scroll=0 confirmations can be viewport-local; AD's independent
  capture is the safety net). MY GATE x5: FPS 107-123, dash CLEAN x5, lathe + index vlint 0/0,
  ramakien HIGH = frieze rail by-design (A/B-proven). Judge `judge-batch65` running (ramakien
  mural grammar = make-or-break).
- Batch 66 IN FLIGHT `wbvyu87k2` (Vesperwerk X): mudmee-loom-resolve (Thai ikat weave, Fable build,
  entrance resolves hero to crisp register per the parked-shoji rule), spectrogram-waterfall (SDR
  waterfall w/ the 300Hz-3.4kHz voice band as the gold ridge), end-crawl (site as cinema end
  credits, THE END -> THE BEGINNING payoff), readme-manifesto (Monospace Web discipline, VIEW
  SOURCE toggle flips rendered/raw), kranok-flame-frame (breathing ember frame, density follows
  focus). SLUG_CAT pre-added.
- Batch 65 DONE + DEPLOYED (-> 315 live, Vesperwerk = 49, commit 075c699). 5/5 FIRST-TIME PASS
  (first perfect batch at the elevated bar; lathe + editorial-index raise the floor; lathe = judge's
  conversion pick). RAMAKIEN CAVEAT surfaced to King: reads as premium HOMAGE to mural grammar,
  not literal temple density - his heritage, his call; elevations added kranok cartouche trim +
  denser registers either way. Aperture-wipe got the heavy elevation (bold Bass masses + filled
  interiors, thumb now reads BOLD).
- Batch 66 GATED (built 15/15 `wbvyu87k2`, 1.57M tokens - pipeline trend 1.70 -> 1.65 -> 1.57M):
  end-crawl + kranok vlint CLEAN 0/0, readme MEDs, mudmee + spectrogram HIGHs = pre-proven by-design
  clip classes. FPS 66-121, dash CLEAN x5. Judge `judge-batch66` running WITH A LANE-PULSE QUESTION
  (after 49 treatments: still distinct, or convergence creep?) - feeds the stopping-point call.
  FUEL: genuinely-distinct build-ready remainder ~7 = AT the audit threshold; decision after the
  pulse answer: audit round 3 vs surface the natural pause point to King.
- Batch 66 JUDGED: 3 PASS (mudmee = judge's FORCED-PICK for the real site: "arresting + unmistakably
  premium Bangkok + fast business read"; end-crawl top typography; readme best-ICP-fit) + 2 NEEDS-FIX
  (spectrogram surface reads muddy not instrument-grade; kranok anatomy reads art-nouveau-fan not
  lai kranok + hero too sparse) -> 3 agents dispatched (2 Fable fixes + 1 elevation pass).
- LANE PULSE (judge, blunt, IMPORTANT): STRUCTURAL SATURATION detected after 49 treatments. Hero
  surfaces still distinct BUT (a) the spec-chip tic now appears on ALL treatments ("one author's
  trick, not five ideas") and (b) the below-fold skeleton is nearly interchangeable (services
  columns -> clinic-still work -> numbered approach -> contact); "hero-texture novelty is not
  treatment novelty; the marginal treatment adds a hero skin to a fixed skeleton." DECISION MADE
  (loop continues per King's directive, quality-corrected): BATCH 67 carries a STRUCTURAL-VARIATION
  MANDATE - each treatment gets a DIFFERENT below-fold IA (chaptered rooms / hub-and-spoke /
  single-object-no-sections / dialogue IA / index IA) and the spec-chip is DROPPED except where
  register-native. WIND-DOWN QUESTION surfaced to King in status: the lane holds ~54 treatments
  after batch 66; the honest ceiling is closer than the hero-idea backlog implies.
- Batch 66 fixes: spectrogram re-judged PASS (frame-quantized rows + blazing ridge = "genuinely
  resolved"); kranok NEEDS-FIX round 2 -> ROUND 3 dispatched with the judge's ROOT CAUSE ("thin
  gold-on-cream perimeter is inherently low-presence at thumb scale" - contrast inversion + real
  focal center, stop patching the border); park if round 3 fails, per shoji precedent.
- Batch 67 JUDGED: 3 PASS (cutaway-illustration ★ ship-leader "submit today"; shell-session ★
  co-lead; stele PASS w/ motion notes) + 2 NEEDS-FIX (mukku = reintroduced the card-grid tic inside
  the frame, skin-not-structure + pearl-button nacre; trailer-cut = SEVERE, the acts never render on
  scroll - all scroll frames frozen title, same dead-mechanic class as commit-log). STRUCTURAL
  CORRECTION VERDICT: "worked where the architecture changed the content model" (3/5); LESSON
  BANKED: skin != structure. Fixes + elevations dispatched (mukku composition dissolve, trailer
  act-wiring w/ diagnosis of why verify+AD missed it, 3-file elevation pass). Stele click fix
  in flight (click-through class occurrence #3; CLICK-THROUGH GUARD now verify rule 8).
- kranok-flame-frame PARKED after round-3 deciding re-judge (the lane's 2nd park; file on disk,
  NOT cataloged). Rounds fixed anatomy, density, then contrast - but the certificate-border read
  survived all three and the judge's net was "premium and competent, not wow". LESSON BANKED
  (extends the shoji lesson): HAIRLINE-PERIMETER-ORNAMENT registers fight the thumbnail gate by
  construction, same family as veiled-light - a frame is supporting cast; if the concept's hero IS
  the frame, it has no commanding center to sell at 300px.
- trailer-cut re-judged PASS ("structural claim earned"; scroll-root fix worked; acts differentiate
  sparse->dense->grand). Batch 66 closes 4 shipped + 1 parked -> CATALOGED with trailer -> 320 in
  manifest (Vesperwerk = 54). LESSON BANKED as builder SCROLL ROOT RULE in _batch-workflow.js:
  page scrolls on the document root, never an inner overflow container.
- ENDGAME CONVERGENCE (two judges agree): AT MOST ONE more architecture batch (only architectures
  that also COMMUNICATE the offer: map/atlas of Bangkok districts=services, paged physical artifact
  [passport/letterpress you page through], continuous-camera diorama) then STOP and consolidate
  into the real-site flagship shortlist. Awaiting King's call on the wind-down question; default
  plan = finish 66+67 fixes -> deploy -> ONE final 3-concept batch 68 -> consolidation deliverable.
- Batch 63 FIX RESULTS: corridor door clickability FIXED (root cause = sibling stacking contexts,
  .stage z-index could never escape .scroll + an invisible faded .vinyl still ate clicks;
  pointer-events:none default + opt-in restore; occluded findings 0/0, fast-walk fires); isometric
  perf PROFILED + tuned (sway ease-in-out caused ~15 raster tasks/frame; steps(48) sampling + CSS
  containment -> idle 121, scroll ~51-54 = structural software-render residual, fine on real GPU
  per standing FPS rule). Judge `judge-batch63` running - FIRST judge under the elevation-notes
  policy.
- Batch 64 IN FLIGHT `w6d0aps7n` - FIRST FULL NEW-PIPELINE BATCH (build -> verify -> FABLE ART
  DIRECTOR) + the TOKEN MEASUREMENT batch (compare vs 62 = 1.20M / 63 = 1.25M; prediction +25-35%).
  Picks: api-console (Stripe-class sync console, Opus), lai-rot-nam-gilding (Thai gold-on-lacquer,
  FABLE builder per concept-risk routing; brief INVERTS the audit's resist-only scroll=0 to
  fully-gilded post-ritual - the parked-shoji lesson applied), voiceprint-monogram (one spoken
  word as the whole identity system, Opus), material-cabinet (oak+brass drawer wall, Opus),
  soft-brutalism (page annotates its own construction with TRUE computed measurements, Opus).
- shoji-ma PARKED after round-3 deciding re-judge (file on disk, NOT cataloged). Rounds 1-3 fixed
  clickability, luminosity, composition and the crescendo (all verified), but the judge's final
  read: the residual weaknesses are CONCEPT-INHERENT - a star seen only as a halo through
  translucent paper is structurally soft and cannot deliver a commanding gallery thumb; washi
  texture never survived downscale; mobile loses the concept entirely. LESSON BANKED: veiled-light
  registers (glow-behind-diffuser as the ONLY hero) fight the scroll=0 thumbnail gate by
  construction - prefer registers whose signature object survives small + static. Batch 62 closes
  4/5 shipped + 1 parked (the lane's first park; 61 batches, 0 parks before it).
- WORKFLOW UPGRADE (King approved 2026-07-17 ~01:00): 3-part taste plan ACTIVE. (1) _batch-workflow.js
  now has STAGE 3 = FABLE ART DIRECTOR pass on EVERY template (schema ELEVATED w/ adChanges; inherits
  session model; self-captures via harness; surgical elevation only). (2) Judges from batch 63 on
  must return 2-3 TASTE ELEVATION NOTES even on PASS - notes get applied by AD/fix agents. (3)
  Concept-risk routing: extreme-restraint + material-simulation registers get buildModel omitted
  (= Fable builds). MEASURE: compare batch-64 workflow subagent_tokens vs baselines (batch 62 =
  1,197,516; batch 63 = 1,250,387 build+verify only) + fix-round counts; report to King. Prediction
  on record: +25-35% tokens/batch, partially offset by fewer post-judge fix loops.
- Batch 63 GATED (built 10/10 `wt45pv7oy`, 0 errors; verify caught commit-log's DEAD scroll mechanic
  - missing html.anim class, entire IO choreography inert; + corridor RM layout fix + isometric RM
  fix). MY GATE: FPS 42-121 - isometric 60/42 = first sub-50 scroll reading -> Sonnet perf agent
  `fix-isometric-perf` profiling (sway/breathing/walker suspects). Dash CLEAN x5. vlint: commit-log
  + switchboard CLEAN 0/0; numbers ticks = 1px-anchor-label false positive (probed, docSW clean);
  isometric plaques = SVG-text clientWidth-0 artifact class; gallery-corridor = REAL DEFECT (door
  plaque buttons NEVER clickable at any depth - full-viewport sections eat clicks, same class as
  shoji) -> Sonnet fix `fix-corridor-clicks` (pointer-events:none default on sections/spacers).
  Judge next (WITH elevation notes per new policy); then retro-AD pass on batch-63 passes.
- LANE SCOREBOARD @28 treatments: judges rate ~15 Awwwards-submit-ready. Top tier across batches:
  bas-relief-light, planisphere-instrument, observatory-log, broadsheet-evening, almanac-of-hours,
  terminator-clock, field-notes (best SMB conversion), bibliophile-spread, riso-nocturne.
- Batch 61 WAS IN FLIGHT as `wmlu5jv6k` (Vesperwerk V, Fable-designed / Opus-built; axes: journalistic /
  illuminated manuscript / poster scale / bookbinding / aerospace): vesperwerk-broadsheet-evening
  (front page goes to press, real ICT clock, LATE EDITION palette toggle), vesperwerk-illuminated-hours
  (Book of Hours, drop cap gilds itself, vines grow, cursor-tracked leaf shimmer),
  vesperwerk-poster-crop (WERK bleeding off all four edges, scroll re-crops the giant letterform,
  overflow-hidden stage), vesperwerk-bibliophile-spread (open book, LIVING marbled endpaper flows,
  gilt tabs, tissue-guard hover), vesperwerk-mission-insignia (patch embroiders itself, T+ clock
  from registration epoch, trajectory phases). All structure-guarded, 0 WebGL. (Vesperwerk IV, Fable-designed / Opus-built; axes: WebGL jewel /
  curatorial / observatory / handmade / hospitality): vesperwerk-jeweled-vitrine (THE lane's one
  WebGL: three.js jeweled star under museum glass, capture-safe rules baked in, static CSS fallback
  = mobile + RM state), vesperwerk-auction-lot (Lot 01 catalogue with 3D page-flip plates),
  vesperwerk-observatory-log (dome cross-section opens + tracks the star's real azimuth, night-log
  entries), vesperwerk-field-notes (warm stapled logbook, taped polaroid, courts Thai SMB warmth),
  vesperwerk-evening-service (candlelit degustation menu, courses served on scroll, ribbon progress). (Vesperwerk III, Fable-designed / Opus-built, 5 new axes: operable
  celestial instrument / patent document / wow-via-absence / print craft / planetary product-story):
  vesperwerk-planisphere-instrument (drag-rotate star wheel, REAL sidereal math + bright-star catalog),
  vesperwerk-patent-plate (FIG.1 self-drawing axonometric of the Yimwhan system, claim cards, REV A
  stamp), vesperwerk-mono-ink-restraint (two-color absence register; the gold star = bookmark of light
  that leads scroll; craft bar highest), vesperwerk-riso-nocturne (two-plate riso star chart, breathing
  misregistration, snap-to-register hover, edition stamp), vesperwerk-terminator-clock (live computed
  day/night line, after-hours call pings arc to Bangkok = the PRODUCT story planetarily; honest
  SIMULATION label). All briefs now include the DOCTYPE structure guard. 0 WebGL. (Vesperwerk II, Fable-designed / Opus-built, 5 new axes vs batch 57:
  engraved-document, typographic-craft, object-card, light-as-player, artifact-ritual; 0 WebGL):
  vesperwerk-engraved-ledger (self-engraving copperplate ledger + folio-turn + stroke-count HUD),
  vesperwerk-specimen-lab (living foundry specimen, real Fraunces variable-axis testers + proof mode),
  vesperwerk-monogram-card (embossed 3D club card, cursor raking sheen, flip = articles of membership),
  vesperwerk-bas-relief-light (whole page carved stone under a cursor-held light; drag light down =
  evening payoff), vesperwerk-sealed-invitation (wax seal auto-cracks + tri-fold unfolds in entrance;
  thumbnail = OPEN letter + broken seal, never closed envelope).
- Batch 56 DONE + cataloged + DEPLOYED (-> 271 live, commit b15befa). Judge (SOTD bar, filmstrips):
  4/5 first-time PASS; clinic-digital-twin NEEDS-FIX (diorama static after boot: root cause = clock
  0.7 min/s + terminating at close while transitions are 20-40 min apart -> nothing moved in any
  capture window) -> fix agent: looping delta-timed day at ~2.4 min/s + pulsing operatory lights +
  5s-idle scrub auto-resume, RM fully gated -> re-judged PASS (clock 10:40->10:52 across strip, KPI
  18->19->20, walk events every 3-4s). Judge ship-rank: silvered-complication #1, private-bank #2,
  solari #3, mission-control #4, clinic #5. vlint false-positive class BANKED: odometer reels /
  split-flap cells / ellipsis-truncated single-line text ALL trip overflow rules by construction -
  probe page docSW==vw + eyeball before calling them defects.
- DEPLOY-CLONE GOTCHA (cost one failed push): a fresh `git clone git@github.com:Kinzen-dev/...`
  binds the DEFAULT ssh key (= Hum69 account -> push denied). The remote MUST be
  `git@github-ktpz:Kinzen-dev/ai-media-reel.git` (host alias in ~/.ssh/config with the
  id_ed25519-kinzen-dev key). Fix: `git remote set-url origin git@github-ktpz:...`.
- Batch 57 PROGRESS: build run `w1hq50d0c` = 4/5 Opus builders dropped ("Connection closed
  mid-response", transient class). DISK CHECK: atelier-faceplate BUILT+VERIFIED (ok:true; verify
  fixed hash-jump IO reveal bug), grand-ascenseur BUILT (verify-only run `wa5o53h8o` fixed a
  MISSING DOCTYPE/head/viewport wrapper - LESSON: a clean tail is NOT proof of a complete file,
  always check the head too; ok:true), other 3 never wrote -> relaunched fresh `wfs9d6h6a`.
  MY GATE both: FPS 120-121, dash CLEAN, thumbs+mobile+filmstrips captured; vlint HIGHs all
  probed BY-DESIGN (faceplate: corner-cropped rear star clipped by overflow:hidden; ascenseur:
  crown star-on-fan composition + oversized wipe/grille panels clipped by parents; page docSW==vw
  at 1440+390 on both). Judge when all 5 ready.
- Batch 56 gate RESUMED: qa-harness re-run OK (idle FPS 120-121 x5; silvered scroll 73 > 50 bar).
  Dash scan x5 CLEAN (python codepoint scan). vlint: silvered + clinic-digital-twin 0/0;
  private-bank-ledger MED x12 = INTENTIONAL odometer digit reels (overflow-y-clipped on od-* spans;
  judge to eyeball div#ticks); mission-control-live HIGH x6 @390 (feed line clipping) + solari HIGH
  (alertText both viewports, rows @390) -> two Sonnet fix agents dispatched. Remaining: re-vlint,
  motion filmstrips x5, fresh SOTD judge (filmstrips + thumbs + mobile), catalog builtBy "Fable 5",
  rsync + commit + push. /tmp/reel-deploy re-cloned fresh (old clone + /tmp/mediagen-preview were
  wiped during the pause; mobile shots + filmstrips regenerate).

## PAUSED 2026-07-03 ~00:40 (King: "paused งานไว้ก่อนครับ เดี๋ยวผมค่อยบอกให้เริ่มต่อทีหลัง") [SUPERSEDED by resume above]
DO NOT launch new batches until King resumes. EXACT RESUME POINT:
- Batch 56 (experiential backoffice, Fable, stardust formula) BUILT 10/10 `wt8u4q9dl` (~3h, heavy
  throttling near King's 5h limit but zero failures). Files on disk: private-bank-ledger,
  silvered-complication, mission-control-live, clinic-digital-twin, solari-split-flap (-backoffice).
  GATE PROGRESS: qa-harness DONE (FPS 120-121 x5, thumbs + mobile shots regenerated post-3.9s-wait).
  REMAINING on resume: (1) vlint x5 (1440+390, MED), (2) Python dash scan x5, (3) motion filmstrips
  x5 (mediagen-tpl-motion.mjs), (4) fresh judge at SOTD bar w/ filmstrips (these WERE briefed for
  liveliness - judge it fully), (5) catalog PASSes with builtBy "Fable 5" (slugs already in SLUG_CAT
  as admin), (6) rsync + commit + push /tmp/reel-deploy, (7) next batch = lane B (Vesperwerk
  experiential from _backlog-vesperwerk.json, stardust formula + motion systems now mandatory).
- Batch 55 stays PARKED (Sonnet A/B, not cataloged; broadsheet Thai fix applied on disk).
- Local :8765 server may still be running (idempotent restart per drill).
- STYLE IDEAS bank for lane A after batch 53: gradient-mesh-vibrant, art-nouveau, brutalist-mono,
  retro-terminal-amber, comic/ben-day, sticker-collage, magazine-broadsheet, pixel-arcade,
  spreadsheet-raw, kanban-board (+ paper-cut/data-noir/gov-civic/minimal-mono/glass-light consumed).
- STANDING RULES (King 2026-07-02): (1) EVERY batch ends with rsync + commit + push of /tmp/reel-deploy
  (never skip the deploy). (2) MARK THE BUILDER MODEL: at catalog time set `builtBy` on each new
  manifest entry to the model that BUILT it ("Fable 5" now; "Sonnet 5" if the A/B batch runs). The
  gallery card renders it as a gold chip (`.mdl` badge in index.html). Templates from before 2026-07-02
  predate the marker and stay unmarked.
- WOW-BAR RECALIBRATION (King 2026-07-02, CRITICAL): King reviewed batches that PASSED the full gate
  and said "ยังไม่ว้าว" - the internal judge bar is BELOW his bar. Asked which dimension is missing
  (motion-liveliness / bolder concepts / craft depth / live-vs-thumb gap); NO ANSWER YET - re-ask when
  he responds. ACTING ON BEST JUDGMENT for batch 56+ until he calibrates: (a) briefs REQUIRE a designed
  MOTION SYSTEM (entrance choreography w/ stagger, scroll-driven reveals, micro-interactions, one
  signature motion moment; prefers-reduced-motion still fully honored), (b) gate adds MOTION EVIDENCE:
  scroll-through filmstrip + hover-state shots to the judge (not static-only), (c) judge harshness up:
  "would a real Awwwards jury score this SOTD-class? fail borderline", (d) favor bolder concepts over
  safe reskins. He is reviewing batch 55 (Sonnet A/B) himself as his own test.
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
