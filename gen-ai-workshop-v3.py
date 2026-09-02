#!/usr/bin/env python3
"""Assemble the AI Workshop deck, v3.

Source brief: SecondBrain Output/Drafts/AI Workshop - Presentation and Workshop
Outline v3 - 2026-09-01.md (which came out of the 9/1 Chris/Michael/Jessie meeting).

Not a prospect sales deck. It is the backdrop for the Sept 22 90 minute workshop:
20 minute presentation, 45 to 50 minute workshop, 5 minute close.

Visual approach, per Chris: take real liberty. Aseva color tokens and fonts are
kept because they still look good, but the layouts are purpose built for this
talk rather than the six sales archetypes. The two devices Chris called out are
the engine of the deck:
  1. A persistent level ladder on the right edge, so the room always sees the climb.
  2. The coral strike through a word, used on the four moments that need a reversal.
Michael's "but" is the third device: every level slide ends with the problem the
next level solves, in a coral band at the bottom of the frame.
"""
import base64
import pathlib

root = pathlib.Path(__file__).parent
tpl = (root / "template/template.html").read_text()

style = tpl[tpl.index("<style>"): tpl.index("</style>") + len("</style>")]
deckjs = (root / "template/deck-stage.js").read_text()


def b64(rel, mime):
    data = base64.b64encode((root / rel).read_bytes()).decode()
    return f"data:{mime};base64,{data}"


LOGO = b64("template/assets/aseva-horizontal.png", "image/png")

WAVE_BG = '''<svg class="wave-bg" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <g fill="#00a1e2" opacity="0.22">
      <rect x="70" y="560" width="16" height="40" rx="2"/><rect x="110" y="500" width="16" height="160" rx="2"/><rect x="150" y="420" width="16" height="320" rx="2"/><rect x="190" y="340" width="16" height="480" rx="2"/><rect x="230" y="280" width="16" height="600" rx="2"/><rect x="270" y="230" width="16" height="700" rx="2"/><rect x="310" y="200" width="16" height="760" rx="2"/><rect x="350" y="180" width="16" height="800" rx="2"/><rect x="390" y="170" width="16" height="820" rx="2"/><rect x="430" y="180" width="16" height="800" rx="2"/><rect x="470" y="210" width="16" height="740" rx="2"/><rect x="510" y="260" width="16" height="640" rx="2"/><rect x="550" y="320" width="16" height="520" rx="2"/><rect x="590" y="380" width="16" height="400" rx="2"/><rect x="630" y="430" width="16" height="300" rx="2"/><rect x="670" y="470" width="16" height="220" rx="2"/><rect x="710" y="500" width="16" height="160" rx="2"/><rect x="750" y="520" width="16" height="120" rx="2"/><rect x="790" y="540" width="16" height="80" rx="2"/><rect x="830" y="550" width="16" height="60" rx="2"/>
    </g>
  </svg>'''

WAVE_SOFT = '''<svg class="wave-soft" viewBox="0 0 1000 1000" aria-hidden="true">
    <g fill="#00a1e2">
      <rect x="70" y="560" width="16" height="40"/><rect x="110" y="500" width="16" height="160"/><rect x="150" y="420" width="16" height="320"/><rect x="190" y="340" width="16" height="480"/><rect x="230" y="280" width="16" height="600"/><rect x="270" y="230" width="16" height="700"/><rect x="310" y="200" width="16" height="760"/><rect x="350" y="180" width="16" height="800"/><rect x="390" y="170" width="16" height="820"/><rect x="430" y="180" width="16" height="800"/><rect x="470" y="210" width="16" height="740"/><rect x="510" y="260" width="16" height="640"/><rect x="550" y="320" width="16" height="520"/><rect x="590" y="380" width="16" height="400"/><rect x="630" y="430" width="16" height="300"/><rect x="670" y="470" width="16" height="220"/><rect x="710" y="500" width="16" height="160"/><rect x="750" y="520" width="16" height="120"/>
    </g>
  </svg>'''

CORNER = '<div class="corner-logo" role="img" aria-label="Aseva"></div>'
DARK_MARK = '<div class="w-mark" role="img" aria-label="Aseva"></div>'

