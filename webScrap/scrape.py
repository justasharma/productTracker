from bs4 import BeautifulSoup
import requests
import pandas as pd

HEADERS = ({
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Accept-Language':
    'en-US, en;q=0.5'
})

url = 'https://www.amazon.in/ASRock-RX7600-SL-8GO-Graphics/dp/B0C6HTVV52/ref=sr_1_1?crid=146L2NZF5VYN0&dib=eyJ2IjoiMSJ9.l8dcHOIJA_H5yld6_UJ0MvdAIJQ9jO6UezgWJSa3U3I7sQXKjB-lUkf812Ep3U2QUlkY_RdwPTxo_7edDyjBIDnk9WVEk0dK6s1VeHHiLZ8ODUe4r03OUxNX-Fsx8jnatQG0t2bMk_S3_x3veMTY-wALZKuceD9Ovn-azFhcDtFrayzlEsS5Bfhh3ftSaVOpnFgzNuSPPNuVddzWjyZm0vkfs9DRups4lCqMB3vIfbg.JfbJ0BGetnrb7cSBMNie6MOhhqsbomlfiixslaLKivY&dib_tag=se&keywords=graphics+card&qid=1714832827&sprefix=graphics+ca%2Caps%2C289&sr=8-1'
html_text = requests.get(url, headers=HEADERS).text
soup = BeautifulSoup(html_text, 'lxml')

try:
    price = soup.find('span',attrs={'class':'aok-offscreen'}).get_text().strip()
    title = soup.find('span',attrs={'class' : 'a-size-large product-title-word-break'}).get_text().strip()
    data = {'Product': [title], 'Price': [price]}
    df = pd.DataFrame(data)
    df.to_csv('./products.csv',index= False)
    print('data saved')
except AttributeError as e:
    print('request was unsuccessful')