# AutoMyCourse 自动麦课

## 开发日志

## 抓包分析

### 登录请求

Request URL: https://weiban.mycourse.cn/pharos/login/login.do

Status Code: 200 OK

HEAD:
```
Host: weiban.mycourse.cn
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 64
Connection: keep-alive
Referer: https://weiban.mycourse.cn/
Cookie: XXXX
```

Parameter: 

|                |                |
|----------------|----------------|
|keyNumber       |学号            |
|password	     |密码            |
|tenantCode	     |学院编码         |

Response:
```Json
{
    "code":"0",
    "data":{
        "userId":"用户ID",
        "userName":"账号，吉珠是身份证",
        "isBind":"1",
        "tenantCode":"学院编号",
        "batchCode":"003",
        "gender":1,
        "openid":"oeNC****57Zc",
        "switchGoods":1,
        "switchDanger":1,
        "switchNetCase":1,
        "isConfirmed":2,
        "preUserProjectId":"4ca8****c6a6任务ID",
        "preAlias":"新生安全教育",
        "preBanner":"https://h.mycourse.cn/pharosfile/resources/images/projectbanner/pre.png",
        "normalAlias":"安全课程",
        "normalBanner":"https://h.mycourse.cn/pharosfile/resources/images/projectbanner/normal.png",
        "specialAlias":"专题学习",
        "specialBanner":"https://h.mycourse.cn/pharosfile/resources/images/projectbanner/special.png",
        "militaryAlias":"军事理论",
        "militaryBanner":"https://h.mycourse.cn/pharosfile/resources/images/projectbanner/military.png",
        "isLoginFromWechat":2
    },
    "detailCode":"0"
}
```

### 