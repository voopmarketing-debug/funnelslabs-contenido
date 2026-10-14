"""Recorta las 4 vistas del muñeco de ref/muneco-hoja.webp (fondo gris claro con cuadrícula)
-> img/muneco-<vista>.png con transparencia. Cuerpo: rembg; zapatos (blancos sobre piso claro): trazados a mano."""
import numpy as np, cv2, os
from PIL import Image
from rembg import remove, new_session
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sheet=Image.open('ref/muneco-hoja.webp').convert('RGB')
VIEWS={'frontal':(0,0,282,490),'perfil':(284,0,564,490),'trasera':(0,506,282,994),'tres-cuartos':(336,506,564,994)}
# polígonos de zapatos en coordenadas de la franja de los pies (110 px de alto, borde inferior de la vista)
SHOES={
 'frontal':[[(75,52),(97,49),(105,54),(116,59),(117,72),(107,85),(96,99),(64,97),(59,92),(60,84),(65,75),(70,60)],
            [(160,56),(175,50),(195,49),(201,54),(212,82),(210,94),(195,99),(185,99),(175,85),(165,75),(159,62)]],
 'perfil':[[(100,65),(112,48),(128,42),(140,56),(150,60),(180,62),(183,72),(181,92),(150,98),(110,100),(100,96)]],
 'trasera':[[(72,62),(116,62),(118,84),(112,100),(90,104),(78,102),(72,90)],[(165,62),(205,62),(206,84),(200,100),(178,104),(168,100),(164,88)]],
 'tres-cuartos':[[(20,60),(35,70),(45,62),(68,58),(78,62),(80,80),(70,105),(55,110),(35,105),(20,95)],
                 [(92,58),(115,55),(120,50),(132,45),(142,40),(145,52),(155,65),(170,75),(172,85),(160,90),(145,88),(115,92),(95,88),(92,70)]],
}
def build(name):
    x0,y0,x1,y1=VIEWS[name]; c=sheet.crop((x0,y0,x1,y1)); h=c.size[1]
    if name=='tres-cuartos':                       # tapa el recuadro del reloj, que cae dentro del recorte
        arr=np.array(c); arr[:108,:16]=np.median(arr[2:20,60:200].reshape(-1,3),0).astype(np.uint8); c=Image.fromarray(arr)
    out=np.array(remove(c,session=new_session('u2net'))); a=(out[...,3]>128).astype(np.uint8)
    rgb=np.array(c); hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV)
    colored=((hsv[...,1]>70)&(a>0)).astype(np.uint8)          # azul/verde/rojo/piel
    zone=np.zeros_like(a); zone[h-110+40:]=1
    m=np.where(zone>0,colored,a).astype(np.uint8)
    if name=='tres-cuartos': m[:,:34]=colored[:,:34]      # el borde izquierdo del recorte trae un trozo de piso
    for poly in SHOES[name]:
        cv2.fillPoly(m,[np.array([(x,y+h-110) for x,y in poly],np.int32)],1)
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(m); m=(lab==(np.argmax(st[1:,4])+1)).astype(np.uint8)
    mp=np.pad(m,3); inv=1-mp; mm=np.zeros((mp.shape[0]+2,mp.shape[1]+2),np.uint8); cv2.floodFill(inv,mm,(0,0),2); m=(mp|(inv==1)).astype(np.uint8)[3:-3,3:-3]
    alpha=cv2.GaussianBlur(m.astype(np.float32),(0,0),0.7)
    rgba=np.dstack([rgb,(alpha*255).astype(np.uint8)])
    Image.fromarray(rgba,'RGBA').save(f'img/muneco-{name}.png')
    return rgba
if __name__=='__main__':
    S='/tmp/claude-0/-home-user/a313ded0-1d40-59bc-812f-5f47f2864937/scratchpad/'
    ims=[Image.fromarray(build(n),'RGBA') for n in VIEWS]
    sh=Image.new('RGB',(sum(i.width for i in ims),490),(30,34,40)); x=0
    for i in ims: sh.paste(i,(x,0),i); x+=i.width
    sh.save(S+'cuts-final.png')
