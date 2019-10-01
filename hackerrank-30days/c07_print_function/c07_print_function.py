#ref https://www.hackerrank.com/challenges/python-print/problem?h_r=next-challenge&h_v=zen
# Without using any string methods

import math
def print_number(n):
    i = 1
    j = 0
    while i <= n:
        m = int(1 + math.trunc((math.log10(i))))
        j = j * (10**m) + i
        i += 1
    return j

if __name__ == '__main__':
    n = 20
    print(print_number(n))

