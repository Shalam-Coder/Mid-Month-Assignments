try:
    size = int(input("Enter the size of the triangle: "))
    for row in range(1 + size, 1):
        for col in range(1 + size, 1):
            
            if row + col >= size + 1:
                print("# ")
            else:
                print()
        print()

except ValueError:
    print("Sorry, invalid input. Please try again.")
