#ref https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    try:
        int(year)
        if year % 4 != 0:
            return False
        else:
            if year % 100 == 0 and year % 400 != 0:
                return False
            elif year % 400 == 0:
                return True
            else:
                return True
    except ValueError:
        print('It is not a year!!')
        return False