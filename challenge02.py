id = []
first_name = []
middle_name = []
last_name = []
dob = []
dob1 = []
premium = []
claim_count = []
year = []
month = []
day = []
age = []

#mo file
with open("input02.txt", "r") as f1:

    topic = f1.readline().rstrip('\n')
    n = f1.readline().rstrip('\n')
    data = f1.readlines()
idx = 0  # mốc bắt đầu
length = len(data)  # mốc kết thúc

while idx < length:
    # tách một dòng thành một list
    line_list = data[idx].split()

    id.append(line_list[0])
    first_name.append(line_list[1])
    middle_name.append(line_list[2])
    last_name.append(line_list[3])
    dob.append(line_list[4])
    premium.append(int (line_list[5]))
    claim_count.append(int (line_list[6]))
    dob1.append(dob[idx].split('-'))
    idx += 1


i = 0
#nhap vao gia tri year month day
while i < length:
    year.append(int(dob1[i][0]))
    month.append(int(dob1[i][1]))
    day.append(int(dob1[i][2]))
    i += 1

#tinh tuoi va tinh premium
for j in range(length):
    age.append(2019 - year[j])
    if claim_count[j] == max(claim_count):
        premium[j] *= 3
    elif age[j] <= 26:
        premium[j] *= 2

#viet vao file output
f2 = open("output02.txt", "w")
f2.write('%s\n' % (topic))
k = 0
while k < length:
    f2.write('%s, %s %s. %s, %d, %d\n' %(id[k], first_name[k].title(), middle_name[k][0].title(), last_name[k].upper(), age[k], premium[k]))
    k += 1
f2.close()