EXTRA_CSS = """<style>
:root { --aseva-logo: url(ASEVA_LOGO_URI); }
/* ================= AI Workshop v3 layouts =================
   Aseva tokens and fonts only. Nothing renders below 24px.
   Custom layouts, because this is a talk and not a sales deck. */

section.w-dark  { background: var(--primary); color: var(--white); position: relative; overflow: hidden; }
section.w-light { background: var(--white);   color: var(--primary); position: relative; overflow: hidden; }
section.w-tint  { background: var(--blue-extra-light); color: var(--primary); position: relative; overflow: hidden; }

.w-dark .frame, .w-light .frame, .w-tint .frame {
  position: relative; z-index: 3; height: 100%;
  display: flex; flex-direction: column; justify-content: center;
  padding: 96px 120px 140px 120px;
}
.w-light .frame, .w-tint .frame { padding-top: 152px; }
.w-dark .frame.hasmark { padding-top: 152px; }
/* Level slides: headline block up top, the "but" pinned to the bottom rule. */
.frame.stack { justify-content: flex-start; padding-top: 150px; }
.frame.stack .grow { flex: 1 1 auto; }

.w-dark .wave-soft { position: absolute; right: -300px; bottom: -300px; width: 1040px; opacity: 0.055; z-index: 1; }
.w-dark.bigwave .wave-soft { right: -220px; bottom: -240px; width: 1320px; opacity: 0.15; }
.w-tint .wave-soft { position: absolute; right: -340px; top: -420px; width: 900px; opacity: 0.055; z-index: 1; }
.w-light .wave-soft { position: absolute; left: -300px; bottom: -320px; width: 860px; opacity: 0.05; z-index: 1; }

.w-mark { position: absolute; top: 48px; left: 120px; height: 36px; width: 156px;
  background: var(--aseva-logo) no-repeat left center / contain;
  filter: brightness(0) invert(1); opacity: 0.85; z-index: 5; }
div.corner-logo { position: absolute; top: 48px; left: 120px; height: 36px; width: 156px;
  background: var(--aseva-logo) no-repeat left center / contain; z-index: 5; }

/* ---- type ---- */
.w-eyebrow {
  font-family: var(--font-body); font-weight: 600; font-size: 24px;
  letter-spacing: 0.22em; text-transform: uppercase; color: var(--secondary);
  margin: 0 0 34px 0;
}
.w-eyebrow.muted { color: rgba(255,255,255,0.5); }
.w-eyebrow.dim   { color: var(--grey-medium); }

.w-h1 { font-family: var(--font-heading); font-weight: 600; letter-spacing: -0.015em; margin: 0; }
.w-h1.xxl { font-size: 148px; line-height: 0.94; }
.w-h1.xl  { font-size: 112px; line-height: 1.0; }
.w-h1.lg  { font-size: 88px;  line-height: 1.04; }
.w-h1.md  { font-size: 68px;  line-height: 1.1; }
.w-h1.sm  { font-size: 54px;  line-height: 1.14; }
.w-h1 .cy   { color: var(--secondary); }
.w-h1 .thin { font-weight: 300; }
.w-dark .w-h1 { color: var(--white); }

.w-sub {
  font-family: var(--font-heading); font-weight: 300; font-size: 40px; line-height: 1.3;
  margin: 36px 0 0 0; max-width: 1080px;
}
.w-dark .w-sub { color: rgba(255,255,255,0.78); }
.w-light .w-sub, .w-tint .w-sub { color: var(--grey); }
.w-sub .cy { color: var(--secondary); font-weight: 400; }

.w-bar { width: 128px; height: 8px; background: var(--secondary); margin-bottom: 44px; }

/* ---- the strike: a coral line through the word being reversed ---- */
.strike { position: relative; white-space: nowrap; }
.strike:after {
  content: ""; position: absolute; left: -10px; right: -10px; top: 51%; height: 8px;
  background: var(--coral); transform: rotate(-1.6deg); border-radius: 2px;
}
.strike.thin:after { height: 6px; }

/* ---- the ghost numeral behind each level slide ---- */
.ghost {
  position: absolute; right: 450px; top: 50%; transform: translateY(-53%);
  font-family: var(--font-heading); font-weight: 700; font-size: 780px; line-height: 0.8;
  color: transparent; -webkit-text-stroke: 2px rgba(255,255,255,0.10);
  z-index: 1; pointer-events: none; user-select: none;
}

/* ---- the persistent level ladder on the right edge ---- */
.rail { position: absolute; right: 96px; top: 50%; transform: translateY(-50%); width: 360px; z-index: 4; }
.rail .step {
  display: grid; grid-template-columns: 52px 1fr; align-items: center; gap: 20px;
  padding: 20px 0; border-top: 1px solid rgba(255,255,255,0.14);
}
.rail .step:last-child { border-bottom: 1px solid rgba(255,255,255,0.14); }
.rail .step .no {
  font-family: var(--font-heading); font-weight: 300; font-size: 34px; line-height: 1;
  text-align: right; color: rgba(255,255,255,0.26);
}
.rail .step .nm {
  font-family: var(--font-body); font-weight: 600; font-size: 24px; letter-spacing: 0.05em;
  color: rgba(255,255,255,0.26);
}
.rail .step.done .no, .rail .step.done .nm { color: rgba(255,255,255,0.5); }
.rail .step.on {
  margin: 0 -30px; padding: 26px 30px; background: rgba(0,161,226,0.16);
  border-top: 1px solid rgba(0,161,226,0.45); border-bottom: 1px solid rgba(0,161,226,0.45);
  grid-template-columns: 82px 1fr;
}
.rail .step.on .no { color: var(--secondary); font-size: 62px; font-weight: 400; }
.rail .step.on .nm { color: var(--white); font-size: 28px; }

/* ---- Michael's "but": the problem the next level solves ---- */
.but {
  border-top: 1px solid rgba(255,255,255,0.18); padding-top: 34px; margin-top: 30px;
  display: grid; grid-template-columns: 190px 1fr; gap: 44px; align-items: start;
  max-width: 1180px;
}
.but .tag {
  font-family: var(--font-heading); font-weight: 700; font-size: 76px; line-height: 0.86;
  color: var(--coral); letter-spacing: -0.02em;
}
.but .lines { display: flex; flex-direction: column; gap: 16px; }
.but p {
  font-family: var(--font-heading); font-weight: 300; font-size: 36px; line-height: 1.28;
  margin: 0; color: rgba(255,255,255,0.88);
}
.but p .hot { color: var(--coral); font-weight: 400; }

/* ---- ladder preview: all five levels as one climb ---- */
.climb { display: flex; flex-direction: column; gap: 0; margin-top: 20px; }
.climb .rung {
  display: grid; grid-template-columns: 100px 420px 1fr; align-items: center; gap: 40px;
  padding: 21px 0; border-top: 1px solid rgba(255,255,255,0.16);
}
.climb .rung:last-child { border-bottom: 1px solid rgba(255,255,255,0.16); }
.climb .rung .no { font-family: var(--font-heading); font-weight: 300; font-size: 60px; line-height: 1; color: var(--secondary); }
.climb .rung h4 { font-family: var(--font-heading); font-weight: 600; font-size: 42px; line-height: 1; margin: 0; color: var(--white); }
.climb .rung p  { font-family: var(--font-body); font-weight: 400; font-size: 28px; line-height: 1.35; margin: 0; color: rgba(255,255,255,0.7); }
.climb .rung .bump { padding-left: 0; }

/* ---- the chain: five levels, five buts, one they cannot solve ---- */
.chain { display: flex; flex-direction: column; gap: 0; margin-top: 8px; }
.chain .link {
  display: grid; grid-template-columns: 76px 420px 1fr; align-items: center; gap: 36px;
  padding: 26px 0; border-top: 1px solid rgba(255,255,255,0.16);
}
.chain .link .no { font-family: var(--font-heading); font-weight: 300; font-size: 46px; color: rgba(255,255,255,0.4); }
.chain .link h4  { font-family: var(--font-heading); font-weight: 600; font-size: 38px; margin: 0; color: var(--white); }
.chain .link p   { font-family: var(--font-heading); font-weight: 300; font-size: 34px; line-height: 1.25; margin: 0; color: rgba(255,255,255,0.66); }
.chain .link.last {
  border-top: 1px solid var(--coral); border-bottom: 1px solid var(--coral);
  background: rgba(239,107,81,0.12); margin: 0 -32px; padding: 32px;
}
.chain .link.last .no { color: var(--coral); font-size: 46px; }
.chain .link.last p   { color: var(--white); font-weight: 400; }

/* ---- versus: two things set against each other ---- */
.versus { display: grid; grid-template-columns: 1fr 150px 1fr; align-items: stretch; gap: 20px; margin-top: 44px; }
.versus .side h4 { font-family: var(--font-heading); font-weight: 300; font-size: 118px; line-height: 1; margin: 0 0 20px 0; color: var(--secondary); }
.versus .side.cold h4 { color: rgba(255,255,255,0.34); }
.versus .side h5 { font-family: var(--font-heading); font-weight: 600; font-size: 40px; margin: 0 0 14px 0; color: var(--white); }
.versus .side p  { font-family: var(--font-body); font-weight: 400; font-size: 28px; line-height: 1.4; margin: 0; color: rgba(255,255,255,0.72); }
.versus .mid { display: flex; align-items: center; justify-content: center;
  font-family: var(--font-heading); font-weight: 300; font-size: 38px; color: rgba(255,255,255,0.38);
  border-left: 1px solid rgba(255,255,255,0.16); border-right: 1px solid rgba(255,255,255,0.16); }

/* ---- timeline strip ---- */
.strip { display: grid; grid-template-columns: 24fr 46fr 15fr; gap: 16px; margin-top: 56px; }
.strip .seg { position: relative; padding-top: 34px; border-top: 8px solid rgba(255,255,255,0.2); }
.strip .seg.hot { border-top-color: var(--secondary); }
.strip .seg .t { font-family: var(--font-heading); font-weight: 300; font-size: 66px; line-height: 1; color: var(--white); }
.strip .seg.hot .t { color: var(--secondary); }
.strip .seg h5 { font-family: var(--font-heading); font-weight: 600; font-size: 36px; margin: 16px 0 10px 0; color: var(--white); }
.strip .seg p  { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.4; margin: 0; color: rgba(255,255,255,0.66); }

/* ---- panels, tiles, rows ---- */
.w-two { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
.w-panel { border: 1px solid rgba(255,255,255,0.26); padding: 42px 44px 46px 44px; }
.w-panel .cap { font-family: var(--font-body); font-weight: 600; font-size: 24px; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--secondary); margin-bottom: 22px; }
.w-panel h4 { font-family: var(--font-heading); font-weight: 600; font-size: 44px; line-height: 1.08; margin: 0 0 20px 0; color: var(--white); }
.w-panel p  { font-family: var(--font-body); font-weight: 400; font-size: 28px; line-height: 1.45; margin: 0; color: rgba(255,255,255,0.82); }
.w-panel.warm { border-color: rgba(239,107,81,0.6); }
.w-panel.warm .cap { color: var(--coral); }

.w-band {
  margin-top: 40px; border-left: 8px solid var(--secondary); padding: 30px 40px;
  background: rgba(0,161,226,0.12);
  font-family: var(--font-heading); font-weight: 300; font-size: 36px; line-height: 1.32; color: var(--white);
}
.w-band strong { font-weight: 600; color: var(--secondary); }
.w-light .w-band, .w-tint .w-band { background: rgba(0,161,226,0.08); color: var(--primary); }

.w-tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 34px; margin-top: 20px; }
.w-tile { border: 1px solid #d1d6dc; background: var(--white); padding: 38px 34px 42px 34px; }
.w-dark .w-tile { background: transparent; border-color: rgba(255,255,255,0.26); }
.w-tile .cap { font-family: var(--font-body); font-weight: 600; font-size: 24px; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--secondary); margin-bottom: 20px; }
.w-tile h4 { font-family: var(--font-heading); font-weight: 600; font-size: 38px; line-height: 1.1; margin: 0 0 16px 0; color: var(--primary); }
.w-dark .w-tile h4 { color: var(--white); }
.w-tile p { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.45; margin: 0; color: var(--grey); }
.w-dark .w-tile p { color: rgba(255,255,255,0.78); }

.w-rows { display: flex; flex-direction: column; gap: 22px; margin-top: 8px; }
.w-row { display: grid; grid-template-columns: 110px 1fr; align-items: start; gap: 36px;
  padding-bottom: 22px; border-bottom: 1px solid #d1d6dc; }
.w-dark .w-row { border-bottom-color: rgba(255,255,255,0.18); }
.w-row:last-child { border-bottom: none; padding-bottom: 0; }
.w-row .n { font-family: var(--font-heading); font-weight: 300; font-size: 60px; line-height: 0.9; color: var(--secondary); }
.w-row h4 { font-family: var(--font-heading); font-weight: 600; font-size: 38px; line-height: 1.14; margin: 0 0 10px 0; }
.w-light .w-row h4, .w-tint .w-row h4 { color: var(--primary); }
.w-dark  .w-row h4 { color: var(--white); }
.w-row p { font-family: var(--font-body); font-weight: 400; font-size: 27px; line-height: 1.4; margin: 0; }
.w-light .w-row p, .w-tint .w-row p { color: var(--grey); }
.w-dark  .w-row p { color: rgba(255,255,255,0.78); }

/* ---- score dials ---- */
.dials { display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; margin-top: 52px; }
.dial-wrap { display: flex; flex-direction: column; align-items: center; text-align: center; }
.dial { width: 250px; height: 250px; border-radius: 50%; display: grid; place-items: center; }
.dial .hole { width: 190px; height: 190px; border-radius: 50%; background: var(--blue-extra-light);
  display: grid; place-items: center;
  font-family: var(--font-heading); font-weight: 300; font-size: 78px; color: var(--secondary); }
.dial-wrap h5 { font-family: var(--font-heading); font-weight: 600; font-size: 38px; line-height: 1.14; margin: 32px 0 12px 0; color: var(--primary); }
.dial-wrap p  { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.4; margin: 0; color: var(--grey); max-width: 400px; }

/* ---- buckets ---- */
.w-buckets { display: grid; grid-template-columns: repeat(3, 1fr); gap: 34px; margin-top: 48px; }
.w-bucket { border-top: 10px solid var(--secondary); padding-top: 28px; }
.w-bucket.mid  { border-top-color: var(--blue-light); }
.w-bucket.cold { border-top-color: var(--grey-light); }
.w-bucket .rng  { font-family: var(--font-heading); font-weight: 300; font-size: 72px; line-height: 1; color: var(--primary); }
.w-bucket .verb { font-family: var(--font-heading); font-weight: 600; font-size: 44px; margin-top: 14px; color: var(--secondary); }
.w-bucket.mid .verb  { color: var(--supplemental); }
.w-bucket.cold .verb { color: var(--grey-medium); }
.w-bucket p { font-family: var(--font-body); font-weight: 400; font-size: 27px; line-height: 1.4; margin: 14px 0 0 0; color: var(--grey); }

/* ---- QR moment ---- */
.qr { display: grid; grid-template-columns: 460px 1fr; gap: 90px; align-items: center; margin-top: 20px; }
.qr .box { width: 460px; height: 460px; border: 10px solid var(--secondary); display: grid; place-items: center;
  background: rgba(0,161,226,0.10); text-align: center; padding: 30px; }
.qr .box span { font-family: var(--font-body); font-weight: 600; font-size: 28px; letter-spacing: 0.14em;
  text-transform: uppercase; color: var(--secondary); line-height: 1.5; }

/* ---- split: statement left, list right ---- */
.w-split { display: grid; grid-template-columns: 1fr 1fr; gap: 90px; align-items: start; margin-top: 48px; }
.w-list { display: flex; flex-direction: column; gap: 26px; }
.w-item { display: grid; grid-template-columns: 8px 1fr; gap: 26px; }
.w-item .pip { background: var(--secondary); }
.w-item h5 { font-family: var(--font-heading); font-weight: 600; font-size: 32px; line-height: 1.18; margin: 0 0 8px 0; color: var(--primary); }
.w-item p  { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.4; margin: 0; color: var(--grey); }
.w-dark .w-item h5 { color: var(--white); }
.w-dark .w-item p  { color: rgba(255,255,255,0.78); }
.w-split .lead { font-family: var(--font-heading); font-weight: 300; font-size: 36px; line-height: 1.34; color: var(--grey); margin: 0; }
.w-dark .w-split .lead { color: rgba(255,255,255,0.8); }

/* ---- big stat ---- */
.w-stat { display: grid; grid-template-columns: 0.85fr 1.15fr; gap: 80px; align-items: center; margin-top: 24px; }
.w-stat .num { font-family: var(--font-heading); font-weight: 300; font-size: 210px; line-height: 0.9; color: var(--secondary); letter-spacing: -0.02em; }
.w-stat .src { font-family: var(--font-body); font-weight: 400; font-size: 24px; letter-spacing: 0.04em; color: rgba(255,255,255,0.55); margin-top: 24px; }
.w-stat .say { font-family: var(--font-heading); font-weight: 300; font-size: 42px; line-height: 1.28; color: rgba(255,255,255,0.88); }
</style>"""

