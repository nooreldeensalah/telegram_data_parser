import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the directory where the compressed files are stored
SOURCE_DIR = os.getenv('DOWNLOAD_PATH')
EXTRACT_DIR = os.getenv('EXTRACTION_PATH')

os.makedirs(EXTRACT_DIR, exist_ok=True)

def extract_with_7z(file_path: str) -> None:
    """Extract files using 7z."""
    command = ['7z', 'x', file_path, f'-o{EXTRACT_DIR}']
        
    try:
        subprocess.run(command, check=True)
        print(f"Extracted: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting {file_path}: {e}")

def extract_files_in_directory(source_dir: str) -> None:
    """Extract all compressed archives in the specified directory."""
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        extract_with_7z(file_path)

if __name__ == "__main__":
    extract_files_in_directory(SOURCE_DIR)
