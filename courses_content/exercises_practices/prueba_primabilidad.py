import math

def is_prime(numero):
  for i in range(2,int(math.sqrt(numero))+1):
    if (numero % i) == 0:
      return False
    return True
    
def run():
    numero = int(input("Digite un numero: "))
    if is_prime(numero):
        print("Es primmo")
    else:
        print("No es primo")




if __name__ == '__main__':
    run()