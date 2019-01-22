try:
    list = []
    print(list[0])
except Exception as ex:
    print('오류가 발생했습니다.', ex)
    
try:
    text = 'abc'
    number = int(text)
except Exception as ex:
    print('오류가 발생했습니다.', ex)