EXTRA_CSS = EXTRA_CSS.replace("ASEVA_LOGO_URI", LOGO)

LEVELS = [
    ("Ask better",     "A better search engine, and nothing more."),
    ("Give it memory", "It knows your business before you ask."),
    ("Custom apps",    "Everyone else gets to use it too."),
    ("Agents",         "You give it a goal and stop asking."),
    ("Full context",   "It knows everything you know."),
]


def rail(active):
    out = ['<div class="rail">']
    for i, (name, _) in enumerate(LEVELS, start=1):
        cls = "step on" if i == active else ("step done" if i < active else "step")
        out.append(f'<div class="{cls}"><div class="no">{i}</div><div class="nm">{name}</div></div>')
    out.append('</div>')
    return "".join(out)


def ghost(n):
    return f'<div class="ghost" aria-hidden="true">{n}</div>'


def meta_dark(section, num):
    return (f'<div class="page-meta" style="color:rgba(255,255,255,0.5);z-index:5;">'
            f'<span>{section}</span><span class="rule" style="background:rgba(255,255,255,0.22);"></span>'
            f'<span>{num}</span></div>')


def meta_light(section, num):
    return f'<div class="page-meta" style="z-index:5;"><span>{section}</span><span class="rule"></span><span>{num}</span></div>'


