#Write a function that returns the elements on odd positions in a list.
def odd_element(list):
    return list[1::2]

num = [1, 7, 9]
print(odd_element(num))