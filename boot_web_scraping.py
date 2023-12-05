#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup # For collecting data
import json # To create a JSON file
import requests # For sending request to the server to get data


# In[2]:


# Define a function to calculate median value

def calculate_median(prices):
    """
    Calculates the median value of a list of prices.

    Parameters:
    - prices (list of float): A list of numerical values representing prices.

    Returns:
    - float: The median value of the provided prices.
    """
    sorted_prices = sorted(prices)
    n = len(sorted_prices)

    if n % 2 == 0:
        median = (sorted_prices[n//2 - 1] + sorted_prices[n//2]) / 2
    else:
        median = sorted_prices[n//2]

    return median


# Use this function with a working URL
def scrape_boots_website(url):
    """
    Scrapes product information from the Boots website.

    Parameters:
    - url (str): The URL of the Boots website page to be scraped.

    Returns:
    - BeautifulSoup: A BeautifulSoup object representing the parsed HTML content of the webpage.

    Example:
    >>> url = "https://www.boots.com/health-pharmacy/medicines-treatments/sleep?paging.index=0&amp;paging.size=24&amp;sortBy=mostRelevant&amp;criteria.category=wellness---sleep&amp;criteria.brand=Bach+Rescue+Remedy---Boots"
    >>> soup = scrape_boots_website(url)
    >>> # Countinue with Ln [4]
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


# In[3]:


# Give file name or path, depending on the location of your file
file_path = 'orignal.html' 

# Read the contents of the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parsing the HTML content to extract different data's
soup = BeautifulSoup(html_content, 'html.parser')


# In[4]:


# Creating two list for storing respected values
result_list = [] # For appending all the items
prices = [] # For appending all the "numeric_price"

# Fetching all the products information from the webpage
products_items = soup.find_all('div', class_='oct-grid__row oct-grid__row--full-width oct-listers-hits')

# Loop to find required item from the product list
for item in products_items:
    
    # Finding Title from the products_items
    try:
        item_titles = item.find_all('h3', {'class': 'oct-text oct-text--standard oct-text--size_m oct-aem-text oct-aem-text--h3--variant-2 oct-teaser__title oct-teaser-with-listers'})
    except:
        print("")
        
    # Finding Price from the products_items
    try:
        item_prices = item.find_all('p', {'class': 'oct-text oct-text--standard oct-text--size_m oct-aem-text oct-aem-text--p--variant-subtext oct-teaser__productPrice'})
    except:
        print("")
    
    # Finding Offer from the products_items
    try:
        item_offer = item.find_all('div', {'class': 'oct-teaser__wrap'})
    except:
        print("")

    # Running a loop to capture information of each product     
    for title, price, offer in zip(item_titles, item_prices, item_offer):
        title_text = title.get_text(strip=True)
        price_text = price.get_text(strip=True)
        offer_text = offer.get_text(strip=True)
        
        # "result_list" accumulates these dictionaries for all products on the page 
        result_list.append({'Title': title_text, 'Price': price_text, 'Price_Unit': '£', 'Offer': offer_text})
        
        # Extract numerical prices for median calculation
        numeric_price = float(price_text.replace('£', '').replace(',', ''))
        prices.append(numeric_price)


# In[5]:


# Calculate the median price
median_price = calculate_median(prices)

# Save the information in a JSON file
output_data = {
    'Products': result_list,
    'Median': median_price
}


# In[6]:


# Dumping the JSON file, named "output.json"
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, indent=2, ensure_ascii=False)

