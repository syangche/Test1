books_list = []
authors_set = set()
books_dict = {}

books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Structures and Algorithm")
authors_set.add("Jane Doe")
books_dict["Data Structures and Algorithm"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

search_book = input("Enter the book you want to search for: ").lower()
if search_book in books_list:
    print(f"Book found! Author: {books_dict[search_book]}\n") 
else:
    print("Book not found!\n")
for book in books_list:
    print(book)    

remove_book = input("\nEnter the book you want to remove: ")
if remove_book in books_list:
    remove_author = books_dict[remove_book]
    books_list.remove(remove_book)
    authors_set.remove(remove_author)
    del books_dict[remove_book]
    print("Book removed successfully!")
else:
    print("Book not found!")
    
print(books_list)