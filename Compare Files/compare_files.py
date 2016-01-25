f1 = input('Name the first file you want to compare.\n')
f2 = input('Name of second file.\n')
file1_read = open(f1, 'r')
file2_read = open(f2, 'r')

file1 = file1_read.readlines()
file2 = file2_read.readlines()

error_list = []

def compare():
    for i in range(len(file1)):
        line1_f1 = file1[i]
        line1_f2 = file2[i]
        if line1_f1 != line1_f2:
            print('ERROR: NOT EQUAL')
            string_to_print = line1_f1 + '!=' + line1_f2
            print(string_to_print)
            error_list.append('Error')
            break
    if (len(error_list) == 0):
        print('ALL EQUAL')


if __name__ == '__main__':
    compare()
    
