from PIL import UnidentifiedImageError
from fastapi import FastAPI, UploadFile, HTTPException
from starlette.middleware.cors import CORSMiddleware

from load_image import load_image
from image_to_string import image_to_string

# router
from create_event import router as create_event_router
from parse_event_details import router as parse_event_details_router

app = FastAPI()
app.include_router(create_event_router)
app.include_router(parse_event_details_router)

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://app.localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/image-to-text')
async def image_to_text(file: UploadFile):
    try:
        image = load_image(await file.read())
    except UnidentifiedImageError as e:
        return HTTPException(status_code=400, detail="unknown image format")
    return image_to_string(image)
