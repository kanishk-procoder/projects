#project in which we check if a string or phrase is a palindrome or not
#if not then make it palindrome string or phrase
#then return the palindrome string or phrase

main_str = input("Enter the string : ")
n = main_str
main_str = main_str.lower()
main_str = main_str.replace(" ","")
rev_str = main_str[::-1]

if main_str==rev_str:
    print(n)
else :
    n = main_str+rev_str
    print(n)