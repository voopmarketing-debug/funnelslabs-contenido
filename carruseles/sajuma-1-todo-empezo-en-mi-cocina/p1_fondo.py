"""Pieza 1: cambia SOLO la pared rosada de ref/pieza1-cupcake-mano.png a verde olivo (luz y sombras originales) -> img/p1-fondo.jpg"""
import numpy as np, cv2, os
from PIL import Image
from rembg import remove, new_session
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SR='/tmp/claude-0/-home-user/a313ded0-1d40-59bc-812f-5f47f2864937/scratchpad/sr/EDSR_x4.pb'
src=cv2.imread('ref/pieza1-cupcake-mano.png'); h,w=src.shape[:2]
# pedestal (GrabCut con semillas)
m=np.full((h,w),cv2.GC_BGD,np.uint8); m[520:722,60:455]=cv2.GC_PR_BGD
m[538:566,78:420]=cv2.GC_PR_FGD; m[545:560,100:160]=cv2.GC_FGD; m[575:705,205:340]=cv2.GC_PR_FGD
m[540:560,160:360]=cv2.GC_FGD; m[600:690,225:290]=cv2.GC_FGD; m[582:665,90:200]=cv2.GC_BGD; m[582:640,360:410]=cv2.GC_BGD; m[705:722,60:455]=cv2.GC_BGD
cv2.grabCut(src,m,None,np.zeros((1,65)),np.zeros((1,65)),8,cv2.GC_INIT_WITH_MASK)
st=((m==cv2.GC_FGD)|(m==cv2.GC_PR_FGD)).astype(np.uint8)
n,lab,s,_=cv2.connectedComponentsWithStats(st); st=(lab==(np.argmax(s[1:,4])+1)).astype(np.uint8)
st[582:672,:205]=0; st[590:668,290:]=0; st[578:590,300:]=0
st=cv2.morphologyEx(st,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8)); st=cv2.morphologyEx(st,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
sr=cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(SR); sr.setModel('edsr',4)
big=sr.upsample(src); H,W=big.shape[:2]; f=4
yy,xx=np.mgrid[0:H,0:W]
hsv=cv2.cvtColor(big,cv2.COLOR_BGR2HSV).astype(np.float32); Sg=cv2.GaussianBlur(hsv[...,1],(0,0),2)
hand=((Sg>70)&(yy<170*f)&(xx>110*f)&(xx<345*f)).astype(np.uint8)
n,lab,s,_=cv2.connectedComponentsWithStats(hand); hand=(lab==(np.argmax(s[1:,4])+1)).astype(np.uint8)
crumbs=((Sg>95)&(yy>=170*f)&(yy<345*f)&(xx>200*f)&(xx<370*f)).astype(np.uint8)
cup=(np.array(remove(Image.fromarray(cv2.cvtColor(big,cv2.COLOR_BGR2RGB)),session=new_session('u2net')))[...,3]>128).astype(np.uint8); cup[:300*f]=0
stand=cv2.resize(st,(W,H),interpolation=cv2.INTER_NEAREST)
jar=np.zeros((H,W),np.uint8); jar[398*f:650*f,414*f:]=1
prot=cv2.dilate(hand,np.ones((13,13),np.uint8))|cv2.dilate(crumbs,np.ones((7,7),np.uint8))|cv2.dilate(cup,np.ones((5,5),np.uint8))|cv2.dilate(stand,np.ones((5,5),np.uint8))|jar
prot[648*f:]=1
pm=cv2.GaussianBlur(prot.astype(np.float32),(0,0),2.5)[...,None]
lab=cv2.cvtColor(big,cv2.COLOR_BGR2LAB).astype(np.float32)
wall=(prot==0)&(Sg>30); Lm=lab[...,0][wall].mean()
tgt=cv2.cvtColor(np.uint8([[[53,74,62]]]),cv2.COLOR_BGR2LAB)[0,0].astype(np.float32)   # #3E4A35
new=lab.copy(); new[...,0]=tgt[0]+(lab[...,0]-Lm)*0.9; new[...,1]=tgt[1]; new[...,2]=tgt[2]
rec=cv2.cvtColor(np.clip(new,0,255).astype(np.uint8),cv2.COLOR_LAB2BGR).astype(np.float32)
out=np.clip(big.astype(np.float32)*pm+rec*(1-pm),0,255).astype(np.uint8)
y0=60*f; hh=int(W*1350/1080); crop=cv2.resize(out[y0:y0+hh],(1080,1350),interpolation=cv2.INTER_AREA)
cv2.imwrite('img/p1-fondo.jpg',crop,[cv2.IMWRITE_JPEG_QUALITY,95])
