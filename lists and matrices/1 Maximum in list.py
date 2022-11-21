listin = [1, 4 ,-1, 646, 34]

m = listin[0]
for i in range (len(listin)):
    if m < listin[i]:
        m = listin[i]
print(m)        