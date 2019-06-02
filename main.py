def main():

    import os
    import time
    from re import sub
    import actions

    def strings_substract(str1, str2, n=1):
        return sub(r'%s' % (str2), '', str1, n)

    first_path = os.path.dirname(os.path.abspath(__file__)) # inpecting path of current directory
    previous_directories_list = [] # creating empty list for storaging previous directories path
    previous_directories_list.append(first_path) # adding current directory to previous directories path
    t = 0 # creating counter that show how much times user jumped to directories forward
    l = 0 # counter that show how much times user entered "back"
    biggest_string_length = 0

    while True:
        template_path = os.path.dirname(os.path.abspath(__file__)) # inspectiong path of current directory
        print('\n ' * 100) # creating empty place in terminal
        print('_______________________________')
        print('[YOU AT ' + template_path + ']')
        current_directory = os.listdir() # inspecting elements in current directory and writing them into current_directory list
        for i in range(len(current_directory)): # i == counter. for counter in range of length of current directory
            file_size = os.stat(current_directory[i]) # variable keep os stats of every element in cycle
            file_size = file_size.st_size # program take only file size from the whole stats
            temp_length = len(current_directory[i])
            if temp_length > biggest_string_length:
                biggest_string_length = temp_length
            elif temp_length == biggest_string_length:
                biggest_string_length = temp_length
            elif temp_length < biggest_string_length:
                pass
            str_biggest_string_length = ' ' * biggest_string_length
            length_to_size = str_biggest_string_length + '    '
            var = ' ' * temp_length
            length_to_size_difference = strings_substract(length_to_size, var)
            print(str(i + 1) + ". " + current_directory[i] + length_to_size_difference + str(file_size >> 10) + ' KB') # print count of every element in current directory
        #print('length to size difference : |' + length_to_size_difference + '|')
        if t >= 1: # if user has jumped to directories before OR if he is not in root directory
            selected_directory = input('Enter directory [name] to jump to it or:\nEnter <back> to return to previous directory \nEnter <remove> to remove file or folder \nEnter <refresh> to refresh directory \nEnter <create> to create file or folder \nEnter <edit> to edit any file > ')
            if selected_directory in ['back', 'Back']: # if user want to return to previous directory
                if l == 0: # if user have not returned to previous directories before
                    l = 1 # user returned to previos directory before
                    plus_one = True # boolean show that user jumped back in a row
                else:
                    if l == 1: # if user have returned to previous directories before
                        t -= 1 # previous_directories_list index should decrease
                        plus_one = False
                os.chdir(previous_directories_list[t]) # change dir on directory from previous_directories_list
                reset_previous_directories_list1 = os.path.dirname(os.path.abspath(__file__)) # first variable keeps current path itself
                reset_previous_directories_list2 = str(previous_directories_list[0]) # second variable keeps root directory
                if reset_previous_directories_list1 == reset_previous_directories_list2: # if current path == root directory
                    previous_directories_list = [] # empty previous_directories_list
                    t = 0 # empty main counter
                else:
                    True
            elif selected_directory in current_directory: # if selected directory equal to any element in current directory
                previous_directory = template_path
                previous_directories_list.append(template_path) # add template path to previous directories list
                directory_exists = os.path.isdir(previous_directories_list[t]) # else check is dir exists
                if directory_exists == True:  # if dir exists
                    t += 1
                    os.chdir(selected_directory) # change directory to selected
                else:
                    print('It\'s not a directory. Please, select directory')
                    time.sleep(2)
            else:
                actions.actions(selected_directory)

        elif t == 0: # if user has not jumped to directories forward OR if user did "back" to root directory
            selected_directory = input('Enter directory [name] to jump to it or:\nEnter <remove> to remove file or directory \nEnter <refresh> to refresh directory \nEnter <create> to create file or folder  \nEnter <edit> to edit any file > ')
            if selected_directory in current_directory: # if selected directory equal to any element in current directory
                previous_directory = template_path
                if previous_directories_list == []: # if previous directories list is empty
                    True # pass
                else:
                    directory_exists = os.path.isdir(previous_directories_list[t]) # else check is dir exists
                if directory_exists == True: # if dir exists
                    t += 1
                    if previous_directories_list == []: # if previous directories list is empty
                        True # pass
                    else:
                        os.chdir(selected_directory) # change directory to selected
                    previous_directories_list.append(template_path) # add template path to previous directories list
            else:
                actions.actions(selected_directory)
            
main() # executing main function
