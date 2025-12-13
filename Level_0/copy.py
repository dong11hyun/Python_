colors = ['red,','blue','green']
b = colors
b.append('white')
print(b)
print(colors)


# 변수 a ─────▶ [ 리스트 A (ID: 100) ] ──┐
#                                       │
#                                       ▼
#                                     (내용물)
#                                       ▲
# 변수 b ─────▶ [ 리스트 B (ID: 200) ] ──┘
#                (새로 생성됨!)

# 1. 원본 데이터 (힘들게 크롤링 함)
raw_data = ['C', 'A', 'B'] 
# 2. 보여주기용 복사본 생성 (껍데기만 복사)
view_data = raw_data.copy()
# 3. 복사본을 정렬해서 보여줌
view_data.sort() 
print(view_data) # ['A', 'B', 'C'] (정렬됨)
# 4. 원본은?
print(raw_data)  # ['C', 'A', 'B'] (살아있음! 언제든 복구 가능)


# 단순 조회,그냥 a 씀,굳이 복사할 필요 없음. 보기만 할 거니까.
# 정렬/필터링,b = a.copy(),원본 순서나 데이터가 망가지면 안 되니까.
# 데이터 수정,b = deepcopy(a),"리스트 안의 딕셔너리 값까지 싹 바꿔야 하고, 원본은 지켜야 할 때."