import os


def get_folder_elements(element, list):
    if os.path.isfile(element):
        element_path = os.path.abspath(element)
        list.append(element_path)
    elif os.path.isdir(element):
        folder = os.listdir(element)
        for i in range(len(folder)):
            element_path = os.path.abspath(os.path.join(os.path.abspath(element), folder[i]))
            if os.path.isfile(element_path):
                list.append(element_path)
            elif os.path.isdir(element_path):
                get_folder_elements(folder[i], list)
    return list


def directory_output(content):
    for i in range(len(content)):
        print(str(i + 1) + '. ' + content[i])


def previous_directory_returning(dirs_list):
    os.chdir(dirs_list[len(dirs_list) - 1])


def removing_directory_when_go_back(dirs_list, directory):
    for i in range(len(dirs_list)):
        if directory == dirs_list[i]:
            dirs_list.remove(dirs_list[i])
    return dirs_list


def main():

    folder_elements = []
    os.chdir('/home/yuri/Python')
    directories_history = []
    start_directory = os.getcwd()
    directories_history.append(start_directory)
    start_directory_content = os.listdir(start_directory)
    for i in range(len(start_directory_content)):
        folder_elements = get_folder_elements(start_directory_content[i], folder_elements)
    directory_output(start_directory_content)

    while True:

        user_action = input('Back or forward?[b/f]')

        if user_action == 'f':
            selecting_directory = input('Enter directory name to jump to it\n>>>')
            os.chdir(selecting_directory)
            current_directory = os.getcwd()
            directories_history.append(current_directory)
            current_directory_content = os.listdir(current_directory)
            directory_output(current_directory_content)
        elif user_action == 'b':
            directories_history = removing_directory_when_go_back(directories_history, current_directory)
            previous_directory_returning(directories_history)
            current_directory = os.getcwd()
            current_directory_content = os.listdir(current_directory)
            directory_output(current_directory_content)


if __name__ == '__main__':
    main()
