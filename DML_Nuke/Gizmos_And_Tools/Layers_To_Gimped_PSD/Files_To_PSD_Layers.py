
from gimpfu import *
import os
#psd_file    = 'U:/dloveridge/_For Drew/from_Bruce/PSD_Layered_Output_TEST_v07_psd_build_info.json'
#image_files = []
#image_width = 640
#image_height = 480

psd_image = gimp.Image(image_width,image_height)

for image_file in image_files:
	layer_name = os.path.splitext(os.path.basename(image_file))[0]
	image_file = image_file.replace("\\","/")
	layer = pdb.gimp_file_load_layer(psd_image, image_file)
	layer.name = layer_name
	psd_image.add_layer(layer)

pdb.file_psd_save(psd_image, None, psd_file,"", 0, 0)
gimp.delete(psd_image)

pdb.gimp_quit(1)
