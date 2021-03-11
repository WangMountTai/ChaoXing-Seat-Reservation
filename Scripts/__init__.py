import requests
import datetime
import base64
import json


def login():
    # 使用ajax发送请求。
    url = "https://passport2.chaoxing.com/fanyalogin"
    # 登录的用户名
    uname = "15707262946"
    # 登录的明文密码
    password = "12345678asdf"
    # 使用base64进行密码加密
    pwd = base64.b64encode(password.encode())
    fid = "-1"
    # 登录成功以后跳转的链接
    refer = ""
    #
    t = "true"
    data = {
        "fid": fid,
        "uname": uname,
        "password": pwd,
        "refer": refer,
        "t": t
    }
    # 发送post请求
    response = requests.post(url, data)
    # 将cookies对象转化为dict对象
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    with open("cookies.txt", "w") as f:
        # 将cookies信息写入到文件中
        f.write(json.dumps(cookies, ensure_ascii=True))


"""
   传入已经登录成功后返回的cookie。传入一个字典
"""


def SeatReservation(cookie):
    # 用于登录超星，获得相应的cookie
    url = "http://office.chaoxing.com/front/third/apps/seat/code?id=5695&seatNum=48"
    # url = "http://blog.jacksonben.top:8090"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Host": "office.chaoxing.com",
        "Connection": "keep-alive",
        # "Cookie": cookie,
        "Cookie": "route=211ba283594120b6653b6e1a70b74da6; oa_deptid=1907; oa_uid=83125222; oa_name=%E9%98%BF%E5%90%88%E5%88%AB%E5%8B%92%E5%BE%B7%C2%B7%E5%8F%B6%E6%9D%A5%E6%95%A3%E6%8B%9C; oa_enc=1cd9d7143e01080acb68bbb9e2772c1e; uname=2018403282; lv=1; fid=1907; _uid=83125222; uf=b2d2c93beefa90dc9de887681ac536ff2a9e62be89d6345b67fa403a528d2aadc0c447c66104c3bffc2a53bcc19ef720c49d67c0c30ca5047c5a963e85f11099a647e086c098c4d1ce71fc6e59483dd3da99cdbc3bcd97d5e4aa1821de1215610c8b139300376554; _d=1615393730465; UID=83125222; vc=F749A39C614EC10061EBE7907E9326FB; vc2=30421DE7FF3B5C81E54E70C31ED5A27E; vc3=Qv3IgrgPBNWmNj9TB8iAQSpu73WWWgQsH3PmZWB8H5DlQJx6Jy5b5w6j6ZGsoN%2BwI0O9v9LToankBmFz5yvhZIj%2FOnlUhQchv0Vq2eKp%2FizVFFLlLCzWHq%2BNjz2%2BMoJss7Bh1bC6OoLqQ63RZkArERKtGMtQrDaWUbXLVfycxLw%3D067d4e98fc3eeaef5f582f3be1c4b44a; xxtenc=7c50f9a7afc64b2e14ec479d93f80d7d; DSSTASH_LOG=C_38-UN_208-US_83125222-T_1615393730466; JSESSIONID=672C0D872A71B19B7F5BDEEFB060FFB9.reserve_web_123",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 10; zh-Hans-CN; JER-AN20 Build/HUAWEIJER-AN20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Quark/4.6.9.167 Mobile Safari/537.36",
        "Referer": "http://office.chaoxing.com/front/third/apps/seat/code?id=5695&seatNum=49",
        "X-Requested-With": "XMLHttpRequest"
    }
    proxies = {
        'http': 'http://10.254.4.145:8888',
        'https': 'http://10.254.4.145:8888'
    }
    # print(str(type(headers)))
    # pass
    print(headers)
    return requests.get(url, headers=headers, proxies=proxies)


if __name__ == '__main__':
    cookie_dict = {}
    # main方法
    # print(datetime.time)
    # login()
    # response = login()
    # with open()
    # print(response)
    # print(response.headers)
    # print(response.cookies)
    # data = "12345678asdf"
    # re = base64.b64encode(data.encode())
    # print(re)
    # 调用登录方法，登录成功以后将cookie写入到本地文件中
    # response = login()
    # 登录方法测试成功
    # print(response.text)
    # print(response.headers)
    # print(response.cookies)
    # type(response.text)
    # 将获得的cookie保存到本地的文件中,返回的是一个dict类型
    # cookies = requests.utils.dict_from_cookiejar(response.cookies)
    # 将cookie的dict对象转化为str
    # json = json.dumps(cookies, ensure_ascii=False)
    # print(str(type(json)))
    # print(json)
    # print(cookies)
    # 将cookie写入到文件中
    # with open("cookies.txt", "w") as f:
    #     f.write(json)
    # f的类型为_io.TextIOWrapper
    with open("cookies.txt", "r") as f:
        # dic = []
        for line in f.readlines():
            # 获得的line就是str类型。
            # print(type(i))
            #     dicts = line.split(",")
            #     for i in dicts:
            #         dic.append(i)
            # cookie_dict = dict(dic)
            reponse = SeatReservation(line)
        print(reponse.status_code)
        print(reponse.text)
    #         cookie_dict = eval(line)
    # reponse = SeatReservation(cookie_dict)
    # print(reponse.text)
    # cookie_dic = dict[dic]
    # print(type(cookie_dict))
    # print(cookie_dict)

    # print(type(json.dumps(f, ensure_ascii=type)))
