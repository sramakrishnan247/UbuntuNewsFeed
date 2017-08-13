import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "http://timesofindia.indiatimes.com/rssfeedstopstories.cms"


def load():
    res = requests.get(RSS_FEED_URL)
    # print res.content
    # print " "
    items = []
    root = ET.fromstring(res.content)
    for item in root.findall('./channel/item'):
        news = {}
        # print item.find("title").text
        # print item.find("description").text
        # print item.find("link").text
        news["title"] = item.find("title").text
        news["des"] = item.find("description").text
        items.append(news)
        # print news
    print items
    return items

load()
