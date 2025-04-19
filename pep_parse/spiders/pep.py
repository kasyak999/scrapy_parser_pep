import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css(
            'table.pep-zero-table.docutils.align-default tbody tr')
        for pep in all_pep:
            pep_url = pep.css('a::attr(href)').get()
            name_and_number = pep.css('a::text').getall()
            data = {
                'number': name_and_number[0].strip(),
                'name': name_and_number[1].strip(),
            }
            if pep_url is not None:
                yield response.follow(
                    pep_url, callback=self.parse_pep, meta={'data': data})

    def parse_pep(self, response):
        response.meta['data']['status'] = (
            response.css('dt:contains("Status") + dd abbr::text').get())
        yield PepParseItem(response.meta['data'])
