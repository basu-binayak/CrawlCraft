# 📤 Exporting Data in Scrapy: A Complete Guide

One of the biggest strengths of Scrapy is how easily it lets you **export scraped data** into different formats. Whether you want to save data as **JSON** , **CSV** , or even a **database** , Scrapy provides flexible options. This article covers all the methods you can use to export data, from quick one-liners to production-grade pipelines.

---

## 🔹 1. Exporting via the Command Line

The **simplest way** to export data is directly from the Scrapy CLI when running a spider.

### Example:

```bash
scrapy crawl books_to_scrape -o books.json
```

This command:

- Runs the spider `books_to_scrape`
- Saves the results into `books.json`

You can change the extension (`.csv`, `.xml`, `.jsonlines`) to get different formats:

- `books.json` → Pretty-printed JSON
- `books.jl` → JSON Lines (one object per line)
- `books.csv` → CSV
- `books.xml` → XML

📌 **Tip** : Use `-O` (capital O) to **overwrite** the file each time, instead of appending.

```bash
scrapy crawl books_to_scrape -O books.json
```

---

## 🔹 2. Using the Feed Exports Settings

Instead of specifying `-o` every time, you can configure Scrapy’s settings to **always export data** in a particular format.

In your `settings.py`:

```python
FEEDS = {
    'data/books.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,   # pretty-printed JSON
    },
    'data/books.csv': {
        'format': 'csv',
        'overwrite': True
    }
}
```

Here:

- You can export **multiple formats simultaneously** (JSON + CSV in this case).
- `indent` makes JSON human-readable.
- `overwrite=True` prevents appending.

---

## 🔹 3. JSON Lines Format (`.jl`)

For **large datasets** , JSON Lines is often better because:

- Each record is written on a new line as soon as it’s scraped.
- More memory-efficient than writing the entire JSON at once.

Command:

```bash
scrapy crawl books_to_scrape -O books.jl
```

Output (example):

```json
{"title": "Book A", "price": "£20.00"}
{"title": "Book B", "price": "£15.00"}
```

---

## 🔹 4. Exporting with Pipelines

If you want **full control** (e.g., exporting only selected fields, or saving to a custom file/database), use **Item Pipelines** .

Example pipeline to write CSV manually:

```python
import csv

class CsvExportPipeline:
    def open_spider(self, spider):
        self.file = open('books.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['title', 'price'])  # header

    def process_item(self, item, spider):
        self.writer.writerow([item.get('title'), item.get('price')])
        return item

    def close_spider(self, spider):
        self.file.close()
```

Enable it in `settings.py`:

```python
ITEM_PIPELINES = {
    'mystery_ebook_scraper.pipelines.CsvExportPipeline': 300,
}
```

---

## 🔹 5. Exporting to Databases

Scrapy doesn’t export directly to databases out-of-the-box, but you can use pipelines to insert data into:

- **SQLite / PostgreSQL / MySQL**
- **MongoDB / NoSQL stores**

Example for SQLite:

```python
import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('books.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, price TEXT)')

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO books VALUES (?, ?)",
                         (item['title'], item['price']))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
```

---

## 🔹 6. Testing in Scrapy Shell

Before exporting at scale, test your selectors in **Scrapy Shell** :

```bash
scrapy shell http://books.toscrape.com
```

```python
response.css('article.product_pod h3 a::attr(title)').getall()
```

This ensures your exported data is **clean and accurate** .

---

## 🚀 Summary

Scrapy gives you multiple ways to export data:

1. **Quick CLI export** → `-o output.json`
2. **FEEDS setting** → define multiple formats at once
3. **JSON Lines** → efficient for large datasets
4. **Pipelines** → custom exports (CSV, JSON, etc.)
5. **Database pipelines** → directly save into DB

👉 For small projects: stick with CLI `-O file.json`.

👉 For production: use **FEEDS** or **pipelines** for structured and repeatable workflows.
