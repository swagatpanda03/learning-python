course = 'Python for Beginners'

print(len(course))

#len is a general purpose function
#print is also general purpose funciton 
print(course.upper())  #specific to string method
course = course.upper()
print(course)
print(course.lower())
course = course.lower();
print(course)


print(course.find('p'))     #index of P
#find is case-sensitive
#if found returns index else returns -1 (p != P)

print(course.replace('beginners', 'absolute beginners'))    #case-sensitive

#in operator

print('python' in course)
