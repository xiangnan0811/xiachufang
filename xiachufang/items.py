# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiachufangItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()                                      # 菜谱名
    category = scrapy.Field()                                  # 菜谱分类
    recipe_url = scrapy.Field()                                # 菜谱详情链接
    cover_image_url = scrapy.Field()                           # 菜谱封面图链接
    score = scrapy.Field()                                     # 评分
    cooked_num = scrapy.Field()                                # 多少人做过
    author = scrapy.Field()                                    # 作者
    description = scrapy.Field()                               # 菜谱描述
    ingredient = scrapy.Field()                                # 用料
    steps = scrapy.Field()                                     # 步骤
    create_time = scrapy.Field()                               # 创建时间
    collection = scrapy.Field()                                # 收藏量
