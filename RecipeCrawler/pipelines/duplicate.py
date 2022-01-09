from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class DuplicatesPipeline:

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['id'] in self.ids_seen or adapter['id'] is None:
            raise DropItem(f"Duplicate or Null item found: {item!r}")
        else:
            self.ids_seen.add(adapter['id'])
            return item