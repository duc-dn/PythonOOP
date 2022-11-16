import os

COUNTLY_DB = os.getenv("COUNTLYDB", "countly")
URL = os.getenv("URL", "localhost/27017")