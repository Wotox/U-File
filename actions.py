def actions(selected_directory):

    import time
    import os

    if selected_directory in ['Remove', 'remove']: # offer user to remove any element in folder
        deleting_file_or_directory = input('Select file or directory to remove > ')
        os.system('rm -rf ' + deleting_file_or_directory) # UNIX command to remove element

    elif selected_directory in ['Create', 'create']: # offer user to create any element in folder
        creating_directory =        input('Enter file name > ')
        creating_directory_suffix = input('1).py\n2).txt\n3).html\n4).php\n5).markdown\n6).md\n7).css\n8).xml\n9)\n10)\n11)\nEnter file extension > ') # file extension
        file_name = creating_directory + creating_directory_suffix # whole name = file name + file extension
        os.system('echo > ' + file_name) # UNIX command that can be used to create file

    elif selected_directory in ['Refresh', 'refresh']: # offer user to refresh current directory. (can be used if there is new file added not from U-File)
        True # just passing this branch to run code above

    elif selected_directory in ['Edit', 'edit']:
        file_name = input('Enter file name that you want to edit > ')
        os.system('nano ' + file_name)

    else:
        print('Please, select folder or press [CTRL + C] to exit') # if user don't choose any option from offered
        time.sleep(2) # waiting 2 sec
        True # pass
