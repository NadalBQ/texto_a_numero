
number_set = {"uno": 1, "un": 1, "ún": 1, "dos": 2, "dós": 2, "tres": 3, "trés": 3, "cuatro": 4, "cinco": 5, "seis": 6, "séis": 6, "siete": 7, "sete": 7, "ocho": 8, "nueve": 9, "nove": 9, "diez": 10, "diec": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "veinte": 20, "veint": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100, "quinien": 500, "mil": 1000}
operadores = {"y", "i", "to", "tos", "es"}
unidades = {"uno", "un", "dos", "tres", "cuatro", "cinco", "seis", "séis", "siete", "sete", "ocho", "nueve", "nove"}
decenas = {"diez", "diec", "once", "doce", "trece", "catorce", "quince", "veinte", "veint", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"}
centenas = {"cien", "quinien"}
millares = {"mil", "millón", "millon", "billón", "billon", "trillón", "trillon", "cuatrillón", "cuatrillon", "quintillón", "quintillón", "sextillón", "sextillon", "septillón", "septillon"}


def tokenize(string: str) -> list:
    words = string.lower().split()
    lista = []
    l = []
    for word in words:
        for operador in operadores:
            if word.endswith(operador):
                word = word[:-len(operador)]
        l.append(word)
        if word in millares:
            lista.append(l)
            l = []
    if l: lista.append(l)
    return lista



def sumar(*args) -> int:
    respuesta = sum(args)
    return respuesta


def multiplica_millar(num, millar):
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


def string_to_int(string:str) -> int:
    # comprobar sumas como treintaicinco


    
    # comprobar unidades, decenas y centenas
    if string in unidades or string in decenas or string in centenas:
        return number_set[string]
    
    # comprobar millares
    

    pass


def find_number_name(string:str = "Dos") -> int:
    string = string.lower()
    numeros = string.split(" ")
    numeros = numeros[::-1]
    suma = 0
    for numero in numeros:
        num = string_to_int(numero)
        suma += sumar(suma, num)
    

print(tokenize("Dos mil trescientos cuarenta y cinco"))
print(tokenize("doce mil trescientos cuatro millones seiscientos cincuenta y seis mil ciento dieciséis"))