BODY = f'''
<deck-stage width="1920" height="1080">

<!-- 01 COVER -->
<section data-label="01 Cover" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <img src="{LOGO}" alt="Aseva" style="height:104px;width:auto;margin-bottom:56px;display:block;filter:brightness(0) invert(1);" />
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.32em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-bottom:38px;">Business Optimization with AI</div>
      <p class="kicker" style="font-size:96px;line-height:1.02;max-width:1460px;">You're already using AI.<br/>You're using a <em>fraction</em> of it.</p>
      <div style="font-family:var(--font-heading);font-weight:300;font-size:40px;color:rgba(255,255,255,0.72);margin-top:42px;">Five levels. Then you build one.</div>
    </div>
  </div>
  <div class="footer-line">September 22 · WorkZones, Santa Barbara · aseva.com</div>
</section>

<!-- 02 HOW TODAY WORKS -->
<section data-label="02 How today works" class="w-dark hasframe">
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow muted">How the next 90 minutes go</p>
    <h2 class="w-h1 md">Twenty minutes of me.<br/>Then <span class="cy">you work</span>.</h2>
    <div class="strip">
      <div class="seg"><div class="t">20</div><h5>The five levels</h5><p>Where AI actually is, shown live. Every level ends with the problem it leaves you.</p></div>
      <div class="seg hot"><div class="t">50</div><h5>Your turn</h5><p>Phones out. You find the one task in your week to hand to AI first, then sketch how it works.</p></div>
      <div class="seg"><div class="t">5</div><h5>Close</h5><p>One thing to do this month.</p></div>
    </div>
    <div class="w-band" style="max-width:1500px;">Everything about AI comes down to <strong>context and content</strong>. Today is recorded, so you get all of it afterward.</div>
  </div>
  {meta_dark("Aseva · Business Optimization with AI", "02")}
</section>

<!-- 03 HANDS TEST -->
<section data-label="03 Hands test" class="w-dark">
  {DARK_MARK}
  <div class="frame hasmark">
    <div class="w-bar"></div>
    <h2 class="w-h1 xxl" style="max-width:1560px;">Who used AI<br/>this week?</h2>
    <div class="w-band" style="margin-top:60px;max-width:1440px;">Keep your hand up if it was for more than <strong>search or summarizing an email</strong>.</div>
  </div>
  {meta_dark("Aseva · Show of hands", "03")}
</section>

<!-- 04 THE ONE IDEA -->
<section data-label="04 The one idea" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow muted">Hold onto this one</p>
    <h2 class="w-h1 lg">AI doesn't <span class="strike">replace</span> your people.<br/>It makes them <span class="cy">more powerful</span>.</h2>
    <p class="w-sub" style="max-width:1300px;">Everything you'll see today was built or run by regular people at our company. None of them write code for a living.</p>
  </div>
  {meta_dark("Aseva", "04")}
</section>

<!-- 05 THE CLIMB -->
<section data-label="05 The climb" class="w-dark">
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow">The climb</p>
    <h2 class="w-h1 sm" style="margin-bottom:26px;">Five levels. Each one fixes<br/>what the last one <span class="cy">couldn't</span>.</h2>
    <div class="climb">
      <div class="rung"><div class="no">1</div><div><h4>Ask better</h4></div><div class="bump"><p>A smarter search box. It forgets you the second you close it.</p></div></div>
      <div class="rung"><div class="no">2</div><div><h4>Give it memory</h4></div><div class="bump"><p>Now it knows your business. But only on your computer.</p></div></div>
      <div class="rung"><div class="no">3</div><div><h4>Custom apps</h4></div><div class="bump"><p>Now your whole team uses it. Somebody has to build and host it.</p></div></div>
      <div class="rung"><div class="no">4</div><div><h4>Agents</h4></div><div class="bump"><p>Now it works without being asked. Hard to build, and it costs on every run.</p></div></div>
      <div class="rung"><div class="no">5</div><div><h4>Full context</h4></div><div class="bump"><p>Now it knows everything you know. This one is a system, not a purchase.</p></div></div>
    </div>
  </div>
  {meta_dark("Aseva · The climb", "05")}
</section>

<!-- 06 LEVEL 1 -->
<section data-label="06 Level 1 Ask better" class="w-dark">
  {DARK_MARK}
  {ghost(1)}
  {rail(1)}
  <div class="frame stack">
    <div class="grow">
      <p class="w-eyebrow">Level 1 of 5</p>
      <h2 class="w-h1 xl" style="max-width:1000px;">Ask better.</h2>
      <p class="w-sub" style="max-width:1000px;">Don't ask it for the answer. Make it <span class="cy">interview you</span> first.</p>
      <div class="w-band" style="max-width:1000px;">"Ask me one question at a time until you know enough to write this."</div>
    </div>
    <div class="but">
      <div class="tag">But</div>
      <div class="lines">
        <p>It forgets everything the moment you close the window.</p>
        <p><span class="hot">You are the memory.</span> Every single time.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 1 · Live", "06")}
</section>

<!-- 07 LEVEL 2 -->
<section data-label="07 Level 2 Give it memory" class="w-dark">
  {DARK_MARK}
  {ghost(2)}
  {rail(2)}
  <div class="frame stack">
    <div class="grow">
      <p class="w-eyebrow">Level 2 of 5</p>
      <h2 class="w-h1 xl" style="max-width:1000px;">Give it<br/>memory.</h2>
      <p class="w-sub" style="max-width:1000px;">Level 1 is a smart stranger.<br/>Level 2 <span class="cy">already knows your business</span>.</p>
    </div>
    <div class="but">
      <div class="tag">But</div>
      <div class="lines">
        <p>It lives on your computer. It is your world and it never leaves you. Nobody else on your team gets any of it.</p>
        <p><span class="hot">And everything you put in there is going somewhere.</span></p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 2 · Live", "07")}
</section>

<!-- 08 DATA SAFETY -->
<section data-label="08 Data safety" class="w-dark">
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow muted">Stop here for a minute</p>
    <h2 class="w-h1 md" style="margin-bottom:44px;">Is my data safe? <span class="cy">Three rules.</span></h2>
    <div class="w-two">
      <div class="w-panel">
        <div class="cap">Rule one · fine to send</div>
        <h4>Anything you'd hand a new contractor on day one</h4>
        <p>Draft copy, public information, general questions, the files you already pass around the office.</p>
      </div>
      <div class="w-panel warm">
        <div class="cap">Rule two · never send</div>
        <h4>Anything you are legally on the hook to protect</h4>
        <p>Passwords, customer records, anything covered by a contract or a regulator. When in doubt, leave it out.</p>
      </div>
    </div>
    <div class="w-band"><strong>Rule three.</strong> A paid business account means your data is not used to train the model, and you get admin controls. That one switch covers most of the worry.</div>
  </div>
  {meta_dark("Aseva · Data safety", "08")}
</section>

<!-- 09 LEVEL 3 -->
<section data-label="09 Level 3 Custom apps" class="w-dark">
  {DARK_MARK}
  {ghost(3)}
  {rail(3)}
  <div class="frame stack">
    <div class="grow">
      <p class="w-eyebrow">Level 3 of 5</p>
      <h2 class="w-h1 xl" style="max-width:1000px;">Custom<br/>apps.</h2>
      <p class="w-sub" style="max-width:1000px;">Instead of you asking well, the app asks <span class="cy">the same thing the same way</span>, every time, for everyone.</p>
    </div>
    <div class="but">
      <div class="tag">But</div>
      <div class="lines">
        <p>Somebody has to build it, and it is harder than it looks.</p>
        <p><span class="hot">And where does it live?</span> Jill in accounting cannot host it, secure it, or decide who gets in.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 3 · Live", "09")}
</section>

<!-- 10 IT SCALES PAST YOU -->
<section data-label="10 It scales past you" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow">Why Level 3 is the real jump</p>
    <h2 class="w-h1 md">It <span class="cy">scales past you</span>.</h2>
    <div class="versus">
      <div class="side cold">
        <h4>1</h4>
        <h5>My own setup</h5>
        <p>Tuned exactly to how I work. Nobody else at the company has ever opened it.</p>
      </div>
      <div class="mid">versus</div>
      <div class="side">
        <h4>6</h4>
        <h5>Bill Buddy</h5>
        <p>One app, built for one job, used by six people who never had to learn a thing about AI.</p>
      </div>
    </div>
    <div class="w-band" style="max-width:1560px;">That is the whole difference between a tool <strong>you</strong> use and a tool <strong>your company</strong> uses.</div>
  </div>
  {meta_dark("Aseva · Level 3", "10")}
</section>

<!-- 11 LEVEL 4 -->
<section data-label="11 Level 4 Agents" class="w-dark">
  {DARK_MARK}
  {ghost(4)}
  {rail(4)}
  <div class="frame stack">
    <div class="grow">
      <p class="w-eyebrow">Level 4 of 5</p>
      <h2 class="w-h1 lg" style="max-width:1000px;">An agent is AI<br/>you <span class="cy">stop asking</span>.</h2>
      <div class="w-rows" style="margin-top:34px;max-width:1000px;gap:16px;">
        <div class="w-row"><div class="n">01</div><div><h4>A goal, and memory</h4><p>A standing job, and it remembers what happened last time.</p></div></div>
        <div class="w-row"><div class="n">02</div><div><h4>Tools it can actually touch</h4><p>Your email, your calendar, your systems. Not just a chat window.</p></div></div>
        <div class="w-row"><div class="n">03</div><div><h4>Rules for acting alone</h4><p>You deputize it. You stay the sheriff.</p></div></div>
      </div>
    </div>
    <div class="but">
      <div class="tag">But</div>
      <div class="lines">
        <p>Hard to train, and easy to build wrong.</p>
        <p><span class="hot">And now you pay on every single run.</span></p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 4", "11")}
</section>

<!-- 12 LEVEL 5 -->
<section data-label="12 Level 5 Full context" class="w-dark">
  {DARK_MARK}
  {ghost(5)}
  {rail(5)}
  <div class="frame stack">
    <div class="grow">
      <p class="w-eyebrow">Level 5 of 5</p>
      <h2 class="w-h1 xl" style="max-width:1000px;">Full<br/>context.</h2>
      <p class="w-sub" style="max-width:1000px;">Every meeting, every email, every idea I've ever had. Watch what it <span class="cy">hands me before I ask</span>.</p>
    </div>
    <div class="but">
      <div class="tag">But</div>
      <div class="lines">
        <p>This one is not a product you buy. It is a system.</p>
        <p><span class="hot">Somebody has to own it.</span></p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 5 · Live", "12")}
</section>

<!-- 13 THE LINE -->
<section data-label="13 The line" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow muted">If you leave with one line</p>
    <h2 class="w-h1 lg">The AI didn't get <span class="strike">smarter</span>.<br/>What changed is <span class="cy">what it knows</span>.</h2>
    <p class="w-sub" style="max-width:1300px;">Same AI in all five demos. The only thing that moved was the context.</p>
  </div>
  {meta_dark("Aseva", "13")}
</section>

<!-- 14 THE CHAIN -->
<section data-label="14 The chain" class="w-dark">
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow">Every level left you a problem</p>
    <h2 class="w-h1 sm" style="margin-bottom:30px;">Four of these you can solve yourself.</h2>
    <div class="chain">
      <div class="link"><div class="no">1</div><h4>Ask better</h4><p>It forgets you every time.</p></div>
      <div class="link"><div class="no">2</div><h4>Give it memory</h4><p>Stuck on one laptop, and your data is going out.</p></div>
      <div class="link"><div class="no">3</div><h4>Custom apps</h4><p>Someone has to build it, host it, and secure it.</p></div>
      <div class="link"><div class="no">4</div><h4>Agents</h4><p>Hard to build right, and it costs on every run.</p></div>
      <div class="link last"><div class="no">5</div><h4>Full context</h4><p>Somebody has to own the whole thing. That is the one nobody does alone.</p></div>
    </div>
  </div>
  {meta_dark("Aseva · The chain", "14")}
</section>

<!-- 15 TWO ASIDES -->
<section data-label="15 Two asides" class="w-light">
  {WAVE_SOFT}
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Two things nobody puts on a slide</p>
    <h2 class="w-h1 md" style="margin-bottom:46px;">While we're being honest.</h2>
    <div class="w-two" style="gap:64px;">
      <div style="border-top:8px solid var(--secondary);padding-top:30px;">
        <h4 style="font-family:var(--font-heading);font-weight:600;font-size:44px;line-height:1.1;margin:0 0 20px 0;color:var(--primary);">People use AI on each other more than they admit</h4>
        <p style="font-family:var(--font-body);font-weight:400;font-size:28px;line-height:1.45;margin:0;color:var(--grey);">Our VP of Engineering and I have both asked our AI what the other one actually meant in a meeting. It works. Nobody talks about it.</p>
      </div>
      <div style="border-top:8px solid var(--coral);padding-top:30px;">
        <h4 style="font-family:var(--font-heading);font-weight:600;font-size:44px;line-height:1.1;margin:0 0 20px 0;color:var(--primary);">Your customers' AI is already choosing who to hire</h4>
        <p style="font-family:var(--font-body);font-weight:400;font-size:28px;line-height:1.45;margin:0;color:var(--grey);">People stopped searching for a carpenter and started asking for one. The businesses that get named are the ones AI can read. Ask it about yours tonight.</p>
      </div>
    </div>
  </div>
  {meta_light("Aseva", "15")}
</section>

<!-- 16 THE HONEST PART -->
<section data-label="16 The honest part" class="w-light">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">The honest part</p>
    <h2 class="w-h1 md" style="margin-bottom:36px;">Most AI that gets bought<br/>never gets <span class="cy">used</span>.</h2>
    <div class="w-rows">
      <div class="w-row"><div class="n">01</div><div><h4>We did it too</h4><p>We bought Copilot for the company and barely touched it for eight months. Nobody was accountable for making it land.</p></div></div>
      <div class="w-row"><div class="n">02</div><div><h4>95 percent of company AI pilots produce nothing measurable</h4><p>Not because the AI failed. Because they bought a tool and hoped. Source: MIT.</p></div></div>
      <div class="w-row"><div class="n">03</div><div><h4>Adoption spreads by one visible win, not a memo</h4><p>How it went here: one engineer, then me, then our VP of Engineering, then the team, then our GM, and finally our owner.</p></div></div>
      <div class="w-row"><div class="n">04</div><div><h4>Which tool you buy matters less than owning what it learns</h4><p>We moved big pieces of this from one tool to another and lost nothing, because the knowledge lives in our files and not inside one company's product.</p></div></div>
    </div>
  </div>
  {meta_light("Aseva · The honest part", "16")}
</section>

<!-- 17 YOUR TURN DIVIDER -->
<section data-label="17 Your turn" class="w-dark bigwave">
  {WAVE_SOFT}
  <div class="frame">
    <p class="w-eyebrow">Part two · 50 minutes</p>
    <h2 class="w-h1 xxl">Your turn.</h2>
    <p class="w-sub" style="font-size:44px;max-width:1400px;">You've seen what the levels are. Now you find the one task in your own week that belongs to a machine.</p>
  </div>
  {meta_dark("Aseva · Workshop", "17")}
</section>

<!-- 18 SCAN -->
<section data-label="18 Scan the code" class="w-tint">
  {WAVE_SOFT}
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Phones out</p>
    <div class="qr">
      <div class="box"><span>QR code<br/>goes here</span></div>
      <div>
        <h2 class="w-h1 md" style="margin-bottom:26px;">Scan it. Then turn<br/>to the person <span class="cy">next to you</span>.</h2>
        <p class="w-sub" style="margin-top:0;font-size:34px;">Name and email first, so we can send you what you build. Then work through it as a pair. Two people arguing about a task get further than one person typing.</p>
      </div>
    </div>
  </div>
  {meta_light("Aseva · Workshop", "18")}
</section>

<!-- 19 ROUND 1 -->
<section data-label="19 Round one" class="w-light">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Round one · 10 minutes</p>
    <h2 class="w-h1 md" style="max-width:1560px;">Name three things you do every week<br/>that you'd love to <span class="cy">never do again</span>.</h2>
    <div class="w-split">
      <div>
        <p class="lead">Not the big strategic stuff. The grind. The report you rebuild every Monday, the email you retype twelve times a week, the quote you assemble by hand.</p>
      </div>
      <div class="w-list">
        <div class="w-item"><div class="pip"></div><div><h5>Write them the way you'd say them</h5><p>No process documents. Plain sentences.</p></div></div>
        <div class="w-item"><div class="pip"></div><div><h5>Steal your partner's</h5><p>If theirs sounds like yours, you both have it.</p></div></div>
      </div>
    </div>
    <div class="w-band" style="max-width:1560px;">You are not looking for what AI <strong>could</strong> do. You are looking for what you would <strong>hand over today</strong>.</div>
  </div>
  {meta_light("Aseva · Round one", "19")}
</section>

<!-- 20 THE SCORE -->
<section data-label="20 The score" class="w-tint">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Three questions the app asks about each one</p>
    <h2 class="w-h1 md">This is how you know <span class="cy">which one to hand over first</span>.</h2>
    <div class="dials">
      <div class="dial-wrap">
        <div class="dial" style="background:conic-gradient(var(--secondary) 0turn 0.34turn, rgba(0,161,226,0.16) 0.34turn 1turn);"><div class="hole">1</div></div>
        <h5>How often?</h5>
        <p>Daily beats monthly. Repetition is what makes it worth automating at all.</p>
      </div>
      <div class="dial-wrap">
        <div class="dial" style="background:conic-gradient(var(--secondary) 0turn 0.67turn, rgba(0,161,226,0.16) 0.67turn 1turn);"><div class="hole">2</div></div>
        <h5>How much time?</h5>
        <p>Twenty minutes a day is eighty hours a year. Add it up before you dismiss it.</p>
      </div>
      <div class="dial-wrap">
        <div class="dial" style="background:conic-gradient(var(--secondary) 0turn 1turn, rgba(0,161,226,0.16) 1turn 1turn);"><div class="hole">3</div></div>
        <h5>How clear are the rules?</h5>
        <p>Could you write them down for a new hire? If yes, you can write them down for AI.</p>
      </div>
    </div>
  </div>
  {meta_light("Aseva · The score", "20")}
</section>

<!-- 21 BUCKETS -->
<section data-label="21 Three buckets" class="w-light">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">What your score means</p>
    <h2 class="w-h1 md" style="max-width:1500px;">Your highest score is the first thing<br/>you should <span class="cy">deputize</span>.</h2>
    <div class="w-buckets">
      <div class="w-bucket"><div class="rng">8 to 10</div><div class="verb">Deputize</div><p>Hand it off. Set the rules once, then check the output instead of doing the work.</p></div>
      <div class="w-bucket mid"><div class="rng">4 to 7</div><div class="verb">Duet</div><p>AI does the first pass. You stay in the loop and finish it.</p></div>
      <div class="w-bucket cold"><div class="rng">0 to 3</div><div class="verb">Defend</div><p>This one stays yours. Protect the time for it, that is where your judgment earns its money.</p></div>
    </div>
    <div class="w-band" style="max-width:1560px;">Don't pick the one that sounds most impressive. Pick the <strong>highest score</strong>.</div>
  </div>
  {meta_light("Aseva · The score", "21")}
</section>

<!-- 22 DEBRIEF -->
<section data-label="22 Debrief" class="w-dark">
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow">Round one debrief · 8 minutes</p>
    <h2 class="w-h1 md" style="margin-bottom:40px;">Read us your top one.<br/>We'll tell you <span class="cy">which level it lives at</span>.</h2>
    <div class="climb" style="margin-top:8px;">
      <div class="rung"><div class="no">2</div><div><h4>Give it memory</h4></div><div><p>It's yours alone and it needs your files. You can do this one on Monday.</p></div></div>
      <div class="rung"><div class="no">3</div><div><h4>Custom apps</h4></div><div><p>Other people need to run it the same way you would. Now it has to be built.</p></div></div>
      <div class="rung"><div class="no">4</div><div><h4>Agents</h4></div><div><p>It should happen without anyone remembering to start it.</p></div></div>
    </div>
    <div class="w-band" style="max-width:1560px;">Three of us in the room, three different answers on how we'd approach yours. That is the useful part.</div>
  </div>
  {meta_dark("Aseva · Debrief", "22")}
</section>

<!-- 23 ROUND 2 -->
<section data-label="23 Round two" class="w-light">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Round two · 10 minutes</p>
    <h2 class="w-h1 md" style="margin-bottom:44px;">Now sketch it. Three questions,<br/>and you've <span class="cy">designed an app</span>.</h2>
    <div class="w-tiles">
      <div class="w-tile"><div class="cap">Question one</div><h4>What goes in?</h4><p>What does it need from you or from your systems before it can start? Be specific about where that lives today.</p></div>
      <div class="w-tile"><div class="cap">Question two</div><h4>What comes out?</h4><p>What does good look like? If you cannot describe the finished thing, neither can the AI.</p></div>
      <div class="w-tile"><div class="cap">Question three</div><h4>Who else would use it?</h4><p>The moment the answer is more than one person, you have left Level 2 behind.</p></div>
    </div>
  </div>
  {meta_light("Aseva · Round two", "23")}
</section>

<!-- 24 POKE HOLES -->
<section data-label="24 Poke holes" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow">Round two debrief · 10 minutes</p>
    <h2 class="w-h1 md" style="margin-bottom:40px;">Now we <span class="cy">poke holes</span> in it.</h2>
    <div class="w-split" style="margin-top:26px;">
      <div class="w-list">
        <div class="w-item"><div class="pip"></div><div><h5>Where does the data come from?</h5><p>And is any of it something you shouldn't be sending out?</p></div></div>
        <div class="w-item"><div class="pip"></div><div><h5>Who checks the output?</h5><p>And what happens the day it is confidently wrong?</p></div></div>
        <div class="w-item"><div class="pip"></div><div><h5>Where does it run?</h5><p>Who pays for it, who can log into it, who turns it off.</p></div></div>
      </div>
      <div>
        <p class="lead">Every hole we poke is one of the buts from the first 20 minutes. That is not us being difficult, it is the actual work.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Poke holes", "24")}
</section>

<!-- 25 THE APP YOU JUST USED -->
<section data-label="25 The app you just used" class="w-tint">
  {WAVE_SOFT}
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">One last thing</p>
    <h2 class="w-h1 md" style="margin-bottom:42px;">The app on your phone right now<br/>is <span class="cy">Level 3 with a Level 4 piece</span> in it.</h2>
    <div class="w-tiles">
      <div class="w-tile"><div class="cap">Level 3</div><h4>Built for this room</h4><p>Same questions, same scoring, same output for all of you. That is what makes it an app and not a chat.</p></div>
      <div class="w-tile"><div class="cap">Level 4</div><h4>It costs on every run</h4><p>There's an agent inside it, so it spends money each time. We built it to pick the cheaper model whenever the cheaper model is good enough.</p></div>
      <div class="w-tile"><div class="cap">The hosting problem</div><h4>Hosted on our platform</h4><p>Which is how a brand new app gets in front of a room by lunch and still stays locked down.</p></div>
    </div>
  </div>
  {meta_light("Aseva · The app", "25")}
</section>

<!-- 26 ONE ASK -->
<section data-label="26 One ask" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame hasmark">
    <p class="w-eyebrow">One ask before you go</p>
    <h2 class="w-h1 lg">Deputize one task <span class="cy">this month</span>.</h2>
    <p class="w-sub" style="font-size:44px;max-width:1400px;">You already scored it. You already know which one it is. Don't start a program, start with that one.</p>
  </div>
  {meta_dark("Aseva", "26")}
</section>

<!-- 27 CLOSE -->
<section data-label="27 Close" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--secondary);margin-bottom:44px;">And we're out of time</div>
      <h1 class="title" style="color:#ffffff;font-size:96px;line-height:1.03;max-width:1520px;">Give me 30 minutes<br/>and we'll <span style="color:var(--secondary);">build yours</span>.</h1>
      <p style="font-family:var(--font-heading);font-weight:300;font-size:42px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1420px;line-height:1.3;">Your score and your sketch are already in the app, so we are not starting from zero. Book it before you leave the room.</p>
    </div>
  </div>
  <div class="footer-line">Sign up sheet at the door · aseva.com · (800) 456-5800</div>
</section>

</deck-stage>
'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Aseva · Business Optimization with AI</title>
<meta name="pluribus-source" content="Output/Drafts/AI Workshop - Presentation and Workshop Outline v3 - 2026-09-01.md" />
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;600;700&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
<script>
{deckjs}
</script>
{style}
{EXTRA_CSS}
</head>
<body>
{BODY}
</body>
</html>
'''

out = root / "prospect-ai-workshop-v3-deck.html"
out.write_text(html)
print(f"wrote {out} ({len(html):,} bytes)")

assert "data:image/png;base64" in html
assert "customElements.define" in html
assert 'src="assets/' not in html
assert 'src="deck-stage.js"' not in html
# Dash scan runs against AUTHORED copy only. The inlined deck-stage.js and the
# template CSS carry em dashes in their own code comments.
for name, blob in (("BODY", BODY), ("EXTRA_CSS", EXTRA_CSS.replace(LOGO, ""))):
    assert "—" not in blob, f"em dash found in {name}"
    assert "–" not in blob, f"en dash found in {name}"
stripped = BODY.replace("var(--", "").replace("<!--", "").replace("-->", "")
assert "--" not in stripped, "double hyphen in slide copy"
print("checks passed:", BODY.count("<section data-label"), "slides")
