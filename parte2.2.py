'''
Maria Jose Castro 181202
Diana de Leon 18607
Camila Gonzalez 18398
Maria Ines Vasquez 18250
'''

import scrypt

#aqui vamos a guardar en mensaje y la contrasena 
mensaje = 'Hola este es el mensaje para lab 9'
#esta contrasena permitira verificar el mensaje 
password = 'CC3078-10-2020'
mensajeEncriptado = scrypt.encrypt(mensaje, password, maxtime=0.1) # This will take at least 0.1 seconds
#se mostrata el mensaje
print('Este es el mensaje cifrado', mensajeEncriptado)
print()

#aqui mostraremos el mensaje recibido y sera descenriptado
#esta funcion recibe como parametros el mensaje, la llave y el tiempo
mensajeDesencriptado = scrypt.decrypt(mensajeEncriptado, password, maxtime=0.1)
print('El mensaje recibido es: ', mensajeDesencriptado) 
print()

#Aqui haremos la simulacion de que se ingreso un dato incorrecto en este caso sera la contrasena
mensajeDesencriptado = scrypt.decrypt(mensajeEncriptado, 'hola', maxtime=0.1) 
print('El mensaje recibido es: ', mensajeDesencriptado) 