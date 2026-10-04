#[ ffmpeg -f lavfi -i anullsrc -t 60s 60s.wav]
#gotta conbvert this to .py sometime

import subprocess

filter = "lavfi" 
lib = "anullsrc"
time = "60s"
output = "out/60s.wav"

hi = subprocess.run(["ffmpeg", "-f", filter, "-i", lib, "-t", time, output])
print(hi)
