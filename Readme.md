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

   pip install fastapi uvicorn motor pydantic python-dotenv requests mangum

   pip freeze > requirements.txt
   ```

## Setup of MongoDB Schema and Populating of Documents

2. Used Gen AI to generate 2 mock data for each collection: sprites, audio, scores

   ```bash
   manually inputted the mock data one by one into the 3 collections
   ```

## Configuring and Testing API with MongoDB

3. Running the API server

   ```bash
   uvicorn main:app --reload
   ```

4. Open browser to test using Swagger UI

   ```
   http://127.0.0.1:8000/docs
   ```

## Implemented POST Requests for Each Collection

- /upload_sprite -> Uploads sprite image file to MongoDB
- /upload_audio -> Uploads audio file to MongoDB
- /player_score -> Adds player name and score to the database

## Implemented GET Requests for Data Retrieval

- /player_scores -> Fetches all player names and scores
- /sprites -> Fetches filenames of uploaded sprites
- /audio -> Fetches filenames of uploaded audio files

## Whitelisting a port and added credentials

-whitelisted -> 0.0.0.0.0
-Credentials -> temporary credentials for a day made for testing

## Security Measures Against Injection Attacks

- Used Pydantic to enforce strict data types for incoming requests
- Manually validated and sanitized player names in /player_score endpoint
  - Blocked special characters like $, {, } and ;
  - Rejected malformed types such as object payloads instead of plain text

##Hosted on Render.com

- https://de-aidanfarrugia-ccd6-2a.onrender.com/docs#/
