
# Example 1
# start_string = "hackerhappy"
# desired_string = "hackerrank"
# desired_operations = 9
# min_operations = 0
# start_string = "hackerhapp"
# desired_string = "hackerrank"
# min_operations = 1
# desired_operations = 9
# start_string = "happ"
# desired_string = "rank"
# desired_operations = 9
# min_operations = 5

# Example 2
# start_string = "abac"
# desired_string = "abad"
# desired_operations = 7
# min_operations = 0
# start_string = "c"
# desired_string = "d"
# min_operations = 2
# desired_operations = 7

# Example 3
# start_string = "abcdef"
# desired_string = "abcfghi"
# desired_operations = 5
# min_operations = 0
# start_string = "def"
# desired_string = "fghi"
# desired_operations = 5
# min_operations = 0
# start_string = ""
# desired_string = "fghi"
# desired_operations = 5
# min_operations = 3
# start_string = desired_string = "fghi"
# desired_operations = 5
# min_operations = 7


input_start_string = input()
input_desired_string = input()
int_input_desired_operations = int(input())


def append_and_delete(start_string, desired_string, desired_operations):
    # Where length of start_string > length of desired_string
    if len(start_string) > len(desired_string):
        start_string = start_string


print(append_and_delete(input_start_string, input_desired_string, int_input_desired_operations))
