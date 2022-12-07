i1,i2=input("Enter the digits to be operated on:").split()
o=input("Enter the operator")
if o=="+":
    print(int(i1)+int(i2))
elif o=="-":
    print(int(i1)-int(i2))
elif o=="x":
    print(int(i1)*int(i2))
elif o=="/":
    print(int(i1)/int(i2))
elif o=="%":
    print(int(i1)%int(i2) and int(i2)%int(i1))
