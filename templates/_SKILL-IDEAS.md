# SKILL IDEAS - banked from the template-factory loop

Working notes captured DURING the autonomous research -> build -> verify -> catalog loop, to be
promoted into real skills later (use `/promote-to-skill`). Two skill candidates:
(A) the loop itself (an autonomous design-template factory), and (B) award-level frontend design.
Append a dated bullet whenever a batch teaches something new. Keep it concrete and actionable.

================================================================================
## A. SKILL CANDIDATE: "autonomous template factory" (the loop as a reusable skill)
================================================================================

### What it is
A self-sustaining loop that produces many genuinely-distinct, verified, award-aspiring single-page
web templates with almost no human input: research fresh design paradigms -> build a batch in parallel
-> verify each (real browser, FPS, visual judge) -> fix -> catalog -> deploy -> launch the next batch.
Driven by Workflow-completion notifications, so it keeps going across turns until interrupted.

### Architecture (the reusable parts)
- `_batch-workflow.js` - a Workflow script: `pipeline(archetypes, build, verify)`. Each archetype is
  built by one agent (writes one self-contained HTML file), then immediately verified+polished by a
  second agent. Shared build RULES + ASSETS constants carry every hard-won lesson (see section B).
  Archetypes passed via `args` (robust parse: string|array|{archetypes}).
- `_verify-workflow.js` - verify-only (no rebuild) over existing files. The RECOVERY tool: when a
  build run dies after writing files (rate-limit / session-limit), re-run this on the slugs.
- `_manifest.json` - SINGLE SOURCE OF TRUTH (catalog). The picker `index.html` fetches it at runtime,
  so a new batch only appends to the manifest; the picker needs no edits. ONLY the orchestrator writes
  it (added a guard to the workflow prompts: agents must touch only their one template file - an agent
  once appended to the manifest itself and bypassed the judge gate).
- `_backlog-refresh.json` - archetype fuel. A research agent tops it up in MERGE mode (carry forward
  unbuilt, drop already-built, add new to 12 total), capping new-WebGL at ~2 per refresh.
- qa-harness `mediagen-tpl-verify.mjs` - headed Playwright: per slug, screenshot PC@1440 + Mobile@390,
  measure idle+scroll FPS, write thumb to `_thumbs/<slug>.png`. deviceScaleFactor:1.
- Fresh-context "visual judge" agent per batch - reads the PC+Mobile screenshots and returns a hard
  PASS / NEEDS-FIX verdict per template. WHY fresh: the main loop's context bloats with images and the
  API starts rejecting image reads; delegating keeps the perceptual ground-truth gate intact.

### Per-iteration algorithm
1. Pick 5 strongest unbuilt archetypes (limit WebGL to ~1 per batch -> cheap, fast verify).
2. Launch `_batch-workflow` (build+verify in parallel).
3. On completion: qa-harness all 5 (FPS + screenshots). Parse the workflow result for catalog metadata.
4. Fresh visual judge on the screenshots. PASS -> catalog. NEEDS-FIX -> spawn a focused fix agent ->
   re-shoot -> re-judge -> catalog.
5. Append passing templates to `_manifest.json` (Python append is safest given mixed formatting).
   Commit + deploy (rsync to the gh-pages clone, push).
6. Launch the NEXT batch (pipeline: build next while cataloging current). Refresh the backlog when low.

### The non-stop discipline (King flagged this as a skill on its own, 2026-06-20)
This is the working STYLE King wants captured, distinct from the loop's plumbing: relentless, never-idle
autonomous production that keeps quality high without supervision. Ingredients of the skill:
- NEVER end a turn idle. Drive the loop off Workflow-completion notifications; the moment a batch
  finishes you verify+judge+catalog it AND have already launched the next one. No waiting, no "should I
  continue?" - continue until the user interrupts. (King: "ห้ามหยุด", "ลุยต่อยาวๆ".)
- Pipeline, never serialize: build the next batch WHILE cataloging the current. Wall-clock is the budget.
- Quality never drops for speed: every unit passes a real gate (FPS + fresh visual judge + fix loop),
  and a stubborn unit is PARKED honestly, never shipped weak. Relentless != sloppy.
