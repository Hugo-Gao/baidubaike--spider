# -*- coding: UTF-8 -*-
class UrlManager(object):
    def __init__(self):
        self.new_urls = list()
        self.old_urls = list()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)
            self.new_urls = list(set(self.new_urls))

    def add_new_urls(self, urls):
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls)

    def get_new_url(self):
        new_url = self.new_urls.pop(0)
        self.old_urls.append(new_url)
        return new_url
