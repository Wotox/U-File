def main():
    import os
    #import inspect
    import time

    t = 0
    while True:
        template_path = os.path.dirname(os.path.abspath(__file__))
        #print('\n ' * 100)
        print('_______________________________')
        print('[YOU AT ' + template_path + ']')
        current_directory = os.listdir()
        #for i in current_directory:
            # Split the extension from the path and normalise it to lowercase.
            #ext = os.path.splitext(fp)[-1].lower()
        for i in range(len(current_directory)):
            print(str(i + 1) + ". " + current_directory[i])
        if t >= 1:
            selected_directory = input('Select directory [name] or enter <back> to return to previous directory > ')
            if selected_directory in ['back', 'Back']:
                os.chdir(previous_directory)
            elif selected_directory in current_directory:
                previous_directory = template_path
                directory_exists = os.path.isdir(selected_directory)
                print(directory_exists)
                if directory_exists == True:
                    os.chdir(selected_directory)
                else:
                    print('It\'s not a directory. Please, select directory')
                    time.sleep(2)
            else:
                print('Please, select folder or press [CTRL + C] to exit')
                time.sleep(2)
                True 
        elif t == 0:
            selected_directory = input('Select directory [name] > ')
            if selected_directory in current_directory:
                previous_directory = template_path
                directory_exists = os.path.isdir(selected_directory)
                print(directory_exists)
                if directory_exists == True:
                    os.chdir(selected_directory)
                    t += 1
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