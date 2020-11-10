import googletrans as gt
d1 = gt.LANGUAGES
d2 = {}
count = 0
for i in d1.items() :
    if (i[0] == 'hi') :
        print(count)
    d2[i[1]] = i[0]
    count += 1
print(d2)