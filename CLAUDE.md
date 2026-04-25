# Aseva Slides — Claude Code Instructions

This repo serves Aseva-branded sales decks at slides.aseva.ai via a Cloudflare Worker.

## Generating a prospect deck

Before generating ANY prospect deck, read these files in order:
1. `template/DESIGN_SYSTEM.md` — color tokens, fonts, slide archetypes (the visual constraint for every slide)
2. `template/Content Changes Changelog.md` — approved copy patterns and mistakes to avoid
3. `template/template.html` — HTML/CSS patterns for each archetype; use these to build slides

Also read from the Aseva knowledge base:
4. `/Users/macmini/asevaknowledge/derivatives/aseva-writing-rules.md`
5. `/Users/macmini/asevaknowledge/derivatives/aseva-positioning.md`
6. `/Users/macmini/asevaknowledge/aseva-customer-stories.md` — always load for proof points
7. For connectivity scope: `/Users/macmini/asevaknowledge/derivatives/aseva-products-connectivity.md`
8. For cybersecurity scope: `/Users/macmini/asevaknowledge/derivatives/aseva-products-cybersecurity.md`
9. For voice scope: `/Users/macmini/asevaknowledge/derivatives/aseva-products-voice.md`

## Deck philosophy — customize heavily, look exactly like Aseva

The design system is the constraint, not the slide count or slide content. Build a custom deck for this specific prospect. Think of `template.html` as a pattern library showing the HTML/CSS for each slide archetype — use those patterns to build new slides.

**Always include (copy from template.html):**
- The `<head>` block, CSS, and `deck-stage.js` inlined as a `<script>` block
- Cover slide (update customer name; headline can be prospect-focused)
- "Who We Are" slide — Aseva identity and three-pillar positioning
- Close/CTA slide

**Build custom for this prospect:**
- A "Your Situation" slide that names their specific pain points
- Only the pillar sections relevant to them — skip pillars they don't need; go deeper on ones they do
- Capability slides focused on their industry, scale, and named pain
- A dedicated slide for any specific product they mentioned (Cato, eSentire, Teams Voice, ClearStar)
- Matching customer stories from the knowledge base as proof points
- Slide count should match brief depth: thin brief = 8–10 slides; detailed brief = 14–18

**Visual/technical contract — non-negotiable:**
- Only color tokens, fonts (Source Sans 3 + Open Sans), and archetypes from DESIGN_SYSTEM.md
- Inline `template/deck-stage.js` as a `<script>` block
- Base64-encode all images from `template/assets/`
- Canvas 1920×1080. Minimum font size 24px. No new colors or fonts.
- Every slide uses one archetype: cover, section-divider, who, provide, partner, close

## Output contract

Produce a file named `prospect-<slug>-deck.html` in the repo root.

## Wiring into the Worker

After creating the deck file:
1. Add `import <slug>DeckHtml from '../prospect-<slug>-deck.html';` to `src/index.ts`
2. Add `'/<slug>': <slug>DeckHtml` to the `routes` map
3. Commit and push to main — Conductor deploys automatically
