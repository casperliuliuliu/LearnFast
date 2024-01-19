import requests
from bs4 import BeautifulSoup

def get_cambridge_definition(word):
    base_url = "https://dictionary.cambridge.org/dictionary/english/"
    url = f"{base_url}{word}"
    print(url)
    # Send an HTTP request to the website
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the definition from the HTML
        definition = soup.find("div", {"class": "def ddef_d db"})
        pos = soup.find("div", {"class": "posgram dpos-g hdib lmr-5"})
        print(pos)
        # Check if a definition was found
        if definition:
            # Join text within the div tag with spaces between words
            definition = ' '.join(definition.stripped_strings)
            return definition
        else:
            return f"No definition found for {word}"

    # else:
    #     return f"Failed to retrieve data. Status code: {response.status_code}"
        
def store_definition(word, definition, filename="vocabulary.txt"):
    with open(filename, 'a') as file:
        file.write(f"{word}: {definition}\n")

def sort_and_save(filename="vocabulary.txt"):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines.sort()

    with open(filename, 'w') as file:
        file.writelines(lines)
        
if __name__ == "__main__":
    word_to_search = "nostalgia"
    definition = get_cambridge_definition(word_to_search)
    print(f"Definition of '{word_to_search}':\n {definition}")
            
    # store_definition(word_to_search, definition)
    
    # sort_and_save()