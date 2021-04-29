import requests
from urllib.parse import quote, unquote
import ssl
import lxml
import pyperclip
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
kv = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}


def danyinzichuli(soup):
    yin = soup.find(id='pinyin').find('b')
    yin = str(yin).replace('<b>', '').replace('</b>', '')
    shiyi = []
    shiyin_weichuli = soup.find('div', {'class': 'tab-content'}).find('dl').find('dd').find_all('p')
    for i in shiyin_weichuli:
        i = str(i)
        i = i.replace('<span>', ' ').replace('</span>', ' ').replace('<p>', '').replace('</p>', '') + '\n'
        shiyi.append(i)
    return {yin: shiyi}



def duoyinzichuli(soup):
    result = {}
    temp = []
    shiyin_weichuli = soup.find('div', {'class': 'tab-content'}).find_all('dl')
    for i in shiyin_weichuli:
        yin = str(i.find('dt', {'class': 'pinyin'})).replace('<dt class="pinyin">[ ', '').replace(' ]</dt>', '')
        shiyi_weichuli = i.find('dd').find_all('p')
        for j in shiyi_weichuli:
            j = str(j)
            j = j.replace('<span>', ' ').replace('</span>', ' ').replace('<p>', '').replace('</p>', '') + '\n'
            temp.append(j)
        result[yin] = temp
        temp = []
    return result

def chakanduobuduo(soup):
    shiyin_weichuli = soup.find('div', {'class': 'tab-content'})
    if '查看更多' in str(shiyin_weichuli):
        return True
    else:
        return False


def get_message(r):
    url = "http://hanyu.baidu.com/s?wd=" + quote(r, 'utf-8') + "&ptype=zici"
    print(url)
    r = requests.get(url, headers=kv, timeout=30, verify=False)
    soup = BeautifulSoup(r.text, "lxml")
    pinyin = soup.find(id='pinyin').find_all('b')
    if len(pinyin) == 0:
        print('没有查询到')
        result = {}
    elif len(pinyin) == 1:
        print('查询到了一个')
        result = danyinzichuli(soup)
        key = list(result.keys())
        pyperclip.copy (key[0])
        print('已经复制到粘贴板')

    elif len(pinyin) > 1:
        print('这是多音字')
        result = duoyinzichuli(soup)
    if chakanduobuduo(soup):
        print("拼音太多，请前往网页查看。链接为{}".format(url))
        return True, True, result
    elif len(result) > 0:
        return False, True, result
    else:
        return False, False, {}

if __name__ == '__main__':
	while True:
		try:
			a = input("输入你要查询的字：")
			if a == '0':
				exit(0)
			duoma, chaxun, result = get_message(a)
			print(result)
		except:
			print("遇到问题了")
