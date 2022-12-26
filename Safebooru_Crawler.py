import requests
import re
from bs4 import BeautifulSoup
import urllib.request


def spider(max_pages):
    page = 1
    while page < max_pages:
        res =requests.get(
            url = 'https://safebooru.org/index.php?page=post&s=list&tags=made_in_abyss+&pid=' + str(
            (page - 1) * 40)
        )
        soup = BeautifulSoup(res.content, 'lxml')
        
        for link in soup.find_all("span", attrs={"class":"thumb"}):
            link=str(link.find_all("a")[0].attrs["href"])
            
            url_pic = "http://safebooru.org/" + link
            # print (url_pic)
            
            source_code_pic = requests.get(url_pic)
            soup1=BeautifulSoup(source_code_pic.content, 'lxml')
            image=soup1.find("img",attrs={"id":"image"}).attrs["src"]
            source_code_pic=requests.get(image)
            img_data=BeautifulSoup (source_code_pic.content, "lxml")
            name=image.split('/')[-1].split('?')[0]
            asdf=img_data.find("body")
            print (image)
            # print(asdf)
            img_data = requests.get(image, verify=False).content
            with open(name, 'wb') as handle:
                handle.write(img_data)

        page += 1

spider(50)