- Self-refueling: when the work-queue runs low, spawn a research agent to top it up so the loop never
  starves. Keep STATE in files so a context reset resumes seamlessly.
- Surface progress without stopping: short status pings to the user between batches, full state in files.
- Cost is not the constraint the user set; THROUGHPUT of genuinely-great units is. Spawn freely
  (build agents, verify agents, judges, fix agents, research agents) - it's a swarm, not a soloist.
- Self-correcting: bank every lesson learned into a notes file mid-run so the loop gets smarter each
  batch (this file). The longer it runs the better the output, because the rule-set compounds.
Candidate skill name: "relentless-loop" / "autonomous-factory" - a generic harness for ANY produce-
verify-improve domain (templates here, but also: bug sweeps, content batches, migrations, audits).

### Loop-discipline lessons
- NEVER trust agent self-report for quality. Gate on (a) FPS measured by the harness + (b) a fresh
  visual judge looking at the actual pixels. The verify agents catch real bugs code-reading misses
  (IntersectionObserver pause-race, SVG mask rects never appended, a seed that fades to empty in 1.5s).
- Pipeline, don't serialize: launch the next batch's build while verifying/cataloging the current one.
- Recovery drill (happened 3x): when a batch "fails", check disk FIRST - build agents write the file
  before the failing return/verify call, so the HTML usually survives. Then run `_verify-workflow`.
  - "Server is temporarily limiting requests" = transient Anthropic overload (retry soon).
  - "You've hit your session limit, resets <time>" = the USER's quota (wait for reset). Different.
- One judge per ~5 templates (10 images). More bloats the agent; fewer wastes round-trips.
- Keep STATE in files (`_manifest.json`, `_backlog-refresh.json`, `_LOOP.md`, this file) so a context
  reset can resume the loop by reading them.

================================================================================
## B. SKILL CANDIDATE: "award-level frontend design" (what makes a template land)
================================================================================

### Design principles that consistently produce award-level results
- Commit FULLY to ONE paradigm per page. The failure mode is always the same: falling back to a
  generic dark card grid + one accent. Pick a real interaction/layout idea and build the whole page
  around it (the mechanic IS the brand).
- Two-color discipline by default: near-black or bone + ONE accent; let the MEDIA bring the color.
  Use a richer palette only when the archetype demands it (riso = pink+teal, holo = iridescent).
- THE SIGNATURE MUST BE VISIBLE AT scroll=0. This is the #1 recurring defect by far (caught ~8 times).
  The first impression / catalog thumbnail is a scroll=0, no-interaction screenshot. Sub-failures:
    * title-only hero pushes the mechanic below the fold -> compact the hero so the mechanic peeks in.
    * an entrance animation is caught mid-transition (ghost text) -> seed the SETTLED end state at
      scroll=0; animate only later sections / on interaction.
    * a "frozen mid-X demo" auto-completes before the 3.5s capture -> hold the state (no auto-timeout)
      until the user actually scrolls/moves.
    * a generative effect (noise, dither, halftone) is too faint and downscales to flat -> make it
      bold enough to survive thumbnail downscale; darken grain on light grounds.
    * a lazy/observer-gated tile hasn't initialized at scroll=0 -> eager-init near-viewport tiles.
    * a WebGL canvas reads blank in capture -> preserveDrawingBuffer:true (see below).
- Type at architectural scale. Structural devices (numbers, eyebrows, labels) must encode real content
  (a true sequence), not decorate.
- Medium-as-claim: let the technique carry meaning (riso = print revival, ASCII/terminal = dev craft,
  1-bit dither = anti-AI-polish, lenticular = collectible).
- Mobile is a first-class gate, judged every time at 390px.

### Recurring TECHNICAL failure modes + the fix (the most valuable bank)
- SVG: `setAttribute('fill','var(--x)')` does NOT resolve - CSS custom properties don't work in SVG
  PRESENTATION ATTRIBUTES, so the shape renders invisible/wrong. Use a hex/rgb() literal or
  element.style.fill. (Cost 3 failed fixes on blind-mask-wipe before a DOM probe found it.)
