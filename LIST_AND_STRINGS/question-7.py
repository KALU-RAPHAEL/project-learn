#Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.

#1
def for_loop(num):
    total = 0
    for n in num:
        total += n
    return total

#2
def while_loop(num):
    total = 0
    index = 0
    while index < len(num):
        total += num[index]
        index += 1
    return total

#3
def recursion(num):
    if not num:
        return 0
    else:
        return num[0] + recursion(num[1:])

rem = [1, 2, 3, 45, -4, 69]
print(for_loop(rem))
print(while_loop(rem))
print(recursion(rem))