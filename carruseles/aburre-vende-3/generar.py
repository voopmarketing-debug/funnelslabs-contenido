import os,sys
BASE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.dirname(BASE))
from _motor_aburre_vende import render
cfg=dict(name='WhatsApp: aburre vs vende',key='LEADS',cover='WhatsApp',cover_size=170,
 niches=[
  dict(title='TIENDAS ONLINE',size=108,foto='tiendas',desc='emprendedora joven con paquetes y celular en su bodega',aburre='“Escríbenos para hacer tu pedido”',vende='Respondió 3 horas tarde y perdió la venta',por='Por este',hot='MOTIVO',color='#ffb02e'),
  dict(title='CLÍNICAS DENTALES',size=96,foto='dental',desc='odontólogo con bata y tapabocas bajo el cuello, sonriendo',aburre='“Agenda tu cita con nosotros”',vende='Le escribieron 40 pacientes y contestó a 10',por='Por no tener',hot='ESTO',color='#b5ff2b'),
  dict(title='ACADEMIAS',foto='academias',desc='profesora joven con tablet en un salón de clases',aburre='“Inscripciones abiertas”',vende='Tenía 200 interesados y se inscribieron 3',por='Por no hacer',hot='SEGUIMIENTO',color='#ff4b3e'),
  dict(title='AGENCIAS',foto='agencias',desc='dueño de agencia en una oficina creativa con laptop',aburre='“Cotiza tu proyecto con nosotros”',vende='Envió 20 cotizaciones y nadie respondió',por='Por este',hot='OLVIDO',color='#ffb02e')],
 cta=dict(img='img/cta-4x5.jpg',l1='NO PERDER NI UN',l2='CLIENTE',l3='con respuestas automáticas con IA'))
render(cfg,BASE)
