length = None
breadth = None
try:
    length = int(input("Enter the length of the rectangle: "))

except ValueError:
    print(Exception("Invalid length"))

try:
    breadth = int(input("Enter the breadth of the rectangle: "))

except ValueError:
    print(Exception("Invalid breadth"))

if length is not None and breadth is not None:
    print(f"The perimeter of the rectangle is {2 * (length + breadth)}")
    print(f"The area of the rectangle is {length * breadth}")

elif length is None and breadth is None:
    print(Exception("Because both length and breadth were invalid so could not print the area and perimeter"))

elif length is None:
    print(Exception("Because length was invalid so could not print the area and perimeter."))

elif breadth is None:
    print(Exception("Because breadth was invalid so could not print the area and perimeter."))
