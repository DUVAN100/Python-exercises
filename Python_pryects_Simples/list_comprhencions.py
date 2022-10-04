import math


def run():
  #  squares = []
  #  for i in range(1, 101):
  #      if i % 3 != 0:
  #          squares.append(i**2)
   
   #list comprehenions
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)


if __name__ == "__main__":
    run()