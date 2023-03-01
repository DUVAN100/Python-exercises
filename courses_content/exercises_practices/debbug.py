def divisors(num):
    divisors =[]
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("ya se acabo")
    except ValueError :
        print("Ingrese un numero por favor..")


if __name__ == "__main__":
    run()