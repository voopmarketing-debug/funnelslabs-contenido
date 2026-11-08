"""Pieza 5: cambia SOLO la pared rosada de ref/pieza5-frambuesa.webp a verde olivo (luz y sombra originales) -> img/p5-frambuesa.png (bordes difuminados al verde)"""
import numpy as np, cv2, os
from PIL import Image
from rembg import remove, new_session
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SR='/tmp/claude-0/-home-user/a313ded0-1d40-59bc-812f-5f47f2864937/scratchpad/sr/EDSR_x4.pb'
im=Image.open('ref/pieza5-frambuesa.webp').convert('RGB'); src=cv2.cvtColor(np.array(im),cv2.COLOR_RGB2BGR)
sr=cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(SR); sr.setModel('edsr',4)
big=sr.upsample(src); H,W=big.shape[:2]
al=np.array(remove(Image.fromarray(cv2.cvtColor(big,cv2.COLOR_BGR2RGB)),session=new_session('u2net')))[...,3]>128
n,lab,st,_=cv2.connectedComponentsWithStats(al.astype(np.uint8)); cake=(lab==(np.argmax(st[1:,4])+1)).astype(np.uint8)
cake=cv2.morphologyEx(cake,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
pm=cv2.GaussianBlur(cake.astype(np.float32),(0,0),2.2)[...,None]
lab=cv2.cvtColor(big,cv2.COLOR_BGR2LAB).astype(np.float32)
Lm=lab[...,0][cake==0].mean()
tgt=cv2.cvtColor(np.uint8([[[53,74,62]]]),cv2.COLOR_BGR2LAB)[0,0].astype(np.float32)     # #3E4A35
new=lab.copy(); new[...,0]=tgt[0]+(lab[...,0]-Lm)*0.9; new[...,1]=tgt[1]; new[...,2]=tgt[2]
rec=cv2.cvtColor(np.clip(new,0,255).astype(np.uint8),cv2.COLOR_LAB2BGR).astype(np.float32)
out=np.clip(big.astype(np.float32)*pm+rec*(1-pm),0,255).astype(np.uint8)
# alfa: bordes que se funden con el verde de la slide
a=np.ones((H,W),np.float32); F=int(W*0.14)
for i in range(F):
    t=(i/F)**1.2; a[i,:]=np.minimum(a[i,:],t); a[:,i]=np.minimum(a[:,i],t); a[:,W-1-i]=np.minimum(a[:,W-1-i],t); a[H-1-i,:]=np.minimum(a[H-1-i,:],t)
a=cv2.GaussianBlur(a,(0,0),8)
cv2.imwrite('img/p5-frambuesa.png',np.dstack([out,(a*255).astype(np.uint8)]))
cv2.imwrite('/tmp/claude-0/-home-user/a313ded0-1d40-59bc-812f-5f47f2864937/scratchpad/p5-prev.png',cv2.resize(out,(W//4,H//4)))
