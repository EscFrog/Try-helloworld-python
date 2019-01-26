areas =[]
for i in range(1,11):
    areas.append(i**2)
print(areas)

areas2 = [i**2 for i in range(1,11)]
print("areas2:", areas2)

# 한 변의 길이가 짝수인 정사각형의 넓이 구하기
areas3 = []
for i in range(1,11):
    if i % 2 == 0:
        areas3.append(i**2)
print(areas3)

# 위와 같은 프로그램을 list_comprehension 으로 구하기
areas4 = [i**2 for i in range(1,11) if i % 2 == 0]
print("areas4:",areas4)