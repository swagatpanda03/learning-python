#Binary Search

numbers = [1, 2, 3, 4, 5]
target = 13
low = 0
high = len(numbers)
is_found = False
while low < high:
    mid = int((low+high)/2)

    if numbers[mid] == target:
        print(f'Present at index: {mid}')
        is_found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if is_found == False:
    print("Element is not present in the list")
