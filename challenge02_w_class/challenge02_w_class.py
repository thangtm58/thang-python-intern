import datetime
today = datetime.date.today()

class Person:
    def __init__(self, id, first_name, middle_name, last_name, dob, premium, claim_count):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = dob
        self.premium = premium
        self.claim_count = claim_count
#TODO: Em đã khai báo class như a Nam k dùng __init__ nhưng e debug thì bị lỗi dòng 28
employee = []

#Open input file
with open("input02.txt", "r") as f1:

    topic = f1.readline().rstrip('\n')
    n = f1.readline().rstrip('\n')
    data = f1.readlines()

#Assign value for each employee
idx = 0
while idx < len(data):
    #Split line into list
    nricfin = data[idx].split()
    employee_all = Person(*nricfin)
    employee.append(employee_all)
    employee[idx].year = int(employee[idx].dob[0:4])
    idx += 1

#Compute Age and Premium of each employee
for j in range(len(data)):
    employee[j].age = today.year - employee[j].year
    if employee[j].claim_count == max(employee.claim_count):
#TODO: Claim_count ở đây không phải là list nên không xài được max(),
# em có nên khai báo thêm 1 list rồi gán claim_count của tất cả employee vào không anh?
        employee[j].premium = int(employee[j].premium) * 3
    elif employee[j].age <= 26:
        employee[j].premium = int(employee[j].premium) * 2

#Write into output file
f2 = open("output02.txt", "w")
f2.write('%s\n' %(topic))
k = 0
while k < len(data):
    f2.write(f'{employee[k].id}, {employee[k].first_name.title()} {employee[k].middle_name[0]}. {employee[k].last_name}, {employee[k].age}, {employee[k].premium}\n')
    k += 1
f2.close()

