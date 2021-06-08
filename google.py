# importing required modules
from zipfile import ZipFile
import os, glob
import shutil

# specifying the zip file name
file_name = "file_path"
total_fotos = 0

ruta = "root_directory"

os.chdir(ruta)
os.mkdir(ruta + "/auxiliar")
os.mkdir(ruta + "/final")

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
	# printing all the contents of the zip file
	listOfFilenames = zip.namelist()

	# extracting all the files
	print('Extrayendo...')
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
	print('Fin Extraccion...')

print('Arreglando directorios...')
os.chdir(ruta + "/auxiliar/Takeout/Google Fotos")
listCarpetas = os.listdir()

for carpeta in listCarpetas:
	os.chdir(ruta + "/auxiliar/Takeout/Google Fotos/" + carpeta)
	print("PROCESANDO CARPETA CON NOMBRE: " + carpeta)
	listFotos = os.listdir()
	for foto in listFotos:
		try:
			shutil.move(foto, ruta + "/final")
		except:
			os.remove(foto)
	os.chdir(ruta + "/auxiliar/Takeout/Google Fotos")
	os.rmdir(ruta + "/auxiliar/Takeout/Google Fotos/" + carpeta)

os.chdir(ruta)
os.rmdir(ruta + "/auxiliar/Takeout/Google Fotos")
os.rmdir(ruta + "/auxiliar/Takeout")
os.rmdir(ruta + "/auxiliar")



print("El total de fotos procesadas es de: " + str(total_fotos))
