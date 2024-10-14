# Telegram Media Downloader

A suite of Python-based scripts that support downloading files from a specific telegram channel, decompressing archived files, and parsing the password files for credentials and inserting them to a MongoDB database.

The project also consists of a backend application written with `Django` and `Django Rest Framework` that provides an API for the parsed data, and a frontend `React` that displays the data in a dashboard page

The project leverages concurrency when applicable to improve performance
  
## Requirements

- Python 3.7 or higher
- Telegram API credentials (`API_ID`, `API_HASH`, and `PHONE_NUMBER`)
- MongoDB Instance

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
EXTRACTION_PATH = <extraction_path>
FEHU_LOGS_PASSWORD = <fehu_logs_password>

# Django backend
DJANGO_SECRET_KEY = <secret_key>
MONGODB_URI = <mongo_db_uri>

# React frontend
REACT_APP_API_URL=<react_app_uri>
```

## Usage

The scripts are intended to be run in this order:

- `download.py`: To download the archived files from a specific channel.
- `extract.py`: To decompress the compressed archives
- `parse.py`: To parse the extracted data for password credentials

Then eventually you can run the backend and frontend applications respectively.

### Creating an initial user

In the backend application, you can create an initial user that has the credentials `siaforce` and password `siaforce` that can be used for demo purposes.

```bash
# Apply migrations
python manage.py migrate
# Create initial user
python manage.py createinitialuser
```

And to run the frontend application, you can either use the development, or create a production build that can be served using a production tool

```bash
npm run dev # Development mode
npm run build # Generate production build
```
