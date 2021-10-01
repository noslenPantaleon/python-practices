
horario= []
cursos = {"Buenosaires":
						{
				"matematicas":
						{"aula":1,
						"usuario":1,
						"horario":horario,
						"Ingreso":False
						},
				"fisica":
						{"aula":2,
						"usuario":2,
						"horario":horario,
						"Ingreso":False
						},
				"quimica":
						{"aula":3,
						"usuario":4,
						"horario":horario,
						"Ingreso":False
						}
						},
						
						
		"Madrid":
						{
				"matematica":
						{"aula":4,
						"usuario":4,
						"horario":horario,
						"Ingreso":False
						},
				"fisica":
						{"aula":5,
						"usuario":5,
						"horario":horario,
						"Ingreso":False
						},
				"quimica":
						{"aula":6,
						"usuario":6,
						"horario":horario,
						"Ingreso":False
						}
						},
						}
						

while True:


	ingreso = input("Ingrese nombre: ").capitalize()

	ref = cursos["Madrid"]			
				
	print(f"Bienvenido {ingreso} Su aula es #{ref['Sister']}" )
	 
	#print(([key for key in cursos.keys()][1], [value for value in cursos.values()][1]))


