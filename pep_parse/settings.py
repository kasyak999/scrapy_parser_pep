BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {  # 'quotes_text_%(time)s.csv' добавить время
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
