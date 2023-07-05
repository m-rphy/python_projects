#  Write a function that takes in
#  a string and returns a boolean;
#  'True" if the string is a valid palindrome
#  and 'False' if it is not


def validPalindrom(str):
    l, r = 0, len(str) - 1

    while l <= r:
        if str[l] != str[r]:
            return False
        else:
            l += 1
            r -= 1

    return True


print(validPalindrom("racecar"))  # -> True
print(validPalindrom("notTrue"))  # -> False
