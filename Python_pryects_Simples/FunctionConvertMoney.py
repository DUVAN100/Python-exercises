def conversor(tipo_pesos, valor_dolar) :
    pesos = float(input("Cuantos pesos" + tipo_pesos + " tienes: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tientes $'  + dolares+ ' dolares') 

moneda = """---Digite 1 si tu moneda es colombiana  🪙
            ---Digite 2 si tu moneda es Argentina"""
moneda = float(input(moneda))
if moneda == 1 :
    conversor("colombianos", 3875)
elif moneda == 2 :
    conversor("Argentinos", 0.02342)
else :
    print("Digite un valor correcto")
print("Esto fue todo Muchas gracias")