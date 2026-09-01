#!/usr/bin/env python3
"""Assemble the AI Workshop deck, simple/direct version.

Source brief: SecondBrain Output/Drafts/AI Workshop - Slide Brief v2 - 2026-08-31.md

NOT a prospect sales deck. It is the slide backdrop for Chris's 90-minute
small-business AI workshop. It uses the Aseva design language (color tokens,
Source Sans 3 + Open Sans, waveform, corner logo, page-meta) but deliberately
omits the sales-deck mandatory slides (Who We Are three-pillar positioning,
sales CTA). The workshop is not a pitch; contact appears once, on the closing
footer.

Layouts are custom rather than the six sales archetypes, per Chris's request.
Every custom class below is built only from DESIGN_SYSTEM tokens and fonts,
and nothing renders below 24px.
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
MARK = b64("template/assets/aseva-brandmark.png", "image/png")

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

CORNER = f'<img src="{LOGO}" alt="Aseva" class="corner-logo" />'

# ---------------------------------------------------------------- custom CSS
EXTRA_CSS = """<style>
/* Workshop deck layouts. Aseva tokens only, nothing below 24px. */

section.w-dark { background: var(--primary); color: var(--white); position: relative; }
section.w-light { background: var(--white); color: var(--primary); position: relative; }
section.w-tint { background: var(--blue-extra-light); color: var(--primary); position: relative; }

.w-dark .frame, .w-light .frame, .w-tint .frame {
  position: relative; z-index: 2; height: 100%;
  display: flex; flex-direction: column; justify-content: center;
  padding: 96px 120px 140px 120px;
}
/* Light slides carry the corner logo, so content starts below it. */
.w-light .frame, .w-tint .frame { padding-top: 152px; }
.w-dark .wave-soft { position: absolute; right: -120px; bottom: -160px; width: 1000px; opacity: 0.10; z-index: 1; }
.w-tint .wave-soft { position: absolute; right: -260px; top: -300px; width: 820px; opacity: 0.07; z-index: 1; }

/* Eyebrow */
.w-eyebrow {
  font-family: var(--font-body); font-weight: 600; font-size: 24px;
  letter-spacing: 0.22em; text-transform: uppercase; color: var(--secondary);
  margin: 0 0 34px 0;
}
.w-dark .w-eyebrow.muted { color: rgba(255,255,255,0.55); }

/* Headlines */
.w-h1 { font-family: var(--font-heading); font-weight: 600; letter-spacing: -0.01em; margin: 0; }
.w-h1.xl  { font-size: 112px; line-height: 1.0; }
.w-h1.lg  { font-size: 88px;  line-height: 1.05; }
.w-h1.md  { font-size: 72px;  line-height: 1.1; }
.w-h1 .cy { color: var(--secondary); }
.w-h1 .lightweight { font-weight: 300; }

.w-sub {
  font-family: var(--font-heading); font-weight: 300; font-size: 40px; line-height: 1.32;
  margin: 40px 0 0 0; max-width: 1240px;
}
.w-dark .w-sub { color: rgba(255,255,255,0.78); }
.w-light .w-sub, .w-tint .w-sub { color: var(--grey); }
.w-sub .cy { color: var(--secondary); font-weight: 400; }

/* Cyan hairline used as a graphic beat */
.w-bar { width: 120px; height: 6px; background: var(--secondary); margin-bottom: 44px; }
.w-bar.wide { width: 100%; height: 1px; background: rgba(255,255,255,0.22); margin: 56px 0 0 0; }

/* --- Level rail: a persistent 1..5 climb marker on the right edge --- */
.w-rail { position: absolute; right: 120px; top: 50%; transform: translateY(-50%); z-index: 3;
  display: flex; flex-direction: column; gap: 26px; align-items: flex-end; }
.w-rail .step {
  display: flex; align-items: center; gap: 20px;
  font-family: var(--font-body); font-weight: 600; font-size: 24px;
  letter-spacing: 0.04em; color: rgba(255,255,255,0.32);
}
.w-rail .step .tick { width: 44px; height: 4px; background: rgba(255,255,255,0.22); }
.w-rail .step.on { color: var(--secondary); font-size: 32px; }
.w-rail .step.on .tick { width: 96px; height: 6px; background: var(--secondary); }
.w-rail .step.done { color: rgba(255,255,255,0.55); }
.w-rail .step.done .tick { background: rgba(255,255,255,0.42); }

