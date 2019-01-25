import hashlib
user_db = {}

class SignUpError(Exception):
    pass    # 메소드나 클래스 정의 후 꼭 들여쓰기된 문장이 있어야 하므로 pass 키워드가 있다.

class UsernameAlreadyExists(SignUpError):
    pass

class UnsafePassword(SignUpError):
    pass

class PasswordDoesNotMatches(SignUpError):
    pass


def sign_up(username, password, password_check):
    if username in user_db.keys():
        raise UsernameAlreadyExists('이미 존재하는 아이디 {}'.format(username))
    
    if len(password) < 6 or username == password:
        raise UnsafePassword('안전하지 않은 암호입니다.')
    
    if password != password_check:
        raise PasswordDoesNotMatches('암호와 암호 확인이 일치하지 않습니다')

    user_db[username] = hashlib.sha1(
        '$G:{}:{}'.format(username, password).encode()
    ).hexdigest()

try:
    sign_up('hello world', 'safe_password', 'safe_password')
    sign_up('hello world1', 'safe_password', 'safe_password11')
except (UsernameAlreadyExists, UnsafePassword, PasswordDoesNotMatches) as e:
    print(e)



