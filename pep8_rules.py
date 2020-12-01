# Correct:

# Aligned with opening delimiter.
# foo = long_function_name(var_one, var_two,
#                        var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
# def long_function_name(
#         var_one, var_two, var_three,
#         var_four):
#     print(var_one)

# Hanging indents should add a level.
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)

# Hanging indents *may* be indented to other than 4 spaces.
# foo = long_function_name(
#   var_one, var_two,
#   var_three, var_four)
# No extra indentation.
# if (this_is_one_thing and
#     that_is_another_thing):
#     do_something()
#
# # Add a comment, which will provide some distinction in editors
# # supporting syntax highlighting.
# if (this_is_one_thing and
#     that_is_another_thing):
#     # Since both conditions are true, we can frobnicate.
#     do_something()
#
# # Add some extra indentation on the conditional continuation line.
# if (this_is_one_thing
#         and that_is_another_thing):
#     do_something()
# my_list = [
#     1, 2, 3,
#     4, 5, 6,
#     ]
# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f',
#     )
# my_list = [
#     1, 2, 3,
#     4, 5, 6,
# ]
# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f',
# )
# Limit all lines to maximum 79 characters
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
# Correct:
#
# code: int
#
# class Point:
#     coords: Tuple[int, int]
#     label: str = '<unknown>'
