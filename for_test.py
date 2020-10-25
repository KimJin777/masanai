# a = [1,2,3,4,5,6,7]

# for i in a:
#     print(i*100)



number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dan = [2, 3, 4, 5, 6, 7, 8, 9]


for i in dan:
    if i == 3: 
        continue
    for j in number:
        print(i, " * ", j, "= ", i * j )

