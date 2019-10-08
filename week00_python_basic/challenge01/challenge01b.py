import os

def read_input(input):
    with open(input, "r") as f1:
        n = f1.readline().rstrip()
        data = [line.rstrip('\n') for line in f1.readlines()]
    return n, data
def write_output(output, list, length):
    with open(output, 'w+') as f2:
        # tc04b
        if len(list) == 0:
            raise Exception('Claim-count is empty')
        else:
            try:
                list = [int(i) for i in list]
                is_max = []
                for i in range(length):
                    if list[i] == max(list):
                        is_max.append(1)
                    else:
                        is_max.append(0)
                # tc02
                for j in range(length):
                    f2.write(f'{is_max[j]}\n')
            # tc04a
            except:
                raise Exception('All claim-count must be valid')

def find_max_claim(input, output):
    # tc00
    if os.path.isfile(input):
        # Read file
        n, data = read_input(input)
    else:
        raise Exception(f'File {input} not found')

    # Write to output
    # tc03c
    if os.path.getsize(input) == 0:
        raise Exception('Invalid input: Empty file')
    # tc03b
    elif n == '':
        raise Exception('N must have a value')

    else:
        try:
            if int(n) != 0:
                write_output(output, data, int(n))
            # tc01
            else:
                with open(output, 'w') as f:
                    f.write('\n')
        # tc03a
        except ValueError:
            raise Exception('N must be an integer number')

if __name__ == '__main__':
    find_max_claim(input='input01b.txt', output='output01b.txt')
