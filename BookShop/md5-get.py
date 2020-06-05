import hashlib

for i in range(100000000):
    str_i = str(i)
    hash1 = hashlib.md5()                #md5转utf-8
    hash1.update(str_i.encode("utf-8"))  #转码 
    str_md = hash1.hexdigest()
    if str_md[:6] == '6cf9fc':
        print(i)
        break

#输出结果
#a146d9  ==>  31772644
