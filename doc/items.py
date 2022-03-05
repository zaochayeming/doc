# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DocItem(scrapy.Item):
    # define the fields for your item here like:
    avatar = scrapy.Field()   # 医生头像url
    name = scrapy.Field()   # 医生名称
    doctor_title = scrapy.Field()   # 医生职称
    doctor_educate_title = scrapy.Field()   # 学位
    hospital = scrapy.Field()   # 医院名称
    department = scrapy.Field()  # 科室
    major = scrapy.Field()  # 专业擅长
    profile = scrapy.Field()    # 个人简介
    print(scrapy.Item)
    pass
