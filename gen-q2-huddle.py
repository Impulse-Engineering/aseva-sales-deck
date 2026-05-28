#!/usr/bin/env python3
"""Generate q2-huddle-2026-deck.html from assets."""
import base64, pathlib, re

REPO = pathlib.Path(__file__).parent
ASSETS = REPO / "template" / "assets"
JS_SRC = REPO / "template" / "deck-stage.js"

logo_b64 = base64.b64encode((ASSETS / "aseva-horizontal.png").read_bytes()).decode()
logo_data = f"data:image/png;base64,{logo_b64}"
deck_js   = JS_SRC.read_text()

WAVEFORM_FULL = """<svg class="wave-bg" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <g fill="#00a1e2" opacity="0.22">
      <rect x="70" y="560" width="16" height="40" rx="2"/>
      <rect x="110" y="500" width="16" height="160" rx="2"/>
      <rect x="150" y="420" width="16" height="320" rx="2"/>
      <rect x="190" y="340" width="16" height="480" rx="2"/>
      <rect x="230" y="280" width="16" height="600" rx="2"/>
      <rect x="270" y="230" width="16" height="700" rx="2"/>
      <rect x="310" y="200" width="16" height="760" rx="2"/>
      <rect x="350" y="180" width="16" height="800" rx="2"/>
      <rect x="390" y="170" width="16" height="820" rx="2"/>
      <rect x="430" y="180" width="16" height="800" rx="2"/>
      <rect x="470" y="210" width="16" height="740" rx="2"/>
      <rect x="510" y="260" width="16" height="640" rx="2"/>
      <rect x="550" y="320" width="16" height="520" rx="2"/>
      <rect x="590" y="380" width="16" height="400" rx="2"/>
      <rect x="630" y="430" width="16" height="300" rx="2"/>
      <rect x="670" y="470" width="16" height="220" rx="2"/>
      <rect x="710" y="500" width="16" height="160" rx="2"/>
      <rect x="750" y="520" width="16" height="120" rx="2"/>
      <rect x="790" y="540" width="16" height="80" rx="2"/>
      <rect x="830" y="550" width="16" height="60" rx="2"/>
    </g>
  </svg>"""

WAVEFORM_SOFT = """<svg class="wave-soft" viewBox="0 0 1000 1000" aria-hidden="true">
    <g fill="#00a1e2">
      <rect x="70" y="560" width="16" height="40"/><rect x="110" y="500" width="16" height="160"/><rect x="150" y="420" width="16" height="320"/><rect x="190" y="340" width="16" height="480"/><rect x="230" y="280" width="16" height="600"/><rect x="270" y="230" width="16" height="700"/><rect x="310" y="200" width="16" height="760"/><rect x="350" y="180" width="16" height="800"/><rect x="390" y="170" width="16" height="820"/><rect x="430" y="180" width="16" height="800"/><rect x="470" y="210" width="16" height="740"/><rect x="510" y="260" width="16" height="640"/><rect x="550" y="320" width="16" height="520"/><rect x="590" y="380" width="16" height="400"/><rect x="630" y="430" width="16" height="300"/><rect x="670" y="470" width="16" height="220"/><rect x="710" y="500" width="16" height="160"/><rect x="750" y="520" width="16" height="120"/>
    </g>
  </svg>"""

CORNER_LOGO = f'<img src="{logo_data}" alt="Aseva" class="corner-logo" />'

