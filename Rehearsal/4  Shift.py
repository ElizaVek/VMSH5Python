
def shift(df,d):
    a = df
    
    
    iters = 0
    answer = [0] * len(a)
    for i in range(len(a)):
        
        if d > 0:
            answer[i] = a[-d]
            d -= 1
        else:
            answer[i] = a[iters]
            iters += 1
    
    return answer
        
d = int(input())
df = [1,2,3,4,5,6,7]

shift (df,d)
print(shift (df,d))