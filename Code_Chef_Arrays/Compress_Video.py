
t = int(input())
f
for _ in range(): 
    n = int(input()) 
    frames = list(map(int, input().split())) 

    min_frames = 0 
    for i in range(n - 1): 
        if frames[i] == frames[i + 1]: 
            min_frames -= 1 

    print(min_frames)