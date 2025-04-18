from itemadapter import ItemAdapter
from collections import defaultdict
import datetime


class PepParsePipeline:
    filename = (
        'results/status_summary_'
        f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    )
    file = open(filename, mode='w', encoding='utf-8')
    total = 0
    status_dict = defaultdict(int)

    def open_spider(self, spider):
        self.file.write('Статус,Количество\n')

    def process_item(self, item, spider):
        self.total += 1
        self.status_dict[item['status']] += 1

        return item

    def close_spider(self, spider):
        for status, count in self.status_dict.items():
            self.file.write(f'{status},{count}\n')
        self.file.write(f"Total,{self.total}\n")
        self.file.close()
