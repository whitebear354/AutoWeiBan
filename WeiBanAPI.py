from urllib import request, parse
import http.cookiejar
import json

getCookiesURL = 'https://weiban.mycourse.cn/#/login'  # 获取Cookies URL

loginURL = 'https://weiban.mycourse.cn/pharos/login/login.do'  # 登录请求 URL

getNameURL = 'https://weiban.mycourse.cn/pharos/my/getInfo.do'  # 获取姓名 URL


# 获取一个新Cookie
def getCookie():
    cookie = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(getCookiesURL)
    # todo delete
    # for item in cookie:
    #     print(item.name + "=" + item.value)
    # todo
    print(cookie)
    return cookie


def login(keyNumber, password, tenantCode, cookie):
    param = {
        'keyNumber': keyNumber,
        'password': password,
        'tenantCode': tenantCode
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=loginURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    print(responseText)
    responseJSON = json.loads(responseText)
    print(responseJSON['data']['userId'])
    return responseJSON['data']['userId']


def getName(userId, tenantCode, cookie):
    param = {
        'userId': userId,
        'tenantCode': tenantCode
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getNameURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    print(responseJSON['data']['realName'])
    return responseJSON['data']['realName']
