import requests
from bs4 import BeautifulSoup
from lxml import html

# Define user agent to mimic a web browser request (type "my user agent" in your browser )
headers = {
    'User-Agent': 'put you browser user agent here'
}

# Define the URL of the MICCAI 2022 papers page
url = "https://conferences.miccai.org/2022/papers/categories/"

# Send an HTTP GET request to the URL
res = requests.get(url, headers=headers)

# Parse the response content with lxml and BeautifulSoup
tree = html.fromstring(res.content)
soup = BeautifulSoup(html.tostring(tree), 'html.parser')

# Extract links to individual papers
links = tree.xpath("//div[@class='posts-list-item']/li/a")

# Initialize a list to store paper URLs
papers = []
for link in links:
    url = 'https://conferences.miccai.org' + link.get('href')
    papers.append(url)

# Find unique paper URLs
uniques = list(set(papers))

# Initialize a list to store good papers with links to paper, dataset, and code
good_papers = []

# Loop through the unique paper URLs
for url in uniques:
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        paragh = soup.find_all('p')
        na_found = False  # Flag to check if "N/A" is found on the website
        for para in paragh:
            if "N/A" in para.get_text():
                na_found = True
                break  # Exit the loop if "N/A" is found
        if not na_found:
            good_papers.append(url)
    else:
        print(f"Failed to fetch content for {url}")

# Define areas of interest
area_of_interest = [
    '/2022/papers/categories#Machine Learning - Continual Learning',
    '/2022/papers/categories#Machine Learning - Transfer learning'
]

# Initialize a list to store the final papers in the areas of interest
final_papers = []

# Loop through the good papers
for url in good_papers:
    res = requests.get(url)
    if res.status_code == 200:
        tree = html.fromstring(res.content)
        soup = BeautifulSoup(html.tostring(tree), 'html.parser')
        paragh = tree.xpath("//div[@class='post-categories']/a")
        found_match = False  # Flag to check if any item from the 'default' list is found on the website
        for para in paragh:
            text = para.get('href')
            for item in area_of_interest:
                if item == text:
                    found_match = True
                    break  # Exit the loop if a match is found
        if found_match:
            final_papers.append(url)
    else:
        print(f"Failed to fetch content for {url}")

# Print the list of final paper URLs
print("Final papers:", final_papers)
