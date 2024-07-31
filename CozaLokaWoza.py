def coza_loza_woza():  # why wont it format correctly?
    for number in range(1, 111):  # include prime numbers as well
        # print(number)
        if number % 3 == 0 and number % 5 == 0:
            print("CozaLoza", end=" ")
        elif number % 3 == 0 and number % 7 == 0:
            print("CozaWoza", end=" ")
        elif number % 5 == 0 and number % 7 == 0:
            print("LozaWoza", end=" ")
        elif number % 3 == 0:
            print("Coza", end=" ")
        elif number % 5 == 0:
            print("Loza", end=" ")
        elif number % 7 == 0:
            print("Woza", end=" ")
        elif number % 11 == 0:
            print()
        else:
            print(number)


coza_loza_woza()
