l = []
lst = []
with open("input01b.txt", "r") as f1:
    # Read next line
    n = int (f1.readline())
    line = f1.readline()
    # check line is not empty
    while line:
        l.append(float (line.strip()))
        print(line.strip())
        line = f1.readline()
    print(l)
f1.close()

lst = []
for i in range(n):
    if l[i] == max(l):
        lst.append(1)
    else: lst.append(0)
print(lst)

#ghi vao file output
f2 = open('output01b.txt', 'w+')
for i in range(n):
    f2.write('%d\n' %(lst[i]))
f2.close()

