#---------------------Registro de Usuarios------------------------------------------------
# Creamos una lista vacía para guardar los usuarios
# Cada usuario será una lista con dos elementos: el nombre y la tarjeta
usuarios = []

# Creamos una lista vacía para guardar los préstamos
# Cada préstamo será una lista con tres elementos: el usuario, el origen y el destino
prestamos = []

# Definimos una función para registrar un nuevo usuario
def registrar_usuario(nombre, tarjeta):
  # Creamos una lista con los datos del usuario
  usuario = [nombre, tarjeta]
  # Añadimos el usuario a la lista de usuarios
  usuarios.append(usuario)
  # Mostramos un mensaje de confirmación
  print(f"El usuario {nombre} ha sido registrado con éxito.")

# Definimos una función para tomar una cicla
def tomar_cicla(tarjeta, origen, destino):
  # Buscamos al usuario que tiene la tarjeta indicada
  usuario = None
  for u in usuarios:
    if u[1] == tarjeta: # El segundo elemento de la lista es la tarjeta
      usuario = u
      break
  # Si no encontramos al usuario, mostramos un mensaje de error
  if usuario == None:
    print("No se ha encontrado ningún usuario con esa tarjeta.")
    return
  # Si encontramos al usuario, creamos una lista con los datos del préstamo
  prestamo = [usuario[0], origen, destino] # El primer elemento de la lista es el nombre del usuario
  # Añadimos el préstamo a la lista de préstamos
  prestamos.append(prestamo)
  # Mostramos un mensaje de confirmación
  print(f"El usuario {usuario[0]} ha tomado una cicla desde {origen} hasta {destino}.")

# Definimos una función para consultar el listado de usuarios
def consultar_usuarios():
  # Mostramos el número de usuarios registrados
  print(f"Se han registrado {len(usuarios)} usuarios.")
  # Mostramos los datos de cada usuario
  for usuario in usuarios:
    print(f"Nombre: {usuario[0]}, Tarjeta: {usuario[1]}")

# Definimos una función para consultar el listado de préstamos
def consultar_prestamos():
  # Mostramos el número de préstamos realizados
  print(f"Se han realizado {len(prestamos)} préstamos.")
  # Mostramos los datos de cada préstamo
  for prestamo in prestamos:
    print(f"Usuario: {prestamo[0]}, Origen: {prestamo[1]}, Destino: {prestamo[2]}")

# Al final del código, añadimos estas líneas:

# Creamos una variable para controlar el bucle
continuar = True

# Mientras el usuario quiera agregar más usuarios
while continuar:
  # Preguntamos al usuario su nombre
  nombre = input("Ingrese su nombre: ")

  # Preguntamos al usuario su número de tarjeta
  tarjeta = input("Ingrese su número de tarjeta: ")

  # Llamamos a la función registrar_usuario con los datos del usuario
  registrar_usuario(nombre, tarjeta)

  # Preguntamos al usuario si quiere agregar otro usuario
  respuesta = input("¿Quiere agregar otro usuario? (s/n): ")

  # Si la respuesta es "n", cambiamos el valor de la variable continuar a False
  if respuesta == "n":
    continuar = False

# Preguntamos al usuario su número de tarjeta
tarjeta = input("Ingrese su número de tarjeta: ")

# Preguntamos al usuario el origen del préstamo
origen = input("Ingrese el origen del préstamo: ")

# Preguntamos al usuario el destino del préstamo
destino = input("Ingrese el destino del préstamo: ")

# Llamamos a la función tomar_cicla con los datos del usuario
tomar_cicla(tarjeta, origen, destino)

# Llamamos a la función consultar_usuarios para ver el listado de usuarios registrados
consultar_usuarios()

# Llamamos a la función consultar_prestamos para ver el listado de préstamos realizados
consultar_prestamos()
