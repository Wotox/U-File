import os


def get_folder_elements(element, list):
    if os.path.isfile(os.path.abspath(element)) == False:
        if os.path.isfile(element):
            list.append(element)
    if os.path.isfile(element):
        element_path = os.path.abspath(element)
        list.append(element_path)
    elif os.path.isdir(element):
        list.append(element)
        folder = os.listdir(element)
        for i in range(len(folder)):
            temp_path = os.path.abspath(element)
            element_path = os.path.abspath(os.path.join(temp_path, folder[i]))
            if os.path.isfile(element_path):
                list.append(element_path)
            elif os.path.isdir(element_path):
                list.append(element_path)
                temp_path = os.path.join(element_path)
                get_folder_elements(temp_path, list)
    return list


def get_folder_size(folder):


    folder_size = os.path.getsize(folder)
    subfolders_list = get_folder_elements(folder, [])
    for i in range(len(subfolders_list)):
        folder_size += os.path.getsize(subfolders_list[i])

    if folder_size < 1024:
        folder_size = str(folder_size) + ' b'
    elif folder_size in range(1024, 1048576):
        folder_size = folder_size / 1024
        folder_size = float('%.2f' % folder_size)
        folder_size = str(folder_size) + ' kb'
    elif folder_size in range(1048576, 1073741824):
        folder_size = folder_size / 1024**2
        folder_size = float('%.2f' % folder_size)
        folder_size = str(folder_size) + ' mb'
    elif folder_size in range(1073741824, 1099511627776):
        folder_size = folder_size / 1024**3
        folder_size = float('%.2f' % folder_size)
        folder_size = str(folder_size) + ' gb'
    elif folder_size >= 1099511627776:
        folder_size = folder_size / 1024**4
        folder_size = float('%.2f' % folder_size)
        folder_size = str(folder_size) + ' tb'

    return folder_size
    folder_size = 0
    subfolders_list = []


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


    os.chdir('/home/yuri/Python')
    directories_history = []
    start_directory = os.getcwd()
    directories_history.append(start_directory)
    start_directory_content = os.listdir(start_directory)
    directory_output(start_directory_content)

    while True:

        user_action = input('Back or forward? [b/f]\n>>>')

        if user_action == 'f':
            selecting_directory = input('Enter directory name to jump to it\n>>>')
            if input('Request ' + selecting_directory + ' size? [y/n]\n>>>') == 'y':
                size = get_folder_size(selecting_directory)
                print(size)
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
