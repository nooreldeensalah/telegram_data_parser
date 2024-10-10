# Telegram Media Downloader

A Python-based script that downloads documents from a specific Telegram channel using the [`Telethon`](https://docs.telethon.dev/en/stable/) library. The script supports concurrent downloads using `asyncio` and displays a progress bar using the `tqdm` library.
  
## Requirements

- Python 3.7 or higher
- Telegram API credentials (`API_ID`, `API_HASH`, and `PHONE_NUMBER`)

## Installation

### 1. Clone the repository

```bash
git clone <repository_link>
cd <repository_name>
```

### 2. Create a virtual environment

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux
source .venv/bin/activate
# On Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a .env file in the root directory of the project with the following content:

```.env
API_ID = <telegram_api_id>
API_HASH = <telegram_api_hash>
PHONE_NUMBER = <telegram_phone_number>
CHANNEL_USERNAME = <channel_id>
DOWNLOAD_PATH = <download_path>
```

## Usage

To run the script, simply run the following command

```bash
python app.py
```
