# Aseva Sales Deck — Content Guide

Voice rules, slide-by-slide brief, and the variable-vs-fixed map for prospect customization.

---

## 1. Voice rules

Pulled from real review edits. Apply to every line of copy.

1. **No internal sales vocabulary.** Banned words: "upsell", "flex", "off-catalog", "new-opportunity", "added because customers asked", "roster", "represent". Customers don't speak sell-side.
2. **Lead with customer outcomes, not delivery mechanics.** Don't describe how we source circuits, which datacenter we peer in, what IAD we use. Describe the performance, the experience, the pain solved.
3. **Product-name capitalization.** "Webex Voice" not "Webex voice". "Microsoft Teams Voice". "CrowdStrike Falcon Complete". Always check.
4. **Concrete domains beat abstract ones.** "Security" beats "policy". "Engineers" beats "carrier". "Identity providers" beats "IAM stack".
5. **Vendor names anchor, don't narrow.** Either "multiple Identity providers" (vendor-agnostic) or "partners like Proofpoint" (anchor + flexibility). Don't hard-code one vendor as the whole capability.
6. **Concrete numbers and named pains.** "90 global Cato POPs", "same speeds as HQ", "no more VPN hair-pinning" beats "good quality of service".
7. **Cut delivery specifics from capability cards.** Engineering-call details (Adtran IAD, VoIP-based PRI) don't belong in a sales deck.
8. **Headlines should contrast with a bad industry norm, not restate the category.** "Not a portal quote, a network designed by engineers" beats "We are a carrier".
9. **"Or" not comma when sourcing options are alternatives.** "We operate our own network or buy at wholesale" — not a comma list, not sequential.
10. **Tone is confident, technical, grounded.** Never apologetic, never marketing-fluff, never "elevate your business" generalities.

---

## 2. Slide-by-slide brief

The deck has 14 slides. Each slide has a fixed *vibe* and a fixed *role*.

### Slide 01 — Cover
- **Role:** Set tone and identity in 3 seconds.
- **Vibe:** Confident, brand-anchored. Aseva logo, three-pillar tagline, headline that names the buyer relationship ("trusted extension of your IT team").
- **Fixed:** All copy. Logo. Background.
- **Variable:** *Customer name plate* — small line above or below kicker reading "Prepared for `<Customer Name>`" — see TEMPLATE SLOT in HTML.

### Slide 02 — Who we are
- **Role:** Position Aseva as one team running cyber + voice + connectivity.
- **Vibe:** Plainspoken, operational, 30-year heritage hint without being boastful.
- **Fixed:** Headline, three-pillar framing.
- **Variable:** Lede paragraph can swap a sentence to acknowledge the prospect's situation if you have it from the brief. Otherwise leave as-is.

### Slide 03 — The Differentiator
- **Role:** Stake the claim — we are a carrier *with* engineers, not a reseller.
- **Vibe:** Pointed, technical, confident. Three bordered cards on a navy background.
- **Fixed:** All copy. Do not customize per prospect.

### Slide 04 — Why work with us
- **Role:** Four numbered things you get every engagement.
- **Vibe:** Promise-list, but specific (live humans, wholesale relationships, etc.) not generic.
- **Fixed:** All copy.

### Slide 05 — Connectivity (section divider)
- **Role:** Pillar header.
- **Vibe:** Big, navy, waveform. "Pillar one. Connectivity."
- **Fixed:** All copy.

### Slide 06 — Connectivity · What we provide
- **Role:** Capability grid for the connectivity pillar.
- **Vibe:** Practical, benefit-led. Six capability cards.
- **Fixed:** Card structure and the core capabilities.
- **Variable:** *Card content can be re-ordered* to put the prospect's stated need first. If the prospect explicitly mentions colocation, lead with the colo card. See TEMPLATE SLOT.

### Slide 07 — Connectivity · Why Aseva
- **Role:** Differentiate from the portal-quote experience.
- **Vibe:** Pointed contrast against industry norm.
- **Fixed:** All copy.

