import os

# List of file names to match against (convert to lowercase to ensure case-insensitive matching)
target_files = {file.lower() for file in {"passwords.txt", "password.txt", "pass.txt", 
                                          "all passwords.txt", "_allPasswords_list.txt", 
                                          "password list.txt"}}

# Directory to search
search_directory = "extracted/"

# Function to search files in all subdirectories
def find_matching_files(directory, target_set):
    PASSWORD_FILES_DIRS = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.lower() in target_set:
                PASSWORD_FILES_DIRS.append(os.path.join(root, file_name))
    return PASSWORD_FILES_DIRS

# Example usage
PASSWORD_FILES_DIRS = find_matching_files(search_directory, target_files)

import re
from itertools import zip_longest

# Define regex patterns to extract URL/Host, Username/Login, Password, and Application/Storage/Soft
url_pattern = re.compile(r"(URL|Host):\s*(.+)")
username_pattern = re.compile(r"(Username|Login):\s*(.+)")
password_pattern = re.compile(r"Password:\s*(.+)")
application_pattern = re.compile(r"(Application|Storage|Soft):\s*(.+)")

# Function to parse credentials from a single file
def parse_credentials_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Find all occurrences of each field using regex
    urls = url_pattern.findall(data)
    usernames = username_pattern.findall(data)
    passwords = password_pattern.findall(data)
    applications = application_pattern.findall(data)

    # Extract only the values (ignore the matched field names)
    urls = [url[1] for url in urls]  # Take the second element of the tuple (actual URL)
    usernames = [username[1] for username in usernames]
    passwords = [password for password in passwords]  # Password is already a single group
    applications = [application[1] for application in applications]

    # Use zip_longest to handle cases with missing fields, filling with None
    credentials = []
    for url, username, password, application in zip_longest(urls, usernames, passwords, applications, fillvalue=None):
        credentials.append({
            'URL': url,
            'Username': username,
            'Password': password,
            'Application': application
        })
    
    return credentials

# Function to process a list of file paths
def parse_credentials_from_file_paths(file_paths):
    all_credentials = []
    for file_path in file_paths:
        try:
            credentials = parse_credentials_from_file(file_path)
            all_credentials.extend(credentials)  # Add results to the overall list
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    
    return all_credentials

# Parse all files and get credentials
parsed_data = parse_credentials_from_file_paths(PASSWORD_FILES_DIRS)

from pymongo import MongoClient

# MongoDB Setup
client = MongoClient('mongodb://localhost:27017/')  # Update the connection string if using MongoDB Atlas or another setup
db = client['credentials_db']  # Create/use database
collection = db['credentials']  # Create/use collection

collection.create_index("URL")
collection.create_index("Username")

# Function to insert parsed data into MongoDB
def insert_into_mongodb(data):
    try:
        if data:
            result = collection.insert_many(data)  # Efficient bulk insert
            print(f"Inserted {len(result.inserted_ids)} documents into MongoDB")
        else:
            print("No data to insert")
    except Exception as e:
        print(f"Error inserting into MongoDB: {e}")
        
insert_into_mongodb(parsed_data)
