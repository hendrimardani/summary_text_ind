# from pathlib import Path
# import scrapy
# import json
# target = ''
# for x in response.text.split("\n"):
#     if 'window.kmklabs.channel =' in x:
#         target = x
#         break
# target = target.split("window.kmklabs.article = ")[1]
# target = target.split(";")[0]
# target = json.loads(target)




# import json
# with open("url.json", "r") as f:
#     urls = f.read()
# urls = json.loads(urls)
# print(urls.keys())
# Output 
# dict_keys(['train_urls', 'dev_urls', 'test_urls', 'xtreme_dev_ids', 'xtreme_test_ids'])



# import json
# with open("url.json", "r") as f:
#     urls = f.read()
# urls = json.loads(urls)["train_urls"]
# print(len(urls))
# # Ouput
# # 193883




from pathlib import Path
import scrapy
import json

def scrap_javascript(response):
    target = ''
    for x in response.text.split("\n"):
        if 'window.kmklabs.channel =' in x:
            target = x
            break
    target = target.split("window.kmklabs.article = ")[1]
    target = target.split(";")[0]
    target = json.loads(target)
    return target["shortDescription"]


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        with open("url.json", "r") as f:
            urls = f.read()
        urls = json.loads(urls)["train_urls"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.url) # Cek apakah ada error atau tidak
        for body in response.css("div.read-page--content"):
            yield {
                "text":body.css("div.article-content-body__item-content::text").extract(),
                "summary": scrap_javascript(response)
            }

