def primo(numero):
    producto=1
    for i in range(1,numero):
        producto *= i
    if (producto+1)%numero==0:
        return True
    else:
        False


def run():
    numero=int(input("Escribe un numero "))
    if primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__=="__main__":
    run()
