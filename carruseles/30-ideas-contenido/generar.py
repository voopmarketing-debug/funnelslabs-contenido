N=[("Restaurantes","Para que tu carta se venda sola.",[
("Pide esto si es tu primera vez","Arma el combo ideal: entrada, plato y bebida."),
("El plato que nadie pide (y debería)","Rescata la joya escondida de tu carta."),
("Con $___ comes así","Un plan completo con precios reales."),
("De la cocina a tu mesa","La preparación de tu plato estrella."),
("Antes de abrir","Cocina, montaje y equipo, sin filtro."),
("Lo que el chef nunca quitaría","La historia detrás de ese plato."),
("Primera reacción","Clientes probando por primera vez, con permiso."),
("El error más común al pedir aquí","Con humor, sin regañar a nadie."),
("Dos personas, dos pedidos","Compara gustos y deja que voten."),
("Planes para una cita","Tres opciones según el presupuesto.")]),
("Belleza y<br>cuidado personal","Para que te elijan antes de sentarse en la silla.",[
("El corte que te favorece, no el de moda","Cómo elegirlo según tu rostro."),
("Antes y después sin cortar de más","Cambios sutiles que se notan."),
("Qué decirle a tu estilista","Cómo pedir exactamente lo que quieres."),
("Este servicio, paso a paso","Qué incluye y para qué sirve cada parte."),
("3 hábitos que dañan tu cabello","Con una alternativa para cada uno."),
("Pinterest vs. realidad","Textura, mantenimiento y estilo reales."),
("Un peinado, tres versiones","Un tutorial rápido."),
("¿Cada cuánto retocar?","Tiempos según el tipo de corte."),
("Lo probamos por ti","Cantidad, aplicación y resultado."),
("¿Este o este?","Encuesta primero, explicación después.")]),
("Servicios<br>profesionales","Para que confíen en ti antes de la primera llamada.",[
("Lo que pide vs. lo que necesita","Cómo detectas el problema real."),
("Pregunta esto antes de contratar","Cinco preguntas que protegen al cliente."),
("3 señales de que necesitas ayuda con ___","Situaciones que tu cliente reconoce."),
("Un caso que parecía pequeño","Cuéntalo sin revelar datos privados."),
("Lo barato que sale caro","Un error y su consecuencia."),
("Qué hay detrás de nuestra tarifa","Haz visible el trabajo."),
("Mitos de nuestro sector","Desmiéntelos con ejemplos."),
("Hazlo tú vs. contrata","Dónde está el límite."),
("Si empezara hoy, revisaría esto","Un checklist práctico."),
("La duda más común, en 30 segundos","Responde una objeción.")])]
css='''
:root{--ink:#0a0a0a;--muted:#55554d;--faint:#9a9a92;--line:#e6e6df;--lime:#b5ff2b;--lilac:#c9a9ff}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#d9d9d2;font-family:"Montserrat",Arial,sans-serif;color:var(--ink);display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0}
.slide{position:relative;width:1080px;height:1350px;background:#fff;overflow:hidden;padding:84px 84px 64px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;font-size:20px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--faint)}
.top .b{display:flex;align-items:center;gap:12px;color:var(--ink)} .top .b i{width:12px;height:12px;border-radius:99px;background:var(--lime);box-shadow:0 0 0 4px rgba(181,255,43,.25)}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:20px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--faint);border-top:1px solid var(--line);padding-top:26px}
.foot .go{display:flex;align-items:center;gap:14px;color:var(--ink)} .foot .go span{width:56px;height:2px;background:var(--ink);position:relative} .foot .go span::after{content:"";position:absolute;right:0;top:-5px;width:10px;height:10px;border-top:2px solid var(--ink);border-right:2px solid var(--ink);transform:rotate(45deg)}
.light{font-weight:300;letter-spacing:-0.04em}
.heavy{font-weight:800;letter-spacing:-0.045em}
.mark{background:linear-gradient(transparent 58%, var(--lime) 58%, var(--lime) 92%, transparent 92%);padding:0 .06em}
.big30{font-size:500px;line-height:.78;font-weight:200;letter-spacing:-0.07em;position:relative;display:inline-block}
.big30::after{content:"";position:absolute;right:-30px;top:20px;width:86px;height:86px;border-radius:99px;background:var(--lime)}
.idx{display:flex;flex-direction:column;border-top:1px solid var(--ink)}
.idx div{display:flex;justify-content:space-between;align-items:baseline;padding:20px 0;border-bottom:1px solid var(--line);font-size:30px;font-weight:600}
.idx small{font-size:20px;font-weight:600;letter-spacing:.14em;color:var(--faint)}
.head{display:flex;justify-content:space-between;align-items:flex-end;margin-top:54px;padding-bottom:30px;border-bottom:1px solid var(--ink)}
.head .n{font-size:190px;line-height:.75;font-weight:200;letter-spacing:-0.07em;position:relative}
.head .n::after{content:"";position:absolute;right:-14px;bottom:4px;width:30px;height:30px;border-radius:99px;background:var(--lime)}
.head h2{font-size:72px;line-height:.98}
.head p{font-size:24px;font-weight:500;color:var(--muted);margin-top:16px}
.grid{display:grid;grid-template-columns:1fr 1fr;column-gap:56px;margin-top:8px}
.it{display:flex;gap:18px;padding:27px 0;border-bottom:1px solid var(--line)}
.it .k{flex:none;width:44px;font-size:18px;font-weight:700;letter-spacing:.06em;color:var(--faint);padding-top:5px;font-variant-numeric:tabular-nums}
.it b{display:block;font-size:26px;font-weight:700;line-height:1.18;letter-spacing:-0.02em}
.it span{display:block;font-size:21px;font-weight:400;line-height:1.35;color:var(--muted);margin-top:6px}
'''
def item(j,ideas): return f'<div class="it"><div class="k">{j+1:02d}</div><div><b>“{ideas[j][0]}”</b><span>{ideas[j][1]}</span></div></div>'
def niche(i,n):
    name,sub,ideas=n
    left=''.join(item(j,ideas) for j in range(5)); right=''.join(item(j,ideas) for j in range(5,10))
    return f'''<section class="slide">
  <div class="top"><div class="b"><i></i>Funnels Labs</div><div>Nicho {i:02d} / 03</div></div>
  <div class="head"><div><h2 class="heavy">{name}</h2><p>{sub}</p></div><div class="n">{i:02d}</div></div>
  <div class="grid"><div>{left}</div><div>{right}</div></div>
  <div class="foot"><span>@funnelslabs</span><span class="go">Desliza<span></span></span></div>
</section>'''
cover='''<section class="slide">
  <div class="top"><div class="b"><i></i>Funnels Labs</div><div>Guía de contenido</div></div>
  <div style="margin-top:70px"><span class="big30">30</span></div>
  <div style="margin-top:34px;font-size:96px;line-height:.98" class="heavy">ideas de contenido<br><span class="light">para tu </span><span class="mark">negocio.</span></div>
  <p style="margin-top:26px;font-size:28px;font-weight:500;color:var(--muted)">Para que no vuelvas a quedarte en blanco frente al celular.</p>
  <div class="idx" style="margin-top:46px">
    <div><span>Restaurantes</span><small>10 IDEAS</small></div>
    <div><span>Belleza y cuidado personal</span><small>10 IDEAS</small></div>
    <div><span>Servicios profesionales</span><small>10 IDEAS</small></div>
  </div>
  <div class="foot"><span>@funnelslabs</span><span class="go">Desliza<span></span></span></div>
</section>'''
cta='''<section class="slide">
  <div class="top"><div class="b"><i></i>Funnels Labs</div><div>Antes de irte</div></div>
  <div style="margin:auto 0">
    <div class="heavy" style="font-size:104px;line-height:.98">Las ideas<br><span class="light">ya las tienes.</span></div>
    <div class="heavy" style="font-size:104px;line-height:.98;margin-top:30px">Lo difícil es<br><span class="mark">que vendan.</span></div>
    <p style="margin-top:44px;font-size:30px;font-weight:500;line-height:1.4;color:var(--muted);max-width:840px">Guarda este post para tu próxima semana de contenido. Y si quieres que cada publicación termine en una conversación por WhatsApp, comenta:</p>
    <div style="display:inline-flex;align-items:center;gap:22px;margin-top:34px;border:2px solid var(--ink);border-radius:99px;padding:18px 40px 20px">
      <span style="width:16px;height:16px;border-radius:99px;background:var(--lime);box-shadow:0 0 0 6px rgba(181,255,43,.3)"></span>
      <span class="heavy" style="font-size:54px">SISTEMA</span></div>
  </div>
  <div class="foot"><span>@funnelslabs</span><span>Guárdalo</span></div>
</section>'''
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>30 ideas de contenido — Funnels Labs</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
{cover}
{''.join(niche(i+1,n) for i,n in enumerate(N))}
{cta}
</body></html>'''
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'carrusel.html'),'w').write(html)
