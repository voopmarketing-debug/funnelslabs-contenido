import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
USER='@usuario'     # reemplazar por el usuario real
NOMBRE='Miryam'   # reemplazar por el nombre de la dueña
def brand(c='#F5EEDC'): return f'<div class="brand" style="color:{c}"><span>SAJUMA</span><span>{USER.upper()}</span></div>'
def full(img,inner):
    return f'<section class="slide" style="background:#2a1d14"><div class="photo" style="height:1350px;background-image:url(img/{img})"></div><div class="scrim"></div>{brand()}<div class="over">{inner}</div></section>'
S=[]
# 1 portada
S.append(f'''<section class="slide" style="background:#3E4A35;color:#F5EEDC">{brand()}
<div class="intro" style="top:165px">Todo empezó con una pregunta…</div>
<div class="big" style="top:235px;font-size:176px">¿se lo<br>daría a<br>mis hijos?</div>
<div class="shadow" style="left:350px;top:1190px;width:380px"></div>
<img class="hero" src="img/cupcake.png" style="left:330px;top:700px;width:420px">
<div class="cap" style="bottom:38px">DESLIZA →</div></section>''')
# 2
S.append(full('full-02-manos-masa.jpg',f'<div class="g" style="font-size:150px">Soy {NOMBRE}.</div><div class="t1" style="font-size:60px;margin-top:14px">Mamá antes que pastelera.</div>'))
# 3
S.append(full('full-03-mesa-familiar.jpg','<div class="t1" style="font-size:62px">Quería que en casa celebráramos con postre… sin descuidar lo que más amo: su salud.</div>'))
# 4
S.append(full('full-04-ingredientes.jpg','<div class="t1" style="font-size:58px">Así que empecé a cambiar ingredientes.</div><div class="g" style="font-size:150px;margin-top:10px">uno por uno.</div>'))
# 5
S.append(f'''<section class="slide" style="background:#A3AE84;color:#3E4A35">{brand("#3E4A35")}
<div class="intro" style="top:190px;font-size:50px">Y descubrí algo:</div>
<div class="big" style="top:262px;font-size:112px;line-height:1">lo rico también<br>puede cuidarte</div>
<div class="shadow" style="left:200px;top:1240px;width:680px;opacity:.5"></div>
<img class="hero" src="img/torta-frutas.png" style="left:170px;top:600px;width:740px">
</section>''')
# 6
S.append(full('full-06-horno.jpg','<div class="t1" style="font-size:64px">Si era bueno para mi familia, podía ser bueno para la tuya.</div>'))
# 7
S.append(f'''<section class="slide" style="background:#F5EEDC;color:#3E4A35">{brand("#3E4A35")}
<div class="intro" style="top:330px;font-size:60px;color:#2a2a24">Así nació</div>
<img src="ref/sajuma-logo-transparente.png" style="position:absolute;left:150px;top:440px;width:780px">
<div class="line"></div>
<div class="cap" style="top:1130px;font-size:30px">PRÓXIMO CAPÍTULO →</div><div class="cap" style="top:1190px;font-size:30px">LO QUE LLEVA TU POSTRE</div></section>''')
css='''
*{box-sizing:border-box;margin:0;padding:0}
body{background:#222;display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0;font-family:"Jost",sans-serif}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden}
.brand{position:absolute;z-index:9;left:60px;right:60px;top:52px;display:flex;justify-content:space-between;font-weight:400;font-size:24px;letter-spacing:.32em;text-shadow:0 1px 10px rgba(0,0,0,.35)}
.intro{position:absolute;left:0;right:0;text-align:center;font-weight:300;font-size:54px;letter-spacing:-.005em}
.big{position:absolute;left:0;right:0;text-align:center;font-family:"Gloock",serif;line-height:.98;letter-spacing:-.01em}
.g{font-family:"Gloock",serif;line-height:1}
.cap{position:absolute;left:0;right:0;text-align:center;font-weight:400;font-size:28px;letter-spacing:.34em}
.hero{position:absolute;z-index:3}
.shadow{position:absolute;z-index:2;height:60px;border-radius:50%;background:rgba(0,0,0,.45);filter:blur(26px)}
.photo{position:absolute;left:0;top:0;width:1080px;background-size:cover;background-position:center}
.panel{position:absolute;left:0;width:1080px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 90px}
.t1{font-weight:300;line-height:1.18;text-wrap:balance}
.scrim{position:absolute;inset:0;z-index:2;background:linear-gradient(180deg,rgba(28,18,12,.30) 0,rgba(28,18,12,.12) 30%,rgba(28,18,12,.62) 62%,rgba(28,18,12,.88) 100%)}
.over{position:absolute;z-index:5;left:80px;right:80px;bottom:90px;text-align:center;color:#F5EEDC;text-shadow:0 2px 24px rgba(0,0,0,.45)}
.over .g{line-height:1}
.line{position:absolute;left:480px;width:120px;top:1085px;border-top:1.5px solid #3E4A35;opacity:.5}
'''
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAJUMA — Todo empezó en mi cocina</title>
<link href="https://fonts.googleapis.com/css2?family=Gloock&family=Jost:wght@300;400&display=swap" rel="stylesheet"><style>{css}</style></head><body>{''.join(S)}</body></html>'''
open('carrusel.html','w').write(html)
