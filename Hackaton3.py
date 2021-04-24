notas=[]
# entero=False
# while entero==False :
#     try:
#         numero_notas=int(input(f'cuantas notas se van a ingresar? '))
#         if numero_notas<=1:  
#             print(" Error, el número ingresado debe ser mayor a 1")
#         else:
#             entero=True

#     except (TypeError, ValueError) :
#         print("Error el valor ingresado debe ser número entero")  

numero_notas=5
print(f'Ingrese las {numero_notas} notas')

for nota in range(numero_notas):
    validar_numero=False
    
    while validar_numero==False:
        try:
            numero_ingresado=(int(input(f'nota {nota + 1} ')))
            if numero_ingresado<20 and numero_ingresado>0:
                notas.append(numero_ingresado)
                validar_numero=True
            else:    
                print("Error, el número ingresado no esta en el rango 0-20")
                
        except (TypeError, ValueError) as e:
             print("Error, debes escribir un número")

print(notas)

promedio=sum(notas)/numero_notas
print(f'el promedio de las notas es {round(promedio,2)}')
maxima_nota=max(notas)
print(f'la nota máxima es {maxima_nota}')
minima_nota=min(notas)
print(f'la nota minima es {minima_nota}')