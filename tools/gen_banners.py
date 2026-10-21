import math, random, os, sys
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
MONO = "'Fira Code','JetBrains Mono','SF Mono',Consolas,'DejaVu Sans Mono',monospace"
SANS = "'Segoe UI','Inter',Helvetica,Arial,sans-serif"
CY, VI, PK, GR, AM, RD = "#36d1ff", "#a78bfa", "#ff6bd6", "#4ade80", "#fbbf24", "#ff5c5c"
random.seed(7)


def seq(t0, t1, dur, a="opacity"):
    """fade in at t0 sec, out at t1 sec, within a looping dur-sec cycle."""
    k = [0, t0 / dur, min(t0 / dur + .02, 1), t1 / dur, min(t1 / dur + .02, 1), 1]
    return (f'<animate attributeName="{a}" dur="{dur}s" repeatCount="indefinite" '
            f'values="0;0;1;1;0;0" keyTimes="{";".join(f"{x:.3f}" for x in k)}"/>')


def head(w, h, extra=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070b14"/><stop offset=".55" stop-color="#0c1830"/><stop offset="1" stop-color="#130c2b"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glow2" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity=".05"/></pattern>
{extra}
</defs>
<rect width="{w}" height="{h}" rx="18" fill="url(#bg)"/>
<rect width="{w}" height="{h}" rx="18" fill="url(#grid)"><animateTransform attributeName="patternTransform" type="translate" from="0 0" to="40 40" dur="8s" repeatCount="indefinite"/></rect>
'''


def border(w, h):
    return (f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="17" fill="none" stroke="url(#edge)" stroke-width="1.5"/>')


EDGE = f'<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CY}"/><stop offset=".5" stop-color="{VI}"/><stop offset="1" stop-color="{PK}"/><animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0;-1 0" dur="8s" repeatCount="indefinite"/></linearGradient>'

# ───────────────────────── HERO ─────────────────────────
W, H = 1200, 320
s = head(W, H, EDGE + f'''<linearGradient id="nm" x1="0" y1="0" x2="1" y2="0" spreadMethod="reflect"><stop offset="0" stop-color="{CY}"/><stop offset=".5" stop-color="#fff"/><stop offset="1" stop-color="{VI}"/><animateTransform attributeName="gradientTransform" type="translate" from="-0.6 0" to="0.6 0" dur="5s" repeatCount="indefinite"/></linearGradient>''')
for i in range(46):
    x, y = random.randint(20, W - 20), random.randint(20, H - 20)
    r = random.choice([1, 1.4, 1.8, 2.2])
    c = random.choice([CY, VI, PK, "#fff"])
    d = random.uniform(5, 12)
    s += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity=".55"><animateTransform attributeName="transform" type="translate" '
          f'values="0 0;{random.randint(-20,20)} -{random.randint(30,80)};0 0" dur="{d:.1f}s" repeatCount="indefinite"/>'
          f'<animate attributeName="opacity" values=".15;.8;.15" dur="{d/2:.1f}s" repeatCount="indefinite"/></circle>')
s += f'''<text x="60" y="118" font-family="{SANS}" font-size="66" font-weight="800" fill="url(#nm)" filter="url(#glow)">Sarvadnya Bhatlawande</text>
<text x="62" y="156" font-family="{MONO}" font-size="19" fill="#9fb3c8"><tspan fill="{GR}">$</tspan> whoami <tspan fill="#6b7f95">&#8594;</tspan> systems engineer who measures before claiming</text>
'''
chips = [("AI RESEARCH", CY, 60, 168), ("BACKEND", VI, 262, 130), ("DISTRIBUTED SYSTEMS", PK, 412, 250)]
for i, (t, c, x, w) in enumerate(chips):
    s += (f'<g><rect x="{x}" y="186" width="{w}" height="40" rx="20" fill="{c}" fill-opacity=".10" stroke="{c}" stroke-width="1.6" filter="url(#glow)">'
          f'<animate attributeName="stroke-opacity" values="1;.35;1" dur="3s" begin="{i*.8}s" repeatCount="indefinite"/></rect>'
          f'<circle cx="{x+20}" cy="206" r="4" fill="{c}"><animate attributeName="r" values="3;6;3" dur="2s" begin="{i*.5}s" repeatCount="indefinite"/></circle>'
          f'<text x="{x+34}" y="212" font-family="{MONO}" font-size="15" font-weight="700" fill="{c}" letter-spacing="1.5">{t}</text></g>')
# typed line
s += f'''<clipPath id="tp"><rect x="60" y="246" height="30" width="0"><animate attributeName="width" values="0;640;640;0" keyTimes="0;.45;.9;1" dur="9s" repeatCount="indefinite"/></rect></clipPath>
<text x="60" y="268" font-family="{MONO}" font-size="17" fill="{AM}" clip-path="url(#tp)">100K txns &#183; p95 122ms &#183; 4.4M logs traced &#183; Z3-verified</text>
<rect x="60" y="250" width="9" height="20" fill="{AM}"><animate attributeName="x" values="60;700;700;60" keyTimes="0;.45;.9;1" dur="9s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/></rect>
'''
# orbit emblem
cx, cy = 1010, 160
s += f'<g transform="translate({cx} {cy})">'
for r, c, d, n in [(48, CY, 6, 1), (82, VI, 10, 2), (118, PK, 15, 3)]:
    s += f'<circle r="{r}" fill="none" stroke="{c}" stroke-opacity=".28" stroke-dasharray="3 6"/>'
    for k in range(n):
        a0 = k * 360 / n
        s += (f'<g><animateTransform attributeName="transform" type="rotate" from="{a0}" to="{a0+360 if r!=82 else a0-360}" dur="{d}s" repeatCount="indefinite"/>'
              f'<circle cx="{r}" r="{6 if r==48 else 7}" fill="{c}" filter="url(#glow2)"/></g>')
s += f'<circle r="18" fill="#0b1220" stroke="{CY}" stroke-width="2" filter="url(#glow)"><animate attributeName="r" values="16;21;16" dur="3s" repeatCount="indefinite"/></circle>'
s += f'<text y="5" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="{CY}">SB</text></g>'
s += border(W, H) + '</svg>'
open(f"{OUT}/hero.svg", "w").write(s)

# ───────────────────── DISTRIBUTED SYSTEMS ─────────────────────
W, H = 1200, 380
s = head(W, H, EDGE)
s += f'<text x="40" y="52" font-family="{SANS}" font-size="26" font-weight="800" fill="{PK}" letter-spacing="2">DISTRIBUTED SYSTEMS</text>'
s += f'<text x="40" y="78" font-family="{MONO}" font-size="14" fill="#8aa0b8">event-driven &#183; fault-tolerant &#183; observable</text>'
# ring cluster
ccx, ccy, rx, ry = 270, 198, 170, 84
n = 6
pts = [(ccx + rx * math.cos(2 * math.pi * i / n - math.pi / 2), ccy + ry * math.sin(2 * math.pi * i / n - math.pi / 2)) for i in range(n)]
paths = []
for i in range(n):
    for j in (i + 1, i + 2):
        a, b = pts[i], pts[j % n]
        paths.append((i, j % n))
        s += f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="{CY}" stroke-opacity=".18"/>'
# packets
cols = [CY, VI, PK, GR, AM]
for k, (i, j) in enumerate(paths * 2):
    a, b = pts[i], pts[j]
    if k % 2:
        a, b = b, a
    c = cols[k % 5]
    s += (f'<circle r="3.6" fill="{c}" filter="url(#glow)"><animateMotion dur="{2.2+ (k%5)*.45:.2f}s" begin="{(k*.37)%3:.2f}s" repeatCount="indefinite" '
          f'path="M{a[0]:.0f} {a[1]:.0f} L{b[0]:.0f} {b[1]:.0f}"/></circle>')
for i, (x, y) in enumerate(pts):
    fail = (i == 4)
    s += f'<g transform="translate({x:.0f} {y:.0f})">'
    s += f'<circle r="20" fill="#0b1220" stroke="{CY}" stroke-width="2" filter="url(#glow)">'
    if fail:
        s += f'<animate attributeName="stroke" dur="12s" repeatCount="indefinite" values="{CY};{CY};{RD};{RD};{CY};{CY}" keyTimes="0;.3;.31;.55;.56;1" calcMode="discrete"/>'
    s += '</circle>'
    s += f'<text y="5" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="#cfe8ff">b{i+1}</text>'
    s += f'<circle r="20" fill="none" stroke="{VI}" stroke-width="1.5"><animate attributeName="r" values="20;34;34" dur="3s" begin="{i*.5}s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".7;0;0" dur="3s" begin="{i*.5}s" repeatCount="indefinite"/></circle>'
    s += '</g>'
# failure banner
fx, fy = pts[4]
s += f'<g>{seq(3.7, 6.6, 12)}<text x="{ccx}" y="{ccy+4}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{RD}">b5 down &#8594; rebalance</text></g>'
s += f'<g>{seq(7, 9.6, 12)}<text x="{ccx}" y="{ccy+4}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{GR}">consumer lag = 0 &#10003;</text></g>'
# kafka lanes
lx, lw = 560, 600
s += f'<text x="{lx}" y="52" font-family="{MONO}" font-size="15" font-weight="700" fill="{CY}">KAFKA &#183; 9 partitions &#183; 6 consumer groups</text>'
gcol = [CY, VI, PK, GR, AM, "#fb923c"]
for p in range(9):
    y = 78 + p * 27
    s += f'<rect x="{lx}" y="{y}" width="{lw}" height="20" rx="6" fill="#ffffff" fill-opacity=".04" stroke="#ffffff" stroke-opacity=".08"/>'
    s += f'<text x="{lx+8}" y="{y+14}" font-family="{MONO}" font-size="11" fill="#5d7189">p{p}</text>'
    for m in range(5):
        c = gcol[(p + m) % 6]
        d = 3.2 + (p % 4) * .7
        s += (f'<rect y="{y+4}" x="{lx+34}" width="22" height="12" rx="3" fill="{c}" filter="url(#glow)">'
              f'<animate attributeName="x" from="{lx+34}" to="{lx+lw-30}" dur="{d:.1f}s" begin="{m*d/5 + p*.13:.2f}s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="{d:.1f}s" begin="{m*d/5 + p*.13:.2f}s" repeatCount="indefinite"/></rect>')
# metric bars
my = 335
for i, (lab, val, c) in enumerate([("100K txns", .95, CY), ("p95 122ms", .62, VI), ("lag 0", .03, GR)]):
    x = 40 + i * 185
    s += f'<text x="{x}" y="{my}" font-family="{MONO}" font-size="13" fill="{c}" font-weight="700">{lab}</text>'
    s += f'<rect x="{x}" y="{my+8}" width="160" height="6" rx="3" fill="#ffffff" fill-opacity=".08"/>'
    s += f'<rect x="{x}" y="{my+8}" height="6" rx="3" fill="{c}" filter="url(#glow)"><animate attributeName="width" values="0;{160*val:.0f};{160*val:.0f};0" keyTimes="0;.25;.9;1" dur="7s" repeatCount="indefinite"/></rect>'
s += border(W, H) + '</svg>'
open(f"{OUT}/distributed.svg", "w").write(s)

# ───────────────────── AI RESEARCH ─────────────────────
W, H = 1200, 380
s = head(W, H, EDGE)
s += f'<text x="40" y="52" font-family="{SANS}" font-size="26" font-weight="800" fill="{CY}" letter-spacing="2">AI RESEARCH</text>'
s += f'<text x="40" y="78" font-family="{MONO}" font-size="14" fill="#8aa0b8">baselines before claims &#183; the LLM proposes, Z3 proves</text>'
layers = [3, 5, 5, 3]
lxs = [90, 230, 370, 510]
nodes = []
for li, cnt in enumerate(layers):
    col = []
    for k in range(cnt):
        y = 215 + (k - (cnt - 1) / 2) * 52
        col.append((lxs[li], y))
    nodes.append(col)
edges = []
for li in range(len(layers) - 1):
    for a in nodes[li]:
        for b in nodes[li + 1]:
            edges.append((a, b))
            s += f'<line x1="{a[0]}" y1="{a[1]:.0f}" x2="{b[0]}" y2="{b[1]:.0f}" stroke="{VI}" stroke-opacity=".16"/>'
random.seed(3)
for k in range(26):
    a, b = random.choice(edges)
    c = random.choice([CY, PK, VI])
    s += (f'<circle r="3" fill="{c}" filter="url(#glow)"><animateMotion dur="{random.uniform(1.6,3.2):.2f}s" begin="{random.uniform(0,4):.2f}s" repeatCount="indefinite" '
          f'path="M{a[0]} {a[1]:.0f} L{b[0]} {b[1]:.0f}"/></circle>')
for li, col in enumerate(nodes):
    for k, (x, y) in enumerate(col):
        c = [CY, VI, VI, PK][li]
        s += (f'<circle cx="{x}" cy="{y:.0f}" r="11" fill="#0b1220" stroke="{c}" stroke-width="2" filter="url(#glow)">'
              f'<animate attributeName="fill" values="#0b1220;{c};#0b1220" dur="2.4s" begin="{li*.6 + k*.17:.2f}s" repeatCount="indefinite"/></circle>')
for x, t in zip(lxs, ["input", "reason", "reason", "answer"]):
    s += f'<text x="{x}" y="338" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#5d7189">{t}</text>'
# reasoning chain
rx0 = 680
s += f'<text x="{rx0}" y="52" font-family="{MONO}" font-size="15" font-weight="700" fill="{PK}">trace &#183; verify before you trust</text>'
lines = [
    (f"Q: 18 &#215; 7 + 4 = ?", "#cfe8ff", 1.0),
    ("&#8627; step 1  18 &#215; 7 = 126", VI, 2.4),
    ("&#8627; step 2  126 + 4 = 130", VI, 3.8),
    ("&#8627; candidate: 130", AM, 5.2),
    ("z3.prove(candidate == 18*7+4)", CY, 6.6),
    ("&#10003; proved equivalent &#8594; accept", GR, 8.0),
]
for i, (t, c, at) in enumerate(lines):
    y = 112 + i * 44
    s += (f'<g>{seq(at, 11.4, 12.5)}<rect x="{rx0-12}" y="{y-24}" width="480" height="34" rx="8" fill="{c}" fill-opacity=".08" stroke="{c}" stroke-opacity=".35"/>'
          f'<text x="{rx0}" y="{y-2}" font-family="{MONO}" font-size="16" fill="{c}">{t}</text></g>')
s += f'<text x="{rx0}" y="{H-30}" font-family="{MONO}" font-size="13" fill="#5d7189">SLM reasoning &#183; Z3 verifier &#183; GraphRAG &#183; LoRA</text>'
s += border(W, H) + '</svg>'
open(f"{OUT}/research.svg", "w").write(s)

# ───────────────────── BACKEND ─────────────────────
W, H = 1200, 220
s = head(W, H, EDGE)
s += f'<text x="40" y="52" font-family="{SANS}" font-size="26" font-weight="800" fill="{VI}" letter-spacing="2">BACKEND</text>'
s += f'<text x="40" y="78" font-family="{MONO}" font-size="14" fill="#8aa0b8">Java 21 &#183; Spring Boot 3 &#183; WebFlux &#183; Kafka &#183; Cassandra &#183; Oracle &#183; Redis</text>'
stages = [("gateway", CY), ("fraud", VI), ("validate", PK), ("AML", AM), ("settle", GR), ("audit", "#fb923c")]
bw, gap, x0, y0 = 150, 40, 40, 112
for i, (t, c) in enumerate(stages):
    x = x0 + i * (bw + gap)
    s += (f'<rect x="{x}" y="{y0}" width="{bw}" height="56" rx="12" fill="{c}" fill-opacity=".1" stroke="{c}" stroke-width="1.8" filter="url(#glow)">'
          f'<animate attributeName="fill-opacity" values=".08;.4;.08" dur="6s" begin="{i}s" repeatCount="indefinite"/></rect>'
          f'<text x="{x+bw/2}" y="{y0+34}" text-anchor="middle" font-family="{MONO}" font-size="16" font-weight="700" fill="{c}">{t}</text>')
    if i < len(stages) - 1:
        s += f'<line x1="{x+bw}" y1="{y0+28}" x2="{x+bw+gap}" y2="{y0+28}" stroke="#ffffff" stroke-opacity=".25" stroke-dasharray="4 4"/>'
for k in range(5):
    s += (f'<circle r="5" fill="{AM}" filter="url(#glow2)"><animateMotion dur="6s" begin="{k*1.2}s" repeatCount="indefinite" path="M{x0} {y0+28} L{x0+6*bw+5*gap} {y0+28}"/>'
          f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.05;.95;1" dur="6s" begin="{k*1.2}s" repeatCount="indefinite"/></circle>')
s += f'<text x="40" y="{H-26}" font-family="{MONO}" font-size="13" fill="#5d7189">10 microservices &#183; ISO 20022 &#183; double-entry settlement &#183; SHA-256 audit trail</text>'
s += border(W, H) + '</svg>'
open(f"{OUT}/backend.svg", "w").write(s)
print("ok")
