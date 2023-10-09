import requests
import re

# fetch the content 
def fetch_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# exract info usindg regex

def extract_article_info(html_content):

    article_info = []

    # Define regexfor matching titles and dates

    title_pattern = r'<h3 class="post-title"><a href=".*?">(.*?)</a></h3>'

    date_pattern = r'<time class="entry-date" datetime="(\d{4}-\d{2}-\d{2})T'

    # match usin regex

    titles = re.findall(title_pattern, html_content)

    dates = re.findall(date_pattern, html_content)

    # Combine td to  list of dicts
    for title, date in zip(titles, dates):

        article_info.append({'Title': title.strip(), 'Publication Date': date.strip()})


    return article_info

if __name__ == "__main__":
    # URL
    website_url = 'https://zinduaschool.com/blog/'


    # Fetch webpage content

    webpage_content = fetch_webpage_content(website_url)

    if webpage_content:

        # Extract article information

        article_data = extract_article_info(webpage_content)


        if article_data:
            # Display the extracted data
            for article in article_data:

                print(f"Title: {article['Title']}")

                print(f"Publication Date: {article['Publication Date']}")
                
                print("-" * 30)
        else:
            print("No articles found on the page.")
    else:
        print("Failed to fetch webpage content.")
