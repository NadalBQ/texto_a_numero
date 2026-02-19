# Texto a Número (Text to Integer – Spanish)

Aplicación en Python que convierte números escritos en lenguaje natural en español a su representación entera.

El proyecto implementa un parser basado en reglas que interpreta expresiones numéricas escritas en español y las transforma en valores enteros sin utilizar dependencias externas.

---

## Ejemplos

```
Cuatrocientos veinticinco -> 425
Tres mil doscientos millones ochocientos cincuenta y seis -> 3200000856
```

---

## Características

- Conversión de números escritos en español a enteros
- Soporte para números compuestos
- Manejo de magnitudes grandes (mil, millón, millones, etc.)
- Implementación en Python puro
- Sin dependencias externas

---

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/NadalBQ/texto_a_numero.git
cd texto_a_numero
```

## Uso

Ejemplo básico:

```python
from texto_a_numero import texto_a_numero

resultado = texto_a_numero("cuatrocientos veinticinco")
print(resultado)  # 425
```

---

## Descripción

El programa analiza expresiones numéricas en lenguaje natural mediante reglas que identifican:

* Unidades, decenas y centenas.

* Conectores lingüísticos propios del español.

* Magnitudes jerárquicas como miles y millones.

* La agregación progresiva del valor numérico final.

---

## Objetivo del proyecto

Este proyecto tiene fines educativos y de procesamiento del lenguaje natural (NLP), mostrando cómo interpretar estructuras numéricas del español mediante lógica programada en Python.

---

## Alcance

Este proyecto convierte números escritos en lenguaje natural en español a enteros.
Actualmente solo soporta español y conversión texto → número.

---

## Limitaciones

- Solo números cardinales
- No soporta decimales
- No soporta números ordinales
- Puede producir falsos positivos (cincocientos -> 500)
- Admite números hasta miles de septillones (10^47)

---

## Tests

El proyecto incluye pruebas unitarias para verificar la correcta interpretación de distintas estructuras numéricas del español.

Por ejemplo:

* dieciséis -> 16

* veintitrés -> 23

* cuarenta y cinco -> 45

* setenta y seis -> 76

* noventa y uno -> 91

* ciento ocho -> 108

* doscientos quince -> 215

* quinientos treintaidós -> 532 (forma sin separación aceptada por el parser)

* novecientos treinta y cuatro -> 934 (forma con separación)

* mil cuatro -> 1004

* dos mil cinco -> 2005

* un millón -> 1000000

* tres mil doscientos millones cuatrocientos veintiuno -> 3200000421

---

## Contribuciones

Las contribuciones son bienvenidas. Puedes abrir un issue o enviar un pull request con mejoras o correcciones.

Si deseas soporte para otros idiomas, consulta el proyecto general de conversión multilingüe:
[numtext](https://github.com/NadalBQ/numtext)
