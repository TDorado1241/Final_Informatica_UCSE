array=[]

def cargar_lecturas():
  cantidad = int(input("\nIngresar la cantidad de sensores:"))
  for i in range(cantidad):
    print(f"\nSensorN°{i+1}")
    fuerza = float(input("\nIngresar la fuerza del sensor: "))
    if fuerza > 0:
      array.append(fuerza)
def mostrar_lecturas(array):
  if len(array):
    for i,lectura in enumerate(array):
      print(f"\nLectura N°{i+1}: {lectura}N")
  else:
    print("\nNo hay lecturas registradas.")
def agregar_lectura(array):
  print("\nAgregar Lectura de un Nuevo Sensor")
  fuerza = float(input("\nIngresar la lectura del sensor: "))
  if fuerza > 0:
    array.append(fuerza)

def visualizar_promedio(array):
  if len(array):
    promedio = sum(array) / len(array)
    print(f"\nLa fuerza promedio es: {promedio}N")
  else:
    print("\nNo hay lecturas registradas.")

def mayor_lectura(array):
  if len(array):
    lectura_maxima = max(array)
    print(f"\nLa lectura máxima es: {lectura_maxima}N")
  else:
    print("\nNo hay lecturas registradas.")

def sensore_menores_a_5(array):
  if len(array):
    lecturas_menores_a_5 = [lectura for lectura in array if lectura < 5]
    print(f"\nSensores con lectura inferior a 5 Newtons:")
    for i, lectura in enumerate(lecturas_menores_a_5):
      print(f"\nLectura N°,{i+1}: {lectura}N")
  else:
    print("\nNo hay lecturas menores a 5 Newtons.")   

def eliminar_sensor_especifico(array):
  if len(array):
    sensor_a_eliminar = int(input("\nIngresar el número del sensor a eliminar: "))
    if 0 < sensor_a_eliminar <= len(array):
      del array[sensor_a_eliminar - 1]
      print(f"\nSensorN°{sensor_a_eliminar} fue elimindado correctamente")
  else:
    print("\nNo hay lecturas registradas.")

def ajustar_lecturas_superiores_a_20(array):
  if len(array):
    for i in range(len(array)):
      if array[i] > 20:
        array[i] = 20
        print("Las lecturas fueron ajustadas correctamente")
  else:
    print("\nNo hay lecturas registradas.")


while True:
  print("\nMENU DE OPCIONES")
  print(1,"Cargar Lectura de Fuerza de Sensores.")
  print(2,"Mostrar Lectura de sensores.")
  print(3,"Agregar Lectura de un Nuevo Sensor.")
  print(4,"Visualizar la Fuerza Promedio.")
  print(5,"Ver la Mayor Lectura Registrada.")
  print(6,"Calcular Sensores con Lectura Inferior a 5 Newtons.")
  print(7,"Eliminar la Lectura de un Sensor Especifico.")
  print(8,"Ajustar Lecturas por Encima de 20 Newtons.")
  print(0,"Salir.")

  opcion = int(input("\nIngrese una opcion: "))
  if opcion == 1:
    cargar_lecturas()
  elif opcion == 2:
    mostrar_lecturas(array)
  elif opcion == 3:
    agregar_lectura(array)
  elif opcion == 4:
    visualizar_promedio(array)
  elif opcion == 5:
    mayor_lectura(array)
  elif opcion == 6:
    sensore_menores_a_5(array)
  elif opcion == 7:
    eliminar_sensor_especifico(array)
  elif opcion == 8:
    ajustar_lecturas_superiores_a_20(array)
  elif opcion == 0:
    print("Fin del programa")
    break
  else:
    print("Opcion no valida,Intentar nuevamente")