import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1) as file1_read:
    file1 = file1_read.readlines()

with open(f2) as file2_read:
    file2 = file2_read.readlines()


def compare():
    if (len(file1) != len(file2)):
        print('NOT EQUAL: The files do not have the same number of lines.')
        #return
    for i in range(len(file1)):
        line1_f1 = file1[i]
        line1_f2 = file2[i]
        if line1_f1 != line1_f2:
            print('ERROR: NOT EQUAL')
            line1_f1 = '"' + ' '.join(line1_f1.split()) + '"'
            line1_f2 = '"' + ' '.join(line1_f2.split()) + '"'
            string_to_print = line1_f1 + ' != ' + line1_f2
            print(string_to_print)
            return
    print('ALL EQUAL')

if __name__ == '__main__':
    compare()
    
