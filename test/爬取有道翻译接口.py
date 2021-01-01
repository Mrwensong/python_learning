import requests, time, random, hashlib

base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
value='world'#搜索单词
data = {
    'i': value,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15722497498890',
    'sign': 'a5bfb7f00ee1906773bda3074ff32fec',
    'ts': '1572249749889',
    'bv': '1b6a302b48b06158238e3c036feb6ba1',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '239',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ntes_nnid=106c3a7170510674c7f7d772e62a558b,1565682306312; OUTFOX_SEARCH_USER_ID_NCOO=1135450303.6725993; OUTFOX_SEARCH_USER_ID="-1737701989@10.168.11.11"; P_INFO=str_wjp@126.com|1570794528|0|other|00&99|not_found&1570667109&mail_client#bej&null#10#0#0|152885&0||str_wjp@126.com; _ga=GA1.2.1944828316.1572140505; JSESSIONID=aaa-Ya9um-M_N80M5xr4w; ___rl__test__cookies=1572249749875',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
# ---------------------------------------js代码中
# ts="" + (new Date).getTime()
# salt=r + parseInt(10 * Math.random(), 10)
# sign=n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
# ------------------------------转化为python代码
def get_md5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding='utf-8'))
    return md5.hexdigest()

ts = str(int(time.time() * 1000))
salt = ts + str(random.randint(0, 10))
sign = get_md5("fanyideskweb" + value + salt + 'n%A-rKaT5fb[Gy?;N5@Tj')
response = requests.post(base_url, headers=headers, data=data)
print(response.text)