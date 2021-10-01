import cv2
import numpy as np

  
# seleccionar captura de camara.
cap = cv2.VideoCapture(0)

# inicializamos el loop 
while(1): 
  
    # funcion para leer fotogramas de camara
    ret, frame = cap.read() 
   # funcion para convertir espacio de color BGR a hsv 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 


# funcion para buscar los bordes
    edged = cv2.Canny(hsv, 50, 200)
    cv2.imshow('1 - Canny Edges', edged)
    cv2.waitKey(0)

# funcion para encontrar los contornos e imprimir cuantos hay
    contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print ("Number of contours found = ", len(contours))



cv2.destroyAllWindows()
