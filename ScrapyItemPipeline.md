# 🛠️ Scrapy Item Pipelines: The Backbone of Data Processing

When you scrape data with Scrapy, the raw output often isn’t “production-ready.” You may want to **clean it, validate it, remove duplicates, or store it in a database** . That’s exactly where **Item Pipelines** come in.

---

## 🔹 What is an Item Pipeline?

An **Item Pipeline** is a set of components (Python classes) through which every scraped `Item` passes **after being yielded by a Spider** .

You can chain multiple pipelines together to build a processing workflow.

**Data Flow:**

```
Spider → Item → Item Pipeline(s) → Storage (CSV, JSON, DB, API, etc.)
```

---

## 🔹 When to Use Pipelines?

You should use pipelines when you need to:

- **Clean/Normalize data** (e.g., strip whitespace, fix casing, format prices).
- **Validate data** (e.g., discard items missing required fields).
- **Remove duplicates** .
- **Store items** (into files, databases, or APIs).

---

## 🔹 Anatomy of a Pipeline

A pipeline is simply a class with **three optional methods** :

```python
class MyPipeline:
    def open_spider(self, spider):
        # Runs once when the spider opens
        pass

    def process_item(self, item, spider):
        # Runs for each item
        return item

    def close_spider(self, spider):
        # Runs once when the spider closes
        pass
```

### Method Breakdown:

- **`open_spider(self, spider)`** → Initialize resources (files, DB connections).
- **`process_item(self, item, spider)`** → Core logic: clean, validate, store data.
- **`close_spider(self, spider)`** → Cleanup resources (close files, commit DB).

---

## 🔹 Example 1: Data Cleaning Pipeline

Suppose you scrape book prices like `"£51.77"`. You want **numeric values only** .

```python
class PriceCleaningPipeline:
    def process_item(self, item, spider):
        item['price'] = float(item['price'].replace('£', ''))
        return item
```

---

## 🔹 Example 2: Drop Invalid Items

If an item doesn’t contain a title, discard it:

```python
from scrapy.exceptions import DropItem

class ValidatePipeline:
    def process_item(self, item, spider):
        if not item.get('title'):
            raise DropItem(f"Missing title in {item}")
        return item
```

---

## 🔹 Example 3: Store in JSON

```python
import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
```

---

## 🔹 Activating Pipelines

Pipelines must be registered in `settings.py` under `ITEM_PIPELINES`:

```python
ITEM_PIPELINES = {
    'mystery_ebook_scraper.pipelines.PriceCleaningPipeline': 300,
    'mystery_ebook_scraper.pipelines.ValidatePipeline': 400,
    'mystery_ebook_scraper.pipelines.JsonWriterPipeline': 500,
}
```

- Keys → Pipeline path.
- Values → **Execution order** (lower number = higher priority).

---

## 🔹 Multiple Pipelines Workflow

Example flow:

```
Spider yields Item
   ↓
[300] PriceCleaningPipeline → fixes price
   ↓
[400] ValidatePipeline → checks title
   ↓
[500] JsonWriterPipeline → saves to file
```

If validation fails, the item is dropped and won’t reach the next pipeline.

---

## 🔹 Built-in Pipelines in Scrapy

Scrapy comes with some **pre-built pipelines** you can use:

- **FilesPipeline** → Download and store files.
- **ImagesPipeline** → Download and process images.
- **MediaPipeline** → Base class for handling media.

These can be extended to suit your project.

---

## 🔹 Summary

Scrapy Item Pipelines let you:

✅ Clean & Normalize data

✅ Validate and drop bad data

✅ Remove duplicates

✅ Store results in files or databases

They are the **post-processing stage** that ensures your scraped data is usable.

---

⚡ Pro Tip: For **small projects** , you might just use `-o output.json` to export. But for **production or complex workflows** , **Pipelines are essential** .
