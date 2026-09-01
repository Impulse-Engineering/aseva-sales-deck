#!/usr/bin/env python3
"""Assemble the standalone AI Workshop deck.

This is NOT a prospect sales deck. It is the slide backdrop for Chris's
90-minute small-business AI workshop. It reuses the Aseva design system
(tokens, fonts, archetypes, waveform, page-meta) so it looks unmistakably
Aseva, but it deliberately omits the sales-deck mandatory slides (Who We Are
three-pillar positioning, sales CTA). The workshop is not a pitch; contact
appears once, on the final slide footer.

Source brief: SecondBrain Output/Drafts/AI Workshop - Slide Brief - 2026-08-31.md
"""
import base64
import pathlib

root = pathlib.Path(__file__).parent
tpl = (root / "template/template.html").read_text()

# 1. Exact <style> block from the template (all archetypes).
style = tpl[tpl.index("<style>"): tpl.index("</style>") + len("</style>")]

# 2. deck-stage.js inlined.
deckjs = (root / "template/deck-stage.js").read_text()

# 3. Base64 the assets we reference.
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

CORNER = f'<img src="{LOGO}" alt="Aseva" class="corner-logo" />'

# Helper: white page-meta for dark slides
def meta_dark(section, num):
    return f'<div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>{section}</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>{num}</span></div>'

def meta_light(section, num):
    return f'<div class="page-meta"><span>{section}</span><span class="rule"></span><span>{num}</span></div>'

# Reusable level-marker kicker (cyan on dark)
def level_kicker(n):
    return f'<div class="kicker">Level {n} of 5</div>'

