from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
from fontTools.ttLib import TTFont
import xml.etree.ElementTree as ET
r=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.ids=set();self.h1=0;self.inputs=[];self.labels=set();self.feed(s)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for k in ['href','src']:
   if a.get(k):self.links.append(a[k])
  if a.get('id'):self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ['input','textarea'] and a.get('type')!='checkbox':self.inputs.append(a.get('id'))
  if tag=='label' and a.get('for'):self.labels.add(a['for'])
pages={p:Page(p.read_text()) for p in r.glob('*.html')};errors=[]
for p,s in pages.items():
 if s.h1!=1:errors.append(f'{p.name}: h1 count {s.h1}')
 for v in s.links:
  u=urlparse(v)
  if u.scheme:continue
  t=p.parent/u.path if u.path else p
  if not t.exists():errors.append(f'{p.name}: missing {v}')
  elif u.fragment and t in pages and u.fragment not in pages[t].ids:errors.append(f'{p.name}: missing fragment {v}')
 for i in s.inputs:
  if i not in s.labels:errors.append(f'{p.name}: input label {i}')
for p in (r/'assets').glob('*.svg'):ET.parse(p)
for p in (r/'assets').glob('*.woff'):TTFont(p)
print(f'{len(pages)} pages checked; all local links, anchors, headings, input labels, SVGs and fonts:', 'PASS' if not errors else errors)
f=TTFont('/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf');c=f.getBestCmap();metrics=f['hmtx'].metrics;units=f['head'].unitsPerEm
for t in ['Elsewhere is','closer than','you think.']:
 width=sum(metrics[c[ord(x)]][0] for x in t)/units*62-(len(t)-1)*62*.07
 print(f'320px phone title estimate: {t} = {width:.1f}px')
assert not errors
