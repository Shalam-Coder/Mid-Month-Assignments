def exchange_ciper():
    plaintext = input("Enter a plaintext string (mixed letters only): ")

    chiphertxt = ""

    for char in plaintext:
        if 'A' <= char <= 'Z':
            asciiofchar = ord(char) - ord('A')
            asciiofchar = ord('Z') - asciiofchar
            chiphertxt = chiphertxt + chr(asciiofchar)
        elif 'a' <= char <= 'z':
            asciiofchar = ord(char) - ord('a')
            asciiofchar = ord('z') - asciiofchar
            chiphertxt = chiphertxt + chr(asciiofchar)
        else:
            chiphertxt = chiphertxt + char

    return chiphertxt


outputstr = exchange_ciper()
print(outputstr)

'''
65                                                                          90  #  lowercase a-z = 97 - 122
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
Z, Y, X, W, V, U, T, S, R, Q, P, O, N, M, L, K, J, I, H, G, F, E, D, C, B, A
'''