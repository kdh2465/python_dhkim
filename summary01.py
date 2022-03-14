# 주석 표현

# 자료형 (DataType) : 숫자/문자열/리스트/튜플/집합딕셔너리
'''
# 숫자형
    정수: integer : 파이썬에서는 long형이 따로 없다. 크기의 범위가 제한이 없음 (무제한)
        10진수: 12342
        8진수: 0o123
        16진수: 0x123
        2진수: 0b1100
    실수: 부동소수점(float) : 크기의 범위ㅣ가 8Byte : 4.9*10^-324~1.8*10^308
        123.45
        1e10 : 10의 지수형태로 표기 1*10^10
        1.3E-3 : 10의 지수형태로 표기 1.3*10^-3
    복소수:  크기의 범위가 16Byte : 4.9*10^-324~1.8*10^308 (실수부와 허수부가 각각 8byte)
        3+10j # 허수부분은 j로 표기
        complex(2,3)

#문자열 : 문자와 문자열을 통합하여 사용 (문자의 나열읠 의미) 작은따옴표 또는 큰따옴표 사용
    'hello python' : 공백과 탭 모두 유지, 작은 따옴표 가능
    "hello python" : 큰 따옴표 가능
    "I'm OK!" : 이 경우 큰따옴표로 표현하는 것이 좋음
    'I\'m OK!' : 제어문자(\)를 사용하여 표현가능    


'''
#숫자형--------------------------
#정수형
print(12342)
print(0o123)
print(0x123)
print(0b1100)
#실수형
print(123.45)
print(1.2e3)
#복소수
print(2+3j)
print(complex(2,3))
print((2+3j).real)
print((2+3j).imag)


#문자열 ---------------------------
print('Hello python')
print("Hello python")
print("I'm OK!")
print('I\'m OK!')
print('''안녕하세요
반갑습니다.''') #print문 안에서 '''를 세개 쓰는 경우 여러줄로 표현 가능 (주석+여러줄 출력)

""" #마찬가지로 내부에 '''이 포함되어 있어 혼동의 여지가 있는 경우 " 표시 3개를 사용하여 주석처리 가능
print('''안녕하세요
반갑습니다.''') #print문 안에서 '''를 세개 쓰는 경우 여러줄로 표현 가능 (주석+여러줄 출력)
"""
print('반갑습니다.')




# 숫자연산 : (+, -, *, /)
a=10
b=10
c=100
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a**3)#a^3
print(a//3)
print(a%3)
print(divmod(a,3))

# 문자연산 : 이스케이프 코드(\n: 줄바꿈, \r: 캐리지리턴, \":큰따옴표 출력, \':작은따옴표 출력, \000: 널문자, \t: 수평탭, \\:'\'문자)
#           파이썬은 문자열을 더하고 곱할 수 있다.

#문자열 더하기 (concatenation)
a="You've got"
b=' a friend'
print(a+b) #문자열 더하기
print('abc'*5) #문자열 * 숫자 : 문자를 숫자만큼 반복하기
print('+'*30)


# 인덱싱과 슬라이싱
# 인덱싱
str = "you've got a friend!"
for i in range(0, len(str)):
    print(i, str[i])

for i in range (-1, -len(str)-1, -1):
    print(i, str[i])

# 슬라이싱
print(str[13:19])
print(str[0:3])
print(str[11:])
print(str[:19])
print(str[:])
print(str[19::-1])
print(str[-7:-1])
print(str[-7:])
print('0123456789'[-1::-1])

str="20220314 18:50"
date = str[0:8]
time = str[9:]
print(date+'년')
print(time+'시')

#문자열의 교체
aa="ABCD"
print(aa[1])
# aa[1]='F' #오류. 문자열의 요소값은 변경할 수 없다 (자바등과 동일한 개념)
print(aa[1])

aa=aa[:1]+'F'+aa[2:]
print(aa)

#문자열 포맷팅(Format) : 문자열 내에 어떤 값을 삽입하는 것 예>'평균점수는 {}이다'

"""
%s: 문자열(String)
%d: 정수(decimal)
%o: 8진수(octal)
%x: 16진수(hex)
%c: 문자(character)
%%: 리터럴 %
"""

print("내이름은 %s 이다." %"홍길동")
print("나이는 %d입니다." %20)

print('내 이름은 %s이고 %d살이다.' %('홍길동', 20))

print('|%6.2f|'%4.1256)
print('|%-6.2f|'%4.1256)
print('|%10s|'%'abc') #오른쪽정렬
print('|%-10s|'%'abc') #왼쪽정렬

print('|%10s|'%'방가워') #오른쪽정렬
print('|%-10s|abc'%'hello')


age=22
print("나이는 %d입니다"%age)

name='홍길동'
print("이름:%s 나이:%d%%" %(name, age) )

#포맷코드의 활용예 - 소숫점 표현하기
print('%0.5f'%2.4545)

# 
