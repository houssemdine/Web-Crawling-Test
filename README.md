├── /scripts/
│   ├── web.py              Main script for web scraping
│   └── ingest_data.py      Script to ingest data into the database
│
├── /data/
│   └── products.json        Output JSON file with extracted product data
│
├── /docs/
│   └── database_schema.sql 
│
├── requirements.txt  


NB * 
I don't use Requests because I encountered many errors with it during the scraping process. Instead, I opted for Selenium WebDriver because it is more reliable when handling dynamic content.

