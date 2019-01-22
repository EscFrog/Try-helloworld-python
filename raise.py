def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError("'가위', '바위', '보' 가운데 하나의 값만 입력받을 수 있습니다.")
    if yours not in allowed:
        raise ValueError("'가위', '바위', '보' 가운데 하나의 값만 입력받을 수 있습니다.")

# rsp('가위','바')
# try-except 문을 넣어서 예외를 잡아내면 프로그램이 종료되지 않는다.
try:
    rsp('가위','바')
except ValueError:
    print('잘못된 값을 넣었습니다')
 

classroom = {
    '1반':[162,175,198,137,145,199],
    '2반':[165,177,157,160,191]
}
try:
    for class_id, heights in classroom.items():
        for height in heights:
            if height > 190:
                print(class_id, '에 190이 넘는 학생이 있습니다')
                raise StopIteration
except StopIteration:
    print('정상종료')
