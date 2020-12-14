# Algorithm
class Counter:
    def __init__(self, string):
        # Initialize a dictionary
        self.dictionary = {}
        # Take a string as input
        self.string = iter(str(string))
# Then key is alphabet and value is no. of occurrences.
# If the key is found in the string then add 1 to value
# Finally iterate through the whole string and then remove the cases in dictionary having zero as value
# Then print the result dictionary.
