import os,sys
BASE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.dirname(BASE))
from _motor_aburre_vende import render
cfg=dict(name='Anuncios: aburre vs vende',key='ANUNCIOS',cover='Anuncios',cover_size=170,
 niches=[
  dict(title='RESTAURANTES',size=128,foto='restaurantes',desc='chef o dueña de restaurante con delantal, de pie en su cocina',aburre='“Visítanos, tenemos menú del día”',vende='Su restaurante estaba vacío los martes',por='Hasta que cambió este',hot='DETALLE',color='#ffb02e'),
  dict(title='INMOBILIARIAS',size=118,foto='inmobiliarias',desc='asesor inmobiliario con traje frente a un edificio moderno',aburre='“Apartamentos en venta, escríbenos”',vende='Mostró 30 apartamentos y no vendió ninguno',por='Por no decir',hot='ESTO',color='#ff4b3e'),
  dict(title='ESTÉTICA',foto='estetica',desc='esteticista con bata blanca en un spa luminoso, manos juntas',aburre='“Agenda tu cita de limpieza facial”',vende='Perdió 12 clientas en un solo mes',por='Por este',hot='ERROR',color='#b5ff2b'),
  dict(title='COACHES',foto='coaches',desc='coach joven con camisa, sentado en un sillón, con un cuaderno',aburre='“Coaching para transformar tu vida”',vende='Tenía 5.000 seguidores y cero clientes',por='Por no hacer',hot='ESTO',color='#ff4b3e')],
 cta=dict(img='img/cta-4x5.jpg',l1='VENDER MÁS',l2='CLIENTES',l3='con anuncios que sí funcionan'))
render(cfg,BASE)