BODY = f'''
<deck-stage width="1920" height="1080">

<!-- ================= 01 TITLE ================= -->
<section data-label="01 Title" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <img src="{LOGO}" alt="Aseva" style="height:120px;width:auto;margin-bottom:56px;display:block;filter:brightness(0) invert(1);" />
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.32em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-bottom:40px;">A working session on AI</div>
      <p class="kicker" style="font-size:84px;line-height:1.06;max-width:1400px;">You're already using AI.<br/>You're using a <em>fraction</em> of it.</p>
      <div style="font-family:var(--font-heading);font-weight:300;font-size:38px;color:rgba(255,255,255,0.72);margin-top:36px;">Five levels, shown live.</div>
    </div>
  </div>
</section>

<!-- ================= 02 OPENER - HANDS TEST ================= -->
<section data-label="02 Hands test" class="section-divider">
  <div class="frame">
    <div class="kicker">Show of hands</div>
    <h2 style="font-size:88px;line-height:1.05;max-width:1500px;">Who used ChatGPT<br/>this week?</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:44px;color:rgba(255,255,255,0.72);margin-top:44px;max-width:1300px;line-height:1.3;">Keep your hand up if it was for more than search or summarizing an email.</div>
  </div>
  {meta_dark("Aseva", "02")}
</section>

<!-- ================= 03 THE ONE IDEA ================= -->
<section data-label="03 The one idea" class="section-divider">
  {WAVE_SOFT}
  <div class="frame">
    <div class="kicker">Hold onto this</div>
    <h2 style="font-size:84px;line-height:1.05;max-width:1520px;">AI doesn't replace your people.<br/>It makes them <span style="color:var(--secondary);">more powerful</span>.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:38px;color:rgba(255,255,255,0.72);margin-top:40px;max-width:1300px;line-height:1.35;">Everything you'll see today was built or run by regular people, not programmers.</div>
  </div>
  {meta_dark("Aseva", "03")}
</section>

<!-- ================= 04 LEVEL 1 - ASK BETTER ================= -->
<section data-label="04 Level 1 Ask better" class="section-divider">
  <div class="frame">
    {level_kicker(1)}
    <h2 style="font-size:96px;line-height:1.02;">Ask better.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:44px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1300px;line-height:1.3;">Don't ask it for the answer. Make it <span style="color:var(--secondary);">interview you</span>.</div>
  </div>
  {meta_dark("Aseva · Level 1", "04")}
</section>

<!-- ================= 05 LEVEL 2 - GIVE IT MEMORY ================= -->
<section data-label="05 Level 2 Give it memory" class="section-divider">
  <div class="frame">
    {level_kicker(2)}
    <h2 style="font-size:96px;line-height:1.02;">Give it memory.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:44px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1320px;line-height:1.3;">Level 1 is a smart stranger. Level 2 knows your business.</div>
  </div>
  {meta_dark("Aseva · Level 2", "05")}
</section>

<!-- ================= 06 DATA SAFETY ================= -->
<section data-label="06 Data safety" class="diff">
  {WAVE_SOFT}
  <div class="frame">
    <p class="eyebrow">Before you upload anything</p>
    <h2 class="title">Is my data safe?</h2>
    <p class="lede">The number one reason owners hold back. Three simple rules, and you can stop worrying about the rest.</p>
    <div class="three">
      <div class="card">
        <h4>Safe to paste</h4>
        <p>Anything you'd email a new contractor. Draft copy, public info, general questions, and files you already share day to day.</p>
      </div>
      <div class="card">
        <h4>Not safe to paste</h4>
        <p>Passwords, customer records, anything you're legally on the hook to protect. When in doubt, leave it out.</p>
      </div>
      <div class="card">
        <h4>What a business account changes</h4>
        <p>A paid business account means your data isn't used to train the model. That one switch covers most of the worry.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Data safety", "06")}
</section>

<!-- ================= 07 LEVEL 3 - CUSTOM APPS ================= -->
<section data-label="07 Level 3 Custom apps" class="section-divider">
  <div class="frame">
    {level_kicker(3)}
    <h2 style="font-size:96px;line-height:1.02;">Custom apps.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:44px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1360px;line-height:1.3;">Most people think this means a six-figure project. It doesn't.</div>
  </div>
  {meta_dark("Aseva · Level 3", "07")}
</section>

<!-- ================= 08 CUSTOM APP DEMOS (live holder) ================= -->
<section data-label="08 Custom app demos" class="diff">
  {WAVE_SOFT}
  <div class="frame">
    <p class="eyebrow" style="color:rgba(255,255,255,0.55);">Three real apps · live</p>
    <h2 class="title" style="color:#ffffff;">Watch, don't take notes.</h2>
    <div class="three">
      <div class="card" style="background:transparent;border:1px solid rgba(255,255,255,0.28);">
        <h4 style="color:var(--secondary);">Contract generator</h4>
        <p style="color:rgba(255,255,255,0.82);">Built in three evenings, by a non-programmer. In use today.</p>
      </div>
      <div class="card" style="background:transparent;border:1px solid rgba(255,255,255,0.28);">
        <h4 style="color:var(--secondary);">Call Coach</h4>
        <p style="color:rgba(255,255,255,0.82);">The internal demo where the exec asked for phase two before it ended.</p>
      </div>
      <div class="card" style="background:transparent;border:1px solid rgba(255,255,255,0.28);">
        <h4 style="color:var(--secondary);">This room's app</h4>
        <p style="color:rgba(255,255,255,0.82);">Built this morning, for this room. Take out your phone.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 3 · Live", "08")}
</section>

<!-- ================= 09 LEVEL 4 - AGENTS ================= -->
<section data-label="09 Level 4 Agents" class="diff">
  {WAVE_SOFT}
  <div class="frame">
    {level_kicker(4)}
    <h2 class="title" style="color:#ffffff;margin-top:24px;">An agent is AI you <em>stop asking</em>.</h2>
    <div class="three" style="margin-top:20px;">
      <div class="card" style="background:transparent;border:1px solid rgba(255,255,255,0.28);">
        <h4 style="color:var(--secondary);">A goal</h4>
        <p style="color:rgba(255,255,255,0.82);">A standing job it's working toward, not a one-off question.</p>
      </div>
      <div class="card" style="background:transparent;border:1px solid rgba(255,255,255,0.28);">
        <h4 style="color:var(--secondary);">Memory and tools</h4>
        <p style="color:rgba(255,255,255,0.82);">It remembers, and it can touch your real systems: email, calendar, billing.</p>
      </div>
      <div class="card" style="background:transparent;border:1px solid rgba(255,255,255,0.28);">
        <h4 style="color:var(--secondary);">Rules, and it learns</h4>
        <p style="color:rgba(255,255,255,0.82);">It knows when to act alone versus check with a human, and it gets better the longer it runs.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Level 4", "09")}
</section>

<!-- ================= 10 DEPUTIZE ================= -->
<section data-label="10 Deputize" class="section-divider">
  <div class="frame">
    <div class="kicker">The word for it</div>
    <h2 style="font-size:128px;line-height:1;letter-spacing:-0.01em;">Deputize.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:44px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1320px;line-height:1.3;">You hand it the job and the authority. You stay the <span style="color:var(--secondary);">sheriff</span>.</div>
  </div>
  {meta_dark("Aseva", "10")}
</section>

<!-- ================= 11 LEVEL 5 - FULL CONTEXT (live holder) ================= -->
<section data-label="11 Level 5 Full context" class="section-divider">
  <div class="frame">
    {level_kicker(5)}
    <h2 style="font-size:96px;line-height:1.02;">Full context.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:44px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1360px;line-height:1.3;">What happens when it knows <span style="color:var(--secondary);">everything</span>. Every meeting, every email, every idea you said out loud in the car.</div>
  </div>
  {meta_dark("Aseva · Level 5 · Live", "11")}
</section>

<!-- ================= 12 THE LINE ================= -->
<section data-label="12 The line" class="section-divider">
  {WAVE_SOFT}
  <div class="frame">
    <div class="kicker">The whole game</div>
    <h2 style="font-size:80px;line-height:1.08;max-width:1560px;">The AI didn't get smarter<br/>between those demos.<br/>What changed is <span style="color:var(--secondary);">what it knows</span>.</h2>
  </div>
  {meta_dark("Aseva", "12")}
</section>

<!-- ================= 13 WHICH TOOL SHOULD I BUY ================= -->
<section data-label="13 Which tool" class="who">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">The buying advice you came for</p>
    <h2 class="title">Which tool should I buy?</h2>
    <div class="grid">
      <div>
        <p class="pitch">
          Tools change every month. We started this whole system on <span class="mark">one tool</span> and moved big pieces to another, and lost nothing.
          <br/><br/>
          The reason: the knowledge lives in <strong>our files</strong>, not inside one company's product. Whatever you pick, make sure what it learns about your business is yours and moves with you.
        </p>
      </div>
      <div class="stats">
        <div class="stat">
          <div class="n">Any</div>
          <div class="lbl">The tool matters less than you think. Pick one and start.</div>
        </div>
        <div class="stat">
          <div class="n">Yours</div>
          <div class="lbl">What it learns about your business has to belong to you.</div>
        </div>
      </div>
    </div>
  </div>
  {meta_light("Aseva", "13")}
</section>

<!-- ================= 14 YOUR CUSTOMERS' AI ================= -->
<section data-label="14 Customers AI" class="section-divider">
  <div class="frame">
    <div class="kicker">Now flip it</div>
    <h2 style="font-size:76px;line-height:1.06;max-width:1560px;">Your customers' AI is<br/>already <span style="color:var(--secondary);">choosing</span>.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:40px;color:rgba(255,255,255,0.72);margin-top:36px;max-width:1360px;line-height:1.35;">People ask ChatGPT who to hire near them. The businesses that get recommended are the ones whose websites AI can actually read. Tonight, ask ChatGPT about your own business. That's homework.</div>
  </div>
  {meta_dark("Aseva", "14")}
</section>

<!-- ================= 15 THE HONEST PART ================= -->
<section data-label="15 The honest part" class="whyus">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">The honest part</p>
    <div class="split">
      <div class="left">
        <div class="rule-cyan"></div>
        <h2>What nobody selling AI will <em>tell you</em>.</h2>
        <p>Most AI efforts go nowhere, and it's almost never the technology's fault. It's how the business went about it.</p>
        <p>The ones that work make their existing people more powerful, name an owner, and spread by showing one real win instead of sending a memo.</p>
      </div>
      <div class="right reasons">
        <div class="reason">
          <div class="idx">01</div>
          <div>
            <h5>Most pilots produce nothing measurable</h5>
            <p>Not because the AI failed. Because they bought a tool and hoped. (MIT)</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">02</div>
          <div>
            <h5>Heavy adopters grew headcount</h5>
            <p>Up 10 percent over two years, including entry level. A third of so-called AI layoffs quietly rehired. (Ramp / Revelio, 21,000 firms)</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">03</div>
          <div>
            <h5>It spreads by one visible win</h5>
            <p>How it spread at our company: one engineer, then me, then our VP of Engineering, then the rest, then our GM, finally our owner. No memo.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">04</div>
          <div>
            <h5>Someone has to own it</h5>
            <p>About triple the return when a named person is accountable. In a business your size, that's probably you. (KPMG)</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  {meta_light("Aseva · The honest part", "15")}
</section>

<!-- ================= 16 YOUR TURN - THE AUDIT ================= -->
<section data-label="16 Your turn" class="who">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Your turn</p>
    <h2 class="title">Five tasks you'd love<br/>to never do again.</h2>
    <div class="grid">
      <div>
        <p class="pitch">
          On the worksheet, write down five weekly tasks you'd love to hand off. Score each one, then find its bucket.
          <br/><br/>
          You don't have to <strong>trust</strong> AI. You have to be able to <span class="mark">check it fast</span>. Then the real question: what would AI need to know to do this, and where does that live today. A system, a spreadsheet, or your head.
        </p>
      </div>
      <div class="stats">
        <div class="stat">
          <div class="n">8&ndash;10</div>
          <div class="lbl">Deputize. Hand it off.</div>
        </div>
        <div class="stat">
          <div class="n">4&ndash;7</div>
          <div class="lbl">Duet. AI does part, you stay in the loop.</div>
        </div>
        <div class="stat">
          <div class="n">0&ndash;3</div>
          <div class="lbl">Defend. This one's yours.</div>
        </div>
      </div>
    </div>
  </div>
  {meta_light("Aseva · Your turn", "16")}
</section>

<!-- ================= 17 CLOSE ================= -->
<section data-label="17 Close" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--secondary);margin-bottom:48px;">One ask</div>
      <h1 class="title" style="color:#ffffff;font-size:104px;line-height:1.03;max-width:1500px;">Pick one task.<br/>Deputize it <span style="color:var(--secondary);">this month</span>.</h1>
      <p style="font-family:var(--font-heading);font-weight:300;font-size:42px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1320px;line-height:1.3;">The AI didn't get smarter. What changed is what it knows.</p>
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
<title>Aseva , AI Workshop</title>
<meta name="pluribus-source" content="Output/Drafts/AI Workshop - Slide Brief - 2026-08-31.md" />
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;600;700&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
<script>
{deckjs}
</script>
{style}
</head>
<body>
{BODY}
</body>
</html>
'''

out = root / "prospect-ai-workshop-deck.html"
out.write_text(html)
print(f"wrote {out} ({len(html):,} bytes)")
assert "data:image/png;base64" in html
assert "customElements.define" in html
assert 'src="assets/' not in html
assert 'src="deck-stage.js"' not in html
# No em/en dash in the AUTHORED SLIDE COPY. Scanned against BODY, not the
# assembled file: the inlined deck-stage.js and template CSS carry em dashes
# in their own code comments, which no audience ever sees.
assert "—" not in BODY, "em dash found in slide copy"
assert "–" not in BODY, "raw en dash found in slide copy (use &ndash;)"
print("checks passed:", html.count("<section"), "sections")
