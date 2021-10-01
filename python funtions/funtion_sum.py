



def sumador(n):
    def sumar_mas(x):
        return n + x
    return sumar_mas	# el regreso de la función sumador es la llamada a sumar_mas


valor_agregado_5 = sumador(5)(10)(5)
print(valor_agregado_5)#SALIDA: 15

valor_agregado_6 = sumador(6)
print(valor_agregado_6(10))#SALIDA: 16
