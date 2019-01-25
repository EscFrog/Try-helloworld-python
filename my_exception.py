from unexpected_rsp_value import UnexpectedRSPValue

value = '가'
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue

except UnexpectedRSPValue:
    print("오류가 발생했습니다.")