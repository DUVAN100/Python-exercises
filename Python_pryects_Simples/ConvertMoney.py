from re import DOTALL


pesos = float(input("Cuantos pesos colombainos tienes: "))
valor_dolar= 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tientes $'  + dolares+ ' dolares')