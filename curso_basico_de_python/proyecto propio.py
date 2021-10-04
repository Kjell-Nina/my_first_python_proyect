def run():
    vidas =4
    while vidas > 0:
        texto=int(input("Adivina el número entre 1 y 10. Tienes "+str(vidas)+ " intentos: "))
        if texto == 3:
            print("Muy bien, adivinaste")
            break
        if texto>10:
            print("Escoge un numero valido")
        elif texto != 3:
            vidas-=1
            print("Vuelve a intentar")
    if vidas==0:
        print("Te quedaste sin vidas")
        print("Suerte para la proxima")


if __name__=="__main__":
    run()