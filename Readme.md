# Database Essentials Readme File - Aidan Farrugia CCD6.2A

## Project Structure

env Folder
.gitattributes
main.py
Readme.md
requirements.txt

## ⚙️ Environment Setup Instructions

1. Create Virtual Environment

   ```bash
   python -m venv env

   source env/bin/activate

   pip install fastapi uvicorn motor pydantic python-dotenv requests

   pip freeze > requirements.txt
   ```
