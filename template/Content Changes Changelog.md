# Aseva Sales Deck — Content Changelog

This document records every copy change made by hand during review, so the source markdown briefs can be updated. For each entry: the slide, the original text the LLM produced, the corrected text, and the "vibe" — what the slide is trying to communicate. Use the vibe notes to steer future copy generation away from the same mistakes.

---

## Slide 03 — The Differentiator

**Vibe:** Positioning slide. We are a carrier *with* engineers, an account team, and a real service layer — not a reseller. This slide should emphasize engineering depth and security/operational expertise the team carries into every engagement. Tone is confident, technical, grounded in real operations.

### Edit 1 — lede paragraph

- **Original:**
  > Running our own network created engineers who understand circuits, failover, identity, and **policy** at depth. That expertise is *portable*. It shows up in every connectivity, voice, and cybersecurity engagement we deliver, whose ever product sits underneath.
- **Changed to:**
  > Running our own network created engineers who understand circuits, failover, identity, and **security** at depth. That expertise is *portable*. It shows up in every connectivity, voice, and cybersecurity engagement we deliver, whose ever product sits underneath.
- **Why:** "Policy" is vague and reads like corporate filler. "Security" is the concrete, customer-relevant domain we actually own. Prefer concrete technical domains over abstract governance words.

---

## Slide 06 — Connectivity · What we provide

**Vibe:** Capability grid. Each card describes a connectivity product in plain terms and explains why it matters to the customer's operations — not how we source it. Benefits over backend sourcing mechanics.

### Edit 2 — Dedicated internet card

- **Original:**
  > Symmetric dedicated internet with SLA, from 50 Mbps to multi-gig. Delivered on our own fiber in the Santa Barbara region, or on-net through a Tier 1 provider with our IP running over it.
- **Changed to:**
  > Symmetric dedicated internet with SLA, from 50 Mbps to multi-gig. Dedicated speeds mean the performance is always there when you need it.  Low latency and low jitter guaranteed.
- **Why:** The original leans into sourcing/geography, which is inside-baseball. Customers care about *performance outcomes* — speed, latency, jitter. Lead with what the customer experiences, not how the sausage is made.

---

## Slide 07 — Connectivity · Why Aseva

**Vibe:** Differentiation against the typical carrier-portal experience. This slide should feel like a pointed, almost opinionated correction of a bad industry norm. Crisp and punchy.

### Edit 3 — Headline

- **Original:**
  > Not a quote from a portal, a network from a carrier.
- **Changed to:**
  > Not a generic quote from a portal, a network designed by engineers.
- **Why:** "Network from a carrier" is tautological — every carrier sells a network. The real contrast is portal-quote versus engineer-designed network. Lead with the human expertise, not the corporate label.

### Edit 4 — Second paragraph

- **Original:**
  > We sit in a different category. We operate our own network**,** buy at the wholesale level directly from carriers, and stay in the relationship after the sale. The circuits are on our bill. The engineers stay with you.
- **Changed to:**
  > We sit in a different category. We operate our own network **or** buy at the wholesale level directly from carriers, and stay in the relationship after the sale. The circuits are on our bill. The engineers stay with you.
- **Why:** The comma made these two sourcing models sound sequential. They're actually alternatives — we do either, depending on the geography. "Or" makes the two-track reality accurate.

---

## Slide 08 — Voice (section divider)

**Vibe:** Pillar header. Short, confident, brand-accurate. Product names must be capitalized correctly.

### Edit 5 — Subheading

- **Original:**
  > Webex **voice**, Microsoft Teams Voice, and contact center, designed around how your business actually works.
- **Changed to:**
  > Webex **Voice**, Microsoft Teams Voice, and contact center, designed around how your business actually works.
- **Why:** Product-name capitalization. "Webex Voice" is a Cisco product name; it must be title-cased like "Microsoft Teams Voice" right beside it. Watch for this anywhere proper product names appear.

---

## Slide 09 — Voice · What we provide

**Vibe:** Capability grid. Practical, sales-forward. Avoid jargon like "upsell" that sounds like internal sales-speak. Avoid over-describing delivery mechanics the customer doesn't care about.

### Edit 6 — ClearStar card

- **Original:**
  > Our branded hosted voice platform, geographically hosted in multiple datacenters across the US. Cisco or Polycom handsets, native call center **upsell**, and integration with Webex as the softphone.
- **Changed to:**
  > Our branded hosted voice platform, geographically hosted in multiple datacenters across the US. Cisco or Polycom handsets, native call center **features**, and integration with Webex as the softphone.
- **Why:** "Upsell" is internal sales vocabulary — it describes our revenue motion, not the customer's experience. "Features" is what the customer actually gets. Never use sell-side language in customer-facing copy.

### Edit 7 — PRI & analog card

