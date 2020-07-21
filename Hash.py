from tda_tabla_hash import crear_tabla, agregar_ta, agregar_tc, quitar_ta, quitar_tc, buscar_tc, buscar_ta
from tda_tabla_hash import cantidad_ta, cantidad_tc, hash_division, hash_diccionario, bernstein, barrido_ta
from tda_tabla_hash import barrido_tc, hash_guia_division, hash_catedra_division, bernstein_contactos
from tda_tabla_hash import hash_troopers_division, bernstein_SW, bernstein_pokemones, bernstein_palabra
from tda_tabla_hash import hash_pokemon_division,bernstein_catedra,bernstein_troopers,desifrar,hash_cifrado
from tda_lista import Lista,insertar,eliminar,tamanio,busqueda_lista,barrido_lista
from random import randint, choice
from math import sqrt
from time import sleep


#Ej 1. Desarrollar un algoritmo que permita implementar una tabla hash para representar un
#diccionario que permita resolver las siguientes actividades:
#a. agregar una palabra y su significado al diccionario;
#b. determinar si una palabra existe y mostrar su significado;
#c. borrar una palabra del diccionario;
'''
class Palabra(object):
    def __init__(self,palabra,significado):
        self.palabra = palabra
        self.significado = significado

    def __str__(self):
        return '- ' + self.palabra + ': ' + self.significado

tabla = crear_tabla(28)
# A
dato = Palabra('Zapato', 'Calzado que cubre total o parcialmente el pie sin sobrepasar el tobillo')
agregar_ta(tabla, hash_diccionario, dato, 'palabra')
dato = Palabra('Aro', 'Pieza u objeto, generalmente de material rígido, en forma de circunferencia.')
agregar_ta(tabla, hash_diccionario, dato, 'palabra')
dato = Palabra('Contraseña', 'Palabra, frase o señal que solo conocen determinadas personas y que les permite ser reconocidas entre sí o por otras personas.')
agregar_ta(tabla, hash_diccionario, dato, 'palabra')
dato = Palabra('Cancion','Composición literaria, generalmente en verso, a la que se le pone música para ser cantada.')
agregar_ta(tabla,hash_diccionario,dato,'palabra')
sleep(1)
print('Mostrando palabras guardadas...')
barrido_ta(tabla)
print()
# B
pos = buscar_ta(tabla, hash_diccionario, Palabra('Zapato',''), 'palabra')
if pos is not None:
    print('La palabra existe \n', pos.info)
else:
    print('La palabra no fue encontrada.')
# C
pos = buscar_ta(tabla, hash_diccionario, Palabra('Aro',''), 'palabra')
if pos is not None:
    print('- La palabra '+ pos.info.palabra + ' ha sido eliiminada.')
    quitar_ta(tabla, hash_diccionario, Palabra('Aro',''), 'palabra')
else:
    print('La palabra no fue encontrada.')
print()
print('Elementos de la tabla:')
barrido_ta(tabla)
'''
#Ej 2. Desarrollar un algoritmo que implemente una tabla hash para una guía de teléfono, 
# los datos que se conocen son número de teléfono, apellido, nombre y dirección de la persona.
# El campo clave debe ser el número de teléfono.
'''
class Guia(object):
    def __init__(self, numero, apellido, nombre, direccion):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return self.apellido + " " + self.nombre + ": numero " + str(self.numero) + "\n- Vive en " + self.direccion

tabla = crear_tabla(20)

dato = Guia(3442458080, 'Messi', 'Lionel', 'Albuquerque 123')
agregar_ta(tabla, hash_guia_division, dato, 'numero')
dato = Guia(3446654321, 'Fernandez', 'Guillermo', 'Albuquerque 572')
agregar_ta(tabla, hash_guia_division, dato, 'numero')
dato = Guia(3224669900, 'Clark', 'Tomás', 'Albuquerque 1528')
agregar_ta(tabla, hash_guia_division, dato, 'numero')
dato = Guia(3442454455, 'Fazzio', 'Fernando', 'Albuquerque 741')
agregar_ta(tabla, hash_guia_division, dato, 'numero')
dato = Guia(3213556677, 'Gutti', 'Walter', 'Nuevo Mexico 1068')
agregar_ta(tabla, hash_guia_division, dato, 'numero')
print('Datos de la Guia:')
barrido_ta(tabla)
print()
'''
#Ej 3. Implementar un tabla hash cerrada para guardar las cátedras de una carrera universitaria
#de acuerdo a su código, que permita resolver las siguientes actividades:
#a. cargar cátedras de una carrera de las cuales se conoce nombre, modalidad (anual
#o cuatrimestral), cantidad de horas;
#b. además se deben poder agregar los docentes vinculados con las cátedras;
#c. debe ser una tabla cerrada;
#d. debe poder solucionar las colisiones;
#e. no podrán estar cargadas de manera correlativa de acuerdo a un número.

