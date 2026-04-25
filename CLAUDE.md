# Aseva Slides — Claude Code Instructions

This repo serves Aseva-branded sales decks at slides.aseva.ai via a Cloudflare Worker.

## Generating a prospect deck

Before generating ANY prospect deck, read these files in order:
1. `template/DESIGN_SYSTEM.md` — visual contract (colors, type, layout archetypes)
2. `template/CONTENT_GUIDE.md` — slide-by-slide brief, variable vs. fixed map, voice rules
3. `template/Content Changes Changelog.md` — approved copy patterns, mistakes to avoid
4. `template/template.html` — the master 14-slide template (clone this, do not modify it)

Also read from the Aseva knowledge base:
5. `/Users/macmini/asevaknowledge/derivatives/aseva-writing-rules.md`
6. `/Users/macmini/asevaknowledge/derivatives/aseva-positioning.md`
7. For connectivity scope: `/Users/macmini/asevaknowledge/derivatives/aseva-products-connectivity.md`
8. For cybersecurity scope: `/Users/macmini/asevaknowledge/derivatives/aseva-products-cybersecurity.md`
9. For voice scope: `/Users/macmini/asevaknowledge/derivatives/aseva-products-voice.md`

## Output contract

Produce a file named `prospect-<slug>-deck.html` in the repo root (e.g. `prospect-selectstaffing-deck.html`).

- Clone `template/template.html` exactly — only fill in `<!-- TEMPLATE SLOT -->` positions
- Inline `template/deck-stage.js` as a `<script>` block (replace `<script src="deck-stage.js"></script>`)
- Base64-encode all images from `template/assets/` (replace `src="assets/..."` with data URIs)
- Do NOT change any slide copy outside TEMPLATE SLOT markers
- Do NOT resize the 1920×1080 canvas or use fonts outside Source Sans 3 + Open Sans
- Minimum font size: 24px

## Wiring into the Worker

After creating the deck file:
1. Add `import <slug>DeckHtml from '../prospect-<slug>-deck.html';` to `src/index.ts`
2. Add `'/<slug>': <slug>DeckHtml` to the `routes` map
3. Commit and push to main — Conductor deploys automatically

## Fixed vs variable slides

Fixed (never change per prospect): slides 3, 5, 7, 8, 10, 12, 13, 14
Variable (TEMPLATE SLOT markers): slides 1 (customer name plate), 2 (industry lede), 6 (connectivity card order), 9 (voice card order), 11 (compliance hint), 14 footer (rep contact)
Optional: prospect situation slide between slides 2 and 3 — only insert if the brief gives 3+ specific needs
