# Algorithm
# Firstly, I would create the string iterable
# Then I would create wanted_string in which all the non-a's would be poped out.
# Then I would create a new int variable which would be the atleast no. of non-a's.

def repeatedString(string, integer):
    iter(string)
    wanted_string = str(filter(lambda a: a == "a", string))
    new_int = (len(string) - len(wanted_string)) * (integer // len(string))


input_string = input()
input_integer = int(input())
print(repeatedString(input_string, input_integer))
