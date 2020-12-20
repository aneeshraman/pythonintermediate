def isPalindrome(char):
    return char == char[::-1]


string = input("Enter a string: ")
print(isPalindrome(string))
