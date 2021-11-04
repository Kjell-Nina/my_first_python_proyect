# a=0
# print("2 elevado a "+ str(a)+"es igual a: "+ str(2**a))

# a=1
# print("2 elevado a "+ str(a)+"es igual a: "+ str(2**a))

# a=2
# print("2 elevado a "+ str(a)+"es igual a: "+ str(2**a))

# a=3
# print("2 elevado a "+ str(a)+"es igual a: "+ str(2**a))

# a=4
# print("2 elevado a "+ str(a)+"es igual a: "+ str(2**a))

# a=5
# print("2 elevado a "+ str(a)+"es igual a: "+ str(2**a))

def run():
    LIMITE = 1000 #Si esta con mayusculas es una constante
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador)+'es igual a: ' +str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
    

if __name__ =='__main__':
    run()

