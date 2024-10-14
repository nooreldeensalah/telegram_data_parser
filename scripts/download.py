import os
import asyncio
from tqdm import tqdm
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up your API ID, Hash, and Phone Number here
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

# Define the channel to download files from and the destination folder
CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME')
DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH')

# Create the download folder if it doesn't exist
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

# Function to download a single file with progress tracking
async def download_file(client, message):
    # Define the file path for the download
    file_path = os.path.join(DOWNLOAD_PATH, message.file.name)
    
    # Get the total size of the file for the progress bar
    total_size = message.file.size
    # Create a progress bar using tqdm
    with tqdm(total=total_size, desc=f"Downloading {message.file.name}", unit='B', unit_scale=True, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        # Create a callback function to update the progress bar
        async def progress_callback(current, total):
            pbar.n = current  # Set the current number of bytes downloaded
            pbar.refresh()  # Refresh the progress bar to display the new value

        # Download the media with the custom progress callback
        await client.download_media(message, file_path, progress_callback=progress_callback)
    
    print(f"Downloaded: {file_path}")

# Function to download all files concurrently
async def download_files_concurrently(client, messages):
    # Use asyncio.gather to download all files concurrently
    await asyncio.gather(*[download_file(client, message) for message in messages])

# Main function to connect to Telegram and download files from the channel
async def main():
    # Create the Telethon client
    client = TelegramClient('session_name', API_ID, API_HASH)

    # Connect to the Telegram API
    await client.start(PHONE_NUMBER)

    # Get the channel entity
    channel = await client.get_entity(CHANNEL_USERNAME)

    # Fetch messages containing media (documents, etc.) from the channel
    messages = await client.get_messages(channel, limit=50, filter=InputMessagesFilterDocument)

    # Download files concurrently
    await download_files_concurrently(client, messages)

    # Disconnect the client
    await client.disconnect()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
