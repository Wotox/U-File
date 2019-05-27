def main():
    import os
    import inspect
    import time

    t = 0
    while True:
        template_path = os.path.dirname(os.path.abspath(__file__))
        print('\n ' * 100)
        print('_______________________________')
        print('[YOU AT ' + template_path + ']')
        print(t)
        current_directory = os.listdir()
        for i in range(len(current_directory)):
            print(str(i + 1) + ". " + current_directory[i])
        if t >= 1:
            selected_directory = input('Select directory [name] or enter <back> to return to previous directory > ')
            if selected_directory in ['back', 'Back']:
                os.chdir(previous_directory)
            elif selected_directory in current_directory:
                previous_directory = template_path
                os.chdir(selected_directory)
                t += 1
            else:
                print('Please, select folder or press [CTRL + C] to exit')
                time.sleep(2)
                True 
        elif t == 0:
            selected_directory = input('Select directory [name] > ')
            if selected_directory in current_directory:
                previous_directory = template_path
                t += 1
                os.chdir(selected_directory)
            else:
                print('Please, select folder or press [CTRL + C] to exit')
                time.sleep(2)
                True 
main()