import urllib.request
import urllib.parse

from bs4 import BeautifulSoup
from googletrans import Translator


def imageLookup(imagepath):
    try:
        googlepath = 'http://www.images.google.com/searchbyimage?image_url=' + imagepath
        print(googlepath)
        headers = {}
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        req = urllib.request.Request(googlepath, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        soup = BeautifulSoup(respData, "html.parser")

        container = soup.find('div', class_='r5a77d')
        translator = Translator()
        val = translator.translate(container.a.text)
        ret = val.text

        container = soup.find('div', class_='wwUB2c kno-fb-ctx')
        try:
            x = str(container)
            val = x.split('">')[2].replace("</span></div>", "", -1)
            val = translator.translate(val)
            ret = ret + "\n" + val.text
        except Exception:
            ret + "\n" + "no additional info found"
        return ret

    except Exception as e:
        print(str(e))

