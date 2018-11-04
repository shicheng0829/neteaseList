import requests
from bs4 import BeautifulSoup


def get_music(url):
    musicListFile = open('musicList.txt', 'a')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    find_list = soup.find('ul',class_="f-hide").find_all('a')
    musicListFile.write(soup.find('h2',class_='f-ff2 f-brk').string+'\n')
    for a in find_list:
        music_url = 'http://music.163.com'+a['href']
        music_name = a.text
        musicListFile.write(music_name+' '+music_url+'\n')
    musicListFile.write('\n')
    musicListFile.close()


def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    results = soup.find_all(name='a', attrs={'class': 'tit f-thide s-fc0'})
    lst = []
    for a in results:
        print(a['href'])
        lst.append(a['href'])
    return lst


def crawlerByPage(num):
    url = 'https://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
    for i in range(num):
        url = url.replace('offset='+str((i-1)*35), 'offset='+str(i*35))
        print(url)
        lst = get_url(url)
        for a in lst:
            get_music('https://music.163.com'+a)


if __name__ == '__main__':
    crawlerByPage(3)