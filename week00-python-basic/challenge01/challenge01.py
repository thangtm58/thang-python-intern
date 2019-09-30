
# Open file
l = []
with open("input01.txt", "r") as f1:
    # Read next line
    line = f1.readline()
    # check line is not empty
    while line:
        v = float(line.strip())  # v aka value
        l.append(v)
        print(line.strip())
        line = f1.readline()
f1.close()

f = open('output01.txt', 'w')
f.write(f'Day la so nho nhat: {min(l)} ')
print(min(l))
f.close()

