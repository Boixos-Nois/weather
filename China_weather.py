

from bs4 import BeautifulSoup
import requests
import time
from echarts import Echart,Bar,Axis


TEMPERATURE_LIST = []
CITY_LIST = []
MIN_LIST = []


def get_mmm(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://www.weather.com.cn/textFC/db.shtml',
        'Host': 'www.weather.com.cn'
    }

    req = requests.get(url, headers=headers )

    content = req.content

    soup = BeautifulSoup(content, 'lxml')

    conMidtab = soup.find('div', class_='conMidtab')
    conMidtab2_list = conMidtab.find_all('div', class_='conMidtab2')
    for x in conMidtab2_list:
        tr_list = x.find_all('tr')[2:]
        p = ''
        for index, tr in enumerate(tr_list):
            min = 0
            if index == 0:
                td_list = tr.find_all('td')
                p = td_list[0].text.replace('\n', '')
                city = td_list[1].text.replace('\n', '')
                min = td_list[7].text.replace('\n', '')
            else:
                td_list = tr.find_all('td')
                city = td_list[0].text.replace('\n', '')
                min = td_list[6].text.replace('\n', '')

            print(p + city + '  ' + '最低气温' + min)


def main():
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml']
    for url in urls:
        get_mmm(url)
        time.sleep(3)

if __name__ == '__main__':
    main()










