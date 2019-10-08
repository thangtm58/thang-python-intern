import os


def find_min(input, output):
    if os.path.isfile(input):
        # Read file
        with open(input, "r") as f1:
            data = [line.rstrip('\n') for line in f1.readlines()]
    # tc00 pass
    else:
        raise Exception(f'File {input} not found')

    # tc03c pass
    if os.path.getsize(input) == 0:
        raise Exception('Invalid input: Empty file')
    # tc03b pass
    elif all(s == '' or s.isspace() for s in data):
        raise Exception('Invalid input: Empty file with empty String')
    # tc02 pass
    elif len(data) != 6:
        raise Exception('Invalid input: List of numbers should have 6 numbers')

    else:
        try:
            data = [float(n.rstrip(', ')) for n in data]
            # Write to file
            f = open(output, 'w')
            f.write(f'{int(min(data))}') # tc01
            f.close()
        # tc03a
        except:
            raise Exception('Invalid input: The item in the list must be a number')

if __name__ == '__main__':
    find_min(input='input01.txt', output='output01.txt')
