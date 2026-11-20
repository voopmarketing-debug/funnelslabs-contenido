import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
HANDLE='@funnelslabs'; KEY='SISTEMA'
def foto(n,desc):
    p=f'img/foto-{n}.jpg'
    if os.path.exists(p): return f'<div class="ph" style="background-image:url({p})"></div>'
    return f'<div class="ph empty"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><circle cx="12" cy="8" r="3.6"/><path d="M5 20c.8-4 3.5-6 7-6s6.2 2 7 6"/></svg><span>FOTO<br><b>{desc}</b></span></div>'
def bar(extra=''):
    return f'<div class="bar"><span>{HANDLE.upper()}</span><span>COMENTA “{KEY}”</span><span>GUÁRDALO</span></div>'
def card(kind,n,desc,t1,t2=None,hot=None,color=None):
    cls='aburre' if kind=='a' else 'vende'
    inner=f'<div class="ct">{t1}</div>'
    if kind=='v' and t2: inner+=f'<div class="ct2">{t2}</div>'
    if kind=='v' and hot: inner+=f'<div class="hot" style="color:{color}">{hot}</div><svg class="arr" viewBox="0 0 60 40"><path d="M4 6c20-6 40 4 46 26M50 32l-10-4M50 32l2-11" fill="none" stroke="{color}" stroke-width="3.5" stroke-linecap="round"/></svg>'
    return f'<div class="card {cls}">{foto(n,desc)}<div class="shade"></div>{inner}</div>'
