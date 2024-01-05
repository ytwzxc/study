#리스트 자료형
odd = [1, 3, 5, 7, 9]
empty = list() # 비어 있는 리스트 생성

#리스트 인덱싱
a = [1, 2, 3, 4, 5]
print(a) # output : [1, 2, 3, 4, 5]
print(a[0]) # output : 1
print(a[0] + a[2]) # output : 4
print(a[-1]) # output : 3, [-1] : 마지막 요소
print(a[:2]) # output : [1, 2], 두번째 요소까지
print(a[2:]) # output : [3, 4, 5], 두번째 요소 이후 끝까지
b = [1, 2, [1, 2, 3]] # 중첩하여 사용 가능
print(b[2][1]) # output : 2

#리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # output : [1, 2, 3, 4, 5, 6]
print(a * 2) # output : [1, 2, 3, 1, 2, 3]

#리스트 문자열과 더하기
a = [1, 2, 3]
print(a[2] + "hi") # output : Error, 정수와 문자열은 더할 수 없음.
print(str(a[2]) + "hi") # output : 3hi

#리스트 길이 구하기
a = [1, 2, 3]
len(a) # output : 3

#리스트 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a) # output : [1, 2, 4]

#리스트 요소 삭제하기
a = [1, 2, 3]
del a[1]
print(a) # output : [1, 3]

a = [1, 2, 3, 4, 5] 
del a[2:] # 두번째 요소 이후부터 삭제
print(a) # output : [1, 2]

#리스트에 요소 추가하기
a = [1, 2, 3]
a.append(4) # 리스트 맨 끝에 4를 추가
print(a) # output : [1, 2, 3, 4]

a.append([5, 6])
print(a) # output : [1, 2, 3, 4, [5, 6]]

#리스트 정렬
a = [1, 4, 3, 2]
a.sort() # 리스트의 요소를 순서대로 정렬
print(a) # output : [1, 2, 3, 4]

#리스트 뒤집기
a = ['a', 'c', 'd']
a.reverse()
print(a) # output : ['b', 'c', 'a']

#인덱스 반환
a = [1, 2, 3]
a.index(3) #3의 위칫값을 리턴
print(a) # output : 2

#리스트 요소 삽입
a = [1, 2, 3]
a.insert(0, 4) #0번째 위치에 4를 삽입
print(a) # output : [4, 1, 2, 3]

#리스트 요소 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 처음 나오는 3만 제거
print(a) # output : [1, 2, 1, 2, 3]

#리스트 요소 꺼내기
a = [1, 2, 3]
a.pop() # 맨 마지막 요소를 리턴하고 그 요소를 삭제
print(a) # output : [1, 2]

#리스트에 포함된 요소 x의 개수 세기
a = [1, 2, 3, 1]
a.count(1) # output : 2












