mine = '보'
yours = '바위'

if mine == yours:
    print('비김')
elif mine == '가위' and yours == '보':
    print('이겼다')
elif mine == '바위' and yours == '가위':
    print('이겼다')
elif mine == '보' and yours == '바위':
    print('이겼다')
else:
    print('졌다')