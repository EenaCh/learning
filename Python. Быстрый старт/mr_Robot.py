import os
import psutil
import shutil
import sys
import random


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print('File', newfile, 'was successfully created')
            return True
        else:
            print('Having trouble copying')
            return False


def sys_info():
    print('That\'s what i know about the system:')
    print('  - number of processors:', psutil.cpu_count())
    print('  - platform: ', sys.platform)
    print('  - file system encoding: ', sys.getfilesystemencoding())
    print('  - Current directory:', os.getcwd())
    print('  - Current user: ', os.getlogin())


def del_dublicats(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0
    for i in file_list:
        fullname = os.path.join(dirname, i)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                doubl_count += 1
                print('File', fullname, 'was deleted successfully')
    return doubl_count


def duble_files(dirname):
    file_list = os.listdir(dirname)
    for i in file_list:
        fullname = os.path.join(dirname, i)
        duplicate_file(fullname)


def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print('File', fullname, 'was deleted random')


def main():
    print('Great Python Program!')
    print('Hello programmer')
    name = input('Your name: ')
    print(name + ', welcome to the world of python')
    answer = ''

    while answer != 'q':
        answer = input('Let\'s work? (Y/N/q)')

        if answer == 'Y':
            print('Fine, master!')
            print('I can:')
            print(' [1] - I will list the files')
            print(' [2] - I will display information about the system')
            print(' [3] - I will list the processes')
            print(' [4] - Duplicate files in the current directory')
            print(' [5] - Duplicate the specified file')
            print(' [6] - Remove duplicate files')
            print(' [7] - Delete random file')
            do = int(input('Enter action number: '))

            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()

            elif do == 3:
                print(psutil.pids())

            elif do == 4:
                print('=Duplication of current directory files=')
                duble_files('.')

            elif do == 5:
                print('=Duplication of the specified file=')
                filename = input('Enter the file name: ')
                duplicate_file(filename)

            elif do == 6:
                print('=Remove duplicates in the directory=')
                dirname = input('Enter the directory name: ')
                count = del_dublicats(dirname)
                print('-- Deleted files: ', count)

            elif do == 7:
                print('=Delete random file=')
                dirname = input('Enter the directory name: ')
                random_delete(dirname)

            else:
                pass

        elif answer == 'N"':
            print('Goodbye,', name)
        else:
            print('Famous answer')


if __name__ == '__main__':
    main()