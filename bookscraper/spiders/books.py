
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # Select all book containers on the current page
        books = response.css("article.product_pod")

        for book in books:
            # Extract the book title
            title = book.css("h3 a::attr(title)").get()

            # Extract the book price
            price = book.css(".price_color::text").get()

            # Extract the book rating
            rating = book.css("p.star-rating::attr(class)").get()
            rating = rating.replace("star-rating ", "") if rating else None

            # Extract availability
            availability = book.css(".availability::text").getall()
            availability = "".join(availability).strip()

            # Extract the book URL
            book_url = response.urljoin(
                book.css("h3 a::attr(href)").get()
            )

            # Follow the book link to get its category
            yield response.follow(
                book_url,
                callback=self.parse_book,
                meta={
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "availability": availability,
                    "book_url": book_url,
                },
            )

        # Find the next page and follow it
        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        # Extract the category from the breadcrumb
        category = response.css(
            "ul.breadcrumb li:nth-child(3) a::text"
        ).get()

        yield {
            "title": response.meta["title"],
            "price": response.meta["price"],
            "rating": response.meta["rating"],
            "availability": response.meta["availability"],
            "category": category.strip() if category else None,
            "book_url": response.meta["book_url"],
        }
