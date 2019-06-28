import WeiBanAPI
import json
import time  # time.sleep延时


tenantCode = '51900002' # 吉珠学院码


# 程序版本信息打印，脚本写的咋样不说，先把B装了
figletFile = open('.\\figlet', 'r')
print(figletFile.read())
figletFile.close()

print(
    '默认院校为吉林大学珠海学院，ID:' + tenantCode + '\n'
    + '若有需要，请自行抓包获取院校ID修改' + '\n'
)

# 登录信息输入
account = input('请输入账号\n')
password = input('请输入密码\n')


# 获取Cookies
print('\n获取Cookies中')
cookie = WeiBanAPI.getCookie()
print('Cookies获取成功')

# 登录请求
loginResponse = WeiBanAPI.login(account, password, tenantCode, cookie)

try:
    print('登录成功，userName:' + loginResponse['data']['userName'])
except BaseException:
    print('登录失败')
    print(loginResponse)# TODO: 这里的loginResponse调用没有考虑网络错误等问题
    exit(0)

# 请求解析并打印用户信息
try:
    print('请求用户信息')
    stuInfoResponse = WeiBanAPI.getStuInfo(loginResponse['data']['userId'],
                                           tenantCode,
                                           cookie)
    print('用户信息：' + stuInfoResponse['data']['realName'] + '\n'
          + stuInfoResponse['data']['orgName']
          + stuInfoResponse['data']['specialtyName']
          )
except BaseException:
    print('获取用户信息失败，将尝试继续运行，请注意运行异常')

# 请求课程完成进度
try:
    getProgressResponse = WeiBanAPI.getProgress(loginResponse['data']['preUserProjectId'],
                                                tenantCode,
                                                cookie)
    print('课程总数：' + str(getProgressResponse['data']['courseNum']) + '\n'
          + '完成课程：' + str(getProgressResponse['data']['courseFinishedNum']) + '\n'
          + '结束时间' + str(getProgressResponse['data']['endTime']) + '\n'
          + '剩余天数' + str(getProgressResponse['data']['lastDays'])
          )
except BaseException:
    print('获取课程进度失败，将尝试继续运行，请注意运行异常')
    print(getProgressResponse) # TODO: 这里的getProgress调用没有考虑网络错误等问题

# 请求课程列表
try:
    getListCourseResponse = WeiBanAPI.getListCourse(loginResponse['data']['preUserProjectId'],
                              '3',
                              tenantCode,
                              '',
                              cookie)
except BaseException:
    print('请求课程列表失败')

##################################################################################以上为抓到课程列表代码，全部注释对返回JSON进行研究
#
# f = open('.\\JSON', 'r')
# getListCourseResponse = json.loads(f.read())
#
##################################################################################
print('解析课程开始')
print(len(getListCourseResponse['data']))
for i in getListCourseResponse['data']:
    print('\n----章节码：' + i['categoryCode'] + '章节内容：' + i['categoryName'])
    for j in i['courseList']:
        print('课程内容：' + j['resourceName'] + '\nuserCourseId:' +j['userCourseId'])
        print('发送完成请求')
        delayInt = WeiBanAPI.getRandomTime()
        print('随机延时' + str(delayInt))
        time.sleep(delayInt)
# try:
#     print('请求课程进度')

# print('获取Cookie中')
# cookie = WeiBanAPI.getCookie()
#
# userId = WeiBanAPI.login(studentNum, studentNum, tenantCode, cookie)
# stuInfo = WeiBanAPI.getStuInfo(userId, tenantCode, cookie)
#
#
# # print(crawlerStuInfo(studentNum))
#
# # file = open('C:\\Users\\Adam\\Desktop\\student', 'a')
#
# for studentNum in range(00000000, 0000000): # 这里填写学号信息
#     file = open('C:\\Users\\Adam\\Desktop\\student16', 'a')
#     studentNumStr = '0' + str(studentNum)
#     print('正在获取学生' + studentNumStr)
#     try:
#         studentInfo = crawlerStuInfo(studentNumStr)
#         file.write(studentNumStr + '  ' + studentInfo + '\n')
#     except BaseException:
#         print(BaseException)
#     file.close()
#     time.sleep(1)

#
# for i in range(101):
#     string = 'loading... ' + str(i) + '%'
#     print(string, end='')    # 不换行
#     print('\b' * len(string), end='', flush=True)    # 删除前面打印的字符
#     time.sleep(0.2)
