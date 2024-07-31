try:
    size = (int(input("Enter the size of the triangle: ")))
    if size >= 1:
        for row in range(1, size + 1):
            for col in range(1, size +e 1):
                if row + col <= size + 1:
                    print("#",  end=" ")
                else:
                    print(" ", end=" ")
            print()
except ValueError:
    print("Sorry, invalid input, please try again.")

