from collections import defaultdict
import datetime
import os
import csv


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = 0
        self.status_dict = defaultdict(int)

        time_format = spider.settings.get('TIME_FORMAT', "%Y-%m-%d_%H-%M-%S")
        # Получаем путь к results из FEEDS или настройки
        results_path = next(iter(spider.settings.getdict('FEEDS')))
        results_dir = os.path.dirname(results_path)
        os.makedirs(results_dir, exist_ok=True)

        self.filename = os.path.join(
            results_dir, (
                f'status_summary_'
                f'{datetime.datetime.now().strftime(time_format)}.csv'
            ))

    def process_item(self, item, spider):
        self.total += 1
        self.status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in self.status_dict.items():
                writer.writerow([status, count])
            writer.writerow(['Total', self.total])
