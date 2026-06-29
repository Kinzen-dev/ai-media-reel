#!/usr/bin/env python3
# Adds a "category" field to every _manifest.json entry.
# Source of truth = the explicit SLUG_CAT map below (hand-assigned). Any slug NOT in the map
# falls back to a keyword classifier so new templates still get a best-effort bucket
# (override by adding them to SLUG_CAT). Idempotent: safe to re-run after each batch.
# Run: python3 _categorize.py   (from showcase/templates/)
import json, sys

# Category display order + names. The gallery renders categories in THIS order.
ORDER = [
    ("interaction", "Interaction & Motion"),
    ("spatial",     "3D & Spatial"),
    ("generative",  "Generative & Data-Art"),
    ("platform",    "Platform-Primitive Showcases"),
    ("product",     "Page Purpose & Product UI"),
    ("vertical",    "Industry Verticals"),
    ("admin",       "Admin & Backoffice"),
    ("document",    "Document & Microsite Artifacts"),
    ("movement",    "Design Movements & Eras"),
    ("editorial",   "Editorial & Typographic"),
]
VALID = {k for k, _ in ORDER}

SLUG_CAT = {
    # --- Interaction & Motion (mechanic-driven: scroll, cursor, drag, reveal, marquee) ---
    "playhead": "interaction", "query": "interaction", "arc": "interaction", "film-strip": "interaction",
    "parallax-depth": "interaction", "glitch-datamosh": "interaction", "split-diptych": "interaction",
    "infinite-canvas": "interaction", "time-of-day": "interaction", "draggable-scatter": "interaction",
    "vertical-ticker": "interaction", "elastic-ribbon": "interaction", "morphing-grid": "interaction",
    "axis-shift-scroll": "interaction", "scrollytelling-chapter": "interaction", "svgmap-journey": "interaction",
    "sticky-grid-unfold": "interaction", "scroll-velocity-mood": "interaction", "blind-mask-wipe": "interaction",
    "never-ending-parallax": "interaction", "soundscape-reactive": "interaction", "motion-path-flow": "interaction",
    "sticky-iris-expansion": "interaction", "split-bisect-cursor": "interaction", "fluid-xray-reveal": "interaction",
    "magnetic-grid-snap": "interaction", "gravity-image-trail": "interaction", "ripple-click-canvas": "interaction",
    "typewriter-reveal-grid": "interaction", "noise-displacement-hover": "interaction", "spotlight-noir": "interaction",
    "diagonal-marquee-scroll": "interaction", "scroll-snap-choreography": "interaction", "real-time-collab-cursors": "interaction",
    "svg-icon-morph-nav": "interaction", "nested-marquee-matrix": "interaction", "weather-reactive-scene": "interaction",
    "device-orientation-spatial": "interaction", "page-morph-barba": "interaction", "clip-path-morph-scroll": "interaction",
    "radial-hub-menu": "interaction",
    # --- 3D & Spatial ---
    "orbit": "spatial", "space": "spatial", "liquid-distortion": "spatial", "coverflow-3d": "spatial",
    "ring-carousel": "spatial", "fold-origami": "spatial", "tech-organic-mesh": "spatial", "scroll-3d-rotation": "spatial",
    "infinite-image-tube": "spatial", "css-cube-rotator": "spatial", "lenticular-flip": "spatial", "corridor-walk": "spatial",
    "horizontal-parallax-shader": "spatial", "depth-map-tilt": "spatial", "isometric-pixel-room": "spatial",
    "css-voxel-isometric": "spatial",
    # --- Generative & Data-Art ---
    "particle-constellation": "generative", "dithered-lo-fi": "generative", "offscreen-canvas-substrate": "generative",
    "ascii-rasterizer": "generative", "generative-svg-filter": "generative", "procedural-bezier-ribbon": "generative",
    "generative-data-letterforms": "generative", "data-physics-particle-sort": "generative", "voronoi-cell-gallery": "generative",
    "reaction-diffusion-canvas": "generative", "slit-scan-temporal": "generative", "particle-image-morph": "generative",
    "gooey-metaball-merge": "generative", "css-houdini-paint": "generative", "feturbulence-organic-hero": "generative",
    "voronoi-skin-layout": "generative", "calendar-heatmap-data-hero": "generative", "truchet-tile-generative": "generative",
    "chord-diagram-hero": "generative",
    # --- Platform-Primitive Showcases (a modern web platform feature IS the point) ---
    "view-transition-morph": "platform", "zero-js-scroll-timeline": "platform", "anchor-annotated-index": "platform",
    "has-relational-reveal": "platform", "container-query-layout": "platform", "scope-cascade-gallery": "platform",
    "view-timeline-cinematic-scrub": "platform", "starting-style-burst": "platform", "color-mix-oklch-gallery": "platform",
    "blend-mode-stack-gallery": "platform", "custom-highlight-scroll": "platform", "property-gradient-brand": "platform",
    "native-carousel-filmstrip": "platform", "light-dark-adaptive-brand": "platform", "scroll-trigger-manifesto": "platform",
    "popover-invoker-glossary": "platform", "custom-highlight-reader": "platform", "scroll-timeline-chapter-nav": "platform",
    # --- Page Purpose & Product UI ---
    "generating": "product", "ops-dashboard": "product", "saas-dark-metric-hero": "product", "spec-table-hero": "product",
    "agent-chain-of-thought": "product", "pudding-scrollytell": "product", "configurator-hero": "product",
    "linkinbio-glass-stack": "product", "recipe-howto-card": "product", "interactive-timeline": "product",
    "multistep-onboarding-form": "product", "token-stream-canvas": "product", "cmd-k-portfolio": "product",
    "annotated-case-study": "product", "stat-annual-report": "product", "changelog-diff-timeline": "product",
    "split-master-detail": "product", "api-docs-dark-sidebar": "product", "mass-changelog-scroll-map": "product",
    "luxury-watch-callouts": "product", "satirical-product-void": "product",
    # --- Industry Verticals ---
    "la-carta-restaurant-character": "vertical", "fintech-trust-stack": "vertical", "devtools-live-code-hero": "vertical",
    "biotech-investor-brief": "vertical", "property-developer-presales": "vertical", "music-release-hub": "vertical",
    "esports-team-roster": "vertical", "nuclear-authority-editorial": "vertical", "masterclass-course-pdp": "vertical",
    # --- Document & Microsite Artifacts ---
    "conference-schedule-grid": "document", "interactive-cv-print-replica": "document", "uptime-status-page": "document",
    "ticket-stub-pass": "document", "countdown-rsvp-launch": "document", "e-receipt-invoice": "document",
    "digital-memorial-tribute": "document",
    # --- Design Movements & Eras ---
    "stdout": "movement", "swiss-poster": "movement", "zine-collage": "movement", "boot-sequence": "movement",
    "redacted-classified": "movement", "interface-nostalgia-os": "movement", "retro-futurism-holo": "movement",
    "liquid-glass-depth": "movement", "collage-scrapbook": "movement", "surveillance-cctv": "movement",
    "generative-stamp-collection": "movement", "webtoon-panel-scroll": "movement", "risograph-print-emulation": "movement",
    "playable-terminal-game": "movement", "skeuomorphic-mixer": "movement", "frutiger-aero-revival": "movement",
    "swiss-international-typographic": "movement", "de-stijl-mondrian": "movement", "soviet-constructivist": "movement",
    "mid-century-saul-bass": "movement", "ukiyo-e-woodblock": "movement", "art-deco-luxe": "movement",
    "memphis-neo-postmodern": "movement", "art-nouveau-organic": "movement", "bauhaus-photogram": "movement",
    "psychedelic-60s-poster": "movement",
    # --- Editorial & Typographic ---
    "bento": "editorial", "press": "editorial", "provenance": "editorial", "morph": "editorial",
    "swiss-poster ": "editorial",  # guard (unused)
    "magazine-takeover": "editorial", "blueprint-svg": "editorial", "manifesto-essay": "editorial",
    "variable-font-pressure": "editorial", "proximity-glyph-field": "editorial", "text-clip-reveal": "editorial",
    "text-on-path-poster": "editorial", "kinetic-broken-grid": "editorial", "knockout-video-type": "editorial",
    "svg-paint-order-poster": "editorial", "silent-luxury-restraint": "editorial", "broadsheet-newspaper": "editorial",
    "variable-font-axis-playground": "editorial", "neo-print-halftone-type": "editorial", "festival-lineup-poster": "editorial",
    "inflatable-balloon-type-hero": "editorial",
    # --- batch 36+ (bold/wow round) ---
    "ai-detective-narrative-hero": "product", "acid-rave-flyer": "movement",
    "svg-ferrofluid-field-lines": "generative", "oracle-card-draw-navigation": "interaction",
    # --- batch 37 (bold + market) ---
    "wealth-management-lifestyle-asset": "vertical", "cybersecurity-threat-graph": "vertical",
    "hyperpop-chromatic-overload": "movement", "moire-op-art-field": "generative", "game-map-room-nav": "interaction",
    # --- batch 38 (market + bold) ---
    "supplement-3d-product-stage": "vertical", "museum-collection-explorer": "vertical", "developer-api-code-hero": "vertical",
    "spatial-perspective-type-wall": "editorial", "future-medieval-illuminated": "movement",
    # --- batch 39 (market + bold) ---
    "luxury-resort-cinematic-stillness": "vertical", "beauty-skincare-ritual-editorial": "vertical",
    "flow-field-still-portrait": "generative", "gothic-horror-editorial": "movement", "chrome-mercury-letterpress": "editorial",
    # --- batch 40 (bold + market) ---
    "generative-woven-textile-hero": "generative", "css-voxel-data-city": "spatial",
    "ev-automotive-cinematic-hero": "vertical", "mental-health-calm-canvas": "vertical", "ben-day-pop-couture": "movement",
    # --- batch 41 (bold + market) ---
    "digital-rococo-baroque": "movement", "l-system-botanical-canvas": "generative", "vertical-elevator-floors": "interaction",
    "cpg-food-brand-bold-color": "vertical", "cloud-devops-blueprint-grid": "vertical",
    # --- batch 43 (YIMWHAN BACKOFFICE lane, King 2026-06-29) ---
    "admin-owner-overview": "admin", "admin-case-inbox": "admin", "admin-bookings-calendar": "admin",
    "admin-handoff-liveops": "admin", "admin-analytics-report": "admin",
    # --- batch 44 (Yimwhan backoffice cont.) ---
    "admin-patient-profile": "admin", "admin-ai-config": "admin", "admin-owner-dark-bento": "admin",
    "admin-live-activity": "admin", "admin-multiclinic-rollup": "admin",
    # --- batch 45 (Yimwhan backoffice LIVING-NOTE / hand-drawn aesthetic) ---
    "living-note-owner-overview": "admin", "living-note-case-inbox": "admin", "living-note-daily-brief": "admin",
    "living-note-bookings": "admin", "living-note-patient-card": "admin",
    # --- batch 46 (living-note backoffice cont.) ---
    "living-note-handoff": "admin", "living-note-analytics": "admin", "living-note-ai-config": "admin",
    "living-note-live-feed": "admin", "living-note-week-review": "admin",
}

