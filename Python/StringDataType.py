#문자열 연산

head = "Python"
tail = " is fun!"

print("=" * 15)
print(head + tail)
print("=" * 15)
""" 
===============
Python is fun!
===============
"""

#문자열 길이 구하기, len 함수
Greeting = "Hello, Python!"
print(len(Greeting)) # output : 14

#문자열 인덱싱 : indexing이란 무엇인가를 '가리킨다'라는 의미이다.

print(Greeting[0]) # output : H
print(Greeting[1]) # output : e
print(Greeting[2]) # output : l

# Python은 0부터 숫자를 셈

#문자열 슬라이싱
s = Greeting[0:5] #끝 번호인 5번 문자는 포함하지 않음
print(s) # output : Hello

# 문자열 포매팅
a = "I eat %d apples"
print(a%3) #output : I eat 3 apples

b = "I eat %s apples"
print(b%"five") #output : I eat five apples

#문자열 포맷 코드
"""
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)
"""