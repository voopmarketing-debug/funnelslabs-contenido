# Escena en marco + personajes "saliendo" de la pantalla.
# Para cada slide genera: img/b<N>.jpg (fondo del marco) e img/p<N>.png (personajes, capa con alfa).
import cv2, numpy as np, os
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1350
FX0,FX1,FB,FEET=40,1040,1255,1335          # marco: x, borde inferior; pies (salen por debajo del marco)
# bg: foto de fondo, ytop: y de la cabeza, ft: borde superior del marco
CFG={
 2:dict(bg=2,ch='silla-lado',ytop=580,ft=648,bright=.90),
 3:dict(bg=3,ch='chat',     ytop=636,ft=704,bright=.95),
 5:dict(bg=4,ch='caminando',ytop=616,ft=684,bright=.85,billboard=True),
 6:dict(bg=5,ch='modelo',   ytop=580,ft=648,bright=.95),
 4:dict(bg=1,ch='brazos',   ytop=400,ft=500,bright=.92),
 7:dict(bg=6,ch='abrazo',   ytop=400,ft=500,bright=1.0,floor=True),
}
def load_bg(n,c,w,h):
    im=cv2.imread(f'bg/orig-{n}.jpg'); hh,ww=im.shape[:2]
    im=im[6:hh-16,18:ww-18]                       # quita el margen de la captura
    if c.get('billboard'):                       # tapa el cartel blanco
        sub=(im[420:900,480:800].min(2)>225).astype(np.uint8)
        sub=cv2.dilate(sub,np.ones((21,21),np.uint8)).astype(bool)
        ring=im[400:920,460:820].reshape(-1,3)[~np.pad(sub,((20,20),(20,20)))[:520,:360].reshape(-1)]
        patch=im[420:900,480:800].astype(np.float32)
        patch[sub]=(np.median(ring,0)+np.random.default_rng(1).normal(0,3,(480,320,1)).repeat(3,2))[sub]
        im[420:900,480:800]=np.clip(cv2.GaussianBlur(patch,(0,0),2),0,255).astype(np.uint8)
    hh,ww=im.shape[:2]
    s=max(w/ww,h/hh); im=cv2.resize(im,(int(ww*s)+1,int(hh*s)+1),interpolation=cv2.INTER_AREA if s<1 else cv2.INTER_CUBIC)
    hh,ww=im.shape[:2]
    x0=(ww-w)//2; y0=hh-h                          # alineado abajo (suelo)
    im=im[y0:y0+h,x0:x0+w].astype(np.float32)*c['bright']
    if c.get('floor'):                             # suelo oscuro para pared sin piso
        yy=np.linspace(0,1,h)[:,None,None]; k=np.clip((yy-0.78)/0.22,0,1)**1.3
        im=im*(1-0.78*k)+np.array([14,12,10],np.float32)*0.78*k
    return im
