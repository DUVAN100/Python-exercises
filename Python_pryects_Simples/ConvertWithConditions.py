moneda = """---Digite 1 si tu moneda es colombiana  🪙
            ---Digite 2 si tu moneda es Argentina"""
moneda = float(moneda)
if moneda == 1 :
    pesos = float(input("Cuantos pesos colombainos tienes: "))
    valor_dolar= 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tientes $'  + dolares+ ' dolares')
elif moneda == 2 :
        pesos = float(input("Cuantos pesos Argentions tienes: "))
        valor_dolar= 0.02342
        dolares = pesos * valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print('Tientes $'  + dolares+ ' dolares')        
print("Esto fue todo Muchas gracias")

