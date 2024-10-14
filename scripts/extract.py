# TODO: Might want to make it more efficient or use process calls, just wanna start parsing the data for now 
import os
import zipfile
import rarfile
import patoolib
from getpass import getpass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the directory where the compressed files are stored
SOURCE_DIR = os.getenv('DOWNLOAD_PATH')
EXTRACT_DIR = os.getenv('EXTRACTION_PATH')

# Create the destination directory if it doesn't exist
if not os.path.exists(EXTRACT_DIR):
    os.makedirs(EXTRACT_DIR)

# Function to extract a ZIP file
def extract_zip(file_path, destination, password=None):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            if password:
                patoolib.extract_archive(archive=file_path, verbosity=1, interactive=1, outdir=EXTRACT_DIR+file_path.split('/')[-1][:-4], password=password)
            else:
                patoolib.extract_archive(archive=file_path, verbosity=1, interactive=1, outdir=EXTRACT_DIR+file_path.split('/')[-1][:-4])
            print(f"Extracted: {file_path}")
    except zipfile.BadZipFile:
        print(f"Error: {file_path} is not a valid ZIP file.")
    except RuntimeError as e:
        print(f"Error extracting {file_path}: {e}")

# Function to extract a RAR file
def extract_rar(file_path, destination, password=None):
    try:
        with rarfile.RarFile(file_path, 'r') as rar_ref:
            if password:
                patoolib.extract_archive(archive=file_path, verbosity=1, interactive=1, outdir=EXTRACT_DIR+file_path.split('/')[-1][:-4], password=password)
            else:
                patoolib.extract_archive(archive=file_path, verbosity=1, interactive=1, outdir=EXTRACT_DIR+file_path.split('/')[-1][:-4])
            print(f"Extracted: {file_path}")
    except rarfile.BadRarFile:
        print(f"Error: {file_path} is not a valid RAR file.")
    except rarfile.RarWrongPassword:
        print(f"Error: Wrong password for {file_path}.")
    except Exception as e:
        print(f"Error extracting {file_path}: {e}")

# Function to extract files in the directory
def extract_files_in_directory(source_dir, extract_dir):
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if file_name.endswith('.zip'):
            print(f"Extracting ZIP: {file_name}")
            password = None
            # Prompt for password if needed
            try:
                with zipfile.ZipFile(file_path, 'r') as z:
                    if z.testzip() is not None:
                        password = getpass(f"Enter password for {file_name}: ")
            except:
                pass
            extract_zip(file_path, extract_dir, password)
        
        elif file_name.endswith('.rar'):
            print(f"Extracting RAR: {file_name}")
            password = None
            # Prompt for password if needed
            try:
                with rarfile.RarFile(file_path, 'r') as rar:
                    if rar.needs_password():
                        password = getpass(f"Enter password for {file_name}: ")
            except:
                pass
            extract_rar(file_path, extract_dir, password)

if __name__ == "__main__":
    extract_files_in_directory(SOURCE_DIR, EXTRACT_DIR)
