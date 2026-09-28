#!/usr/bin/env python3
"""Assemble the Aseva / BEGA AI Demos deck.

Source brief: SecondBrain Output/Drafts/BEGA - AI Demos Deck Brief - 2026-09-28.md

The deck is the frame around roughly 40 minutes of live app demos and 20 minutes of
discussion. Each app gets one light title slide, then the presenter switches to the
live app. Standard sales archetypes only: cover, section-divider, whyus, why, diff.

Two switches for Chris, both below:
  APPS                     demo lineup and order. Reorder or delete rows; slide numbers follow.
  SHOW_BILL_BUDDY_NUMBERS  off until Chris confirms the internal figures for a slide.
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

# Leave False until Chris confirms these go on a slide. Aseva's own reported
# internal figures. Keep recovered money and identified savings as separate lines.
SHOW_BILL_BUDDY_NUMBERS = False

# Demo lineup, in presentation order. Approved copy from the September 22 workshop
# deck. Order: Bill Buddy lands fastest; ANN goes last because an ANN-style tool on
# BEGA's own data is a candidate first build and it sets up the discussion.
# Fields: name, headline (<em> renders cyan), what it does.
APPS = [
    ("Bill Buddy",
     "Carrier bill reconciliation for <em>hundreds of circuits</em> across several carriers.",
     "Used by the whole accounts payable team, with approvals, lead sheets, and analytics."),
    ("ContractGen",
     "Contracts in minutes, <em>not hours</em>.",
     "Fills the contract, remembers every custom price, sends it for signature and pushes the "
     "order into billing. About 20 minutes off every contract."),
    ("Resolve",
     "Never miss an <em>on-call alert</em>.",
     "Pages, escalates, texts and calls from inside the tools the team already uses. "
     "The vendor said someday. We shipped it that week."),
    ("Aseva Learning",
     "Training that <em>tracks itself</em>.",
     "Courses, quizzes and completions for the whole team in one place, built for how we "
     "actually train."),
    ("Sales Radar",
     "The pipeline, <em>in plain English</em>.",
     "One dashboard over HubSpot and Apollo, so reps see what is moving without digging "
     "through either."),
    ("ANN",
     "One question, <em>answered across every system</em>.",
     "Billing, CRM, tickets, documents. Ask in plain English instead of asking the one "
     "person who knows."),
]

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

# The logo is inlined once as a CSS variable instead of once per slide.
CORNER = '<div class="corner-logo" role="img" aria-label="Aseva"></div>'

EXTRA_CSS = """<style>
:root { --aseva-logo: url(ASEVA_LOGO_URI); }
/* BEGA AI Demos additions. Tokens and fonts only, nothing under 24px. */
div.corner-logo { position: absolute; top: 48px; left: 120px; height: 36px; width: 156px;
  background: var(--aseva-logo) no-repeat left center / contain; z-index: 5; }

h2.title em { font-style: normal; color: var(--secondary); font-weight: 600; }
.why .frame { padding-top: 132px; }
.whyus .frame { padding-top: 132px; }
.diff .frame { padding-top: 120px; }

/* section dividers carry the waveform accent, per the design system */
.section-divider .wave-soft { position: absolute; right: -200px; bottom: -200px; width: 760px; opacity: 0.12; }
.section-divider .frame { z-index: 2; }

/* app title slides */
.section-divider .app-line {
  font-family: var(--font-heading); font-weight: 400; font-size: 60px; line-height: 1.14;
  color: var(--white); margin: 44px 0 0 0; max-width: 1480px;
}
.section-divider .app-line em { font-style: normal; color: var(--secondary); }
.section-divider .app-desc {
  font-family: var(--font-heading); font-weight: 300; font-size: 40px; line-height: 1.35;
  color: rgba(255,255,255,0.7); margin: 28px 0 0 0; max-width: 1380px;
}
.section-divider .app-stats {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px; margin-top: 56px; max-width: 1560px;
}
.section-divider .app-stats div { border-top: 2px solid var(--secondary); padding-top: 20px;
  font-family: var(--font-body); font-size: 26px; line-height: 1.4; color: rgba(255,255,255,0.82); }
.section-divider .app-src { font-family: var(--font-body); font-size: 24px; color: rgba(255,255,255,0.55);
  margin-top: 24px; letter-spacing: 0.04em; }

