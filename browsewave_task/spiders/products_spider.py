import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        url = "https://mr-bricolage.bg/bg/%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8/%D0%90%D0%B2%D1%82%D0%BE-%D0%B8-%D0%B2%D0%B5%D0%BB%D0%BE%D0%B0%D0%BA%D1%81%D0%B5%D1%81%D0%BE%D0%B0%D1%80%D0%B8/%D0%92%D0%B5%D0%BB%D0%BE%D0%B0%D0%BA%D1%81%D0%B5%D1%81%D0%BE%D0%B0%D1%80%D0%B8/c/006008012"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for product in response.css("div.product"):
            yield {
                'title': product.css("div.title a::text").extract_first().strip(),  # doc for pipelines + utf-8 encoding
                'price': product.css("div.price::text").extract_first(),
                # 'image': product.css("div.image a img::attr(src)").extract_first,  # doc for images
                # 'characteristics': "",  # create func to follow product url and extract data from the table
            }

        for href in response.css("li.pagination-next a::attr(href)"):
            yield response.follow(href, self.parse)
