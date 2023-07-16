import os
import shutil


def move_file_to_specified_folder(file_name, file_extension, current_directory):
    # TODO: Add more extension and its folders, for now I only require this extensions
    extension_to_folder = {
        ".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".webp": "Images"
    }

    # If file_extension is not in map ignore it
    if file_extension not in extension_to_folder:
        return

    # Get the directory name to which it is to be moved
    new_directory_name = extension_to_folder.get(file_extension)
    new_directory_absolute_path = os.path.join(
        current_directory, new_directory_name)

    # Check if the directory already exits in the current directory
    is_directory_present = os.path.isdir(new_directory_absolute_path)
    if not is_directory_present:
        print("Creating directory: ", new_directory_absolute_path)
        os.makedirs(new_directory_absolute_path)

    # move the file to new location
    old_location = os.path.join(current_directory, file_name)
    new_location = os.path.join(new_directory_absolute_path, file_name)

    shutil.move(old_location, new_location)


def main():
    # Take absolute path of the directory
    directory = input("Enter the absolute path of Directory: ")

    # Check if the directory is present
    is_directory_present = os.path.isdir(directory)

    if not is_directory_present:
        print("Given Directory is not Present")
        return

    # Ask to be sure to move it
    is_sure = input("Type YES to start the process: ")

    if is_sure is not "YES":
        print("Cancelling the Process")
        return

    # Read the directory and find the names of files and folders
    for file_name in os.listdir(directory):
        root, file_extension = os.path.splitext(file_name)

        # Check if it is a directory, if yes ignore
        if not file_extension:
            continue

        move_file_to_specified_folder(file_name, file_extension, directory)

    # Display the done message
    print("\nMoving files Completed\n")


if __name__ == "__main__":
    main()
