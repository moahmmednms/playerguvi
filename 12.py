inp=int(input())
sum=1
if(inp == 0):
    print("0")
elif(inp  > 0 ):
    for i in range(inp ,0,-1):
        sum=sum*i
elif(inp < 0):
    print("Invalid")
        
print(sum)
