import requests
# 读取url

base_url = 'http://baidu.com'
# 发送请求get
response = requests.get(base_url)
# print(response.encoding)
# print(response.text)
# with open('index.html', 'w', encoding='utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))
# print(response.status_code)
# print(response.headers)
# print(type(response.text))
print(type(response.content))
