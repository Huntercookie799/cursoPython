
#Concatenacion de caracteres

mensaje = "Hola"
mensaje += " "
mensaje += "Angel"
print(mensaje)

print("\nConcatenacion:")
mensaje1 = "Hola"
mensaje2 = " "
mensaje3 = "Angel"
print(mensaje1+mensaje2+mensaje3)

print("\nSuma [conc + num]:")
suma = 1 + 2
print("La suma es: " + str(suma))

#Busqueda de caracteres
print("\nPosicion de cadena:")
mensaje = "Hola angel"
buscar_subcadena = mensaje.find("angel")
print(buscar_subcadena)

#Extracion de cadenas
print("\nExtracion de cadena:")
mensaje = "Hola angel"
buscar_subcadena = mensaje[0:4]
print(buscar_subcadena)

#Comparacion de cadena
print("\nComparacion de cadena:")
mensaje_1 = "Hola"
mensaje_2 = "Hol2"
print(mensaje_1 == mensaje_2)
