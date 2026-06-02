class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        age = current_year - self.publication_year
        return age

   
    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"



book1=Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "978-0-7475-3269-9", 1997)
book2=Book("The Alchemist", "Paulo Coelho", "0-06-250217-4", 1993)
book3=Book("A Man Called Ove", "Fredrik Backamn", "9781476738024", 2012)


print(book1.get_summary())
print(f"Age_of_thebook: {book1.get_age()} years.")