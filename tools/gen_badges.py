import math,sys
OUT=sys.argv[1]
MONO="'Fira Code','JetBrains Mono',Consolas,'DejaVu Sans Mono',monospace"
SANS="'Segoe UI','Inter',Helvetica,Arial,sans-serif"
T={"gold":("#ffe27a","#f5a300","#7a4a00"),"silver":("#f1f5f9","#9fb0c3","#3b4b5f"),"bronze":("#ffc08a","#c26a2b","#5a2a08"),
   "cyan":("#9af0ff","#1fb6ff","#05425e"),"violet":("#d8c8ff","#8b5cf6","#2c1566"),"pink":("#ffc2ec","#ec4899","#5a0f3a"),"green":("#b9f8cf","#22c55e","#0b4a22")}
B=[("🥇","1ST PRIZE","PICT InC 2026","International","gold"),("🥇","1ST PLACE","iMocha Hackathon","2026","gold"),("🏛","TOP 12","Aavishkar 2025","Govt. of Maharashtra","violet"),
   ("🥇","1ST PLACE","TECHTHESIS","Bharatiyugam 2025","gold"),("🥈","2ND PLACE","IETE NLPC","2025 · 61 teams","silver"),("🥉","3RD PLACE","ASPIRE 2K25","50+ teams","bronze"),
   ("📄","PUBLISHED","IEEE SILCON","2024 · LoRA/QLoRA","cyan"),("📄","PUBLISHED","IJRES 2025","ADAS on Raspberry Pi","cyan"),("🥇","1ST PLACE","Pulzion'24","PICT ACM","gold"),
   ("🥉","3RD PLACE","Navdhara","2024","bronze"),("🤗","1,200+","HF Downloads","Ram20307","pink"),("🏦","INTERN","Barclays","Jun–Aug 2026","green")]
W,H=1200,500
s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img"><defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070b14"/><stop offset=".55" stop-color="#0c1830"/><stop offset="1" stop-color="#130c2b"/></linearGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#36d1ff"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#ff6bd6"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".75"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="hx"><path d="M0 -50 L43 -25 L43 25 L0 50 L-43 25 L-43 -25 Z"/></clipPath>'''
for k,(a,b,c) in T.items():
    s+=f'<linearGradient id="g-{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{a}"/><stop offset=".55" stop-color="{b}"/><stop offset="1" stop-color="{c}"/></linearGradient>'
s+=f'''</defs><rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
<text x="40" y="50" font-family="{SANS}" font-size="24" font-weight="800" fill="#fff" letter-spacing="2">ACHIEVEMENTS UNLOCKED</text>
<text x="40" y="74" font-family="{MONO}" font-size="13" fill="#8aa0b8">12 / 12 &#183; competitions, publications, industry</text>'''
for i,(ic,top,name,sub,tier) in enumerate(B):
    r,c=divmod(i,6); cx=100+c*200; cy=170+r*180; d=3+(i%4)*.4
    s+=f'<g transform="translate({cx} {cy})"><animateTransform attributeName="transform" additive="sum" type="translate" values="0 0;0 -6;0 0" dur="{d}s" begin="{i*.3}s" repeatCount="indefinite"/>'
    s+=f'<path d="M0 -54 L47 -27 L47 27 L0 54 L-47 27 L-47 -27 Z" fill="{T[tier][1]}" opacity=".35" filter="url(#glow)"/>'
    s+=f'<path d="M0 -50 L43 -25 L43 25 L0 50 L-43 25 L-43 -25 Z" fill="url(#g-{tier})" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>'
    s+=f'<path d="M0 -40 L34 -20 L34 20 L0 40 L-34 20 L-34 -20 Z" fill="none" stroke="#000" stroke-opacity=".25"/>'
    s+=f'<g clip-path="url(#hx)"><rect x="-60" y="-60" width="30" height="120" fill="url(#sh)" transform="skewX(-20)"><animate attributeName="x" values="-90;90;90" keyTimes="0;.35;1" dur="4s" begin="{i*.45}s" repeatCount="indefinite"/></rect></g>'
    s+=f'<text y="9" text-anchor="middle" font-size="30">{ic}</text></g>'
    s+=f'<text x="{cx}" y="{cy+78}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{T[tier][1]}" letter-spacing="1.5">{top}</text>'
    s+=f'<text x="{cx}" y="{cy+96}" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="700" fill="#e6eefc">{name}</text>'
    s+=f'<text x="{cx}" y="{cy+112}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#6b7f95">{sub}</text>'
s+=f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="17" fill="none" stroke="url(#edge)" stroke-width="1.5"/></svg>'
open(OUT,"w").write(s)
