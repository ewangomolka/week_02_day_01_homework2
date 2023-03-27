

class Book:
    def __init__(self, title, author, year, pulped):
        self.title = title
        self.author = author
        self.date_of_publication = year
        self.number_pulped = pulped

    def read(self):
        return "It put me into a coma"
        
    
