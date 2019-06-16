import WeiBanAPI
import time

tenantCode = '51900002X'  # 吉珠
sleeptime = 0


def crawlerStuInfo(studentNum):
    cookie = WeiBanAPI.getCookie()
    # print('Get Cookie: ' + cookie)
    userId = WeiBanAPI.login(studentNum, studentNum, tenantCode, cookie)
    stuInfo = WeiBanAPI.getStuInfo(userId, tenantCode, cookie)
    return stuInfo


# print(crawlerStuInfo(studentNum))

# file = open('C:\\Users\\Adam\\Desktop\\student', 'a')

for studentNum in range(00000000, 0000000): # 这里填写学号信息
    file = open('C:\\Users\\Adam\\Desktop\\student16', 'a')
    studentNumStr = '0' + str(studentNum)
    print('正在获取学生' + studentNumStr)
    try:
        studentInfo = crawlerStuInfo(studentNumStr)
        file.write(studentNumStr + '  ' + studentInfo + '\n')
    except BaseException:
        print(BaseException)
    file.close()
    time.sleep(1)