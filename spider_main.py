# -*- coding: UTF-8 -*-
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_praser
from baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.praser = html_praser.HtmlPraser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加新的url进入url管理器
        self.urls.add_new_url(root_url)
        # 循环检查url管理器是否还有未爬完的url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d :%s ' % (count, new_url)
                # 将目标html文件下载下来成字符串保存到html_cont变量中
                html_cont = self.downloader.download(new_url)

                # 获取新获得的多个url，和data
                new_urls, new_data = self.praser.prase(new_url, html_cont)
                # 将urls添加进入url管理器,数据添加进入数据管理器
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == item_num:
                    break
                count += 1
            except:
                print '爬取失败'

        self.outputer.output_html()


if __name__ == '__main__':
    print '欢迎使用百度百科超级爬虫!!!--------'
    item_name = raw_input("请输入你要搜索的字段：")
    item_num = input("请输入你要搜索的网站数目（最好不要超过1000）:")
    root_url = "http://baike.baidu.com/item/" + item_name
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
