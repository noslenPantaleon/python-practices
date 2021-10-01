
import cv2  
import numpy as np 
  
  
# seleccionar captura de camara.
cap = cv2.VideoCapture(0) 
  
  
# inicializamos el loop
while(1): 
  
    # leemos los fotogramas de la camara 
    ret, frame = cap.read() 
  
    # convertimos a colores hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
      
    # definimos un rango de color usando un array de numpy
    lower_green = np.array([65,60,60])
    upper_green = np.array([80,255,255]) 
      
  
    # creamos un umbral de la imagen 
    mask = cv2.inRange(hsv, lower_green, upper_green) 
  
    # Bitwise-AND mascara
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # Values below 127 goes to 0 (black, everything above goes to 255 (white)
    ret,thresh1 = cv2.threshold(res, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('1 Threshold Binary', thresh1)

  
    # Display edges in a frame 
    cv2.imshow('res',res) 
  
  
 
    # # funcion para buscar los contornos de la  imagen
    # edges = cv2.Canny(frame,100,200) 
  
    # # mostramos los bordes en pantalla
    # cv2.imshow('Edges',edges) 
  
  
    # cerramos el programa con la tecla Esc 
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
  
# cerrar ventana
cap.release() 
  
# Desasignar cualquier uso de memoria asociado 
cv2.destroyAllWindows()  
