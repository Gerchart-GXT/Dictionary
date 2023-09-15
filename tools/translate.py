from bs4 import BeautifulSoup
import re, sys, requests
class HttpErro(Exception):
    def __init__(self, message):
        super().__init__(message)

class Translate:
    def __init__(self, lang):
        self.__lang = lang

    def _check_chinese(self, text):
        pattern = re.compile(r"[\u4e00-\u9fa5]+")
        return bool(pattern.search(text))

    def _get_xml(self, word):
        url = "https://www.youdao.com/result?word=" + word + "&lang=" + self.__lang

        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            raise HttpErro(str(response.status_code) + " 请求失败，请检查网咯")
            
    def _handle_en_to_cn(self, soup):
        dic = []

        express = soup.find('div', class_ = 'dict-book')
        if(express):
            meaning = express.find_all('li', class_ = 'word-exp')
            if(len(meaning) > 0):
                for i in meaning: 
                    pos = i.find('span', class_ = 'pos')
                    trans = i.find('span', class_ = 'trans')
                    if(pos and trans):
                        dic.append(pos.text + "\n" + trans.text)
                    else:
                        dic.append(trans.text)
            else:
                trans = express.find("p", class_ = "trans-content")
                if(trans):
                    dic.append(trans.text)
    
        phrase = []
        express = soup.find('div', class_ = 'webPhrase')
        if(express):
            meaning = express.find_all('div', class_ = 'col2')
            for i in meaning: 
                en = i.find('a', class_ = 'point')
                cn = i.find('p', class_ = 'sen-phrase')
                if(en and cn):  
                    phrase.append(en.text + "\n" + cn.text)
        return {
            "dic": dic,
            "phrase": phrase
        }
    
    def _handle_cn_to_en(self, soup):
        dic = []

        express = soup.find('div', class_ = 'dict-book')
        if(express):
            meaning = express.find_all('div', class_ = 'word-exp')
            if(len(meaning) > 0):
                for i in meaning: 
                    word = i.find('div', class_ = 'trans-ce')
                    dic.append(word.text)
            else:
                trans = express.find("p", class_ = "trans-content")
                if(trans):
                    dic.append(trans.text)
    
        phrase = []
        express = soup.find('div', class_ = 'webPhrase')
        if(express):
            meaning = express.find_all('div', class_ = 'col2')
            for i in meaning: 
                en = i.find('a', class_ = 'point')
                cn = i.find('p', class_ = 'sen-phrase')
                if(en and cn):  
                    phrase.append(en.text + "\n" + cn.text)
        return {
            "dic": dic,
            "phrase": phrase
        }

    def trans_from_youdaodic(self, word):
        trans_mode = self._check_chinese(word)
        response = ""

        try:
            response = self._get_xml(word)
        except HttpErro as e:
            print(e)    
            return

        soup = BeautifulSoup(response, 'html.parser')
        if(trans_mode):
            res = self._handle_cn_to_en(soup)
            return (1, res)
        else:
            res = self._handle_en_to_cn(soup)
            return (0, res)

if __name__ == "__main__":
    t = Translate("en")
    print(t.trans_from_youdaodic(input()))