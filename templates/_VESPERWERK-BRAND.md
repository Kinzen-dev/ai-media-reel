# VESPERWERK - canonical brand + content spec

Every `vesperwerk-*` template build agent MUST read this file first and mirror the copy EXACTLY,
so King compares STYLE TREATMENTS of the same site, never different content. The REGISTER
(art direction) is the only thing that varies per template. WOW MANDATE (King 2026-07-02):
every treatment must be genuinely wow, never AI slop - no generic dark-SaaS gradient hero,
no glowing bento grid, no purple-AI cliche, no templated component look. Commit fully to one
register.

## Facts
- Vesperwerk is King's newly registered software company (registered 2026). Founder-led
  independent software + AI studio based in Bangkok, Thailand.
- Audience: prospective clients (international + Thai), senior-level buyers.
- Copy language: ENGLISH (assumption flagged to King: international-client register).
- The name comes from Vesper, the evening star.

## Logo / mark
- Mark: eight-point vesper star, antique gold, two-facet bevel. Reusable asset:
  `../assets/vesperwerk-star.svg` (reference it or inline the SVG; keep facet colors).
- Wordmark: VESPERWERK all caps, Playfair Display 500-600 via Google Fonts (verified closest
  match to the real logo serif; Cormorant Garamond acceptable where a lighter voice fits),
  letter-spacing 0.18-0.25em, ink on light / cream on dark.
- Brand anchors: ink #2e2a26, antique gold #a8802f (facets #c09a4a light / #8a6526 dark),
  warm white / cream grounds (#faf7f1 class). A treatment MAY reinterpret palette and mood,
  but the star mark + serif wordmark must stay recognizable.

## Canonical copy (mirror EXACTLY; no em or en dashes anywhere)
- Hero positioning: "An independent software and AI studio. We architect, build, and operate
  production systems for businesses that cannot afford them to fail."
- Hero CTA: "Start a conversation" (secondary: "See our work")
- Services (3):
  1. AI Systems: "Voice agents, LLM assistants, and the evaluation infrastructure that keeps
     them honest. AI that answers like your best employee, in production, around the clock."
  2. Product Engineering: "Full-stack product engineering from architecture to operations:
     event-driven backends, modern web frontends, and infrastructure that scales without drama."
  3. Commerce and Platforms: "Deep Shopify and LINE platform work: storefronts, admin apps,
     integrations, and the messaging rails Southeast Asian commerce runs on."
- Selected work (flagship): Yimwhan AI: "An AI voice and LINE assistant for dental clinics in
  Thailand. It answers after-hours calls, books and reschedules appointments, and hands off to
  staff the moment a human matters. In production at live clinics."
  (Media: `../assets/flux-clinic-4k.png` fits this case; use it if the register wants imagery.)
- Approach (4 principles):
  1. Architecture first: "We design the system before we write the code."
  2. Production-worthy: "Demos impress; production endures. We build for the second one."
  3. Scope discipline: "The most valuable thing we tell clients is what not to build."
  4. Senior hands: "No juniors learning on your budget. Founder-led, senior hands on every line."
- About: "Vesperwerk takes its name from the evening star: the first light you can navigate by.
  We are a founder-led studio in Bangkok building software for businesses across Asia and beyond."
- Contact: "kittipong.k@vesperwerk.com" (CONFIRMED by King 2026-07-02) + "Bangkok, Thailand"
- Footer: star mark + VESPERWERK + "Bangkok, Thailand" + "(c) 2026 Vesperwerk"

## Required sections per treatment
HERO (mark + wordmark + positioning + CTA), SERVICES (3), SELECTED WORK (Yimwhan flagship),
APPROACH (4 principles), ABOUT (name origin), CONTACT / FOOTER.

## Standing gates (same as every template in this library)
- Signature visible at scroll=0 at 1440x900 AND 390px (thumbnail = scroll=0 shot).
- Mobile 390 clean: single-column logic, no landscape cover-crop, zero horizontal overflow.
- GEOMETRY (vlint-checked): min-width:0 on flex children; truncate/wrap; no element wider
  than its container; zero page overflow at 390 and 1440.
- prefers-reduced-motion fully honored (gate rAF / inline transforms too).
- NO em dashes or en dashes anywhere (hyphen with spaces, colon, parens).
- Self-contained single HTML file; content in a top DATA array; first-line TEMPLATE comment.
