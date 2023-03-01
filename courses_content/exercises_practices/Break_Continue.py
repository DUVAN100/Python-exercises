from ast import If


def run():
    for contador in range(10):
        if contador % 2 != 0:
            continue
        print(contador)
def secund_run():
    for i in range(0, 99):
        print(i)
        if i == 44:
            break
   
def three_run():
    texto = input("digite un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)
if __name__ == '__main__':
    run()
    print("ya paro el primer ciclo")
    secund_run()
    three_run()