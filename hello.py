from  source import trySDK
import booksSDK

book = trySDK("iman.a", 72)
print(booksSDK.add_book(book))

print(booksSDK.get_books())

print(booksSDK.get_book_by_title("iman.a"))

book = booksSDK.get_book_by_title("iman.a")

print(type(book))
