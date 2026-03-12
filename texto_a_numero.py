# mapa (diccionario) con nombre de número y su valor (para cada forma en que se puede encontrar)
number_set: dict[str, int] = {"uno": 1, "un": 1, "ún": 1, "dos": 2, "dós": 2, "tres": 3, "trés": 3, "cuatro": 4, "cinco": 5, "seis": 6, "séis": 6, "siete": 7, "sete": 7, "ocho": 8, "nueve": 9, "nove": 9, "diez": 10, "diec": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "veinte": 20, "veint": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100, "quinien": 500, "mil": 1000}
operadores: set = {"y", "i", "to", "tos", "es"}
unidades: set = {"uno", "un", "ún", "dos", "dós", "tres", "trés", "cuatro", "cinco", "seis", "séis", "siete", "sete", "ocho", "nueve", "nove"}
decenas: set = {"diez", "diec", "once", "doce", "trece", "catorce", "quince", "veinte", "veint", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"}
centenas: set = {"cien", "quinien"}
millares: set = {"mil", "millón", "millon", "billón", "billon", "trillón", "trillon", "cuatrillón", "cuatrillon", "quintillón", "quintillon", "sextillón", "sextillon", "septillón", "septillon"}


def _tokenize(string: str) -> list:
    '''
    Recibe una cadena y la divide en grupos de cadenas más pequeñas que se devuelven en una lista.
    La lista devuelta contiene en su interior tantas listas como grupos de millares haya en el número recibido como cadena.
    Cada lista interior contiene una cadena por palabra, preparadas para tratarse de forma individual como número escrito en lenguaje natural.    
    '''
    words = string.lower().split()
    lista = []
    l = []
    for word in words:
        for operador in operadores: # Si termina en alguno de los "operadores" y pertenece al conjunto de millares o centenas, se guarda limpio
            if word.endswith(operador):
                if word[:-len(operador)] in centenas or word[:-len(operador)] in millares:
                    word = word[:-len(operador)]
            elif word == operador: # Si la palabra entera es un "operador" entonces no contiene un número y se puede eliminar
                word = ""
        if word: l.append(word) # Se añaden las palabras que contienen algún número
        if word in millares: # Se separan las palabras en grupos de millares
            lista.append(l)
            l = []
    if l: lista.append(l)
    return lista


def _strip(string: str) -> str:
    '''Elimina las letras al principio y final de palabra que no aportan valor al número.'''
    for operador in operadores: # Si comienza o termina por un "operador" se eliminan
        if string.endswith(operador):
            string = string[:-len(operador)]
        if string.startswith(operador):
            string = string[len(operador):]
    return string


def _split(string: str) -> list:
    '''Divide un número no convertible directamente en sus dos partes convertibles.'''
    tmp = []
    dec = False
    for decena in decenas: # Se busca si la palabra comienza por una decena (por ejemplo treintaidós)
        if string.startswith(decena):
            tmp.append(decena) # Se guarda la primera parte de la palabra
            string = string[len(decena):]
            dec = True
            for operador in operadores:
                if string.startswith(operador): # Si la pabalra contiene operador intermedio se elimina
                    string = string[len(operador):] # Se guarda la segunda parte de la palabra
                    break
            break
    if not dec: # Si no comienza por decena, se comprueba que comience por unidad (por ejemplo doscientos)
        uni = False
        for unidad in unidades:
            if string.startswith(unidad):
                tmp.append(unidad) # Se guarda la primera parte de la palabra
                string = string[len(unidad):] # Se guarda la segunda parte de la palabra
                string = _strip(string)
                uni = True
                break
        if not uni: # Si la palabra no comienza ni por decena ni por unidad, se limpia y se guarda (por ejemplo ciento)
            string = _strip(string)
    tmp.append(string)
    return tmp


def _multiplica_millar(num: int, millar: str) -> int:
    '''Devuelve la transformación pertinente numérica según el millar encontrado.'''
    if millar == "mil":
        return num * 10**3
    if millar == "millon":
        return num * 10**6
    if millar == "billon":
        return num * 10**12
    if millar == "trillon":
        return num * 10**18
    if millar == "cuatrillon":
        return num * 10**24
    if millar == "quintillon":
        return num * 10**30
    if millar == "sextillon":
        return num * 10**36
    if millar == "septillon":
        return num * 10**42
    
    if millar == "millón":
        return num * 10**6
    if millar == "billón":
        return num * 10**12
    if millar == "trillón":
        return num * 10**18
    if millar == "cuatrillón":
        return num * 10**24
    if millar == "quintillón":
        return num * 10**30
    if millar == "sextillón":
        return num * 10**36
    if millar == "septillón":
        return num * 10**42


def _string_to_int(string: str) -> int:
    '''Convierte el número recibido en lenguaje natural a su forma numérica.'''
    # comprobar unidades, decenas y centenas
    if string in unidades or string in decenas or string in centenas:
        return number_set[string]
    # comprobar sumas como treintaicinco o multiplicaciones como doscientos
    elif string not in millares:
        tmp = _split(string)
        if tmp[0] in unidades:
            return number_set[tmp[0]] * number_set[tmp[1]] # dos * cientos (2 * 100)
        return number_set[tmp[0]] + number_set[tmp[1]] # treinta + cinco (30 + 5)


def main(string: str = None) -> int:
    '''Pide por consola un número en lenguaje natural, lo procesa y devuelve su forma numérica'''
    if not string:
        string = input()
    tok = _tokenize(string) # Separa las palabras para trabajar una por una
    suma = 0
    tmp = 0
    for num_list in tok: # Itera por cada grupo de millares en el número
        for i in range(len(num_list)): # Accede a cada número de la lista
            if num_list[i] in operadores: # Ignora operadores
                continue
            
            if i == (len(num_list) - 1): # Comprueba al final de la lista si el número termina en unidad o en millar para continuar
                if num_list[i] not in unidades:
                    num_list[i] = _strip(num_list[i])
                if num_list[i] in millares: # Realiza la operación de millar pertinente
                    if tmp:
                        tmp = _multiplica_millar(tmp, num_list[i])
                    else:
                        tmp = _multiplica_millar(1, num_list[i])
                    if num_list[i] != "mil": # Actualiza la suma total con la suma parcial del grupo de millar calculado
                        suma += tmp
                        tmp = 0
                else: # Si no es unidad ni millar se suma (por ejemplo veinte)
                    tmp += _string_to_int(num_list[i])
            else: # Cada número se transforma y se añade a la suma parcial del grupo de millar actual
                num = _string_to_int(num_list[i])
                tmp += num
    if tmp: # Se añade el valor del último grupo de millar calculado
        suma += tmp # Se actualiza la suma total del número introducido originalmente
    return suma



if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if args:
        args = " ".join(args)
        print(main(args))
    else:
        print(main())