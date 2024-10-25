# Telegram Media Downloader

A suite of Python-based scripts that support downloading files from a specific telegram channel, decompressing archived files, and parsing the password files for credentials and inserting them to a MongoDB database.

The project also consists of a backend application written with `Django` and `Django Rest Framework` that provides an API for the parsed data, and a frontend `React` that displays the data in a dashboard page

The project leverages concurrency when applicable to improve performance

## Requirements

- Python 3.7 or higher
- Telegram API credentials (`API_ID`, `API_HASH`, and `PHONE_NUMBER`)
- MongoDB Instance
- `7z`

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
API_ID=<telegram_api_id>
API_HASH=<telegram_api_hash>
PHONE_NUMBER=<telegram_phone_number>
CHANNEL_USERNAME=<channel_id>
DOWNLOAD_PATH=<download_path>
EXTRACTION_PATH=<extraction_path>
FEHU_LOGS_PASSWORD=<fehu_logs_password>

# Backend variables
DJANGO_SECRET_KEY=<secret_key>
MONGODB_URI=<mongo_db_uri>
```

## Usage

### Dependencies

- The extraction uses `7z`, I've picked `7z` because the performance of `rarfile` and `zipfile` was slow.
- Make sure to install `7z` on your system:

```bash
# To install 7z using Chocolatey
choco install 7zip
```

And to install `7z` on **Debian-based** systems:

```bash
sudo apt update
sudo apt install p7zip-full p7zip-rar
```

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
# Running the backend application
python manage.py runserver 0.0.0.0:8000
```

And to run the frontend application which uses `Vite`:

To run the application in development mode:

```bash
npm run dev
```

To create a servable production build:

```bash
npm run build
```

## Deployment with Docker

An easier and more straightforward to deploy the application would be with Docker, a docker-compose setup consisting of 4 services:

- `mongodb`: A service to deploy a MongoDB locally.
- `data-preparation`: A service to download the required archives, extract them, and parse them for the password credentials, and eventually insert them to MongoDB.
- `backend`: A service to deploy the Django API application.
- `frontend`: A service to deploy the React frontend application.

### Steps

- Add the `.env` file in the root directory.
- Run the following commands:

```bash
docker compose up
```

#### Attach a terminal to the `data-preparation` container

This will create the containers, but the `data-preparation` stage has to be completed, to do so, attach a terminal to the data preparation container and type the code received from the Telegram API, afterwards the files are decompressed and inserted to the database and the remaining containers will be started.

```bash
docker attach python-scripts-app
```

Afterwards, you can access the application at `http://localhost:3000`