'''
class Catedra(object):
    def __init__(self,codigo,nombre,modalidad,c_horas,docente):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modalidad
        self.c_horas = c_horas
        self.docente = docente

    def __str__(self):
        return 'Codigo= ' +str(self.codigo) + ' | Nombre materia: ' + self.nombre + ', La materia es ' + self.modalidad + ', Cant. de horas: ' + str(self.c_horas) + '; Docente: ' + self.docente

tabla = crear_tabla(30)

materias = ['Algorimtos y Estr. de Datos','Base de Datos','Prog. Orientada a Objetos','Fundamentos de Computacion','Mat. Discreta']
modalidad = ['Anual', 'Cuatrimestral']
profe = ['Lic. Carmona', 'Prof. Gutierrez', 'Lic. Perez', 'Ing. Nuñez','Ing. Sosa','Lic. Gandhi']
hora_anual = [80,90,100,120,140,160,190]
hora_cua = [30,40,50,60]

def universidad(tabla):
    for i in range(len(materias)):
        nom= choice(materias)
        materias.remove(nom)
        mod = choice(modalidad)
        if mod =='Anual':
            horas = choice(hora_anual)
        else:
            horas = choice(hora_cua)
        prof = choice(profe)
        profe.remove(prof)

        catedra = Catedra((nom[0:3]+str(randint(1100, 10000))),nom, mod, horas, prof)
        agregar_tc(tabla, bernstein_catedra, catedra)
    print('Mostrando todas las catedras:')
    barrido_tc(tabla)

print(universidad(tabla))
'''

#Ej 4. Desarrollar un algoritmo que implemente una tabla hash cerrada para cargar personajes
# de Star Wars de los que solo se conoce su nombre, contemplando las siguientes
# actividades:
# a. la tabla inicialmente será de 20 posiciones;
# b. deberá permitir el manejo de colisiones;
# c. cuando el factor de carga de la tabla exceda el 75%, se deberá incrementar el
# tamaño de la tabla al doble y hacer un rehashing de las claves cargadas.

class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

nombres = ['Darth Vader','Chewbacca','Maestro Yoda','R2D2','Obi-Wan Keobi','Han Solo',
            'Beru Lars','Leia Organa','Poe Dameron','Luke Skywalker']

tabla = crear_tabla(10)

for i in range(len(nombres)):
    dato = Personaje(nombres[i])
    agregar_tc(tabla, bernstein_SW, dato)
    # porcentaje usado en tabla
    porc_tabla = (cantidad_tc(tabla)*100)/len(tabla)
    if porc_tabla > 75:
        print('La tabla supero el 75% de su memoria. Necesitamos hacer un Rehashing.')
        print('Haciendo Rehashing...')
        tabla_aux = crear_tabla(len(tabla)*2)
        for dato in tabla:
            if dato is not None:
                agregar_tc(tabla_aux, bernstein_SW, dato)
        print('>>> Mostrando datos de la nueva tabla... <<<')
        sleep(2)
        barrido_tc(tabla_aux)
        porc_tabla_aux = (cantidad_tc(tabla_aux)*100)/len(tabla_aux)
        print('Porcentaje ocupado en tabla: ' + str(porc_tabla_aux))
print()
print('Tabla Final')
barrido_tc(tabla_aux)
print('Taamaño = ' + str(cantidad_tc(tabla)))

