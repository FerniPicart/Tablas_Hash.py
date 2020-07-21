from tda_lista import Lista,insertar,eliminar,tamanio,busqueda_lista,barrido_lista


def crear_tabla(tamanio):
    '''Crea una tabla hash vacia'''
    tabla = [None] * tamanio
    return tabla


def agregar_tc(tabla, hash, dato):
    '''Agrega elementos a una tabla cerrada'''
    pos = hash(dato, tabla)
    if tabla[pos] is None:
        tabla[pos] = dato
    else:
        if pos == len(tabla)-1:
            pos = -1
        pos_aux = pos
        while tabla[pos+1] is not None and hash(tabla[pos+1], tabla) == pos_aux:
            pos += 1
            if pos == len(tabla)-1:
                pos = -1
        if tabla[pos+1] is None:
            tabla[pos+1] = dato
        else:
            rehasing(tabla,hash)


def agregar_ta(tabla, hash, dato, criterio=None):
    '''Agrega elementos a una tabla abierta'''
    pos = hash(dato, tabla)
    if tabla[pos] is None:
        tabla[pos] = Lista()
    insertar(tabla[pos], dato, criterio)


def quitar_tc(tabla, hash, dato):
    '''Quita elementos de una tabla cerrada'''
    dato = None
    pos = hash(dato, tabla)
    if tabla[pos] is not None:
        if tabla[pos] == dato:
            dato = tabla[pos]
            tabla[pos] = None
            # revisar si hay colision y realizar desplazamiento
        else:
            print('colision')
    return None


def quitar_ta(tabla, hash, dato, criterio=None):
    '''Quita elementos de una tabla abierta'''
    pos = hash(dato, tabla)
    if tabla[pos] is not None:
        return eliminar(tabla[pos], dato.palabra, criterio)
    else:
        return None


def buscar_tc(tabla, hash, dato):
    '''Busca un dato en una tabla cerrada'''
    p = None
    pos = hash(dato, tabla)
    if tabla[pos] is not None:
        if tabla[pos] == dato:
            p = pos
        else:
            if(pos == len(tabla)-1):
                pos = -1
            # completar
            pos_aux = pos
            while tabla[pos+1] is not None and hash((tabla[pos+1], tabla) == pos_aux):
                pos += 1
                if pos == len(tabla)-1:
                    pos = -1
                if tabla[pos] == dato:
                    p = pos
                    break
    return p


def buscar_ta(tabla, hash, dato, criterio=None):
    '''Busca un dato en una tabla abierta'''
    pos = hash(dato, tabla)
    if tabla[pos] is not None:
        return busqueda_lista(tabla[pos], dato.palabra, criterio)
    else:
        return None


def cantidad_tc(tabla):
    '''Cantidad de elementos de una tabla cerrada'''
    return len(tabla) - tabla.count(None)


def cantidad_ta(tabla):
    '''Cantidad de elementos de una tabla abierta'''
    cant = 0
    for elemento in tabla:
        if elemento is not None:
            cant += tamanio(elemento)
    return cant


def barrido_ta(tabla):
    '''Muestra los elementos de una tabla abierta'''
    for indice in tabla:
        if indice is not None:
            barrido_lista(indice)


def barrido_tc(tabla):
    '''Muestra los elementos de una tabla cerrada'''
    for indice in tabla:
        if indice is not None:
            print(indice)


def rehasing(tabla, hash):
    nueva_tabla = crear_tabla(len(tabla)*2)
    for dato in tabla:
        if dato is not None:
            agregar_tc(nueva_tabla, hash, dato)
    return nueva_tabla


def hash_division(clave, tabla):
    '''Funcion hash para tablas'''
    return clave % len(tabla)


def hash_troopers_division(trooper, tabla):
    return trooper.codigo % len(tabla)


def hash_guia_division(guiatel, tabla):
    return guiatel.numero % len(tabla)


def hash_catedra_division(catedra, tabla):
    return catedra.codigo % len(tabla)


def hash_pokemon_division(pokemon,tabla):
    return pokemon.numero % len(tabla)

def hash_diccionario(dato, tabla):
    '''Funcion hash para tablas abiertas'''
    return ord(dato.palabra[0].upper()) % len(tabla)


def bernstein(cadena, tabla):
    '''Funcion bernstein para tablas hash'''
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_catedra(cadena, tabla):
    '''Funcion bernstein para tablas hash'''
    h = 0
    for caracter in cadena.codigo:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_SW(cadena, tabla):
    '''Funcion bernstein para tablas hash'''
    h = 0
    for caracter in cadena.nombre:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_contactos(cadena, tabla):
    '''Funcion bernstein para tablas hash'''
    h = 0
    for caracter in cadena.nombre:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_troopers(cadena, tabla):
    '''Funcion hash de Bernstein para cadenas'''
    h = 0
    for caracter in cadena.legion:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_pokemones(pokemon, tabla):
    '''Funcion hash de Bernstein para cadenas'''
    h = 0
    for caracter in pokemon.tipo:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_palabra(cadena, tabla):
    '''Función hash de Bernstein para cadenas.'''
    h = 0
    for caracter in cadena.palabra:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def hash_cifrado(dato, tabla):
    return ord(dato.palabra[0].upper()) % len(tabla)


def desifrar(dato):
    dic = {"#?&": '0',"abc": '1',"def":'2',"ghi":'3',"jkl":'4',"mnñ":'5',"opq":'6',"rst":'7',"uvw":'8',"xyz":'9'}
    cadena = ''
    for i in range (0, len(dato),3):
        cadena += dic[dato[i:i+3]]
    return chr(int(cadena))