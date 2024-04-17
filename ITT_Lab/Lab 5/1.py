a=input("enter an expression:")
try:
    print(eval(a))
except Exception as e:
    print("Error:",e)
