import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
USER='@sajuma_reposteria'
CREMA='#F5EEDC'; OLIVO='#3E4A35'; CACAO='#4A2E22'; CAR='#B07A47'
def top(c=OLIVO,n=''):
    return f'<div class="brand" style="color:{c}"><span>SAJUMA</span><span>{USER.upper()}</span></div>'
def prod(img,l,t,w,sh=(0,0,0)):
    return f'<div class="shadow" style="left:{l+w*0.12}px;top:{t}px;width:{w*0.76}px"></div><img class="hero" src="img/{img}" style="left:{l}px;top:{t-w*0.0}px;width:{w}px">'
S=[]
# 1 portada: crema, texto arriba, torta abajo
S.append(f'''<section class="slide" style="background:{CREMA};color:{OLIVO}">{top()}
<div class="lab" style="top:170px">LO QUE LLEVA TU POSTRE</div>
<div class="intro" style="top:225px">Ingredientes que puedes</div>
<div class="big" style="top:290px;font-size:176px">pronunciar</div>
<div class="rule" style="top:560px"></div>
<div class="shadow" style="left:200px;top:1190px;width:680px"></div>
<img class="hero" src="img/torta-frutas.png" style="left:150px;top:640px;width:780px">
<div class="arrow">→</div></section>''')
# 2 foto IA a sangre
S.append(f'''<section class="slide" style="background:#2a1d14"><div class="photo" style="background-image:url(img/full-02-fruta.jpg)"></div><div class="scrim"></div>{top(CREMA)}
<div class="over"><div class="lab" style="position:static;color:{CREMA};opacity:.85">FRUTA FRESCA</div><div class="g" style="font-size:96px;margin-top:18px">Fruta de verdad.</div><div class="t1" style="font-size:56px;margin-top:8px">Picada esa misma mañana.</div></div></section>''')
# 3 y 4 plantillas de ingrediente (pendientes de datos)
def ing(n,bg,fg,ph,sub,lab):
    return f'''<section class="slide" style="background:{bg};color:{fg}">{top(fg)}
<div class="lab" style="top:170px">{lab}</div>
<div class="big" style="top:225px;font-size:120px;line-height:1">{ph}</div>
<div class="intro" style="top:380px;font-size:50px">{sub}</div>
<div class="rule" style="top:520px;border-color:{fg}"></div>
<div class="slot" style="border-color:{fg}">imagen del ingrediente · pendiente</div></section>'''
S.append(ing(3,CREMA,OLIVO,'[ingrediente 1]','en lugar de [lo que reemplaza].','INGREDIENTE 01'))
S.append(ing(4,'#E9DCC3',CACAO,'[ingrediente 2]','[beneficio sencillo, sin promesas médicas].','INGREDIENTE 02'))
# 5 quiche
S.append(f'''<section class="slide" style="background:{CREMA};color:{OLIVO}">{top()}
<div class="lab" style="top:170px">TAMBIÉN HAY SALADO</div>
<div class="intro" style="top:225px;font-size:60px">Y sí:</div>
<div class="big" style="top:300px;font-size:150px;line-height:1">también<br>hay salado</div>
<div class="rule" style="top:640px"></div>
<div class="shadow" style="left:190px;top:1150px;width:700px"></div>
<img class="hero" src="img/quiche.png" style="left:130px;top:760px;width:820px"></section>''')
# 6 solo tipografía
S.append(f'''<section class="slide" style="background:{CACAO};color:{CREMA}">{top(CREMA)}
<div class="cap" style="top:300px;font-size:30px">LO QUE NO ENTRA EN MI COCINA</div>
<div class="strike" style="top:480px">[colorantes artificiales]</div>
<div class="strike" style="top:660px">[conservantes]</div>
<div class="strike" style="top:840px">[lo que confirme la dueña]</div></section>''')
# 7 cierre
S.append(f'''<section class="slide" style="background:{CREMA};color:{OLIVO}">{top()}
<img src="ref/sajuma-logo-transparente.png" style="position:absolute;left:340px;top:150px;width:400px">
<div class="big" style="top:330px;font-size:104px;line-height:1.02">Postre rico.<br>Familia cuidada.</div>
<div class="intro" style="top:600px;font-size:54px">Ese es el trato.</div>
<div class="shadow" style="left:380px;top:1010px;width:320px"></div>
<img class="hero" src="img/cupcake.png" style="left:400px;top:760px;width:280px">
<div class="rule" style="top:1110px"></div>
<div class="cap" style="top:1150px;font-size:26px">PRÓXIMO CAPÍTULO →</div><div class="cap" style="top:1195px;font-size:26px">PARA LOS MOMENTOS QUE IMPORTAN</div></section>''')
css='''*{box-sizing:border-box;margin:0;padding:0}
body{background:#222;display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0;font-family:"Jost",sans-serif}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden}
.brand{position:absolute;z-index:9;left:60px;right:60px;top:52px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em}
.lab{position:absolute;left:0;right:0;text-align:center;font-size:24px;letter-spacing:.34em;opacity:.75}
.intro{position:absolute;left:0;right:0;text-align:center;font-weight:300;font-size:54px}
.big{position:absolute;left:0;right:0;text-align:center;font-family:"Gloock",serif;line-height:.98;letter-spacing:-.01em}
.g{font-family:"Gloock",serif;line-height:1}
.t1{font-weight:300;line-height:1.18}
.cap{position:absolute;left:0;right:0;text-align:center;font-size:28px;letter-spacing:.34em}
.rule{position:absolute;left:480px;width:120px;border-top:1.5px solid currentColor;opacity:.45}
.hero{position:absolute;z-index:3}
.shadow{position:absolute;z-index:2;height:56px;border-radius:50%;background:rgba(74,46,34,.38);filter:blur(24px)}
.arrow{position:absolute;right:60px;top:52px;display:none}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.scrim{position:absolute;inset:0;z-index:2;background:linear-gradient(180deg,rgba(28,18,12,.25) 0,rgba(28,18,12,0) 30%,rgba(28,18,12,.6) 62%,rgba(28,18,12,.88) 100%)}
.over{position:absolute;z-index:5;left:80px;right:80px;bottom:90px;text-align:center;color:#F5EEDC;text-shadow:0 2px 24px rgba(0,0,0,.45)}
.slot{position:absolute;left:140px;right:140px;top:640px;height:560px;border:2px dashed;border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:26px;letter-spacing:.2em;text-transform:uppercase;opacity:.5}
.strike{position:absolute;left:0;right:0;text-align:center;font-family:"Gloock",serif;font-size:72px;text-decoration:line-through;text-decoration-thickness:3px;text-decoration-color:#B07A47}
'''
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAJUMA — Lo que lleva tu postre</title>
<link href="https://fonts.googleapis.com/css2?family=Gloock&family=Jost:wght@300;400&display=swap" rel="stylesheet"><style>{css}</style></head><body>{''.join(S)}</body></html>'''
open('carrusel.html','w').write(html)
