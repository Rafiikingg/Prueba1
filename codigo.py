

#Inicio de 

print("Bienvenido al sistema de envio de mankekestravel.")
print("")
print("Para continuar debe iniciar sesión")
print("")

usuario= 'vendedor'
contra= '12345'
while True:
    user=input("Ingresa tu usuario: ")
    print("")
    try:
        clave=int(input("Ingrese su clave númerica: "))
        print("")
    except ValueError:
        print("Ha ingresado un valor distinto a númerico: ")
    else:
            if user == usuario and clave == contra:
                print("Has inciado sesión con éxito")
            break

#costos distancia
costomenor10000 = 3000
costomayor10000 = 5000
costomayor20000 = 7000
costomayor30000 = 8000

#costosengramos

costomayor5000 = 150
costomenor5000 = 100



while True:
    print("Ahora elige una de las opciones")
    print("1.Enviar paquete")
    print("2.Ver recaudación total")
    print("3.Salir")
    print("")
    opc=int(input("Selecciona la opción que prefieras: "))
    print("")

    if opc == 2:
        print("Debes enviar algo antes.")
        print("")

    if opc == 1:
        print("Bien, ahora ingresa la distancia a recorrer del paquete")
        print("")
        try:
            distancia= int(input("Ingrese distancia en metros: "))
            print("")
            
        except ValueError:
            print('Ha ingresado un "valor" distinto de un número')
        else:
            print(f"La distancia es: {distancia}")
            print("")

        if distancia <= 10000:
            print(f"El costo en distancia es de: {costomenor10000}")
            print("")
            costodistancia= costomenor10000
            try:
                gramos = int(input("Ahora ingresa la cantidad en gramos: "))
            except ValueError:
                print('Ha ingresado un "valor" distinto de un número')
            else:
                print(f"La cantidad en gramos es: {gramos}")
                print("")
            if gramos > 5000:
                print(f"El precio del total de gramos es {gramos*costomayor5000}")
                preciogramos = gramos*costomayor5000
            elif gramos < 5000:
                print(f"El  precio del total de gramos es {gramos*costomenor5000}")
                preciogramos = gramos*costomenor5000
                totalapagar = costodistancia + preciogramos
                



        elif distancia < 19999 :
                print(f"El costo en distancia es de: {costomayor10000}")
                costodistancia = costomayor10000

                try:
                    gramos = int(input("Ahora ingresa la cantidad en gramos: "))
                except ValueError:
                    print('Ha ingresado un "valor" distinto de un número')
                else:
                    print(f"La cantidad en gramos es: {gramos}")
                    print("")
                if gramos > 5000:
                    print(f"El precio del total de gramos es {gramos*costomayor5000}")
                    preciogramos = gramos*costomayor5000
                elif gramos < 5000:
                    print(f"El precio del total de gramos es {gramos*costomenor5000}")
                    preciogramos = gramos*costomenor5000
                    totalapagar = costodistancia + preciogramos
            


        elif distancia < 29999  :
                print(f"El costo en distancia es de: {costomayor20000}")
                costodistancia = costomayor20000
                try:
                    gramos = int(input("Ahora ingresa la cantidad en gramos: "))
                except ValueError:
                    print('Ha ingresado un "valor" distinto de un número')
                else:
                    print(f"La cantidad en gramos es: {gramos}")
                    print("")
                if gramos >= 5000:
                    print(f"El precio del total de gramos es {gramos*costomayor5000}")
                    preciogramos = gramos*costomayor5000
                elif gramos < 5000:
                    print(f"El precio del total de gramos es {gramos*costomenor5000}")
                    preciogramos = gramos*costomenor5000
                    totalapagar = costodistancia + preciogramos


        elif distancia >= 30000:
                print(f"El costo en distancia es de: {costomayor30000}")
                costodistancia = costomayor30000
                try:
                    gramos = int(input("Ahora ingresa la cantidad en gramos: "))
                except ValueError:
                    print('Ha ingresado un "valor" distinto de un número')
                else:
                    print(f"La cantidad en gramos es: {gramos}")
                    print("")
                if gramos >= 5000:
                    print(f"El precio del total de gramos es {gramos*costomayor5000}")
                    preciogramos = gramos*costomayor5000
                elif gramos < 5000:
                    print(f"El precio del total de gramos es {gramos*costomenor5000}")
                    preciogramos = gramos*costomenor5000
                    totalapagar = costodistancia + preciogramos

   


    continuar = input("¿Desea cancelar el viaje o confirmarlo? 'si' para cancelar. 'no' para ver la boleta. (si/no): ")
    if continuar.lower() != 'no':
        print("Su envío ha sido cancelado")
        break
    if continuar.lower() != 'si':

        while True:
            print("/"*100)
            print(f"El total a pagar es: {totalapagar}")
            pago = float(input("Ingrese el monto a pagar: "))
            if pago < totalapagar:
                print(f"El pago es insuficiente. Faltan ${totalapagar - pago}")
            elif pago > totalapagar:
                print(f"Gracias por su compra. Su cambio es ${pago - totalapagar}")
                break
            else:
                print("Gracias por su compra.")
                print("/"*100)
                break
        break
        
