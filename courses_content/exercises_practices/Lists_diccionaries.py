def run():
    my_list =[1, "hello", True, 4.5]
    my_dict = {"FirstNmae": "Duvan", "Edad": 20}
    list_of_diccionaries = [
        {"FirstNmae": "Duvan", "Edad": 20},
        {"FirstNmae": "Vivas", "Edad": 30},
        {"FirstNmae": "Yesid", "Edad": 50},
        {"FirstNmae": "DuvanVivas", "Edad": 10},
    ]
    dicionary_of_list = {
        "one_dicc": [1, "hello", True, 4.5],
        "two_dicc": [2, "maria", False, 5],
        "three_dicc": [3, "Bye", False, 5],
        "four_dicc": [4, "Morning", True, 7],
    }
    for key, value in  dicionary_of_list.items():
        print(key, "-", value)
    for item, dicc in  list_of_diccionaries.items():
        print(item, "-", dicc)

if __name__ == '__main__':
    run()