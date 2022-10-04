from ast import If


def run():
    squares = [ i**4 for i in range(1, 10) if i % 4 ==0]
    print(squares)


if __name__ == "__main__":
    run()