- **Original:**
  > PRI phone service for on-premises phone systems and PBXs, **delivered natively or via VoIP-based PRI on an Adtran IAD.** Analog lines supported where they are still the right fit.
- **Changed to:**
  > PRI phone service for on-premises phone systems and PBXs.  Analog lines supported where they are still the right fit.
- **Why:** Too much implementation detail for a capability card. "Adtran IAD" and "VoIP-based PRI" are engineering-call specifics, not sales-deck specifics. Trim delivery mechanics from capability-grid copy.

---

## Slide 11 — Cybersecurity (full stack)

**Vibe:** Survey of the security stack. Each layer card explains what we do at that layer and why it matters. Customer-benefit framing, not internal process framing.

### Edit 8 — Identity layer

- **Original:**
  > Deep working knowledge across **Entra ID and other providers**. Identity is load-bearing in every modern security deployment.
- **Changed to:**
  > Deep working knowledge across **multiple Identity providers** is load-bearing in every modern security deployment.
- **Why:** Naming a specific vendor (Entra ID) narrows the message and dates the copy. The right framing is vendor-agnostic depth. Also tightened two sentences into one.

### Edit 9 — Email security layer

- **Original:**
  > A real product on the roster through a premier email security partnership, added because customers asked.
- **Changed to:**
  > Cloud-based email security from partners like Proof-point is a must have in today's world of phishing and social engineering attacks.
- **Why:** Original was internal-roadmap framing ("added because customers asked") — customers don't care why *we* added it, they care why *they* need it. Rewrote to lead with the threat landscape (phishing, social engineering) and a recognizable partner anchor.

### Edit 10 — Pen-testing layer heading

- **Original:**
  > Pen testing & flex
- **Changed to:**
  > Pen-testing
- **Why:** "Flex" was internal shorthand for a flexible resale motion; it meant nothing to customers. Hyphenated "pen-testing" matches the brand's preferred style.

### Edit 11 — Pen-testing layer body

- **Original:**
  > Penetration testing through partner resale, plus new-opportunity flex to find the right vendor for anything off-catalog.
- **Changed to:**
  > Multiple penetration testing options brought to you by the Aseva team to ensure the security in place is actually working.
- **Why:** Same "flex"/"off-catalog" problem — internal vocabulary. Reframed around the customer outcome (verifying that existing security actually works). Emphasizes *why* a customer would want pen-testing, not how we resell it.

---

## Slide 12 — Cato / SASE

**Vibe:** Partner slide for a specific security product. Needs to be customer-benefit-forward and concrete about the operational pain Cato solves, not a generic "closest POP" description.

### Edit 12 — Global POP point

- **Original:**
  > A remote user in London hops onto the closest Cato POP for quality of service. Other platforms have not built out this dedicated POP coverage.
- **Changed to:**
  > A remote user in London connects to one of 90 global Cato POPs providing them with the same connectivity speeds as the HQ in Chicago.  No more hauling and hair-pinning VPN bottlenecks.
- **Why:** "Hops onto the closest POP for quality of service" is abstract. The new version gives a concrete number (90 POPs), a concrete user comparison (remote = HQ speeds), and names the specific pain it solves (VPN hauling and hair-pinning). Always reach for the specific pain + the specific relief.

---

# Patterns for the LLM to internalize

Taking all of the above together, here are the recurring mistakes to avoid:

1. **No internal sales vocabulary.** "Upsell", "flex", "new-opportunity flex", "added because customers asked", "off-catalog" — all cut. Customers don't speak sell-side.
2. **Lead with customer outcomes, not delivery mechanics.** Don't describe how we source circuits, which carrier we peer with, or what IAD we use. Describe the performance, the experience, the pain solved.
3. **Product-name capitalization matters.** "Webex Voice", not "Webex voice". Match other product names on the same line.
4. **Prefer concrete domains to abstract governance words.** "Security" beats "policy". "Engineers" beats "carrier". Specific, technical, human.
5. **Vendor names should anchor, not narrow.** Either say "multiple Identity providers" (vendor-agnostic depth) or "partners like Proof-point" (anchor + flexibility). Don't hard-code a single vendor as if it's the whole capability.
6. **Two sourcing tracks are "or", not a comma-list.** If the brief says "we do A or B depending on situation," use "or". A comma makes it sound sequential.
7. **Replace vague promises with concrete numbers and comparisons.** "Quality of service" → "same speeds as HQ, across 90 global POPs". Numbers + named pain (VPN hair-pinning) always win.
8. **Cut delivery specifics from capability cards.** Implementation details (Adtran IAD, VoIP-based PRI, datacenter geography) belong in engineering conversations, not sales-deck capability grids.
9. **Headlines should contrast with a bad industry norm, not restate the category.** "Not a carrier that sells a network" is tautology; "Not a portal quote, a network designed by engineers" is a real contrast.

---

*Generated from a human-review pass on `Aseva Sales Deck.html`.*