def niche(i,title,n,desc,a,v1,v2,hot,color):
    return f'''<section class="slide"><div class="n">{i}/6</div><div class="kick"><i></i>Funnels Labs</div>
<div class="title">{title}</div>
<div class="tag a">ABURRE <em>✕</em></div><div class="tag v">VENDE <em>✓</em></div>
{card('a',n,desc,a)}{card('v',n,desc,v1,v2,hot,color)}{bar()}</section>'''
S=[]
S.append(f'''<section class="slide cover"><div class="n">1/6</div><div class="kick"><i></i>Funnels Labs</div>
<div class="half top"><div class="big">Storytelling</div><div class="sub"><i></i><span>QUE ABURRE</span><i></i></div></div>
<div class="half bot"><div class="big g">Storytelling</div><div class="sub"><i></i><span>QUE VENDE</span><i></i></div></div>{bar()}</section>''')
S.append(niche(2,'FINANZAS','finanzas','hombre de negocios maduro, traje, manos en los bolsillos, oficina','3 Tips para mejorar tus finanzas','Este cliente perdió el 40% de su dinero','Por no saber','ESTO','#ff4b3e'))
S.append(niche(3,'MÉDICOS','medicos','médico con bata azul y brazos cruzados, equipo detrás','Ven a hacerte tu chequeo anual','Llegó al hospital por una revisión… Pero terminó en urgencias','Por estos 3 simples','“SÍNTOMAS”','#b5ff2b'))
S.append(niche(4,'VENTAS','ventas','mujer ejecutiva hablando por teléfono con laptop','“Cómo manejar objeciones”','Tuvo +15 llamadas y no cerró ni un cliente','Por este error','COMÚN','#ffb02e'))
S.append(niche(5,'ABOGADOS','abogados','abogado leyendo un contrato, balanza de justicia','“Asesoría legal disponible”','Facturaba $2 millones/año y su socio le robó todo','Por firmar sin LEER esta','CLÁUSULA','#ff4b3e'))
S.append(f'''<section class="slide cta"><img class="bleed" src="img/selfie-4x5.jpg"><div class="shadeall"></div><div class="n">6/6</div>
<div class="c1">PERO RECUERDA</div><div class="c2">COMENTA<br><span>“{KEY}”</span></div><div class="c3">SI QUIERES</div>
<div class="c4"><b>CONSEGUIR MÁS</b><span>CLIENTES</span><em>sin perseguirlos, con IA</em></div>{bar()}</section>''')
css='''*{box-sizing:border-box;margin:0;padding:0}
body{background:#333;display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0;font-family:"Montserrat",Arial,sans-serif}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;background:#0a0a0a;color:#fff}
.n{position:absolute;top:44px;right:56px;z-index:9;background:rgba(40,40,40,.8);border:1px solid rgba(255,255,255,.18);font-weight:700;font-size:23px;padding:9px 20px;border-radius:99px}
.kick{position:absolute;z-index:9;left:60px;top:54px;font-weight:800;font-size:22px;letter-spacing:.3em;text-transform:uppercase;color:#dcdcd5;display:flex;align-items:center;gap:14px}
.kick i{width:42px;height:3px;background:#b5ff2b;display:block}
.bar{position:absolute;left:0;right:0;bottom:0;height:150px;border-top:5px solid #b5ff2b;background:#000;display:flex;justify-content:space-between;align-items:center;padding:0 64px;font-family:"Bebas Neue","Montserrat",sans-serif;font-weight:800;font-size:25px;letter-spacing:.06em;color:#f2f2ec;z-index:8}
.cover .half{position:absolute;left:0;right:0;height:600px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.cover .top{top:0;background:#111}.cover .bot{top:600px;background:#0a0a0a;border-top:5px solid #b5ff2b}
.big{font-weight:900;font-size:150px;letter-spacing:-.045em;line-height:1;color:#e9e9e2}.big.g{color:#b5ff2b}
.sub{display:flex;align-items:center;gap:26px;margin-top:20px;font-weight:800;font-size:54px;letter-spacing:.02em}.sub i{width:120px;height:3px;background:#b5ff2b;display:block;opacity:.7}.top .sub span{color:#8d8d86}
.title{position:absolute;left:0;right:0;top:130px;text-align:center;font-weight:900;font-size:160px;letter-spacing:-.05em;line-height:1;color:#fff}
.tag{position:absolute;top:400px;font-weight:900;font-size:62px;letter-spacing:-.03em;display:flex;align-items:center;gap:12px}
.tag.a{left:70px;color:#8d8d86}.tag.v{left:560px;color:#fff}
.tag em{font-style:normal;font-size:36px;width:56px;height:56px;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#fff;background:#e23d3d}.tag.v em{background:#b5ff2b;color:#0a0a0a}
.card{position:absolute;top:490px;width:455px;height:690px;border-radius:26px;overflow:hidden;background:#161616;border:1.5px solid rgba(255,255,255,.14)}
.card.aburre{left:55px;opacity:.92}.card.vende{left:570px;border-color:rgba(181,255,43,.55);box-shadow:0 0 50px -18px rgba(181,255,43,.5)}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.ph.empty{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;color:#4f4f4a;background:repeating-linear-gradient(45deg,#141414 0 18px,#191919 18px 36px);text-align:center;font-size:19px;letter-spacing:.2em;padding:30px}
.ph.empty svg{width:96px;height:96px}.ph.empty b{display:block;margin-top:8px;font-weight:600;letter-spacing:.04em;line-height:1.3;color:#5d5d57}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0,rgba(0,0,0,.05) 34%,rgba(0,0,0,.05) 62%,rgba(0,0,0,.5) 100%)}
.ct{position:absolute;left:26px;right:26px;top:30px;text-align:center;font-weight:700;font-size:34px;line-height:1.16;text-shadow:0 2px 14px rgba(0,0,0,.7)}
.ct2{position:absolute;left:26px;right:26px;top:560px;text-align:center;font-weight:700;font-size:26px;text-shadow:0 2px 12px rgba(0,0,0,.8)}
.hot{position:absolute;left:20px;right:20px;top:592px;text-align:center;font-weight:900;font-size:58px;letter-spacing:-.04em;line-height:1;white-space:nowrap;text-shadow:0 3px 16px rgba(0,0,0,.6)}
.arr{position:absolute;right:26px;top:662px;width:72px;height:48px;display:none}
.cta .bleed{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shadeall{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.85) 0,rgba(0,0,0,.55) 30%,rgba(0,0,0,.35) 55%,rgba(0,0,0,.85) 100%)}
.c1{position:absolute;left:0;right:0;top:150px;text-align:center;font-weight:800;font-size:44px;z-index:5}
.c2{position:absolute;left:0;right:0;top:215px;text-align:center;font-weight:900;font-size:110px;line-height:.95;letter-spacing:-.04em;color:#b5ff2b;z-index:5}.c2 span{color:#fff;font-size:128px}
.c3{position:absolute;left:0;right:0;top:500px;text-align:center;font-style:italic;font-weight:800;font-size:40px;z-index:5}
.c4{position:absolute;left:0;right:0;top:870px;text-align:center;z-index:5;display:flex;flex-direction:column;align-items:center}
.c4 b{font-weight:900;font-size:68px;letter-spacing:-.03em;text-shadow:0 2px 20px rgba(0,0,0,.7)}.c4 span{font-weight:900;font-size:140px;letter-spacing:-.05em;color:#b5ff2b;line-height:1}.c4 em{font-style:italic;font-weight:700;font-size:36px;margin-top:6px;color:#e6e6df}
'''
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Funnels Labs — Aburre vs Vende</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,500;0,600;0,700;0,800;0,900;1,700;1,800&display=swap" rel="stylesheet"><style>{css}</style></head><body>{''.join(S)}</body></html>'''
open('carrusel.html','w').write(html)
