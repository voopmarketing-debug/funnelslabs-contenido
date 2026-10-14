"""Compone las escenas a sangre (foto de fondo + muñeco solo) -> img/f<N>.jpg (1080x1350).
Requiere: img/muneco-<vista>.png (recortar_muneco.py) y img/bg-<foto>-x4.png (escalado de ref/fondo-*)."""
import cv2, numpy as np, os
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W,H=1080,1350
SR_PATH='/tmp/claude-0/-home-user/a313ded0-1d40-59bc-812f-5f47f2864937/scratchpad/sr/EDSR_x4.pb'
# slide: foto, vista del muñeco, alto del muñeco, y de los pies, x del centro, desplazamiento vertical del fondo (0=arriba,1=abajo), oscurecer base
CFG={
 1:dict(bg='times',  v='frontal',      h=800,feet=1290,cx=540,shift=1.0,bright=.95,floor=0.0,dark=640),
 2:dict(bg='metro',  v='perfil',       h=560,feet=1262,cx=620,shift=1.0,bright=.95,floor=0.0,dark=700),
 9:dict(bg='cables', v='tres-cuartos', h=560,feet=1262,cx=540,shift=1.0,bright=.92,floor=0.55,dark=800),
 10:dict(bg='aerea', v='trasera',      h=800,feet=1290,cx=540,shift=0.5,bright=.95,floor=0.8,dark=620),
}
def sr_voxel(v):
    out=f'img/muneco-{v}-x4.png'
    if os.path.exists(out): return Image.open(out).convert('RGBA')
    im=Image.open(f'img/muneco-{v}.png'); rgb=cv2.cvtColor(np.array(im.convert('RGB')),cv2.COLOR_RGB2BGR)
    sr=cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(SR_PATH); sr.setModel('edsr',4)
    up=cv2.cvtColor(sr.upsample(rgb),cv2.COLOR_BGR2RGB)
    a=cv2.resize(np.array(im)[...,3],(up.shape[1],up.shape[0]),interpolation=cv2.INTER_CUBIC)
    res=Image.fromarray(np.dstack([up,a]),'RGBA'); res.save(out); return res
def load_bg(n,c):
    im=cv2.imread(f'img/bg-{n}-x4.png'); h,w=im.shape[:2]
    s=max(W/w,H/h); im=cv2.resize(im,(int(w*s)+1,int(h*s)+1),interpolation=cv2.INTER_AREA if s<1 else cv2.INTER_CUBIC)
    h,w=im.shape[:2]; x0=(w-W)//2; y0=int((h-H)*c['shift'])
    im=im[y0:y0+H,x0:x0+W].astype(np.float32)*c['bright']
    if c['floor']:                       # base oscura donde no hay suelo: el muñeco se apoya en ella
        yy=np.linspace(0,1,H)[:,None,None]; k=np.clip((yy-0.80)/0.20,0,1)**1.2*c['floor']
        im=im*(1-k)+np.array([10,10,10],np.float32)*k
    yy=np.arange(H,dtype=np.float32)[:,None,None]            # degradado oscuro arriba, para el texto
    g=np.clip(1-yy/c['dark'],0,1)**1.1*0.93; im=im*(1-g)+np.array([8,8,8],np.float32)*g
    # grano leve para que el fondo ampliado no se vea liso
    return np.clip(im+np.random.default_rng(3).normal(0,2.2,im.shape[:2])[...,None],0,255)
def place(vox,c):
    a=np.array(vox)[...,3]; ys,xs=np.where(a>128); ymin,ymax,xmin,xmax=ys.min(),ys.max(),xs.min(),xs.max()
    s=c['h']/(ymax-ymin); nw,nh=int(vox.width*s),int(vox.height*s)
    v=np.array(vox.resize((nw,nh),Image.LANCZOS)).astype(np.float32)
    left=int(c['cx']-(xmin+xmax)/2*s); top=int(c['feet']-ymax*s)
    R=np.zeros((H,W,3),np.float32); A=np.zeros((H,W),np.float32)
    y0,x0=max(top,0),max(left,0); y1,x1=min(top+nh,H),min(left+nw,W)
    R[y0:y1,x0:x1]=v[y0-top:y1-top,x0-left:x1-left,2::-1]; A[y0:y1,x0:x1]=v[y0-top:y1-top,x0-left:x1-left,3]/255
    A=cv2.erode(A,np.ones((3,3),np.uint8))                    # quita el halo claro del borde
    A=cv2.GaussianBlur(A,(0,0),0.8)
    return R,A,(xmin,xmax,ymin,ymax,s,left,top)
def shadow(A,feet,cx,wd):
    sh=np.zeros((H,W),np.float32); cv2.ellipse(sh,(int(cx),int(feet)-4),(int(wd*0.55),int(wd*0.07)),0,0,360,1.0,-1)
    return cv2.GaussianBlur(sh,(0,0),16)
if __name__=='__main__':
    for n,c in CFG.items():
        vox=sr_voxel(c['v']); bg=load_bg(c['bg'],c); R,A,(xmin,xmax,ymin,ymax,s,left,top)=place(vox,c)
        sh=shadow(A,c['feet'],c['cx'],(xmax-xmin)*s)
        bg=bg*(1-0.7*sh[...,None])
        amb=bg.reshape(-1,3).mean(0); R=R*0.95+amb*0.05
        out=R*A[...,None]+bg*(1-A[...,None])
        cv2.imwrite(f'img/f{n}.jpg',np.clip(out,0,255).astype(np.uint8)[...,::-1] if False else np.clip(out,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,95])
        print('ok',n,c['v'],'alto',c['h'])
