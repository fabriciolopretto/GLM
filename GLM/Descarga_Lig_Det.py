"""
Decarga los archivos .nc que tienen los datos del sensor GLM
del satélite GOES-16 para la detección de actividad eléctrica
en tormentas. 
"""

# Se importan las librerias necesarias
import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc
import s3fs

# Se usan credenciales anonimas para acceder a datos publicos
fs = s3fs.S3FileSystem(anon=True)

# Lsta de contenidos del GOES-16
fs.ls('s3://noaa-goes16/')

cont = 0
# Se descarga el día 01 Enero 2024! (Los días van de 001 a 365)
dia_tex = '001'
anno_tex = '2024'
for hora in range(24):
    if 10 > hora >= 0:
        hora_tex = '0' + str(hora)
    if hora >= 10:
        hora_tex = str(hora)
    # List specific files of GOES-16 CONUS data (multiband format) on a certain hour
    files = np.array(fs.ls('noaa-goes16/GLM-L2-LCFA/'+ anno_tex +'/'+ dia_tex +'/'+ hora_tex +'/'))
    # Cada hora tiene 180 escaneos
    for j in range(180):
        # Descarga todos los archivos para esta hora, los renombra sin la estructura del directorio
        fs.get(files[j], files[j].split('/')[-1])
        cont = cont + 1
        print(cont)
    del j,hora_tex,files
del cont,hora
