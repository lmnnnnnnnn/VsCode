 # -*- coding: utf-8 -*-
import sys
import imp
imp.reload(sys)
# sys.setdefaultencoding('utf-8')
#Python 默认脚本文件都是 UTF-8 编码的,当脚本出现中文汉字时需要对其进行解码。
import scrapy
class itemSpider(scrapy.Spider):
  # scrapy.Spider 是一个简单的爬虫类型。
  # 它只是提供了一个默认start_requests()实现。
  # 它从start_urlsspider属性发送请求，并parse 为每个结果响应调用spider的方法。
    name ="demo_scrapy"
  # 定义此爬虫名称的字符串。
   # 它必须是唯一的。
    start_urls = ['http://lab.scrapyd.cn']
  #爬虫抓取自己需要的网址列表。
  #该网站列表可以是多个。
    def parse(self, response):
       # 定义一个parse规则，用来爬取自己需要的网站信息。
        pachong = response.css('div.quote')
        # 用变量pachong来保存获取网站的部分内容。
        for v in pachong:
            text = v.css('.text::text').extract_first()
            autor = v.css('.author::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            tags = ','.join(tags)
             # 循环提取所有的标题、作者和标签内容。
            fileName = u'%s-语录.txt' % autor
             # 文件的名称为作者名字—语录.txt。
            with open(fileName, "a+")as f:
                 f.write(u'标题：'+text)
                 f.write('\n')
                 f.write(u'标签：' + tags)
                 f.write('\n------------------------------------------------\n')
                 # 打开文件并写入标题和标签内容。
                 f.close()
                 # 关闭文件
            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
                 # 查看存在不存在下一页的链接，如果存在下一页，把下一页的内容提交给parse然后继续爬取。
                 # 如果不存在下一页链接结束爬取。