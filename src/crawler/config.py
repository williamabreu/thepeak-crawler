import os


class CrawlerConfig:
    selenium_url = os.environ.get("SELENIUM_URL") or "http://localhost:4444"
