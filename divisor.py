num=int(input("ingrese un valor entero:"))
den=int(input("inrese otro valor entero:"))
x=0
y=num
while y>=den:
    y-=den
    x+=1
print("la division es "+str(x) +" con resto "+ str(y))
print(num/den)
