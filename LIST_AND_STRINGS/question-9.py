#Write a function that concatenates two lists. [a,b,c],[1,2,3] -> [a,b,c,1,2,3]
def con_list(list1, list2):
    return list1 + list2

a = ["a", "b", "c"]
b = [1, 2, 3]
c = con_list(a, b)
print(c)