#변수 (variable) Part1.9

from re import A


aa=100  #여기서 aa는 변수, =는 대입연산자, 100은 리터럴
        #변수는 객체를 가리키고 있음(참조) 파이선에서 사용하는 모든 자료는 객체

a='a'
b=a
a='b'
print(a,b)

aa=100
bb=100

print(id(aa))
print(id(bb))
bb=200
print(id(bb))
cc=bb
print(id(cc))
cc=300
print(id(cc))

print(aa, bb, cc) # 마치 자바에서 String의 저장방식과 유사