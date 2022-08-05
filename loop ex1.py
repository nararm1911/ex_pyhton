num_1 = '1244215'
num_even = 0
num_odd = 0
for i in num_1:
    conv_i = int(i)
    if conv_i % 2 == 0:
        num_even += 1
    else:
        num_odd += 1

print(f'{num_even} num_even')
print(f'{num_odd} num_odd')