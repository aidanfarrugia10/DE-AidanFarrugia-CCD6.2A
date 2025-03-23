# Database Essentials Readme File - Aidan Farrugia CCD6.2A

## Project Structure

env Folder
.gitattributes
main.py
Readme.md
requirements.txt

## Environment Setup Instructions

1. Create Virtual Environment

   ```bash
   python -m venv env

   source env/bin/activate

   pip install fastapi uvicorn motor pydantic python-dotenv requests

   pip freeze > requirements.txt
   ```

## Setup of mongoDb Schema and populating of Documents

2. Used Gen Ai to generate 2 mock data for each collection sprites, audio, scores

   ```bash
   manualy inputed the mock data one by one for the 3 collections
   ```

## Configurating code in appendix to connect with my database and testing the code itself.

3. running the api server

   ```bash
   uvicorn main:app --reload

   opening browser tab to test
   http://127.0.0.1:8000/docs#/
   ```

## Adjusting of code and adding POST requests for each collection

    ```bash
    POST Function for the following:
    /player_scores - To post PlayerName and Score
    /sprites - To post Filename
    /audio - To post Filename
