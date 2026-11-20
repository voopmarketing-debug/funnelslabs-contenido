import os,sys
BASE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.dirname(BASE))
from _motor_aburre_vende import render
cfg=dict(name='Aburre vs Vende',key='SISTEMA',cover='Storytelling',
 niches=[
  dict(title='FINANZAS',foto='finanzas',desc='hombre de negocios maduro, traje, manos en los bolsillos, oficina',aburre='3 Tips para mejorar tus finanzas',vende='Este cliente perdió el 40% de su dinero',por='Por no saber',hot='ESTO',color='#ff4b3e'),
  dict(title='MÉDICOS',foto='medicos',desc='médico con bata azul y brazos cruzados, equipo detrás',aburre='Ven a hacerte tu chequeo anual',vende='Llegó al hospital por una revisión… Pero terminó en urgencias',por='Por estos 3 simples',hot='“SÍNTOMAS”',color='#b5ff2b'),
  dict(title='VENTAS',foto='ventas',desc='mujer ejecutiva hablando por teléfono con laptop',aburre='“Cómo manejar objeciones”',vende='Tuvo +15 llamadas y no cerró ni un cliente',por='Por este error',hot='COMÚN',color='#ffb02e'),
  dict(title='ABOGADOS',foto='abogados',desc='abogado leyendo un contrato, balanza de justicia',aburre='“Asesoría legal disponible”',vende='Facturaba $2 millones/año y su socio le robó todo',por='Por firmar sin LEER esta',hot='CLÁUSULA',color='#ff4b3e')],
 cta=dict(img='img/selfie-4x5.jpg',l1='CONSEGUIR MÁS',l2='CLIENTES',l3='sin perseguirlos, con IA'))
render(cfg,BASE)
