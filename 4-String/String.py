course = "Python's Course for Beginners"

sentence = '''
Hello Bruce,
Here is our first mail to you.
Thank You
'''
print(course)
print(sentence)

print(course[0])    #first index
print(course[-1])   #last index
print(course[-2])   #2nd last index

print(course[0:3])  #starting from index 0 to index 2
print(course[0:])   #starting form index 0  to end
print(course[2:])

print(course[:5])

course1 = course[:]     #copying the whole string

print(course1)
