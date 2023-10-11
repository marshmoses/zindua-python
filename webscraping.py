
import requests
from bs4 import BeautifulSoup

# Function to fetch webinfo
def fetch_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# extracting book info
def extract_book_info(html_content):

    book_info = []

    soup = BeautifulSoup(html_content, 'html.parser')

    # book information

    book_section = soup.find('section', class_='article-page')
    
    if book_section:

        # info from list items

        list_items = book_section.find_all('li')

        for item in list_items:

            book_info.append(item.text.strip())

    return book_info

# save the extracted
def save_to_text_file(data, file_path):

    with open(file_path, 'w', encoding='utf-8') as file:

        for book in data:

            file.write(f"{book}\n")

# read and display data 

def read_and_display_from_text_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:

        for line in file:

            print(line.strip())

if __name__ == "__main__":
    # URL
    website_url = 'https://www.ign.com/articles/best-selling-books-of-all-time'

    # Fetch webpage info
    webpage_content = fetch_webpage_content(website_url)

    if webpage_content:
        print("Webpage content fetched successfully.")

        # Extract book information
        book_data = extract_book_info(webpage_content)

        if book_data:
            print("Book information extracted successfully.")

            # Save extracted data 

            save_to_text_file(book_data, 'book_data.txt')

            print("Data saved to 'book_data.txt'.")

            # Display 

            read_and_display_from_text_file('book_data.txt')
            
        else:
            print("Failed to extract book information.")
    else:
        print("Failed to fetch webpage content.")
