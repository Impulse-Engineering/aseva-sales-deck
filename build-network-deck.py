#!/usr/bin/env python3
"""Assemble the standalone 'We built the network' Aseva deck.

Reuses the template's CSS framework verbatim, inlines deck-stage.js, and
base64-encodes the three logos used so the file is a single self-contained
HTML the Worker can serve as-is.
"""
import base64
import pathlib
import re

root = pathlib.Path(__file__).parent
tpl = (root / "template/template.html").read_text()

# 1. Extract the exact <style> block from the template (all archetypes).
style = tpl[tpl.index("<style>"): tpl.index("</style>") + len("</style>")]

# 2. deck-stage.js inlined.
deckjs = (root / "template/deck-stage.js").read_text()

# 3. Base64 the assets we reference.
def b64(rel, mime):
    data = base64.b64encode((root / rel).read_bytes()).decode()
    return f"data:{mime};base64,{data}"

LOGO = b64("template/assets/aseva-horizontal.png", "image/png")
CATO = b64("template/assets/cato-networks.png", "image/png")
ESEN = b64("template/assets/esentire.jpg", "image/jpeg")

# Reusable SVG waveform blocks pulled from the template.
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

BODY = f'''
<deck-stage width="1920" height="1080">

<!-- ================= 01 COVER ================= -->
<section data-label="01 Cover" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <img src="{LOGO}" alt="Aseva" style="height:150px;width:auto;margin-bottom:56px;display:block;filter:brightness(0) invert(1);" />
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.32em;text-transform:uppercase;color:rgba(255,255,255,0.55);margin-bottom:40px;">The carrier that answers the phone</div>
      <p class="kicker" style="font-size:80px;line-height:1.08;max-width:1320px;">We run our own network.<br/>Call us, and you get the <em>engineer who built&nbsp;it</em>.</p>
    </div>
  </div>
  <div class="footer-line">aseva.com · (800) 456-5800 · Since 1995</div>
</section>

<!-- ================= 02 THE REFRAME ================= -->
<section data-label="02 The reframe" class="section-divider">
  <div class="frame">
    <div class="kicker">What we are</div>
    <h2 style="font-size:86px;line-height:1.02;max-width:1550px;">We are not a help desk<br/>that got&nbsp;big.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:40px;color:rgba(255,255,255,0.72);margin-top:36px;max-width:1320px;line-height:1.35;">We are a carrier that decided to answer the phone. We own the fiber, the datacenters, and the voice platform. The difference you feel is simple: the person who fixes your network is the person who built&nbsp;it.</div>
  </div>
  <div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>Aseva</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>02</span></div>
</section>

<!-- ================= 03 WE BUILT THE NETWORK ================= -->
<section data-label="03 We built the network" class="who">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Where it all comes from</p>
    <h2 class="title">Most providers resell a network.<br/>We built&nbsp;ours.</h2>
    <div class="grid">
      <div>
        <p class="pitch">
          Three decades ago we laid fiber on the central coast and put carrier equipment in <span class="mark">central-office datacenters</span>. We run a hosted voice platform on our own gear and buy at the wholesale level directly from carriers.
          <br/><br/>
          That is the foundation. <strong>Every engineer we put in front of you runs a live carrier network every day.</strong> The expertise is not borrowed from a vendor. It is ours.
        </p>
      </div>
      <div class="stats">
        <div class="stat">
          <div class="n">1995</div>
          <div class="lbl">Building and operating our own network on the central coast</div>
        </div>
        <div class="stat">
          <div class="n">3,000<span class="unit">+</span></div>
          <div class="lbl">Companies served across three decades of operating history</div>
        </div>
        <div class="stat">
          <div class="n">25<span class="unit">yr</span></div>
          <div class="lbl">Average tenure across our principal engineers and leadership</div>
        </div>
        <div class="stat">
          <div class="n">1</div>
          <div class="lbl">Team accountable for cybersecurity, voice, and connectivity, on one bill</div>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva</span><span class="rule"></span><span>03</span></div>
</section>

<!-- ================= 04 THE DIFFERENTIATOR ================= -->
<section data-label="04 Differentiator" class="diff">
  {WAVE_SOFT}
  <div class="frame">
    <p class="eyebrow">Why it matters to you</p>
    <h2 class="title">The engineer who designs your rollout<br/>runs a live network every&nbsp;day.</h2>
    <p class="lede">Running our own network created engineers who understand circuits, failover, identity, and security at depth. That expertise is <em>portable</em>. It shows up in every connectivity, voice, and cybersecurity engagement we deliver, whichever product sits underneath.</p>
    <div class="three">
      <div class="card">
        <h4>Carrier roots</h4>
        <p>We own and operate a fiber network, carrier equipment in central-office datacenters, and a hosted voice platform on our own gear.</p>
      </div>
      <div class="card">
        <h4>Engineers on the phone</h4>
        <p>The same engineers who run our network are the ones you reach. Every carrier has engineers. Not every carrier puts them on the phone with you.</p>
      </div>
      <div class="card">
        <h4>One bill, one team</h4>
        <p>Consolidated billing across every location and service. A dedicated account manager and support team, with the engineers staffed behind them.</p>
      </div>
    </div>
  </div>
  <div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>Aseva</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>04</span></div>
</section>

<!-- ================= 05 THE 2AM TEST ================= -->
<section data-label="05 The 2am test" class="whyus">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">The question that actually matters</p>
    <div class="split">
      <div class="left">
        <div class="rule-cyan"></div>
        <h2>When it breaks at <em>2am</em>, who actually picks&nbsp;up?</h2>
        <p>With most providers it is a ticket queue and a stranger who has never seen your network. You explain it from scratch, every single time.</p>
        <p>With us it is a live human, a dedicated account manager who knows your environment, and the engineers who built the thing. Our customers stop calling us a vendor. Most cannot tell you the day it happened.</p>
      </div>
      <div class="right reasons">
        <div class="reason">
          <div class="idx">01</div>
          <div>
            <h5>Live humans, around the clock</h5>
            <p>People answer the phone. No IVR tree, no revolving door of tier-one reps reading from a script they have never tested.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">02</div>
          <div>
            <h5>A dedicated account manager</h5>
            <p>One person who knows your environment and your history, with the engineers reachable directly behind them.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">03</div>
          <div>
            <h5>Engineers, not a hand-off</h5>
            <p>The people who designed your network are the people who fix it. Nothing bounces between a vendor and a reseller while the problem keeps happening.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">04</div>
          <div>
            <h5>Wholesale escalation</h5>
            <p>When we escalate to an underlying carrier we go in at the wholesale level, which gets prioritized attention. One call to us and we work the rest.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva</span><span class="rule"></span><span>05</span></div>
</section>

<!-- ================= 06 THE PROOF (divider) ================= -->
<section data-label="06 The proof" class="section-divider">
  <div class="frame">
    <div class="kicker">The proof</div>
    <h2 style="font-size:104px;line-height:1;">Three proofs.<br/>One&nbsp;network.</h2>
    <div style="font-family:var(--font-heading);font-weight:300;font-size:40px;color:rgba(255,255,255,0.72);margin-top:36px;max-width:1340px;line-height:1.35;">Cybersecurity, voice, and connectivity are not three businesses we bolted together. They are three things one carrier-grade network lets us do better than a reseller ever&nbsp;could.</div>
  </div>
  <div class="page-meta" style="color:rgba(255,255,255,0.55);"><span>Aseva · The proof</span><span class="rule" style="background:rgba(255,255,255,0.25);"></span><span>06</span></div>
</section>

<!-- ================= 07 CYBERSECURITY ================= -->
<section data-label="07 Cybersecurity" class="cyber">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Proof one · Cybersecurity</p>
    <h2 class="title">A large part of security<br/>lives on the&nbsp;network.</h2>
    <p class="lede" style="font-size:28px;color:var(--grey);margin-top:28px;max-width:1520px;">We cover identity, email, endpoint, network, and monitoring. The network layer is where modern security actually lives, and it is exactly where running our own carrier network creates an advantage a reseller cannot copy.</p>
    <div class="stack-row">
      <div class="layer">
        <div class="cat">Identity</div>
        <h4>Integration expertise</h4>
        <p>Deep working knowledge across multiple Identity providers is load-bearing in every modern security deployment.</p>
      </div>
      <div class="layer">
        <div class="cat">Email</div>
        <h4>Email security</h4>
        <p>Cloud email security from partners like Proofpoint, a must-have in today's world of phishing and social engineering.</p>
      </div>
      <div class="layer flag">
        <div class="cat">Endpoint · Monitoring</div>
        <h4>MDR, SOC, SIEM</h4>
        <p>Flagship depth through our premier MDR partnership. A 24/7 SOC with real remediation, not just alerts.</p>
      </div>
      <div class="layer flag">
        <div class="cat">Network</div>
        <h4>SASE, firewalls, ZTNA</h4>
        <p>Flagship depth through our Cato partnership. Where carrier engineering and cybersecurity meet, and where we do our best work.</p>
      </div>
      <div class="layer">
        <div class="cat">Assessment</div>
        <h4>Pen-testing</h4>
        <p>Multiple penetration-testing options brought by the Aseva team to confirm the security in place is actually working.</p>
      </div>
    </div>
    <div class="legend">
      <div><span class="dot flag"></span>Flagship practice · Aseva as MSP or premier reseller</div>
      <div><span class="dot reg"></span>Partner resale and integration expertise</div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva · Cybersecurity</span><span class="rule"></span><span>07</span></div>
</section>

<!-- ================= 08 SASE WITH CATO ================= -->
<section data-label="08 SASE Cato" class="partner">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Proof one · SASE</p>
    <div class="grid">
      <div class="logo-panel cato">
        <div style="font-family:var(--font-body);font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:rgba(255,255,255,0.8);font-weight:600;">Premier partnership</div>
        <div class="logo-wrap">
          <img src="{CATO}" alt="Cato Networks" />
        </div>
        <div class="partner-meta">
          <div>
            <div class="label">Our role</div>
            <div class="val">Certified MSP, full implementation and management</div>
          </div>
          <div>
            <div class="label">Coverage</div>
            <div class="val">90+ global POPs, one platform, single-pass inspection</div>
          </div>
        </div>
      </div>
      <div class="right">
        <div class="partner-badge"><span class="dot"></span>Flagship SASE partner</div>
        <h2>The SASE and the circuit, designed by <em>one team</em>.</h2>
        <p class="intro">Cato is a pure-play SASE platform built on one cloud with a single-pass inspection engine. Because we are also the carrier, the overlay and the circuit underneath it are never someone else's problem.</p>
        <div class="points">
          <div class="point">
            <div class="bar"></div>
            <div>
              <h5>One platform, one pane of glass</h5>
              <p>Firewall, SD-WAN, ZTNA, CASB, DLP, IPS, and threat prevention on a single cohesive stack. Not a collection of acquisitions stitched together.</p>
            </div>
          </div>
          <div class="point">
            <div class="bar"></div>
            <div>
              <h5>Global POP footprint</h5>
              <p>A remote user in London connects to one of 90 global Cato POPs at the same speeds as HQ in Chicago. No more VPN hauling and hair-pinning.</p>
            </div>
          </div>
          <div class="point">
            <div class="bar"></div>
            <div>
              <h5>We design, implement, and manage</h5>
              <p>Certified Cato engineers on staff run discovery, scope, and cutover, then stay on as the managed service. Circuit and socket work happens inside one team.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva · SASE</span><span class="rule"></span><span>08</span></div>
</section>

<!-- ================= 09 MDR WITH ESENTIRE ================= -->
<section data-label="09 MDR eSentire" class="partner">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Proof one · MDR &amp; SOC</p>
    <div class="grid">
      <div class="logo-panel esentire">
        <div style="font-family:var(--font-body);font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--grey);font-weight:600;">Premier partnership</div>
        <div class="logo-wrap">
          <img src="{ESEN}" alt="eSentire" />
        </div>
        <div class="partner-meta">
          <div>
            <div class="label">Our role</div>
            <div class="val">Scoping, sales expertise, and consolidated billing</div>
          </div>
          <div>
            <div class="label">Recognition</div>
            <div class="val">Gartner Strong Performer, top-five MDR globally</div>
          </div>
        </div>
      </div>
      <div class="right">
        <div class="partner-badge"><span class="dot"></span>Flagship MDR &amp; SOC partner</div>
        <h2>A 24/7 SOC your team could never afford to build <em>in-house</em>.</h2>
        <p class="intro">eSentire runs an outsourced SOC that ingests multi-signal telemetry across endpoint, network, logs, cloud, identity, and vulnerability. Human threat hunters investigate and remediate, not just alert.</p>
        <div class="points">
          <div class="point">
            <div class="bar"></div>
            <div>
              <h5>Real remediation</h5>
              <p>They cut off a compromised user and stop the threat where competitors notify you and hand the work back. That is the difference between detection and response.</p>
            </div>
          </div>
          <div class="point">
            <div class="bar"></div>
            <div>
              <h5>Works with your existing stack</h5>
              <p>Integrates with CrowdStrike, Microsoft Defender, Sumo Logic, Tanium, Tenable, and more. No forklift upgrade, no ripping out what you already trust.</p>
            </div>
          </div>
          <div class="point">
            <div class="bar"></div>
            <div>
              <h5>CrowdStrike, better</h5>
              <p>One of the largest CrowdStrike resellers. We package the agent with eSentire's MDR on top and typically beat Falcon Complete on price and service.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva · MDR</span><span class="rule"></span><span>09</span></div>
</section>

<!-- ================= 10 VOICE & CONNECTIVITY ================= -->
<section data-label="10 Voice and connectivity" class="whyus">
  {CORNER}
  <div class="frame">
    <p class="eyebrow">Proof two &amp; three · Voice and connectivity</p>
    <div class="split">
      <div class="left">
        <div class="rule-cyan"></div>
        <h2>The same network carries your <em>calls</em> and your <em>connectivity</em>.</h2>
        <p>Call quality is a network problem. Redundancy is a network problem. When one team owns the fiber, the failover design, and the phone platform, there is no finger-pointing on a Tuesday when something sounds wrong.</p>
        <p>We run our own hosted voice platform and deliver Microsoft Teams Voice and contact center. We design dedicated fiber, diverse-carrier redundancy, and colocation. One bill, one team, every location.</p>
      </div>
      <div class="right reasons">
        <div class="reason">
          <div class="idx">01</div>
          <div>
            <h5>Voice that fits how you work</h5>
            <p>ClearStar hosted voice, Microsoft Teams Voice, and contact center. We pick the one that fits your business, not the one that lands on our platform.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">02</div>
          <div>
            <h5>Connectivity, engineered</h5>
            <p>Dedicated fiber with SLA, diverse-carrier redundancy that actually fails over, and colocation. Designed by the engineers who also manage it.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">03</div>
          <div>
            <h5>Proactive monitoring on every circuit</h5>
            <p>One dashboard across every carrier. Our engineers get paged before most customers notice anything is wrong.</p>
          </div>
        </div>
        <div class="reason">
          <div class="idx">04</div>
          <div>
            <h5>One bill, one accountable team</h5>
            <p>Consolidated billing across every location and every service. A single number to call, the same team every time.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="page-meta"><span>Aseva · Voice &amp; Connectivity</span><span class="rule"></span><span>10</span></div>
</section>

<!-- ================= 11 CLOSE ================= -->
<section data-label="11 Close" class="cover">
  {WAVE_BG}
  <div class="frame">
    <div>
      <div style="font-family:var(--font-body);font-weight:600;font-size:24px;letter-spacing:0.24em;text-transform:uppercase;color:var(--secondary);margin-bottom:48px;">Connect · Discover · Solve · Guide</div>
      <h1 class="title" style="color:#ffffff;font-size:104px;line-height:1.03;max-width:1500px;">Bring the engineer.<br/>Keep the <span style="color:var(--secondary);">map</span>.</h1>
      <p style="font-family:var(--font-heading);font-weight:300;font-size:42px;color:rgba(255,255,255,0.78);margin-top:40px;max-width:1280px;line-height:1.3;">Forty-five minutes with one of our network engineers. We map what you run today and give you a straight read on where you are solid and where you are aging out. No pitch. You keep the map either way.</p>
      <div style="display:inline-flex;align-items:center;gap:20px;margin-top:64px;padding:24px 40px;border-radius:999px;background:var(--secondary);">
        <span style="font-family:var(--font-body);font-weight:600;font-size:24px;color:#ffffff;letter-spacing:0.04em;">Start the conversation</span>
        <span style="font-family:var(--font-heading);font-size:26px;color:#ffffff;">&#8594;</span>
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
<title>Aseva — We Built the Network</title>
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

out = root / "aseva-network-deck.html"
out.write_text(html)
print(f"wrote {out} ({len(html):,} bytes)")
# sanity checks
assert "data:image/png;base64" in html
assert "customElements.define" in html
assert 'src="assets/' not in html
assert 'src="deck-stage.js"' not in html
print("checks passed:", html.count("<section"), "sections")
