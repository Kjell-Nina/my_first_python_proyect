import random
#esta libreria permite sacar la aletoriedad

def run():
    aleatorio = random.randint(1,100) #el 1er random invoca a la libreria importada, el randint singnifica que escoga un numero random entero.
    numero= int(input("Elige un numero del 1 al 100: "))
    while numero != aleatorio:
        if numero < aleatorio:
            print("Escoge un número más grande")
        else:
            print("Escoge un numero más pequeño")
        numero=int(input("Elige otro número: "))
    print("Muy bien, ganaste") #no es necesario poner un if, porr que este seria el unico 2do caso


if __name__=="__main__":
    run()