# Ej 5. Desarrollar un algoritmo que implemente una tabla hash cerrada para administrar los
# contactos de personas de las cuales se conoce nombre, apellido y correo electrónico,
# contemplando las siguientes pautas:
# a. El campo clave para generar las posiciones son el apellido y nombre.
# b. Deberá contemplar una función de sondeo para resolver las colisiones.
'''
class Contacto(object):
    def __init__ (self, apellido, nombre, correo):
        self.apellido = apellido
        self.nombre = nombre
        self.correo = correo
    
    def __str__ (self):
        return '-' + self.apellido + " " + self.nombre + ": " + self.correo

tabla = crear_tabla(20)

dato = Contacto('Picart','Fernando','fxpicart@gmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Fernandez','Solange','sm_1020@hotmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Jessie','Diaz','Diaz_jes@gmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Hernandez', 'Mike', 'Mike@hotmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Hunt', 'Horacio', 'H_hunt@yahoo.com.ar')
agregar_tc(tabla, bernstein_contactos, dato)
print('Datos de los contactos:')
barrido_tc(tabla)
'''
# Ej 6. Darth Vader le encarga desarrollar los algoritmos para organizar los Stormtrooper
# cumpliendo con las siguientes demandas:
# a. Deberá generar 2000 Stormtrooper siguiendo el formato de la imagen anterior
# contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados
# de manera aleatoria;
# b. deberá cargar los Stormtrooper generados en dos tablas hash encadenadas, en la
# primera se deberá agrupar de acuerdo a los tres últimos dígitos del código y en la
# segunda a partir de las iniciales de la legión;
# c. ahora obtenga todos los Stormtrooper terminados en 781 para asignarlos a una
# misión de asalto y a los terminados en 537 para una misión de exploración;
# d. ahora obtenga los Stormtrooper de la legión CT para que custodien a Darth Vader
# a una misión de exploración al planeta Hoth y los de la legión TF para una misión
# de exterminación a Endor.
'''
class StormTrooper():
    def __init__(self,legion,codigo):
        self.legion = legion
        self.codigo = codigo

    def __str__(self):
        return self.legion + ' ; ' + str(self.codigo)

legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']


t_legion = crear_tabla(20)
t_codigo = crear_tabla(1000)
# A
for i in range(20):
    legion = choice(legiones)
    codigo = randint(10000, 99999)
    trooper = StormTrooper(legion, codigo)
    agregar_ta(t_legion, bernstein_troopers, trooper, 'legion')
    agregar_ta(t_codigo, hash_troopers_division, trooper, 'codigo')
# B
print('Troopers por legion')
barrido_ta(t_legion)
print()
print('Troopers por código')
barrido_ta(t_codigo)
print()
# C
posc = hash_division(537, t_codigo)
if t_codigo[posc]:
    print('Trooper para misión de exploración')
    barrido_lista(t_codigo[posc])
print()
posc = hash_division(781, t_codigo)
if t_codigo[posc]:
    print('Trooper para misión de asalto')
    barrido_lista(t_codigo[posc])
print()
# D
posl = bernstein('FN', t_legion)
if t_legion[posl]:
    print('Legión FN')
    barrido_lista(t_legion[posl])
print()
posl = bernstein('CT', t_legion)
if t_legion[posl]:
    print('Legión CT')
    barrido_lista(t_legion[posl])
'''
# 7. Escribir un algoritmo que permita utilizar una tabla hash doble para guardar los datos de
# Pokémons, que contemple las siguientes actividades:
# a. la primera tabla hash debe ser cerrada y la función hash debe ser sobre el tipo de
# Pokémon, con lo cual se obtendrá el acceso a la segunda tabla;
# b. la segunda tabla debe ser encadenada utilizando listas enlazadas y la función
# hash deberá utilizar el número del Pokémon como clave;
# c. el tamaño de la primera tabla debe ser lo suficientemente grande como para que
# pueda almacenar todos los distintos tipos de Pokémon, debe manejar las
# colisiones con alguna función de sondeo;
#d. el tamaño de cada una de las segundas tablas debe ser 15;
# #e. el algoritmo debe permitir cargar tipos de Pokémon en la primera tabla y crear su
# respectiva segunda tabla, –en el caso de que no exista–;
# f. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# g. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo, nivel.
'''
class Pokemon():
    def __init__(self, numero, nombre, tipo, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return str(self.numero) + ' | Pokemon: ' + self.nombre + ' | Tipo: ' + self.tipo + ' | Nivel: ' + str(self.nivel)

nombres = ['Bulbasaur','Charmander','Squirtle','Pelliper','Cyndaquil','Jigglypuff','Caterpie','Eevee',
            'Pikachu', 'Spearow','Hitmonlee','Mewtwo','Articuno','Dugtrio','Primeape','Terrakion']

tipos = ['Planta','Fuego','Agua','Agua','Fuego','Normal','Bicho','Normal',
        'Eléctrico','Volador', 'Lucha','Psiquico','Hielo','Tierra','Lucha','Roca']

def tabla_pokemon():
    tabla_c = crear_tabla(50) #por tipo
    tabla_a = crear_tabla(20) #por numero
    for i in range(len(nombres)):
        nom = nombres[i]
        tipo = tipos[i]
        pokemon = Pokemon(randint(100, 999), nom, tipo, randint(1, 50))
        agregar_tc(tabla_c, bernstein_pokemones, pokemon)
    print()
    print('Tabla Pokemon Hash Por Tipo: ')
    barrido_tc(tabla_c)
    print('tamaño = '+ str(cantidad_tc(tabla_c)))

    for i in range(len(tabla_c)):
        if tabla_c[i] != None:
            dato = tabla_c[i]
            agregar_ta(tabla_a,hash_pokemon_division,dato,'numero')
    print()
    print('Tabla Pokemon Hash Por Numero: ')
    barrido_ta(tabla_a)
    print('tamaño = '+ str(cantidad_ta(tabla_a)))


print(tabla_pokemon())
'''

