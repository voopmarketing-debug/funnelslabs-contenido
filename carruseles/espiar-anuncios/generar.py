import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ICON={
'cal':'<rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
'copy':'<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/>',
'layers':'<path d="M12 4l9 5-9 5-9-5z"/><path d="M3 14l9 5 9-5"/>',
'eye':'<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
'free':'<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.8 1.8 0 0 1 0 3.5h-3a1.8 1.8 0 0 0 0 3.5h4"/>',
'list':'<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/>',
}
def ic(k): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>'
def row(k,t,d,last=False): return f'<div class="row{" last" if last else ""}"><span class="ic">{ic(k)}</span><div><b>{t}</b><span>{d}</span></div></div>'
def photo(n,W,T): return f'<div class="ph" style="width:{W}px;top:{T}px;left:{(1080-W)//2}px"><img src="img/{n}-c.png"></div>'
def head(i,kick,l1,l2=None,sub=None,size=88):
    s=f'<div class="n">{i}/10</div><div class="kick"><i></i>{kick}</div><div class="h" style="font-size:{size}px">{l1}'
    if l2: s+=f'<br><span class="l">{l2}</span>'
    s+='</div>'
    if sub: s+=f'<div class="sub">{sub}</div>'
    return s
foot='<div class="foot"><span>@funnelslabs</span></div>'
# ventana de pantalla para el video: x=60 y=620 (barra 48px) -> video 960x540 en (60,668)
def brand(i,cat,name,desc,look,size=118):
    return f'''<section class="slide">{head(i,f"{i-2:02d} · {cat}",name,None,desc,size)}
<div class="look"><b>Fíjate en</b><span>{look}</span></div>
<div class="win" id="slot{i}"><div class="bar"><i></i><i></i><i></i><em>Biblioteca de anuncios de Meta · {name}</em></div><div class="vid"><span>Aquí va tu video de {name}</span></div></div>{foot}</section>'''
S=[]
S.append(f'''<section class="slide">{photo('brazos',860,404)}{head(1,'Biblioteca de anuncios','Las marcas que reviso','cuando no tengo ideas.','Anuncios reales, a un clic de distancia.',70)}{foot}</section>''')
S.append(f'''<section class="slide">{head(2,'Biblioteca de anuncios','Tu competencia ya probó','lo que tú aún no.',None,72)}
<div class="panel" style="top:300px">
{row('free','Es pública y gratis','Cualquier persona puede entrar, sin cuenta de anunciante.')}
{row('eye','Muestra anuncios activos','Los mensajes, formatos y ofertas que una marca tiene hoy.')}
{row('list','Te ahorra horas','Ves ideas reales antes de gastar en probar las tuyas.',True)}
</div>{photo('chat',545,720)}{foot}</section>''')
B=[('Ropa deportiva','Gymshark','Anuncios con creadores, producto y ofertas.','Quién aparece en los primeros 3 segundos.'),
   ('Apps','Duolingo','Anuncios que parecen contenido, no publicidad.','El humor y cómo cuentan una idea en pocos segundos.'),
   ('Comida a domicilio','HelloFresh','Anuncios centrados en la oferta.','Cómo muestran el precio y qué incluye.'),
   ('Bebidas','Olipop','Anuncios que explican un beneficio con palabras simples.','Cómo explican el producto sin tecnicismos.'),
   ('Agua en lata','Liquid Death','Anuncios con una personalidad muy marcada.','Los ganchos inesperados y el tono de la marca.'),
   ('Suplementos','Ritual','Anuncios que construyen confianza.','Cómo muestran los ingredientes y de dónde vienen.')]
for k,(c,n,d,l) in enumerate(B): S.append(brand(3+k,c,n,d,l,118 if len(n)<10 else 100))
S.append(f'''<section class="slide">{head(9,'Cómo leerlos','Cómo saber si un','anuncio funciona.',None,84)}
<div class="panel" style="top:300px">
{row('cal','En circulación desde','Si lleva meses activo, es una pista de que sigue dando resultado.')}
{row('layers','Varias versiones','La marca está probando cambios sobre una misma idea.')}
{row('copy','Mismo texto, varios anuncios','Es el mensaje que más repite. Fíjate en cuál es.',True)}
</div><div class="tag">Copia el método, no el anuncio.</div>{photo("caminando",520,790)}{foot}</section>''')
S.append(f'''<section class="slide">{photo('abrazo',744,430)}{head(10,'Biblioteca de anuncios','Escribe <span class="pill">ANUNCIOS</span>','y te envío la guía.','Cómo espiar anuncios en la Biblioteca de Meta y convertirlos en ideas para tu negocio.',92)}{foot}</section>''')
css=open('estilo.css').read()
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Espiar anuncios — Funnels Labs</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,500;0,600;0,700;0,800;0,900;1,800&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
{''.join(S)}
</body></html>'''
open('carrusel.html','w').write(html)
