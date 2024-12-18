'''WAP to print bookdata as title, year, author etc with class and object
concept'''

class Books:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def display_info(self):
        print(f"Name of the Book: {self.title}, Year of Publish: {self.year},Name of the author: {self.author}")

#Creating Objects
Book1 = Books("ABC",2007,"William")
Book2 = Books("XYZ",2010,"Stefan")

#Accessing object methods
Book1.display_info()
Book2.display_info()
