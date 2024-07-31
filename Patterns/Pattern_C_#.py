try:
    size = (int(input("Enter the size of the triangle: ")))
    if size >= 1:
        for row in range(1, size + 1):
            for col in range(1, size, 1):
                print()
                if row <= col:
                    print("# ")
                else:
                    print()

except ValueError:
    print("Sorry, invalid input. Please try again.")
