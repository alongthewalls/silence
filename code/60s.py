#[ ffmpeg -f lavfi -i anullsrc -t 60s 60s.wav]
#gotta conbvert this to .py sometime

import subprocess

lib1 = "lavfi" 
lib2 = "anullsrc"
time = "60s"
output = "out/60s.wav"

hi = subprocess.run(["ffmpeg", "-f", lib1, "-i", lib2, "-t", time, output])
print(hi)