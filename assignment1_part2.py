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

        print(f"{self.title}, written by {self.author}.")
        pass


if __name__ == "__main__":
    a1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    a2 = Book("Walter Scott", "Ivanhoe: A Romance")

    a1.display()
    a2.display()
    pass