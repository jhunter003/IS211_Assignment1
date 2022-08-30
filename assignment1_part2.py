class Book:
    def __init__(self, author, title):
        """
        Constructor of an Author Class
        :param author: The name of the author
        :param title: The name of the book
        """
        self.author = author
        self.title = title
        pass

    def display(self):
        """Display the author's name and book title"""

        print(f"I'm an author. My name is {self.author}.")
        print(f"I wrote the book called {self.title}.")
        pass


if __name__ == "__main__":
    a1 = Book("first name1", "Book Title1")
    a2 = Book("first name2", "Book Title2")

    a1.display()
    a2.display()
    pass