import requests
def postjson(url,datas):
    maxTryNum = 40
    for tries in range(maxTryNum):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
            }
            response = requests.post(url=url, headers=headers, timeout=60,data=datas)
            return response.json()
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                print("Has tried %d times to access url %s, all failed!" % (maxTryNum, url))
                break
def gettext(url):
    maxTryNum = 40
    for tries in range(maxTryNum):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'
            }
            response = requests.get(url=url, headers=headers, timeout=60)
            response.encoding = response.apparent_encoding
            r1_text=response.text
            return r1_text
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                print("Has tried %d times to access url %s, all failed!" % (maxTryNum, url))
                break