import os


def directory_output(content):
    for i in range(len(content)):
        print(str(i + 1) + '. ' + content[i])


def previous_directory_returning(dirs_list):
    os.chdir(dirs_list[len(dirs_list) - 2])


def removing_directory_when_go_back(dirs_list, directory):
    for i in range(len(dirs_list)):
        if directory == dirs_list[i]:
            dirs_list.remove(dirs_list[i])
    return dirs_list


"""
def removing_repeated_directories_from_history(history):
    history_list = []
    for i in range(len(history)):
        history_list.append(history[i])
    for i in range(len(history)):
        for k in range(len(history_list)):
            if history[i] == history_list[k]:
                history_list.remove(history_list[k])
    return history_list
"""

def main():
    os.chdir('/')
    directories_history = []
    start_directory = os.getcwd()
    directories_history.append(start_directory)
    start_directory_content = os.listdir(start_directory)
    directory_output(start_directory_content)

    while True:
        print('directories history' + str(directories_history))
        user_action = input('Back or forward?[b/f]')
        if user_action == 'f':
            selecting_directory = input('Enter directory name to jump to it\n>>>')
            os.chdir(selecting_directory)
            current_directory = os.getcwd()
            directories_history.append(current_directory)
            current_directory_content = os.listdir(current_directory)
            directory_output(current_directory_content)
            print('current directory ' + str(current_directory))
        elif user_action == 'b':
            directories_history = removing_directory_when_go_back(directories_history, current_directory)
            previous_directory_returning(directories_history)
            current_directory = os.getcwd()
            current_directory_content = os.listdir(current_directory)
            directory_output(current_directory_content)


main()
