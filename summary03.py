# 튜플(tuple) : 리스트와 유사하나 값의 변경 및 추가 삭제 불가능 + 소괄호 사용

from xmlrpc.client import Boolean


tu=() # 빈 값이 들어가 있는 형태 (값을 추가하거나 변경이 안되기 때문에 이렇게 사용하는 예는 없음)
print(tu)
#tu[0]=2 # 오류: 값변경 불가

tu2=(1,) #중요, 하나의 요소가 있을때는 뒤에 쉼표를 표시 (수학식의 ()소괄호와의 구분을 위해서인듯 )
print(tu2)

tu3=(10, 20, 30, 40)
print(tu3)

tu4=10, 20, 30 # 괄호없이 사용가능 자동 튜플화
print(tu4)

tu5=('국제시장', '명량', (2,3), [1, 2, 3])
print(tu5) #튜플내의 원소로도 어떤 타입도 올 수 있음



# 튜플의 인덱싱, 슬라이싱, 연산
# 인덱싱
tu=('a', 'b', 'c', 10, 1000)
print(tu[0])

#슬라이싱
print(tu[2:])

tu=tu+('d', 'e', 'f')
print(tu)
print(tu*3)

# del tu[2] # 오류발생 (문자열과 튜플은 삭제 불가능)


 


#불리언 (True, False) : 
#   문자열  :   "aa"(True), ""(False)
#   리스트  :   [1,2,3](True), [](False)
#   튜플    :   ('a', 'b')(True), ()(False)
#   숫자    :   0 이외의 값(True), 0(False)
#   None    :   (False)

print(bool('ab'))
print(bool(''))
print(bool([1,2,3]))
print(bool([]))
print(bool((1,)))
print(bool(()))
print(bool(1))
print(bool(-0.5))
print(bool(0.012))
print(bool(0))
print(bool(None))




