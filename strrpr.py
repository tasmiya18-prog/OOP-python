lass Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"Name of the book is {self.title} author is {self.author} and price is {self.price}"
    
    def __repr__(self):
         return f"(Name of the book is {self.title} author is {self.author} and price is {self.price})"
    
a = Book("abc","abcd",130)
b = Book("xyz","xyzz",167)

print(a)
print(b)

books = [a,b]
print(books)

