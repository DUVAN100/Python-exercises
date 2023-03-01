def divisors(num):
    divisors =[]
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
        num = int(input("Ingresa un numero: "))
        assert num.isnumeric(), "Ingrese un numero por favor.."
      #  print(divisors(num))
        print("ya se acabo")


if __name__ == "__main__":
    run()