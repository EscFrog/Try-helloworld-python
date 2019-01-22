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
