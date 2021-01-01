import json
import re

import requests


class GuBa(object):
    def __init__(self):
        self.base_url = 'http://guba.eastmoney.com/default,99_%s.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        self.infos = []
        self.parse()

    def parse(self):
        for i in range(1, 13):
            response = requests.get(self.base_url % i, headers=self.headers)

            '''阅读数,评论数,标题,作者,更新时间,详情页url'''
            ul_pattern = re.compile(r'<ul id="itemSearchList" class="itemSearchList">(.*?)</ul>', re.S)
            ul_content = ul_pattern.search(response.text)
            if ul_content:
                ul_content = ul_content.group()

            li_pattern = re.compile(r'<li>(.*?)</li>', re.S)
            li_list = li_pattern.findall(ul_content)
            # print(li_list)

            for li in li_list:
                item = {}
                reader_pattern = re.compile(r'<cite>(.*?)</cite>', re.S)
                info_list = reader_pattern.findall(li)
                # print(info_list)
                reader_num = ''
                comment_num = ''
                if info_list:
                    reader_num = info_list[0].strip()
                    comment_num = info_list[1].strip()
                print(reader_num, comment_num)
                title_pattern = re.compile(r'title="(.*?)" class="note">', re.S)
                title = title_pattern.search(li).group(1)
                # print(title)
                author_pattern = re.compile(r'target="_blank"><font>(.*?)</font></a><input type="hidden"', re.S)
                author = author_pattern.search(li).group(1)
                # print(author)

                date_pattern = re.compile(r'<cite class="last">(.*?)</cite>', re.S)
                date = date_pattern.search(li).group(1)
                # print(date)

                detail_pattern = re.compile(r' <a href="(.*?)" title=', re.S)
                detail_url = detail_pattern.search(li)
                if detail_url:
                    detail_url = 'http://guba.eastmoney.com' + detail_url.group(1)
                else:
                    detail_url = ''

                print(detail_url)
                item['title'] = title
                item['author'] = author
                item['date'] = date
                item['reader_num'] = reader_num
                item['comment_num'] = comment_num
                item['detail_url'] = detail_url
                self.infos.append(item)
        with open('guba.json', 'w', encoding='utf-8') as fp:
            json.dump(self.infos, fp)

gb=GuBa()