#Write a function that tests whether a string is a palindrome.
def palindrome(string):
    string = string.lower()
    string = string.replace(" ","")
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")

name = input("Word: ")
palindrome(name)