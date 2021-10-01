a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# funcion para multiplicar 2 listas con la funcion map

map1 = list( map(lambda x,y : x*y, a,b) )
print (map1)