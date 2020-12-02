import bs4
import requests
import  os

def pic_and_gif():
    url = 'http://zmarsa.pl'
    soup = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
    path = os.getcwd()

    k = 0
    pages = int(input('how many pages :'))

    for i in soup.find_all("div", {"class": "bigImg"}):
        for j in i.find_all('img'):
            uri = j.get('src')
            ext = str(uri).split('.')
            ext = '.' + ext[1]
            r = requests.get(url + uri)
            with open(path + str(k) + ext, 'wb') as f:
                f.write(r.content)
                k += 1
    if pages > 1:
        for a in range(2, pages+1):
            uri = url + '/strona/' + str(a)
            soup = bs4.BeautifulSoup(requests.get(uri, verify=True).text, 'html.parser')
            for i in soup.find_all("div", {"class": "bigImg"}):
                for j in i.find_all('img'):
                    uri = j.get('src')
                    ext = str(uri).split('.')
                    ext = '.' + ext[1]
                    r = requests.get(url + uri)
                    with open(path + str(k) + ext, 'wb') as f:
                        f.write(r.content)
                        k += 1


def vid():
    url = 'http://pornhub.com'
    soup = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
    k = 0
    for i in soup.find_all("li", {"class": "js-pop videoblock videoBox"}):
        for j in i.find_all('a'):
            uri = j.get('href')
            if str(uri).split('.')[0] == "/view_video":
                u = url + uri
                print(uri)
                r = requests.get(u)
                with open('D:/turbo_download/' + str(k) + '.mp4', 'wb') as f:
                    f.write(r.content)
                    k += 1


pic_and_gif()
# vid()
