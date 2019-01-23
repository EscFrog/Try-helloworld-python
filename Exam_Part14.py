def safe_index(a_list, value):
    if value in a_list:
        return a_list.index(value)
    else:
        return None

a = safe_index([2,3,4,1], 3)
b = safe_index([2,3,4,1], 8)
print(a,b)

list1 = [1,2,3,4]
print(list1)

list1.insert(0, 8)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

weather = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장
words = weather.split()

# index()를 이용해서 "흐림"이 words의 몇 번째에 있는지 찾고 position에 저장
position = words.index("흐림")
words[position] = "맑음"

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장
# words를 문자열로 바꿀 때는 공백 한 칸을 기준으로 붙인다.
new_weather = " ".join(words)

print(new_weather)


rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

# red_colors가 빨주노의 값을 갖도록 rainbow를 슬라이스
red_colors = rainbow[:3]
print(red_colors)

# blue_colors가 파남보의 값을 갖도록 rainbow를 슬라이스
blue_colors = rainbow[rainbow.index("파"):]
print(blue_colors)

def substring(s, start, end):
    return s[start:end]

str = "Hello world"
between_2_5 = substring(str, 2, 5)
print(between_2_5)

list2 = list(range(20))

new_list = list2[5:15:3]
print(new_list)

another_list = list2[5:18:4]
print(another_list)

list3 = list(range(6))
print(list3)

list3[1:4] = [11,22,33]
print(list3)

list4 = list(range(6))
print(list4)

del list4[1:4]
print(list4)