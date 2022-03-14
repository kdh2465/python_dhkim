#제어문 (조건문, 반복문) : 프로그램의 흐름을 제어해서 효율적으로 이용하기 우한 명령문

# 조건문 : if문
# 반복문 : while문/for문

# if문의 기본 구조 
#    중요1. (indentation(들여쓰기)가 가장 중요) : 파이썬에만 있는 특징
#    중요2. (들여쓰기 이전에는 : 사용)

# if <조건문>:
#     <실행명령 1>
#     <실행명령 2>
#     ...
# else:
#     <실행명령 1>
#     <실행명령 2>
#     ...

#참고 세미콜론
a=1; b=2 #단, 한줄에 여러 명령어를 위치시키는 경우에는 각 명령어를 구분하기 위해 사용
print(a,b)

number = 1; #마지막에 세미콜론을 써도 되지만 생략해도 무방

if number:
    print("0이 아니다")

else :
    print("0이다")

# 비교연산자
# <, >, ==, !=, >=, <= : 자바의 연산자와 동일

x=1000
y=1000
print(x>y)
print(x!=y)


"""
#논리연산자 (and는 논리연산, &는 비트연산) : 연산자별로 따로 정의 필요
x and y =  x & y (&&,||,!기호 없음 )
x or y = x|y
not x



"""
print (3 and 5, 3 or 5) # 계산이 어
print(True & False, True and False)
print(True | False, True or False)
print(not False)

print(3 and 4, '값')
print(3 & 5, '값')

print(0 or 0, '값')


# in 연산자
# x in 리스트/튜플/문자열
# x not in 리스트/튜플/문자열

print('a' in ['a', 'b', 'c'])
print('a' not in ['a', 'b', 'c'])
print('a' in 'abcde')
print('bc' in 'abcde')

