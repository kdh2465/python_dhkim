#변수 (variable) Part1.9

from re import A


aa=100  #여기서 aa는 변수, =는 대입연산자, 100은 리터럴
        #변수는 객체를 가리키고 있음(참조) 파이선에서 사용하는 모든 자료는 객체


#is 파이썬의 내장함수 (두개의 변수가 서로 같은 값을 가지고 있는지 파악)
# 참고 현재 변수가 가리키는 참조값(주소) 알아오기 id

#문자번지비교
a='kkk'
b=a
print(a is b) # True
a='mmm'
print(a is b) #False
print(a,b) 
print(id(a), id(b))
print()

#숫자번지비교
a=100
b=100
print(a is b) # True
b=200
print(a is b) # False
print(a,b)
print(id(a), id(b))
print()

#튜플번지비교
a=(1,2,3)
b=a
print(a is b) # True
b=(4,5,6)
print(a is b) # True
print(a,b)
print(id(a), id(b))
print()

#리스트번지비교
a=[1,2,3]
b=a
print(a is b) # True
b[2]=5
print(a is b) # True
print(a,b)
print(id(a), id(b))
print()

#셋번지비교
a={1,2,3}
b=a
print(a is b) # True
b.add(4)
print(a is b) # True
print(a,b)
print(id(a), id(b))
print()

#딕셔너리번지비교
a={1:'가',2:'나',3:'다'}
b=a
print(a is b) # True
b[4]='라'
print(a is b) # True
print(a,b)
print(id(a), id(b))
print()

# 중요-------------------
# 즉, 정리하면 Java의 리터럴로 생성한 String처럼 숫자, 문자, 튜플의 경우 한번 생성된 값을 공유하는 방식
# 새롭게 값이 바꾸면 새로운 번지를 가리킴
# 반면 리스트, 셋, 딕셔너리는 객체 내부의 데이터를 수정할 수 있는 형태라 두 변수가 공유함



#변수의 삭제
aa=3
bb=5
# del aa   #변수의 삭제방법1 (파이썬에서도 가비지컬렉터가 있어서 사용하지 않는 경우 자동으로 사라짐)
# del(bb)  #변수의 삭제방법2
print(aa)
print(bb)

#변수의 선언 및 초기화
cc = dd =100 # 여러개의 변수에 동일한 값을 대입
print(cc, dd)
cc, dd = "국제시장",  '명량'
print(cc, dd)
(cc, dd) = ('aa', 'bb') # 튜플형태로 받기
print(cc, dd)
[cc, dd] = ['하이', '파이선'] # 리스트형태로 받기 
print(cc, dd)
print()

#참조변수의 복사 1. : 하나의 객체를 두개의 변수가 바라보고 있는 경우
aa=['a', 'b', 'c']
bb=aa
print(aa is bb) # True
print(aa,bb)
print(id(aa), id(bb))
print()

#참조변수의 복사 2. : 각각의 객체를 쳐다보고 있는 경우
aa=['a', 'b', 'c']
bb=aa[:] # 이렇게하면 주소값을 복사하는 것이 아니라 객체 생성이후 내용물 자체를 복사하는 개념
print(aa is bb) # False
print(aa,bb)
print(id(aa), id(bb))
print()

#파이선에서 변수(식별자) 이름 만들기 규칙
#1. 식별자의 첫문자는 알파벳, 밑줄(_)
#2. 첫문자이외에 나머지 글자는 밑줄, 숫자(0~9)가 올 수 있다.
#3. 식별자는 대/소문자를 구분한다. (myname vs. myName)
#4. i, aa, name_1_2 (O) 2name, a ab, my-name, ?abc(X)


_a=3
print(_a)