### Slide 08 — Voice (section divider)
- **Role:** Pillar header.
- **Fixed:** All copy.

### Slide 09 — Voice · What we provide
- **Role:** Capability grid for the voice pillar.
- **Fixed:** Card content.
- **Variable:** Re-order to highlight prospect's voice priority (Teams Voice for Microsoft shops, contact center for service-heavy industries, etc.).

### Slide 10 — Voice · Why Aseva
- **Role:** Voice-pillar differentiator.
- **Fixed:** All copy.

### Slide 11 — Cybersecurity (full stack)
- **Role:** Survey the security stack with vendor-agnostic depth.
- **Vibe:** Layered, comprehensive. Each layer card explains what we cover at that layer and why it matters.
- **Fixed:** Layer structure and copy.
- **Variable:** If the prospect names an industry with specific compliance demands (healthcare = HIPAA, finance = PCI/SOX, etc.), the lede can mention it. See TEMPLATE SLOT.

### Slide 12 — Cato / SASE
- **Role:** Anchor partner slide for SASE.
- **Vibe:** Specific operational pain (VPN hair-pinning) + specific relief (90 POPs, HQ-equivalent speeds).
- **Fixed:** All copy.

### Slide 13 — eSentire / MDR
- **Role:** Anchor partner slide for managed detection & response.
- **Fixed:** All copy.

### Slide 14 — Close
- **Role:** Schedule-the-call CTA.
- **Vibe:** Confident, navy, full-bleed waveform, big headline.
- **Fixed:** All copy.
- **Variable:** Footer line can include the rep's direct line if provided in the brief.

---

## 3. Variable-vs-fixed cheat sheet

What changes per prospect, in priority order:

| Change | Where | How |
|---|---|---|
| Customer name plate | Slide 01 cover | TEMPLATE SLOT: `customer_name` |
| Customer logo (optional, paired with Aseva on cover) | Slide 01 | TEMPLATE SLOT: `customer_logo_path` (omit if none) |
| Industry-aware lede sentence | Slide 02 | TEMPLATE SLOT: `who_lede_industry_line` |
| Capability card ordering | Slide 06, 09 | Reorder card divs based on prospect's stated needs |
| Compliance hint | Slide 11 | TEMPLATE SLOT: `cyber_compliance_line` |
| Optional "Your situation" insert slide | After Slide 02 | TEMPLATE SLOT: `prospect_situation_slide` (a single slide mapping their needs to our pillars; only insert if the brief gives you 3+ specific needs) |
| Rep contact line | Slide 14 footer | TEMPLATE SLOT: `rep_contact_line` |

What stays fixed across every prospect:

- All differentiator and "why us" copy (slides 3, 4, 7, 10)
- All section dividers (slides 5, 8)
- All partner slides (slides 12, 13)
- All capability core copy — only ordering changes
- All visual styling, layout, type sizes, colors, motifs

---

## 4. Optional: prospect situation slide

If the brief gives 3+ concrete needs, insert a slide between Slide 02 and Slide 03 that mirrors the prospect's needs back at them. Use the partner-slide layout (`.partner`) but with:

- Logo panel = the prospect's logo on a `--blue-extra-light` background
- Right column eyebrow = "Your situation"
- Right column headline = a one-line summary you write from the brief
- Right column points = 3 bullet points, each pairing a stated need with the Aseva pillar that addresses it ("Multi-site connectivity → our connectivity engineers", "HIPAA compliance → our cybersecurity stack with eSentire MDR", etc.)

Skip this slide if the brief is too thin or the points would feel generic.

---

## 5. Fact-check rules

Never invent:
- Prospect names, industries, or facts not in the brief
- Aseva customers, case studies, or testimonials
- Specific numbers about Aseva's network (POP count, customer count, revenue) beyond what is in the existing slide copy
- Compliance certifications Aseva does or doesn't hold

When in doubt, leave the existing copy alone. The deck works without prospect-specific embellishment.
