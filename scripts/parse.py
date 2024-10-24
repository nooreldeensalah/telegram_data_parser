import os
import re
import logging
from itertools import zip_longest
from dotenv import load_dotenv
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of file names to match against
target_files = {file.lower() for file in {"passwords.txt", "password.txt", "pass.txt", 
                                          "all passwords.txt", "_allPasswords_list.txt", 
                                          "password list.txt"}}

# Directory to search
search_directory = os.getenv('EXTRACTION_PATH')

# Regex patterns compiled once for performance
url_pattern = re.compile(r"(URL|Host):\s*(.+)")
username_pattern = re.compile(r"(Username|Login):\s*(.+)")
password_pattern = re.compile(r"Password:\s*(.+)")
application_pattern = re.compile(r"(Application|Storage|Soft):\s*(.+)")

def find_matching_files(directory, target_set):
    """Search for files matching the target names in the directory."""
    return [
        os.path.join(root, file_name)
        for root, _, files in os.walk(directory)
        for file_name in files
        if file_name.lower() in target_set
    ]

def parse_credentials_from_file(file_path):
    """Parse credentials from a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
    except (FileNotFoundError, IOError) as e:
        logging.error(f"Error reading {file_path}: {e}")
        return []

    # Find all occurrences of each field using regex
    urls = [url[1] for url in url_pattern.findall(data)]
    usernames = [username[1] for username in username_pattern.findall(data)]
    passwords = [password[0] for password in password_pattern.findall(data)]
    applications = [application[1] for application in application_pattern.findall(data)]

    # Zip results together
    credentials = [
        {
            'url': url,
            'username': username,
            'password': password,
            'application': application
        }
        for url, username, password, application in zip_longest(urls, usernames, passwords, applications, fillvalue=None)
    ]
    
    return credentials

def insert_into_mongodb(data):
    """Insert parsed data into MongoDB."""
    if not data:
        logging.info("No data to insert")
        return

    try:
        MONGODB_URI = os.getenv('MONGODB_URI')
        client = MongoClient(MONGODB_URI)
        db = client['siaforce_db']
        collection = db['credentials']
        result = collection.insert_many(data)
        logging.info(f"Inserted {len(result.inserted_ids)} documents into MongoDB")
    except Exception as e:
        logging.error(f"Error inserting into MongoDB: {e}")

def parse_credentials_from_file_paths(file_paths):
    """Parse credentials from a list of file paths using concurrent processing."""
    all_credentials = []
    
    with ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(parse_credentials_from_file, file_path): file_path for file_path in file_paths}
        
        for future in as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                credentials = future.result()
                all_credentials.extend(credentials)
                logging.info(f"Parsed {len(credentials)} credentials from {file_path}")
            except Exception as e:
                logging.error(f"Error parsing {file_path}: {e}")
    
    return all_credentials

# Main execution
if __name__ == "__main__":
    PASSWORD_FILES_PATHS = find_matching_files(search_directory, target_files)
    parsed_data = parse_credentials_from_file_paths(PASSWORD_FILES_PATHS)
    insert_into_mongodb(parsed_data)
