import requests
from lxml import etree
from selenium import webdriver

url = "https://www.xiami.com/"

res = requests.get(url)

res.encoding='utf-8'

print(res.text)