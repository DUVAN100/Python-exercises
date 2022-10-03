def run():
    mi_diccionario = {
            'llave1': 1,
            'llave2': 2,
            'llave3': 3,
    }
    print(mi_diccionario['llave3'])
    poblacion_paises = {
        'colombai': 52000,
        'Argentina': 200000,
        'Brazil': 40000,
    }
    print(poblacion_paises['colombai'])
    for pais, poblacion in poblacion_paises.items():
      print(pais+ ' tiene '+ str(poblacion)+ ' habitantes.')
    for pais in poblacion_paises.values():
      print(pais)



    

if __name__ == '__main__':
    run()