# 8. La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico
# interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo
# de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los
# siguientes requerimientos:
# a. cada carácter deberá ser encriptado a ocho caracteres;
# b. se deberá generar dos tablas hash para encriptar y desencriptar, para los
# caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
'''
def encriptar(oracion):
    clave = ""
    for letra in oracion:
        parte1 = str(ord(letra)*37)
        parte2 = hex(ord(letra)*2)
        clave += parte1[0] + parte2[1] + parte2[3] + parte1[1] + parte1[2] + parte2[0] + parte1[3] + parte2[2]
    return clave

def desencriptar(clave):
    oracion = ""
    while len(clave) > 0:
        caracter = ""
        caracter += clave[0] + clave[3] + clave[4] + clave[6]
        clave = clave[8:]
        caracter = int(caracter)
        caracter = int(caracter/37)
        caracter = chr(caracter)
        oracion += caracter
    return oracion
    
tabla1: crear_tabla(10000)

msj = input('ingrese un msj el cual quiera encriptar: ')
msj_encrip = encriptar(msj)
print('Mostrando mensaje encriptado...')
print(msj_encrip)
print()
msj_desenc = desencriptar(msj_encrip)
print('Desencriptando mensaje...')
print(msj_desenc)
'''
# 9. Desarrollar un algoritmo que permita cifrar y descifrar un mensaje carácter a carácter,
#contemplando las siguientes pautas:
#a. Se debe utilizar una tabla hash para guardar los valores de codificación y
#decodificación respectivamente que se vayan utilizando.
#b. Se deberá cifrar de la siguiente manera: primero, convertir al valor numérico
#correspondiente de la tabla ASCII cada carácter y luego, cada número de dicho
#valor se deberá remplazar por su valor correspondiente según los siguientes
#valores: 1 – “abd”, 2 – “def”, 3 – “ghi”, 4 –“ jkl”, 5 –“mnñ”, 6 – “opq”, 7 – “rst”, 8 –
#“uvw”, 9 – “xyz”, 0 – “#?&”, y se debe agregar al final el carácter %. Por ejemplo D
#= 68 debería quedar de la siguiente manera “opquvw%”.
'''
def cifrar(dato):
    valor = str(ord(dato))
    valor_cirado = ["#?&","abc","def","ghi","jkl","mnñ","opq","rst","uvw","xyz"]
    cadena = ""
    for num in valor:
        numInt = int(num)
        cadena += valor_cirado[numInt]
    cadena += "%"
    return cadena

tabla = crear_tabla(10)
tabla2 = crear_tabla(10)
a = 'Hola Mundo...'
a_cifrado = ''
for letra in a:
    valor = buscar_ta(tabla, hash_cifrado, Palabra(letra, ''), 'palabra')
    cifrado = ''
    if(valor is None):
        cifrado = cifrar(letra)
        palabra = Palabra(letra, cifrado)
        agregar_ta(tabla, hash_cifrado, palabra, 'palabra')
    else:
        cifrado = valor.info.significado
    a_cifrado += cifrado
print(a_cifrado)
lista = a_cifrado.split('%')
lista.pop()
msj = ''
for letras in lista:
    valor = buscar_ta(tabla2, bernstein_palabra, Palabra(letras, ''), 'palabra')
    decifrado = ''
    if(valor is None):
        decifrado = desifrar(letras)
        palabra = Palabra(letras, decifrado)
        agregar_ta(tabla2, bernstein_palabra, palabra, 'palabra')
    else:
        decifrado = valor.info.significado
    msj += decifrado
print(msj)
'''
# Ej 10. 