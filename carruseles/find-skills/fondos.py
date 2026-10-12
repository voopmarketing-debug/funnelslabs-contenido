# Compone los personajes (recortes bg/cut-*.png) sobre las fotos de fondo (bg/orig-*.jpg)
# y deja un fondo 1080x1350 por slide en img/f<N>.jpg
import cv2, numpy as np, os
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1350
# slide: (fondo, personaje, y0 del recorte original, ancho, top, dx, ajustes del fondo)
CFG={
 1:dict(bg=1,ch='brazos',   y0=194,w=860,top=404,dx=0, shift=0.0,bright=.92),
 2:dict(bg=2,ch='silla-lado',y0=232,w=628,top=662,dx=0,shift=1.0,bright=.90),
 3:dict(bg=3,ch='chat',     y0=172,w=545,top=720,dx=0, shift=1.0,bright=.95),
 5:dict(bg=4,ch='caminando',y0=227,w=554,top=744,dx=0, shift=1.0,bright=.85,billboard=True),
 6:dict(bg=5,ch='modelo',   y0=171,w=585,top=690,dx=0, shift=1.0,bright=.95),
 7:dict(bg=6,ch='abrazo',   y0=72, w=744,top=430,dx=0, shift=0.0,bright=1.0,floor=True),
}
def load_bg(n,c):
    im=cv2.imread(f'bg/orig-{n}.jpg'); h,w=im.shape[:2]
    im=im[4:h-14,16:w-4]            # quita el margen de la captura
    if c.get('billboard'):          # tapa el cartel blanco
        h,w=im.shape[:2]
        sub=(im[420:900,480:800].min(2)>225).astype(np.uint8)
        sub=cv2.dilate(sub,np.ones((21,21),np.uint8)).astype(bool)
        ring=im[400:920,460:820].reshape(-1,3)[~np.pad(sub,((20,20),(20,20)))[:520,:360].reshape(-1)]
        col=np.median(ring,0)
        noise=np.random.default_rng(1).normal(0,3,(480,320,1))
        patch=im[420:900,480:800].astype(np.float32)
        patch[sub]=(col+noise.repeat(3,2))[sub]
        im[420:900,480:800]=np.clip(cv2.GaussianBlur(patch,(0,0),2),0,255).astype(np.uint8)
    h,w=im.shape[:2]
    s=max(W/w,H/h); im=cv2.resize(im,(int(w*s)+1,int(h*s)+1),interpolation=cv2.INTER_AREA if s<1 else cv2.INTER_CUBIC)
    h,w=im.shape[:2]
    x0=(w-W)//2; y0=int((h-H)*c['shift'])   # shift=1 -> alinea abajo (suelo), 0 -> arriba
    im=im[y0:y0+H,x0:x0+W].astype(np.float32)*c['bright']
    if c.get('floor'):              # suelo oscuro para pared sin piso
        yy=np.linspace(0,1,H)[:,None,None]
        k=np.clip((yy-0.80)/0.20,0,1)**1.3
        im=im*(1-0.78*k)+np.array([14,12,10],np.float32)*0.78*k
    return im
def cut(c):
    a=np.array(Image.open(f'bg/cut-{c["ch"]}.png'))
    rgb=a[...,2::-1].astype(np.float32); al=a[...,3].astype(np.float32)/255
    al=np.clip((al-.25)/.6,0,1)                        # quita velos débiles
    al=cv2.erode(al,np.ones((3,3),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats((al>.3).astype(np.uint8))
    keep=np.zeros_like(al)
    for i in range(1,n):
        if st[i,4]>2500: keep[lab==i]=1
    al=cv2.GaussianBlur(al*cv2.dilate(keep,np.ones((5,5),np.uint8)),(0,0),0.8)
    return rgb,al
def place(rgb,al,c):
    s=c['w']/rgb.shape[1]
    nw,nh=int(rgb.shape[1]*s),int(rgb.shape[0]*s)
    rgb=cv2.resize(rgb,(nw,nh),interpolation=cv2.INTER_AREA); al=cv2.resize(al,(nw,nh),interpolation=cv2.INTER_AREA)
    left=(W-c['w'])//2+c['dx']; top=int(c['top']-c['y0']*s)
    R=np.zeros((H,W,3),np.float32); A=np.zeros((H,W),np.float32)
    ys0,xs0=max(top,0),max(left,0); ys1,xs1=min(top+nh,H),min(left+nw,W)
    R[ys0:ys1,xs0:xs1]=rgb[ys0-top:ys1-top,xs0-left:xs1-left]; A[ys0:ys1,xs0:xs1]=al[ys0-top:ys1-top,xs0-left:xs1-left]
    return R,A
def shadow(A):
    ys,xs=np.where(A>.5); yb=ys.max(); h=110
    band=A[yb-h:yb+1].copy(); band[:h-55]=0                 # solo la zona de los zapatos
    band=np.flipud(band); sq=cv2.resize(band,(W,int(band.shape[0]*.22)))
    sh=np.zeros_like(A); y=yb-8
    sh[y:y+sq.shape[0],:]=sq[:H-y]
    sh=cv2.GaussianBlur(sh,(0,0),11)
    wide=cv2.GaussianBlur(A[yb-30:yb+1].max(0,keepdims=True).repeat(40,0),(0,0),20)  # sombra ancha suave
    big=np.zeros_like(A); big[yb-6:yb+34]=wide[:,:]
    return np.clip(sh*1.1+big*.5,0,.7)
for n,c in CFG.items():
    bg=load_bg(c['bg'],c); rgb,al=cut(c); R,A=place(rgb,al,c)
    sh=shadow(A)[...,None]
    bg=bg*(1-sh*0.85)
    # un poco del color ambiente sobre el personaje, para que no se vea pegado
    amb=bg.reshape(-1,3).mean(0)
    R=R*0.93+amb*0.07
    out=R*A[...,None]+bg*(1-A[...,None])
    cv2.imwrite(f'img/f{n}.jpg',np.clip(out,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,95])
    print('ok',n)
