## 람다 함수
$$lambda \text{ 입력값} : \text{ 결과값}$$

```python
plus_ten = lambda x: x + 10
print(plus_ten(5))  # 결과: 15
```
```python
users = [
    {'name': '김철수', 'age': 25},
    {'name': '이영희', 'age': 20},
    {'name': '박민수', 'age': 30}
]
# lambda u: u['age'] -> "유저(u)가 들어오면 나이(u['age'])를 기준으로 삼아라"
sorted_users = sorted(users, key=lambda u: u['age'])

print(sorted_users)
# [
# {'name': '이영희', 'age': 20}, 
# {'name': '김철수', 'age': 25}, 
# {'name': '박민수', 'age': 30}
# ]
```

```python
nums = [1, 2, 3, 4, 5]

# 모든 숫자를 제곱하고 싶다면?
# lambda x: x ** 2 -> "x가 들어오면 x의 제곱을 내놔라"
squared = list(map(lambda x: x ** 2, nums))

print(squared) 
# 결과: [1, 4, 9, 16, 25]
```


```python
nums = [1, 2, 3, 4, 5, 6]

# 짝수만 남기고 싶다면?
# lambda x: x % 2 == 0 -> "x를 2로 나눈 나머지가 0인 것(True)만 통과시켜라"
evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)
# 결과: [2, 4, 6]
```