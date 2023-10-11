 # MICCAI Papers Extraction

This Python script scrapes the MICCAI 2022 conference website to extract paper links in your area of interest. It only fetches papers whose authors have provided the paper, dataset, and code links. You can also modify the year accordingly.

## How to Run the code

- 1. Ensure you have Python installed on your system.
- 2. Install the required Python libraries using pip:

   ### pip install requests beautifulsoup4 lxml

## Open your terminal and navigate to the directory where the script is located.

Run the script

### python miccai_paper_scraper.py

# note

There are many areas of interest available on the Miccai website (search by topics). Following are a few of them:

- Machine Learning - Continual Learning, 
- Machine Learning - Active Learning, 
- Machine Learning - Data efficient Learning, 
- Machine Learning - Interpretability

select the exact same area of interest from the Miccai website and append this ""/2022/papers/categories#"" with your area of interest.

## Example:

area_of_interest = ['/2022/papers/categories#Machine Learning - Continual Learning','/2022/papers/categories#Machine Learning - Transfer learning']
