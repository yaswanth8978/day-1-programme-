def numsquaresum(n):
    squaresum=0;
    while(n):
        squaresum+=(n%10)*(n%10);
        n=int(n/10);
        return squaresum;
def ishappynumber(n):
    slow=n;
    fast=n;
    while(True):
        slow=numsquaresum(slow);
        fast=numsquaresum(numsquaresum(fast));
        if(slow!=fast):
            continue;
        else:
            break;
        return (slow==1);
n=int(input("enter the number:"))
if (n<=0):
    print("invalid")
else:
    if(ishappynumber(n)):
        print(True);
    else:
        print(False);
