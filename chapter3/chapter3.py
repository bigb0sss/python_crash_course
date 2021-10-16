#!/usr/bin/python3

# List

lst = ['tmp1', 'tmp2', 'tmp3']

# Append
lst.append('tmp4')
print(lst)

def listAdd():
    lst2 = []

    n = 0
    while True:
        if n == 5:
            break
        else:
            lst2.append(str(n))
            n += 1

    return lst2

print(listAdd())

# Pop - Remove items by position
lst.pop(0)
print(lst)

# Remove - Remove items by value
lst.remove('tmp2')
print(lst)

# Sort 
lst.sort()
print(lst)
print(sorted(lst))

lst.sort(reverse=True)
print(lst)

# Reverse Order
lst.reverse()
print(lst)