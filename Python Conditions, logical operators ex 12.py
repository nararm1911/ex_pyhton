""" x - absizneri arancq
    y - oridinatneri arancq
"""

x = int(input('insert abscissa axis = '))
y = int(input('insert ordinate axis = '))

if x > 0 and y > 0:
    print('quarter is first')
elif x < 0 and y > 0:
    print('quarter is second')
elif x < 0 and y < 0:
    print('quarter is third')
elif x > 0 and y < 0:
    print('quarter is fourth')
