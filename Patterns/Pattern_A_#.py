try:
    size = (int(input("Enter the size of your pattern: ")))
    if size >= 1:
        for row in range(1, size, 1):
            for col in range(1, size, 1):
                if row >= col:
                    print("#", end=" ")
                else:
                    print("", end=" ")
            print()
except ValueError:
    print("Sorry, invalid input.")