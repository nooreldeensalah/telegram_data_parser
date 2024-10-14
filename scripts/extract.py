import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the directory where the compressed files are stored
SOURCE_DIR = os.getenv('DOWNLOAD_PATH')
EXTRACT_DIR = os.getenv('EXTRACTION_PATH')

os.makedirs(EXTRACT_DIR, exist_ok=True)

def extract_with_7z(file_path: str) -> None:
    """Extract files using 7z."""
    file_name = os.path.basename(file_path)
    command = ['7z', 'x', file_path, f'-o{EXTRACT_DIR}']

    if 'FEHU' in file_name:
        password = os.getenv('FEHU_LOGS_PASSWORD')
        command.extend(['-p' + password])
    
    print(f"Extracting {file_name}...")

    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Extracted: {file_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting {file_name}: {e}")

def extract_files_in_directory(source_dir: str, max_workers: int = 4) -> None:
    """Extract all compressed archives in the specified directory using parallel processing."""
    file_paths = [os.path.join(source_dir, file_name) for file_name in os.listdir(source_dir)]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(extract_with_7z, file_paths)

if __name__ == "__main__":
    extract_files_in_directory(SOURCE_DIR)
