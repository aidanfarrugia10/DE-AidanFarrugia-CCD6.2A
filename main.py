from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio
from typing import List

app = FastAPI()

# Connect to Mongo Atlas
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:mcast@cluster.rckut.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")
db = client["AssignmentDB"]

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    # In a real application, the file should be saved to a storage service
    content = await file.read()
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

@app.post("/player_score")
async def add_score(score: PlayerScore):
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}

@app.get("/player_scores")
async def get_player_scores():
    scoresDb = db.scores.find()
    scores = []
    async for score in scoresDb:
        scores.append({
            "player_name": score.get("player_name"),
            "score": score.get("score")
        })
    return scores

@app.get("/sprites")
async def get_sprites():
    spriteDb = db.sprites.find()
    sprites = []
    async for sprite in spriteDb:
        sprites.append({
            "filename": sprite.get("filename")
        })
    return sprites

@app.get("/audio")
async def get_audio():
    audioDb = db.audio.find()
    audio = []
    async for audioFile in audioDb:
        audio.append({
            "filename": audioFile.get("filename")
        })
    return audio


