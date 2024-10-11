import os

# List of file names to match against (convert to lowercase to ensure case-insensitive matching)
target_files = {file.lower() for file in {"passwords.txt", "password.txt", "pass.txt", 
                                          "all passwords.txt", "_allPasswords_list.txt", 
                                          "password list.txt"}}

# Directory to search
search_directory = "extracted/"

# Function to search files in all subdirectories
def find_matching_files(directory, target_set):
    PASSWORD_FILES_DIRS = set()
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.lower() in target_set:
                PASSWORD_FILES_DIRS.add(os.path.join(root, file_name))
    return PASSWORD_FILES_DIRS

# Example usage
PASSWORD_FILES_DIRS = find_matching_files(search_directory, target_files)
