year = input('請輸入西元年')
year = int(year)

def is_leap(x):
    if x % 4 != 0:     #2003是平年
        return False
    elif x % 100 != 0:  #2004是閏年
        return True
    elif x % 400 != 0:  #1900是平年
        return False
    elif x % 3200 != 0: #2000是閏年
        return True
    else:               #3200是平年
        return False

if is_leap(year):
    print(year, '是閏年')
else:
    print(year, '是平年')


