
from gimpfu import *
import os
#psd_file    = 'U:/dloveridge/_For Drew/from_Bruce/PSD_Layered_Output_TEST_v07_psd_build_info.json'
#image_files = []
#image_width = 640
#image_height = 480

psd_image = gimp.Image(image_width,image_height)
pdb.plug_in_icc_profile_apply(psd_image, "//isln-smb/aw_config/Git_Live_Code/Software/Nuke/ICC_Profiles/sRGB.icc", 0, False)

for image_file in image_files:
	layer_name = os.path.splitext(os.path.basename(image_file))[0]
	image_file = image_file.replace("\\","/")
	layer = pdb.gimp_file_load_layer(psd_image, image_file)
	layer.name = layer_name
	psd_image.add_layer(layer)

psd_folder = os.path.dirname(psd_file)
if not os.path.exists(psd_folder):
	os.makedirs(psd_folder)

pdb.file_psd_save(psd_image, None, psd_file,"", 0, 0)
gimp.delete(psd_image)

pdb.gimp_quit(1)
