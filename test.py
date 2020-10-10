Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def findMax(a,b,c):
	if a>b:
		biggest=a
	else:
		biggest=b
	if c>biggest:
		biggest=c
	return biggest
a=int(input(“첫 번째 숫자 입력:”))
b=int(input(“두 번째 숫자 입력:”))
c=int(input(“세 번째 숫자 입력:”))

biggest=findMax(a,b,c)
print(a,b,c,“중 가장 큰 수는",biggest,“입니다.")