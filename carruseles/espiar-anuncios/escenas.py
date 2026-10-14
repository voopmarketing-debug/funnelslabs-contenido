"""Prepara los fondos a sangre (solo foto, oscurecida) -> img/f<N>.jpg (1080x1350).
Requiere img/bg-<foto>-x4.png (ampliación de ref/fondo-*)."""
import cv2, numpy as np, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1350
# bright: brillo general; top/bot: altura (px) del degradado oscuro arriba/abajo y su fuerza; shift: 0 = muestra arriba de la foto, 1 = abajo
CFG={
 1:dict(bg='times', shift=0.55,bright=.62,top=(420,.55),bot=(820,.85)),
 2:dict(bg='metro', shift=0.5, bright=.58,top=(520,.6), bot=(760,.8)),
 9:dict(bg='cables',shift=0.5, bright=.56,top=(520,.65),bot=(720,.6)),
 10:dict(bg='aerea',shift=0.5, bright=.6, top=(420,.5), bot=(860,.88)),
}
def grad(y0,y1,H):
    return np.clip((np.arange(H,dtype=np.float32)-y0)/(y1-y0),0,1)
for n,c in CFG.items():
    im=cv2.imread(f'img/bg-{c["bg"]}-x4.png'); h,w=im.shape[:2]
    s=max(W/w,H/h); im=cv2.resize(im,(int(w*s)+1,int(h*s)+1),interpolation=cv2.INTER_AREA if s<1 else cv2.INTER_CUBIC)
    h,w=im.shape[:2]; x0=(w-W)//2; y0=int((h-H)*c['shift'])
    im=im[y0:y0+H,x0:x0+W].astype(np.float32)*c['bright']
    yy=np.arange(H,dtype=np.float32)[:,None,None]
    th,ts=c['top']; g=np.clip(1-yy/th,0,1)**1.2*ts
    bh,bs=c['bot']; g2=np.clip((yy-(H-bh))/bh,0,1)**1.2*bs
    k=np.maximum(g,g2); im=im*(1-k)+np.array([8,8,8],np.float32)*k
    # viñeta suave en las esquinas
    xx=np.linspace(-1,1,W)[None,:,None]; vy=np.linspace(-1,1,H)[:,None,None]
    v=np.clip((xx**2+vy**2)/2,0,1)*0.28; im=im*(1-v)
    im=im+np.random.default_rng(3).normal(0,2.0,im.shape[:2])[...,None]        # grano leve
    cv2.imwrite(f'img/f{n}.jpg',np.clip(im,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,95]); print('ok',n)
