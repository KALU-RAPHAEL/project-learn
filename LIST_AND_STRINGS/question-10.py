#Write a function that combines two lists by alternatingly taking elements, [a,b,c],[1,2,3] -> [a,1,b,2,c,3]
def com_list(list1, list2):
    combined_list = []
    min_length = min(len(list1), len(list2))
    
    for item1, item2 in zip(list1, list2):
        combined_list.append(item1)
        combined_list.append(item2)
    
    if len(list1) > min_length:
        combined_list.extend(list1[min_length:])
    elif len(list2) > min_length:
        combined_list.extend(list2[min_length:])
        
    return combined_list

a = ['a', 'b', 'c']
b = [1, 2, 3]
c = com_list(a, b)
print(c)