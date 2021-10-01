
# diccionario a analizar
    
rack= {
  "lights": {
    "light1": True,
    "light2": True,
    "light3": False,
    "light4": False
  },
  
  "coolers": {
    "coolers1": True,
    "coolers2": True,
    "coolers3": True,
    "coolers4": True
  },
  "waterpumps": {
    "waterpumps1": True,
    "waterpumps2": False,    
  }   
}


#extraemos la clave y valor de la posicion 0 que corresponde a lights en el diccionario y quedara alamacenada en tupla 

lights= (([key for key in rack.keys()][0], [value for value in rack.values()][0]))

print (lights)
print( '-' * 80) 

lights_dict= lights[1]#dentro la tupla hay un diccionario, con este metodo buscamos la siguiente clave [1] y entramos a diccionario lights

print (lights_dict)	
print( '-' * 80)



#extraemos las claves del diccionario lights_dict
for keydata in lights_dict.keys():

	print (keydata)
print( '-' * 80)
	 


#extraemos los valores del diccionario lights_dict
for valuedata in lights_dict.values():
	print ( valuedata)
	
print( '-' * 80)



#extraemos la clave y valor del diccionario lights_dict y enumeramos cada elemento
for key, value in enumerate (lights_dict.items()):
	lights_data= key, value
	print (lights_data )

print( '-' * 80)

#extraemos la clave y valor del diccionario rack y enumeramos cada elemento

for key, value in(rack.items()):
	data= key, value	
	print (data)
print( '-' * 80)


#extraemos todas las primeras claves del diccionario rack
for data in rack:	
	rackdata= data
	print (rackdata)

print( '-' * 80)	
					

#extraemos la cantidad de keys principales
			
for i in range(len(rack)):
	print(i)

print( '-' * 80)   


#extraemos los items del diccionario rack y guardamos en tuplas
		
for data in rack.items():	
	rackdata= data					#guardamos items en tuplas que devuelve la funcion items()	  		
	dicdata= rackdata[1] 			#entramos a la tupla y selecionamos el dato de la posicion 2 que corresponde a un diccionario
		
print( '-' * 80) 	


# buscar a traves del nombre del key el valor generando nuevas variables
			 
             
lights = rack["lights"]   			#buscamos dentro del diccionario rack y guardamos el diccionario que esta adentro de la clave lights en nuevo diccionario
light1= (lights['light1'] ) 		#buscamos el valor de la key light1 dentro del diccionario lights
light2= (lights['light2'] )
light3= (lights['light3'] )
light4= (lights['light4'] )



coolers = rack["coolers"]   			#buscamos dentro del diccionario rack y guardamos el diccionario que esta adentro de la clave lights en nuevo diccionario
coolers1= (coolers['coolers1'] ) 		#buscamos el valor de la key light1 dentro del diccionario lights
coolers2= (coolers['coolers2'] )
coolers3= (coolers['coolers3'] )
coolers4= (coolers['coolers4'] )


print (light1,light2,light3,light4)
print( '-' * 80)


if light1:							#si el valor es True envia mensaje para encender luces
	print ("light1_on")
else:
	print ("light1 off")        
             
print( '-' * 80)



if coolers1:							#si el valor es True envia mensaje para encender luces
	print ("cooler1_on")
else:
	print ("cooler1 off")        
             
print( '-' * 80)



