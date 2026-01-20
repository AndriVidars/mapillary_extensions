from fastapi import FastAPI
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
