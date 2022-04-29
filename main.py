from requests import get

while 1:
    print('shit')
    try:
        get("http://kotofoto.ru", timeout=0.00001)
    except:
        continue
