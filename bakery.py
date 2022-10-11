f=int(input("enter the number to fresh loaves purchased:"))
o=int(input("enter the number of day old loaves purchased:"))
if((f<0)or(o<0)):
    print ("enter proper value:")
else:
    r=185
    f*=185
    o*=185*60/100
    total=f+o
    print("regular price:rs.",r)
    print("amount of new loaves:",f)
    print("amount of day old loaves:",o)
    print("total amount:rs.",total)

