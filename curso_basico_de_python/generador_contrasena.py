import random

def cont_aleatorio():
    mayusculas = ["A" ,"B" ,"C" ,"D" ,"E"]
    minusculas =  ["a" ,"b" ,"c" ,"d" ,"e"]
    simbolos = ["!" ,"#" ,"$" ,"&"]
    numeros = ["1", "2", "3", "4", "5"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena= "".join(contrasena)
    return contrasena

def run():
    contrasena = cont_aleatorio()
    print("Tu nueva contraseña es: " + contrasena)

if __name__=="__main__":
    run()