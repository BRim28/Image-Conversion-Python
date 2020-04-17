import os
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir('images') if isfile(join('images', f))]
count = len(onlyfiles)
for i in range(count):
	stream = os.popen('dcmj2pnm images/'+onlyfiles[i]+' '+onlyfiles[i]+'.pgm')
	output = stream.read()

