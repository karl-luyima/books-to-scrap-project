# Books to Scrape - Web Scraping Project

## Project Overview

This project uses Python and Scrapy to scrape book information from [Books to Scrape](https://books.toscrape.com/), a practice website designed for web scraping.

The extracted information is exported into a CSV file for further analysis.

## Technologies Used

- Python
- Scrapy
- CSV

## Data Extracted

The spider collects the following information:

- Book Title
- Price
- Rating
- Availability
- Category
- Book URL

## Project Structure

```text
books-to-scrap-project/
├── bookscraper/
│   ├── spiders/
│   │   └── books.py
│   ├── settings.py
│   ├── items.py
│   ├── pipelines.py
│   └── middlewares.py
├── books.csv
├── scrapy.cfg
├── README.md
└── .gitignore
```

## How to Run the Project

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install Scrapy:

   `pip install scrapy`

4. Run the spider:

   `scrapy crawl books -O books.csv`

## Output

The scraped book information is saved in `books.csv`.

## Target Website

https://books.toscrape.com/