
# in an array find the maximum in array 

t = int(input()) 

for _ in range(t): 
    n = int(input()) 

    arr = [int(x) for x in input().split()] 

    max = arr[0] 

    for i in range(1,n): 
        if arr[i] > max: 
            max = arr[i] 

    print(max) 