# Scrapy Python Web Scrapper

## Running Instructions

### 1. Clone the repo and cd into the folder

    git clone https://github.com/dvjakhar31/scrapy-web-crawler.git && cd scrapy-web-crawler
    
### 2. Set up [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

    virtualenv venv
    
### 3. Install requirements

    pip install requirements.txt
    
### 4. Run the scrapper

    scrapy crawl primers_spider

## Project structure

```sh
├── task
|   ├── spiders
|       └── primers_spider.py
|   ├── items.py
|   ├── middlewares.py
|   ├── pipelines.py
|   ├── settings.py
├── requirements.txt
├── scrapy.cfg
├── README.md
```
