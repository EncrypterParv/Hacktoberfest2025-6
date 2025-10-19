n,a,b,c= map(int, input().split())
sum= a+b+c
day= n//sum
rem=n%sum
td= day*3
if rem !=0:

    if rem<=a:
        
        td+=1
    elif rem<=a+b:
        
        td+=2

    else:
        td+=3
print(td)