/* --- Two-panel compare (data safety) --- */
.w-two { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 12px; }
.w-panel { border: 1px solid rgba(255,255,255,0.26); padding: 44px 44px 48px 44px; }
.w-panel .cap {
  font-family: var(--font-body); font-weight: 600; font-size: 24px; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--secondary); margin-bottom: 24px;
}
.w-panel h4 { font-family: var(--font-heading); font-weight: 600; font-size: 44px; line-height: 1.1; margin: 0 0 24px 0; color: var(--white); }
.w-panel p { font-family: var(--font-body); font-weight: 400; font-size: 28px; line-height: 1.45; margin: 0; color: rgba(255,255,255,0.82); }
.w-panel.warm .cap { color: var(--coral); }
.w-band {
  margin-top: 40px; border-left: 6px solid var(--secondary); padding: 30px 40px;
  background: rgba(0,161,226,0.10);
  font-family: var(--font-heading); font-weight: 300; font-size: 34px; line-height: 1.35; color: var(--white);
}
.w-band strong { font-weight: 600; color: var(--secondary); }

/* --- Numbered rows --- */
.w-rows { display: flex; flex-direction: column; gap: 26px; margin-top: 8px; }
.w-row { display: grid; grid-template-columns: 120px 1fr; align-items: start; gap: 36px;
  padding-bottom: 26px; border-bottom: 1px solid #d1d6dc; }
.w-dark .w-row { border-bottom-color: rgba(255,255,255,0.18); }
.w-row:last-child { border-bottom: none; }
.w-row .n { font-family: var(--font-heading); font-weight: 300; font-size: 64px; line-height: 1; color: var(--secondary); }
.w-row h4 { font-family: var(--font-heading); font-weight: 600; font-size: 40px; line-height: 1.15; margin: 0 0 12px 0; }
.w-light .w-row h4, .w-tint .w-row h4 { color: var(--primary); }
.w-dark .w-row h4 { color: var(--white); }
.w-row p { font-family: var(--font-body); font-weight: 400; font-size: 28px; line-height: 1.4; margin: 0; }
.w-light .w-row p, .w-tint .w-row p { color: var(--grey); }
.w-dark .w-row p { color: rgba(255,255,255,0.78); }

/* --- Tiles (three across) --- */
.w-tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 36px; margin-top: 20px; }
.w-tile { border: 1px solid #d1d6dc; background: var(--white); padding: 40px 36px 44px 36px; }
.w-dark .w-tile { background: transparent; border-color: rgba(255,255,255,0.26); }
.w-tile .cap { font-family: var(--font-body); font-weight: 600; font-size: 24px; letter-spacing: 0.16em;
  text-transform: uppercase; color: var(--secondary); margin-bottom: 22px; }
.w-tile h4 { font-family: var(--font-heading); font-weight: 600; font-size: 38px; line-height: 1.12; margin: 0 0 18px 0; color: var(--primary); }
.w-dark .w-tile h4 { color: var(--white); }
.w-tile p { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.45; margin: 0; color: var(--grey); }
.w-dark .w-tile p { color: rgba(255,255,255,0.78); }
.w-tile .huge { font-family: var(--font-heading); font-weight: 300; font-size: 96px; line-height: 1; color: var(--secondary); margin-bottom: 16px; }

/* --- Big stat block --- */
.w-stat { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 80px; align-items: center; margin-top: 20px; }
.w-stat .num { font-family: var(--font-heading); font-weight: 300; font-size: 200px; line-height: 0.92; color: var(--secondary); letter-spacing: -0.02em; }
.w-stat .src { font-family: var(--font-body); font-weight: 400; font-size: 24px; letter-spacing: 0.04em; color: rgba(255,255,255,0.55); margin-top: 22px; }
.w-light .w-stat .src, .w-tint .w-stat .src { color: var(--grey-medium); }
.w-stat .say { font-family: var(--font-heading); font-weight: 300; font-size: 44px; line-height: 1.28; }
.w-dark .w-stat .say { color: rgba(255,255,255,0.86); }
.w-light .w-stat .say, .w-tint .w-stat .say { color: var(--primary); }

/* --- Score buckets --- */
.w-buckets { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 36px; }
.w-bucket { border-top: 6px solid var(--secondary); padding-top: 26px; }
.w-bucket .rng { font-family: var(--font-heading); font-weight: 300; font-size: 76px; line-height: 1; color: var(--primary); }
.w-bucket .verb { font-family: var(--font-heading); font-weight: 600; font-size: 40px; margin-top: 14px; color: var(--secondary); }
.w-bucket p { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.4; margin: 14px 0 0 0; color: var(--grey); }

/* --- Split: statement left, list right --- */
.w-split { display: grid; grid-template-columns: 1fr 1fr; gap: 96px; align-items: start; }
.w-split .lead { font-family: var(--font-heading); font-weight: 300; font-size: 34px; line-height: 1.4; color: var(--grey); margin: 28px 0 0 0; }
.w-list { display: flex; flex-direction: column; gap: 26px; }
.w-item { display: grid; grid-template-columns: 6px 1fr; gap: 26px; }
.w-item .pip { background: var(--secondary); }
.w-item h5 { font-family: var(--font-heading); font-weight: 600; font-size: 32px; line-height: 1.2; margin: 0 0 8px 0; color: var(--primary); }
.w-item p { font-family: var(--font-body); font-weight: 400; font-size: 26px; line-height: 1.4; margin: 0; color: var(--grey); }

/* --- Quote-scale statement slide --- */
.w-statement { max-width: 1560px; }
.w-statement .strike { position: relative; }
.w-statement .strike:after {
  content: ""; position: absolute; left: -6px; right: -6px; top: 52%; height: 6px;
  background: var(--coral); transform: rotate(-1.2deg);
}

/* Corner mark on dark slides */
.w-mark { position: absolute; top: 48px; left: 120px; height: 36px; width: auto;
  filter: brightness(0) invert(1); opacity: 0.85; z-index: 3; }
</style>"""


def meta_dark(section, num):
    return (f'<div class="page-meta" style="color:rgba(255,255,255,0.55);">'
            f'<span>{section}</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span>'
            f'<span>{num}</span></div>')


def meta_light(section, num):
    return f'<div class="page-meta"><span>{section}</span><span class="rule"></span><span>{num}</span></div>'


LEVEL_NAMES = ["Ask better", "Give it memory", "Custom apps", "Agents", "Full context"]


def rail(active):
    """Vertical 1..5 climb marker. Shows where the room is in the five levels."""
    out = ['<div class="w-rail">']
    for i in range(1, 6):
        cls = "step on" if i == active else ("step done" if i < active else "step")
        out.append(f'<div class="{cls}"><span>{i}</span><span class="tick"></span></div>')
    out.append('</div>')
    return "".join(out)


DARK_MARK = f'<img src="{LOGO}" alt="Aseva" class="w-mark" />'

BODY = f'''
<deck-stage width="1920" height="1080">

<!-- 01 TITLE -->
<section data-label="01 Title" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <img src="{LOGO}" alt="Aseva" style="height:112px;width:auto;margin-bottom:60px;display:block;filter:brightness(0) invert(1);" />
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.32em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-bottom:40px;">A working session on AI</div>
      <p class="kicker" style="font-size:92px;line-height:1.04;max-width:1420px;">You're already using AI.<br/>You're using a <em>fraction</em> of it.</p>
      <div style="font-family:var(--font-heading);font-weight:300;font-size:40px;color:rgba(255,255,255,0.72);margin-top:40px;">Five levels. Shown live.</div>
    </div>
  </div>
</section>

<!-- 02 HANDS TEST -->
<section data-label="02 Hands test" class="w-dark">
  {DARK_MARK}
  <div class="frame">
    <div class="w-bar"></div>
    <h2 class="w-h1 xl" style="max-width:1500px;">Who used ChatGPT<br/>this week?</h2>
    <div class="w-band" style="margin-top:56px;max-width:1400px;">Now keep your hand up if it was for more than <strong>search or summarizing an email</strong>.</div>
  </div>
  {meta_dark("Aseva · Show of hands", "02")}
</section>

<!-- 03 THE ONE IDEA -->
<section data-label="03 One idea" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame">
    <p class="w-eyebrow muted">Hold onto this</p>
    <h2 class="w-h1 lg w-statement">AI doesn't replace your people.<br/>It makes them <span class="cy">more powerful</span>.</h2>
    <p class="w-sub">Everything you'll see today was built or run by regular people at our company. None of them are programmers.</p>
  </div>
  {meta_dark("Aseva", "03")}
</section>

<!-- 04 LEVEL 1 -->
<section data-label="04 Level 1 Ask better" class="w-dark">
  {DARK_MARK}
  {rail(1)}
  <div class="frame">
    <p class="w-eyebrow">Level 1 of 5</p>
    <h2 class="w-h1 xl" style="max-width:1180px;">Ask better.</h2>
    <p class="w-sub" style="max-width:1120px;">Don't ask it for the answer. Make it <span class="cy">interview you</span>.</p>
    <div class="w-band" style="max-width:1120px;">"Ask me one question at a time until you know enough to write this."</div>
  </div>
  {meta_dark("Aseva · Level 1 · Live", "04")}
</section>

<!-- 05 LEVEL 2 -->
<section data-label="05 Level 2 Give it memory" class="w-dark">
  {DARK_MARK}
  {rail(2)}
  <div class="frame">
    <p class="w-eyebrow">Level 2 of 5</p>
    <h2 class="w-h1 xl" style="max-width:1180px;">Give it memory.</h2>
    <p class="w-sub" style="max-width:1120px;">Level 1 is a smart stranger.<br/>Level 2 <span class="cy">knows your business</span>.</p>
  </div>
  {meta_dark("Aseva · Level 2 · Live", "05")}
</section>

<!-- 06 DATA SAFETY -->
<section data-label="06 Data safety" class="w-dark">
  {DARK_MARK}
  <div class="frame">
    <p class="w-eyebrow muted">Before you upload anything</p>
    <h2 class="w-h1 md" style="margin-bottom:44px;">Is my data safe? <span class="cy">Three rules.</span></h2>
    <div class="w-two">
      <div class="w-panel">
        <div class="cap">Rule one</div>
        <h4>Safe to paste</h4>
        <p>Anything you'd hand a new contractor on day one. Draft copy, public information, general questions, the files you already pass around.</p>
      </div>
      <div class="w-panel warm">
        <div class="cap">Rule two</div>
        <h4>Not safe to paste</h4>
        <p>Passwords, customer records, anything you are legally on the hook to protect. When in doubt, leave it out.</p>
      </div>
    </div>
    <div class="w-band"><strong>Rule three.</strong> A paid business account means your data is not used to train the model. That one switch covers most of the worry.</div>
  </div>
  {meta_dark("Aseva · Data safety", "06")}
</section>

<!-- 07 LEVEL 3 -->
<section data-label="07 Level 3 Custom apps" class="w-dark">
  {DARK_MARK}
  {rail(3)}
  <div class="frame">
    <p class="w-eyebrow">Level 3 of 5</p>
    <h2 class="w-h1 xl" style="max-width:1180px;">Custom apps.</h2>
    <p class="w-sub" style="max-width:1120px;">Most people think this means a six figure project.<br/><span class="cy">It doesn't.</span></p>
  </div>
  {meta_dark("Aseva · Level 3", "07")}
</section>

<!-- 08 THE APPS -->
<section data-label="08 The apps" class="w-tint">
  {WAVE_SOFT}
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Three real apps · running live</p>
    <h2 class="w-h1 md" style="margin-bottom:40px;">None of these were built<br/>by a developer.</h2>
    <div class="w-tiles">
      <div class="w-tile">
        <div class="cap">In use today</div>
        <h4>Contract generator</h4>
        <p>Built in three evenings by someone who does not write code.</p>
      </div>
      <div class="w-tile">
        <div class="cap">Internal demo</div>
        <h4>Call Coach</h4>
        <p>The executive watching asked for phase two before the demo ended.</p>
      </div>
      <div class="w-tile">
        <div class="cap">Take out your phone</div>
        <h4>This room's app</h4>
        <p>Built this morning, for this room.</p>
      </div>
    </div>
  </div>
  {meta_light("Aseva · Level 3 · Live", "08")}
</section>

<!-- 09 LEVEL 4 AGENTS -->
<section data-label="09 Level 4 Agents" class="w-dark">
  {DARK_MARK}
  {rail(4)}
  <div class="frame">
    <p class="w-eyebrow">Level 4 of 5</p>
    <h2 class="w-h1 lg" style="max-width:1180px;">An agent is AI you<br/><span class="cy">stop asking</span>.</h2>
    <div class="w-rows" style="margin-top:48px;max-width:1180px;">
      <div class="w-row"><div class="n">01</div><div><h4>A goal, and memory</h4><p>A standing job it works toward, and it remembers what happened last time.</p></div></div>
      <div class="w-row"><div class="n">02</div><div><h4>Tools it can actually touch</h4><p>Your email, your calendar, your systems. Not just a chat window.</p></div></div>
      <div class="w-row"><div class="n">03</div><div><h4>Rules for acting alone</h4><p>It knows when to go ahead and when to come back to you. You deputize it. You stay the sheriff.</p></div></div>
    </div>
  </div>
  {meta_dark("Aseva · Level 4 · Live", "09")}
</section>

<!-- 10 LEVEL 5 -->
<section data-label="10 Level 5 Full context" class="w-dark">
  {DARK_MARK}
  {rail(5)}
  <div class="frame">
    <p class="w-eyebrow">Level 5 of 5</p>
    <h2 class="w-h1 xl" style="max-width:1180px;">Full context.</h2>
    <p class="w-sub" style="max-width:1120px;">What happens when it knows <span class="cy">everything</span>. Every meeting, every email, every idea.</p>
  </div>
  {meta_dark("Aseva · Level 5 · Live", "10")}
</section>

<!-- 11 THE LINE -->
<section data-label="11 The line" class="w-dark">
  {WAVE_SOFT}
  {DARK_MARK}
  <div class="frame">
    <p class="w-eyebrow muted">If you leave with one line</p>
    <h2 class="w-h1 lg w-statement">The AI didn't get <span class="strike">smarter</span>.<br/>What changed is <span class="cy">what it knows</span>.</h2>
    <p class="w-sub">Same AI in all five demos. Only the context changed.</p>
  </div>
  {meta_dark("Aseva", "11")}
</section>

<!-- 12 WHICH TOOL -->
<section data-label="12 Which tool" class="w-light">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">The buying question</p>
    <h2 class="w-h1 md" style="max-width:1500px;">Which tool to buy matters less<br/>than owning <span class="cy">what it learns</span>.</h2>
    <div class="w-split" style="margin-top:56px;">
      <div>
        <p class="lead" style="margin-top:0;">We started this whole system on one tool and moved big pieces of it to another. We lost nothing, because the knowledge lives in our files and not inside one company's product.</p>
      </div>
      <div class="w-list">
        <div class="w-item"><div class="pip"></div><div><h5>Pick any of them</h5><p>Tools change every month. Starting beats picking perfectly.</p></div></div>
        <div class="w-item"><div class="pip"></div><div><h5>Keep the context portable</h5><p>What AI learns about your business has to stay yours and move with you.</p></div></div>
      </div>
    </div>
  </div>
  {meta_light("Aseva", "12")}
</section>

<!-- 13 CUSTOMERS AI -->
<section data-label="13 Customers AI" class="w-dark">
  {DARK_MARK}
  <div class="frame">
    <p class="w-eyebrow muted">Now flip it</p>
    <h2 class="w-h1 md" style="margin-bottom:20px;">Your customers' AI is already<br/>choosing <span class="cy">who to hire</span>.</h2>
    <div class="w-stat">
      <div>
        <div class="num">3x</div>
        <div class="src">AI driven business traffic, year over year. Source: Shopify.</div>
      </div>
      <div class="say">People ask ChatGPT who to hire near them. The businesses that get recommended are the ones AI can actually read.<br/><br/><span style="color:var(--secondary);">Homework tonight: ask ChatGPT about your own business.</span></div>
    </div>
  </div>
  {meta_dark("Aseva", "13")}
</section>

<!-- 14 THE HONEST PART -->
<section data-label="14 The honest part" class="w-light">
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">The honest part</p>
    <h2 class="w-h1 md" style="margin-bottom:34px;">Four things I'd rather tell you now.</h2>
    <div class="w-rows">
      <div class="w-row"><div class="n">01</div><div><h4>95 percent of company AI pilots produce nothing measurable</h4><p>Not because the AI failed. Because they bought a tool and hoped. Source: MIT.</p></div></div>
      <div class="w-row"><div class="n">02</div><div><h4>Heavy AI adopters grew headcount 10 percent</h4><p>It punishes cutting before you redesign, and rewards making your people more powerful. Source: Ramp and Revelio, 21,000 firms.</p></div></div>
      <div class="w-row"><div class="n">03</div><div><h4>Adoption spreads by one visible win, not a memo</h4><p>How it went at our company: one engineer, then me, then our VP of Engineering, then the rest of the team, then our GM, finally our owner.</p></div></div>
      <div class="w-row"><div class="n">04</div><div><h4>Someone has to own it</h4><p>Roughly triple the return when a named person is accountable. In a business your size, that is you. Source: KPMG.</p></div></div>
    </div>
  </div>
  {meta_light("Aseva · The honest part", "14")}
</section>

<!-- 15 YOUR TURN -->
<section data-label="15 Your turn" class="w-tint">
  {WAVE_SOFT}
  {CORNER}
  <div class="frame">
    <p class="w-eyebrow">Your turn · the Deputization Audit</p>
    <h2 class="w-h1 md" style="max-width:1500px;">Write five weekly tasks you'd love<br/>to <span class="cy">never do again</span>.</h2>
    <p class="w-sub" style="font-size:34px;margin-top:28px;">Score each one on the worksheet, then find its bucket.</p>
    <div class="w-buckets">
      <div class="w-bucket"><div class="rng">8 to 10</div><div class="verb">Deputize</div><p>Hand it off. Set the rules and check the output.</p></div>
      <div class="w-bucket"><div class="rng">4 to 7</div><div class="verb">Duet</div><p>AI does part of it. You stay in the loop.</p></div>
      <div class="w-bucket"><div class="rng">0 to 3</div><div class="verb">Defend</div><p>This one stays yours. Protect the time for it.</p></div>
    </div>
  </div>
  {meta_light("Aseva · Your turn", "15")}
</section>

<!-- 16 CLOSE -->
<section data-label="16 Close" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--secondary);margin-bottom:48px;">One ask</div>
      <h1 class="title" style="color:#ffffff;font-size:104px;line-height:1.03;max-width:1500px;">Pick one task.<br/>Deputize it <span style="color:var(--secondary);">this month</span>.</h1>
      <p style="font-family:var(--font-heading);font-weight:300;font-size:42px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1360px;line-height:1.3;">The AI didn't get smarter. What changed is what it knows.</p>
    </div>
  </div>
  <div class="footer-line">Cheat sheet at the door · aseva.com · (800) 456-5800</div>
</section>

</deck-stage>
'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Aseva · AI Workshop</title>
<meta name="pluribus-source" content="Output/Drafts/AI Workshop - Slide Brief v2 - 2026-08-31.md" />
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

out = root / "prospect-ai-workshop-simple-deck.html"
out.write_text(html)
print(f"wrote {out} ({len(html):,} bytes)")

assert "data:image/png;base64" in html
assert "customElements.define" in html
assert 'src="assets/' not in html
assert 'src="deck-stage.js"' not in html
# Em/en dash scan runs against the AUTHORED copy only. The inlined deck-stage.js
# and template CSS carry em dashes in their own code comments.
for name, blob in (("BODY", BODY), ("EXTRA_CSS", EXTRA_CSS)):
    assert "—" not in blob, f"em dash found in {name}"
    assert "–" not in blob, f"en dash found in {name}"
assert "--" not in BODY.replace("var(--", "").replace("<!--", "").replace("-->", ""), "double hyphen in slide copy"
print("checks passed:", BODY.count("<section data-label"), "slides")
