import requests
import scrapy
import os, datetime;
import wget

class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    date = "20201019"
    url ="https://www.release.tdnet.info/inbs/I_list_001_{}.html".format(date)

    start_urls = [url]
    key = "株式会社"
    base_link = "https://www.release.tdnet.info/inbs/"
    page_number = 2

    def __init__(self):
        try:
            os.mkdir(f"Data/{self.date}")
            os.mkdir(f"Data/{self.date}/pdf")
            os.mkdir(f"Data/{self.date}/zip")
        except:
            print("error")

    def parse(self, response):

        pdf = response.css('.kjTitle a')
        xbrl = response.css(".style002")
        for link in pdf:
            title = link.css("::text")[0].extract()

            if self.key in title:

                href = link.css('a::attr(href)')[0].extract()
                final_url=self.base_link+href
                wget.download(final_url,f'Data/{self.date}/pdf/')
        for link in xbrl:
            href = link.css('a::attr(href)')[0].extract()
            final_url = self.base_link+href
            wget.download(final_url,f'Data/{self.date}/zip/')

        next_page = "https://www.release.tdnet.info/inbs/I_list_00{}_{}.html".format(self.page_number,self.date)
        res = requests.get(next_page)
        if res:
            SpiderSpider.page_number+=1
            yield response.follow(next_page,callback=self.parse)




