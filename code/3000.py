from PIL import Image

mode = "1" #"RGB"
res = (3000, 3000)
color = 0 #(255, 0, 0)

yo = Image.new(mode,res,color)
yo.save('out/3000x3000 - BLACK.png')