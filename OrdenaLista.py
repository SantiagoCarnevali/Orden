# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	lista = [str() for ind0 in range(200)]
	print("Ingrese los nombres (enter en blanco para terminar):")
	# leer la lista
	cant = 0
	nombre = input()
	while nombre!="":
		cant = cant+1
		lista[cant-1] = nombre
		# leer un nombre y ver que no este ya en la lista
		while True:# no hay 'repetir' en python
			nombre = input()
			se_repite = False
			for i in range(1,cant+1):
				if nombre==lista[i-1]:
					se_repite = True
			if not se_repite: break
	# ordenar
	for i in range(1,cant):
		# busca el menor entre i y cant
		pos_menor = i
		for j in range(i+1,cant+1):
			if lista[j-1]<lista[pos_menor-1]:
				pos_menor = j
		# intercambia el que estaba en i con el menor que encontro
		aux = lista[i-1]
		lista[i-1] = lista[pos_menor-1]
		lista[pos_menor-1] = aux
	# mostrar como queda la lista
	print("La lista ordenada es:")
	for i in range(1,cant+1):
		print("   ",lista[i-1])

