import sys

if (sys.version_info >= (2,0) and sys.version_info < (3,0)):
    f1 = raw_input('Name the first file you want to compare.\n')
    f2 = raw_input('Name of second file.\n')
if (sys.version_info >= (3,0)):
    f1 = input('Name the first file you want to compare.\n')
    f2 = input('Name of second fileasdfasdf.\n')

 


file1_read = open(f1, 'r')
file2_read = open(f2, 'r')



file1 = file1_read.readlines()
file2 = file2_read.readlines()


def compare():
    if (len(file1) != len(file2)):
        print('NOT EQUAL: The files do not have the same number of lines.')
        return
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
    
