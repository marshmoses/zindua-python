import csv
books = [
    {
        'title': "Mstahiki Meya",
        'author': 'Timothy Arege',
        'ISBN': '254-112008-7',
        'price': 500
    },
    {
        'title': 'Damu Nyeusi',
        'author': 'Ken Walibora',
        'ISBN': '254-28423-6',
        'price': 700
    },
    {
        'title': 'The Caucasian Circle',
        'author': 'Bertolt Brecht',
        'ISBN': '2547356-1',
        'price': 650
    },
    {
        'title': "Shreds of Tenderness",
        'author': 'John Ruganda',
        'ISBN': '212-0-4',
        'price': 950
    },
    {
        'title': 'maxmillan Dictionary',
        'author': 'Oxford Press',
        'ISBN': '44-0-486-2-1',
        'price': 2500
    },
    {
        'title': 'Kiswahili Kitukuzwe',
        'author': 'Wallah Bin Wallah',
        'ISBN': '256-0-316',
        'price': 1000
    }
]
csv_file = 'challenge-csv'

#Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    fieldnames = ['title', 'author', 'ISBN', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()


def read_books_from_csv(file_name):
    """
    Reads a CSV file containing information about books and returns a list of dictionaries.

    Args:
    file_name (str): The name of the CSV file to read.

    Returns:
    list: A list of dictionaries, where each dictionary represents a book with keys for
          title, author, ISBN, and price.
    """
    books = []
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append({
                    'title': row['title'],
                    'author': row['author'],
                    'ISBN': row['ISBN'],
                    'price': float(row['price'])
                })
        return books
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
# books_list = read_books_from_csv('books.csv')

def search_books_by_author(author_name):
    """
    Searches for books by a specific author in a list of books.

    Args:
    books (list): A list of dictionaries, where each dictionary represents a book.
    author_name (str): The name of the author to search for.

    Returns:
    list: A list of dictionaries representing books written by the specified author.
    """
    author_books = []
    for book in books:
        if book['author'].lower() == author_name.lower():
            author_books.append(book)
    return author_books
#You can use this function by passing in the list of books and the author's name as arguments. It will return a list of dictionaries representing books written by the specified author, based on a case-insensitive comparison of author names.

def search_book_by_isbn(isbn):
    """
    Searches for a book by ISBN in a list of books and returns the title and price.

    Args:
    books (list): A list of dictionaries, where each dictionary represents a book.
    isbn (str): The ISBN of the book to search for.

    Returns:
    dict or None: A dictionary containing the 'title' and 'price' of the book if found,
                  or None if the book is not found.
    """
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None

# Example usage:
# book_info = search_book_by_isbn(books_list, '254-112008-7')
# if book_info:
#     print(f"Title: {book_info['title']}, Price: {book_info['price']}")
# else:
#     print("Book not found.")

def search_books_by_price_range(min_price, max_price):
    """
    Searches for books within a specified price range in a list of books.

    Args:
    books (list): A list of dictionaries, where each dictionary represents a book.
    min_price (float): The minimum price of books to include in the result.
    max_price (float): The maximum price of books to include in the result.

    Returns:
    list: A list of dictionaries representing books that fall within the specified price range.
    """
    result = []
    for book in books:
        book_price = float(book['price'])
        if min_price <= book_price <= max_price:
            result.append(book)
    return result

# Example usage:
# books_in_price_range = search_books_by_price_range(books_list, 500, 1000)
# for book in books_in_price_range:
#     print(f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}")

def main():
    # Read the list of books from a CSV file
    file_name = 'books.csv'
    books_list = read_books_from_csv(file_name)

    while True:
        print("\nMenu:")
        print("1. Search books by author")
        print("2. Search books by ISBN")
        print("3. Search books by price range")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            author_name = input("Enter author's name: ")
            author_books = search_books_by_author(author_name)
            if author_books:
                print("\nBooks by", author_name, ":")
                for book in author_books:
                    print(f"Title: {book['title']}, ISBN: {book['ISBN']}, Price: {book['price']}")
            else:
                print("No books by that author found.")

        elif choice == '2':
            isbn = input("Enter ISBN: ")
            book_info = search_book_by_isbn(isbn)
            if book_info:
                print("\nBook found:")
                print(f"Title: {book_info['title']}, Price: {book_info['price']}")
            else:
                print("Book not found.")

        elif choice == '3':
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            price_range_books = search_books_by_price_range(min_price, max_price)
            if price_range_books:
                print("\nBooks within price range:")
                for book in price_range_books:
                    print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Price: {book['price']}")
            else:
                print("No books within that price range found.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
