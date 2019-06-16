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
    responseJSON = json.loads(responseText)
    return responseJSON['data']['userId']


def getStuInfo(userId, tenantCode, cookie):
    param = {
        'userId': userId,
        'tenantCode': tenantCode
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getNameURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    return responseJSON['data']['realName'] + ' ' + responseJSON['data']['gender']