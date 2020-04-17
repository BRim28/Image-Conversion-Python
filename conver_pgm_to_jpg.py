import os
from os import listdir
from os.path import isfile, join
from PIL import Image
onlyfiles = [f for f in listdir('../PGM') if isfile(join('../PGM', f))]
print(onlyfiles.remove("conver_pgm_jpg.py"))
count = len(onlyfiles)

for i in range(count):
	x=Image.open(onlyfiles[i])
	imsz=x.size
	newimg=Image.new('L',imsz)
	newimg.putdata(x.getdata())
	newimg.save(onlyfiles[i]+".jpg")


