n=int(input("number of words:"))
l=[]
print("enter words")
for i in range(n):
    word=input()
    l.append(word)
print("Sorted words:",sorted(l))
