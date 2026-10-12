import cv2, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ICON={
'book':'<path d="M4 5.5c3-1.4 5.7-1.2 8 .6 2.3-1.8 5-2 8-.6v13c-3-1.4-5.7-1.2-8 .6-2.3-1.8-5-2-8-.6z"/><path d="M12 6.1v13"/>',
'search':'<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5.5 5.5"/>',
'help':'<circle cx="12" cy="12" r="9"/><path d="M9.3 9.5a2.8 2.8 0 1 1 4.3 2.4c-.9.6-1.6 1.1-1.6 2.3"/><circle cx="12" cy="17.3" r=".6" fill="currentColor"/>',
'chat':'<path d="M4 5h16v11H9.5L5 20v-4H4z"/>',
'term':'<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><path d="M7 10l3 2.5L7 15M12.5 15H17"/>',
'web':'<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><path d="M3 9.5h18"/><circle cx="6" cy="7" r=".5" fill="currentColor"/><circle cx="8.2" cy="7" r=".5" fill="currentColor"/>',
'shield':'<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8-7.5 9.5-4.3-1.5-7.5-5-7.5-9.5V6z"/><path d="M9 12l2.2 2.2L15.5 10"/>',
'pencil':'<path d="M4 20l1-4L16.5 4.5a2 2 0 0 1 3 3L8 19z"/><path d="M14.5 6.5l3 3"/>',
'folder':'<path d="M3.5 7.5a2 2 0 0 1 2-2H10l2 2.5h6.5a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2z"/><rect x="9.5" y="12.5" width="5" height="4" rx=".8"/>',
'one':'<circle cx="12" cy="12" r="9"/><path d="M10.5 9.5L12.5 8v8"/>',
}
def ic(k): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>'
def row(k,t,d,last=False): return f'<div class="row{" last" if last else ""}"><span class="ic">{ic(k)}</span><div><b>{t}</b><span>{d}</span></div></div>'

def photo(n,W,T,dx=0,extra=''):
    return f'<div class="ph" style="width:{W}px;top:{T}px;left:{(1080-W)//2+dx}px;{extra}"><img src="img/{n}-c.png"></div>'
def BG(n): return f'<img class="bleed" src="img/f{n}.jpg"><div class="shade"></div>'
def head(i,l1,l2,sub=None,size=88):
    s=f'<div class="n">{i}/7</div><div class="kick"><i></i>Find skills</div><div class="h" style="font-size:{size}px">{l1}<br><span class="l">{l2}</span></div>'
    if sub: s+=f'<div class="sub">{sub}</div>'
    return s
foot='<div class="foot"><span>@funnelslabs</span></div>'

S=[]
# 1 portada
S.append(f'''<section class="slide">{BG(1)}{head(1,'Instala una sola skill.','Que sea esta.','La más instalada de skills.sh: <b>más de 3 millones</b> de instalaciones.',88)}{foot}</section>''')
# 2 qué es
S.append(f'''<section class="slide">{BG(2)}{head(2,'Claude no sabe','qué skills existen.',None,84)}
<div class="panel" style="top:296px">
{row('book','Qué es una skill','Un archivo de instrucciones que le enseña una tarea nueva a Claude.')}
{row('search','Qué hace find-skills','Busca en el catálogo la que necesitas y te ayuda a instalarla.')}
{row('help','Por qué la necesitas','Sin ella, tendrías que buscar y probar skills una por una.',True)}
</div>{foot}</section>''')
# 3 cuéntale
S.append(f'''<section class="slide">{BG(3)}{head(3,'Dile qué necesitas,','sin saber el nombre.',None,84)}
<div class="panel" style="top:296px">
<div class="ph2">Pídeselo con tus propias palabras</div>
<div class="chips"><span>¿Cómo respondo más rápido mis mensajes de WhatsApp?</span><span>Busca una skill para crear mis carruseles.</span><span>¿Existe una skill que revise la ortografía de mis textos?</span></div>
{row('shield','Antes de instalarla','Revisa sus auditorías de seguridad en skills.sh. Una skill puede hacer lo mismo que tu Claude.',True)}
</div>{foot}</section>''')
# 4 afirmación (asfalto a sangre)
S.append(f'''<section class="slide"><img class="bleed" src="img/asfalto.png"><div class="shade"></div>{head(4,'Una skill para','encontrarlas todas.','Tú le dices qué necesitas. Ella busca por ti.',96)}{foot}</section>''')
# 5 instalar
S.append(f'''<section class="slide">{BG(5)}{head(5,'Instálala con','un solo comando.',None,84)}
<div class="panel cmp" style="top:296px">
<div class="code">npx skills add vercel-labs/skills --skill find-skills -a claude-code -g -y</div>
<div class="note">Pégalo en tu terminal. Queda disponible en todos tus proyectos.</div>
<div class="ph2" style="margin-top:8px;padding-bottom:2px">3 formas de buscar</div>
<div class="cols">
<div>{ic('chat')}<b>En Claude</b><span>Pídeselo como hablas.</span></div>
<div>{ic('term')}<b>En la terminal</b><span><code>npx skills find [palabra]</code></span></div>
<div>{ic('web')}<b>En la web</b><span>skills.sh: las más usadas y las nuevas.</span></div>
</div>
</div>{foot}</section>''')
# 6 hazla tuya
S.append(f'''<section class="slide">{BG(6)}{head(6,'Hazla tuya,','con tus reglas.',None,88)}
<div class="panel" style="top:296px">
{row('one','1 · Encuentra la skill','find-skills te muestra la que más se parece a lo que haces.')}
{row('pencil','2 · Pídele a Claude que la adapte','Cuéntale cómo es tu negocio y cómo trabajas.')}
{row('folder','3 · Guárdala con otro nombre','Así, cuando salga una versión nueva, no pierdes tus cambios.',True)}
</div>{foot}</section>''')
# 7 CTA
S.append(f'''<section class="slide">{BG(7)}{head(7,'Escribe <span class="pill">SKILLS</span>','y te envío la guía.','Con el paso a paso para instalarla y adaptarla a tu negocio.',92)}{foot}</section>''')

