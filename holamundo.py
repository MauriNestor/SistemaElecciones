#definicion de variables
edad = 20
nombre = 'Nestor'

#contactenar con f-strings
saludo = f'hola {nombre} como estai weon'

#contactenar con =
saludo = "hola a " + nombre +"como estas?"

#operadores de pertenencia in and not it
#print("juan" not in saludo)
#print("juan" in saludo)

#datos compuestos

lista = ['Mauricio', 28, True, '12'] #se puede modificar
tupla = ('Mauricio', 28, True, '12')  #no se puede modificar

#se puede
lista[1] = 'felipe' 
#print(lista[1])

#no se puede
#tupla[1] = 'rogelio'
#print(tupla[1])

#for elemento in lista:
 #  print(f'El elemento {elemento} es del tipo {type(elemento)}')

#creando un conjunto {set} {no almacena elementos por indice, no alamacena datos duplicados]}
conjunto = {"mauri", "nestor", True, 1.73}

#diccionario
diccionario = {
    'nombre ': "mauricio", 
    'apellido' : "apaza callapa",
    "edad" : "20",
    'es feli' : False

}
#print(diccionario['edad'])

#OPERADORES ARITMETICOS
#suma +  
#resta -  
#divisiones /   
#multuplicacion *  
#potenciacion **  
#division baja(redondeo hacia abajo) //  
#resto o modulo %

#tipo_Dato = type(param)

#OPERADORES ARTIMETICOS
# < menor q      >mayor q   <=menor o igual     >= mayor o igual    == es igual a      != es distinto 

#METODOS DE CADENAS
cadena1 = 'que onda perrito malvado'

#convertir mayuscualas
resultado = cadena1.upper()

#convertir imnusculas 
minusc = cadena1.lower()

#primera letra mayuscula 
primer_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena, sino existe devuelve -1
busqueda_find = cadena1.find('a')

#buscamaos cadena dentro de otra cadena, sino existe sale error
busqueda_index = cadena1.index('a')

#si es numerico, devuelve true, sino false
es_numerico = cadena1.isnumeric()

#es alfanumerico, true o false
es_alfa = cadena1.isalpha()

#nos dice cuantas veces se encontro conicidencias
nro_coincidencias = cadena1.count('a')

#contar cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificar si una cadena emepiza con otra cadena dad, si es asi devuelve true
empieza_con = cadena1.startswith('que')

#verificar si una cadena termina con otra cadena dad, si es asi devuelve true
termina_con = cadena1.endswith('ado')

#cambia un pedazo de la cadena dad, por otra dada
cadena_nueva = cadena1.replace('rr', 'gg')
cadena_new = cadena_nueva.capitalize()

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(' ')
#print(cadena_separada)


#METODOS LISTAS, usado para crear listas vacias
lista = list(['hola',21,'gloe'])

#cantidad de elementos de una lista
resultado = len(lista)

#agredano un elemento a la lista
agregar_elemento = lista.append(45)

#agerga un elemneto en una posicion especifica
agregar_pos = lista.insert(2, 12)

#agergar varios elementos a la lista
lista.extend([False, 12, 23])

#elminar  un elemento de la lista por el indiice
lista.pop(0)
lista.pop(-1)

#remover un elemento de la lista por su valor
lista.remove('gloe')

#eliminiando todos los elemntos de una lista
#lista.clear()

#ordenando la lista numericamene(si unsamos el parametro reverse = true lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()


print(dir(tupla))
