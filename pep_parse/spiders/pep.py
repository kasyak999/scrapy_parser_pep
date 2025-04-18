import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        all_pep = response.css(
            'table.pep-zero-table.docutils.align-default tbody tr')
        for pep in all_pep:
            name_and_number = pep.css('a::text').getall()
            data = {
                'number': name_and_number[0],
                'name': name_and_number[1],
                'status': pep.css('abbr::text').get()
            }
            yield PepParseItem(data)
