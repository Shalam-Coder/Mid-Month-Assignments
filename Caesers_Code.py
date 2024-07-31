def caesar_cipher():
    n = 3
    plaintxt = input("Enter a string you want encrypted: ")
    chipertext = ""

    for char in plaintxt:
        if 'A' <= char <= 'W':
            encodedval = ord(char) + n
            chipertext = chipertext + chr(encodedval)
        elif 'a' <= char < 'w':
            encodedval = ord(char) + n
            chipertext = chipertext + chr(encodedval)
        elif char == 'X':
            chipertext = chipertext + 'A'
        elif char == 'Y':
            chipertext = chipertext + 'B'
        elif char == 'Z':
            chipertext = chipertext + 'C'
        elif char == 'x':
            chipertext = chipertext + 'a'
        elif char == 'y':
            chipertext = chipertext + 'b'
        elif char == 'z':
            chipertext = chipertext + 'c'
        else:
            chipertext = chipertext + char

    return chipertext


while True:
    outputstr = caesar_cipher()
    print(outputstr)