# huecos de fondo que sí se quitan (centro aprox. en la foto original); el resto del negro es sombra de la ropa o del sillón y se conserva
REMOVE={'silla-lado':[(565,634),(565,927),(699,937)],'caminando':[(734,530)],'modelo':[(713,466)],'abrazo':[(613,518),(314,537)]}
EXTRA={'abrazo','silla-lado'}   # solo donde rembg pierde partes oscuras (patas del sillón); en las demás crea un halo negro
PATCH={'caminando':[[(655,830),(738,830),(728,885),(700,935),(648,935),(660,885)]]}   # pierna de atrás
def cut(c):
    a=np.array(Image.open(f'bg/cut-{c["ch"]}.png'))
    src=cv2.imread(f'img/{c["ch"]}.png').astype(np.float32)
    shape=(a[...,3]>128).astype(np.uint8)
    n,lab,st,_=cv2.connectedComponentsWithStats(shape)
    keep=np.zeros_like(shape)
    for i in range(1,n):
        if st[i,4]>2500: keep[lab==i]=1
    shape=keep
    # rembg pierde la ropa muy oscura (pierna de atrás, patas del sillón): se recupera con la foto original.
    # El fondo real es negro exacto (0), así que los huecos de verdad siguen siendo huecos.
    m=cv2.GaussianBlur(src.max(2),(0,0),0.8)
    near=cv2.dilate(shape,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(61,61)))
    extra=((m>=3.0)&(near>0)&(c['ch'] in EXTRA)).astype(np.uint8)
    extra=cv2.morphologyEx(extra,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9)))
    full=(shape|extra).astype(np.uint8)
    # huecos de fondo negro exacto dentro de la silueta
    hole=((m<2.0)&(full>0)).astype(np.uint8)
    hole=cv2.morphologyEx(hole,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(19,19)))   # solo huecos anchos; las ranuras finas son sombra
    n2,lab2,st2,_=cv2.connectedComponentsWithStats(hole)
    pk=np.zeros_like(shape)
    for i in range(1,n2):
        if st2[i,4]>=700: pk[lab2==i]=1
    full=(full&(1-cv2.dilate(pk,np.ones((5,5),np.uint8)))).astype(np.uint8)
    for poly in PATCH.get(c['ch'],[]):          # partes casi negras que ni la foto ni el recorte distinguen del fondo
        cv2.fillPoly(full,[np.array(poly,np.int32)],1)
        pm=np.zeros(full.shape,np.float32); cv2.fillPoly(pm,[np.array(poly,np.int32)],1.0)
        pm=cv2.GaussianBlur(pm,(0,0),7)[...,None]*(full[...,None]>0)       # lleva el negro de la sombra al verde oscuro de la tela, con borde suave
        src=src+pm*np.maximum(0,np.array([46,44,6],np.float32)-src)
    n3,lab3,st3,_=cv2.connectedComponentsWithStats(full)
    shape=np.zeros_like(full)
    for i in range(1,n3):
        if st3[i,4]>2500: shape[lab3==i]=1
    d_in=cv2.distanceTransform(shape,cv2.DIST_L2,3); d_out=cv2.distanceTransform(1-shape,cv2.DIST_L2,3)
    # el borde lo decide la foto original (fondo negro puro): conserva el pelo y no deja halo oscuro
    key=cv2.GaussianBlur(np.clip((src.max(2)-7)/16,0,1),(0,0),0.6)
    band=np.where(d_in>6,1.0,np.where(d_out<6,key,0.0))
    al=cv2.GaussianBlur(band.astype(np.float32),(0,0),0.6)
    rgb=np.where((al<0.98)[...,None],src/np.clip(al,0.65,1)[...,None],src)
    return np.clip(rgb,0,255),al
def place(rgb,al,c):
    ys,xs=np.where(al>.5); ymin,ymax,xmin,xmax=ys.min(),ys.max(),xs.min(),xs.max()
    s=(FEET-c['ytop'])/(ymax-ymin); top=int(c['ytop']-ymin*s); left=int(W/2-(xmin+xmax)/2*s)
    nw,nh=int(rgb.shape[1]*s),int(rgb.shape[0]*s); itp=cv2.INTER_AREA if s<1 else cv2.INTER_CUBIC
    rgb=cv2.resize(rgb,(nw,nh),interpolation=itp); al=cv2.resize(al,(nw,nh),interpolation=itp)
    R=np.zeros((H,W,3),np.float32); A=np.zeros((H,W),np.float32)
    y0,x0=max(top,0),max(left,0); y1,x1=min(top+nh,H),min(left+nw,W)
    R[y0:y1,x0:x1]=rgb[y0-top:y1-top,x0-left:x1-left]; A[y0:y1,x0:x1]=al[y0-top:y1-top,x0-left:x1-left]
    print(c['ch'],'escala',round(s,2),'alto',round((ymax-ymin)*s),'ancho',round((xmax-xmin)*s))
    return R,A
for n,c in CFG.items():
    fw,fh=FX1-FX0,FB-c['ft']
    bg=load_bg(c['bg'],c,fw,fh); cv2.imwrite(f'img/b{n}.jpg',np.clip(bg,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,93])
    rgb,al=cut(c); R,A=place(rgb,al,c)
    R=R*0.94+bg.reshape(-1,3).mean(0)*0.06      # un toque del color del ambiente
    out=np.dstack([np.clip(R,0,255).astype(np.uint8)[...,::-1],np.clip(A*255,0,255).astype(np.uint8)])
    Image.fromarray(out,'RGBA').save(f'img/p{n}.png')
