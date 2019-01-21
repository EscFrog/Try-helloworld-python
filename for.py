patterns = ['가위', '보', '보', '가위', '가위', '가위','보','가위','가위','보']
for pattern in patterns:
    print(pattern)

for i in range(5):
    print(i)

names = ['철수','영희','바둑이','귀도']

for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i+1, name))

names.append('비단뱀')
for i, name in enumerate(names): # 파이썬은 쉼표를 사용하여 반환값을 여러 개 돌려줄 수 있다.
    print('{}번: {}'.format(i+1, name))

