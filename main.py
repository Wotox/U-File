def main():
    import os
    #import inspect
    import time
    previous_directories_list = []
    t = 0
    while True:
        template_path = os.path.dirname(os.path.abspath(__file__))
        print('\n ' * 5)
        print('_______________________________')
        print('[YOU AT ' + template_path + ']')
        current_directory = os.listdir()
        #for i in current_directory:
            # Split the extension from the path and normalise it to lowercase.
            #ext = os.path.splitext(fp)[-1].lower()
        for i in range(len(current_directory)):
            print(str(i + 1) + ". " + current_directory[i])
        if t >= 1:
            selected_directory = input('Enter directory [name] to jump to it or:\nEnter <back> to return to previous directory \nEnter <remove> to remove file or folder \nEnter <refresh> to refresh directory \nEnter <create> to create file or folder > ')
            if selected_directory in ['back', 'Back']:
                t -= 1
                print('t IN BACK IS ' + str(t))
                print(previous_directories_list)
                os.chdir(previous_directories_list[t-1])
                if str(current_directory) == str(previous_directories_list[0]):
                    print('GOT IT')
                    previous_directories_list = []
                else:
                    print('NOPE, WE HAVE' + str(template_path))
                    print('WE NEED ' + str(previous_directories_list[0]))
                """
                k = 0
                if k == 0:
                    k += 1
                    t -= 1
                    print('k IN BACK IS ' + str(k))
                    print('t IN BACK IS ' + str(t))
                    print(previous_directories_list)
                    os.chdir(previous_directories_list[t-1])
                    if str(current_directory) == str(previous_directories_list[0]):
                        print('GOT IT')
                        previous_directories_list = []
                    else:
                        print('NOPE, WE HAVE' + str(template_path))
                        print('WE NEED ' + str(previous_directories_list[0]))
                elif k > 0:
                    t -= 1
                    print('k IN BACK IS ' + str(k))
                    print('t IN BACK IS ' + str(t))
                    print(previous_directories_list)
                    os.chdir(previous_directories_list[t-1])
                    if str(current_directory) == str(previous_directories_list[0]):
                        print('GOT IT')
                        previous_directories_list = []
                    else:
                        print('NOPE, WE HAVE ' + str(template_path))
                        print('WE NEED' + str(previous_directories_list[0]))
                """
                #os.chdir(previous_directories_list[t-1])
            elif selected_directory in current_directory:
                previous_directory = template_path
                previous_directories_list.append(template_path)
                print('__________________________________________-')
                print('prev dir list -- ' + str(previous_directories_list))
                print('[t] is -- ' + str(t))
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
                previous_directories_list.append(template_path)
                print('____________________________________________________')
                print('prev dir list -- ' + str(previous_directories_list))
                directory_exists = os.path.isdir(previous_directories_list[t])
                if directory_exists == True:
                    t += 1
                    os.chdir(selected_directory)
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

#import time 
#import os
#directory_exists = os.path.exists()
#print(kek)
#time.sleep(2)

main()