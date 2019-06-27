import WeiBanAPI
import time #time.sleep延时

tenantCode = '51900002' # 吉珠学院码

figletFile = open('.\\figlet', 'r')
print(figletFile.read())
figletFile.close()

print(
    '默认院校为吉林大学珠海学院，ID:' + tenantCode + '\n'
    + '若有需要，请自行抓包获取院校ID修改' + '\n'
)

account = input('请输入账号\n')
password = input('请输入密码\n')

print('\n获取Cookies中')
cookie = WeiBanAPI.getCookie()
print('Cookies获取成功')

loginResponse = WeiBanAPI.login(account, password, tenantCode, cookie)

try:
    print('登录成功，userName:' + loginResponse['data']['userName'])
except BaseException:
    print('登录失败')
    print(loginResponse)
    exit(0)

try:
    print('请求用户数据')
    stuInfoResponse = WeiBanAPI.getStuInfo(loginResponse['data']['userId'],
                                           tenantCode,
                                           cookie)
    print('用户资料：' + stuInfoResponse['data']['realName'] + '\n'
          + stuInfoResponse['data']['orgName']
          + stuInfoResponse['data']['specialtyName']
          )
except BaseException:
    print('解析用户数据失败，将尝试继续运行，请注意运行异常')

print(WeiBanAPI.getProgress(loginResponse['data']['preUserProjectId'],
                            tenantCode,
                            cookie))

try:
    print('请求课程进度')

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


for i in range(101):
    string = 'loading... ' + str(i) + '%'
    print(string, end='')    # 不换行
    print('\b' * len(string), end='', flush=True)    # 删除前面打印的字符
    time.sleep(0.2)