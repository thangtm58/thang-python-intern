#open file
# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
#
# f = f'{dir_path}/input01.txt'
#
# n = 6
# l = []
#
# for i in range(0, n):
#     l[i] = f.readline()
#     print(l, end = '\n')
#
# # Close file
# f.close()


# Open file
l = []
lst = []
with open("input01.txt", "r") as f1:
    # Read next line
    line = f1.readline()
    # check line is not empty
    while line:
        v = float(line.strip())  # v aka value
        l.append(v)
        print(line.strip())
        line = f1.readline()
    print(l)
f1.close()

f = open('output01.txt', 'w')
f.write('Day la so nho nhat: %.2f ' % (min(l)))  #TODO Thang use f-string please
print(min(l))
f.close()

#TODO Thang collect challenge01 's related file into challenge01/ folder