- WebGL GLSL ES 1.0: a local `float m[64]` array read by a dynamic loop index returns 0 on ANGLE
  (Chrome's GL backend) -> the whole shader output flattens (dithered-lo-fi rendered all-paper). Use a
  LUT texture (NEAREST/REPEAT) or arithmetic; never dynamic-index a local array.
- WebGL screenshots/thumbnails: with `preserveDrawingBuffer:false` the capture reads an already-cleared
  buffer = blank canvas, even though the live page renders. Set `preserveDrawingBuffer:true` for any
  template whose thumbnail must show the GL output. Add a blank-frame readPixels probe -> CSS fallback.
- Mobile cover-crop: never object-fit:cover a landscape asset into a portrait phone viewport. Use
  object-fit:contain + a letterbox mat at <=640px. A JS-created `<video>` with inline object-fit:cover
  can beat the media-query rule by specificity -> add an explicit `.card video{object-fit:contain}`.
- prefers-reduced-motion: gate BOTH the CSS animations AND the JS rAF loop / inline-transform writes /
  autoplay, and show the settled final state. A CSS-only RM block is insufficient if JS keeps writing.
- Simultaneous video decode tanks FPS: on a shared stage play only the focused/in-view clip (a single
  active-video governor). The IntersectionObserver's first synthetic callback can pause a just-started
  video (en.isIntersecting=false momentarily) -> guard (pause only when ratio===0 && currentTime>0).
- Zero-JS templates can't gate autoplay (no IntersectionObserver) -> rest on posters, no autoplay, or
  it's a decode storm.
- crossorigin="anonymous" on a same-origin <img> taints canvas getImageData -> remove it.
- Perf budget: backdrop-filter blur is GPU-bounded (cap ~3 concurrent); mix-blend + many gradients
  repaint every frame (a transform-translated overlay is GPU-composited and far cheaper).
- SVG <mask> over a <foreignObject> video renders INVERTED on Chromium/ANGLE: the GPU-composited video
  layer escapes the SVG mask, so you get a full video rectangle with the letters punched out as black
  HOLES (the opposite of intended). Use CSS `mask-image` with an inline-SVG-text data-URI on a PLAIN DOM
  element (video/img/gradient div) instead - it clips per-glyph and survives GPU compositing. Resolve
  the SVG fill to %23fff in the data-URI, never var().
- em-based letter-spacing/tracking SCALES WITH FONT-SIZE. The exact value (e.g. 0.42em) that reads as
  tasteful tracking on a ~40px mobile headline becomes scattered illegible gaps (~56px) on a clamp()-
  sized ~134px desktop headline. A "fix on mobile" can leave desktop broken with the SAME value. Verify
  the rendered headline WIDTH fits the viewport at the LARGEST breakpoint (a fast DOM probe:
  h1.getBoundingClientRect().width < viewport), not just eyeball one size.
- A gradient sized `auto` on a full-viewport MASKED element samples only its midpoint inside small
  letterforms -> the knockout text looks like a flat solid colour. Size/position the gradient to the
  glyph BAND (background-size/background-position) so the full colour range renders inside the letters.
- `clip-path: path()` is NOT responsive - the path coordinates are fixed CSS pixels in the element's
  own box, they do NOT scale to the element. A path authored in a ~1000-unit design space looks right
  only when the element is ~1000px; on a wider viewport the path clips off a vertical strip (reads as a
  side panel, not the intended shape). For a responsive clipped shape use `clip-path: polygon()` with
  PERCENT coords (which scale), or an inline SVG `<clipPath clipPathUnits="objectBoundingBox">`. (Parked
  clip-path-morph-scroll over this; path()->path() morphs are easy to author but non-responsive.)

### Process insights
- Perceptual loop: build -> capture the REAL artifact -> critique as a demanding reviewer (composition,
  the mechanic-at-scroll=0, mobile, FPS) -> fix -> re-capture. 1-3 rounds is normal; one-shot is the
  exception. Code-correct is NOT perceptually right.
- "Logic-correct but perceptually-invisible" is a real failure class. has-relational-reveal: the violet
  rings WERE all applied (a computed-style DOM probe proved seed + 2 mates ringed, in view, 9 dimmed),
  but they were thin INSET rings over busy media and washed out at thumbnail scale. Fix = a bold OUTER
  ring on the dark ground (not clipped by the card, reads at any scale). Lesson: when a judge says "not
  visible" but you believe the code is right, probe the computed style FIRST (confirm/deny it's applied),
  then it's a contrast problem, not a logic problem. Inset rings over media < outer rings on a plain
  ground for legibility. Thumbnail downscale averages fine detail away - make signal coarse enough.
- Instrument before hypothesizing on opaque render bugs: after ~2 failed surface fixes, STOP guessing
  and probe the live DOM/computed-style/pixels. Root cause then shows in one cycle (blind-mask var(),
  dithered Bayer-LUT, scroll-3d perspective-on-scroll-container).
- A fresh-context judge that only sees the screenshots grades harder and more honestly than the agent
  that built the thing.
- Know when to PARK. css-houdini-paint resisted 3 fix rounds: the worklet IS registered and painting
  (probe-confirmed paint(ink-bleed) on a top overlay, band math reads ~21px), yet it renders as a thin
  hairline in the 1440x900 screenshot every time. CSS Houdini paint-worklet output is unreliable to
  CAPTURE in headless/thumbnail screenshots even when the live page is fine. Lesson: when the mechanic
  is a capture-fragile API (Houdini paint, possibly some WebGPU), the thumbnail can't sell it, so the
  template fails the library's purpose regardless of correctness. Better to park one stubborn template
  (mark needs-rework, bank the insight) than perfectionism-stall the loop. Great-not-sloppy is also
  served by NOT shipping a weak one. Candidate skill rule: "for a template library whose value is the
  thumbnail, prefer mechanics that render in a static capture; treat capture-fragile APIs as high-risk."

### Archetype ideas bank (paradigms that proved genuinely distinct + worked)
Bento, webgl-orbit hero, generating/denoise reel, scroll playhead, command-palette, press-kit,
museum/old-master, terminal stdout, liquid morph, chromatic arc, spotlight-noir, kinetic type, tarot
flip, blueprint, contact-sheet, brutalist index, glitch/datamosh, split-diptych, infinite canvas, ring
carousel, manifesto essay, OS boot, time-of-day, redacted/FOIA, particle constellation, fold-origami,
ops dashboard, draggable scatter, elastic ribbon, broadcast ticker, morphing grid, surveillance CCTV,
axis-shift scroll, scrollytelling chapter, bioluminescent WebGL mesh, postage-stamp loupe, liquid
glass, Win95 desktop, variable-font pressure, scrapbook collage, holographic foil, 1-bit dither,
webtoon panels, blind-mask wipe, SVG journey map, sticky-grid unlock, scroll-velocity mood, glyph
field, scroll-3d tumble, never-ending parallax, soundscape equalizer, image tube, view-transition
morph, CSS cube, sticky-iris bloom, motion-path arc, text-clip window, zero-JS scroll-timeline,
lenticular flip, text-on-path poster, cursor bisect, offscreen-canvas substrate, fluid x-ray reveal,
corridor walk, ASCII raster, broken grid, anchor-positioned annotations, magnetic snap, horizontal
WebGL lens, gravity card trail, ripple unlock, typewriter reveal, depth-map tilt, noise displacement,
riso print, diagonal marquee, playable terminal game.
Less-obvious territory still open: CSS Houdini paint, :has() relational, container queries as layout,
generative SVG filters, collab-cursor presence, data-physics particle sort, print/risograph emulation.

================================================================================
## CHANGELOG (append per batch)
================================================================================
- 2026-06-20 seed: written after batch 16 (~80 templates). Captures sections A + B from batches 1-16.
