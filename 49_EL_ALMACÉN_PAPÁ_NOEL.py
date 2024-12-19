# ## EJERCICIO:
#  Papá Noel tiene que comenzar a repartir los regalos... <br>
#  ¡Pero ha olvidado el código secreto de apertura del almacén!<br>
#  Crea un programa donde introducir códigos y obtener pistas.

#  # Código:
#  - El código es una combinación de letras y números aleatorios de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
#  - No hay repetidos.
#  - Se genera de manera aleatoria al iniciar el programa.
#  *
#  # Usuario:
#  - Dispone de 10 intentos para acertarlo.
#  - En cada turno deberá escribir un código de 4 caracteres, y el programa le indicará para cada uno lo siguiente:
#     - Correcto: Si el caracter está en la posición correcta.
#     - Presente: Si el caracter existe, pero esa no es su posición.
#     - Incorrecto: Si el caracter no existe en el código secreto. <br>

# Deben controlarse errores de longitud y caracteres soportados.
  
#  # Finalización:
#  - Papa Noel gana si descrifra el código antes de 10 intentos.
#  - Pierde si no lo logra, ya que no podría entregar los regalos.

import numpy as np

print("This is a test")

letters = ['A','B','C']
nums = np.arange(1,4)
total_info = letters + [str(i) for i in nums]
print(total_info)

len_code = 4

code = np.random.choice(total_info,size=len_code,replace=False)
finalCode = "".join(code)
print(finalCode)

print("You need to help to Santa, You have 10 attemps to guess the scret code of 4 characters")

for x in range(10):
  print(f"This is your {x+1} attemp")
  input_user = input("Enter the secret Code (4 characters): ").upper()
  while len(input_user) != len(finalCode):
    input_user = input("Enter the new secret Code only 4 characters: ").upper()

  if input_user == finalCode:
    print(f"You input is correct, the secret code is: {input_user}")
    break
  else:
    print("ERROR...")
    for i,op_chart in enumerate(input_user):
      if op_chart == code[i]:
        print(f"{op_chart} this character is in correct position")
      elif op_chart in code:
        print(f"{op_chart} this character is present, but it's not its position")
      else:
        print(f"{op_chart} this character is not present")

  print("------------------------")