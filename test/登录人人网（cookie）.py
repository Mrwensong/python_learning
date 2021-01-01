import requests

base_url = 'https://www.cnblogs.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36',
    'set-cookie': 'set-cookie',
}
response=requests.get(base_url, headers=headers)
# with open('新浪.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)
if 'dronw' in response.text:
    print('登录成功')
else:
    print('登录失败')