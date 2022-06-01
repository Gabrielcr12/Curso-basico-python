#Declaramos una variable
calificacion = input("Introduce tu calificación de la AZ-900- ")

calificacion = int(calificacion)

#Preguntamos si la calificación es menor a 700
if calificacion < 700 :
    print("Por no estudiar :(") # Si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("MIENTES!! No puedees sacar más de mil")
else : #Si no se cumple el if anterior pasa a esta linea 
        print("Felicidades, pasa por tu certificado") #Se ejecuta si ninguno de los if se cumple
#Verificador de mayoria de edad
edad = input("Introduce tu edad ") # input / para leer variables
edad = int(edad)
#Operador "and" | Operador "or" solo una de las condiciones se tienen que cumplir
if edad >= 18 and edad <=100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acomañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros") 
    
# EN PYTHON NO HAY SWITCH CASE



