#list methods

numbers = [5,2,1,7,4,5,5,5]

print(numbers)

#insert a number at the end of the list
numbers.append(20)

print(numbers)

#insert a number at any index
numbers.insert(0,12)
print(numbers)


numbers.insert(4,112)
print(numbers)

#remove an item
numbers.remove(5)
print(numbers)


#removes last item from the list
numbers.pop()
print(numbers)

#returns the first occurence of a number passed
print(numbers.index(4))

#returns true or false
print(112 in numbers)

#it will returns how many times a number is stored in the list.
print(numbers.count(5))

#sorting the list
numbers.sort()      #it does not return any values so if we print this it will display None
print(numbers)

#reverse our list
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

#remove all elements of the list
numbers.clear()
print(numbers)
