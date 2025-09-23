# CrawlCraft 🕷️

CrawlCraft is a starter repository for learning **Scrapy**, the powerful Python framework for web scraping. This repository provides guidelines to set up your environment, create a Scrapy project, and start scraping efficiently.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Creating a Scrapy Project](#creating-a-scrapy-project)
- [Running Your Spider](#running-your-spider)
- [Project Structure](#project-structure)
- [Best Practices](#best-practices)
- [Resources](#resources)

---

## Overview

Scrapy is an open-source Python framework designed for web scraping and crawling websites to extract structured data. CrawlCraft aims to guide beginners in creating Scrapy projects from scratch in a clean and modular way.

---

## Prerequisites

- Python 3.8 or higher
- `pip` installed
- Basic knowledge of Python

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/CrawlCraft.git
cd CrawlCraft
```

### 2. Create a virtual environment

**Option 1: Using `venv` (standard Python)**

```bash
python -m venv venv
```

**Option 2: Using `conda`**

```bash
conda create --name crawlcraft python=3.10
conda activate crawlcraft
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Scrapy

```bash
pip install scrapy
```

Verify installation:

```bash
scrapy version
```

---

## Creating a Scrapy Project

1. Navigate to your working directory:

```bash
cd CrawlCraft
```

2. Create a new Scrapy project:

```bash
scrapy startproject crawlcraft
```

This creates a folder `crawlcraft` with the following structure:

```
crawlcraft/
├── crawlcraft/
│   ├── spiders/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── scrapy.cfg
```

---

## Running Your Spider

1. Create a spider inside `crawlcraft/spiders/`:

```bash
scrapy genspider example example.com
```

2. Run your spider:

```bash
scrapy crawl example
```

3. Save the output to a file:

```bash
scrapy crawl example -o output.json
```

---

## Project Structure

- `items.py` – Define the data structures (fields) you want to scrape.
- `pipelines.py` – Process scraped data (e.g., save to database or CSV).
- `middlewares.py` – Customize Scrapy’s request/response handling.
- `settings.py` – Configure your project (user-agent, download delay, etc.).
- `spiders/` – Store all spider scripts for crawling websites.

---

## Best Practices

- Use a virtual environment for isolation.
- Respect `robots.txt` and website terms.
- Implement delays to avoid being blocked.
- Modularize spiders for maintainability.
- Use `pipelines` to clean and store data.

---

## Resources

- [Scrapy Official Documentation](https://docs.scrapy.org/en/latest/)
- [Scrapy Tutorials](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Scrapy Tips & Tricks](https://doc.scrapy.org/en/latest/topics/practices.html)

---

Happy Crawling! 🕷️🚀