css='''
:root{--lime:#b5ff2b}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#333;font-family:"Montserrat",Arial,sans-serif;display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0}
.slide{position:relative;width:1080px;height:1350px;background:#000;overflow:hidden;color:#fff}
.ph{position:absolute;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 9%,#000 91%,transparent 100%);mask-image:linear-gradient(90deg,transparent 0,#000 9%,#000 91%,transparent 100%)}
.ph img{display:block;width:100%;height:auto}
.bleed{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.66) 0,rgba(0,0,0,.34) 30%,rgba(0,0,0,0) 48%)}
.n{position:absolute;top:50px;right:60px;z-index:5;background:rgba(40,40,40,.78);border:1px solid rgba(255,255,255,.18);color:#fff;font-weight:700;font-size:23px;padding:9px 20px;border-radius:99px}
.kick{position:absolute;z-index:5;left:64px;top:62px;font-weight:800;font-size:24px;letter-spacing:.3em;text-transform:uppercase;color:#e8e8e2;display:flex;align-items:center;gap:16px}
.kick i{width:46px;height:3px;background:var(--lime);display:block}
.h{position:absolute;z-index:5;left:64px;right:64px;top:112px;font-weight:900;letter-spacing:-0.045em;line-height:1;text-shadow:0 4px 28px rgba(0,0,0,.45)}
.h .l{color:var(--lime);font-style:italic;font-weight:800}
.h .pill{display:inline-block;background:var(--lime);color:#0a0a0a;border-radius:18px;padding:0 22px 6px;margin-left:6px;text-shadow:none}
.sub{position:absolute;z-index:5;left:64px;right:64px;top:318px;font-weight:600;font-size:31px;line-height:1.3;color:#ececE6;letter-spacing:-0.01em;text-shadow:0 2px 18px rgba(0,0,0,.6)}
.sub b{color:#fff;font-weight:800}
.panel{position:absolute;z-index:5;left:40px;right:40px;border-radius:34px;padding:12px 34px;background:linear-gradient(180deg,rgba(12,12,12,.58),rgba(12,12,12,.46));border:1.5px solid rgba(255,255,255,.24);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);box-shadow:0 30px 60px -30px rgba(0,0,0,.8)}
.row{display:flex;gap:24px;align-items:center;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.2)}
.row.last{border-bottom:0}
.cmp .row{padding:10px 0}.cmp .note{padding-bottom:10px}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:4px 0 14px}.cols>div{display:flex;flex-direction:column;gap:6px}.cols svg{width:44px;height:44px;color:#fff;margin-bottom:2px}.cols b{font-weight:800;font-size:27px;letter-spacing:-0.02em}.cols span{font-weight:500;font-size:21px;line-height:1.3;color:#dcdcd5}.cols code{font-family:"Courier New",monospace;font-weight:700;font-size:19px;word-break:break-all}
.row .ic{flex:none;width:58px;height:58px;color:#fff;display:flex;align-items:center;justify-content:center}.row .ic svg{width:50px;height:50px}
.row b{display:block;font-weight:800;font-size:30px;letter-spacing:-0.02em;line-height:1.15}
.row span{display:block;font-weight:500;font-size:23px;line-height:1.3;color:#dcdcd5;margin-top:3px}
.row code,.code{font-family:"Courier New",monospace;font-weight:700}
.ph2{font-weight:800;font-size:30px;letter-spacing:-0.02em;padding:14px 0 8px}
.chips{display:flex;flex-direction:column;gap:10px;align-items:flex-start;padding-bottom:16px;border-bottom:1px solid rgba(255,255,255,.2)}
.chips span{border:1.5px solid rgba(255,255,255,.55);border-radius:99px;padding:9px 22px;font-weight:500;font-size:24px}
.code{font-size:20px;line-height:1.35;padding:18px 4px 6px;color:#fff;word-break:break-all}
.note{font-size:23px;font-weight:500;color:#dcdcd5;padding:4px 4px 16px;border-bottom:1px solid rgba(255,255,255,.2)}
.foot{position:absolute;z-index:6;right:64px;bottom:34px;text-align:right;font-weight:700;font-size:19px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.75);text-shadow:0 2px 12px rgba(0,0,0,.9)}
'''
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Find skills — Funnels Labs</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,500;0,600;0,700;0,800;0,900;1,800&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
{''.join(S)}
</body></html>'''
open('carrusel.html','w').write(html)
