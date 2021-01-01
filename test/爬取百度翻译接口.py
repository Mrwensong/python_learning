import requests

base_url = 'https://fanyi.baidu.com/sug'
kw = input('请输入要翻译的英文单词：')
data = {
    'kw': kw
}
headers = {
    # 由于百度翻译没有反扒措施，因此可以不写请求头
    'content-length': str(len(data)),
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'referer': 'https://fanyi.baidu.com/',
    'x-requested-with': 'XMLHttpRequest'
}
response = requests.post(base_url, headers=headers, data=data)
# print(response.json())
result = ''
for i in response.json()['data']:
    result += i['v'] + '\n'
    print(i['v'] + '\n')
print(kw+'的翻译结果为：')
print(result)
