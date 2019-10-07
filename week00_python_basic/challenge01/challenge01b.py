def find_max_claim(input, output):
    l = []
    with open(input, "r") as f1:
        # Read next line
        n = int(f1.readline())
        line = f1.readline()
        # check line is not empty
        while line:
            l.append(float(line.strip()))
            print(line.strip())
            line = f1.readline()
        print(l)
    f1.close()

    is_max = []
    for i in range(n):
        if l[i] == max(l):
            is_max.append(1)
        else:
            is_max.append(0)
    print(is_max)

    # ghi vao file output
    f2 = open(output, 'w+')
    for i in range(n):
        f2.write(f'{is_max[i]}\n')
    f2.close()

find_max_claim(input='input01b.txt', output='output01b.txt')