# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:50:02 2022

@author: COEP
"""

#Importamos las librerias para el manejo de archivos
import os
import random
from shutil import copyfile
import shutil

#Colocar el nombre del directorio
dir = "all_images_old"
#Colocar el nombre de nuestra clase (No usar espacios)
name_class="CSeguridad"

count = 0
list_files=os.listdir(dir)
new_dir=dir+"_rename"

if not os.path.exists(new_dir):
    os.makedirs(new_dir)     
else :
    shutil.rmtree(new_dir)
        
for filename in list_files:
    if filename.endswith(".jpg"):
        new_name=name_class+'_'+str(count)+ '.'+ filename.split('.')[-1]
        copyfile( os.path.join(dir, filename),os.path.join(new_dir, new_name ) )
        #print(filename,"-->" , new_name)
        count += 1
print("Archivosx JPG totales", count)