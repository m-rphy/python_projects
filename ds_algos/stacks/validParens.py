#  Write a function that takes in a string and returns a 'True'
#  if the parentheses are balances or 'False' if they are not

# Input: s = "()[]{}"
# Output: True


def validParens(str):
    dict = {"[": "]", "{": "}", "(": ")"}
    stack = []

    for char in str:
        if char in dict:
            stack.append(char)
        elif stack and char == dict[stack[-1]]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


print(validParens("[{[()]}]()"))
