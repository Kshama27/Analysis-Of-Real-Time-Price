# Product-Price-Scraper-from-Amazon-and-Flipkart

Product Price Scraper is a web application that allows users to enter the name of a product and fetches the prices of the product from both Flipkart and Amazon websites. The backend of the application is built using Python with Flask, and web scraping is done using BeautifulSoup and Selenium.

## Features

- User-friendly web interface to enter the product name and fetch prices.
- Scrapes prices from both Flipkart and Amazon websites.
- Displays the fetched prices on the web page.

## Prerequisites

- Python 3.x
- Flask
- BeautifulSoup
- Selenium
- Chrome WebDriver (for Selenium)

## How to Run

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your_username/product-price-scraper.git
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Download the appropriate Chrome WebDriver for your operating system and place it in your system's PATH.

4. Run the Flask application:

   ```
   python app.py
   ```

5. Open your web browser and access the application at `http://127.0.0.1:5000/`.

6. Enter the name of the product in the input field and click "Scrape Prices" to view the prices from Flipkart and Amazon.

## How It Works

The Flask application (`app.py`) serves as the backend of the web application. When the user submits the product name through the web form, the backend fetches the prices from both Flipkart and Amazon websites using web scraping techniques.

- The `scrape_flipkart` function uses BeautifulSoup to scrape the Flipkart website and obtain the product price.
- The `scrape_amazon` function uses Selenium to render the Amazon website and then uses BeautifulSoup to extract the product price from the rendered page.

The scraped prices are then sent back to the frontend and displayed on the web page.

## Folder Structure

```
product-price-scraper/
├── app.py
├── style.css
├── index.html
├── requirements.txt
└── README.md
```

- `app.py`: Contains the Flask application and web scraping functions.
- `style.css`: CSS file to style the HTML frontend.
- `index.html`: HTML file containing the frontend of the web application.
- `requirements.txt`: List of required Python packages.
- `README.md`: This file, containing information about the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please note that web scraping might violate the terms of service of websites. Use this application responsibly and ensure compliance with the terms and conditions of the websites you scrape. The authors of this project are not responsible for any misuse or violations.
