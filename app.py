from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from flask import Flask, request, render_template
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from urllib.parse import quote_plus
import random
# Initialize the app and CSRF protection
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for CSRF protection
csrf = CSRFProtect(app)

import requests
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Set a secret key for CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize CSRF protection
csrf = CSRFProtect(app)


app = Flask(__name__)

def scrape_flipkart(product_name):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    url = f'https://www.flipkart.com/search?q={product_name.replace(" ", "+")}'
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    price_element = soup.find("div", {"class": "Nx9bqj _4b5DiR"})
    if price_element:
        return f'Flipkart : {price_element.text.strip()}'
    return 'Flipkart: Price not found'



# ... (keep the existing imports)

def scrape_amazon(product_name):
    amazon_url = f'https://www.amazon.in/s?k={product_name.replace(" ", "+")}'
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(amazon_url)

        # Wait until at least one price element appears
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price .a-offscreen"))
        )

        # Parse the updated page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Locate the first price element
        price_element = soup.select_one(".a-price .a-offscreen")
        price = price_element.text.strip() if price_element else 'Price not found'

        # Locate the first product image
        image_element = soup.select_one(".s-image")
        image_url = image_element['src'] if image_element else ''

        return f'Amazon: {price}', image_url

    except Exception as e:
        print(f"Error: {e}")
        return 'Amazon: Price not found', ''

    finally:
        driver.quit()

# ... (keep other scraping functions unchanged)


def scrape_croma(product_name):
    croma_url = f'https://www.croma.com/searchB?q={product_name.replace(" ", "+")}'
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    try:
        print(f"Navigating to: {croma_url}")
        driver.get(croma_url)

        # Wait for the price container to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.amount"))
        )

        # Parse the page source using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Locate the price element using the updated CSS selector
        price_element = soup.select_one("span.amount")
        
        # Check if price element exists
        if price_element:
            price = price_element.text.strip()
            print(f"Price Found on Croma: {price}")
            return f'Croma: {price}'
        else:
            print("Croma Price not found.")
            return 'Croma: Price not found'

    except Exception as e:
        print(f"Error scraping Croma: {e}")
        return 'Croma: Price not found'

    finally:
        driver.quit()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        if product_name:
            flipkart_price = scrape_flipkart(product_name)
            amazon_price, amazon_image = scrape_amazon(product_name)
            croma_price = scrape_croma(product_name)  
            
            # Pass all variables to the template
            return render_template(
                'results.html', 
                product_name=product_name, 
                flipkart_price=flipkart_price, 
                amazon_price=amazon_price, 
                croma_price=croma_price,
                amazon_image=amazon_image
            )
    return render_template('index.html')

# ... (keep the rest of the file unchanged)


if __name__ == '__main__':
    app.run(debug=True)