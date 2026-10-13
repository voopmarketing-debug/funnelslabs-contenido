"""Pone cada video grabado dentro del marco de su slide y exporta slide-0N.mp4 (1080x1350).
Uso: guarda los videos en videos/ con estos nombres (mp4 o mov) y ejecuta: python3 componer-videos.py"""
import os, glob, subprocess
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLIDES={3:'shein',4:'temu',5:'mercado-libre',6:'nubank',7:'rappi',8:'nike'}
X,Y,W,H=60,668,960,540          # hueco del video dentro del marco
for n,slug in SLIDES.items():
    v=[f for f in glob.glob(f'videos/{slug}.*') if f.lower().endswith(('.mp4','.mov','.m4v','.webm'))]
    if not v: print(f'falta videos/{slug}.mp4 -> slide {n} queda con el marco vacío'); continue
    out=f'slide-{n:02d}.mp4'
    fc=f"[1:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black,setsar=1[v];[0:v][v]overlay={X}:{Y}:shortest=1,format=yuv420p"
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-i',f'slide-{n:02d}.png','-i',v[0],'-filter_complex',fc,
                    '-t','15','-r','30','-c:v','libx264','-crf','18','-preset','medium','-an','-movflags','+faststart',out],check=True)
    print('listo',out)
