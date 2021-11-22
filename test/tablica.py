from bs4 import BeautifulSoup
from urllib import request, error

try:
    with request.urlopen('https://ru.uefa.com/uefachampionsleague/standings/') as resp:
        data = resp.read()
        soup = BeautifulSoup(data, 'html.parser')
        items = soup.get_text()
        items = soup.find_all('span', attrs={' class': 'ellipsisize hsKSJe '})
        print(items)
        for item in items:
            text = item.get_text()
            print(text)
        

    # with request.urlopen('https://ru.uefa.com/uefachampionsleague/standings/') as resp:
    #     data = resp.read()
    #     soup = BeautifulSoup(data, 'html.parser')
    #     # items = soup.get_text()
    #     items = soup.find_all('strong', attrs={'class': 'js-points'})
    #     # print(items)
    #     for item in items:
    #         text = item.get_text()
    #         print(text)
    
                
except error.HTTPError as e:
    print(e)  

