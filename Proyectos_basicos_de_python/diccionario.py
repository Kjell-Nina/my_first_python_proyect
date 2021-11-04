def run():
    my_diccionario =  {
        "llave1":1,
        "llave2":2,
        "llave3":3,
    }
    # print(my_diccionario["llave1"])
    # print(my_diccionario["llave2"])
    # print(my_diccionario["llave3"])
    poblacion={
        "Perú":43000,
        "Chile":34000,
        "Colombia": 19000
    }
    # for pais in poblacion.keys():#como resultado será las los paises(osea las llaves)
    #     print(pais)

    # for pais in poblacion.values(): #El resultado será los valorez de las llaves
    #     print(pais)

    for pais, gente in poblacion.items(): #parra que te genere todos los valores
        print(pais+ " tiene "+ str(gente)+" habitantes")




if __name__=="__main__":
    run()