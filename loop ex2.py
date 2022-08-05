numbers = '12345'
num_sum = 0
num_prod = 1
for number in numbers:
    conv_number = int(number)
    num_sum += conv_number
    num_prod *= conv_number

print(f'sum is {num_sum}')
print(f'prod is {num_prod}')