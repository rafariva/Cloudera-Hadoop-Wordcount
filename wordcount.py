import sys
import os
import time

def remove_special(palabra):
	caracteres = ["\xe2\x80\x9d","\xe2\x80\x9c","?","(",")","!",".",",","\r","\n",";","*","_"]
	for caracter  in caracteres:
		palabra = palabra.replace(caracter,"")

	return palabra.lower()


start_time = time.time()
try:
	archivo = sys.argv[1]
except Exception:
	exit("No file args")

if not os.path.isfile(archivo):
	print("archivo no existe")
else:
	archivo = open(archivo)
	print("leyendo archivo...")
end_time = time.time()
load_time = end_time - start_time

pal_dict = {}

start_time = time.time()
for linea in archivo:
	linea = linea.replace("--"," ")
	palabras = linea.split(" ")
	for palabra in palabras:
		palabra = remove_special(palabra)
		pal_dict[palabra] = pal_dict.get(palabra,0)+1

end_time = time.time()
running_time = end_time - start_time

print("Palabras: ",pal_dict)
print("Cantidad de palabras unicas:",len(pal_dict))
print("Tiempo de carga: ",load_time)
print("Tiempo de Ejecucion: ",running_time)
