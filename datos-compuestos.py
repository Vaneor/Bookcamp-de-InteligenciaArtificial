#El primer tipo de datos compuesto que veremos sera la lista

lista = ["Vanessa Ortega", "celular 3187614455", True, 1.60]
#En el mundo de la programación no contamos del uno al diez., contamos del cero al nueve
print(lista[0])
lista[0] = "Vaneortega"
print(lista[0])

#La lista es una lista que no se puede modificar
tupla = ("huevos rancheros", "arepa", "chocolate", False, 7.30)
print(tupla[1])
#tupla[1] = "aguapanela"
#print(tupla[1])

#Creando un conjunto set
#El conjunto no adminte elementos duplicados 
conjunto = {"Vanessa Ortega", "celular 3187614455", True, 1.60, "Vanessa Ortega"}
print(conjunto)

#Creando un diccionario
diccionario = {
    "nombre": "Vanessa", 
    "apellido": "Ortega",
    "estatura": 1.60,
    "estoy feliz": True,
    "nombre": "Vanessa",
    "edad": 25
}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estoy feliz"])
print(diccionario["estatura"] + 2) #3.69