KEYWORDS = [  # fallback for any slug not in SLUG_CAT (first match wins)
    ("spatial",    ["webgl","3d","isometric","voxel","parallax","cube","orbit","depth","tilt","fly-through","corridor"]),
    ("generative", ["particle","voronoi","reaction-diffusion","feturbulence","truchet","ascii","dither","canvas","procedural","heatmap","chord","generative"]),
    ("platform",   ["@property","scroll-timeline","view-transition","container-query","popover","highlight","anchor","color-mix","light-dark","scope","starting-style","has(",":has"]),
    ("vertical",   ["fintech","biotech","devtool","saas","restaurant","esports","property","music","course","clinic","real-estate"]),
    ("document",   ["receipt","invoice","ticket","resume","cv","schedule","status","countdown","rsvp","memorial","timetable"]),
    ("movement",   ["bauhaus","swiss","deco","nouveau","memphis","ukiyo","constructiv","mondrian","de-stijl","saul-bass","brutalist","riso","frutiger","psychedelic","retro","skeuo","noir","y3k"]),
    ("editorial",  ["editorial","newspaper","broadsheet","magazine","poster","type","typograph","essay","manifesto","letterform","serif"]),
    ("product",    ["dashboard","landing","hero","form","pricing","changelog","portfolio","timeline","configurator","report","docs","feed","report"]),
    ("interaction",["scroll","hover","cursor","drag","reveal","marquee","ticker","snap","click","swipe","nav"]),
]

def classify(t):
    s = t["slug"]
    if s in SLUG_CAT and SLUG_CAT[s] in VALID:
        return SLUG_CAT[s]
    hay = " ".join(str(t.get(k, "")) for k in ("slug", "archetype", "title", "signature", "whenToUse")).lower()
    for cat, kws in KEYWORDS:
        if any(k in hay for k in kws):
            return cat
    return "interaction"

def main():
    p = "_manifest.json"
    d = json.load(open(p))
    counts = {k: 0 for k, _ in ORDER}
    unmapped = []
    for t in d["templates"]:
        if t["slug"] not in SLUG_CAT:
            unmapped.append(t["slug"])
        c = classify(t)
        t["category"] = c
        counts[c] += 1
    json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)
    print("categorized", len(d["templates"]), "templates")
    for k, name in ORDER:
        print(f"  {counts[k]:3d}  {name}")
    if unmapped:
        print("FALLBACK-classified (not in SLUG_CAT, add them to lock the bucket):")
        for s in unmapped:
            print("   -", s)

if __name__ == "__main__":
    main()
