
def conversor(tipo_moneda,valor_dolar):
    moneda = input('¿Cuantos '+ tipo_moneda +' tines?: ')
    moneda = float(moneda)
    #valor_dolar = 4.025 se quita por que ya se invoca en la parte de función
    dolares = moneda / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $'+ dolares + ' dolares')

menu = """
Bienvenidos al conversor de monedas 💰

1 - Soles
2 - Pesos Mexicanos
3 - Pesos Colombianos

Elige una opción: """
opcion = int(input(menu))
if opcion == 1:
    conversor('soles',4.09)
elif opcion == 2:
    conversor("pesos mexicanos", 18)
elif opcion == 3:
    conversor("pesos argentinos",204)
else:
    print("Escribe una opción correcta por favor")
