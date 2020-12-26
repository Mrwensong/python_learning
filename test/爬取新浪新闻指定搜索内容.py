import requests

# ------------------爬取带参数的get请求-------------------爬取新浪新闻，指定的内容
# 1.寻找基础url
base_url = 'http://search.sina.com.cn/?'
# 2.设置headers字典和params字典，再发请求
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36',
}
key = '蔡徐坤'  # 搜索内容
params = {
    'q': key,
    'c': 'news',
    'from': 'channel',
    'ie': 'utf-8',
}
response = requests.get(base_url, headers=headers, params=params)
with open('sina_news.html', 'w', encoding='gb18030') as fp:
    fp.write(response.text)
