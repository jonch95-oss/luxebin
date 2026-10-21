# Builds direction-b.html from the template + product data.
import json,re
d=json.load(open('products.json'))
bleed=('ATU-RARE','ATU-TRU','LANE-009','ATU-JANE','ATU-KYLIE-131')
def money(x): return f"${x:.0f}" if x==int(x) else f"${x:.2f}"
def card(p):
  s,b,n,pr,c=p; pct=round((c-pr)/c*100); cls='card bleed' if s.startswith(bleed) else 'card'
  return f'''<a class="{cls}" href="#"><div class="ph"><img src="../images/{s}-1.jpg" alt="{b} {n}"><span class="tag">Save {pct}%</span></div>
<p class="brand">{b}</p><p class="name">{n}</p>
<p class="price"><span class="now">{money(pr)}</span><s><span class="sr">Retail </span>{money(c)}</s></p></a>'''
t=open('_direction-b.tpl.html').read()
t=t.replace('{{BEST}}',''.join(map(card,d['best']))).replace('{{NEW}}',''.join(map(card,d['new']))).replace('{{BRANDS}}',''.join(f'<a href="#">{b}</a>' for b in d['brands']))
open('direction-b.html','w').write(t)