ECOSYSTEM_SVG = """<svg viewBox="0 0 1440 500" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:500px;">
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 1 L9 5 L0 9 Z" fill="#00a1e2"/>
    </marker>
    <marker id="aht" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 1 L9 5 L0 9 Z" fill="#00a1e2"/>
    </marker>
    <marker id="ah-big" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M0 1 L9 5 L0 9 Z" fill="#051a35"/>
    </marker>
  </defs>

  <!-- Sales &amp; Marketing (navy filled, far left) -->
  <rect x="10" y="190" width="185" height="115" rx="10" fill="#051a35"/>
  <text x="102" y="243" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="26" font-weight="600" fill="#ffffff">Sales &amp;</text>
  <text x="102" y="275" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="26" font-weight="600" fill="#ffffff">Marketing</text>

  <!-- Account Management -->
  <rect x="285" y="190" width="210" height="115" rx="10" fill="#ffffff" stroke="#051a35" stroke-width="2.5"/>
  <text x="390" y="243" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="26" font-weight="600" fill="#051a35">Account</text>
  <text x="390" y="275" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="26" font-weight="600" fill="#051a35">Management</text>

  <!-- Billing -->
  <rect x="600" y="55" width="175" height="105" rx="10" fill="#ffffff" stroke="#051a35" stroke-width="2.5"/>
  <text x="688" y="115" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="28" font-weight="600" fill="#051a35">Billing</text>

  <!-- Accounting -->
  <rect x="1010" y="10" width="185" height="100" rx="10" fill="#ffffff" stroke="#051a35" stroke-width="2.5"/>
  <text x="1103" y="68" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="28" font-weight="600" fill="#051a35">Accounting</text>

  <!-- SI / PM -->
  <rect x="1010" y="195" width="185" height="105" rx="10" fill="#ffffff" stroke="#051a35" stroke-width="2.5"/>
  <text x="1103" y="255" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="28" font-weight="600" fill="#051a35">SI / PM</text>

  <!-- TAC -->
  <rect x="600" y="340" width="175" height="105" rx="10" fill="#ffffff" stroke="#051a35" stroke-width="2.5"/>
  <text x="688" y="400" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="28" font-weight="600" fill="#051a35">TAC</text>

  <!-- NOC -->
  <rect x="1010" y="375" width="185" height="105" rx="10" fill="#ffffff" stroke="#051a35" stroke-width="2.5"/>
  <text x="1103" y="435" text-anchor="middle" font-family="Source Sans 3, sans-serif" font-size="28" font-weight="600" fill="#051a35">NOC</text>

  <!-- ARROWS -->

  <!-- Sales &amp; Marketing to Account Management (one-way, thick navy) -->
  <line x1="197" y1="247" x2="283" y2="247" stroke="#051a35" stroke-width="4" marker-end="url(#ah-big)"/>

  <!-- Account Management to/from Billing (diagonal up-right) -->
  <line x1="450" y1="210" x2="598" y2="140" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- Account Management to/from TAC (diagonal down-right) -->
  <line x1="450" y1="285" x2="598" y2="355" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- Billing to/from Accounting (diagonal up-right) -->
  <line x1="777" y1="90" x2="1008" y2="55" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- Billing to/from SI/PM (diagonal down-right) -->
  <line x1="777" y1="130" x2="1008" y2="220" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- Accounting to/from SI/PM (vertical) -->
  <line x1="1103" y1="112" x2="1103" y2="193" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- SI/PM to/from NOC (vertical) -->
  <line x1="1103" y1="302" x2="1103" y2="373" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- TAC to/from NOC (horizontal) -->
  <line x1="777" y1="410" x2="1008" y2="415" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>

  <!-- TAC to/from SI/PM (diagonal up-right) -->
  <line x1="777" y1="365" x2="1008" y2="290" stroke="#00a1e2" stroke-width="2.5" marker-start="url(#aht)" marker-end="url(#ah)"/>
</svg>"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Aseva — 2026 Q2 Extended Huddle</title>
<template id="__bundler_thumbnail">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
    <rect width="400" height="300" fill="#051a35"/>
    <g fill="#00a1e2" transform="translate(140, 110)" opacity="0.9">
      <rect x="0" y="36" width="6" height="8"/>
      <rect x="12" y="28" width="6" height="24"/>
      <rect x="24" y="18" width="6" height="44"/>
      <rect x="36" y="8" width="6" height="64"/>
      <rect x="48" y="2" width="6" height="76"/>
      <rect x="60" y="0" width="6" height="80"/>
      <rect x="72" y="4" width="6" height="72"/>
      <rect x="84" y="14" width="6" height="52"/>
      <rect x="96" y="26" width="6" height="28"/>
      <rect x="108" y="34" width="6" height="12"/>
    </g>
    <text x="200" y="220" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-weight="300" font-size="42" letter-spacing="-1">aseva</text>
  </svg>
</template>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;600;700&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
<script>{deck_js}</script>
<style>
  :root {{
    --primary: #051a35;
    --secondary: #00a1e2;
    --supplemental: #0071ce;
    --blue-light: #86C1E9;
    --blue-extra-light: #EEFAFF;
    --grey: #475467;
    --grey-medium: #7b8792;
    --grey-light: #F0F3F4;
    --white: #ffffff;
    --coral: #EF6B51;
    --font-heading: "Source Sans 3", "Source Sans Pro", sans-serif;
    --font-body: "Open Sans", sans-serif;
  }}
  html, body {{ margin: 0; padding: 0; background: #000; font-family: var(--font-body); color: var(--primary); }}
  deck-stage {{ background: #000; }}

  section {{
    background: #ffffff;
    color: var(--primary);
    font-family: var(--font-body);
    overflow: hidden;
    position: relative;
  }}

  .frame {{
    position: absolute;
    inset: 0;
    padding: 96px 120px 140px 120px;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
  }}

  .eyebrow {{
    font-family: var(--font-body);
    font-weight: 600;
    font-size: 24px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--secondary);
    margin: 0 0 28px 0;
  }}

  h2.title {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 72px;
    line-height: 1.1;
    letter-spacing: -0.005em;
    margin: 0 0 48px 0;
    color: var(--primary);
  }}
  h3.sub {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 32px;
    line-height: 1.25;
    margin: 0;
    color: var(--secondary);
  }}
  .lede {{
    font-family: var(--font-body);
    font-weight: 400;
    font-size: 36px;
    line-height: 1.35;
    color: var(--primary);
    max-width: 1350px;
  }}

  /* Corner logo + page numbers */
  .corner-logo {{
    position: absolute;
    top: 48px;
    left: 120px;
    height: 36px;
  }}
  .page-meta {{
    position: absolute;
    bottom: 44px;
    left: 120px;
    right: 120px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: var(--font-body);
    font-size: 24px;
    color: var(--grey);
    letter-spacing: 0.04em;
  }}
  .page-meta .rule {{ flex: 1; height: 1px; background: #d1d6dc; margin: 0 24px; }}

  /* Cover */
  .cover {{ background: var(--primary); color: var(--white); }}
  .cover .frame {{
    padding: 0;
    justify-content: center;
    align-items: flex-start;
    padding-left: 140px;
  }}
  .cover .wave-bg {{
    position: absolute;
    right: -140px;
    top: 50%;
    transform: translateY(-50%);
    width: 1100px;
    height: 1100px;
    opacity: 0.85;
  }}
  .cover .kicker {{
    font-family: var(--font-heading);
    font-weight: 300;
    font-size: 52px;
    line-height: 1.2;
    color: var(--white);
    margin: 0 0 24px 0;
    max-width: 1050px;
  }}
  .cover .kicker em {{
    font-style: normal;
    color: var(--secondary);
    font-weight: 600;
  }}
  .cover .footer-line {{
    position: absolute;
    left: 140px;
    bottom: 64px;
    font-family: var(--font-body);
    font-size: 24px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.55);
  }}

  /* Section divider */
  .section-divider {{ background: var(--primary); color: var(--white); }}
  .section-divider .frame {{ justify-content: center; padding-left: 140px; }}
  .section-divider .kicker {{
    font-family: var(--font-body);
    font-weight: 600;
    font-size: 24px;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: var(--secondary);
    margin: 0 0 32px 0;
  }}
  .section-divider h2 {{
    font-family: var(--font-heading);
    font-weight: 400;
    font-size: 100px;
    line-height: 1.0;
    letter-spacing: -0.015em;
    color: var(--white);
    margin: 0;
    max-width: 1400px;
  }}
  .section-divider .sub-text {{
    font-family: var(--font-heading);
    font-weight: 300;
    font-size: 40px;
    color: rgba(255,255,255,0.7);
    margin-top: 32px;
    max-width: 1300px;
    line-height: 1.35;
  }}

  /* Diff (dark, 3 cards) */
  .diff {{ background: var(--primary); color: var(--white); }}
  .diff .eyebrow {{ color: var(--secondary); }}
  .diff h2.title {{ color: var(--white); font-size: 60px; margin-bottom: 32px; }}
  .diff .three {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-top: 24px;
  }}
  .diff .card {{
    border-top: 2px solid var(--secondary);
    padding-top: 24px;
  }}
  .diff .card h4 {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 30px;
    color: var(--secondary);
    margin: 0 0 14px 0;
    letter-spacing: 0.01em;
  }}
  .diff .card p {{
    font-family: var(--font-body);
    font-size: 26px;
    line-height: 1.5;
    color: rgba(255,255,255,0.82);
    margin: 0;
  }}
  .diff .wave-soft {{
    position: absolute;
    right: -200px;
    bottom: -200px;
    width: 700px;
    opacity: 0.12;
  }}

  /* Why (pillars) */
  .why .pillars {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px 64px;
    margin-top: 12px;
  }}
  .why .pillar {{
    display: grid;
    grid-template-columns: 80px 1fr;
    gap: 20px;
    align-items: start;
  }}
  .why .num {{
    font-family: var(--font-heading);
    font-weight: 300;
    font-size: 80px;
    line-height: 0.9;
    color: var(--secondary);
    letter-spacing: -0.02em;
  }}
  .why .pillar h4 {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 30px;
    color: var(--primary);
    margin: 8px 0 10px 0;
  }}
  .why .pillar p {{
    font-family: var(--font-body);
    font-size: 24px;
    line-height: 1.5;
    color: var(--grey);
    margin: 0;
  }}

  /* Field focus (dark 2-column) */
  .field {{ background: var(--primary); color: var(--white); }}
  .field .frame {{ padding-top: 100px; }}
  .field .eyebrow {{ color: var(--secondary); }}
  .field h2.title {{ color: var(--white); font-size: 60px; margin-bottom: 40px; }}
  .field .two {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    margin-top: 8px;
  }}
  .field .col {{
    border-top: 2px solid var(--secondary);
    padding-top: 28px;
  }}
  .field .col h4 {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 32px;
    color: var(--secondary);
    margin: 0 0 16px 0;
  }}
  .field .col p {{
    font-family: var(--font-body);
    font-size: 26px;
    line-height: 1.55;
    color: rgba(255,255,255,0.82);
    margin: 0;
  }}

  /* Discussion (light) */
  .discuss .frame {{ justify-content: center; align-items: flex-start; padding-left: 140px; }}
  .discuss .big-q {{
    font-family: var(--font-heading);
    font-weight: 300;
    font-size: 80px;
    line-height: 1.1;
    color: var(--primary);
    max-width: 1400px;
    margin: 0;
  }}
  .discuss .big-q em {{
    font-style: normal;
    color: var(--secondary);
    font-weight: 600;
  }}

  /* Ecosystem diagram slide */
  .ecosystem .frame {{ padding-top: 90px; }}
  .ecosystem h2.title {{ font-size: 56px; margin-bottom: 20px; }}

  /* New structure (whyus-style) */
  .newstruct .split {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    margin-top: 24px;
    align-items: start;
  }}
  .newstruct .left h2 {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 60px;
    line-height: 1.08;
    color: var(--primary);
    margin: 0 0 28px 0;
  }}
  .newstruct .left h2 em {{ font-style: normal; color: var(--secondary); }}
  .newstruct .left p {{
    font-family: var(--font-body);
    font-size: 26px;
    line-height: 1.55;
    color: var(--grey);
    margin: 0 0 20px 0;
  }}
  .newstruct .reasons {{ display: flex; flex-direction: column; gap: 24px; margin-top: 8px; }}
  .newstruct .reason {{
    display: grid;
    grid-template-columns: 48px 1fr;
    gap: 20px;
    align-items: start;
    padding-bottom: 20px;
    border-bottom: 1px solid #d1d6dc;
  }}
  .newstruct .reason:last-child {{ border-bottom: 0; }}
  .newstruct .reason .idx {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 26px;
    color: var(--secondary);
    line-height: 1.1;
  }}
  .newstruct .reason h5 {{
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 26px;
    color: var(--primary);
    margin: 0 0 6px 0;
    line-height: 1.2;
  }}
  .newstruct .reason p {{
    font-family: var(--font-body);
    font-size: 24px;
    line-height: 1.5;
    color: var(--grey);
    margin: 0;
  }}

  .rule-cyan {{ width: 96px; height: 4px; background: var(--secondary); margin-bottom: 32px; }}
</style>
</head>
<body>

<deck-stage width="1920" height="1080">

<!-- ================= 01 COVER ================= -->
<section data-label="01 Cover" class="cover">
  {WAVEFORM_FULL}
  <div class="frame">
    <div>
      <img src="{logo_data}" alt="Aseva" style="height:160px;width:auto;margin-bottom:56px;display:block;filter:brightness(0) invert(1);" />
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.32em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-bottom:40px;">2026 Q2 Extended Huddle</div>
      <p class="kicker">Shifting from getting the house in order to <em>growth and strategic execution</em>.</p>
    </div>
  </div>
  <div class="footer-line">aseva.com &nbsp;&middot;&nbsp; May 2026</div>
</section>

<!-- ================= 02 THE SHIFT ================= -->
<section data-label="02 The Shift" class="section-divider">
  <div class="frame">
    <div class="kicker">The shift</div>
    <h2>We are no longer just<br/>building stability.</h2>
    <div class="sub-text">We are building a scalable growth organization.</div>
  </div>
  <div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>02</span></div>
</section>

<!-- ================= 03 HOW WE DO THIS ================= -->
<section data-label="03 How We Do This" class="diff">
  {WAVEFORM_SOFT}
  <div class="frame">
    <p class="eyebrow">How we do this</p>
    <h2 class="title">Three pillars driving<br/>the growth agenda.</h2>
    <div class="three">
      <div class="card">
        <h4>Verticalization</h4>
        <p>Going deeper in specific verticals to build a repeatable sales motion. Focused industry expertise translates to faster qualification, stronger proposals, and higher close rates.</p>
      </div>
      <div class="card">
        <h4>Book-of-Business</h4>
        <p>Systematic expansion within the existing account base. Customers who already trust Aseva are the fastest path to growth, and every account manager owns a defined growth plan.</p>
      </div>
      <div class="card">
        <h4>Marketing</h4>
        <p>Building the pipeline that feeds the machine. Marketing moves from reactive to proactive, generating qualified leads that the sales team can work rather than waiting for referrals.</p>
      </div>
    </div>
  </div>
  <div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>03</span></div>
</section>

<!-- ================= 04 IN THE FIELD ================= -->
<section data-label="04 In the Field" class="field">
  <div class="frame">
    <p class="eyebrow">Michael &amp; Chris &nbsp;&middot;&nbsp; Field focus</p>
    <h2 class="title">Two roadshow initiatives running in parallel.</h2>
    <div class="two">
      <div class="col">
        <h4>Midwest Roadshows</h4>
        <p>Michael and Chris taking Aseva's full story on the road in the Midwest. Direct in-person engagement in a market where we are building presence and name recognition. Face-to-face beats email every time at this stage of a relationship.</p>
      </div>
      <div class="col">
        <h4>Win-back Roadshows</h4>
        <p>Targeted outreach to former customers who left for reasons that no longer apply. Aseva is a materially different company from what they experienced. These are warm conversations, not cold calls, and the close rate reflects it.</p>
      </div>
    </div>
  </div>
  <div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>04</span></div>
</section>

<!-- ================= 05 HOW THE OFFICE HELPS ================= -->
<section data-label="05 How the Office Helps" class="why">
  {CORNER_LOGO}
  <div class="frame">
    <p class="eyebrow">Q2 Extended Huddle</p>
    <h2 class="title">How the Office Helps.</h2>
    <div class="pillars">
      <div class="pillar">
        <div class="num">01</div>
        <div>
          <h4>Waytek: office management</h4>
          <p>Waytek takes over office management duties, freeing up the attention and bandwidth that currently pulls Michael and Chris back into administrative work. This is the structural change that makes everything else possible.</p>
        </div>
      </div>
      <div class="pillar">
        <div class="num">02</div>
        <div>
          <h4>Bolstering account management</h4>
          <p>A stronger account management layer handles customer relationships, renewal conversations, and service coordination. The field can stay focused on new business instead of splitting time between prospects and existing accounts.</p>
        </div>
      </div>
      <div class="pillar">
        <div class="num">03</div>
        <div>
          <h4>Optimize processes with AI</h4>
          <p>The internal workflows that currently require manual coordination, handoffs, and follow-up are candidates for AI-assisted automation. Less friction on process means more energy on growth.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule"></span><span>05</span></div>
</section>

<!-- ================= 06 CLIENT SERVICES ECOSYSTEM ================= -->
<section data-label="06 Client Services Ecosystem" class="ecosystem">
  {CORNER_LOGO}
  <div class="frame">
    <p class="eyebrow">Client Services Ecosystem &nbsp;&middot;&nbsp; Waytek inserted as a director</p>
    <h2 class="title">How the office connects.</h2>
    <div style="margin-top:8px;flex:1;display:flex;align-items:center;">
      {ECOSYSTEM_SVG}
    </div>
  </div>
  <div class="page-meta"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule"></span><span>06</span></div>
</section>

<!-- ================= 07 NEW STRUCTURE ================= -->
<section data-label="07 New Structure" class="newstruct">
  {CORNER_LOGO}
  <div class="frame">
    <p class="eyebrow">Office leadership</p>
    <div class="split">
      <div class="left">
        <div class="rule-cyan"></div>
        <h2>Waytek steps in as a <em>director</em>. Michael can focus on the field.</h2>
        <p>Michael cannot run an outbound sales organization and manage the internal operating details at the same time. The two jobs are incompatible at the pace we need to move.</p>
        <p>Waytek's role as director gives the office a clear owner for the operational layer. Michael's attention goes where it creates the most value: in front of customers and prospects.</p>
      </div>
      <div class="right reasons">
        <div class="reason">
          <div class="idx">01</div>
          <div>
            <h5>Single owner for the operational layer</h5>
            <p>Every internal process, handoff, and follow-up has one person accountable. No more gaps between what the field commits and what the office delivers.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">02</div>
          <div>
            <h5>Account management gets real bandwidth</h5>
            <p>With office management off the plate, account managers can deepen customer relationships instead of triaging administrative requests.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">03</div>
          <div>
            <h5>AI integration starts with process clarity</h5>
            <p>You cannot automate a process no one owns. Waytek's role creates the organizational clarity needed to identify which workflows are ready for AI and which need redesign first.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule"></span><span>07</span></div>
</section>

<!-- ================= 08 CLOSING ================= -->
<section data-label="08 Close" class="cover">
  {WAVEFORM_FULL}
  <div class="frame">
    <div>
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--secondary);margin-bottom:48px;">Q2 Extended Huddle &nbsp;&middot;&nbsp; May 2026</div>
      <h1 style="font-family:var(--font-heading);font-weight:400;font-size:88px;line-height:1.05;letter-spacing:-0.01em;color:#ffffff;margin:0;max-width:1450px;">We are no longer just building stability. We are building a <span style="color:var(--secondary);font-weight:600;">scalable growth organization</span>.</h1>
    </div>
  </div>
</section>

<!-- ================= 09 DISCUSSION ================= -->
<section data-label="09 Discussion" class="discuss">
  {CORNER_LOGO}
  <div class="frame">
    <p class="eyebrow">Discussion</p>
    <p class="big-q">Any questions on <em>why this needs to happen</em>?</p>
  </div>
  <div class="page-meta"><span>Aseva &nbsp;&middot;&nbsp; Q2 Extended Huddle</span><span class="rule"></span><span>09</span></div>
</section>

</deck-stage>

</body>
</html>"""

out = REPO / "q2-huddle-2026-deck.html"
out.write_text(HTML)
print(f"Written: {out} ({out.stat().st_size:,} bytes)")
