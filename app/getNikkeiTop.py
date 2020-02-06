# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup

def scraping():
  # アクセスするURL
  url_str = "http://www.nikkei.com/"

  # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
  html = urllib.request.urlopen(url=url_str)

  # htmlをBeautifulSoupで扱う
  soup = BeautifulSoup(html, "html.parser")

  # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
  title_tag = soup.title

  # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
  title = title_tag.string

  # タイトル要素を出力
  print(title_tag)

  # タイトルを文字列を出力
  print (title)

def getScrapingResult():
    # アクセスするURL
    url_str = "http://www.nikkei.com/"

    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    html = urllib.request.urlopen(url=url_str)
 
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")
 
    # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
    title_tag = soup.title
 
    # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
    title = title_tag.string
 
    # タイトルを文字列を出力
    return str(title)

if __name__ == '__main__':
  scraping()


