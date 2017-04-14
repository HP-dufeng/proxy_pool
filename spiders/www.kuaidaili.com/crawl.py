from bs4 import BeautifulSoup
import requests

import publisher

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

def crawl_proxy(url):
    count = 0
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    for sc in soup.find_all(attrs={"data-title": "IP"}):
        try:
            tr = sc.parent
            host = sc.text.strip()
            port = tr.find(attrs={"data-title": "PORT"}).text.strip()
            proxy_type = tr.find(attrs={"data-title": "类型"}).text.strip()
            publisher.push((host, port, proxy_type))

            count+=1
        except:
            pass

    return count

def getther_links(size): 
    links = set()

    for i in range(size):
        url = "http://www.kuaidaili.com/free/inha/{0}/".format(i+1)
        links.add(url)
    
    return links




