lista=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
dic={}


for lugar, dato in enumerate(lista):
	print (lugar, dato)
	dic[lugar]=dato
# print (dic)

# print (dic[9])

print (dic[0])


print(dic.keys())
print(dic.values())

print  (lista[8])

print (f"{lista[8]} este es la posicion 8")
