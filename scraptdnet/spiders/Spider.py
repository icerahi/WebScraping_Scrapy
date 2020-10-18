import scrapy
import os, datetime;
import wget

class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    date = "20201016"
    url ="https://www.release.tdnet.info/inbs/I_list_001_{}.html".format(date)

    start_urls = [url]
    key = "株式会社"
    pdf_base_link = "https://www.release.tdnet.info/inbs/"

    def __init__(self):
        try:
            path = os.mkdir(f"Data/{self.date}")
        except:
            print("error")



    def parse(self, response):

        data = response.css('.kjTitle a')
        for link in data:
            title = link.css("::text")[0].extract()

            if self.key in title:

                href = link.css('a::attr(href)')[0].extract()
                final_url=self.pdf_base_link+href


                wget.download(final_url,f'Data/{self.date}/')




