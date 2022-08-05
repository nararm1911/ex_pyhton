
a = int(input('side1 ='))
b = int(input('side2 ='))
c = int(input('side3 ='))

if a + b <= c or a + c <= b or b + c <= a:
    print('not valid')
else:
    if a == b == c:
        print('valid equilateral')
    elif  a == b or a == c or b == c:
        print('valid , isosceles')
    else:
        print('valid scalene')




