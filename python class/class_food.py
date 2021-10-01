class Alimento:
	def __init__ (self, producto):
		self.articulo= producto.capitalize ()

	def alimentar (self):
			print (f" voy a comer {self.articulo}" )
			
	def prohibir (self):
			print (f"no me alimento de {self.articulo}" )


class Salados(Alimento):
	def __init__ (self, producto):
		self.articulo= producto.capitalize ()
		
		
	def degustar (self):
		print (f"el {self.articulo} es salado" )

	
class Agrio(Alimento):
	def __init__ (self, producto):
		self.articulo= producto.capitalize ()
	def astringente (self):
		print (f"el {self.articulo} es astringente" )
			
	def degustar (self):
		print (f"el {self.articulo} es agrio" )
	
class Dulce(Alimento):
	def __init__ (self, producto):
		self.articulo= producto.capitalize ()
		
		
	def degustar (self):
		print (f"el {self.articulo} es astringente" )

		
		
		
objeto_1= Salados ("salamin")
objeto_1.degustar ()	
objeto_1.alimentar  () 
objeto_1.prohibir  ()

objeto_2=Dulce ("chocolate")
objeto_2.prohibir ()
objeto_2.degustar ()

objeto_3= Alimento ("limon")
objeto_3.alimentar ()
objeto_3.prohibir ()

objeto_4 = Agrio ("helado limon")
objeto_4.degustar ()
objeto_4.astringente ()



	
		


