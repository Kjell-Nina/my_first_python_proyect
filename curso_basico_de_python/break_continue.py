def run():
    # for A in range(501):
    #     if A %2 != 0 :
    #         continue 
    #     print(A)


    # for i in range(10000):
    #     print(i)
    #     if i ==5000:
    #         break
    #     #print(i)    podria ir aqui y no abria problema

    texto= input("Escribe un texto: ")
    for letra in texto:
        if letra =="o":
            break
        print(letra)


if __name__=="__main__":
    run()