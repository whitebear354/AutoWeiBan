import WeiBanAPI

getCookiesURL = 'https://weiban.mycourse.cn/#/login'  # 获取CookiesURL

loginURL = 'https://weiban.mycourse.cn/pharos/login/login.do'  # 登录请求URL

studentNum = '04181030'

tenantCode = '51900002X'


def crawlerName():
    cookie = WeiBanAPI.getCookie()
    # print('Get Cookie: ' + cookie)
    userId = WeiBanAPI.login(studentNum, studentNum, tenantCode, cookie)
    name = WeiBanAPI.getName(userId, tenantCode, cookie)
    return name

crawlerName()