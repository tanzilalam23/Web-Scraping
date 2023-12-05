<h1>Boots Website Scraper</h1>

<p>This Python script is designed to scrape product information from the Boots website. It utilizes the BeautifulSoup library for HTML parsing and requests to send HTTP requests to the server. Because the request for the website content was unsuccessful, a copy of the website in .html format was obtained and used instead.</p>

<h2>Prerequisites</h2>

<p>Before running the script, make sure you have the required Python libraries installed. You can install them using the following command:</p>

<pre><code>pip install beautifulsoup4</code></pre>

<h2>Usage</h2>

<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/your-username/Web-Scraping.git</code></pre>

  <li>Navigate to the project directory:</li>
  <pre><code>cd Web-Scraping</code></pre>

  <li>Run the script to download the JSON file directly:</li>
  <pre><code>python boot_web_scraping.py</code></pre>

</ol>

<h2>Functions</h2>

<h3><code>calculate_median(prices)</code></h3>

<p>Calculates the median value of a list of prices.</p>

<h4>Parameters</h4>

<ul>
  <li><code>prices</code> (list of float): A list of numerical values representing prices.</li>
</ul>

<h4>Returns</h4>

<ul>
  <li><code>float</code>: The median value of the provided prices.</li>
</ul>

<h3><code>scrape_boots_website(url)</code></h3>

<p>Scrapes product information from the Boots website.</p>

<h4>Parameters</h4>

<ul>
  <li><code>url</code> (str): The URL of the Boots website page to be scraped.</li>
</ul>

<h4>Returns</h4>

<ul>
  <li><code>BeautifulSoup</code>: A BeautifulSoup object representing the parsed HTML content of the webpage.</li>
</ul>

<h2>Script Flow</h2>

<ol>
  <li>The script opens the <code>orignal.html</code> file and retrieves the HTML content.</li>
  <li>The HTML content is then parsed using BeautifulSoup.</li>
  <li>Product information, including Title, Price, and Offer, is extracted from the parsed HTML. As the Price_Unit was hard coded, so no extraction needed there.</li>
  <li>The script calculates the median price from the extracted numerical prices.</li>
  <li>The results are saved in a JSON file named <code>output.json</code>.</li>
</ol>

<h2>File Input</h2>

<p>The script expects an HTML file named <code>orignal.html</code> in the project directory. Make sure to provide the correct file path or name in the script.</p>

<h2>File Output</h2>

<p>The script generates a JSON file named <code>output.json</code> containing a list of products and their details, along with the calculated median price.</p>

----------------------------------------
----------------------------------------

# Web Scraping Unit Test

This unit test script is designed to validate the functionality of the Boots Website Scraper. It uses the `unittest` library to conduct tests on the scraping and calculation functions.

## Test Cases

### Test Case 1: `test_scrape_data`

This test ensures that the scraping function retrieves data from the HTML content correctly. It checks the following:
1. `result_list` is not empty.
2. `prices` list is not empty.
3. The lengths of `result_list` and `prices` match.

### Test Case 2: `test_calculate_median`

This test verifies the correctness of the `calculate_median` function by testing it with different inputs.

## How to Run Tests

1. Ensure you have the required Python libraries installed. You can install them using the following command:

    ```bash
    pip install beautifulsoup4
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Web-Scraping.git
    ```

3. Navigate to the project directory:

    ```bash
    cd Web-Scraping
    ```

4. Run the unit tests:

    ```bash
    python test_web_scraping.py
    ```

## Additional Information

- The HTML content for testing is loaded from the `orignal.html` file in the project directory.
- The script uses BeautifulSoup for HTML parsing and includes a `calculate_median` function for calculating the median value of a list of prices.
- The results of the scraping are stored in a list named `result_list`.
- The numerical prices are stored in a list named `prices`.
- The script includes assertions to ensure the correctness of the scraping and calculation functions.

