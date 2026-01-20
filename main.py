import os
import logging
from fastapi import FastAPI, HTTPException

# Vercel Read-Only Filesystem Fix: Completely disable Mapillary's file-based logging
# 1. Mock os.makedirs to prevent errors when Mapillary attempts to create a 'logs' directory
original_makedirs = os.makedirs
def hooked_makedirs(name, mode=0o777, exist_ok=False):
    if "mapillary" in name:
        return
    return original_makedirs(name, mode, exist_ok)
os.makedirs = hooked_makedirs

# 2. Mock logging.FileHandler so Mapillary doesn't try to open any log files
class NullFileHandler(logging.NullHandler):
    def __init__(self, *args, **kwargs):
        super().__init__()
    def setFormatter(self, *args, **kwargs):
        pass
logging.FileHandler = NullFileHandler

import mapillary.interface as mly
import random

app = FastAPI()


@app.get("/random-image")
def get_random_image(token: str, lat:float, lng:float, radius:int = 500):
    """
    Get a random image from Mapillary within a given radius of a point
    """
    mly.set_access_token(token)
    try:
        data = mly.get_image_close_to(longitude=lng, latitude=lat, radius=radius)
        if not data:
            return None
        
        features = data.to_dict()['features']
        if not features:
            return None
            
        return {"id": random.choice(features)['properties']['id']}
    except Exception as e:
        print(f"Error fetching image: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
