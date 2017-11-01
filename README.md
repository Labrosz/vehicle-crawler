# Update Oct-2017: This project has been moved to a private(bitbucket) repositoty and will be released after its development is finished

# Vehicle-crawler
A web crawler to collect vehicle classifieds and send them to a web server. The web server can later be used to organize the data into a database.

# Framework
The framework for the development of this project is Scrapy(https://scrapy.org/).

# Usage
You can use the following commands to run the crawler and get a .json response.
```
scrapy crawl vehicle -o africa.json -a tag='bikes/?condition=Καινούριο&condition=Μεταχειρισμένο&offer_type=sale&pg=1&variant=XRV+750+Africa+TWIN'
```
