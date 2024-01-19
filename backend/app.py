from PIL import UnidentifiedImageError
from fastapi import FastAPI, UploadFile, HTTPException

from load_image import load_image
from image_to_string import image_to_string

# router
from create_event import router as create_event_router
from parse_event_details import router as parse_event_details_router

app = FastAPI()
app.include_router(create_event_router)
app.include_router(parse_event_details_router)

@app.post('/image-to-text')
async def image_to_text(file: UploadFile):
    try:
        image = load_image(await file.read())
    except UnidentifiedImageError as e:
        return HTTPException(status_code=400, detail="unknown image format")
    return image_to_string(image)
