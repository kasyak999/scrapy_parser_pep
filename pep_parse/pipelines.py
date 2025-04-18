from itemadapter import ItemAdapter
from collections import defaultdict
import datetime


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = 0
        self.status_dict = defaultdict(int)
        self.filename = (
            'results/status_summary_'
            f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        )
        with open(self.filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')

    # def open_spider(self, spider):
    #     filename = (
    #         'results/status_summary_'
    #         f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    #     )
    #     self.file = open(filename, mode='w', encoding='utf-8')
    #     self.file.write('Статус,Количество\n')

    def process_item(self, item, spider):
        self.total += 1
        self.status_dict[item['status']] += 1

        return item

    def close_spider(self, spider):
        # for status, count in self.status_dict.items():
        #     self.file.write(f'{status},{count}\n')
        # self.file.write(f"Total,{self.total}\n")
        # self.file.close()

        with open(self.filename, mode='a', encoding='utf-8') as f:
            for status, count in self.status_dict.items():
                f.write(f'{status},{count}\n')
            f.write(f"Total,{self.total}\n")
