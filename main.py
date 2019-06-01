def main():

    import os
    import time

    first_path = os.path.dirname(os.path.abspath(__file__))
    previous_directories_list = []
    previous_directories_list.append(first_path)
    t = 0
    l = 0

    while True:
        print('t is -- ' + str(t))
        template_path = os.path.dirname(os.path.abspath(__file__))
        print('\n ' * 100)
        print('_______________________________')
        print('[YOU AT ' + template_path + ']')
        current_directory = os.listdir()
        for i in range(len(current_directory)):
            print(str(i + 1) + ". " + current_directory[i])
        if t >= 1:
            selected_directory = input('Enter directory [name] to jump to it or:\nEnter <back> to return to previous directory \nEnter <remove> to remove file or folder \nEnter <refresh> to refresh directory \nEnter <create> to create file or folder > ')
            if selected_directory in ['back', 'Back']:
                if l == 0:
                    l = 1
                    plus_one = True
                else:
                    if l == 1:
                        t -= 1
                        plus_one = False
                os.chdir(previous_directories_list[t])
                reset_previous_directories_list1 = os.path.dirname(os.path.abspath(__file__))
                reset_previous_directories_list2 = str(previous_directories_list[0])
                if reset_previous_directories_list1 == reset_previous_directories_list2:
                    previous_directories_list = []
                    t = 0
                else:
                    True
            elif selected_directory in current_directory:
                previous_directory = template_path
                previous_directories_list.append(template_path)
                directory_exists = os.path.isdir(previous_directories_list[t])
                if directory_exists == True:
                    t += 1
                    os.chdir(selected_directory)
                else:
                    print('It\'s not a directory. Please, select directory')
                    time.sleep(2)
            elif selected_directory in ['Remove', 'remove']:
                deleting_file_or_directory = input('Select file or directory to remove > ')
                os.system('rm -rf ' + deleting_file_or_directory)
            elif selected_directory in ['Create', 'create']:
                creating_directory =        input('Enter file name > ')
                creating_directory_suffix = input('1).py\n2).txt\n3).html\n4).php\n5).markdown\n6).md\n7).css\n8).xml\n9)\n10)\n11)\nEnter file extension > ')
                file_name = creating_directory + creating_directory_suffix
                os.system('echo > ' + file_name)
            elif selected_directory in ['Refresh', 'refresh']:
                True
            else:
                print('Please, select folder or press [CTRL + C] to exit')
                time.sleep(2)
                True
        elif t == 0:
            selected_directory = input('Enter directory [name] to jump to it or:\nEnter <remove> to remove file or directory \nEnter <refresh> to refresh directory \nEnter <create> to create file or folder > ')
            if selected_directory in current_directory:
                previous_directory = template_path
                if previous_directories_list == []:
                    True
                else:
                    directory_exists = os.path.isdir(previous_directories_list[t])
                if directory_exists == True:
                    t += 1
                    if previous_directories_list == []:
                        True
                    else:
                        os.chdir(selected_directory)
                    previous_directories_list.append(template_path)
            elif selected_directory in ['Remove', 'remove']:
                deleting_file_or_directory = input('Select file or directory to remove > ')
                os.system('rm -rf ' + deleting_file_or_directory)
            elif selected_directory in ['Create', 'create']:
                creating_directory =        input('Enter file name > ')
                creating_directory_suffix = input('1).py\n2).txt\n3).html\n4).php\n5).markdown\n6).md\n7).css\n8).xml\n9)\n10)\n11)\nEnter file extension > ')
                file_name = creating_directory + creating_directory_suffix
                os.system('echo > ' + file_name)
            elif selected_directory in ['Refresh', 'refresh']:
                True
            else:
                print('Please, select folder or press [CTRL + C] to exit')
                time.sleep(2)
                True

main()
