import csv

# Define a list of dictionaries for book information
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

# CSV file
csv_file = 'books-csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    fieldnames = ['title', 'author', 'ISBN', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # book=data for each book writer row writes data foreach book
    for book in books:
        writer.writerow(book)



