# class Movie:
#     def __init__(self,title,available_seats):
#         self.title=title
#         self.available_seats=available_seats
#     def book_ticket(self,seats):
#         print(f"{seats} tickets booked successfully.")
#         if seats <=self.available_seats:
#             self.available_seats-=seats
         
#         else:
#             print ("Not enough seats.") 

# title=input("Enter movie title:")
# available_seats=int(input("Enter available seats:"))




# movie=Movie(title,available_seats)
# book=int(input("Enter seats to book: "))
# movie.book_ticket(book)

# book=int(input("Enter seats to book: "))
# movie.book_ticket(book) 




class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        print(f"Title:{self.title}\n Author:{self.author}\n Copies: {self.copies}")

library = []

for i in range(3):
    print("\nEnter details for book", i + 1)
    title = input("Enter book title: ")
    author = input("Enter author: ")
    copies = int(input("Enter copies: "))

    book = Book(title, author, copies)
    library.append(book)

search_title = input("\nEnter book title to search: ")

found = False
for book in library:
    if book.title.lower() == search_title.lower():
        book.display_info()
        found = True
        break

if not found:
    print("Book not available")