data = ['a', 'b', 'c', 'd', 'e']
print(data)
data.append('g')  # append 는 리스트 끝에 추가 / 하나의 (리스트 자체) 도 추가가능

data.insert(1,"dh") # insert는 리스트(인덱스에 추가 가능)
print(data)

list = [1,2]
data.extend(list) # extend는 "반복가능객체" 를 개별 요소로 추가 
print(data)

# pop() - 제거기준(인덱스) / 반환값 = 제거된 요소
# remove() - 제거기준('값') / 반환값 없음
# del - 제거기준_인덱스or슬라이스 / 반환값 없음

# print("".join(data))