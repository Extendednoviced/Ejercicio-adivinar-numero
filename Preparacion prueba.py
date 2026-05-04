import os, random
os.system("cls")

try:
    inf = int(input("Ingrese el limite inferior: "))
    sup = int(input("Ingrese el limite superior: "))

    if inf >= sup:
        print("Error el numero inferior es superior al inferior")
    else:
        secreto = random.randint(inf, sup)      
        if secreto % 2 != 0:
            if secreto +1 <= sup:
                secreto += 1
            else:
                secreto -= 1

        intento1 = int(input("Intenet adivinar: "))
        
        if intento1 == secreto:
            print("Felicidades lo adivinaste")
        else:
            if intento1 < secreto:
                print("El numero es mayor")
            else:
                print("El numero es menor")  
                
        intento2 = int(input("Intenet adivinar otra vez: "))     
        
        if intento2 == secreto:
            print("Felicidades lo adivinaste")
        else:
            if intento2 < secreto:
                print("El numero es mayor")
            else:
                print("El numero es menor")

        distancia1 = abs(secreto - intento1)
        distancia2 = abs(secreto - intento2)
        
        print("Te dare una pista")
        if distancia2 < distancia1:
            print(f"El numero que buscas esta mas cerca de {intento2} que de {intento1}")
        else:
            print(f"El numero que buscas esta mas cerca de {intento1} que de {intento2}")

        intento3 = int(input("Ultimo intento: "))
        if intento3 == secreto:
            print("Felicidades lo adivinaste")
        else:
            print(f"Prediste, el numero era {secreto}")
except:
    print("Error")