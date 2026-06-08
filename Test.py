dic = {"Codingal":2, "is":2, "best":2, "for":2,"coding":1}

print("The orignal dictionary : " + str(dic))

K = 2
r = 0

for k in dic: 
    if dic[k] == K: 
        r = r + 1

print("Frequency of K = ", str(r))