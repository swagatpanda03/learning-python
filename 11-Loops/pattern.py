#pattern

numbers = [5,2,5,2,2]
nums = [2,2,2,2,5]
#for i in numbers:
#    print('x' * i)

for i in nums:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)