/* your turn: three questions, big type */
.section-divider .asks { margin-top: 56px; max-width: 1560px; }
.section-divider .ask { display: grid; grid-template-columns: 96px 1fr; gap: 32px; align-items: baseline;
  padding: 28px 0; border-top: 1px solid rgba(255,255,255,0.18); }
.section-divider .ask:last-child { border-bottom: 1px solid rgba(255,255,255,0.18); }
.section-divider .ask .n { font-family: var(--font-heading); font-weight: 300; font-size: 64px; line-height: 1;
  color: var(--secondary); }
.section-divider .ask p { font-family: var(--font-heading); font-weight: 300; font-size: 60px; line-height: 1.15;
  color: var(--white); margin: 0; }

/* close: prove, build, grow */
.cover .steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px; margin-top: 56px; max-width: 1560px; }
.cover .steps div { border-top: 2px solid var(--secondary); padding-top: 22px; }
.cover .steps h4 { font-family: var(--font-heading); font-weight: 600; font-size: 36px; color: var(--secondary);
  margin: 0 0 10px 0; }
.cover .steps p { font-family: var(--font-body); font-size: 26px; line-height: 1.45; color: rgba(255,255,255,0.82); margin: 0; }
</style>""".replace("ASEVA_LOGO_URI", LOGO)


def meta_light(section, num):
    return f'<div class="page-meta"><span>{section}</span><span class="rule"></span><span>{num:02d}</span></div>'


def meta_dark(section, num):
    return (f'<div class="page-meta" style="color:rgba(255,255,255,0.55);z-index:3;">'
            f'<span>{section}</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span>'
            f'<span>{num:02d}</span></div>')


BILL_BUDDY_STATS = '''
    <div class="app-stats">
      <div>Reconciliation dropped from roughly 30 hours a week to one or two.</div>
      <div>About $10,000 recovered in historical billing disputes.</div>
      <div>About $20,000 in monthly recurring savings identified in the first week.</div>
    </div>
    <div class="app-src">Aseva's own reported internal figures.</div>'''


def app_slide(num, idx, total, name, line, desc):
    stats = BILL_BUDDY_STATS if (name == "Bill Buddy" and SHOW_BILL_BUDDY_NUMBERS) else ""
    return f'''
<section data-label="{num:02d} Demo {name}" class="section-divider">
  {WAVE_SOFT}
  <div class="frame">
    <div class="kicker">Live demo · {idx} of {total}</div>
    <h2>{name}</h2>
    <p class="app-line">{line}</p>
    <p class="app-desc">{desc}</p>{stats}
  </div>
  {meta_dark("Aseva · Live demo", num)}
</section>
'''


N_APPS = len(APPS)
N_WORD = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][N_APPS]
FIRST_APP = 5
AFTER = FIRST_APP + N_APPS            # first slide after the demos
S_LEARNED, S_TURN, S_FIRST, S_CLOSE = AFTER, AFTER + 1, AFTER + 2, AFTER + 3

app_slides = "".join(
    app_slide(FIRST_APP + i, i + 1, N_APPS, *app) for i, app in enumerate(APPS)
)

BODY = f'''
<deck-stage width="1920" height="1080">

<!-- 01 COVER -->
<section data-label="01 Cover" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <img src="{LOGO}" alt="Aseva" style="height:120px;width:auto;margin-bottom:64px;display:block;filter:brightness(0) invert(1);" />
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.32em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-bottom:40px;">September 28, 2026</div>
      <p class="kicker" style="font-size:112px;line-height:1.02;max-width:1500px;">Aseva / BEGA<br/><em>AI Demos</em></p>
      <div style="font-family:var(--font-heading);font-weight:300;font-size:40px;color:rgba(255,255,255,0.72);margin-top:40px;max-width:1300px;line-height:1.3;">Finished apps our own teams use every day, then what BEGA builds first.</div>
    </div>
  </div>
  <div class="footer-line">aseva.com · (800) 456-5800</div>
</section>

<!-- 02 TODAY -->
<section data-label="02 Today" class="diff">
  {WAVE_SOFT}
  <div class="frame">
    <p class="eyebrow">Today</p>
    <h2 class="title">{N_WORD} live apps,<br/>then <em>your first build</em>.</h2>
    <p class="lede">Each app gets one slide, then we switch to the real thing.</p>
    <div class="three">
      <div class="card">
        <h4>What we built</h4>
        <p>{N_WORD} apps our own teams open every day to do their jobs. About forty minutes, all live.</p>
      </div>
      <div class="card">
        <h4>How we built it</h4>
        <p>Every one started as a written problem, then got built with AI coding tools and hosted on our own platform.</p>
      </div>
      <div class="card">
        <h4>What BEGA builds first</h4>
        <p>The last twenty minutes are a conversation about where your team loses time, and which system we start on.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · Today", 2)}
</section>

<!-- 03 WHO WE ARE -->
<section data-label="03 Who we are" class="whyus">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Who we are</p>
    <div class="split">
      <div class="left">
        <div class="rule-cyan"></div>
        <h2>We fix the slow, <em>expensive</em> parts of how work gets done.</h2>
        <p>We find where your team loses time or money, then build the application, integration, or automation that fixes it.</p>
        <p>AI is the enabler. It lets us build that work faster and less expensively.</p>
        <p>Behind it is the same Aseva you already know, with more than thirty years of running service provider operations and cybersecurity.</p>
      </div>
      <div class="right reasons">
        <div class="reason">
          <div class="idx">01</div>
          <div>
            <h5>Business process optimization</h5>
            <p>We map how the work actually gets done and find the steps that cost the most time or money.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">02</div>
          <div>
            <h5>Custom applications</h5>
            <p>Apps built around your workflow and used by the whole team, not one person's laptop.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">03</div>
          <div>
            <h5>Integrations</h5>
            <p>Your systems connected, so data moves between them without anyone retyping it.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">04</div>
          <div>
            <h5>Automation</h5>
            <p>Work that runs on its own when something happens, the same way every time.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  {meta_light("Aseva · Who we are", 3)}
</section>

<!-- 04 HOW WE BUILD -->
<section data-label="04 How we build" class="why">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">How we build</p>
    <h2 class="title">Every app started as<br/>a <em>written problem</em>.</h2>
    <div class="pillars">
      <div class="pillar">
        <div class="num">01</div>
        <div>
          <h4>A written problem</h4>
          <p>Each one began as a plain description of the problem: what was slow, what kept going wrong, and what better would look like.</p>
        </div>
      </div>
      <div class="pillar">
        <div class="num">02</div>
        <div>
          <h4>Built with AI coding tools</h4>
          <p>AI wrote the code from that description, following our own written rules for how apps get built, secured, and hosted.</p>
        </div>
      </div>
      <div class="pillar">
        <div class="num">03</div>
        <div>
          <h4>Hosted on our own platform</h4>
          <p>Every app runs on the same Aseva platform, with sign in and access control handled the same way every time.</p>
        </div>
      </div>
      <div class="pillar">
        <div class="num">04</div>
        <div>
          <h4>Used every day</h4>
          <p>These are not mockups built for this meeting. Our own teams open them every day to do their jobs.</p>
        </div>
      </div>
    </div>
  </div>
  {meta_light("Aseva · How we build", 4)}
</section>
{app_slides}
<!-- WHAT WE LEARNED -->
<section data-label="{S_LEARNED:02d} What we learned" class="diff">
  {WAVE_SOFT}
  <div class="frame">
    <p class="eyebrow">What we learned</p>
    <h2 class="title">Not every process needs<br/>AI <em>running inside it</em>.</h2>
    <p class="lede">Bill Buddy started as an AI approach. It was not accurate to the penny, so we used AI to build ordinary software instead.</p>
    <div class="three">
      <div class="card">
        <h4>What we tried first</h4>
        <p>An AI approach that read the carrier bills and reconciled them. Close was not good enough, and every run cost money.</p>
      </div>
      <div class="card">
        <h4>What we built instead</h4>
        <p>AI coding tools wrote a parser for each carrier's bill, with rules that find every charge and circuit.</p>
      </div>
      <div class="card">
        <h4>What that gets you</h4>
        <p>Ordinary software with no AI inside. It does the same thing every time and costs nothing per run.</p>
      </div>
    </div>
  </div>
  {meta_dark("Aseva · What we learned", S_LEARNED)}
</section>

<!-- YOUR TURN -->
<section data-label="{S_TURN:02d} Your turn" class="section-divider">
  {WAVE_SOFT}
  <div class="frame">
    <div class="kicker">Discussion</div>
    <h2>Your turn.</h2>
    <div class="asks">
      <div class="ask"><div class="n">1</div><p>Where does your team lose the most time?</p></div>
      <div class="ask"><div class="n">2</div><p>What do you redo by hand?</p></div>
      <div class="ask"><div class="n">3</div><p>What do you look up more than once a week?</p></div>
    </div>
  </div>
  {meta_dark("Aseva · Your turn", S_TURN)}
</section>

<!-- WHAT WE BUILD FIRST -->
<section data-label="{S_FIRST:02d} What we build first" class="whyus">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">What we build first</p>
    <div class="split">
      <div class="left">
        <div class="rule-cyan"></div>
        <h2>What do we build first, and <em>on what system</em>?</h2>
        <p>Something like ANN on your own data is one option. Either way, the first decision is which system it starts on.</p>
        <p>This is an open question. We want your read before anything gets scoped.</p>
      </div>
      <div class="right reasons">
        <div class="reason">
          <div class="idx">01</div>
          <div>
            <h5>The Visibility ERP sandbox</h5>
            <p>Start where the business process already lives, without touching production.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">02</div>
          <div>
            <h5>Salesforce</h5>
            <p>Start on the customer and sales side, with the data your sales team works from every day.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">03</div>
          <div>
            <h5>Or something you named today</h5>
            <p>If the last twenty minutes surfaced something better, it goes on the list too.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  {meta_light("Aseva · What we build first", S_FIRST)}
</section>

<!-- CLOSE -->
<section data-label="{S_CLOSE:02d} Close" class="cover">
  {WAVE_BG.replace('class="wave-bg"', 'class="wave-bg" style="opacity:0.4;"')}
  <div class="frame">
    <div>
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--secondary);margin-bottom:44px;">Prove · Build · Grow</div>
      <h1 class="title" style="color:#ffffff;font-size:96px;line-height:1.03;max-width:1520px;">Let's agree on the <span style="color:var(--secondary);">first build</span>.</h1>
      <div class="steps">
        <div><h4>Prove</h4><p>A working proof of concept within an agreed scope, with acceptance defined up front.</p></div>
        <div><h4>Build</h4><p>Development, testing, rollout, and training, with the handover agreed before we start.</p></div>
        <div><h4>Grow</h4><p>Ongoing support and new features as your team puts it to work.</p></div>
      </div>
      <div style="display:inline-flex;align-items:center;gap:20px;margin-top:64px;padding:24px 40px;border-radius:999px;background:var(--secondary);">
        <span style="font-family:var(--font-body);font-weight:600;font-size:24px;color:#ffffff;letter-spacing:0.04em;">Next step: agree on the first build target and book a scoping call</span>
        <span style="font-family:var(--font-heading);font-size:26px;color:#ffffff;">→</span>
      </div>
    </div>
  </div>
  <div class="footer-line">aseva.com · (800) 456-5800</div>
</section>

</deck-stage>
'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Aseva / BEGA · AI Demos</title>
<meta name="pluribus-source" content="Output/Drafts/BEGA - AI Demos Deck Brief - 2026-09-28.md" />
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

out = root / "prospect-bega-ai-demos-deck.html"
out.write_text(html)
print(f"wrote {out} ({len(html):,} bytes)")

EXPECTED_SLIDES = S_CLOSE
assert "data:image/png;base64" in html
assert "customElements.define" in html
assert 'src="assets/' not in html
assert 'src="deck-stage.js"' not in html
assert BODY.count("<section data-label") == EXPECTED_SLIDES, "slide count mismatch"

# Dash scan runs against AUTHORED copy only. The inlined deck-stage.js and the
# template CSS carry em dashes in their own code comments.
authored = BODY.replace(LOGO, "") + EXTRA_CSS.replace(LOGO, "")
assert "—" not in authored, "em dash in authored copy"
assert "–" not in authored, "en dash in authored copy"
stripped = BODY.replace(LOGO, "").replace("var(--", "").replace("<!--", "").replace("-->", "")
assert "--" not in stripped, "double hyphen in slide copy"

# Hard rules from the brief.
lower = BODY.lower()
for banned in ("infor ", "infor<", "cato", "teams voice", "landspeed", "retainer", "private ai"):
    assert banned not in lower, f"banned term in slide copy: {banned}"
if not SHOW_BILL_BUDDY_NUMBERS:
    assert "$" not in BODY, "dollar amount on a slide"

print("checks passed:", BODY.count("<section data-label"), "slides")
