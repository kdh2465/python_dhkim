import re;
print("hello, world!");
print(1+1);
#가난다라라
text ='abc'
print(text[0])
text = 'abcde fgh ijk'
print(text[2:5])
print(text[1:8])
print(text[-5:-1])



text = '0123456789'
print(text[0:9:2])
print(text[8:0:-1])
print(text[::-1])

text='abc {} {}'
text=text.format(123,234)
print(text)

print(text.replace('a',"K"))

text='abc b/c-d'
aa=text.split('.|/')
print(text.split('.|/'), aa)

print(re.split('/|-| ', text))

print('/'.join(re.split('/|-| ', text))) 

text = 'abc ABCD ABCD'
print(text.count('ABCD '))




