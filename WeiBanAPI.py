from urllib import request, parse
import http.cookiejar
import json
import random

baseDelayTime = 10  # 基础延时秒数

randomDelayDeviation = 10  # 叠加随机延时差

getCookiesURL = 'https://weiban.mycourse.cn/#/login'  # 获取Cookies URL

loginURL = 'https://weiban.mycourse.cn/pharos/login/login.do'  # 登录请求 URL

getNameURL = 'https://weiban.mycourse.cn/pharos/my/getInfo.do'  # 获取姓名 URL

getProgressURL = 'https://weiban.mycourse.cn/pharos/project/showProgress.do'  # 获取进度 URL

getListCourseURL = 'https://weiban.mycourse.cn/pharos/usercourse/listCourse.do'


# 获取一个新Cookie
def getCookie():
    cookie = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    return cookie


# 登录请求
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
    return responseJSON
    # return responseJSON['data']['userId']


# 获取学生信息
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
    return responseJSON


# 获取课程进度
def getProgress(userProjectId, tenantCode, cookie):
    param = {
        'userProjectId': userProjectId,
        'tenantCode': tenantCode
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getProgressURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    return responseJSON


# 获取课程列表
def getListCourse(userProjectId, chooseType, tenantCode, name, cookie):
    param = {
        'userProjectId': userProjectId,
        'chooseType': chooseType,
        'tenantCode': tenantCode,
        'name': name
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getListCourseURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    return responseJSON


def getRandomTime():
    return baseDelayTime + random.randint(0, randomDelayDeviation)
