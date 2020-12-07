# 1.print
# Hello, world!
# Hello, world! 출력하기

# 1번
print('Hello, world!\nHello, world!')
# 2번
print('Hello, world!'); print('Hello, world!')
# 3번
print('Hello, world!')
print('Hello, world!')
# 4번
print('Hello, world!'), print('Hello, world!'),

# 2.divmod()
(quotient, remainder) = divmod(5,2)
print(quotient, remainder)
print(type(divmod(5,2)))

# 2.복소수
cn = 1.2+1.3j
print(cn)
print(type(cn))

# 3.튜플대입
x, y, z = 10, 20, 30
print(x, y, z)
a = b = c = 40
print(a==c)
x, y = y, x
print(x, y)

# 4.split() => string method
a, b = input('문자열 두 개를 입력해주세요 : ').split()
print(a, b)


# 5.map()
c, d = map(int, input('숫자 두 개를 입력하세요 : ').split())
print(c+d)

# 6.print(sep='{argument}' || end='{argument}')
print(1,2,3, sep=",")
print(1,2,3, end=',')
