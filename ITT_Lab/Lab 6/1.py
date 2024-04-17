text=input("enter a string:")
l=list(text)
if l==l[::-1]:
    print("palindrome")
else:
    print("not palindrome")
