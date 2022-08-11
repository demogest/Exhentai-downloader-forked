# -*- coding: utf-8 -*-
import getpass

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from exhentai.spiders.exHentaiSpider import ExHentaiSpider


def main():
    username = input('用户名:')
    password = getpass.getpass('密码:')
    rule = {
        'keyword' : input('关键字:'),
        'ori' : int(input('是否尝试下载原图 （1 原图 / 0 缩略图）:') or "0"),
        'star' : float(input('最少星标(默认为0，最大为5 输入值可包含两位小数):') or "0"),
        'fav': int(input('最少收藏数（默认为0）:') or "0"),
        'start_page' : int(input('从第几页开始下载（默认为1）:') or "1"),
        'end_page' : int(input('下载至第几页（默认为5）:') or "5"),
        'doujinshi' : (input('是否包含doujinshi（1 包含 / 0 不包含 默认包含）:') or "1" ) == "0" and "off" or "on",
        'manga' : (input('是否包含manga（1 包含 / 0 不包含 默认包含）:') or "1") == "0" and "off" or "on",
        'artist_cg' : (input('是否包含artist_cg（1 包含 / 0 不包含 默认包含）:') or "1") == "0" and "off" or "on",
        'game_cg' : (input('是否包含game_cg（1 包含 / 0 不包含 默认不包含）:') or "0") == "0" and "off" or "on",
        'western' : (input('是否包含western（1 包含 / 0 不包含 默认不包含）:') or "0") == "0" and "off" or "on",
        'non_h' : (input('是否包含non_h（1 包含 / 0 不包含 默认不包含）:') or "0") == "0" and "off" or "on",
        'image_set' : (input('是否包含image_set（1 包含 / 0 不包含 默认包含）:') or "1") == "0" and "off" or "on",
        'cosplay' : (input('是否包含cosplay（1 包含 / 0 不包含 默认包含）:') or "1") == "0" and "off" or "on",
        'asian_porn' : (input('是否包含asian_porn（1 包含 / 0 不包含 默认不包含）:') or "0") == "0" and "off" or "on",
        'misc' : (input('是否包含misc（1 包含 / 0 不包含 默认不包含）:') or "0") == "0" and "off" or "on",
    }


    settings = get_project_settings()
#    disable the scrapy log
#     configure_logging(settings)

    runner = CrawlerRunner(settings)
    runner.crawl(ExHentaiSpider,
                 user = {'username':username,
                         'password':password,
                 },
                 rule = rule)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == '__main__':
    main()





