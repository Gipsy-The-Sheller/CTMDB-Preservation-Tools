import requests as req

def GetSrchRes(keyword):
    url = 'https://www.ganvana.com/'
    info = {'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'key-alive',
            'Content-Length':'19',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host':'ganvana.com',
            'Origin':'https://ganvana.com',
            'Referer':'https://ganvana.com',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'}
    infback = req.post(url = url+'SearchDic', data = {'keyword':keyword},headers = info)
    #在此添加代码
    return infback.text
