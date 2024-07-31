def count_vowels_digits(inputs):  # completed
    vowels_str = "aeiouAEIOU"
    vowelcount = 0
    digitcount = 0

    for char in inputs:
        if char in vowels_str:
            vowelcount = vowelcount + 1
            # vowelpercent = vowelcount / len(inputs) * 100
        elif char.isdigit():
            digitcount = digitcount + 1
            # digitpercent = digitcount / len(inputs) * 100
    vowelpercent = vowelcount / len(inputs) * 100
    digitpercent = digitcount / len(inputs) * 100
    print(f"Number of digits: {digitcount} ({digitpercent:.3f}%)")
    print(f"Number of vowels: {vowelcount} ({vowelpercent:.3f}%)")

    # return vowelcount, digitcount


while True:
    input_str = input("Enter a string:\n")
    count_vowels_digits(input_str)
    # print("Number of vowels:", vowels)
    # print("Number of digits:", digits)





