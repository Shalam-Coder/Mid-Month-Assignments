try:
    size = int(input("Enter the size of the triangle"))
    if size >= 1:
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                if row >= col:
                    print(col, end=" ")
                else:
                    print()
except ValueError:
    print("Sorry, invalid input. Try again later.")
    quit()
