try:
    a = 3/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')


try:
    a = 5
    b = 0
    c = a / b
except Exception as e:
    print('다음과 같은 오류가 발생했습니다: {}'.format(e))