# automatic-guacamole
Web Scraper to CSV

Scrapes size, price, and model of products from stockx to convert to a csv format to be used in shopify.

Trash code but it works.

Features:
- GetURL() grabs links to all products from stockx website.
- Grabs price and available size from stockx and searches stadiumgoods for a suitable image.
- Formats data to an importable CSV file for Shopify
- Exports and uploads to shopify site.

To do:
- Bypass login captcha
- Solve memory leak problem
- Save and store image on external file/SQL database to speed up process.

How to run:
- go to folder/directory
- python main.py
