#Exceptions
#0 - means success
#anything but 0 i.e 1,2,etc - means program crashed

#try:
#    age = int(input('Age: '))
#    income = 20000
#    risk = income/age
#    print(age)
#except ValueError:
#    print('Numbers are accepted only')


try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age  cannot be zero')
except ValueError:
    print('Numbers are accepted only')
