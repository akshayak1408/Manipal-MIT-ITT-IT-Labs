str=input("enter a text")
l=list(str)
n=int(input("enter the shift number:"))
ans=""
for i in l:
    ans+=chr((ord(i)+n)%ord('z'))
print(ans)
