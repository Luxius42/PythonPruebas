import sys

#Típico programa "Hola mundo" en Python
print("Hola mundo!")    

#Usando librería sys para imprimir información del sistema
print("Información del sistema:")
print(sys.version)
print("Plataforma:")
print(sys.platform)

#Así se utiliza la indentación en Python
#La indentación es crucial en Python para definir bloques de código.
#Por ejemplo, en un bloque if:
if 5 > 2:
    print("5 es mayor que 2")   
    
# Esto por ejemplo, sería erróneo
# if 5 > 2:
# print("5 es mayor que 2")
# Ya que no está indentado correctamente

# Al igual que en JS, las variables se definen sin necesidad de declarar su tipo
nombre = "José"
edad = 30   
# En Python, necesitamos usar f-strings o el método format para interpolar variables en cadenas
# Aquí usamos f-strings, que son una forma moderna y eficiente de formatear cadenas
print(f"Hola, {nombre}. Tienes {edad} años.")

# Aunque en Python no necesitamos declarar el tipo de variable, podemos definir tipos de datos
x = str(3)    # x = '3'
y = int(3)    # y = 3
z = float(3)  # z = 3.0

print(f"Tipo de x: {type(x)}\nTipo de y: {type(y)}\nTipo de z: {type(z)}")

# En Python, podemos usar tanto comillas simples como dobles para definir cadenas
cadena_simple = 'Hola mundo'
cadena_doble = "Hola mundo" 
# También podemos usar comillas triples para cadenas multilínea
cadena_multilinea = """Esto es una cadena de texto multilínea,
a veces usada como comentario largo o documentación."""
print(cadena_multilinea)

# Python es sensible a las mayúsculas y minúsculas, por lo que 'Variable' y 'variable' son diferentes
Variable = "Hola"
variable = "Mundo"
print(Variable, variable)  # Imprime: Hola Mundo



