a = None
b = None
a_is_wrong = False
b_is_wrong = False
try:
    a = int(input("Enter a number: "))

except ValueError:
    print("Wrong Input for the first number")
    a_is_wrong = True

try:
    b = int(input("Enter a number: "))

except ValueError:
    print("Wrong Input for the second number")
    b_is_wrong = True

if a_is_wrong == False and b_is_wrong == False:
    print(f"Sum of the numbers is: {a + b}")
    print(f"Difference of the numbers is: {a - b}")
    print(f"Product of the numbers is: {a * b}")
    print(f"Quotient of first number by second number is: {a / b}")
    print(f"Remainder of first number by second number is: {a % b}")

elif a_is_wrong and b_is_wrong:
    print(Exception("\nNot able to print: Because both the first and the second number"
                    " were wrong"))

elif a_is_wrong:
    print(Exception("\nNot able to print: Because the first number is wrong"))

elif b_is_wrong:
    print(Exception("\nNot able to print: Because the second number is wrong"))
