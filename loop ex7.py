from random import randrange


rand_num = int(randrange(1, 100))
attempt = 10

while attempt > 0:
    num_user = int(input('Please input number = '))
    if num_user == rand_num:
        print('you won )))')
        break
    elif num_user <= rand_num:
        print('number is small')
        attempt -= 1
    elif num_user >= rand_num:
        print('number is big')
        attempt -= 1

print(f'hidden number is {rand_num}')
