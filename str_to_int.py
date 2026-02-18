
number_set = {"uno": 1, "un": 1, "ún": 1, "dos": 2, "dós": 2, "tres": 3, "trés": 3, "cuatro": 4, "cinco": 5, "seis": 6, "séis": 6, "siete": 7, "sete": 7, "ocho": 8, "nueve": 9, "nove": 9, "diez": 10, "diec": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "veinte": 20, "veint": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100, "quinien": 500, "mil": 1000}
operadores = {"y", "i", "to", "tos", "es"}
unidades = {"uno", "un", "ún", "dos", "dós", "tres", "trés", "cuatro", "cinco", "seis", "séis", "siete", "sete", "ocho", "nueve", "nove"}
decenas = {"diez", "diec", "once", "doce", "trece", "catorce", "quince", "veinte", "veint", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"}
centenas = {"cien", "quinien"}
millares = {"mil", "millón", "millon", "billón", "billon", "trillón", "trillon", "cuatrillón", "cuatrillon", "quintillón", "quintillon", "sextillón", "sextillon", "septillón", "septillon"}


def _tokenize(string: str) -> list:
    words = string.lower().split()
    lista = []
    l = []
    for word in words:
        for operador in operadores:
            if word.endswith(operador):
                if word in centenas or word in millares:
                    word = word[:-len(operador)]
            elif word == operador:
                word = ""
        if word: l.append(word)
        if word in millares:
            lista.append(l)
            l = []
    if l: lista.append(l)
    return lista


def _strip(string):
    for operador in operadores:
        if string.endswith(operador):
            string = string[:-len(operador)]
        if string.startswith(operador):
            string = string[len(operador):]
    return string


def _split(string):
    tmp = []
    dec = False
    for decena in decenas:
        if string.startswith(decena):
            tmp.append(decena)
            string = string[len(decena):]
            dec = True
            for operador in operadores:
                if string.startswith(operador):
                    string = string[len(operador):]
                    break
            break
    if not dec:
        for unidad in unidades:
            if string.startswith(unidad):
                tmp.append(unidad)
                string = string[len(unidad):]
                string = _strip(string)
                break
    tmp.append(string)
    return tmp


def _sumar(*args) -> int:
    respuesta = sum(args)
    return respuesta


def _multiplica_millar(num, millar):
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


def _string_to_int(string:str) -> int:
    # comprobar unidades, decenas y centenas
    if string in unidades or string in decenas or string in centenas:
        return number_set[string]
    # comprobar sumas como treintaicinco o multiplicaciones como doscientos
    elif string not in millares:
        tmp = _split(string)
        if tmp[0] in unidades:
            return number_set[tmp[0]] * number_set[tmp[1]] # dos * cientos (2 * 100)
        else:
            return number_set[tmp[0]] + number_set[tmp[1]] # treinta + cinco (30 + 5)


def main():
    number = input()
    try:
        tok = _tokenize(number)
        suma = 0
        tmp = 0
        for num_list in tok:
            for i in range(len(num_list)):
                if num_list[i] in operadores:
                    continue
                
                if i == (len(num_list) - 1):
                    if num_list[i] not in unidades:
                        num_list[i] = _strip(num_list[i])
                    if num_list[i] in millares:
                        if tmp:
                            tmp = _multiplica_millar(tmp, num_list[i])
                        else:
                            tmp = _multiplica_millar(1, num_list[i])
                        if num_list[i] != "mil":
                            suma += tmp
                            tmp = 0
                    else:
                        tmp += _string_to_int(num_list[i])
                else:
                    num = _string_to_int(num_list[i])
                    tmp += num
        if tmp:
            suma += tmp
        return suma
    except Exception as e:
        return "Ha habido un problema, consulta con el desarrollador: " + e

if __name__ == "__main__":
    print(main())