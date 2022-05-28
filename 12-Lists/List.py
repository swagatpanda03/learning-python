names = ['Ichigo', 'Bakugo', 'Madara', 'Hashirama', 'Aizen']
print(names)

#accessing 2nd element
print(names[1])
#accessing last item
print(names[-1])

print(names[2:])    #return all items from 2nd index to end of the list.
print(names[2:4])   #return all elements from 2nd index to 3rd index(4-1) index

names[0] = 'Pain'
print(names)
