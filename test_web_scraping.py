#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from bs4 import BeautifulSoup
import json

def calculate_median(prices):
    sorted_prices = sorted(prices)
    n = len(sorted_prices)

    if n % 2 == 0:
        median = (sorted_prices[n // 2 - 1] + sorted_prices[n // 2]) / 2
    else:
        median = sorted_prices[n // 2]

    return median

class TestWebScraping(unittest.TestCase):
    def setUp(self):
        # Load the HTML content from a sample file
        with open('orignal.html', 'r', encoding='utf-8') as file:
            self.html_content = file.read()

        # Parse the HTML content using BeautifulSoup
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def test_scrape_data(self):
        result_list = []
        prices = []

        # Fetching all the products information from the webpage
        products_items = self.soup.find_all('div', class_='oct-grid__row oct-grid__row--full-width oct-listers-hits')

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

        # Assertions
        self.assertTrue(result_list)  # Check that result_list is not empty
        self.assertTrue(prices)  # Check that prices list is not empty
        self.assertEqual(len(result_list), len(prices))  # Check that lengths match

    def test_calculate_median(self):
        # Test calculate_median function with various inputs
        self.assertEqual(calculate_median([1, 2, 3]), 2)
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(calculate_median([5, 2, 8, 1, 9]), 5)

if __name__ == '__main__':
    unittest.main()


# In[ ]:




