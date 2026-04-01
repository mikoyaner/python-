import requests
import json
url='https://mainnet.infura.io/v3/76223180ca554cad9b16c8879ef4db76'
datas={
    "jsonrpc": "2.0",
    "id": "17",
    "method": "eth_call",
    "params": [{"data": "0x76c23ff1","to": "0xc5e9ddebb09cd64dfacab4011a0d5cedaf7c9bdb"}, "latest"]
}
headers = {
'origin':'https://app.proofofhumanity.id',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
}
def getpro():
    maxTryNum = 40
    for tries in range(maxTryNum):
        try:
            repo = requests.post(url=url, headers=headers, data=json.dumps(datas))
            Dict = repo.json()
            str_num = Dict['result']
            num = int(str_num, 16)
            return num
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                print("Has tried %d times to access url %s, all failed!" % (maxTryNum, url))
                break
