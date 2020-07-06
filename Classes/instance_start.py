# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: Add Properties  
        self.author = author
        self.pages = pages
        self.price = price
        # The double underscores are used to show that this __secret would give us a syntax error if used in another
        # class

        self.__secret = "This is a secret attribute"

    # TODO: Create instances methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        # The underscore is used so that nobody tries to access it outside the class
        self._discount = amount


# TODO: Create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: Print the price of book1
print(b1.getprice())

# TODO: Try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())
    
# TODO: Properties with double underscores are hidden by the interpreter
# This shows that the attribute __secret was renamed to _Book__secret because of the double underscores
print(b2._Book__secret)
