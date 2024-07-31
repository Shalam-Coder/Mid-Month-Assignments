def extract_digits(nums):
    result = ""  # blank start
    while nums > 0:
        digit = nums % 10  # takes the lowest sigfig out
        result = result + str(digit) + " "  # concatenation
        nums = nums // 10  # drops the least sigfig
    print(result)
    return result  # returns reversed order


num = (int(input("Input a integer:\n")))
extract_digits(num)  # completed
