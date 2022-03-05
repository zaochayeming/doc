import scrapy
from scrapy.loader import ItemLoader
from doc.items import DocItem


class HaodfSpider(scrapy.Spider):
    name = 'haodf'
    allowed_domains = ['haodf.com']
    start_urls = ['https://www.haodf.com/doctor/list.html?p=1']

    def parse(self, response, **kwargs):
        # url_list：医生详情页面链接地址
        url_list = response.xpath('//div[@class="fam-doc-item clearfix"]/a/@href').extract()
        for i in url_list:
            i = str(i).replace('.html', '/xinxi-jieshao.html')
            yield scrapy.Request(
                i,
                callback=self.parse_detalil
            )
            # print(i)

        # next_url = r'https://www.haodf.com' + response.xpath('//a[contains(text(),"下一页")]/@href').extract_first()
        next_page = r'https://www.haodf.com' + response.xpath('//a[@class="page_turn_a"]/@href').extract()[-1]

        if next_page is not None:
            yield scrapy.Request(
                next_page,
                callback=self.parse
            )

    def parse_detalil(self, response):
        l = ItemLoader(item=DocItem(), response=response)
        l.add_xpath('avatar', '//img[@class="avatar"]/@src')
        l.add_xpath('name', '//h1[@class="doctor-name js-doctor-name"]/text()')
        l.add_xpath('doctor_title', '//span[@class="doctor-title"]/text()')
        l.add_xpath('doctor_educate_title', '//span[@class="doctor-educate-title"]/text()')
        l.add_xpath('hospital', '//li[@class="doctor-faculty"]/a[1]/text()')
        l.add_xpath('department', '//li[@class="doctor-faculty"]/a[2]/text()')
        major_content = response.xpath('normalize-space(//h3[@class="introwarp-title"][contains(text(),"专业擅长")]/following-sibling::*[1])').extract_first()
        profile_content = response.xpath('normalize-space(//h3[@class="introwarp-title"][contains(text(),"个人简介")]/following-sibling::*[1])').extract_first()
        # print(major_content)
        # print(profile_content)
        l.add_value('major', major_content)
        l.add_value('profile', profile_content)
        # print(l.load_item())
        # print(response.url)
        return l.load_item()
