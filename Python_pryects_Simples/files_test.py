from tkinter.font import names


def read():
    numebers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8")as f:
        for line in f:
            numebers.append(line)
    print(numebers)

def write():
    edades = ["25", "12", "30", "18", "23"]
    with open("archivos/numbers.txt", "w") as f:
        for edad in edades: 
            f.write(edad)
            f.write("\n")
def overwrite():
    names = ["duvan", "Gregorio", "Marta", "Susana", "Jose"]
    with open("archivos/numbers.txt", "a") as a:
        for name in names: 
            a.write(name)
            a.write("\n")
    
def run():
    read()
    write()
    overwrite()

if __name__  == "__main__":
    run()