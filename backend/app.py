from PIL import UnidentifiedImageError
from fastapi import FastAPI, UploadFile, HTTPException

from call_agent import call_agent
from load_image import load_image
from image_to_string import image_to_string
from parse_event_details import router as parse_event_details_router

app = FastAPI()
app.include_router(parse_event_details_router)

@app.post('/add_calender')
def add_calender(message: str):
    return call_agent(message)

@app.post('/image-to-text')
async def image_to_text(file: UploadFile):
    try:
        image = load_image(await file.read())
    except UnidentifiedImageError as e:
        return HTTPException(status_code=400, detail="unknown image format")
    return image_to_string(image)
