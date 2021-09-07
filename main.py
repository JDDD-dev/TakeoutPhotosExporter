# importing libraries
from zipfile import ZipFile
import os
import shutil

# specifying the zip file name
ruta = os.getcwd()

os.chdir(ruta)

file_list = os.listdir()
for file_name in file_list:
	if file_name.startswith("takeout"):
		break

total_fotos = 0

erasedPhotos = 0

print("Select your language")
print("1 - English")
print("2 - Spanish")

language = input()

if (language == "1"):
	suffix = "Photos"
elif (language == "2"):
	suffix = "Fotos"
else:
	raise ValueError("Non an existing language")

os.mkdir(ruta + "/auxiliar")
os.mkdir(ruta + "/final")

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
	# printing all the contents of the zip file
	listOfFilenames = zip.namelist()

	# extracting all the files
	print('Extracting...')
	os.chdir(ruta + "/auxiliar")
	for filename in listOfFilenames:
		if filename.endswith(".jpg"):
			zip.extract(filename)
			total_fotos += 1
		elif filename.endswith(".jpeg"):
			zip.extract(filename)
			total_fotos += 1
		elif filename.endswith(".png"):
			zip.extract(filename)
			total_fotos += 1
	print('Extraction finished...')

print('Fixing directories...')
os.chdir(ruta + "/auxiliar/Takeout/Google " + suffix)
listCarpetas = os.listdir()

for carpeta in listCarpetas:
	os.chdir(ruta + "/auxiliar/Takeout/Google " + suffix + "/" + carpeta)
	print("PROCESSING DIRECTORY: " + carpeta)
	listFotos = os.listdir()
	for foto in listFotos:
		try:
			shutil.move(foto, ruta + "/final")
		except:
			erasedPhotos + 1
			os.remove(foto)
	os.chdir(ruta + "/auxiliar/Takeout/Google " + suffix)
	os.rmdir(ruta + "/auxiliar/Takeout/Google " + suffix + "/" + carpeta)

os.chdir(ruta)
os.rmdir(ruta + "/auxiliar/Takeout/Google " + suffix)
os.rmdir(ruta + "/auxiliar/Takeout")
os.rmdir(ruta + "/auxiliar")



print("Scanned Photos: " + str(total_fotos))
print("Duplicate Photos: " + str(erasedPhotos))
