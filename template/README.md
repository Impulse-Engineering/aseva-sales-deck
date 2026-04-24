# Aseva Prospect Deck Template — Claude Code Handoff

This folder is a self-contained template for generating customized Aseva sales decks. Hand the whole folder to Claude Code along with a prospect brief, and it can produce a tailored HTML deck without any design tool.

## What's in this folder

| File | Purpose |
|---|---|
| `README.md` | This file — the operating instructions |
| `DESIGN_SYSTEM.md` | Visual contract: colors, type, layout, slide archetypes, motifs |
| `CONTENT_GUIDE.md` | Voice rules, slide-by-slide brief, what varies vs. stays fixed |
| `Content Changes Changelog.md` | Real edits made during human review — patterns to avoid |
| `template.html` | The working HTML template, marked up with `<!-- TEMPLATE SLOT -->` comments |
| `deck-stage.js` | The slide-deck web component (do not modify) |
| `assets/` | Aseva logos, partner logos, brand imagery |

## How Claude Code uses this

Drop a prospect brief into the prompt with the customer name, logo file, industry, and their stated needs. Then:

```
Read DESIGN_SYSTEM.md, CONTENT_GUIDE.md, Content Changes Changelog.md, and template.html.
Use them as the visual + voice contract. Do not invent new slide layouts, new color
schemes, or new font sizes — copy the patterns exactly.

Given the prospect brief:
  - customer name: <name>
  - customer logo: <path/to/logo.png>
  - industry: <industry>
  - stated needs: <bullet list>

Produce a customized copy of template.html named <slug>-deck.html. Apply changes
ONLY at the spots marked <!-- TEMPLATE SLOT --> in the HTML. Keep all other slides
exactly as written. Reference CONTENT_GUIDE.md for what varies per prospect and
what stays fixed.

When customizing copy, follow the patterns in Content Changes Changelog.md:
  - No internal sales vocabulary (no "upsell", "flex", "off-catalog")
  - Lead with customer outcomes, not delivery mechanics
  - Use concrete numbers and named pains
  - Match product-name capitalization exactly
```

## Output

A single `<slug>-deck.html` file. To make it shareable as a standalone bundle, the
operator can open it in any browser as-is, or use a static-site host. All assets
live in `assets/` and are referenced by relative path.

## Constraints to remind Claude Code about

1. **Slide canvas is 1920×1080.** Never resize.
2. **Minimum body font is 24px.** Smaller fails the visual standard.
3. **Frame padding is 96px top / 120px sides / 140px bottom.** Content must clear page-meta footer.
4. **Max 3 points per partner slide, max 6 cards per capability grid.** Hard limits.
5. **Logo panel background must contrast with logo fill color.** White-on-green logo on green panel = invisible.
6. **The fixed slides (3, 5, 8, 11, 12, 13, 14) do not change per prospect.** Only the variable slots do.
