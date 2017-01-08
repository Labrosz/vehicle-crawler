# Vehicle-crawler
A web crawler to collect vehicle classifieds and import into a database. The database can later be used to notify users interested in certain type of vehicle through a web or mobile app.

# Framework
The framework for the development of this project is Scrapy(https://scrapy.org/).

# Usage
You can use the following commands to run the crawler and get a .json response.
```
scrapy crawl vehicle -o africa.json -a tag='bikes/?condition=Καινούριο&condition=Μεταχειρισμένο&offer_type=sale&pg=1&variant=XRV+750+Africa+TWIN'
```
