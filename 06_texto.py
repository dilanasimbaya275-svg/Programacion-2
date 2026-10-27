# string cadenas de caracteres

jedi = "Qui-Gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droid = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El Jedi es:" + jedi)
print("El Jedi:", type(jedi))
print("El aprendiz es:" + aprendiz)
print("El aprendiz:", type(aprendiz))
print("El droid es:" + droid)
print("El droid:", type(droid))
print("El planeta es:" + planeta)
print("El planeta:", type(planeta))
print("El código es:" + codigo)
print("El código:", type(codigo))

longitud_jedi = len(jedi)
print("La longitud del nombre del Jedi es:" + str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es:" + str(longitud_aprendiz))

mensaje = "La Federación de Comercio ha establecido un bloque en Naboo"
print("El mensaje es:" + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayúsculas es:" + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minúsculas es:" + mensaje_minusculas)

comunicado = "Los Jesi son enviados a Naboo"
print("El comuni