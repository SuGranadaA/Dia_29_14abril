#Importamos las librerías necesarias para el ejercicio
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from skimage.transform import swirl
from skimage import exposure
from skimage.transform import rotate

#Leemos la imágen
im1 = imread('gatito.png')

#Cambiamos la exposición de la imágen para hacerla más luminosa o más oscura
luz = exposure.adjust_gamma(im1, gamma=0.15,gain=1)
oscuridad = exposure.adjust_gamma(im1, gamma=3.0,gain=1)

#Pegamos juntas las imágenes
plt.subplot(131), imshow(im1)
plt.title('ORIGINAL')#Mostramos la imágen original ´para comparar el cambio
plt.subplot(132),imshow(luz)
plt.title('LUZ')
plt.subplot(133),imshow(oscuridad)
plt.title('OSCURIDAD')

#Guardamos el documento como PNG
plt.savefig("RESgatito.png")

#Cerramos la imágen
plt.close()

#Leemos la imágen
im2 = imread('gatitol.png')

#Establecemos la operación para rotar la imágen
nueva = rotate(im2, angle=20)

#Pegamos juntas las imágenes
plt.subplot(121), imshow(im2)
plt.title('RGB') 
plt.subplot(122), imshow(nueva)
plt.title('ROTADA 20°')

#Guardamos el documento como PNG
plt.savefig("RESgatitol.png")

#Cerramos el archivo
plt.close()