import os
import datetime
from datetime import date
today = datetime.date.today()

class Person:
    def __init__(self, nricfin, first_name, middle_name, last_name, dob, premium, claim_count):
        if nricfin.isdigit():
            raise Exception('n must be a string')
        else:
            self.nricfin = nricfin

        name = first_name + ' ' + middle_name + ' ' + last_name
        # tc06b
        if any(char.isdigit() for char in name):
            raise Exception('s must not include number')
        else:
            self.first_name = first_name
            self.middle_name = middle_name
            self.last_name = last_name

        # tc07a
        for ele in dob.split('-'):
            if not ele.isdigit():
                raise Exception('d must be a date i.e. yyyy-mm-dd')
        self.dob = dob

        # tc08a
        if float(premium) > 0:
            self.premium = premium
        else:
            raise Exception('p must be a positive float number')

        # tc09a
        if claim_count.isdigit() and int(claim_count) >= 0:
            self.claim_count = claim_count
        else:
            raise Exception('c must be a not-negative integer')

    def calculate_claims(self, claims_list):
        d = [ele for ele in self.dob.split('-')]
        year = d[2]
        today = date.today()
        self.age = today.year - int(year)

        if self.claim_count == max(claims_list):
            return self.premium * 3
        elif self.age > 26:
            return self.premium
        else:
            return self.premium * 2

def read_input(input):
    # Open input file
    with open(input, "r") as f:
        topic = f.readline().rstrip('\n')
        n = f.readline().rstrip('\n')
        data = f.readlines()

    # Assign value for each employee
    idx = 0
    driver = []
    while idx < len(data):
        # Split line into list
        info = data[idx].split()
        driver_info = Person(*info)
        driver.append(driver_info)
        idx += 1
    claims_list = [dri.claim_count for dri in driver]
    for dri in driver:
        dri.calculate_claims(claims_list)
    return topic, n, driver

def write_input(output, topic, n, driver):
    with open(output, "w") as f:
        # tc00
        if int(n) == 0:
            f.write(f'\n')
        else:
            f.write(f'{topic}\n')
            for k in range(int(n)):
                f.write(f'{driver[k].nricfin}, {driver[k].first_name.title()} {driver[k].middle_name[0].title()}. {driver[k].last_name.upper()}, {driver[k].age}, {driver[k].premium}\n')

def insurance_policies(input, output):
    # Read file
    file_exists = os.path.isfile(input)
    if file_exists:
        topic, n, driver = read_input(input)
    else:
        raise Exception('File %s not found' % input)

    # Write to file
    write_input(output, topic, n, driver)

if __name__ == '__main__':
    insurance_policies(input="input02.txt", output="output02.txt")
